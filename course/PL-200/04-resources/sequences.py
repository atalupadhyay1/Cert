"""32 four-step ordered sequence options (8 groups x 4) for Exam PL-200 (all labels <= 245 chars)."""

SEQUENCES = {
    # 1. Domain 1 (1.5): Enable Dataverse Search and configure Quick Find searchable/view columns
    'seq_dv_search_ok': (
        'Enable Dataverse Search in PPAC environment Features → Open the table Quick Find View in the solution → Add Find Columns (indexed) and View Columns (returned) → Save and publish all customizations',
        'Dataverse Search requires enabling the environment feature in PPAC and configuring each table’s Quick Find View Find Columns (search index) and View Columns.',
    ),
    'seq_dv_search_bad_order': (
        'Delete the table Quick Find View first → Disable Dataverse Search in PPAC → Add columns only to a Personal View → Export an Unmanaged solution without publishing',
        'Personal views never control Dataverse Search indexing, and disabling Dataverse Search turns off Relevance Search across the environment.',
    ),
    'seq_dv_search_bad_sql': (
        'Connect SSMS directly to Dataverse SQL → Create custom clustered T-SQL indexes on base tables → Restart IIS on the Dataverse server → Clear local browser cache',
        'Dataverse is SaaS-managed; makers cannot create raw T-SQL indexes or restart IIS—search indexing is governed through PPAC and Quick Find Views.',
    ),
    'seq_dv_search_bad_audit': (
        'Turn on Column-Level Security for every text column → Create a Bulk Record Deletion job → Configure a Business Rule on Form load → Share the Personal View',
        'Column Security, Bulk Deletion, and Business Rules do not index tables or fields for Dataverse Search.',
    ),

    # 2. Domain 1 (1.12): Configure Dataverse Column-Level Security with a Column Security Profile
    'seq_col_sec_ok': (
        'Enable column security on the sensitive Dataverse column & save → Create a Column Security Profile in the solution/PPAC → Set Read, Read Unmasked, Update, and Create permissions → Add authorized teams or users to the profile',
        'Securing a sensitive column requires enabling column security on the column definition, creating a Column Security Profile, configuring field permissions, and adding users/teams.',
    ),
    'seq_col_sec_bad_order': (
        'Delete Organization Read from all Security Roles first → Add users to an empty Business Unit → Hide the column via JavaScript on one Main form → Leave Enable column security unchecked',
        'Hiding a field on a form does not secure API, Excel export, or view access; Enable column security + a Column Security Profile enforces server-side field security.',
    ),
    'seq_col_sec_bad_dlp': (
        'Create a Blocked DLP policy in PPAC → Export table rows to SharePoint → Assign System Administrator to all clerks → Enable Duplicate Detection on the column',
        'DLP policies govern connectors rather than Dataverse field-level authorization, and System Administrator bypasses restrictions entirely.',
    ),
    'seq_col_sec_bad_team': (
        'Create an Access Team Template first → Turn off Microsoft Entra authentication → Mark the column as Business Required in a Business Rule → Publish without a Column Security Profile',
        'Access Team Templates share record-level rows, whereas field-level masking and Read/Update control require Column Security Profiles.',
    ),

    # 3. Domain 2 (2.9): Trigger a Power Automate cloud flow from a Canvas app and return data
    'seq_canvas_flow_ok': (
        'Build a solution flow with the Power Apps (V2) trigger & typed inputs → End with Respond to a Power App or flow → Add the flow in Canvas Studio Power Automate pane → Call Set(varOut, FlowName.Run(...)) & set Run-only users',
        'Canvas-invoked flows define typed inputs on Power Apps (V2), return outputs via Respond to a Power App or flow, bind in Studio, and capture outputs via FlowName.Run(...).',
    ),
    'seq_canvas_flow_bad_order': (
        'Use a Scheduled Recurrence trigger first → Omit Respond to a Power App or flow → Hardcode FlowName.Run() before adding the flow to the app → Grant Co-owner rights to all 500 end users',
        'Scheduled flows cannot be invoked synchronously via FlowName.Run(), and end users need Run-only user permissions rather than Co-owner edit rights.',
    ),
    'seq_canvas_flow_bad_bpf': (
        'Create a classic Background Dataverse workflow → Embed an iframe pointing to flow.microsoft.com → Store maker passwords inside a Canvas text label → Poll Run History manually',
        'Canvas apps invoke cloud flows natively through the Power Apps (V2) trigger and FlowName.Run() connector bridge, never via iframes or plaintext credentials.',
    ),
    'seq_canvas_flow_bad_unauth': (
        'Remove all triggers from the cloud flow → Export the flow outside any Solution → Bind a Quick View form to the button → Expect synchronous values after 45-minute waits',
        'Every cloud flow requires a trigger, and Respond to a Power App or flow must return within the synchronous HTTP timeout window (~120 seconds).',
    ),

    # 4. Domain 2 (2.12): Secure Dataverse data on a Power Pages site with Table Permissions & Web Roles
    'seq_pages_sec_ok': (
        'Enable Table Permissions on the Power Pages Basic Form or List → Create a Table Permission scoped to Contact/Account with required privileges → Assign it to a custom Web Role → Associate authenticated Contacts with that Web Role',
        'Power Pages secures Dataverse Lists/Forms by enabling Table Permissions on the component, defining row-access scope (Global/Contact/Account/Parent/Self), and binding to Web Roles.',
    ),
    'seq_pages_sec_bad_open': (
        'Leave Enable Table Permissions unchecked → Assign Global Delete privilege to the Anonymous Users Web Role → Enable deprecated local password login → Publish to internet',
        'Granting Global Delete to Anonymous Users exposes every Dataverse row to public deletion, and Microsoft recommends external IdPs (Entra External ID) over local auth.',
    ),
    'seq_pages_sec_bad_order': (
        'Assign Dataverse internal Security Roles directly to anonymous web visitors → Skip Web Roles entirely → Add a Business Rule on Form load → Restart the portal without syncing',
        'External Power Pages Contacts do not use internal Dataverse Security Roles; portal authorization uses Table Permissions mapped to Web Roles.',
    ),
    'seq_pages_sec_bad_share': (
        'Share the internal Model-Driven App URL publicly → Disable SSL certificates in Set up workspace → Hardcode an API admin token in client JavaScript → Skip Page Access Rules',
        'Exposing admin tokens in browser JavaScript or sharing internal model-driven URLs violates Power Pages security architecture.',
    ),

    # 5. Domain 3 (3.8): Add an on-demand Cloud Flow step inside a Business Process Flow stage
    'seq_bpf_flow_ok': (
        'Create a solution Instant flow using When a flow step is run from a business process flow → Open the BPF designer in the same Solution → Add a Flow Step inside the target Stage & bind the flow → Validate, save, and Activate the BPF',
        'To run a cloud flow from a BPF stage button, both the BPF and the flow (using the BPF flow-step trigger) must reside in a Solution before binding and activating.',
    ),
    'seq_bpf_flow_bad_order': (
        'Build a personal My Flows cloud flow outside any Solution → Use an Outlook email trigger → Paste the flow URL into a BPF text column → Leave the BPF in Draft state',
        'Non-solution flows and non-BPF triggers cannot be bound as BPF Flow Steps, and Draft BPFs do not render for users.',
    ),
    'seq_bpf_flow_bad_rpa': (
        'Delete the BPF underlying Dataverse table → Record a desktop flow on a local laptop → Disable BPF security roles → Overwrite Active BPF instances manually in SQL',
        'Every BPF automatically maintains its own Dataverse table for stage tracking and requires security role enablement rather than SQL manipulation.',
    ),
    'seq_bpf_flow_bad_classic': (
        'Add 12 stages across 9 unrelated tables in one BPF → Skip Lookup relationships between tables → Trigger an Unattended RPA flow directly without a gateway/machine → Save without validation',
        'A Business Process Flow supports at most 30 stages and at most 5 related tables connected via 1:N relationships.',
    ),

    # 6. Domain 3 (3.11): Author and invoke a Dataverse Low-Code Power Fx Plug-in
    'seq_lowcode_plugin_ok': (
        'Open the Dataverse Accelerator app → Select Instant (typed parameters) or Automated (table Create/Update/Delete Pre/Post-op) plug-in → Write the Power Fx formula & pick a Solution → Save and test in the Accelerator canvas or app/flow',
        'Dataverse low-code plug-ins are authored in the Dataverse Accelerator app using Power Fx, saved into a Solution as Instant or Automated server-side plug-ins, and tested inline.',
    ),
    'seq_lowcode_plugin_bad_order': (
        'Open Visual Studio 2022 & compile a C# .NET assembly → Register via Plug-in Registration Tool in Production Default Solution → Disable Power Fx → Reboot Dataverse',
        'Low-code plug-ins use Power Fx inside the Dataverse Accelerator app rather than pro-code C# DLL compilation.',
    ),
    'seq_lowcode_plugin_bad_client': (
        'Write client-only Navigate() and Notify() UI calls inside an Automated Pre-operation plug-in → Skip Solution selection → Bind to an Excel file on OneDrive → Run offline',
        'Server-side Dataverse low-code plug-ins execute in the Dataverse event pipeline and cannot invoke client screen functions like Navigate().',
    ),
    'seq_lowcode_plugin_bad_dlp': (
        'Turn off Dataverse database in PPAC → Create a classic 2010 workflow first → Convert the workflow into HTML → Upload as a Power Pages web file',
        'Low-code plug-ins require a Dataverse database and are stored as Custom APIs / plug-in steps, not Power Pages HTML files.',
    ),

    # 7. Domain 4 (4.5): Export an Unmanaged Solution and Import as Managed with Environment Variables & Connection References
    'seq_sol_import_ok': (
        'Clear Dev Current Values on Environment Variables & run Solution Checker → Publish all customizations & Export as Managed → Import the Managed `.zip` into UAT/Production → Bind target Connection References & Environment Variable values',
        'Healthy ALM runs Solution Checker, publishes customizations, exports as Managed, and binds target-stage Connection References and Environment Variables at import.',
    ),
    'seq_sol_import_bad_unmanaged': (
        'Export the entire Default Solution from Dev as Unmanaged → Import Unmanaged directly into Production → Hardcode Dev URLs inside flow steps → Share personal maker logins',
        'Never export the Default Solution or import Unmanaged solutions into Production; use segmented Managed solutions with Connection References and Environment Variables.',
    ),
    'seq_sol_import_bad_order': (
        'Import an unvalidated solution into Production first → Run Solution Checker two weeks later → Create Environment Variables directly inside Production Default Solution → Skip publishing',
        'Unpublished changes in Dev are excluded from exported solutions, and Solution Checker should gate packages before Production import.',
    ),
    'seq_sol_import_bad_patch': (
        'Delete the Managed solution in Production every Friday (removing custom table data!) → Recreate tables manually → Re-import CSV backups → Reassign all Security Roles',
        'Deleting a Managed solution that defines custom tables permanently deletes those tables and their Production data; use Managed Upgrade (`Stage for upgrade`) instead.',
    ),

    # 8. Domain 4 (4.6): Configure Server-Side Synchronization and a Shared Support Queue Mailbox
    'seq_email_sync_ok': (
        'Verify Exchange Online Email Server Profile & Server-Side Sync defaults in PPAC → Create a Dataverse Queue with the shared email → Open the Queue Mailbox & select Approve Email → Run Test & Enable Mailbox until status = Success',
        'Routing shared-inbox emails into a Dataverse Queue via Server-Side Sync requires an Email Server Profile, a Queue with email address, Email Approval, and Test & Enable Mailbox.',
    ),
    'seq_email_sync_bad_order': (
        'Install deprecated Dynamics 365 Email Router on a Windows 7 PC → Skip Approve Email and Test & Enable Mailbox → Expect unapproved mailboxes to sync automatically → Disable Queues',
        'The legacy Email Router is deprecated; Server-Side Synchronization requires mailbox approval (when configured) and Test & Enable Mailbox succeeding.',
    ),
    'seq_email_sync_bad_dlp': (
        'Create a Personal View on the Contact table → Upload a Word Template → Run Bulk Record Deletion on ActivityPointer → Share the Queue via Anonymous Web Role',
        'Views, Word Templates, and Bulk Deletion do not configure Exchange Server-Side Synchronization or Queue mailboxes.',
    ),
    'seq_email_sync_bad_rpa': (
        'Open Outlook in a browser on a developer laptop → Record mouse coordinates with Power Automate for desktop → Copy email text into Notepad → Import CSV nightly',
        'Dataverse includes native Exchange Server-Side Synchronization and Dynamics 365 App for Outlook without brittle UI screen-scraping.',
    ),
}
