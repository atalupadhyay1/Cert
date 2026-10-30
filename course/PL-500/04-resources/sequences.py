"""32 four-step ordered sequence options (8 groups x 4) for Exam PL-500 (all labels <= 255 chars)."""

SEQUENCES = {
    # 1. Domain 1 (1.4): Execute an Unattended Desktop Flow on a locked/signed-out VM from a Cloud Flow
    'seq_unattended_run_ok': (
        'Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion',
        'Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.',
    ),
    'seq_unattended_run_bad_rdp': (
        'Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text',
        'Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.',
    ),
    'seq_unattended_run_bad_order': (
        'Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse',
        'Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.',
    ),
    'seq_unattended_run_bad_local': (
        'Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically',
        'Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.',
    ),

    # 2. Domain 1 (1.9): End-to-End Document Automation Toolkit Processing Lifecycle
    'seq_doc_toolkit_ok': (
        'Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream',
        'The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.',
    ),
    'seq_doc_toolkit_bad_order': (
        'Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse',
        'Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.',
    ),
    'seq_doc_toolkit_bad_sql': (
        'Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows',
        'Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.',
    ),
    'seq_doc_toolkit_bad_dlp': (
        'Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email',
        'Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.',
    ),

    # 3. Domain 2 (2.1): Configure a Solution Cloud Flow to Invoke a Desktop Flow and Consume Outputs
    'seq_cloud_calls_pad_ok': (
        'Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream',
        'Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.',
    ),
    'seq_cloud_calls_pad_bad_order': (
        'Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually',
        'Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.',
    ),
    'seq_cloud_calls_pad_bad_mode': (
        'Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP',
        'Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.',
    ),
    'seq_cloud_calls_pad_bad_share': (
        'Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod',
        'Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.',
    ),

    # 4. Domain 2 (2.8): Build Resilient Dynamic UI Selectors with Fallbacks in Power Automate for Desktop
    'seq_ui_selector_ok': (
        'Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads',
        'Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.',
    ),
    'seq_ui_selector_bad_pixel': (
        'Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs',
        'Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.',
    ),
    'seq_ui_selector_bad_order': (
        'Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field',
        'Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.',
    ),
    'seq_ui_selector_bad_citrix': (
        'Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors',
        'Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).',
    ),

    # 5. Domain 2 (2.14): Author, Sign, Upload, and Use a .NET Custom Action in Power Automate for Desktop
    'seq_custom_action_ok': (
        'Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD',
        'Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.',
    ),
    'seq_custom_action_bad_unsigned': (
        'Write an unsigned `.exe` console app → Copy it manually to `C:\\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically',
        'Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.',
    ),
    'seq_custom_action_bad_order': (
        'Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop',
        'Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).',
    ),
    'seq_custom_action_bad_py': (
        'Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand',
        'Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.',
    ),

    # 6. Domain 2 (2.16): Protect Sensitive Secrets End-to-End Across Cloud and Desktop Flows
    'seq_secure_secrets_ok': (
        'Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs',
        'End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.',
    ),
    'seq_secure_secrets_bad_plain': (
        'Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log',
        'Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.',
    ),
    'seq_secure_secrets_bad_order': (
        'Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing',
        'Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.',
    ),
    'seq_secure_secrets_bad_env': (
        'Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step',
        'Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.',
    ),

    # 7. Domain 3 (3.1): Promote an Enterprise RPA Solution from Dev to Production via Managed ALM
    'seq_rpa_alm_ok': (
        'Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs',
        'Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.',
    ),
    'seq_rpa_alm_bad_unmanaged': (
        'Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names',
        'Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.',
    ),
    'seq_rpa_alm_bad_delete': (
        'Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows',
        'Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.',
    ),
    'seq_rpa_alm_bad_gateway': (
        'Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts',
        'Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.',
    ),

    # 8. Domain 3 (3.8): Register VM Bots into a Load-Balanced Machine Group for Unattended RPA
    'seq_machine_group_ok': (
        'Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference',
        'Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.',
    ),
    'seq_machine_group_bad_order': (
        'Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests',
        'Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.',
    ),
    'seq_machine_group_bad_os': (
        'Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended',
        'Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.',
    ),
    'seq_machine_group_bad_share': (
        'Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly',
        'Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.',
    ),
}
