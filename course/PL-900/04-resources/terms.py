"""Option & distractor vocabulary for Microsoft Exam PL-900 (all labels <= 255 chars, explanations <= 270 chars)."""

from sequences import SEQUENCES

TERMS = {}


def t(key: str, label: str, explanation: str):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    TERMS[key] = (label, explanation)


# --- Domain 1: Business value of Microsoft Power Platform (1.1 - 1.4) ---
t('val_power_apps',
  'Microsoft Power Apps — empowers citizen and professional makers to rapidly build custom web and mobile business apps that connect to organizational data',
  'Power Apps reduces app backlog and manual paper/spreadsheet processes through canvas apps, model-driven apps, Plan designer, and code apps.')
t('val_power_automate',
  'Microsoft Power Automate — automates repetitive tasks, multi-stage approvals, cloud notifications, and legacy UI desktop workflows across services',
  'Power Automate eliminates error-prone manual copy-paste work using cloud flows, desktop flows (RPA), and AI Builder automation.')
t('val_dataverse',
  'Microsoft Dataverse — provides a secure, cloud-managed relational data platform with Common Data Model tables, built-in security roles, and reusable business logic',
  'Dataverse stores and governs structured and file data centrally so multiple apps, flows, websites, and agents share one trusted data model.')
t('val_connectors',
  'Power Platform connectors — provide more than 1,000 prebuilt and custom API wrappers (triggers and actions) to integrate Microsoft 365, Dynamics 365, Azure, and third-party services',
  'Standard, premium, and custom connectors bridge cloud and on-premises data via the on-premises data gateway without custom integration code.')
t('val_gateway_onprem',
  'On-premises data gateway — creates a secure outbound bridge so Power Apps, Power Automate, and Copilot Studio can reach internal SQL Server or file shares behind a corporate firewall',
  'The on-premises data gateway connects cloud Power Platform services securely to internal data sources without opening inbound firewall ports.')
t('val_power_pages',
  'Microsoft Power Pages — builds secure, responsive external-facing business websites and portals where customers, partners, or citizens interact with Dataverse data',
  'Power Pages delivers low-code external websites with role-based web permissions and authenticated (Entra External ID, social) or anonymous access.')
t('val_genai_platform',
  'Generative AI across Power Platform (Copilot & AI Prompts) — accelerates maker productivity from natural language and embeds AI summarization, drafting, and classification into apps and flows',
  'Built-in Copilot features let makers build tables, apps, flows, and agents conversationally while AI Prompts add governed generative AI actions.')
t('val_copilot_studio',
  'Microsoft Copilot Studio — provides a low-code graphical studio to build, ground, evaluate, and publish conversational and autonomous AI agents across channels',
  'Copilot Studio enables teams to build custom agents grounded in enterprise knowledge and tools or extend Microsoft 365 Copilot.')
t('val_fusion_teams',
  'Fusion development — unites business domain experts, low-code citizen makers, IT admins, and pro-code developers collaborating on shared governed solutions',
  'Power Platform bridges citizen makers and professional developers (Visual Studio, Azure, PCF, code apps) inside a single ALM and security model.')

# --- Domain 2: Manage the Microsoft Power Platform environment (2.1 - 2.10) ---
t('dv_vs_traditional_db',
  'Unlike a raw SQL database requiring manual API, auth, and audit plumbing, Dataverse includes Common Data Model schemas, Entra RBAC, server-side business rules, auditing, and native OData APIs out of the box',
  'Dataverse is a managed data-and-logic platform rather than bare table storage, enforcing security and business rules regardless of which app accesses the data.')
t('dv_table_types',
  'Standard/custom tables store relational Dataverse rows; virtual tables surface live external data without copying it; elastic tables handle massive high-velocity semi-structured JSON bursts',
  'Choosing the right Dataverse table type balances relational ACID storage, zero-copy live external projection (virtual), and Cosmos DB horizontal scale (elastic).')
t('dv_columns_choices',
  'Dataverse typed columns (Text, Currency, Lookup, File, Formula) and global/local Choices (picklists) enforce consistent data formatting and reusable dropdown sets across tables',
  'Global Choices allow multiple tables and apps to share one centrally maintained list of picklist options, whereas local choices belong to a single table.')
t('dv_relationships_1n_nn',
  'One-to-many (`1:N` / `N:1`) relationships link a parent row to child rows via a Lookup column, while many-to-many (`N:N`) relationships associate multiple rows on both sides via a hidden intersect table',
  'Lookup columns implement 1:N parent-child links (like Account to Contacts), while N:N links many records to many records (like Students to Courses).')
t('dv_forms_four_types',
  'Main forms provide the full record UX; Quick Create forms streamline slide-out record entry; Quick View forms display read-only parent lookup data; Card forms render compact mobile/subgrid summaries',
  'Understanding the four Dataverse model-driven form types ensures makers pick Quick View for read-only parent details and Quick Create for fast inline creation.')
t('dv_views_types',
  'Dataverse views define which columns, sort order, and row filters appear in lists—including Public views for all users, System views (Lookup/Associated/Quick Find), and Personal views saved by individuals',
  'Views control tabular record filtering and column layout across model-driven grids, lookups, and canvas-app table selections.')
t('dv_business_rules',
  'Dataverse Business Rules apply declarative if/then conditions to show errors, set column values, toggle visibility, lock fields, or mark columns required—enforced across all apps when scoped to Entity',
  'Entity-scoped Business Rules run server-side across canvas apps, model-driven apps, and flows, whereas Form-scoped rules run only on model-driven forms.')
t('dv_powerfx_rollup_calc',
  'Power Fx formula columns calculate real-time values on read using Excel-like expressions, while Rollup columns aggregate related child rows (`SUM`, `COUNT`, `AVG`, `MIN`, `MAX`) on a schedule',
  'Formula columns replace legacy calculated columns with rich Power Fx expressions, while Rollup columns summarize 1:N child records automatically.')
t('dv_copilot_table_gen',
  'Copilot in Dataverse creates and modifies tables, typed columns, sample data, and relationships from natural-language prompts, uploaded Excel workbooks, or SharePoint lists',
  'Makers describe business entities in plain language or upload spreadsheets, review suggested column types in the preview pane, and adjust schemas conversationally.')
t('env_types_overview',
  'Default (auto-created, shared basic maker space), Developer (personal single-user build space), Sandbox (non-production dev/test with reset/copy), Production (live workloads), and Trial (temporary 30-day evaluation)',
  'Each Power Platform environment resides in one geographic region, holds at most one Dataverse database, and isolates apps, flows, and security boundaries.')
t('env_managed_env',
  'Managed Environments — add enterprise governance at scale including weekly admin digest emails, sharing limits, Solution Checker enforcement, maker welcome content, and pipeline support',
  'Enabling Managed Environments in Power Platform Admin Center unlocks guardrails like canvas-app sharing caps and automated solution validation.')
t('sec_entra_roles_bu',
  'Microsoft Entra ID authenticates users and Conditional Access, while Dataverse Business Units, Security Roles (Create/Read/Write/Delete/Append/Append To), Teams, and Column-Level Security control data authorization',
  'Power Platform layers Entra identity authentication with environment roles and granular row-level and column-level Dataverse privileges.')
t('sec_dlp_policies',
  'Data Loss Prevention (DLP) policies classify connectors into `Business`, `Non-Business`, and `Blocked` groups so confidential corporate data cannot mix with unapproved external services in the same app or flow',
  'Tenant and environment admins configure DLP policies in Power Platform Admin Center to prevent accidental data exfiltration across connectors.')
t('gov_privacy_accessibility',
  'Accessibility Checker in Power Apps Studio flags missing `AccessibleLabel` properties, broken `TabIndex` navigation, closed-caption gaps, and low color contrast alongside GDPR/Purview privacy controls',
  'Built-in accessibility checks help makers meet WCAG screen-reader and keyboard standards, while Purview and GDPR tools govern personal data.')
t('gov_ppac_monitoring',
  'Power Platform Admin Center (PPAC) provides built-in tenant/environment analytics for Dataverse storage capacity, Power Apps usage, Power Automate runs/errors, Monitor diagnostics, and Advisor recommendations',
  'Admins track Dataverse database/file/log capacity, active app launches, flow failure trends, and security recommendations directly in PPAC.')
t('alm_solutions_managed',
  'Solutions package customizations as Unmanaged in Dev (editable source) and Managed in Test/Production (locked, cleanly upgradable), using Environment Variables and Connection References for stage settings',
  'Solutions are the mechanism for ALM in Power Platform; Managed solutions protect production integrity and support clean version upgrades.')
t('alm_pp_pipelines',
  'Power Platform pipelines provide an in-product automated deployment experience so makers and admins promote solutions from Dev to Test and Production with pre-configured approvals and governance',
  'Pipelines democratize healthy ALM directly inside Power Apps and Power Platform Admin Center without requiring makers to write YAML scripts.')

# --- Domain 3: Demonstrate the capabilities of Power Apps (3.1 - 3.7) ---
t('app_canvas_usecase',
  'Canvas app — starts from a blank or template screen giving makers pixel-perfect control over layout, camera/barcode controls, and Power Fx formulas across 1,000+ connectors (SharePoint, SQL, Excel, Dataverse)',
  'Canvas apps excel at task-focused mobile/tablet/web experiences where custom visual layout and multi-connector mashups matter most.')
t('app_model_driven_usecase',
  'Model-driven app — generates a responsive, accessible UI automatically from Microsoft Dataverse tables, forms, views, charts, dashboards, and Business Process Flows without pixel-by-pixel layout work',
  'Model-driven apps require Microsoft Dataverse and excel at structured back-office case, inspection, and process-heavy lifecycle management.')
t('app_bpf_guided_stages',
  'Business Process Flow (BPF) — displays a visual stage-and-step ribbon across the top of a record so every user follows consistent, gated business milestones from start to finish',
  'Business Process Flows standardize multi-stage human processes (such as Triage -> Investigation -> Resolution) atop Dataverse tables.')
t('app_plan_designer',
  'Plan designer in Power Apps — uses collaborative AI agents to turn a natural-language business problem and attached screenshots/diagrams into user roles, stories, Dataverse tables, and recommended apps, flows, and agents',
  'Plan designer also generates plans from existing solutions to document architecture and lets makers swap proposed apps with existing apps.')
t('app_code_apps',
  'Power Apps code apps — let professional developers host full custom web applications (such as TypeScript/React) directly on Power Platform with built-in Microsoft Entra auth, managed connectors, and DLP governance',
  'Code apps bring pro-code web frontends onto the governed Power Platform runtime without forcing a rewrite into low-code screens.')
t('app_ai_canvas_copilot',
  'Copilot in canvas apps — builds a responsive app and underlying Dataverse table from a natural-language prompt, suggests/explains Power Fx formulas in the formula bar, and adds an in-app Copilot chat control for end users',
  'Makers both co-build canvas screens/formulas with Copilot in Power Apps Studio and embed Copilot controls so users can ask questions about app data.')
t('app_ai_model_copilot',
  'Copilot in model-driven apps — assists end users with AI form-fill suggestions from pasted text/emails, natural-language grid view filtering, record summaries, and a sidecar Copilot chat over Dataverse data',
  'Model-driven apps include built-in AI assistance that speeds data entry, filters views in plain English, and answers questions about environment records.')
t('app_vibe_experience',
  'Power Apps vibe experience — combines Plan, Data (in-memory draft tables publishable to Dataverse), and App preview/inline editing in one AI-native conversational workspace for rapid web-app creation',
  'In vibe (`vibe.powerapps.com`, transitioning to Copilot Cowork and Apps in Copilot Studio), makers review a proposed plan first, attach work files, refine UI/data together, and publish draft tables to Dataverse.')

# --- Domain 4: Demonstrate the capabilities of Power Automate (4.1 - 4.5) ---
t('flow_cloud_three_types',
  'Automated cloud flows run when an event occurs (such as a new email or Dataverse row); Instant cloud flows run on manual button press; Scheduled cloud flows run on a recurring timer (hourly, daily, weekly)',
  'Matching the business trigger—event-driven, on-demand human button, or fixed calendar schedule—determines which of the three cloud flow types to create.')
t('flow_desktop_rpa_modes',
  'Desktop flows (Power Automate for desktop) automate legacy Windows, terminal, or web UIs lacking APIs—running Attended (with a signed-in user watching) or Unattended (autonomously on a locked/background VM)',
  'Robotic Process Automation (RPA) bridges legacy systems without connectors; Attended mode collaborates with a human user while Unattended runs headless at scale.')
t('flow_process_mining',
  'Process advisor / Process Mining in Power Automate — analyzes event logs and recorded user tasks to visualize workflow bottlenecks, rework loops, and highest-ROI automation candidates',
  'Process and task mining uncover slow manual steps visually before teams invest in building cloud or desktop flows.')
t('flow_m365_approvals',
  'Power Automate Approvals (`First to respond` vs `Everyone must approve`) deliver actionable adaptive cards straight into Microsoft Teams and Outlook so approvers decide without opening a separate portal',
  'Built-in Approvals actions integrate natively with Teams, Outlook, SharePoint lists/libraries, and Microsoft Forms submissions.')
t('flow_aibuilder_doc_proc',
  'AI Builder Document Processing in Power Automate — extracts structured fields and tables from invoices, receipts, IDs, or custom PDF forms and routes extracted values into Dataverse, SharePoint, or ERP',
  'Prebuilt and custom AI Builder models turn unstructured PDF/image attachments from Outlook or SharePoint into structured automation data.')
t('flow_triggers_actions_loop',
  'Every cloud flow starts with one Connector Trigger followed by Actions, using Dynamic Content tokens, `Condition` branches, and `Apply to each` loops to iterate arrays of items automatically',
  'Triggers start the flow, Dynamic Content passes outputs downstream, Conditions split Yes/No logic, and Apply to each processes multi-row lists.')
t('flow_ai_cloud_copilot',
  'Copilot in Power Automate cloud flows — generates a complete draft flow from a natural-language prompt ("Describe it to design it"), modifies steps via chat inside the designer, and explains what an existing flow does',
  'Makers describe desired triggers, conditions, and actions in plain English and ask Copilot to add error notifications, conditions, or flow summaries.')
t('flow_ai_desktop_copilot',
  'Copilot in Power Automate for desktop — generates desktop automation actions from natural language, summarizes complex subflows, answers product questions, and pairs with Recorder/AI generative actions for resilient UI automation',
  'Copilot lowers the RPA learning curve in Power Automate for desktop by drafting UI/file/Excel actions, explaining scripts, and adapting to UI changes.')

# --- Domain 5: Agents in Microsoft Copilot Studio (5.1 - 5.8) ---
t('agt_conv_vs_autonomous',
  'Conversational agents respond interactively to user chat prompts in channels like Teams or websites, whereas Autonomous agents wake up automatically on background event triggers (such as a new Dataverse row or email) to reason and act',
  'Copilot Studio supports both human-initiated conversational chat agents and event-driven autonomous agents—plus extending Microsoft 365 Copilot.')
t('agt_topics_nodes',
  'Topics define structured or AI-selected conversation paths using Trigger phrases/descriptions, `Message` nodes, `Question` nodes (capturing entities into variables), `Condition` branches, and System topics (`Greeting`, `Escalate`, `Fallback`)',
  'With generative orchestration, Copilot Studio selects Topics from their natural-language description or trigger phrases and collects typed user variables.')
t('agt_knowledge_sources',
  'Knowledge sources ground generative agent answers in trusted content—such as SharePoint sites, OneDrive folders, Dataverse tables, uploaded documents, and public URLs—while enforcing the signed-in user’s access permissions',
  'Adding Knowledge sources lets an agent answer broad domain questions accurately with citations without authoring hundreds of manual FAQ topics.')
t('agt_tools_mcp_flows',
  'Tools extend Copilot Studio agents to take real-world actions—combining Agent flows (deterministic `When an agent calls the flow` -> `Respond to the agent`), prebuilt/custom connectors, AI prompts, and Model Context Protocol (MCP) servers',
  'MCP servers expose live enterprise tools and schemas dynamically to Copilot Studio agents, while Agent flows run repeatable deterministic multi-step workflows.')
t('agt_channels_publish',
  'Publishing an agent pushes saved changes live so makers can deploy across Channels including Microsoft Teams + Microsoft 365 Copilot, custom/demo websites, SharePoint, mobile apps, and Azure Bot Service channels',
  'Edits remain in draft inside Copilot Studio until Published; authentication settings control Entra SSO for internal Teams users vs manual/no auth for public web visitors.')
t('agt_agent_365_gov',
  'Microsoft Agent 365 — provides centralized IT governance for Copilot Studio and Foundry agents, including Microsoft Entra agent identities, Conditional Access policies, tenant-wide agent inventory, and Defender threat detection/observability',
  'Microsoft Agent 365 gives security and IT admins unified discovery, Entra identity lifecycle, access governance, and runtime threat protection across organizational agents.')
t('agt_analytics_monitoring',
  'Copilot Studio Analytics tracks total sessions, engagement rate, session outcomes (`Resolved`, `Escalated`, `Abandoned`), Customer Satisfaction (CSAT), unanswered user questions, and Copilot credit consumption',
  'Reviewing session outcomes, user reactions, and Copilot credit usage helps makers spot knowledge gaps, reduce escalations, and forecast capacity.')
t('agt_evaluations_testset',
  'Agent Evaluations in Copilot Studio — run repeatable automated test sets of prompts against graders (keyword, exact match, semantic similarity, LLM-as-judge, tool verification, content safety), Activity maps, and `Compare with` regression views',
  'Evaluations replace manual spot-checking with measurable Pass/Fail test sets, CSV exports, and least-privilege `agent viewer` stakeholder review.')

# --- Fundamentals Anti-Patterns & Common Misconceptions (Distractors) ---
t('anti_powerpages_internal_only',
  'Use a Power Apps model-driven app shared directly with unauthenticated anonymous consumers on the public internet',
  'Model-driven and canvas apps require authenticated Microsoft Entra / licensed internal or guest users; external public/partner websites belong in Microsoft Power Pages.')
t('anti_canvas_no_dataverse_req',
  'Model-driven apps can run solely on an unformatted Excel workbook stored on a personal desktop with zero Microsoft Dataverse database',
  'Model-driven apps strictly require Microsoft Dataverse for metadata, tables, forms, views, and security; Canvas apps connect directly to Excel or SharePoint.')
t('anti_sharepoint_security_row',
  'Store 2 million confidential HR compensation rows in a single SharePoint list expecting native column-level security and hierarchical Business Unit RBAC',
  'SharePoint lists lack Dataverse column-level security, hierarchical Business Units, and high-scale relational performance.')
t('anti_edit_default_solution_prod',
  'Customize tables, forms, and flows directly inside the Production `Default Solution` without creating a dedicated Solution or using pipelines',
  'Editing directly in Production or inside the Default Solution bypasses ALM governance, creates unmanaged drift, and risks live outages.')
t('anti_dlp_encrypts_sql',
  'Data Loss Prevention (DLP) policies encrypt Windows laptop hard drives with BitLocker and block users from taking phone photos of monitors',
  'Power Platform DLP policies govern which connectors and connector actions can coexist in apps, flows, and agents—not device disk encryption.')
t('anti_cloud_flow_legacy_win32',
  'Use an Automated Cloud Flow alone to press buttons inside a 1998 offline Windows Win32 accounting app that has no API or database connector',
  'Apps with no API or connector require a Power Automate Desktop Flow (RPA) to automate local Windows UI elements.')
t('anti_unpublished_agent_live',
  'Closing the browser tab in Copilot Studio automatically deploys all unsaved Topic and Knowledge edits to live Microsoft Teams users without publishing',
  'Copilot Studio changes only reach external channels like Microsoft Teams after an explicit Publish operation.')
t('anti_pl900_openbook_expire',
  'Fundamentals certifications expire every 12 months and include open-book split-screen Microsoft Learn access during the 45-minute exam',
  'Microsoft Fundamentals certifications (like PL-900) NEVER expire and do NOT allow split-screen Microsoft Learn open-book access (which applies only to role-based Associate/Expert exams).')

# --- Fundamentals Formula, UI & Concept Completion Tokens (____ items) ---
t('tok_pfx_filter',
  '`Filter(ServiceTickets, Status = "Open")`',
  '`Filter(Table, Condition)` returns all matching rows from a table or connector to populate a Canvas app Gallery.')
t('tok_pfx_navigate',
  '`Navigate(SuccessScreen, ScreenTransition.Fade)`',
  '`Navigate(TargetScreen, Transition)` moves the user from the current Canvas app screen to another screen.')
t('tok_pfx_submitform',
  '`SubmitForm(EditForm1)`',
  '`SubmitForm(FormName)` validates and saves changes from a Canvas app Edit Form control back to its connected data source.')
t('tok_pfx_newform',
  '`NewForm(EditForm1)`',
  '`NewForm(FormName)` switches a Canvas app Edit Form control into new-record entry mode with blank/default fields.')
t('tok_pfx_lookup',
  '`LookUp(Employees, Email = User().Email)`',
  '`LookUp(Table, Condition)` finds and returns the first single matching record (rather than a multi-row table).')
t('tok_pfx_user_email',
  '`User().FullName` and `User().Email`',
  'The Power Fx `User()` function returns basic profile details (`FullName`, `Email`, `Image`) of the currently signed-in Canvas app user.')
t('tok_dv_quick_view_form',
  '`Quick View` form',
  'A Dataverse `Quick View` form embeds read-only columns from a parent Lookup record (such as Account details on a Contact form) without duplicating data.')
t('tok_dv_business_rule_entity',
  '`Entity` scope',
  'Setting a Dataverse Business Rule scope to `Entity` enforces the rule server-side across all model-driven forms, canvas apps, and automated imports.')
t('tok_dlp_three_groups',
  '`Business`, `Non-Business`, and `Blocked`',
  'Power Platform DLP policies partition connectors into `Business`, `Non-Business` (default), and `Blocked` data groups.')
t('tok_vibe_publish_draft',
  '`Publish draft tables` to Microsoft Dataverse',
  'In the Power Apps vibe experience, newly generated draft tables exist in memory only until the maker selects `Publish draft tables` to persist them in Dataverse.')
t('tok_flow_start_wait_approval',
  '`Start and wait for an approval`',
  '`Start and wait for an approval` sends the approval request and pauses the cloud flow until the required approver(s) respond so downstream conditions can inspect `Outcome`.')
t('tok_flow_apply_to_each',
  '`Apply to each`',
  '`Apply to each` iterates over an array/list of records (such as email attachments or SharePoint rows) and runs inner actions once per item.')
t('tok_agt_question_node',
  '`Question` node',
  'In a Copilot Studio Topic, a `Question` node prompts the user, extracts a typed Entity (such as Date, Email, or City), and saves the answer into a Variable.')
t('tok_agt_mcp_server',
  'Model Context Protocol (`MCP`) server',
  'Connecting an `MCP` server in Copilot Studio dynamically exposes external enterprise tools, resources, and data schemas to the agent without hand-wiring individual actions.')
t('tok_agt_agent_viewer_role',
  '`Agent viewer` evaluation sharing role',
  'Sharing a Copilot Studio agent with the `Agent viewer` role lets domain reviewers inspect and run Evaluation test sets without granting permission to edit or publish the agent.')
t('tok_agt_agent_365',
  '`Microsoft Agent 365`',
  '`Microsoft Agent 365` centralizes IT governance across Copilot Studio and Foundry agents, providing Entra agent identities, Conditional Access, inventory, and Defender threat observability.')

for _k, _v in SEQUENCES.items():
    t(_k, _v[0], _v[1])
