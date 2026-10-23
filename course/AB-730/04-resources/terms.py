"""Original AB-730 option labels and explanations.

Every option in a question is a key in TERMS. The label is what the learner
reads; the meaning is the per-option rationale used in the CSV explanations.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: fundamentals, context, risk, and data protection -------------
t('tntboundary', 'Keep prompts, grounding, and responses inside the Microsoft 365 tenant',
  'Copilot processes the request inside the tenant boundary, so organizational content is not sent to a public consumer service.')
t('notraining', 'Rely on the contractual commitment that tenant data is not used to train foundation models',
  'Microsoft states that prompts, responses, and Graph content are not used to train the underlying models, which is a privacy control rather than an accuracy control.')
t('workiq', 'Ground the answer in Work IQ signals such as mail, files, chats, and meetings',
  'Work IQ supplies the business context of the signed-in user, which is what turns a generic answer into one about this account or project.')
t('webon', 'Use web grounding for current public information',
  'Web grounding adds public, current sources, which helps with market or competitor questions and cannot answer questions about internal records.')
t('appctx', 'Use the open app context, such as the current email, file, or meeting',
  'The open item supplies the subject, recipients, and history without the user retyping them, and it keeps the answer tied to the document in front of them.')
t('graphscope', 'Ground the answer in Microsoft 365 content the signed-in user can already open',
  'Grounding inherits the user’s existing permissions, so the answer can only draw on content that user is entitled to see.')
t('chat', 'Use Microsoft 365 Copilot Chat for the request',
  'Copilot Chat is the general chat surface for a one-off request and can use web and work grounding without a dedicated agent.')
t('agentpre', 'Use a prebuilt agent designed for that task',
  'A prebuilt agent already packages the instructions, skills, and sources for a known task, so no build work is needed.')
t('cowork', 'Delegate the multi-step task to Microsoft Copilot Cowork',
  'Cowork plans and carries out a sequence of steps across apps, which suits a task with several dependent actions rather than a single answer.')
t('inapp', 'Complete the task in the Microsoft 365 app that holds the content',
  'Working in the app keeps the source, formatting, and permissions in place and puts the result where the user will use it.')
t('notebook', 'Keep the sources and notes in a Copilot Notebook',
  'A Notebook holds a persistent set of sources and the analysis built on them, so later questions do not restart from nothing.')
t('pages', 'Move the working draft into Copilot Pages',
  'Pages gives the draft a shareable, editable home that people and Copilot can work on together.')
t('researcher', 'Use Researcher for a cited, multi-source investigation',
  'Researcher performs a deeper multi-step investigation and returns citations, which suits a question that needs evidence from many sources.')
t('analyst', 'Use Analyst to analyse a data file',
  'Analyst runs structured analysis over an uploaded data set and shows its working, which suits quantitative questions over a file.')
t('create', 'Ask Copilot to create the content from a short instruction',
  'A direct creation request is the fastest route when the user can describe the deliverable and will edit the result.')

t('fluentverify', 'Treat the output as a draft and verify every factual claim',
  'Fluent text is not evidence: the model can produce a confident sentence that no source supports, so claims need checking before use.')
t('injection', 'Treat instructions inside retrieved or uploaded content as untrusted data',
  'Prompt injection hides instructions in a document or web page; the design must treat that text as content to summarize, never as a command to follow.')
t('overrely', 'Keep a named person accountable for the decision',
  'Accountability cannot be delegated to a model, so a person must own the judgement and be able to explain it.')
t('citecheck', 'Open each cited source and confirm the passage supports the claim',
  'A citation only helps if someone follows it; checking the passage is what catches a real-looking reference attached to the wrong statement.')
t('humanreview', 'Send the output to a qualified reviewer before it is used',
  'A reviewer with domain knowledge catches errors that the author of the prompt cannot see, and the review step must happen before the output has consequences.')
t('fallback', 'Add a refusal and hand-off when nothing relevant is retrieved',
  'A grounded assistant that always answers will invent content when retrieval returns nothing; an explicit refusal keeps the gap visible.')
t('evalset', 'Test prompt or model changes against a fixed evaluation set',
  'A stable set of representative questions turns quality into a comparable number, which is the only way to know whether a change helped.')
t('redteam', 'Test the assistant with adversarial prompts before launch',
  'Adversarial testing finds the prompts that extract restricted content or bypass instructions before real users do.')
t('feedback', 'Add a user feedback and correction loop',
  'Capturing corrections shows where the assistant is wrong in real use and gives the owner a queue of fixes.')
t('groundonly', 'Restrict answers to the approved internal corpus',
  'Limiting the corpus reduces invented content but leaves the assistant unable to answer anything the corpus does not cover.')
t('weboff', 'Turn off web grounding for the sensitive workflow',
  'Removing web access prevents public or malicious pages from entering the context when only internal material should be used.')
t('datamin', 'Remove unnecessary personal data before prompting',
  'Data minimization reduces what is exposed in the prompt and what may be retained, without changing the business question.')
t('classify', 'Classify the data before deciding where it may be processed',
  'A sensitivity classification decides which tools and locations are allowed, so it must come before the data is uploaded anywhere.')
t('oversharefix', 'Fix source permissions before Copilot is enabled on the site',
  'Copilot surfaces what a user can already open, so permissions that are too broad become visible at machine speed once the site is grounded.')
t('sensitivity', 'Apply sensitivity labels that restrict or encrypt the content',
  'Labels travel with the item and are enforced by the service, so labelled content stays restricted even when Copilot encounters it.')
t('dlp', 'Apply a data loss prevention policy to sensitive content in prompts and responses',
  'A DLP policy blocks or audits sensitive content moving through Copilot, which addresses the exfiltration path rather than the prompt wording.')
t('audit', 'Review Copilot interaction audit logs',
  'Audit records show who prompted what and when, which supports investigation after an incident rather than preventing one.')
t('retention', 'Set retention and residency rules for prompts and outputs',
  'Prompts and responses become records under some regimes, so how long they are kept and where they live must be decided in advance.')
t('residency', 'Confirm the data residency of the service before loading the data',
  'Residency commitments decide whether the content may legally be processed in that tenant and region at all.')
t('permtrim', 'Rely on permission trimming so results match the user’s existing access',
  'Permission trimming filters grounded content to what the user may open, which prevents the assistant becoming a discovery tool.')
t('accessreview', 'Run a site access review before rollout',
  'An access review removes the stale groups and broad links that would otherwise be exposed through grounding.')
t('encryptfile', 'Password-protect each document before it is stored in SharePoint',
  'Password protection blocks the service from reading the file at all, so Copilot cannot ground on it and users lose search.')
t('allusers', 'Grant every employee read access so answers are never incomplete',
  'Broad read access fixes completeness by removing the control that keeps restricted content restricted, which is exactly the oversharing risk.')
t('blockcopilot', 'Block Copilot for the whole tenant until every site is reviewed',
  'A tenant-wide block prevents the exposure but also removes the tool from teams whose content is already well governed.')
t('thirdparty', 'Paste the content into a consumer AI service for a second opinion',
  'A consumer service sits outside the tenant boundary and its terms, so organizational content may leave the protected environment.')
t('personalaccount', 'Use a personal account so the work is not tied to the corporate tenant',
  'A personal account moves the content outside the organization’s controls, audit, and retention, which makes the exposure worse.')
t('modelmemory', 'Assume the model remembers previous conversations with other users',
  'Models do not share one memory across users; assuming they do leads to over-blocking, not to a privacy control.')
t('sharepointlink', 'Share a “anyone with the link” URL so colleagues can open the source',
  'An anonymous link removes the permission check, so the content can surface for people who were never entitled to it.')

# --- Domain 2: prompts and chats ------------------------------------------
t('rolegol', 'State the role, the goal, and the audience',
  'Naming who the output is for and what it must achieve gives the model the criteria to satisfy, not just a topic.')
t('background', 'Supply the background facts the answer must use',
  'Relevant facts in the prompt reduce guessing; a prompt that supplies them does not rely on the model’s general assumptions.')
t('constraints', 'State explicit constraints and exclusions',
  'Constraints such as length, jurisdiction, or “do not include pricing” remove whole classes of wrong answers.')
t('format', 'Specify the output format, length, and tone',
  'A named structure such as a five-row table or a 150-word summary makes the result usable without a rewrite.')
t('examples', 'Include two or three approved examples in the prompt',
  'Examples convey tone and structure far more reliably than a longer description of them.')
t('refsources', 'Reference the exact files, meetings, or people to use',
  'Pointing at specific sources narrows the search and keeps the answer anchored in the material the user intends.')
t('iterate', 'Revise the prompt and rerun it with the gaps named',
  'A first response shows which instruction was ambiguous, so the next prompt can fix that rather than starting over.')
t('clarify', 'Ask Copilot to ask clarifying questions before answering',
  'A clarifying turn surfaces a missing audience or constraint before the model commits to a structure.')
t('chain', 'Break the task into ordered steps and confirm each one',
  'Splitting a large request into steps makes each output checkable and stops one weak assumption carrying through the whole answer.')
t('shorten', 'Remove unrelated instructions and shorten the prompt',
  'A prompt carrying several unrelated asks dilutes attention; trimming it can improve quality without adding anything.')
t('oneprompt', 'Put every requirement into one longer instruction',
  'A single long instruction hides the requirement that matters among many, and the model may satisfy the easy ones only.')
t('moreinstructions', 'Add another paragraph of instructions about the same requirement',
  'Repeating a requirement in prose rarely fixes it; an example or a structural constraint usually does.')
t('modelauto', 'Leave model selection on automatic',
  'Automatic selection matches the model to the request, which is the sensible default when the task is ordinary.')
t('modelreason', 'Choose the reasoning model for the complex analytical task',
  'A reasoning model spends more effort on multi-step analysis, which pays off when the task needs a chain of inference.')
t('modelfast', 'Choose the fast model for the short routine request',
  'A fast model answers a simple rewrite or lookup quickly and at lower cost than a reasoning model.')
t('modelbig', 'Choose the largest available model for every request',
  'Using the largest model for routine work adds cost and latency without improving a simple answer.')
t('save', 'Save the prompt to the prompt library',
  'Saving puts the prompt where it can be reused and shared, instead of living in one person’s chat history.')
t('savetitle', 'Save it with a descriptive title and a note on the task it serves',
  'A descriptive title and note are how a colleague finds the right prompt later among many similar ones.')
t('savechat', 'Keep the prompt only in the chat where it was typed',
  'A prompt left in one chat is hard to find again and cannot be reused consistently by the team.')
t('schedule', 'Schedule the prompt to run at a set time and cadence',
  'Scheduling turns a repeated manual request into a dependable recurring output, such as a Monday pipeline summary.')
t('scheduleonce', 'Run it once and rely on people to remember the cadence',
  'Relying on memory is what causes the weekly summary to be missed when the owner is away.')
t('scheduleall', 'Schedule every saved prompt in the library to run daily',
  'Scheduling everything creates noise and cost; a cadence should match how often the answer actually changes.')
t('share', 'Share the prompt with the team from the library',
  'A shared prompt gives everyone the same tested wording, so output does not vary by who typed it.')
t('sharelink', 'Send the chat link so the team can copy the prompt themselves',
  'A chat link shares one conversation and is not a maintained prompt; the team has to reconstruct the wording each time.')
t('memoryon', 'Turn on memory so standing preferences persist across chats',
  'Memory carries stable preferences such as tone and format into later conversations, which saves repeating them.')
t('memoryoff', 'Turn off memory for the confidential engagement',
  'When the work is confidential, persisting details beyond the conversation is a disclosure risk, so memory should be off.')
t('memorycheck', 'Review and clear saved memories before the meeting',
  'Saved memories can carry outdated or sensitive facts into a new context, so they should be reviewed when the context changes.')
t('instructions', 'Set custom instructions for tone and standing rules',
  'Custom instructions apply the same voice and guardrails to every chat without repeating them in each prompt.')
t('rename', 'Rename the chat to describe its topic',
  'A descriptive name is what makes the chat findable weeks later, when the first line no longer identifies it.')
t('find', 'Search chat history by keyword or topic',
  'Chat search looks across past conversations, which is faster than scrolling when the topic is known.')
t('pin', 'Pin the chat so it stays at the top of the list',
  'Pinning keeps an active piece of work in reach but does not help when the chat has already been lost among many.')
t('deletechat', 'Delete the chat when it is no longer needed',
  'Deleting removes the conversation from the history, which is the right action for a scratch chat or one holding content that should not persist.')
t('deleteall', 'Delete every chat from the last month to tidy up',
  'Bulk deletion removes work that may still be needed and is not a substitute for a retention policy.')
t('notebooksources', 'Add the engagement files and meetings as Notebook sources',
  'A Notebook keeps a fixed source set, so every question in the engagement is answered from the same material.')
t('notebookshare', 'Share the Notebook with the project team',
  'A shared Notebook gives the team one source set and one place where the analysis accumulates.')
t('notebookexport', 'Export the Notebook notes into the deliverable',
  'Exporting carries the working notes into the document where the audience will read them.')
t('notebookscratch', 'Keep everything in one long chat instead of a Notebook',
  'A long chat loses track of which sources applied when, and later questions drift from the original material.')
t('librarycopy', 'Copy an approved prompt from the library instead of rewriting it',
  'Reusing an approved prompt keeps wording and guardrails consistent across the team.')

# --- Domain 3: content and collaboration ----------------------------------
t('graphconnector', 'Add a Graph connector for the third-party repository',
  'A Graph connector indexes external content into Microsoft 365 so Copilot can ground on it alongside mail and files.')
t('federated', 'Use a federated connector that queries the source at answer time',
  'A federated connector leaves the data in place and queries it live, which suits content that must not be copied.')
t('connectoracl', 'Set the connector ACLs so only entitled users see the connected items',
  'Connector ACLs carry the source permissions into grounding; without them the external index becomes a leak.')
t('exportdata', 'Export the source into Word before prompting',
  'A static export is a snapshot that goes stale and loses the source permissions, so it is a fallback rather than a connector.')
t('movefiles', 'Copy the whole repository into one SharePoint site',
  'Copying duplicates content and creates a second version to govern, without solving the permission question.')
t('imagegen', 'Generate the image in Copilot',
  'Image generation creates a new visual from a description, which suits an illustration rather than an exact chart of real data.')
t('designer', 'Use Designer to produce the visual from the draft',
  'Designer turns text and structure into a designed visual quickly, with brand templates where they are configured.')
t('chart', 'Ask Copilot to build the chart from the selected range',
  'Charting the actual range keeps the visual tied to the data, so the numbers can be traced back.')
t('screenshot', 'Screenshot an old chart and paste it into the deck',
  'A screenshot carries no live data, cannot be checked, and silently becomes wrong when the source changes.')
t('worddraft', 'Draft the document in Word from the approved sources',
  'Drafting in Word keeps citations and formatting in the document the reviewer will open.')
t('excelanalyze', 'Analyse the workbook in Excel with Copilot',
  'Excel analysis runs against the workbook itself, so formulas and ranges remain the evidence for the result.')
t('pptdesign', 'Ask Copilot in PowerPoint to build the deck from the document',
  'Building from the approved document keeps the deck consistent with the narrative that was already reviewed.')
t('crossapp', 'Carry the content across Word, Excel, and PowerPoint in one flow',
  'A cross-app flow reuses the same reviewed content instead of letting each document drift.')
t('workiqinsight', 'Ask for insights across the user’s mail, meetings, and files',
  'Cross-source insight finds the pattern that no single document contains, such as a recurring delay across projects.')
t('validategoal', 'Check the output against the stated business goal and audience',
  'A polished output can still miss the goal, so the check is against the brief rather than against readability.')
t('factchecknums', 'Reconcile every generated figure with the source workbook',
  'Numbers are the easiest thing for a model to restate incorrectly, so each figure needs a trace to the source.')
t('brandcheck', 'Check the output against the brand and tone guide',
  'Brand checks catch voice and asset errors that a factual review would pass.')
t('signoff', 'Require the business owner to sign off before publication',
  'Sign-off puts a named owner behind the content and is the last control before it reaches an audience.')
t('publishnow', 'Publish immediately because the draft reads well',
  'Fluent prose is not evidence of correctness, and publishing removes the chance to catch an error.')
t('meetingprep', 'Ask for a pre-meeting brief on attendees, history, and open items',
  'A pre-read built from mail and files means the meeting starts with context rather than a recap of the last one.')
t('meetingprepblind', 'Walk in without preparation and rely on the discussion',
  'Skipping preparation leaves the participant dependent on others to supply the history the tool could have summarized.')
t('facilitator', 'Add the Facilitator agent to the meeting',
  'Facilitator keeps the agenda, tracks time, and records decisions and actions during the meeting.')
t('facilitatornotes', 'Take manual notes and tidy them afterwards',
  'Manual notes compete with participation and are the first thing dropped when the discussion speeds up.')
t('catchup', 'Use real-time catchup after rejoining late',
  'Real-time catchup summarizes what was said while the participant was away, so they can rejoin the discussion rather than the transcript.')
t('catchupask', 'Ask a colleague to repeat the last twenty minutes',
  'Asking a colleague works once, interrupts the meeting, and loses the exact wording of a decision.')
t('recap', 'Use Intelligent recap after the meeting',
  'Intelligent recap produces a summary, decisions, and action items with speakers and timestamps from the recording.')
t('recapactions', 'Pull the actions and owners out of the recap into the tracker',
  'Extracting actions into the tracker is what turns a summary into follow-through.')
t('recaptrust', 'Forward the recap as the official minutes without review',
  'A recap is a generated summary of a recording; decisions and owners still need checking before they become minutes.')
t('pagesedit', 'Collaborate on the draft in Copilot Pages',
  'Pages lets people and Copilot edit the same artifact, so the draft stops being copied between documents.')
t('pagesshare', 'Share the Page with the working group',
  'Sharing the Page keeps one live version instead of a set of attachments.')
t('pagestrack', 'Keep the Page as the single live version of the deliverable',
  'One live Page removes the “latest final” problem in a working group.')
t('pageemail', 'Email the draft as an attachment to each reviewer',
  'Attachments fork the document, and the reviewed changes have to be merged by hand.')

# --- Domain 4: agents ------------------------------------------------------
t('agentstore', 'Find a prebuilt agent in the agent store',
  'The agent store lists agents that Microsoft or the organization already published, which is the fastest route to a known task.')
t('agentbuiltin', 'Use the agent that is already available in the Copilot experience',
  'An in-product agent such as Researcher or Analyst needs no deployment and is appropriate when it matches the task.')
t('customagent', 'Build a scoped custom agent on the department’s content',
  'A custom agent is justified when the task needs specific sources, instructions, or a workflow that no prebuilt agent covers.')
t('customagentowner', 'Assign an owner and a review cadence to the custom agent',
  'A custom agent drifts as content changes, so someone must own its knowledge and instructions.')
t('prebuiltfirst', 'Start with the prebuilt agent and extend only if it falls short',
  'Trying the prebuilt option first avoids build and maintenance work when it already meets the need.')
t('buildfirst', 'Build a custom agent before trying the prebuilt option',
  'Building first spends effort on a solution that may already exist, and adds an asset that must be maintained.')
t('filter', 'Filter the chat list by agent',
  'Filtering by agent separates the conversations held with a specific agent from the rest of the chat history.')
t('agentchat', 'Start the request from inside the agent',
  'Starting inside the agent applies its instructions and sources to the conversation from the first message.')
t('agentanychat', 'Ask in a general chat and mention the agent by name',
  'Naming an agent in a general chat does not apply that agent’s configuration, so the answer may not use its sources.')
t('coworktask', 'Give Cowork the multi-step task with a clear end state',
  'Cowork plans across steps, so the request needs an outcome and constraints rather than a single instruction.')
t('coworkskill', 'Select the prebuilt skill for the step',
  'A prebuilt skill packages a known procedure, such as preparing a briefing, so Cowork does not improvise it.')
t('customskill', 'Create a custom skill for the organization’s own procedure',
  'A custom skill encodes a procedure that is specific to the organization and not covered by a prebuilt skill.')
t('coworkplan', 'Review Cowork’s plan before it acts',
  'The plan shows which steps and sources it intends to use, which is the point to catch a wrong interpretation cheaply.')
t('coworkprogress', 'Check progress at each checkpoint',
  'Checking at checkpoints catches drift while the work is still cheap to correct.')
t('coworkstop', 'Stop the run when the plan drifts from the brief',
  'Stopping a run that has left the brief prevents a wrong result from spreading into later steps.')
t('coworkapprove', 'Approve the next step only after checking the output',
  'Approval is a control only if the approver has looked at the artifact the step produced.')
t('coworkauto', 'Let Cowork run to completion and review only the final output',
  'Reviewing only at the end means an early wrong assumption is carried through every later step.')
t('coworksched', 'Schedule the task to repeat on a cadence',
  'A recurring deliverable such as a weekly brief can be scheduled instead of requested each time.')
t('coworklimit', 'Check the known limitations before delegating regulated work',
  'Known limitations such as unsupported file types or actions decide whether the task can be delegated at all.')
t('coworkperm', 'Confirm the run acts with the user’s own permissions',
  'Cowork must not exceed the requesting user’s access, or delegation becomes a privilege escalation.')
t('coworkdata', 'Keep confidential inputs out of the delegated run',
  'Confidential material may be unsuitable for a delegated workflow, so it should be excluded rather than trusted to the agent.')
t('coworkaudit', 'Review the run history and outputs before sign-off',
  'The run history shows what the agent did, which is the evidence a reviewer needs before approving the result.')
t('coworkhandoff', 'Hand the final output back to a person for approval',
  'A person remains accountable for the outcome, so the delegated run ends in a human decision.')
t('coworkscope', 'Narrow the task to one deliverable',
  'A narrow task is easier to plan, check, and correct than a broad request that combines several deliverables.')
t('coworkparallel', 'Ask Cowork to do everything at once without a plan',
  'Without a plan there is no checkpoint to catch a wrong interpretation before it affects later steps.')
t('agentpublic', 'Publish the custom agent to everyone in the organization on day one',
  'Publishing broadly before the agent’s sources and answers are reviewed exposes errors at scale.')

# Candidate orderings for the sequencing items are kept in their own module so
# the action-option bank stays readable.
from sequences import SEQUENCES

for _key, _value in SEQUENCES.items():
    if _key in TERMS:
        raise ValueError(f'Duplicate term: {_key}')
    TERMS[_key] = _value
