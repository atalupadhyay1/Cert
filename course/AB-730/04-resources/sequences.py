"""Candidate orderings for the AB-730 sequencing items.

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


# --- Exam 1 ---------------------------------------------------------------
s('seq1a_ok',
  'Inventory sites and fix permissions → classify the content → pilot with one team → review audit and feedback → expand',
  'Permissions and classification must be right before grounding is switched on, and a pilot produces the evidence that justifies expansion.')
s('seq1a_b1',
  'Expand to all staff → fix permissions after the first oversharing report → classify the content → review audit findings',
  'Expanding first exposes every stale permission at once, and the review arrives after the damage.')
s('seq1a_b2',
  'Pilot with one team → expand to all staff → inventory sites and fix permissions → review audit and feedback',
  'A pilot cannot be meaningful when permissions are still unknown, and fixing them during a full rollout creates competing changes.')
s('seq1a_b3',
  'Classify the content → expand to all staff → pilot with one team → inventory sites and fix permissions',
  'Classification helps, but expanding before a pilot and before the inventory removes both the evidence and the control.')

s('seq1b_ok',
  'Open the cited source → check that the passage supports the claim → confirm the policy version in effect → record the reviewer decision',
  'Each step narrows the risk that a fluent answer is accepted on the strength of a citation nobody opened.')
s('seq1b_b1',
  'Accept the answer because it cites a source → check the citation formatting → confirm the policy version → record the decision',
  'Formatting is not evidence; accepting before opening the source skips the only step that catches a wrong citation.')
s('seq1b_b2',
  'Record the reviewer decision → open the cited source → check the passage → confirm the policy version',
  'Recording before checking makes the record attest to a review that has not happened.')
s('seq1b_b3',
  'Confirm the policy version → record the decision → open the cited source → check the passage',
  'Version control matters, but it cannot substitute for reading the passage the answer relies on.')

s('seq1c_ok',
  'Treat the document text as data → check whether the answer changed → quarantine the document → report it to security',
  'Containment starts by refusing to follow embedded instructions, then confirms impact, then prevents reuse and informs the owner.')
s('seq1c_b1',
  'Follow the instruction to see what happens → report it to security → quarantine the document → check the answer',
  'Following the instruction is the harm; testing it on live content is not a safe way to learn what it does.')
s('seq1c_b2',
  'Quarantine the document → follow the instruction → report it to security → check the answer',
  'Quarantine is right, but following the instruction afterwards defeats the containment and can still leak content.')
s('seq1c_b3',
  'Report it to security → quarantine the document → follow the instruction → check the answer',
  'Reporting early is good, yet deliberately executing the injected instruction remains the step that causes the incident.')

s('seq1d_ok',
  'Name the decision to be made → choose the sources that hold the evidence → ask with those sources referenced → check the answer against them',
  'A decision and a source set come before the prompt, and the check closes the loop on what the sources actually say.')
s('seq1d_b1',
  'Ask the question in a general chat → accept the first answer → look for a source afterwards → name the decision',
  'A general answer with no named source is exactly the ungrounded response the workflow should avoid.')
s('seq1d_b2',
  'Choose the sources → ask with those sources referenced → name the decision → check the answer',
  'Choosing sources before knowing the decision can ground the answer in material that is beside the point.')
s('seq1d_b3',
  'Check the answer → name the decision → choose the sources → ask the question',
  'A check cannot come before there is an answer, and the whole order leaves the request unanchored.')

s('seq1e_ok',
  'State the role, goal, and audience → supply the facts and constraints → name the output format → rerun and compare',
  'The first prompt carries everything the model needs, and the rerun is what shows whether the wording worked.')
s('seq1e_b1',
  'Name the output format → ask the question → add constraints after the first draft → state the audience',
  'Fixing format first and adding the audience last produces a well-shaped answer aimed at the wrong reader.')
s('seq1e_b2',
  'Rerun and compare → state the role and goal → supply facts → name the format',
  'A comparison needs two attempts, so it cannot be the first step in building the prompt.')
s('seq1e_b3',
  'Supply the facts → state the role → rerun and compare → state the audience',
  'The rerun comes before the audience is known, so the comparison measures the wrong thing.')

s('seq1f_ok',
  'Confirm the prompt works → save it with a descriptive title → share it with the team → review it after the content changes',
  'A prompt is shared only after it is proven, and it is reviewed when the underlying content moves.')
s('seq1f_b1',
  'Share it with the team → save it → confirm it works → review it after the content changes',
  'Sharing an unproven prompt spreads a defect, and saving it makes the defect durable.')
s('seq1f_b2',
  'Save it with a descriptive title → share it → confirm it works → review it',
  'Saving and sharing before confirming the prompt works gives the team a template nobody has tested.')
s('seq1f_b3',
  'Review it after the content changes → share it → save it → confirm it works',
  'Reviewing before the prompt exists removes the baseline, and the sharing still precedes any proof.')

s('seq1g_ok',
  'Ask for a pre-read → run the meeting with Facilitator → review the recap → move actions into the tracker',
  'Preparation, in-meeting support, and follow-up each build on the previous artifact.')
s('seq1g_b1',
  'Run the meeting → ask for a pre-read → review the recap → move actions into the tracker',
  'A pre-read requested after the meeting cannot inform the discussion, which is its only purpose.')
s('seq1g_b2',
  'Review the recap → run the meeting → ask for a pre-read → move actions into the tracker',
  'A recap of a meeting that has not happened has nothing to summarize.')
s('seq1g_b3',
  'Move actions into the tracker → review the recap → ask for a pre-read → run the meeting',
  'Actions come from the recap, which comes from the meeting, so this order is inverted end to end.')

s('seq1h_ok',
  'Define the deliverable and constraints → review the plan → check each checkpoint → approve the final output',
  'A clear end state shapes the plan, checkpoints catch drift, and approval follows evidence.')
s('seq1h_b1',
  'Approve the final output → review the plan → check each checkpoint → define the deliverable',
  'Approval with no plan or checkpoints is a signature on work nobody has inspected.')
s('seq1h_b2',
  'Review the plan → define the deliverable → approve the final output → check each checkpoint',
  'The plan cannot be sound before the deliverable is defined, and approval before checkpoints skips the controls.')
s('seq1h_b3',
  'Check each checkpoint → define the deliverable → review the plan → approve the output',
  'Checkpoints need a plan and a defined deliverable to check against.')

# --- Exam 2 ---------------------------------------------------------------
s('seq2a_ok',
  'Confirm the client content may be processed in the tenant → restrict the source set to the engagement → work in a Notebook → review the output before it leaves the firm',
  'Client confidentiality is settled before any content is used, and the review is what allows the result to leave the firm.')
s('seq2a_b1',
  'Work in a Notebook → confirm the content may be processed → restrict the source set → review the output',
  'Working first means the content has already been processed before anyone checked whether it was allowed.')
s('seq2a_b2',
  'Restrict the source set → review the output → confirm the content may be processed → work in a Notebook',
  'A review of an output produced before the confidentiality check cannot undo the exposure.')
s('seq2a_b3',
  'Review the output → work in a Notebook → restrict the source set → confirm the content may be processed',
  'Every step is out of order: the result is reviewed before it exists and the permission is confirmed last.')

s('seq2b_ok',
  'Identify the external repository → choose a connector that preserves permissions → set the connector ACLs → ask a question that requires the external content',
  'The connector choice and ACLs decide whether grounded answers can include the external items at all.')
s('seq2b_b1',
  'Ask the question → identify the repository → choose a connector → set the ACLs',
  'Asking first produces a confident answer from internal content only, which hides the gap the exercise was meant to close.')
s('seq2b_b2',
  'Set the ACLs → ask the question → identify the repository → choose a connector',
  'ACLs cannot be set for a connector and repository that have not been chosen yet.')
s('seq2b_b3',
  'Choose a connector → ask the question → set the ACLs → identify the repository',
  'The question is asked before permissions are applied, which is the state in which the external index leaks.')

s('seq2c_ok',
  'Draft the section in Word → check the figures against Excel → build the slides from the reviewed draft → confirm the deck matches the brief',
  'Draft, verify, and present in that order means each artifact inherits content that was already checked.')
s('seq2c_b1',
  'Build the slides → draft in Word → check the figures → confirm the deck matches the brief',
  'Slides built before the draft is checked present numbers that may still be wrong.')
s('seq2c_b2',
  'Check the figures → build the slides → draft in Word → confirm the deck matches the brief',
  'There is nothing to check until the draft exists, and the deck is built from a document that does not exist yet.')
s('seq2c_b3',
  'Build the slides → confirm the deck matches the brief → draft in Word → check the figures',
  'The brief cannot be matched before the content and the numbers are settled.')

s('seq2d_ok',
  'Ask for a pre-read → join with Facilitator running → use catchup if joining late → extract actions from the recap',
  'Preparation, live support, and the recap chain together; each later step depends on the earlier one.')
s('seq2d_b1',
  'Extract actions from the recap → ask for a pre-read → join the meeting → use catchup',
  'Actions cannot be extracted before the meeting has produced a recap.')
s('seq2d_b2',
  'Join the meeting → extract actions → ask for a pre-read → use catchup',
  'The pre-read after the meeting cannot shape it, and catchup after the meeting has ended is meaningless.')
s('seq2d_b3',
  'Use catchup → ask for a pre-read → extract actions → join the meeting',
  'Catchup only applies while a meeting is in progress, so it cannot come before joining.')

s('seq2e_ok',
  'Capture the working notes in a Page → share the Page with the client team → keep the Page as the live version → export the final copy for the record',
  'One live version removes the attachment sprawl, and the export is taken only when the content is settled.')
s('seq2e_b1',
  'Email the draft to each reviewer → capture notes in a Page → export the final copy → share the Page',
  'Emailing first recreates the attachment sprawl that Pages exists to remove.')
s('seq2e_b2',
  'Export the final copy → email the draft → share the Page → capture notes in a Page',
  'An export before the work exists and before the Page is shared produces a record of nothing.')
s('seq2e_b3',
  'Share the Page → export the final copy → capture notes in a Page → keep the Page live',
  'Exporting before the notes are captured freezes a draft as if it were final.')

s('seq2f_ok',
  'Describe the deliverable → choose the prebuilt agent or skill → delegate the run → review the output against the brief',
  'Matching the deliverable to an existing agent first avoids building a duplicate, and the review stays with the person.')
s('seq2f_b1',
  'Build a custom agent → describe the deliverable → review the output → choose a prebuilt agent',
  'Building before checking what already exists duplicates work that may already be maintained.')
s('seq2f_b2',
  'Review the output → delegate the run → describe the deliverable → choose the agent',
  'The output is reviewed before the deliverable is described, so there is no basis for the review.')
s('seq2f_b3',
  'Delegate the run → build a custom agent → review the output → describe the deliverable',
  'Delegating before the agent and deliverable are settled produces a run with no agreed purpose.')

s('seq2g_ok',
  'Decide the cadence → build and test the prompt → save it in the library → schedule it and check the first runs',
  'A tested, saved prompt is what a schedule should run; checking the first runs confirms the cadence works.')
s('seq2g_b1',
  'Schedule the prompt → build it → save it → decide the cadence',
  'Scheduling something that has not been built or tested runs a broken job on a timer.')
s('seq2g_b2',
  'Save it in the library → schedule it → build and test it → decide the cadence',
  'Saving and scheduling before building gives the schedule nothing valid to run.')
s('seq2g_b3',
  'Check the first runs → decide the cadence → build the prompt → save it',
  'The first runs cannot be checked before the prompt exists and the cadence is chosen.')

s('seq2h_ok',
  'Set custom instructions for tone → reference the engagement files → run the prompt → review and clear saved memories when the engagement ends',
  'Standing instructions and explicit sources shape the answer, and memory is cleaned when the context ends.')
s('seq2h_b1',
  'Run the prompt → set custom instructions → reference the files → clear saved memories',
  'Running first answers with the wrong voice and sources, which is the exact problem the instructions solve.')
s('seq2h_b2',
  'Clear saved memories → run the prompt → reference the files → set custom instructions',
  'Clearing memory before the engagement has run removes context that the work still needs.')
s('seq2h_b3',
  'Reference the files → clear saved memories → set custom instructions → run the prompt',
  'Clearing memory in the middle of an engagement removes facts the prompt relies on.')

# --- Exam 3 ---------------------------------------------------------------
s('seq3a_ok',
  'Clean the duplicate records → confirm the unit and date conventions → build the analysis in Excel → have the planner check the result',
  'Duplicate records and mismatched units corrupt any analysis built on them, and the planner is the check on interpretation.')
s('seq3a_b1',
  'Build the analysis → clean the duplicates → confirm the conventions → have the planner check the result',
  'Analysis built on dirty records produces a number that has to be thrown away when the cleaning happens.')
s('seq3a_b2',
  'Have the planner check the result → build the analysis → confirm the conventions → clean the records',
  'There is no result to check before the analysis exists.')
s('seq3a_b3',
  'Confirm the conventions → build the analysis → have the planner check it → clean the duplicates',
  'Cleaning after sign-off means the approved number may not match the cleaned data at all.')

s('seq3b_ok',
  'Select the range → ask Copilot for the chart → check the axes and labels against the data → place the chart in the deck',
  'Charting the selected range keeps the visual tied to data, and the label check catches a misleading axis before an audience sees it.')
s('seq3b_b1',
  'Place the chart in the deck → ask Copilot for the chart → select the range → check the axes',
  'A chart cannot be placed before it is generated, and the deck would carry an unchecked visual.')
s('seq3b_b2',
  'Ask Copilot for the chart → place it in the deck → select the range → check the axes',
  'Placing the chart before checking its axes publishes a visual that may invert the message.')
s('seq3b_b3',
  'Check the axes → select the range → place the chart in the deck → ask for the chart',
  'Axes cannot be checked before a chart exists, and the chart is asked for last.')

s('seq3c_ok',
  'Reconcile the generated figures with the source workbook → check the assumptions with the analyst → draft the narrative → send it for business sign-off',
  'Numbers are verified before prose is built on them, and sign-off is the last gate.')
s('seq3c_b1',
  'Draft the narrative → reconcile the figures → send it for sign-off → check the assumptions',
  'A narrative written before reconciliation embeds numbers that may change the story.')
s('seq3c_b2',
  'Send it for business sign-off → draft the narrative → reconcile the figures → check the assumptions',
  'Sign-off requested before the narrative exists is not a review of anything.')
s('seq3c_b3',
  'Check the assumptions → send it for sign-off → reconcile the figures → draft the narrative',
  'Sign-off precedes both the reconciliation and the draft, so it approves nothing.')

s('seq3d_ok',
  'Confirm the retention rule for prompts and outputs → keep the run history → review the outputs before sign-off → delete the scratch material',
  'Retention is decided before data accumulates, and the run history is the evidence a reviewer needs.')
s('seq3d_b1',
  'Delete the scratch material → confirm the retention rule → keep the run history → review the outputs',
  'Deleting before the retention rule is known may destroy a record the organization is required to keep.')
s('seq3d_b2',
  'Review the outputs → delete the scratch material → confirm the retention rule → keep the run history',
  'Deleting before the retention decision removes the material a review would need.')
s('seq3d_b3',
  'Keep the run history → delete the scratch material → review the outputs → confirm the retention rule',
  'Retention confirmed last means the deletion has already happened without a rule.')

s('seq3e_ok',
  'Identify the recurring exception → check whether a prebuilt agent covers it → if the run needs several steps, delegate it to Cowork → review the run and fix the cause',
  'The prebuilt option is tested before delegating, and the review addresses the cause rather than only the output.')
s('seq3e_b1',
  'Delegate it to Cowork → identify the exception → check for a prebuilt agent → review the run',
  'Delegating before the exception is understood risks automating the wrong step.')
s('seq3e_b2',
  'Review the run → identify the exception → delegate to Cowork → check for a prebuilt agent',
  'A run cannot be reviewed before it exists, and the prebuilt check is skipped entirely.')
s('seq3e_b3',
  'Check for a prebuilt agent → review the run → identify the exception → delegate to Cowork',
  'The run is reviewed before the task is identified and before anything is delegated.')

s('seq3f_ok',
  'Ask for the pre-read → use Facilitator to keep the agenda → use catchup when joining late → turn the recap into actions',
  'Each tool supports a different moment, and the recap converts the meeting into follow-through.')
s('seq3f_b1',
  'Turn the recap into actions → use catchup → ask for the pre-read → use Facilitator',
  'Actions cannot precede the meeting that produces them, and the pre-read comes too late to help.')
s('seq3f_b2',
  'Use catchup → turn the recap into actions → ask for the pre-read → use Facilitator',
  'Catchup applies only during the meeting, so it cannot be the first step of the cycle.')
s('seq3f_b3',
  'Use Facilitator → turn the recap into actions → use catchup → ask for the pre-read',
  'The pre-read after the meeting has no effect on it, and catchup is used too late.')

s('seq3g_ok',
  'Find the agent in the agent store → add it to the Copilot experience → start the request from inside the agent → filter the chat list by agent to find it later',
  'Discovery, deployment, correct use, and retrieval follow the way agents are actually adopted.')
s('seq3g_b1',
  'Filter the chat list by agent → find it in the store → start the request → add it to Copilot',
  'Filtering for an agent that has not been added finds nothing.')
s('seq3g_b2',
  'Start the request → add the agent → filter the chat list → find it in the store',
  'The request is started before the agent exists in the experience, so its sources are never applied.')
s('seq3g_b3',
  'Add it to Copilot → filter the chat list → find it in the store → start the request',
  'The agent is added before it is found, and filtering before use leaves the conversation unclassified.')

s('seq3h_ok',
  'Define the recurring deliverable → confirm the owner → test the run once → schedule it and review the first live output',
  'A recurring job needs an owner and one proven run before the schedule makes it someone’s problem.')
s('seq3h_b1',
  'Schedule it → test the run once → define the deliverable → confirm the owner',
  'A schedule created before the deliverable and owner exist will run something nobody owns.')
s('seq3h_b2',
  'Test the run once → schedule it → define the deliverable → confirm the owner',
  'A test without a defined deliverable cannot establish whether the output is right.')
s('seq3h_b3',
  'Confirm the owner → schedule it → test the run once → define the deliverable',
  'Scheduling before testing turns an untested job into a recurring commitment.')

# --- Exam 4 ---------------------------------------------------------------
s('seq4a_ok',
  'Confirm the record class and retention rule → restrict the sources to the case file → generate the summary → have the case owner approve it',
  'The record class decides what may be kept and for how long, so it is settled before content is processed.')
s('seq4a_b1',
  'Generate the summary → confirm the retention rule → restrict the sources → have the owner approve it',
  'Generating before the retention rule is known can create a record that should never have existed in that form.')
s('seq4a_b2',
  'Have the owner approve it → generate the summary → confirm the retention rule → restrict the sources',
  'Approval is requested before the summary exists, and the retention question is answered last.')
s('seq4a_b3',
  'Restrict the sources → have the owner approve it → confirm the retention rule → generate the summary',
  'There is nothing to approve until the summary is generated, and the rule is still unresolved.')

s('seq4b_ok',
  'Inventory the sites holding case data → remove stale groups and broad links → pilot Copilot with one team → review audit and feedback',
  'An access review before enablement is what stops grounding from revealing permissions that were already too broad.')
s('seq4b_b1',
  'Pilot Copilot with one team → inventory the sites → remove stale groups → review audit',
  'Piloting before the inventory means the pilot itself may expose content the review would have removed.')
s('seq4b_b2',
  'Review audit → remove stale groups → inventory the sites → pilot with one team',
  'Audit review is a later control and cannot replace the inventory and permission clean-up that precede it.')
s('seq4b_b3',
  'Remove stale groups → pilot with one team → inventory the sites → review audit',
  'Groups cannot be removed before the sites and groups are inventoried.')

s('seq4c_ok',
  'Send the agenda and pre-read → run the session with Facilitator → use catchup for late joiners → publish the recap with actions',
  'Preparation and in-meeting support produce the recap, which is then published with owners.')
s('seq4c_b1',
  'Publish the recap with actions → send the pre-read → run the session → use catchup',
  'A recap published before the session summarizes a meeting that has not happened.')
s('seq4c_b2',
  'Use catchup for late joiners → publish the recap → send the pre-read → run the session',
  'Catchup is a live tool, and the recap and pre-read are both out of sequence.')
s('seq4c_b3',
  'Run the session → send the pre-read → publish the recap → use catchup',
  'A pre-read sent after the session cannot inform it, and catchup has no live meeting left.')

s('seq4d_ok',
  'Create a Notebook for the committee → add the submissions and prior minutes → analyse the themes → share the Notebook with the panel',
  'The source set is fixed before analysis, and sharing follows the analysis the panel needs to see.')
s('seq4d_b1',
  'Share the Notebook with the panel → analyse the themes → add the submissions → create a Notebook',
  'There is nothing to share before the Notebook and its sources exist.')
s('seq4d_b2',
  'Analyse the themes → create a Notebook → add the submissions → share it',
  'Analysis cannot precede the sources it analyses, and the Notebook is created after the work.')
s('seq4d_b3',
  'Add the submissions → share the Notebook → create a Notebook → analyse the themes',
  'The Notebook is created after it is shared, and the panel sees unanalysed material.')

s('seq4e_ok',
  'Draft the consultation response in Word → move it into a Page → invite the review group → keep the Page as the live version',
  'The draft is the input, the Page is the shared workspace, and the group works on one live version.')
s('seq4e_b1',
  'Invite the review group → draft in Word → move it into a Page → keep the Page live',
  'Inviting the group before there is a draft gives them nothing to review.')
s('seq4e_b2',
  'Keep the Page live → move it into a Page → draft in Word → invite the review group',
  'The Page is kept live before content exists, and the draft is produced afterwards.')
s('seq4e_b3',
  'Move the draft into a Page → invite the review group → draft the response in Word → keep the Page live',
  'The draft is written after it has been moved, so the Page holds an empty shell.')

s('seq4f_ok',
  'Name the committee decision → gather the cited evidence → draft the briefing → check each citation before circulation',
  'A named decision focuses the evidence, and the citation check is the last gate before members read it.')
s('seq4f_b1',
  'Draft the briefing → circulate it → check each citation → name the decision',
  'Circulating before the citation check publishes claims that may not survive verification.')
s('seq4f_b2',
  'Check each citation → name the decision → draft the briefing → gather the evidence',
  'There is nothing to cite before the evidence is gathered and the brief is written.')
s('seq4f_b3',
  'Gather the evidence → circulate the briefing → check each citation → name the decision',
  'The briefing is circulated before it is written, and the check is too late to matter.')

s('seq4g_ok',
  'Identify the student records system → add a connector with the source ACLs → test with an entitled user and a non-entitled user → document the permission model',
  'A connector that preserves source permissions is proven by testing both an allowed and a disallowed user.')
s('seq4g_b1',
  'Test with a non-entitled user → add a connector → identify the system → document the permission model',
  'The test cannot run before the connector exists, and identifying the system comes last.')
s('seq4g_b2',
  'Document the permission model → test with users → identify the system → add a connector',
  'The permission model cannot be documented before the connector and its ACLs are known.')
s('seq4g_b3',
  'Add a connector → document the permission model → identify the system → test with users',
  'The connector is added before the source system is identified, and testing is deferred to the end.')

s('seq4h_ok',
  'Define the report and its evidence → choose the prebuilt skill or create a custom one → delegate the run and review the plan → approve the draft for the funder',
  'The deliverable and evidence shape the skill choice, and approval stays with the person accountable to the funder.')
s('seq4h_b1',
  'Approve the draft for the funder → delegate the run → define the report → choose the skill',
  'Approval is given before there is a draft, and the deliverable is defined after the run started.')
s('seq4h_b2',
  'Delegate the run → approve the draft → define the report → choose the skill',
  'The run starts with no defined report, and the draft is approved before it is produced.')
s('seq4h_b3',
  'Choose the skill → approve the draft → define the report → delegate the run',
  'The draft is approved before the run that produces it, and the deliverable is still undefined.')

# --- Exam 5 ---------------------------------------------------------------
s('seq5a_ok',
  'Write the creative brief → generate candidate images → check usage rights and brand rules → place the approved image in the campaign',
  'Rights and brand checks come before an image is used publicly, and the brief is what the candidates are judged against.')
s('seq5a_b1',
  'Generate candidate images → place the approved image in the campaign → check usage rights → write the brief',
  'Publishing before rights are checked is the exposure the check exists to prevent.')
s('seq5a_b2',
  'Place the approved image in the campaign → write the brief → generate candidates → check the rights',
  'The campaign is built before any image exists or has been briefed.')
s('seq5a_b3',
  'Check usage rights → place the image → generate candidates → write the brief',
  'There are no rights to check before the images are generated, and the brief comes last.')

s('seq5b_ok',
  'Agree the campaign tone and rules → test a prompt on real briefs → save it with a descriptive title → share it with the campaign team',
  'A tested prompt that encodes the agreed tone is worth sharing; an untested one spreads inconsistency.')
s('seq5b_b1',
  'Share it with the campaign team → agree the tone → test the prompt → save it',
  'Sharing before the tone is agreed and the prompt is tested gives the team a template with no authority.')
s('seq5b_b2',
  'Save it with a descriptive title → share it → agree the tone → test the prompt',
  'Saving and sharing precede both the tone decision and the test.')
s('seq5b_b3',
  'Test the prompt → share it → save it → agree the tone',
  'The test has no criteria before the tone is agreed, and sharing precedes saving.')

s('seq5c_ok',
  'Draft the campaign narrative in Word → build the budget model in Excel → generate the client deck from both → check the numbers in the deck',
  'The narrative and model are the inputs, the deck assembles them, and the numbers are checked in the artifact the client sees.')
s('seq5c_b1',
  'Generate the client deck → draft the narrative → build the budget model → check the numbers',
  'The deck is generated before its inputs exist, so the numbers cannot be traced.')
s('seq5c_b2',
  'Check the numbers → generate the deck → draft the narrative → build the model',
  'Numbers cannot be checked before the model and deck exist.')
s('seq5c_b3',
  'Build the budget model → generate the deck → check the numbers → draft the narrative',
  'The narrative is written after the deck that should present it, so the deck tells a different story.')

s('seq5d_ok',
  'Record the client call with consent → review the intelligent recap → pull the decisions and actions → write the creative brief from them',
  'Consent precedes recording, and the brief is written from a reviewed recap rather than a raw transcript.')
s('seq5d_b1',
  'Write the creative brief → record the call → review the recap → pull the actions',
  'The brief is written before the call that defines it, and consent is not addressed at all.')
s('seq5d_b2',
  'Review the recap → record the call → pull the actions → write the brief',
  'A recap cannot be reviewed before the call is recorded.')
s('seq5d_b3',
  'Pull the decisions and actions → write the brief → record the call → review the recap',
  'Decisions cannot be pulled from a call that has not been recorded or recapped.')

s('seq5e_ok',
  'Map the intake steps → check whether a prebuilt agent fits → build a scoped custom agent if it does not → assign an owner and review cadence',
  'Mapping the process first shows whether a prebuilt agent already covers it, and a custom build needs an owner.')
s('seq5e_b1',
  'Build a scoped custom agent → map the intake steps → check for a prebuilt agent → assign an owner',
  'Building before mapping duplicates a capability that may already exist.')
s('seq5e_b2',
  'Assign an owner → build the agent → check for a prebuilt agent → map the steps',
  'The owner is assigned before the agent exists and before anyone knows what it must do.')
s('seq5e_b3',
  'Check for a prebuilt agent → build a custom agent → map the steps → assign an owner',
  'Checking for a prebuilt agent without mapping the process cannot establish whether it fits.')

s('seq5f_ok',
  'Agree the questions the summary must answer → build and test the prompt → save it in the library → schedule the weekly run and review the first output',
  'The question set defines the prompt, and the first scheduled run is reviewed before it becomes routine.')
s('seq5f_b1',
  'Schedule the weekly run → agree the questions → build the prompt → save it',
  'A schedule created before the questions and prompt exist produces a weekly empty or wrong summary.')
s('seq5f_b2',
  'Save it in the library → schedule the run → agree the questions → build the prompt',
  'The library entry and schedule precede the prompt they are meant to hold.')
s('seq5f_b3',
  'Review the first output → agree the questions → schedule the run → build the prompt',
  'There is no output to review before the prompt is built and scheduled.')

s('seq5g_ok',
  'Write the event brief → choose prebuilt skills for known steps → delegate the plan to Cowork → review the plan before bookings are made',
  'The brief and skill choice shape the plan, and the plan review is the gate before commitments are made.')
s('seq5g_b1',
  'Review the plan → delegate the plan to Cowork → write the brief → choose the skills',
  'The plan cannot be reviewed before it exists, and the brief is written afterwards.')
s('seq5g_b2',
  'Choose prebuilt skills → review the plan → write the brief → delegate the plan',
  'The skills are chosen without a brief, and the plan is reviewed before it is delegated.')
s('seq5g_b3',
  'Delegate the plan to Cowork → write the event brief → review the plan → choose the skills',
  'Delegating before the brief produces a plan for the wrong event, and skills are chosen last.')

s('seq5h_ok',
  'Identify the media archive → connect it with source permissions → confirm an entitled search returns the clip → confirm a non-entitled search does not',
  'Both a positive and a negative permission test are needed before an external archive is trusted with grounding.')
s('seq5h_b1',
  'Confirm a non-entitled search does not return the clip → connect the archive → identify the archive → confirm an entitled search',
  'The tests cannot run before the connector exists, and identifying the archive comes last.')
s('seq5h_b2',
  'Confirm an entitled search returns the clip → identify the archive → connect it → confirm a non-entitled search',
  'The positive test is run before the archive is connected, so it proves nothing.')
s('seq5h_b3',
  'Connect the archive → confirm a non-entitled search does not return the clip → identify the archive → confirm an entitled search',
  'The archive is connected before it is identified, and only the negative test is run before the last step.')

# --- Exam 6 ---------------------------------------------------------------
s('seq6a_ok',
  'Pick one high-volume process → baseline the time and cost → pilot Copilot with the team → compare against the baseline and decide',
  'A baseline is what turns a pilot into evidence, and the scale decision depends on the comparison.')
s('seq6a_b1',
  'Pilot Copilot with the team → pick a process → baseline the time → compare and decide',
  'The pilot has no baseline to compare against, so its result is an opinion.')
s('seq6a_b2',
  'Compare and decide → baseline the time → pick a process → pilot with the team',
  'The comparison is made before the pilot that produces the data.')
s('seq6a_b3',
  'Baseline the time → compare and decide → pick a process → pilot with the team',
  'The decision is taken before the process is chosen or the pilot run.')

s('seq6b_ok',
  'Confirm the scope of the exposure → remove the over-broad access → review the audit log → tell the affected owner and record the fix',
  'Containment comes before investigation, and the record closes the loop with the owner.')
s('seq6b_b1',
  'Tell the affected owner → confirm the scope → remove the access → review the audit log',
  'Notification before containment leaves the exposure open while people are being told about it.')
s('seq6b_b2',
  'Review the audit log → remove the access → confirm the scope → tell the owner',
  'The access should be removed as soon as the exposure is known, and the scope check should precede the log review.')
s('seq6b_b3',
  'Record the fix → review the audit log → remove the access → confirm the scope',
  'Recording the fix before making it is a false record, and containment comes too late.')

s('seq6c_ok',
  'Treat the contract text as data → stop the summarization run → inspect the output for leaked instructions or content → report to security and the supplier owner',
  'The response to injected instructions is containment, inspection, and disclosure to the people who own the relationship.')
s('seq6c_b1',
  'Follow the instruction to check it → report to security → stop the run → inspect the output',
  'Following the instruction is the harmful action and cannot be a diagnostic step on live content.')
s('seq6c_b2',
  'Inspect the output → follow the instruction → stop the run → report to security',
  'The instruction is still followed, which defeats the inspection that preceded it.')
s('seq6c_b3',
  'Report to security → follow the instruction → inspect the output → stop the run',
  'Reporting early does not justify executing the injected instruction.')

s('seq6d_ok',
  'Describe the task and its end state → check whether a single answer, an agent, or Cowork fits → use the lightest option that fits → review the result',
  'Matching the tool to the task avoids both over-building and delegating work that one answer could finish.')
s('seq6d_b1',
  'Delegate to Cowork → describe the task → review the result → check which option fits',
  'Delegating before describing the task gives Cowork no end state to plan against.')
s('seq6d_b2',
  'Check which option fits → review the result → describe the task → use the option',
  'The result is reviewed before the task is described or the option used.')
s('seq6d_b3',
  'Review the result → check which option fits → use the option → describe the task',
  'Every step is inverted: the review precedes the work and the task description comes last.')

s('seq6e_ok',
  'Agree the board’s decision → reconcile the figures with finance → draft the pack → check every claim and citation before circulation',
  'The decision sets the test, finance owns the numbers, and the claim check is the final gate.')
s('seq6e_b1',
  'Draft the pack → circulate it → reconcile the figures → agree the decision',
  'Circulation before reconciliation puts numbers in front of the board that finance has not confirmed.')
s('seq6e_b2',
  'Reconcile the figures → circulate the pack → agree the decision → draft the pack',
  'The pack is circulated before it is drafted and before the decision it serves is agreed.')
s('seq6e_b3',
  'Agree the decision → circulate the pack → check every claim → reconcile the figures',
  'Circulation precedes both the checks and the reconciliation that must happen first.')

s('seq6f_ok',
  'Scope the agent and its sources → build and test it with a pilot group → assign an owner and review cadence → publish it to the wider organization',
  'A tested agent with a named owner is what can be published safely; broad publication is the last step.')
s('seq6f_b1',
  'Publish it to the organization → build and test it → scope the agent → assign an owner',
  'Publishing a scoped but untested agent exposes errors to everyone at once.')
s('seq6f_b2',
  'Assign an owner → publish the agent → build and test it → scope the agent',
  'The agent is published before it is scoped, built, or tested.')
s('seq6f_b3',
  'Build and test it → publish it → scope the agent → assign an owner',
  'Testing without a defined scope cannot establish that the agent is fit for its purpose.')

s('seq6g_ok',
  'Define the recurring task and owner → run it once and check the output → schedule it → review the first scheduled run and the run history',
  'One proven run and a named owner are the preconditions for a schedule; the first scheduled run is checked.')
s('seq6g_b1',
  'Schedule it → run it once → define the task and owner → review the run history',
  'A schedule before the task and owner are defined creates an unowned recurring job.')
s('seq6g_b2',
  'Review the run history → schedule it → run it once → define the task',
  'There is no run history to review before the task has run.')
s('seq6g_b3',
  'Run it once → schedule it → define the task and owner → review the first scheduled run',
  'The task is defined after the run and the schedule, so neither can be evaluated against it.')

s('seq6h_ok',
  'Read the case brief → review the plan Cowork proposes → check each intermediate output → approve the final deliverable',
  'A case brief, a plan, checkpoints, and a final approval are the minimum controls for delegated case work.')
s('seq6h_b1',
  'Approve the final deliverable → read the brief → review the plan → check the outputs',
  'Approval is given before any work or evidence exists.')
s('seq6h_b2',
  'Review the plan → check the outputs → read the brief → approve the deliverable',
  'The plan is reviewed before the brief that defines success, and approval comes last with no checkpoint evidence.')
s('seq6h_b3',
  'Check the intermediate outputs → approve the deliverable → read the brief → review the plan',
  'Checkpoints are inspected without a brief or plan, so there is no standard to check against.')

# --- Additional candidate orderings reused across the later exams --------
s('seq2i_ok',
  'Classify the client data → confirm the permitted processing location → restrict the prompt to the approved source set → review the output before it leaves the firm',
  'Classification and location are settled before the content is used, and the review happens before the result is shared.')
s('seq2i_b1',
  'Review the output before it leaves the firm → classify the data → confirm the processing location → restrict the source set',
  'The review is placed before the work it reviews, and the location question is answered too late.')
s('seq2i_b2',
  'Restrict the source set → review the output → classify the data → confirm the processing location',
  'Restricting sources helps, but the output is reviewed and the data classified in the wrong order.')
s('seq2i_b3',
  'Confirm the processing location → review the output → restrict the source set → classify the data',
  'Reviewing before the prompt is built and before classification leaves the control unproven.')

s('seq2j_ok',
  'Define the delegated outcome → review the proposed plan → check each output against the brief → approve the final pack',
  'The outcome shapes the plan, each output is checked against the brief, and approval comes after the evidence.')
s('seq2j_b1',
  'Approve the final pack → define the delegated outcome → review the proposed plan → check each output',
  'Approval comes first, so the signature is given before any evidence exists.')
s('seq2j_b2',
  'Review the proposed plan → check each output → define the delegated outcome → approve the final pack',
  'The plan and outputs are reviewed before the outcome that defines success has been written.')
s('seq2j_b3',
  'Check each output → approve the final pack → define the delegated outcome → review the proposed plan',
  'The outputs are checked with no brief and approved before the plan is reviewed.')

s('seq2k_ok',
  'Agree the wording with the practice group → test it on three live matters → save it with a descriptive title → share it from the library',
  'The practice group owns the wording, the live matters prove it, and the library is how everyone gets the same version.')
s('seq2k_b1',
  'Share it from the library → agree the wording → test it on three live matters → save it',
  'Sharing before the wording is agreed and tested gives every team an unproven template.')
s('seq2k_b2',
  'Test it on three live matters → share it from the library → agree the wording → save it',
  'The test has no agreed standard to test against, and sharing precedes saving.')
s('seq2k_b3',
  'Save it with a descriptive title → share it from the library → agree the wording → test it',
  'Saving and sharing come before both the agreement and the test that would justify them.')

s('seq3i_ok',
  'Name the audience and the decision → draft the prompt with the approved sources → test it on a live case → save and share the tested version',
  'The audience and decision define the prompt, a live case tests it, and only then is it published to the team.')
s('seq3i_b1',
  'Save and share the tested version → name the audience → test it on a live case → draft the prompt',
  'Publishing precedes both the draft and the test, so the team receives an unproven prompt.')
s('seq3i_b2',
  'Test it on a live case → save and share the version → name the audience → draft the prompt',
  'The test has no defined audience or decision to test against.')
s('seq3i_b3',
  'Draft the prompt with the approved sources → save and share the version → test it on a live case → name the audience',
  'The prompt is shared before the live test, and the audience is named last.')

s('seq6i_ok',
  'Agree the standard wording with the business owner → test it on live cases → save it in the library → review it whenever the underlying policy changes',
  'Ownership, a live test, and a scheduled review keep a standard prompt from becoming a stale template.')
s('seq6i_b1',
  'Review it whenever the policy changes → share it → test it on live cases → agree the wording',
  'Reviewing before the prompt exists and sharing before the test gives every team an unproven template.')
s('seq6i_b2',
  'Share it across the group → agree the wording → test it on live cases → save it',
  'Sharing first spreads wording that nobody has agreed or tested.')
s('seq6i_b3',
  'Save it in the library → review it when policy changes → agree the wording → test it',
  'The saved prompt is never tested and the review happens before the wording is agreed.')

s('seq6j_ok',
  'Confirm the recurring need → assign an owner for the output → test the run once → schedule it and check the first live result',
  'A named owner and one proven run are the preconditions for putting a deliverable on a schedule.')
s('seq6j_b1',
  'Schedule it → confirm the recurring need → test the run once → assign an owner',
  'The schedule exists before the need is confirmed or anyone owns the output.')
s('seq6j_b2',
  'Assign an owner → schedule it → test the run once → confirm the recurring need',
  'Scheduling before the need is confirmed creates a recurring output nobody asked for.')
s('seq6j_b3',
  'Test the run once → schedule it → confirm the recurring need → assign an owner',
  'The test cannot show whether the output matters before the need and owner are settled.')
