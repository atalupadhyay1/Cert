"""Candidate orderings for the sequencing items.

Each key maps to (label, meaning) exactly like the technical option bank, so a
sequencing item can be authored as an ordinary single-answer item whose four
options are four candidate orders. Every label contains the arrow between
steps; build.py and validate.py both rely on that.
"""
SEQUENCES = {}


def s(key, label, meaning):
    if '→' not in label:
        raise ValueError(f'Sequence label needs an arrow: {key}')
    SEQUENCES[key] = (label, meaning)


# ---------------------------------------------------------------- GKE platform
s('seq_gke_ok',
  'Create the project and enable APIs → build a Shared VPC with private subnets → create a regional private cluster with Workload Identity Federation for GKE → deploy through Binary Authorization',
  'Network and identity exist before the cluster, and the admission policy is enforceable only once the cluster is running.')
s('seq_gke_b1',
  'Create a regional private cluster → build a Shared VPC with private subnets → enable APIs → deploy through Binary Authorization',
  'A private cluster needs the shared network first, and the APIs must be enabled before any resource is created.')
s('seq_gke_b2',
  'Deploy through Binary Authorization → create the cluster → build the Shared VPC → create the project',
  'Admission control cannot run before a cluster exists, and no resource can be created before its project.')
s('seq_gke_b3',
  'Build a Shared VPC → deploy through Binary Authorization → create the project → create the cluster',
  'The project precedes its network, and the deploy step belongs after the cluster rather than in the middle.')

# ---------------------------------------------------------------- Terraform delivery
s('seq_iac_ok',
  'Create a remote state bucket with versioning → define modules per environment → run a plan in CI and require review → apply through the pipeline with a scoped service account',
  'State is centralised before modules depend on it, plan review gates the apply, and the pipeline uses the least-privileged identity.')
s('seq_iac_b1',
  'Apply through the pipeline → create the remote state bucket → define modules → run a plan in CI',
  'Applying before state exists duplicates infrastructure, and a plan cannot gate an apply that already happened.')
s('seq_iac_b2',
  'Define modules → apply through the pipeline → run a plan in CI → create the remote state bucket',
  'State must be created before the first apply, and review must precede it as well.')
s('seq_iac_b3',
  'Run a plan in CI → apply through the pipeline → define modules → create the remote state bucket',
  'Nothing can be planned before the modules and the state bucket exist.')

# ---------------------------------------------------------------- migration
s('seq_migrate_ok',
  'Inventory the estate in Migration Center → group servers into dependency-based waves → validate a pilot wave in the target landing zone → cut over wave by wave and decommission the source',
  'Inventory precedes grouping, a pilot proves the landing zone, and decommissioning follows a completed cutover.')
s('seq_migrate_b1',
  'Group servers into waves → inventory the estate → cut over and decommission → validate a pilot wave',
  'Waves cannot be grouped before the inventory, and decommissioning before validation destroys the rollback path.')
s('seq_migrate_b2',
  'Cut over and decommission → validate a pilot wave → inventory the estate → group servers into waves',
  'Decommissioning first removes the evidence and the rollback option for every later step.')
s('seq_migrate_b3',
  'Validate a pilot wave → inventory the estate → group servers into waves → cut over and decommission',
  'A pilot cannot be chosen before the inventory and the wave grouping.')

# ---------------------------------------------------------------- disaster recovery
s('seq_dr_ok',
  'Set the RTO and RPO targets → choose the DR pattern that meets them → build and replicate the standby environment → fail over in a game day and record the result',
  'Targets drive the pattern, the pattern drives the build, and only a rehearsal proves the numbers.')
s('seq_dr_b1',
  'Fail over in a game day → set the RTO and RPO targets → choose the DR pattern → build the standby environment',
  'A failover drill with no targets or standby environment proves nothing.')
s('seq_dr_b2',
  'Choose the DR pattern → fail over in a game day → set the RTO and RPO targets → build the standby environment',
  'The pattern has no basis until the targets exist, and the drill cannot precede the build.')
s('seq_dr_b3',
  'Build and replicate the standby environment → choose the DR pattern → set the RTO and RPO targets → fail over in a game day',
  'Building before the targets and pattern are chosen risks an environment that cannot meet either.')

# ---------------------------------------------------------------- incident response
s('seq_incident_ok',
  'Detect the symptom through an alert → contain the impact and restore service → isolate the root cause from logs, traces, and metrics → apply the permanent fix and write the postmortem',
  'Service recovery comes before deep analysis, and the postmortem follows the fix.')
s('seq_incident_b1',
  'Write the postmortem → detect the symptom → isolate the root cause → restore service',
  'A postmortem cannot be written before the incident has happened and been resolved.')
s('seq_incident_b2',
  'Isolate the root cause → detect the symptom → write the postmortem → restore service',
  'Detection precedes analysis, and the postmortem follows restoration rather than preceding it.')
s('seq_incident_b3',
  'Restore service → detect the symptom → write the postmortem → isolate the root cause',
  'Service cannot be restored before the alert fires, and the root cause is isolated before the postmortem.')

# ---------------------------------------------------------------- perimeter hardening
s('seq_vpcsc_ok',
  'Inventory projects and data flows → enable the audit logs needed for the perimeter → create the service perimeter in dry-run mode → review violations and enforce the perimeter',
  'The inventory defines the boundary, dry run surfaces legitimate flows, and enforcement follows the review.')
s('seq_vpcsc_b1',
  'Enforce the perimeter → create the service perimeter in dry-run mode → inventory projects → enable audit logs',
  'Enforcing before a dry run breaks legitimate traffic that was never catalogued.')
s('seq_vpcsc_b2',
  'Create the service perimeter in dry-run mode → enforce the perimeter → enable audit logs → inventory projects',
  'Enforcement in the second step leaves no review window, and the inventory is the first step.')
s('seq_vpcsc_b3',
  'Enable audit logs → enforce the perimeter → inventory projects → review violations',
  'Reviewing after enforcement means the breakage has already happened.')

# ---------------------------------------------------------------- streaming pipeline
s('seq_stream_ok',
  'Create the Pub/Sub topic and subscription → design the Dataflow windowing and allowed lateness → deploy the streaming job with a dead-letter path → monitor watermark lag and backfill from the raw archive',
  'The source exists before the job, the window policy is chosen before deployment, and monitoring follows the running pipeline.')
s('seq_stream_b1',
  'Deploy the streaming job → create the Pub/Sub topic → design the windowing → monitor watermark lag',
  'A job cannot start without its topic, and the window policy belongs in the design, not after deployment.')
s('seq_stream_b2',
  'Monitor watermark lag → deploy the streaming job → create the topic → design the windowing',
  'There is nothing to monitor before the job runs, and the job needs a topic.')
s('seq_stream_b3',
  'Design the windowing → monitor watermark lag → create the Pub/Sub topic → deploy the job',
  'Monitoring before deployment observes nothing, and the topic is created before the job.')

# ---------------------------------------------------------------- CMEK rollout
s('seq_cmek_ok',
  'Create the key ring and keys in the target region → grant the service agent encrypt and decrypt on each key → enable CMEK on the resource → verify an audit log entry shows the key used',
  'Keys and grants precede the resource change, and the audit entry proves the binding took effect.')
s('seq_cmek_b1',
  'Enable CMEK on the resource → create the key ring → grant the service agent → verify the audit log',
  'Enabling CMEK before the key exists and the grant is in place fails the resource operation.')
s('seq_cmek_b2',
  'Verify the audit log → enable CMEK → create the key ring → grant the service agent',
  'Verification cannot precede the change it verifies.')
s('seq_cmek_b3',
  'Grant the service agent → enable CMEK → create the key ring → verify the audit log',
  'The grant needs a key, and the key must exist in the target region before the resource is encrypted.')

# ---------------------------------------------------------------- release
s('seq_release_ok',
  'Build an immutable image and record its digest → deploy the new revision without traffic → shift a small traffic percentage and watch error and latency signals → promote to full traffic or roll back to the pinned digest',
  'The artifact is fixed before traffic moves, and the decision to promote follows observed signals.')
s('seq_release_b1',
  'Shift full traffic to the new revision → build the image → watch the error rate → promote or roll back',
  'Full traffic before any canary step turns the first failure into an outage.')
s('seq_release_b2',
  'Watch the error rate → deploy the new revision → shift traffic → build the image',
  'Nothing can be watched before the revision exists, and the image precedes the deployment.')
s('seq_release_b3',
  'Deploy the new revision → promote to full traffic → shift a small percentage → build the image',
  'Promoting before the canary step skips the signal that justifies promotion.')

# ---------------------------------------------------------------- BigQuery tuning
s('seq_bq_ok',
  'Inspect the query plan and bytes processed → partition and cluster the table on the filter columns → rewrite the query to prune partitions → measure the new slot time and bytes scanned',
  'The plan identifies the problem, the physical design supports pruning, and only a measurement proves improvement.')
s('seq_bq_b1',
  'Measure slot time → rewrite the query → inspect the plan → partition the table',
  'Partitioning last ignores what the plan and the rewrite revealed.')
s('seq_bq_b2',
  'Partition and cluster the table → measure slot time → inspect the plan → rewrite the query',
  'Measuring before any change establishes no baseline against the plan.')
s('seq_bq_b3',
  'Rewrite the query → partition the table → measure slot time → inspect the plan',
  'The plan is the evidence that drives both the rewrite and the physical design.')

# ---------------------------------------------------------------- ML deployment
s('seq_ml_ok',
  'Curate and version the training data → train and evaluate the model in a pipeline → register the model and record its metrics → deploy to an endpoint with traffic splitting and model monitoring',
  'Data precedes training, the registry holds the evaluated artifact, and monitoring starts with the serving endpoint.')
s('seq_ml_b1',
  'Deploy to an endpoint → train the model → register the model → curate the training data',
  'Serving an untrained, unregistered model has nothing to deploy.')
s('seq_ml_b2',
  'Register the model → curate the training data → deploy to an endpoint → train the model',
  'Registration follows training, and training follows the data.')
s('seq_ml_b3',
  'Train the model → deploy to an endpoint → curate the training data → register the model',
  'Training without curated data and deploying without registration both skip a required stage.')

# ---------------------------------------------------------------- audit evidence
s('seq_audit_ok',
  'Enable data access audit logs for the services in scope → create a locked log bucket with the required retention → route the logs with an aggregated sink → query and export the evidence for the auditor',
  'Logs must be enabled before they can be routed, and retention is fixed on the bucket before the sink writes to it.')
s('seq_audit_b1',
  'Create a locked log bucket → enable data access audit logs → query the evidence → route the logs with a sink',
  'A sink that is created last is needed before any evidence can be queried from the destination.')
s('seq_audit_b2',
  'Query the evidence → create a locked log bucket → enable audit logs → route the logs',
  'There is no evidence to query before logging and routing exist.')
s('seq_audit_b3',
  'Route the logs with a sink → query the evidence → enable audit logs → create a locked bucket',
  'A sink without a destination bucket or enabled logs captures nothing.')
