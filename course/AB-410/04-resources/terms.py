"""Option bank for AB-410: one label and one meaning per answer or distractor.

Keys are stable and referenced by questions/*.txt. Adding an option means
adding it here first; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ---------------------------------------------------------------- domain 1
# Requirements, agents, extensibility, environment and ALM choices.
t('reqmap', 'Map each requirement to the Power Platform component that fits it',
  'Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small.')
t('prototypefirst', 'Build a working prototype in a week and let the business react to it',
  'A prototype answers questions sooner, but it does not settle which component should own the logic.')
t('oneapp', 'Deliver every requirement as a single model-driven app',
  'One app for everything widens access and makes the smallest change a release of the whole solution.')
t('customfirst', 'Start with a custom connector and a plug-in for the first version',
  'Code-first components raise the support and upgrade cost before the requirement is understood.')
t('builtinagent', 'Adopt the built-in agent that already covers the task',
  'A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent.')
t('customagent', 'Build a custom Copilot Studio agent for every requirement',
  'A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process.')
t('agentlessflow', 'Model the process as a cloud flow with no agent at all',
  'A deterministic process belongs in a flow; adding an agent adds a language model where none is needed.')
t('lowaftercode', 'Ship a code-first component now and replace it with low-code later',
  'A deliberate later replacement rarely happens, and meanwhile two implementations must be maintained.')
t('pcfcontrol', 'Build a Power Apps component framework control',
  'PCF is the right answer when the requirement is a visual or interaction the standard control cannot express.')
t('plugincode', 'Write a Dataverse plug-in in C#',
  'A plug-in is for server-side logic that must run on every write, not for a screen interaction.')
t('jswebresource', 'Add a JavaScript web resource to the form',
  'A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere.')
t('envtype', 'Choose the environment type that matches the data boundary and the licence',
  'Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience.')
t('defaultenv', 'Build in the default environment because everyone already has access',
  'The default environment has the widest membership and the least governance, which is where a regulated solution should not start.')
t('trialenv', 'Use the trial environment for production after the pilot',
  'A trial environment expires, taking the solution and its data with it.')
t('sandboxprod', 'Run production workloads in a sandbox environment',
  'A sandbox is for build, test, and acceptance; it is not a production target.')
t('prodenvbuild', 'Do all building in the production environment to avoid deployment',
  'Building in production removes the test step and puts every unfinished change in front of users.')
t('oneenv', 'Share a single environment between development and production',
  'One environment cannot separate an unfinished change from live data.')
t('solutionaware', 'Package the customizations in a solution before moving them',
  'A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment.')
t('unmanagedprod', 'Import unmanaged customizations directly into production',
  'Unmanaged layers in production cannot be cleanly removed or upgraded.')
t('publisher', 'Define the solution publisher and prefix once, before the first table',
  'The prefix is baked into every schema name and is expensive to change after data exists.')
t('managedprod', 'Promote a managed solution to test and production',
  'A managed solution is locked, so it can be upgraded and removed predictably.')
t('unmanageddev', 'Keep unmanaged solutions in the development environment',
  'Development is where the editable, unmanaged layer belongs; it is exported and imported as managed further along.')
t('patchsol', 'Ship a patch to the managed solution',
  'A patch delivers a small fix against the same parent version without a full re-import.')
t('cloneenv', 'Clone the environment each time instead of using a pipeline',
  'Cloning copies data as well as configuration and is not a repeatable deployment path.')
t('pipeline', 'Use Power Platform pipelines to deploy between environments',
  'A pipeline records the deployment and runs the same solution through each stage.')
t('devopsexport', 'Automate export and import with an Azure DevOps pipeline',
  'The automation is not the hard part; the solution boundary and the deployment order are.')
t('solutionlayers', 'Review the solution layers before overwriting a component',
  'Layers show which solution last changed a component, which is how an unexplained behaviour is traced.')
t('deletesolution', 'Delete the managed solution to clear a component conflict',
  'Deleting the carrying solution removes the component and everything that depends on it.')

# Tables, columns, relationships.
t('dataworkspace', 'Create the table in the Dataverse data workspace',
  'The data workspace lets a maker model tables and relationships without leaving the app-building flow.')
t('sharepointlist', 'Keep the records in a SharePoint list and skip Dataverse',
  'A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them.')
t('standardtable', 'Extend the standard table instead of creating a duplicate',
  'Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect.')
t('customtable', 'Create a custom table for the new business entity',
  'A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one.')
t('activitytable', 'Store the interactions in the Activity table',
  'Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship.')
t('tableprops', 'Configure table properties such as ownership and auditing',
  'Ownership decides who can see a row and auditing decides whether its history survives an investigation.')
t('auditon', 'Enable auditing on the tables that hold regulated data',
  'Auditing records who changed which column and when, which is what an audit asks for.')
t('choicecol', 'Add a choice column for the fixed set of options',
  'A choice constrains input to the approved list and renders as a dropdown on every form.')
t('globalchoice', 'Use a global choice so several tables share one option list',
  'One global choice keeps the list consistent instead of drifting across tables.')
t('lookupcol', 'Use a lookup column instead of storing the name as text',
  'A lookup carries the relationship, so the related record can be filtered, secured, and rolled up.')
t('textdup', 'Store the account name as text so the form stays simple',
  'A copied name cannot be joined, renamed, or secured with its source record.')
t('moneycol', 'Use a currency column with the record currency',
  'A currency column keeps the amount and its currency together, which matters as soon as two currencies appear.')
t('decimalcol', 'Use a decimal column for an exact rate',
  'A decimal avoids the rounding drift that a floating-point column introduces in a rate.')
t('autonumber', 'Use an auto-number column for the case identifier',
  'An auto-number gives every record a readable, unique reference that users can quote.')
t('calcnow', 'Use a calculated column for the value that must never change',
  'A calculated column recomputes on read, so it cannot preserve a historic value.')
t('relationship', 'Configure a one-to-many relationship with a lookup on the child table',
  'The lookup on the child is what makes the parent select a record rather than a typed string.')
t('manytomany', 'Model the many-to-many link with a native N:N relationship',
  'A native N:N relationship handles the intersect table when neither side owns the other.')
t('parental', 'Set the relationship behaviour to parental so child records are removed with the parent',
  'Parental behaviour cascades the delete, which is correct when the child has no meaning alone.')
t('referential', 'Keep the relationship referential so child records survive the parent delete',
  'Referential behaviour leaves the children in place, which is what a shared dimension needs.')
t('promptcol', 'Configure a prompt column to generate text per row',
  'A prompt column produces a value for each record from a prompt, without a separate flow.')
t('rowsummary', 'Configure a row summary to summarize the record text',
  'A row summary condenses the record\'s own text, which is what a case recap needs.')
t('publicview', 'Create a public view for the shared filtered list',
  'A public view is available to everyone with access to the table, so the team sees the same list.')
t('personalview', 'Rely on each user\'s personal view of the table',
  'A personal view is private, so every new user starts from the default list instead.')
t('systemview', 'Change the system view so the list order suits the team',
  'The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about.')
t('mainform', 'Design the main form around the record the user opens',
  'The main form is the primary editing surface, so it carries the fields and tabs the role actually uses.')
t('quickcreate', 'Add a quick-create form for entry from a lookup',
  'A quick-create form lets a user create the related record without leaving the current one.')
t('cardform', 'Add the column to a card form on the main form',
  'A card form gives a compact editing surface for a handful of fields.')
t('secrole', 'Assign a security role that grants only the privileges the role needs',
  'A security role is how Dataverse decides create, read, write, and delete per table.')
t('teamowner', 'Assign the record to a team that the group owns',
  'Team ownership shares one queue of records without granting each member the owner role.')
t('businessunit', 'Move the user to another business unit to fix access',
  'Business units partition ownership; moving a user changes far more than one record.')
t('fieldsecurity', 'Use a field security profile for the sensitive column',
  'Field security is the only control that hides a column while the record stays visible.')
t('hierarchysec', 'Use manager hierarchy security for the sales team',
  'Hierarchy security grants a manager sight of the records their reports own.')

# ---------------------------------------------------------------- domain 2
t('formcolumns', 'Add the columns the role uses to the main form',
  'A form carries the working set of fields; everything else belongs in a tab or a view.')
t('formtabs', 'Organize the long form into tabs and sections',
  'Tabs keep a forty-column form scannable without hiding the fields behind a click.')
t('formscript', 'Hide the field with a JavaScript web resource',
  'A form script only affects that form, so the field is still editable everywhere else.')
t('viewfilter', 'Filter the view on the columns the team actually searches',
  'The filter decides which records appear, so it must match the question the list answers.')
t('viewcolumns', 'Choose the view columns before setting the filter',
  'The columns decide what is readable at a glance; the filter decides what is in the list.')
t('viewfetch', 'Write FetchXML for the view to get the exact rows',
  'FetchXML is powerful but bypasses the visual designer the next maker will use.')
t('genpage', 'Generate the page from a natural-language description, then refine it',
  'A generative page gets the layout close quickly, and the maker still owns the data bindings and access.')
t('genpublish', 'Publish the generated page without reviewing its data bindings',
  'An unreviewed page can bind to a table the audience should not read.')
t('genreplaceform', 'Replace the main form with the generated page',
  'A generative page complements the form; replacing it drops the scripting and business rules attached to it.')
t('appcompose', 'Add the forms, views, and pages to the app in the app designer',
  'The app designer decides which components the app exposes, so composition is a security-relevant choice.')
t('sitemap', 'Configure the navigation in the sitemap designer',
  'The sitemap is the app\'s menu, so it decides what a user can reach at all.')
t('appaccess', 'Share the app and assign the security role that backs it',
  'Sharing an app grants the app, and the role grants the data; both are needed.')
t('apponlyshare', 'Share the app only and rely on the app for access',
  'An app is not a permission boundary in Dataverse; the role is.')
t('chart', 'Create the chart on the view for the trend',
  'A chart bound to a view reuses that view\'s filter instead of duplicating it.')
t('dashboard', 'Add the chart and the views to a dashboard',
  'A dashboard composes several components so a manager sees the whole picture on one page.')
t('chartfetch', 'Build the chart in Power BI and embed it',
  'Embedding brings a second security model and a refresh dependency into the app.')
t('canvasfromdata', 'Generate a canvas app from the data source',
  'Generating from data gives working screens over the chosen tables immediately.')
t('canvastablet', 'Use the tablet layout for desk-based users',
  'The tablet layout gives the room a wide screen needs and stays readable on a laptop.')
t('canvasphone', 'Use the phone layout for field staff',
  'The phone layout controls the size and reach of controls on a handheld device.')
t('responsive', 'Use responsive containers so the layout adapts to the device',
  'Responsive containers reflow, so one app fits a phone and a desktop without two layouts.')
t('fixedwidth', 'Fix the layout to one pixel width so it always looks the same',
  'A fixed width is either cut off on a phone or stranded in the middle of a desktop.')
t('delegate', 'Write the filter so the data source performs the delegation',
  'Delegation sends the query to the source, so the app never downloads more rows than it can handle.')
t('localfilter', 'Filter in Power Fx after loading the rows into the app',
  'A local filter only sees the rows the app already fetched, so results silently truncate.')
t('a11ylabel', 'Add accessible labels and screen-reader text to the controls',
  'A control without a label is unusable with a screen reader, however clear it looks.')
t('colouronly', 'Convey status with colour alone',
  'Colour alone fails for a colour-blind user and for anyone reading the app in high contrast.')
t('namedformula', 'Define a named formula for the shared calculation',
  'A named formula evaluates once in the app and is reused by name instead of being copied.')
t('udf', 'Create a user-defined function for the reused expression',
  'A user-defined function takes parameters, which is what a repeated calculation with inputs needs.')
t('componentlib', 'Publish a component library for the shared header and controls',
  'A component library is the reusable, versioned home for a control that several apps must share.')
t('copyscreen', 'Copy the screen into every app that needs it',
  'A copy is a fork: the next design change has to be made in every app.')
t('globalvar', 'Use a global variable for the value that the whole app needs',
  'A global variable persists across screens, which is what a signed-in user\'s selection needs.')
t('contextvar', 'Use a context variable scoped to the screen',
  'A context variable lives with the screen, so it cannot leak into an unrelated part of the app.')
t('collection', 'Collect the rows into a collection for in-memory work',
  'A collection is the right tool for a shaped, temporary set that the app manipulates.')
t('clearme', 'Clear the collection when the screen changes',
  'An un-cleared collection keeps the previous user\'s rows in memory.')
t('iferror', 'Wrap the call in IfError and surface the message to the user',
  'IfError catches the failure and lets the app show a recoverable message instead of a silent blank.')
t('trace', 'Write a Trace message for the support team',
  'Trace records what happened in a session, which is what support needs after a failed save.')
t('monitor', 'Use Monitor to inspect the network call and the formula that fired',
  'Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed.')
t('teststudio', 'Run the app in Test Studio before publishing',
  'Test Studio captures the screens and formulas that a regression would break.')
t('agentcomponent', 'Add the Copilot Studio agent to the canvas app as a component',
  'The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge.')
t('agentiframenone', 'Build a second canvas app just to host the agent',
  'A second app multiplies the maintenance without adding capability.')
t('agentdirectapi', 'Call the agent\'s endpoint directly from Power Fx',
  'Calling the endpoint directly bypasses the agent component\'s authentication and telemetry.')

# ---------------------------------------------------------------- domain 3
t('triggerauto', 'Use an automated trigger on record creation',
  'An automated trigger runs without a user, which is what a background rule needs.')
t('triggermanual', 'Use a manually triggered flow from the app',
  'A manual trigger gives the user the decision about when the process runs.')
t('triggerschedule', 'Use a scheduled trigger for the nightly batch',
  'A schedule matches work that must run at a time rather than on an event.')
t('triggerhttp', 'Expose an HTTP request trigger with a signed URL',
  'An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret.')
t('triggerfilter', 'Trigger when a chosen column changes, with a filter condition',
  'A column filter stops the flow running for updates that cannot affect the outcome.')
t('triggerevery', 'Trigger on every update so nothing is missed',
  'A trigger on every update multiplies runs, cost, and the chance of a loop.')
t('connectorstandard', 'Use the standard Dataverse connector',
  'The standard connector is included in the base licence and covers Dataverse natively.')
t('connectorpremium', 'Use the premium connector the source requires',
  'A premium connector is justified when the data lives where no standard connector reaches.')
t('connectorcustom', 'Build a custom connector for the internal API',
  'A custom connector wraps an authenticated API so flows and apps can call it as a first-class action.')
t('connectorexcel', 'Copy the data into Excel to avoid a premium connector',
  'A manual copy becomes stale and moves the integration cost to a person.')
t('approvalstart', 'Start and wait for an approval',
  'The approval action pauses the run and resumes with the outcome, which is what a sign-off needs.')
t('approvaltype', 'Choose the approval type that matches the sign-off the process requires',
  'Approve or reject, everyone must approve, and first to respond are different business rules.')
t('approvalparallel', 'Send parallel approvals and require every response',
  'Everyone must approve is the right type when each stakeholder holds a veto.')
t('approvalsequence', 'Chain two approvals in sequence for the second-level sign-off',
  'A second approval after the first is how a value threshold adds a second approver.')
t('approvalemail', 'Send an email and treat silence as approval',
  'Silence is not a decision, and it leaves no auditable response.')
t('compose', 'Use Compose to shape the payload the next step consumes',
  'Compose builds the exact object the next action expects, which avoids mapping errors downstream.')
t('parsejson', 'Parse JSON so later steps can use the fields',
  'Parse JSON turns an opaque body into typed properties the designer can offer you.')
t('applytoeach', 'Apply to each over the returned rows',
  'Apply to each iterates the array, which is how one run processes many records.')
t('condition', 'Add a condition to branch on the status',
  'A condition is the explicit branch that makes the two paths readable in the run history.')
t('switch', 'Use a switch for the multi-way branch',
  'A switch keeps four or five outcomes readable where nested conditions become unreadable.')
t('dountil', 'Use Do until with a bounded count for the retry loop',
  'Do until repeats until the condition holds, and the count limit is what stops an infinite loop.')
t('unboundedloop', 'Loop until the record is found with no exit limit',
  'A loop with no bound can run until the run timeout, consuming the flow\'s quota.')
t('scope', 'Wrap the steps in a Scope so one error path handles the failures',
  'A scope groups steps so a single run-after configuration can catch any failure inside it.')
t('runafter', 'Configure run after so the failure path actually executes',
  'By default a step runs only on success, so the failure branch never fires without this setting.')
t('concurrency', 'Turn on concurrency control for the loop',
  'Concurrency runs iterations in parallel, which is faster but reorders side effects.')
t('flowtest', 'Test the flow with the real trigger payload',
  'A run started with the production-shaped payload is what proves the expressions resolve.')
t('runhistory', 'Read the run history to find the failed action and its inputs',
  'The run history shows each action\'s inputs and outputs, which is where the wrong value becomes visible.')
t('resubmit', 'Resubmit the failed run after the fix',
  'Resubmit replays the same inputs, which is safe only when the actions are idempotent.')
t('staticresult', 'Turn on static result to test the rest of the flow',
  'Static result pins one action\'s output so the remaining steps can be tested without re-running it.')
t('prompttemplate', 'Start from a prompt template in AI Hub',
  'A template carries a tested instruction and the input contract, so the prompt starts from something that works.')
t('promptblank', 'Build the prompt from blank',
  'A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself.')
t('promptinputs', 'Add typed inputs so the prompt takes values',
  'Typed inputs become the parameters an app or flow supplies when it calls the prompt.')
t('promptknowledge', 'Add the knowledge source so the prompt grounds on approved content',
  'Knowledge retrieval grounds the answer in the documents rather than in the model\'s memory.')
t('promptmodel', 'Choose the model that fits the task instead of the largest available',
  'Matching the model to the task controls cost and latency without losing the quality the task needs.')
t('promptapp', 'Call the prompt from the canvas app through its connector',
  'Consuming the published prompt keeps one instruction and one model choice behind every app.')
t('promptflow', 'Call the prompt from the cloud flow action',
  'A flow can run a prompt as a step, which is how a generated summary joins an automated process.')
t('promptcopy', 'Copy the prompt text into each app so it can be tuned per app',
  'Copied prompt text drifts, so the same question gets different answers in different apps.')
t('modelconsume', 'Consume the AI Hub model through the same connector pattern as a prompt',
  'A model consumed this way keeps authentication and throttling in one governed place.')
t('modelinflow', 'Call the model from the flow and store the result on the record',
  'Storing the result on the record is what makes the model output visible to the process and the audit.')
t('businessrule', 'Configure a business rule on the table',
  'A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form.')
t('brscope', 'Set the business rule scope to the table so it applies in every form',
  'Table scope is what makes the rule hold for imports and flows as well as the main form.')
t('bpf', 'Model the stages in a business process flow',
  'A business process flow guides a record through stages and pins the fields each stage needs.')
t('bpfbranch', 'Branch the business process flow on the case type',
  'A branch lets one process cover two variants without a second process and a duplicate set of stages.')
t('bpfsame', 'Keep every case type in one linear process to stay simple',
  'One linear process forces every case through fields and stages it does not need.')
t('calcformula', 'Use a formula column where the rule needs Power Fx',
  'A formula column evaluates a Power Fx expression, which is the current way to express derived values.')
t('calcrollup', 'Use a rollup column to aggregate the child records',
  'A rollup sums or counts related rows on a schedule, which is what a parent total needs.')
t('calcplugin', 'Write a plug-in to set the value on every update',
  'A plug-in is heavier than a column or a business rule and needs a developer to maintain it.')
t('logicpick', 'Pick the logic mechanism that matches where the rule must hold',
  'A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form.')
t('serverplugin', 'Enforce the rule in a synchronous plug-in when it must run on every write',
  'A synchronous plug-in runs inside the save, so no caller can bypass it.')

# Candidate orderings for the sequencing items live in their own module so the
# technical option bank stays readable.
from sequences import SEQUENCES

for _key, _value in SEQUENCES.items():
    if _key in TERMS:
        raise ValueError(f'Duplicate term: {_key}')
    TERMS[_key] = _value
