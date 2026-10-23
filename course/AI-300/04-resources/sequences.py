"""Candidate orderings for the AI-300 sequencing items.

Each sequencing item offers four candidate orders; exactly one is correct.
They are exported as `multiple-choice` because Udemy's bulk importer accepts
only multiple-choice and multi-select, and every option here is a complete
candidate sequence.
"""

SEQUENCES = {}


def s(key, label, meaning):
    if key in SEQUENCES:
        raise ValueError(f'Duplicate sequence: {key}')
    SEQUENCES[key] = (label, meaning)


# --- Promotion, deployment, and rollback ---------------------------------
s('seq_promote_ok',
  'Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold',
  'Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic.')
s('seq_promote_b1',
  'Register the model version → train the candidate → evaluate against the gate → shift all traffic',
  'Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version.')
s('seq_promote_b2',
  'Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate',
  'A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic.')
s('seq_promote_b3',
  'Evaluate against the gate → train the candidate → shift all traffic → register the model version',
  'There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target.')

s('seq_iac_ok',
  'Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace',
  'Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it.')
s('seq_iac_b1',
  'Run a smoke job against the workspace → deploy the module → authenticate the pipeline → define the workspace in Bicep',
  'A job cannot run against infrastructure that has neither been defined nor deployed, and the pipeline has no identity yet.')
s('seq_iac_b2',
  'Authenticate the pipeline → run a smoke job → define the workspace in Bicep → deploy the module',
  'Identity is established early, but the smoke job still precedes both the definition and the deployment.')
s('seq_iac_b3',
  'Deploy the module → define the workspace in Bicep → run a smoke job → authenticate the pipeline',
  'The module is deployed before it is written, and authentication last means the pipeline could never have deployed anything.')

s('seq_rollback_ok',
  'Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress',
  'A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change.')
s('seq_rollback_b1',
  'Replace the incumbent deployment → compare error rate and latency → deploy the new version to a second deployment → send traffic to it',
  'Replacing the incumbent destroys the comparison baseline and the thing you would roll back to.')
s('seq_rollback_b2',
  'Compare error rate and latency → deploy the new version → send a small traffic share → replace the incumbent',
  'There is nothing to compare before the candidate exists and is receiving traffic.')
s('seq_rollback_b3',
  'Send all traffic to the new deployment → deploy the new version → compare metrics → move traffic back',
  'All traffic is shifted before the candidate is deployed, and the comparison comes after the exposure it was meant to prevent.')

s('seq_readiness_ok',
  'Review the infrastructure change in a pull request → run the build and test workflow → deploy to staging and run the smoke test → require environment approval and deploy to production',
  'Review precedes execution, tests precede staging, and staging evidence precedes the approval that releases production.')
s('seq_readiness_b1',
  'Require environment approval and deploy to production → run the build and test workflow → review the change → deploy to staging',
  'Production is released before the change is reviewed or tested, which inverts every gate.')
s('seq_readiness_b2',
  'Run the build and test workflow → review the change → require approval → deploy to staging',
  'Tests are run before the change is reviewed, and staging evidence arrives after the production approval.')
s('seq_readiness_b3',
  'Deploy to staging → require environment approval → review the change → run the build and test workflow',
  'The approval is requested before the review and before any automated test has run.')

# --- Diagnosis and incident response --------------------------------------
s('seq_diag_ok',
  'Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set',
  'The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test.')
s('seq_diag_b1',
  'Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set',
  'Retraining before the failing stage is identified changes a component that may not be at fault.')
s('seq_diag_b2',
  'Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span',
  'The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context.')
s('seq_diag_b3',
  'Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set',
  'The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis.')

s('seq_drift_ok',
  'Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate',
  'Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom.')
s('seq_drift_b1',
  'Retrain on refreshed data → detect the drop → compare distributions → promote through the gate',
  'Retraining before the drop is detected and attributed risks training on data that has the same defect.')
s('seq_drift_b2',
  'Compare distributions → identify the upstream source → detect the drop → retrain on refreshed data',
  'A distribution comparison needs a detected drop to compare against, so the trigger is out of order.')
s('seq_drift_b3',
  'Identify the upstream source → retrain → detect the drop → compare distributions',
  'The source is named before any evidence exists, and detection comes last.')

s('seq_capacity_ok',
  'Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration',
  'Measurement and forecasting come before the commercial comparison, and the load test validates the decision.')
s('seq_capacity_b1',
  'Reserve provisioned throughput → measure the request rate → forecast the load → load test the configuration',
  'Capacity is committed before the demand that justifies it has been measured.')
s('seq_capacity_b2',
  'Forecast the peak load → reserve provisioned throughput → measure the current rate → load test',
  'The forecast is made without a measurement baseline, and the commitment precedes the measurement entirely.')
s('seq_capacity_b3',
  'Load test the configuration → reserve provisioned throughput → forecast the load → measure the request rate',
  'A load test needs a configuration chosen from the measurement and forecast, both of which come later.')

s('seq_retire_ok',
  'Find every application and flow that references the version → move callers to the successor deployment → confirm no traffic reaches the old version → delete the version and its endpoint',
  'Dependents are found before anything moves, traffic reaches zero before deletion, and deletion is the last and irreversible step.')
s('seq_retire_b1',
  'Delete the version and its endpoint → find the callers → move callers to the successor → confirm no traffic',
  'Deleting first breaks the callers that the remaining steps were meant to find and migrate.')
s('seq_retire_b2',
  'Move callers to the successor deployment → delete the version → find the callers → confirm no traffic',
  'Callers are moved before they are identified, and deletion happens before traffic is confirmed to be zero.')
s('seq_retire_b3',
  'Confirm no traffic reaches the old version → delete the version → find the callers → move callers',
  'No traffic can be confirmed while unknown callers still exist, and deletion precedes the migration.')

# --- RAG and evaluation ---------------------------------------------------
s('seq_rag_ok',
  'Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness',
  'Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow.')
s('seq_rag_b1',
  'Bind the index to the flow → create the search index → curate the documents → chunk and embed them',
  'The flow is bound to an index that does not exist yet, and evaluation never happens at all.')
s('seq_rag_b2',
  'Create the search index → curate the source documents → evaluate retrieval → chunk and embed them',
  'The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve.')
s('seq_rag_b3',
  'Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents',
  'Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query.')

s('seq_refresh_ok',
  'Update the source content → re-chunk and re-embed the changed documents → refresh the index → re-run the evaluation set',
  'The refresh follows the content change, and the evaluation is what confirms retrieval still finds the current material.')
s('seq_refresh_b1',
  'Re-run the evaluation set → refresh the index → update the source content → re-chunk the documents',
  'Evaluation runs before the content has changed, so it validates the state being replaced.')
s('seq_refresh_b2',
  'Refresh the index → update the source content → re-run the evaluation → re-chunk the documents',
  'The index is refreshed before the source is updated and before the new chunks exist.')
s('seq_refresh_b3',
  'Re-chunk the documents → update the source content → refresh the index → re-run the evaluation',
  'Re-chunking precedes the source update, so the chunks encode content that is about to be replaced.')

s('seq_eval_ok',
  'Collect real queries from logs → grade representative answers against a rubric → build the evaluation harness → calibrate the judge against the human grades',
  'Real traffic supplies the cases, the rubric supplies the standard, and calibration is what makes an automated judge trustworthy.')
s('seq_eval_b1',
  'Build the evaluation harness → collect real queries → calibrate the judge → grade representative answers',
  'The harness has no cases and the judge is calibrated before any human grade exists to calibrate against.')
s('seq_eval_b2',
  'Calibrate the judge → build the evaluation harness → collect real queries → grade answers',
  'Calibration needs both the harness and the human grades, neither of which exists yet.')
s('seq_eval_b3',
  'Grade representative answers → calibrate the judge → collect real queries → build the harness',
  'Answers are graded before the queries that produced them have been collected.')

s('seq_release_prompt_ok',
  'Edit the prompt file in a branch → run the offline evaluation gate → review the diff and metric change in a pull request → deploy the approved version and watch the online metrics',
  'The change is measured before review, review happens before deployment, and online metrics confirm the offline result.')
s('seq_release_prompt_b1',
  'Deploy the approved version → edit the prompt in a branch → run the evaluation gate → review the diff',
  'A version is deployed before it has been edited, evaluated, or reviewed.')
s('seq_release_prompt_b2',
  'Review the diff and metric change → edit the prompt in a branch → deploy the version → run the evaluation gate',
  'The diff cannot be reviewed before the edit, and deployment precedes the gate that would block it.')
s('seq_release_prompt_b3',
  'Run the offline evaluation gate → deploy the version → review the diff → edit the prompt',
  'The gate runs before the prompt is edited, so it measures the old wording and clears the way for an unreviewed deploy.')

s('seq_safety_ok',
  'Assemble jailbreak and injection cases → configure the content filter and system prompt → run the adversarial evaluation → monitor the filtered and blocked rates in production',
  'The attack set defines what is being tested, the control is configured, the test proves it, and monitoring keeps it honest afterwards.')
s('seq_safety_b1',
  'Monitor the blocked rates in production → assemble the cases → configure the filter → run the evaluation',
  'Production monitoring comes before the control it is meant to watch has even been configured.')
s('seq_safety_b2',
  'Configure the content filter → run the adversarial evaluation → assemble the cases → monitor the rates',
  'The evaluation runs before the adversarial cases exist, so it has nothing to test against.')
s('seq_safety_b3',
  'Run the adversarial evaluation → configure the content filter → assemble the cases → monitor the rates',
  'The filter is configured after the evaluation that was supposed to validate it.')

s('seq_cost_ok',
  'Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held',
  'Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe.')
s('seq_cost_b1',
  'Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver',
  'An optimization is applied before anything has been measured or attributed.')
s('seq_cost_b2',
  'Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver',
  'Evaluation precedes both the change it would validate and the measurement that motivates it.')
s('seq_cost_b3',
  'Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization',
  'A driver is named before measurement, and the evaluation runs before the change exists.')

s('seq_incident_ok',
  'Confirm the impact and scope from telemetry → contain the incident by shifting traffic or disabling the feature → fix the identified cause → add a regression case and update the gate',
  'Containment protects users before the root cause is chased, and the gate change stops the same defect returning.')
s('seq_incident_b1',
  'Fix the identified cause → confirm the impact → contain the incident → add a regression case',
  'The cause is fixed before impact is confirmed, and containment arrives after the fix it was meant to buy time for.')
s('seq_incident_b2',
  'Add a regression case → contain the incident → confirm the impact → fix the cause',
  'A regression case is added before the defect is understood, and containment precedes impact assessment.')
s('seq_incident_b3',
  'Contain the incident → add a regression case → fix the cause → confirm the impact',
  'The scope of impact is confirmed last, so nobody knows what was affected while the fix was being written.')

s('seq_env_ok',
  'Publish the component to the registry → build a versioned environment that pins its dependencies → reference both from the pipeline YAML → run the pipeline in the test environment',
  'The reusable assets must exist and be versioned before a pipeline can reference them, and the run comes last.')
s('seq_env_b1',
  'Run the pipeline in the test environment → reference both from the pipeline YAML → publish the component → build the environment',
  'The pipeline runs before its references exist, and the assets are published afterwards.')
s('seq_env_b2',
  'Build the environment → run the pipeline → publish the component → reference it in the YAML',
  'The run precedes both the component publication and the YAML reference that would make it resolvable.')
s('seq_env_b3',
  'Reference both from the pipeline YAML → build the environment → publish the component → run the pipeline',
  'The YAML references assets that have not been published or built yet.')

s('seq_model_onboard_ok',
  'Review the model card and licensing → evaluate it on the task dataset → deploy it to a staging endpoint → canary a share of production traffic',
  'Capability and licence are checked before spend, quality is measured before staging, and staging precedes production.')
s('seq_model_onboard_b1',
  'Canary a share of production traffic → evaluate the model → review the model card → deploy to staging',
  'Production traffic reaches a model whose capability, licence, and quality are all still unchecked.')
s('seq_model_onboard_b2',
  'Evaluate the model on the task dataset → review the model card → canary production traffic → deploy to staging',
  'Production traffic is served before the staging deployment that would have measured it.')
s('seq_model_onboard_b3',
  'Deploy it to a staging endpoint → review the model card → canary production traffic → evaluate the model',
  'Evaluation comes last, so the canary measures a model that was never assessed on the task dataset.')

s('seq_access_ok',
  'Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content',
  'The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds.')
s('seq_access_b1',
  'Grant the identity Owner on each source → inventory the data sources → verify the answer → assign a managed identity',
  'A broad grant is made before the sources are known, and the identity is assigned after it has been granted permissions.')
s('seq_access_b2',
  'Verify a grounded answer → assign the identity → grant the role → inventory the sources',
  'Verification precedes the configuration it verifies, and the inventory comes last.')
s('seq_access_b3',
  'Assign the identity → verify the answer → inventory the sources → grant the role',
  'The answer is verified before any role has been granted, and the sources are inventoried after the grant.')

s('seq_batch_ok',
  'Confirm the workload is not interactive → prepare a batch input dataset → submit the batch endpoint job → validate the output file against the schema',
  'The interaction requirement decides the pattern, the input must exist before submission, and the output is validated afterwards.')
s('seq_batch_b1',
  'Submit the batch endpoint job → prepare the input dataset → validate the output → confirm the workload is not interactive',
  'A batch job is submitted before its input exists and before anyone confirmed batch is the right pattern.')
s('seq_batch_b2',
  'Validate the output file → submit the job → prepare the input → confirm the workload',
  'The output is validated before the job that produces it has run.')
s('seq_batch_b3',
  'Prepare the input dataset → confirm the workload is not interactive → validate the output → submit the job',
  'Validation happens before submission, so there is no output to check.')

s('seq_govern_ok',
  'Register the model with provenance tags → record the evaluation results on the version → require approval before the alias moves → archive the superseded version with its metrics',
  'Provenance and evidence are attached to the artifact, the move is gated, and history is retained rather than overwritten.')
s('seq_govern_b1',
  'Move the alias to production → register the model → record the evaluation results → archive the old version',
  'Production moves before the model exists as a registered artifact with evidence attached.')
s('seq_govern_b2',
  'Archive the superseded version → require approval → register the model → record the results',
  'The previous version is archived before its replacement has been registered or evidenced.')
s('seq_govern_b3',
  'Record the evaluation results → archive the version → register the model → move the alias',
  'Results are recorded for a model that is not registered yet, and the version is archived before promotion.')
