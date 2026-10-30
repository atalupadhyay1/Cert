"""32 four-step ordered sequence options (8 groups x 4) for Exam PL-900 (all labels <= 245 chars)."""

SEQUENCES = {
    # 1. Domain 2 (2.5): Create a Dataverse table and columns with Copilot from Excel/prompt
    'seq_dv_copilot_ok': (
        'Open Tables & select Create with Copilot (or Upload Excel) → Describe or map columns & data types in chat → Review proposed schema, primary column & sample rows → Confirm creation to provision the Dataverse table',
        'Copilot in Dataverse guides makers from a natural-language prompt or Excel sheet through interactive schema/type refinement before provisioning the Dataverse table.',
    ),
    'seq_dv_copilot_bad_prod': (
        'Sign directly into Production Default Solution → Create raw SQL Server tables via SSMS → Disable Microsoft Entra security roles → Paste Excel rows manually into views',
        'Dataverse does not expose raw SSMS table creation, and makers should build inside non-production solutions rather than bypassing security roles in Production.',
    ),
    'seq_dv_copilot_bad_order': (
        'Confirm table creation first → Provision blank columns without data types → Upload Excel headers afterward → Delete the primary name column',
        'You review and refine Copilot-proposed column names and data types before confirming creation, and every standard Dataverse table retains its primary column.',
    ),
    'seq_dv_copilot_bad_dlp': (
        'Create a Blocked DLP policy → Export an empty Managed solution → Run Power Automate desktop recorder → Import Excel as a binary attachment',
        'DLP policies and desktop UI recorders do not provision Dataverse table schemas from natural language or Excel.',
    ),

    # 2. Domain 2 (2.10): Promote a Solution from Dev to Test/Prod with Power Platform Pipelines
    'seq_alm_pipe_ok': (
        'Build apps, tables & flows in an Unmanaged Solution in Dev → Open Pipelines & select Deploy here for target stage → Bind target Connection References & Environment Variables → Submit deployment as Managed',
        'Power Platform pipelines package the Dev unmanaged solution, bind target Connection References and Environment Variables, honor stage approvals, and deploy as Managed.',
    ),
    'seq_alm_pipe_bad_default': (
        'Build components in the Default Solution in Production → Export the entire Default Solution as Unmanaged → Import Unmanaged into Dev → Share personal maker passwords',
        'Never export the Default Solution or deploy Unmanaged solutions into Production; build inside dedicated solutions in Dev and promote Managed packages.',
    ),
    'seq_alm_pipe_bad_order': (
        'Import an empty Managed solution into Prod first → Add tables directly in Prod → Run Pipeline backward to Dev → Configure Connection References after users fail',
        'Pipelines promote forward from Dev to Test/Prod and bind Connection References and Environment Variables during deployment setup before activation.',
    ),
    'seq_alm_pipe_bad_copy': (
        'Back up the entire Dev environment → Overwrite the Production environment database nightly → Reassign all Production user licenses → Recreate every cloud flow manually',
        'Environment copy/restore overwrites entire environments and data; Solutions + Power Platform pipelines move customizations cleanly without wiping Production data.',
    ),

    # 3. Domain 3 (3.3): Design a multi-component solution with Power Apps Plan designer
    'seq_plan_designer_ok': (
        'Describe the business problem & attach context files in Plan designer → Review & refine AI-generated user roles and stories → Adjust proposed Dataverse tables and relationships → Save the plan & generate apps, flows, and agents',
        'Plan designer collaborates step by step—from problem statement to user roles/stories, Dataverse data model, and recommended Canvas/Model-driven apps, flows, and agents.',
    ),
    'seq_plan_designer_bad_order': (
        'Publish canvas apps to Production first → Generate user roles afterward → Delete Dataverse tables → Enter the business problem description last',
        'Plan designer starts from the business problem to derive user roles, data tables, and technology recommendations before generating solution artifacts.',
    ),
    'seq_plan_designer_bad_rpa': (
        'Launch Power Automate for desktop → Record legacy green-screen mouse coordinates → Export raw C# plug-in code → Host an external anonymous website',
        'Desktop UI recording and pro-code C# plug-ins are unrelated to Power Apps Plan designer solution architecture.',
    ),
    'seq_plan_designer_bad_manual': (
        'Disable Copilot in Power Platform Admin Center → Manually code HTML/CSS pages from scratch → Skip Dataverse table relationships → Share unauthenticated links',
        'Plan designer is an AI-first multi-agent planning workspace in Power Apps rather than manual HTML authoring.',
    ),

    # 4. Domain 3 (3.7): Build and publish an app + data model in Power Apps vibe
    'seq_vibe_app_ok': (
        'Enter a prompt (plus optional work files) in Plan mode → Accept the proposed plan to generate app & in-memory draft tables → Refine UI and data across Plan, Data & App views → Publish draft tables to Dataverse & share',
        'In the Power Apps vibe experience, Plan mode proposes a plan first, generates the app with in-memory draft tables, lets makers iterate inline/via chat, and publishes draft tables to Dataverse.',
    ),
    'seq_vibe_app_bad_unpub': (
        'Write raw SQL tables first → Skip Plan review & disable AutoSave → Edit compiled files directly inside read-only Code view → Share in-memory draft tables to Production without publishing',
        'Direct code editing in Code view is read-only in vibe, and in-memory draft tables must be explicitly published to Dataverse before production sharing.',
    ),
    'seq_vibe_app_bad_order': (
        'Share the app with external guests first → Publish empty Dataverse tables → Reject the generated plan → Enter the initial business prompt last',
        'You begin with a prompt and accepted plan, refine the generated app and draft data model, and publish draft tables before sharing.',
    ),
    'seq_vibe_app_bad_canvas': (
        'Open an existing multi-app model-driven solution inside vibe → Coauthor simultaneously with five makers → Export to desktop RPA → Host anonymously on Power Pages',
        'Power Apps vibe supports one generated app per plan, does not open existing canvas/model-driven apps, and does not support multi-maker coauthoring.',
    ),

    # 5. Domain 4 (4.2): Automate a multi-stage SharePoint Approval cloud flow
    'seq_flow_approval_ok': (
        'Trigger flow with SharePoint When an item is created → Add Approvals Start and wait for an approval action → Add a Condition checking Outcome equals Approve → Update SharePoint item status & notify via Teams/Outlook',
        'A standard approval cloud flow triggers on the new item, pauses at Start and wait for an approval, branches on Outcome == Approve, and updates status plus notifies stakeholders.',
    ),
    'seq_flow_approval_bad_nowait': (
        'Use a manual button trigger → Add Create an approval without waiting for a response → Immediately mark every SharePoint item Approved → Send approval emails afterward',
        'Create an approval alone does not wait for the approver decision; Start and wait for an approval (or Wait for an approval) is required before evaluating Outcome.',
    ),
    'seq_flow_approval_bad_order': (
        'Evaluate Condition Outcome equals Approve first → Send final Teams confirmation → Start the approval request → Add the SharePoint trigger at the bottom',
        'Every cloud flow must begin with exactly one trigger, pause for the approval response, and only then evaluate Outcome in a Condition.',
    ),
    'seq_flow_approval_bad_rpa': (
        'Install an on-premises data gateway for SharePoint Online → Launch an unattended desktop flow to read browser pixels → Copy cells into Notepad → Email screenshots',
        'SharePoint Online, Approvals, Teams, and Outlook all have native cloud connectors and never require UI screen-scraping desktop flows or on-premises gateways.',
    ),

    # 6. Domain 4 (4.5): Record and parameterize a Desktop Flow in Power Automate for desktop
    'seq_pad_record_ok': (
        'Create desktop flow & define input/output variables → Launch Recorder to capture legacy app UI steps & elements → Replace hardcoded text with input variables & test locally → Trigger from a cloud flow via Machine runtime',
        'Makers define input/output variables, capture UI interactions with the Recorder, parameterize hardcoded text, test locally, and orchestrate runs from cloud flows.',
    ),
    'seq_pad_record_bad_cloudonly': (
        'Open Power Pages design studio → Connect directly to the legacy desktop app REST API → Skip Power Automate for desktop installation → Publish to Microsoft Teams channel',
        'Legacy desktop apps without APIs require Power Automate for desktop UI automation rather than Power Pages or REST connectors.',
    ),
    'seq_pad_record_bad_order': (
        'Trigger unattended production runs first → Install Power Automate for desktop afterward → Record mouse movements with hardcoded passwords → Define input variables last',
        'Power Automate for desktop must be installed and recorded/parameterized locally with secure inputs before cloud-triggered orchestration.',
    ),
    'seq_pad_record_bad_pixel': (
        'Disable UI element selectors → Rely solely on fixed 4K monitor X/Y screen coordinates → Store plaintext admin passwords inside action labels → Leave windows minimized during attended runs',
        'Reliable desktop flows use resilient UI element selectors and sensitive/secure input variables rather than brittle fixed pixel coordinates or cleartext passwords.',
    ),

    # 7. Domain 5 (5.1-5.5): Build, ground, extend with tools, test, and publish a Copilot Studio agent
    'seq_agent_publish_ok': (
        'Create the agent with clear instructions → Add SharePoint/web Knowledge & configure Topics/Tools (agent flows or MCP) → Validate answers in the Test your agent pane → Publish the agent & enable target channels like Teams',
        'Makers define agent instructions, ground answers in Knowledge sources and Topics/Tools, test behavior, and publish before enabling deployment channels like Teams.',
    ),
    'seq_agent_publish_bad_nopub': (
        'Enable the Microsoft Teams channel first → Edit topics without selecting Publish → Expect live Teams users to see unpublished draft edits immediately → Add knowledge sources last',
        'Channel users only receive updates after you explicitly publish the agent in Copilot Studio.',
    ),
    'seq_agent_publish_bad_order': (
        'Export analytics transcripts first → Delete system Greeting and Fallback topics → Publish an empty agent with no knowledge or topics → Write agent instructions afterward',
        'System topics handle core lifecycle turns, and instructions, knowledge, and tools must be configured and tested prior to publishing.',
    ),
    'seq_agent_publish_bad_pva': (
        'Write custom C# bot middleware from scratch → Copy SharePoint files manually into public anonymous web folders → Disable Microsoft Entra authentication → Email zip files to users',
        'Copilot Studio connects natively to SharePoint while honoring Microsoft Entra user permissions without exposing internal files publicly.',
    ),

    # 8. Domain 5 (5.8): Run and compare automated Agent Evaluations in Copilot Studio
    'seq_agent_eval_ok': (
        'Create an Evaluation test set of prompts & graders → Run Evaluate to score Pass/Fail and latency → Inspect failed cases via Activity map & refine knowledge/instructions → Rerun & select Compare with to verify gains',
        'Copilot Studio evaluations run repeatable test sets against graders, reveal reasoning/tool traces in Activity map, and compare Pass rates across runs via Compare with.',
    ),
    'seq_agent_eval_bad_manual': (
        'Skip test sets entirely → Type one casual prompt in the Test chat pane → Publish straight to all employees → Wait for helpdesk complaints to measure accuracy',
        'Ad-hoc single chat prompts are not repeatable; Evaluation test sets measure systematic Pass/Fail accuracy and prevent regressions before publishing.',
    ),
    'seq_agent_eval_bad_order': (
        'Select Compare with before running any test set → Export empty CSV results → Write prompts without assertions or graders → Delete the Microsoft Copilot Studio connection',
        'Compare with requires at least two completed runs of the same test set, and user-authenticated evaluations require an active Copilot Studio connection.',
    ),
    'seq_agent_eval_bad_viewer': (
        'Assign every reviewer System Administrator rights → Let agent viewers rewrite production topics directly → Turn off content safety graders → Overwrite baseline runs',
        'The least-privilege agent viewer sharing role lets stakeholders view and run evaluations without granting edit or publish access to the agent itself.',
    ),
}
