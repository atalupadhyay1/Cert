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


# ---------------------------------------------------------------- domain 1
s('seq_ws_ok',
  'Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles',
  'The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does.')
s('seq_ws_b1',
  'Create the workspace → choose the region after the first item is built → assign the domain → grant the roles',
  'The region cannot be changed after creation, so choosing it later is not possible.')
s('seq_ws_b2',
  'Grant the workspace roles → create the workspace → choose the capacity → assign the domain',
  'Roles cannot be granted before the workspace exists, and the capacity is chosen before, not after.')
s('seq_ws_b3',
  'Assign the domain → grant the roles → create the workspace → choose the capacity',
  'A domain assignment and a role grant both need the workspace, and the capacity is not a last step.')

s('seq_alm_ok',
  'Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages',
  'The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion.')
s('seq_alm_b1',
  'Create the deployment pipeline → connect the workspace to Git → promote through the stages → add deployment rules → commit the definitions',
  'Promoting before the definitions are committed and before the rules exist overwrites the target with the wrong settings.')
s('seq_alm_b2',
  'Commit the item definitions → connect the workspace to Git → add deployment rules → create the pipeline → promote the stages',
  'There is nothing to commit before the repository is connected, and the rules belong to a pipeline that does not exist yet.')
s('seq_alm_b3',
  'Promote through the stages → create the deployment pipeline → commit the definitions → connect Git → add deployment rules',
  'Every step is in the wrong order: a promotion needs the pipeline, the pipeline needs the definitions in Git, and the rules come first.')

s('seq_sec_ok',
  'Classify the data → apply the sensitivity label → grant the workspace role → add row-level security → test as each persona',
  'The classification drives the label, the role grants the access, and the row filter is proven against each persona after both are in place.')
s('seq_sec_b1',
  'Grant the workspace role → classify the data → test as each persona → apply the label → add row-level security',
  'Testing before the row filter exists proves nothing, and the label follows the classification rather than preceding it.')
s('seq_sec_b2',
  'Add row-level security → grant the workspace role → classify the data → apply the label → test as each persona',
  'A row filter written before the access model exists is written against the wrong identities.')
s('seq_sec_b3',
  'Test as each persona → add row-level security → apply the label → classify the data → grant the role',
  'The persona test is the last step, and a label applied before the data is classified is a guess.')

s('seq_orch_ok',
  'Decide which work is copy, which is orchestration, and which needs PySpark → build the pipeline → add the notebook activity → parameterise the run',
  'The work split decides the items, and the parameter is added once the pipeline has a step to parameterise.')
s('seq_orch_b1',
  'Build the pipeline → decide the work split → parameterise the run → add the notebook activity',
  'Building before the split produces the wrong items, and a parameter without the notebook has nothing to drive.')
s('seq_orch_b2',
  'Parameterise the run → add the notebook activity → build the pipeline → decide the work split',
  'There is no run to parameterise and no pipeline to hold the activity before either exists.')
s('seq_orch_b3',
  'Add the notebook activity → parameterise the run → decide the work split → build the pipeline',
  'The activity needs the pipeline, and the split is the decision that tells you which activities to add.')

s('seq_gov_ok',
  'Confirm the source of truth → apply the label → endorse the item → verify the audit entry',
  'Endorsement claims authority, so the authority is confirmed first, and the audit entry is the proof that the governance action was recorded.')
s('seq_gov_b1',
  'Endorse the item → apply the label → confirm the source of truth → verify the audit entry',
  'Endorsing before confirming the source of truth endorses whatever happened to be there.')
s('seq_gov_b2',
  'Verify the audit entry → endorse the item → confirm the source of truth → apply the label',
  'The audit entry records actions that have already happened, so it cannot come first.')
s('seq_gov_b3',
  'Apply the label → verify the audit entry → endorse the item → confirm the source of truth',
  'The label follows the classification, and the audit entry follows the actions it records.')

# ---------------------------------------------------------------- domain 2
s('seq_load_ok',
  'Read the watermark → extract only the rows after it → merge into the target → update the watermark',
  'The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds.')
s('seq_load_b1',
  'Extract the full table → merge into the target → read the watermark → update the watermark',
  'A full extract ignores the watermark, so reading it afterwards adds nothing and the target reloads the history.')
s('seq_load_b2',
  'Update the watermark → extract the rows → read the watermark → merge into the target',
  'Advancing the watermark before the merge loses every row the failed merge did not write.')
s('seq_load_b3',
  'Merge into the target → read the watermark → update the watermark → extract the rows',
  'Nothing has been extracted, so there is nothing to merge, and the watermark moves before the data does.')

s('seq_medallion_ok',
  'Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table',
  'Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published.')
s('seq_medallion_b1',
  'Conform and deduplicate → land the raw files → publish the gold table → validate the schema',
  'Conforming before the raw data lands transforms whatever was already there, and validation after publication is too late.')
s('seq_medallion_b2',
  'Publish the gold table → validate the schema → land the raw files → conform and deduplicate',
  'The published table would be rebuilt from data that has not landed yet.')
s('seq_medallion_b3',
  'Validate the schema → publish the gold table → land the raw files → conform and deduplicate',
  'There is nothing to validate and nothing to publish before the raw files exist.')

s('seq_stream_ok',
  'Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate',
  'The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate.')
s('seq_stream_b1',
  'Alert on the aggregate → build the materialized view → define the source → add the destination → create the KQL table',
  'The alert has nothing to read until the view, the table, and the stream exist.')
s('seq_stream_b2',
  'Create the KQL table → define the source → alert on the aggregate → add the destination → build the view',
  'The alert fires before the destination and the view that produce the aggregate.')
s('seq_stream_b3',
  'Add the destination → create the KQL table → build the view → define the source → alert on the aggregate',
  'A destination with no source receives nothing, and the source is the first decision.')

s('seq_shortcut_ok',
  'Create the shortcut to the external container → grant the delegated permission on the target → validate the schema → query through the SQL endpoint',
  'The shortcut has to exist before its permission can be checked, and the endpoint only serves a shortcut whose schema resolves.')
s('seq_shortcut_b1',
  'Query through the SQL endpoint → create the shortcut → validate the schema → grant the permission',
  'The endpoint has no table to expose until the shortcut exists.')
s('seq_shortcut_b2',
  'Grant the permission → query through the SQL endpoint → create the shortcut → validate the schema',
  'A permission granted before the shortcut exists is granted on nothing.')
s('seq_shortcut_b3',
  'Validate the schema → grant the permission → query through the endpoint → create the shortcut',
  'The schema cannot be validated until the shortcut points at the source.')

s('seq_dim_ok',
  'Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact',
  'Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own.')
s('seq_dim_b1',
  'Load the fact → build the conformed dimensions → profile the source keys → define the grain → add the surrogate keys',
  'The fact is loaded before the keys it references exist.')
s('seq_dim_b2',
  'Add the surrogate keys → load the fact → define the grain → profile the keys → build the dimensions',
  'Surrogate keys are assigned by the dimensions, which do not exist yet.')
s('seq_dim_b3',
  'Define the grain → add the surrogate keys → load the fact → profile the keys → build the dimensions',
  'The keys are profiled and the dimensions built before the fact can be loaded.')

s('seq_dq_ok',
  'Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate',
  'The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed.')
s('seq_dq_b1',
  'Recompute the aggregate → detect the duplicates → correct the partition → decide the surviving record',
  'Recomputing before the data is corrected republishes the same wrong total.')
s('seq_dq_b2',
  'Correct the partition → recompute the aggregate → decide the surviving record → detect the duplicates',
  'The partition cannot be corrected before the rule decides which record survives.')
s('seq_dq_b3',
  'Decide the surviving record → recompute the aggregate → detect the duplicates → correct the partition',
  'A rule chosen before the duplicates are known is chosen blind.')

# ---------------------------------------------------------------- domain 3
s('seq_tune_ok',
  'Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query',
  'The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect.')
s('seq_tune_b1',
  'Re-measure the query → optimize the table → read the plan → reduce the file count',
  'Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly.')
s('seq_tune_b2',
  'Optimize the table → re-measure the query → read the plan → reduce the file count',
  'The plan is what should have decided whether compaction was the right fix at all.')
s('seq_tune_b3',
  'Reduce the file count → read the plan → re-measure the query → optimize the table',
  'Measuring before the change and again after it is what makes the comparison possible.')

s('seq_spark_ok',
  'Open the Spark UI → find the stage with the skewed task → broadcast or salt the join → re-run and compare the stage time',
  'The UI locates the skew, the join strategy addresses it, and the second run is the evidence.')
s('seq_spark_b1',
  'Re-run and compare the stage time → open the Spark UI → find the skewed stage → salt the join',
  'A comparison before any change compares the job with itself.')
s('seq_spark_b2',
  'Salt the join → re-run the job → open the Spark UI → find the skewed stage',
  'Salting before locating the skew fixes a guess.')
s('seq_spark_b3',
  'Find the skewed stage → open the Spark UI → re-run the job → broadcast the join',
  'The UI is what does the finding, so it cannot come after it.')

s('seq_debug_ok',
  'Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity',
  'The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed.')
s('seq_debug_b1',
  'Rerun only the failed activity → read the run history → isolate the activity → reproduce the input',
  'Rerunning before reading the history repeats the failure without explaining it.')
s('seq_debug_b2',
  'Isolate the failing activity → rerun the activity → read the run history → reproduce the input',
  'The rerun happens before the cause is reproduced, so the second failure looks like a new one.')
s('seq_debug_b3',
  'Reproduce the input → isolate the activity → read the run history → rerun the activity',
  'The failing activity has to be known before its input can be reproduced.')

s('seq_monitor_ok',
  'Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week',
  'There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest.')
s('seq_monitor_b1',
  'Review the alert history → enable the monitoring output → set the threshold → build the dashboard',
  'There is no alert history before the alert exists.')
s('seq_monitor_b2',
  'Set the alert threshold → build the dashboard → review the history → enable the output',
  'A threshold with no output behind it cannot be evaluated.')
s('seq_monitor_b3',
  'Build the dashboard → set the threshold → enable the output → review the history',
  'The dashboard and the threshold both read an output that does not exist yet.')
