"""Candidate orderings for the sequencing items.

Each key maps to (label, meaning) exactly like the technical option bank, so a
sequencing item can be authored as an ordinary single-answer item whose four
options are four candidate orders. Every label contains the arrow between
steps; build.py and validate.py both rely on that.
"""
SEQUENCES = {}


def s(key, label, meaning):
    SEQUENCES[key] = (label, meaning)


# --- solution lifecycle and environment choice
s('seq_alm_ok',
  'Define the publisher prefix → build unmanaged in development → export the solution → import managed into test → deploy managed to production',
  'The prefix is fixed before schema names exist, and each later environment receives a managed copy rather than an edit.')
s('seq_alm_b1',
  'Build unmanaged in production → export the solution → define the publisher prefix → import managed into test → deploy to development',
  'Building in production exposes unfinished work, and a prefix chosen afterwards leaves the schema names inconsistent.')
s('seq_alm_b2',
  'Export the solution → define the publisher prefix → build unmanaged in development → deploy to production → import into test',
  'Exporting before the solution exists and testing after production both break the promotion order.')
s('seq_alm_b3',
  'Import managed into test → build unmanaged in development → deploy to production → define the publisher prefix → export the solution',
  'A managed import cannot precede the unmanaged build it is supposed to carry.')

s('seq_env_ok',
  'Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline',
  'The boundary and licence decide the environment type, and the pipeline carries the packaged result.')
s('seq_env_b1',
  'Create the solution with its publisher → deploy through the pipeline → identify the data boundary → choose the environment type',
  'Choosing an environment after deploying is how a solution ends up in the wrong data boundary.')
s('seq_env_b2',
  'Choose the environment type → deploy through the pipeline → identify the data boundary → create the solution with its publisher',
  'Deployment before packaging has nothing to deploy.')
s('seq_env_b3',
  'Deploy through the pipeline → create the solution with its publisher → choose the environment type → identify the data boundary',
  'Every step here runs ahead of the decision it depends on.')

# --- agents and requirement analysis
s('seq_agent_ok',
  'Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it',
  'Coverage is tested with a pilot before anyone commits to a custom build.')
s('seq_agent_b1',
  'Build a custom agent → map the requirement to a component → pilot in development → measure the outcome → check built-in coverage',
  'Building first pays the custom-agent cost before coverage is even known.')
s('seq_agent_b2',
  'Measure the outcome → pilot the agent in development → build a custom agent → map the requirement to a component → check built-in coverage',
  'There is nothing to measure before a pilot exists.')
s('seq_agent_b3',
  'Check whether a built-in agent covers it → build a custom agent → adopt it in production → map the requirement to a component → pilot in development',
  'Adopting before a pilot skips the step that would have caught the gap.')

# --- data model
s('seq_datamodel_ok',
  'Create the table → add the columns the process needs → configure the relationships → build the main form and public view → assign the security role',
  'Security is last because it depends on the tables, columns, and relationships it protects.')
s('seq_datamodel_b1',
  'Assign the security role → create the table → add the columns → configure the relationships → build the form and view',
  'A role cannot be assigned to a table that does not exist yet.')
s('seq_datamodel_b2',
  'Configure the relationships → create the table → build the form and view → add the columns → assign the security role',
  'Relationships and forms cannot precede the table and the columns they reference.')
s('seq_datamodel_b3',
  'Build the form and view → configure the relationships → assign the security role → create the table → add the columns',
  'The form is the last artifact of the model, not the first.')

s('seq_security_ok',
  'Identify who must see which records → assign the security role → set the business unit scope → add a field profile for the sensitive column → verify with a test user',
  'Access is designed from the data outward, and a test user proves the result.')
s('seq_security_b1',
  'Verify with a test user → assign the security role → identify who must see which records → set the business unit scope → add a field profile',
  'Verification with no design behind it confirms nothing in particular.')
s('seq_security_b2',
  'Add a field profile for the sensitive column → verify with a test user → identify who must see which records → assign the security role → set the business unit scope',
  'Field security is a refinement of the role, not a substitute for it.')
s('seq_security_b3',
  'Set the business unit scope → add a field profile → identify who must see which records → verify with a test user → assign the security role',
  'The role has to exist before scope or field profiles can narrow it.')

# --- model-driven app
s('seq_modelapp_ok',
  'Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role',
  'The app is composed from finished components, and access is granted last.')
s('seq_modelapp_b1',
  'Share the app → assign the backing security role → configure the forms and views → compose the app → set the navigation',
  'Sharing an app that has no components shows users an empty shell.')
s('seq_modelapp_b2',
  'Set the navigation in the sitemap → share the app → configure the forms and views → compose the app → assign the role',
  'Navigation is meaningless until the components exist.')
s('seq_modelapp_b3',
  'Assign the backing security role → configure the forms and views → set the navigation → compose the app → share the app',
  'Granting data access before the app exists gives access with nothing to use it in.')

s('seq_genpage_ok',
  'Describe the page in natural language → generate the page → review the data bindings → add the page to the app → confirm access for the audience',
  'Generation is a draft, so the bindings and the audience are checked before release.')
s('seq_genpage_b1',
  'Generate the page → publish it to the audience → describe the page in natural language → review the data bindings → add the page to the app',
  'Publishing before review exposes whatever the generator chose to bind to.')
s('seq_genpage_b2',
  'Review the data bindings → describe the page in natural language → confirm access for the audience → generate the page → add the page to the app',
  'There are no bindings to review before generation.')
s('seq_genpage_b3',
  'Add the page to the app → generate the page → confirm access for the audience → describe the page → review the data bindings',
  'A page cannot be added before it is generated.')

# --- canvas app
s('seq_canvas_ok',
  'Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app',
  'The data source comes first, and testing precedes publishing.')
s('seq_canvas_b1',
  'Publish the app → connect the data source → build the screens → add error handling → test with Monitor and Test Studio',
  'Publishing before testing is how a broken save reaches users.')
s('seq_canvas_b2',
  'Add error handling → connect the data source → test with Monitor → build the screens → publish the app',
  'Error handling has nothing to wrap before the calls exist.')
s('seq_canvas_b3',
  'Build the screens → test with Monitor → connect the data source → publish the app → add error handling',
  'Screens need a data source, and publishing needs a tested app.')

s('seq_agentcanvas_ok',
  'Build the canvas app → add the Copilot Studio agent as a component → configure the agent topics and knowledge → test the conversation in the app → publish',
  'The agent is added to a working app, and its behaviour is tested before release.')
s('seq_agentcanvas_b1',
  'Configure the agent topics → publish → build the canvas app → add the agent as a component → test the conversation',
  'Publishing before the host app exists delivers an agent nobody can reach.')
s('seq_agentcanvas_b2',
  'Test the conversation in the app → add the agent as a component → build the canvas app → configure the agent topics → publish',
  'The conversation cannot be tested before the component is in an app.')
s('seq_agentcanvas_b3',
  'Add the agent as a component → build the canvas app → publish → configure the agent topics → test the conversation',
  'The topics are what the test is checking, so they come first.')

# --- flows
s('seq_flow_ok',
  'Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run',
  'The event decides the trigger, and the payload decides whether the expressions actually resolve.')
s('seq_flow_b1',
  'Add the actions and branches → add the trigger → test with a real payload → decide which event starts the process → read the run history',
  'Actions placed before the trigger cannot know what data they receive.')
s('seq_flow_b2',
  'Test with a real payload → decide which event starts the process → read the run history → add the trigger → add the actions',
  'There is no payload to test until a trigger and actions exist.')
s('seq_flow_b3',
  'Read the run history → add the trigger → decide which event starts the process → add the actions → test with a real payload',
  'A run history only exists after a run has happened.')

s('seq_approval_ok',
  'Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester',
  'The branch reads the approval outcome, and the record update carries the decision.')
s('seq_approval_b1',
  'Update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome → notify the requester',
  'The record cannot be updated with a decision that has not been taken.')
s('seq_approval_b2',
  'Branch on the outcome → trigger on the submitted request → notify the requester → start and wait for the approval → update the record',
  'A branch with no outcome yet has nothing to evaluate.')
s('seq_approval_b3',
  'Notify the requester → update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome',
  'Notifying first tells the requester about a decision that does not exist.')

s('seq_flowdebug_ok',
  'Reproduce the failure with the real inputs → open the run history → inspect the failing action\'s inputs and outputs → fix the expression or mapping → resubmit the run',
  'The run history is what turns a symptom into a specific wrong value.')
s('seq_flowdebug_b1',
  'Resubmit the run → open the run history → reproduce the failure → fix the expression → inspect the failing action',
  'Resubmitting an unfixed flow repeats the same failure.')
s('seq_flowdebug_b2',
  'Fix the expression → reproduce the failure → resubmit the run → inspect the failing action → open the run history',
  'A fix applied before diagnosis is a guess.')
s('seq_flowdebug_b3',
  'Open the run history → resubmit the run → reproduce the failure → inspect the failing action → fix the expression',
  'There is no run to inspect until the failure is reproduced.')

# --- prompts and models
s('seq_prompt_ok',
  'Choose a template or describe the task → add typed inputs → attach the knowledge source → choose a model for the task → test with sample inputs → consume the prompt from the app or flow',
  'Inputs and knowledge define the contract, and the prompt is tested before anything consumes it.')
s('seq_prompt_b1',
  'Consume the prompt from the app → choose a model → add typed inputs → test with sample inputs → attach the knowledge source → choose a template',
  'A consumer wired to an untested prompt shows the failure to a user.')
s('seq_prompt_b2',
  'Attach the knowledge source → consume the prompt from the app → choose a template → test with sample inputs → add typed inputs → choose a model',
  'Consumption cannot precede the contract the consumer must satisfy.')
s('seq_prompt_b3',
  'Test with sample inputs → attach the knowledge source → choose a template → choose a model → consume the prompt → add typed inputs',
  'A test before the inputs and knowledge exist tests the wrong thing.')

s('seq_promptconsume_ok',
  'Publish the prompt → confirm the connection and its credentials → call it from the canvas app → call it from the cloud flow → review usage and cost after release',
  'Publishing and the connection come first; reviewing usage is what closes the loop.')
s('seq_promptconsume_b1',
  'Call it from the canvas app → publish the prompt → review usage and cost → confirm the connection → call it from the cloud flow',
  'An unpublished prompt is not callable from an app.')
s('seq_promptconsume_b2',
  'Review usage and cost → call it from the cloud flow → publish the prompt → confirm the connection → call it from the canvas app',
  'Usage can only be reviewed after something has called the prompt.')
s('seq_promptconsume_b3',
  'Confirm the connection → review usage and cost → publish the prompt → call it from the cloud flow → call it from the canvas app',
  'The connection is confirmed against a prompt that must already be published.')

# --- business logic
s('seq_businessrule_ok',
  'State the rule in business terms → choose the mechanism that enforces it where it must hold → configure the rule at table scope → test it on the form and through an import → document it for the support team',
  'Choosing the mechanism before configuring anything is what stops a form-only rule being used for a rule that must survive an import.')
s('seq_businessrule_b1',
  'Configure the rule at table scope → state the rule in business terms → document it → test it through an import → choose the mechanism',
  'Configuration before the rule is stated produces a rule nobody agreed to.')
s('seq_businessrule_b2',
  'Test it on the form → configure the rule → state the rule in business terms → choose the mechanism → document it',
  'A test needs the configured rule and the stated requirement behind it.')
s('seq_businessrule_b3',
  'Document it for the support team → test it through an import → choose the mechanism → state the rule → configure the rule',
  'Documentation of an unconfigured rule describes an intention, not a system.')

s('seq_bpf_ok',
  'Define the stages the record moves through → choose the columns each stage requires → branch the process where the case types diverge → test a record through every stage → hand the process to the users',
  'Stages and their required columns define the process; branching handles the variants without a second process.')
s('seq_bpf_b1',
  'Branch the process → define the stages → hand the process to the users → test a record through every stage → choose the columns each stage requires',
  'A branch needs stages to branch from.')
s('seq_bpf_b2',
  'Test a record through every stage → branch the process → define the stages → hand the process to the users → choose the columns',
  'There is nothing to test through until the stages exist.')
s('seq_bpf_b3',
  'Choose the columns each stage requires → hand the process to the users → test a record → define the stages → branch the process',
  'Users handed a process with no stages see an empty tracker.')

s('seq_calccol_ok',
  'Decide whether the value is derived at read time or aggregated from children → add the column of the matching type → configure the formula or the rollup → verify the recalculation on a test record → surface the column on the form and view',
  'The read-time versus aggregate decision is what chooses between a formula column and a rollup.')
s('seq_calccol_b1',
  'Surface the column on the form → add the column of the matching type → decide whether the value is derived or aggregated → verify the recalculation → configure the formula or rollup',
  'The form is the last step, not the first.')
s('seq_calccol_b2',
  'Configure the formula or rollup → decide whether the value is derived or aggregated → surface the column → add the column → verify the recalculation',
  'A formula cannot be configured before the column exists.')
s('seq_calccol_b3',
  'Verify the recalculation on a test record → surface the column on the form → configure the formula or rollup → add the column → decide whether the value is derived or aggregated',
  'Verification is the check on a configured column, not a step before it.')
