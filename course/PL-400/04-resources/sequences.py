"""Ordered 4-step (->) sequence options for Exam PL-400 (8 workflows x 4 candidate orderings = 32 entries, all <= 265 chars)."""

SEQUENCES = {
    # 1. Domain 1 (1.8): Source-controlled ALM with PAC CLI / Build Tools -> Managed Upgrade
    'seq_alm_git_ok': (
        'Export unmanaged solution from Dev → Unpack ZIP to XML/YAML and commit to Git → Run `pac solution check` & pack Managed ZIP in CI → Import Managed solution with Stage & Apply Upgrade in Prod',
        'Healthy Power Platform ALM exports unmanaged metadata from Dev, unpacks into Git source files, runs Solution Checker + Managed pack in CI, and applies a Managed Upgrade in Prod to prune deleted components.',
    ),
    'seq_alm_git_bad_unmanaged_prod': (
        'Export Managed solution from Dev → Commit binary ZIP directly to Git without unpacking → Convert ZIP to Unmanaged in CI → Import Unmanaged solution directly into Prod',
        'Importing unmanaged solutions into Production pollutes the unmanaged active layer, prevents clean uninstall/rollback, and committing binary ZIPs hides component-level Git diffs.',
    ),
    'seq_alm_git_bad_order': (
        'Apply Upgrade in Prod first → Export unmanaged solution from Prod → Unpack into Dev → Run Solution Checker after Production deployment',
        'Changes must originate in Dev, pass Solution Checker prior to Production import, and never be authored or exported from Production.',
    ),
    'seq_alm_git_bad_patch_forever': (
        'Edit components directly inside Default Solution in Prod → Export Default Solution ZIP → Import Default Solution into Dev → Delete Managed layers manually',
        'Editing the Default Solution in Production creates unmanaged layer overrides and cannot export a clean segmented managed package.',
    ),

    # 2. Domain 1 (1.7): Azure Key Vault Environment Variable setup
    'seq_envvar_kv_ok': (
        'Register `Microsoft.PowerPlatform` provider & grant `Dataverse` SPN + maker Key Vault `Get` access → Create Secret Environment Variable in Dev → Remove Current Value before export → Bind Prod Key Vault secret on Prod import',
        'Key Vault Secret Environment Variables require `Microsoft.PowerPlatform` registered on the subscription, Vault `Get` permissions for `Dataverse` + maker, stripping Dev values on export, and binding Prod Vault references on import.',
    ),
    'seq_envvar_kv_bad_hardcode': (
        'Paste plaintext production API secret into a Text Environment Variable Default Value → Commit unpacked XML secret to Git → Import Managed solution into Prod → Rotate secret by editing Prod unmanaged layer',
        'Text Environment Variables store values in readable solution XML and Dataverse tables; secrets must use Secret data type backed by Azure Key Vault without Default Values.',
    ),
    'seq_envvar_kv_bad_norp': (
        'Create Secret Environment Variable in Prod first → Skip `Microsoft.PowerPlatform` Azure resource provider registration → Hardcode Dev Vault URI in C# plug-in → Export Managed solution from Prod to Dev',
        'Without registering the `Microsoft.PowerPlatform` resource provider and granting `Dataverse` access on the Key Vault, Dataverse cannot resolve the secret.',
    ),
    'seq_envvar_kv_bad_keep_dev': (
        'Create Secret Environment Variable in Dev → Leave Dev Current Value inside exported solution → Grant `Anonymous` public access on Key Vault → Share Dev Vault across Prod',
        'Leaving Current Values in exported solutions binds downstream environments to Dev resources, and Azure Key Vault never permits anonymous secret reads.',
    ),

    # 3. Domain 2 (2.5): Create, test, package & deploy PCF code component
    'seq_pcf_deploy_ok': (
        'Scaffold control with `pac pcf init` & `npm install` → Implement manifest + `index.ts` & test in `npm start watch` → Link via `pac solution init` + `pac solution add-reference` → Build Release Managed ZIP (`msbuild`) & import to Prod',
        'Production PCF deployment scaffolds the control, verifies lifecycle logic locally, links the PCF project into a `.cdsproj` solution via `pac solution add-reference`, and builds a Release Managed ZIP (`pac pcf push` is Dev-only).',
    ),
    'seq_pcf_deploy_bad_push_prod': (
        'Scaffold control with `pac pcf init` → Skip `ControlManifest.Input.xml` → Run `pac pcf push` directly against Production Managed Environment → Edit bundled `bundle.js` manually in Production',
        '`pac pcf push` creates a temporary unmanaged `PowerAppsTools` publisher solution for developer inner-loop testing and should never be used for Production deployments.',
    ),
    'seq_pcf_deploy_bad_order': (
        'Run `pac solution init` first without any PCF project → Import empty ZIP to Prod → Run `pac pcf init` inside browser DevTools → Register `index.ts` in Plug-in Registration Tool',
        'PCF components are client-side TypeScript/JavaScript controls packaged via `.cdsproj` solutions, not server-side assemblies registered in the Plug-in Registration Tool.',
    ),
    'seq_pcf_deploy_bad_webres': (
        'Compile TypeScript manually → Upload `index.ts` as an HTML Web Resource → Rename `.html` to `.pcfproj` inside Classic Solution Explorer → Publish All Customizations',
        'Uploading TypeScript source as an HTML web resource does not register a custom control manifest or invoke PCF `init`/`updateView` lifecycle hooks.',
    ),

    # 4. Domain 2 (2.6/2.8/2.9): Build, wire Dataverse & App Insights CSP, and publish a Power Apps code app
    'seq_codeapp_ship_ok': (
        'Initialize project with `pa app init` → Add Dataverse tables/APIs via `pa app add data-source` & test with `pa app run` → Allowlist App Insights/frame hosts in Code App CSP (`connect-src` / `frame-ancestors`) → Publish & grant access via `pa app push` + `pa app share`',
        'Power Apps code apps initialize via `pa app init`, generate typed services via `pa app add data-source`, require CSP `connect-src`/`frame-ancestors` allowlisting, and deploy via `pa app push` + `pa app share`.',
    ),
    'seq_codeapp_ship_bad_nocsp': (
        'Upload raw Vite folder as a Dataverse plug-in package → Disable Entra authentication → Skip CSP `connect-src` so App Insights requests fail in browser → Share raw localhost URL with external users',
        'Plug-in packages run server-side .NET code, code apps enforce `connect-src: none` by default (blocking App Insights until allowlisted), and localhost dev URLs cannot serve tenant users.',
    ),
    'seq_codeapp_ship_bad_order': (
        'Run `pa app share` before `pa app init` → Hardcode admin passwords in `power.config.json` → Bypass Dataverse security roles → Deploy via Classic Ribbon Workbench',
        'A code app must be initialized and pushed (`pa app push`) before sharing, uses delegated Power Platform connections rather than hardcoded credentials, and is unrelated to Ribbon Workbench.',
    ),
    'seq_codeapp_ship_bad_iframe_ext': (
        'Initialize with `pac plugin init` → Add FetchXML & polymorphic lookups to generated code-app service → Leave default `frame-ancestors` unchanged when framing in Dynamics → Share iframe outside tenant',
        '`pac plugin init` scaffolds C# plug-ins, code-app generated services do not support FetchXML or polymorphic lookups, Dynamics framing requires updating `frame-ancestors`, and external-tenant sharing is unsupported.',
    ),

    # 5. Domain 3 (3.4): Configure Power Platform Managed Identity v2 for a Dataverse Plug-in
    'seq_plugin_mi_ok': (
        'Create Entra App Registration or UAMI → Build, sign, and register plug-in assembly/package → Configure Entra Federated Identity Credential (DN hash) → Bind `managedidentity` row in Dataverse & call `IManagedIdentityService.AcquireToken`',
        'Managed Identity v2 links a certificate-signed plug-in assembly/package to an Entra App Registration/UAMI via Federated Identity Credentials (DN hash) and `IManagedIdentityService.AcquireToken` with zero stored secrets.',
    ),
    'seq_plugin_mi_bad_secret': (
        'Create Entra client secret → Hardcode client secret inside `Unsecure Configuration` XML in Plug-in Registration Tool → Register unsigned assembly in Isolation Mode `None` → Call `HttpClient` with static bearer token',
        'Unsecure Configuration is readable by any environment user, Dataverse online requires `Sandbox` isolation mode, and Managed Identity eliminates client secrets altogether.',
    ),
    'seq_plugin_mi_bad_order': (
        'Call `IManagedIdentityService` inside JavaScript form `OnLoad` → Skip certificate signing on the `.dll`/`.nupkg` → Omit Federated Identity Credential in Entra ID → Grant `System Administrator` to `Everyone`',
        '`IManagedIdentityService` is a server-side `Microsoft.Xrm.Sdk` C# plug-in interface requiring a certificate-signed assembly and matching Entra Federated Identity Credential.',
    ),
    'seq_plugin_mi_bad_v1_unsigned': (
        'Enable System-Assigned Managed Identity on the developer laptop → Upload unsigned `.cs` source file to SharePoint → Skip `managedidentity` Dataverse binding → Acquire token via `Xrm.Utility`',
        'Developer machine identities do not run inside the Dataverse sandbox; Entra federation must trust the Dataverse plug-in issuer/subject certificate hash and bind a `managedidentity` record.',
    ),

    # 6. Domain 3 (3.12/3.13): Integrate a custom Microsoft Foundry agent with Dataverse MCP & Copilot Studio
    'seq_foundry_mcp_ok': (
        'Enable Dataverse MCP server & allowlist MCP client in PPAC → Assign least-privilege Dataverse Security Role to caller → Connect Foundry agent to `https://{org}.crm.dynamics.com/api/mcp` & Work IQ skills → Invoke `search`/`read_query`/`update_record` with approval on deletes',
        'Dataverse MCP requires enabling `/api/mcp` and external MCP clients in PPAC, enforces native Dataverse security roles, connects to `https://{org}.crm.dynamics.com/api/mcp`, and requires user confirmation for destructive tools.',
    ),
    'seq_foundry_mcp_bad_bypass': (
        'Disable Dataverse security roles → Point Foundry agent at SQL TDS admin port with SA password → Call removed legacy `list_tables` and `fetch` MCP tools → Auto-execute `delete_table` silently without user approval',
        'Dataverse never exposes SA SQL write access, legacy `list_tables`/`fetch` MCP tools were replaced by `search`/`describe`, external MCP clients must be allowlisted, and `delete_table` requires explicit user approval.',
    ),
    'seq_foundry_mcp_bad_order': (
        'Call `https://{org}.crm.dynamics.com/api/mcp` before enabling external MCP clients in PPAC → Hardcode personal maker cookies in source control → Grant `System Administrator` to all agents → Store skills outside Dataverse',
        'Non-Copilot-Studio MCP clients are disabled by default until enabled in PPAC, cookies expire and violate security, and least-privilege Dataverse security roles must govern agent access.',
    ),
    'seq_foundry_mcp_bad_unsec': (
        'Export entire Dataverse database to public CSV nightly → Disable Managed Environment DLP policies → Connect Foundry agent without OAuth token → Overwrite Dataverse GUIDs randomly',
        'Public CSV dumps violate governance and stale instantly whereas `/api/mcp` provides live OAuth-secured role-trimmed tool access.',
    ),

    # 7. Domain 4 (4.3/4.4): Incremental External Synchronization with Change Tracking + Alternate Key Upsert
    'seq_sync_delta_ok': (
        'Enable `Change Tracking` & create `Alternate Key` on natural ID → Run initial sync with `Prefer: odata.track-changes` & save `@odata.deltaLink` → Poll deltas with `deltaLink` (plus `@odata.removed`) → Apply idempotent `Upsert` writes via Alternate Key',
        'Scalable Dataverse sync uses `Prefer: odata.track-changes` + `@odata.deltaLink` to fetch only changed/deleted rows since the watermark and `Alternate Keys` + `Upsert` to avoid extra `Retrieve` round-trips.',
    ),
    'seq_sync_delta_bad_fullscan': (
        'Disable `Change Tracking` → Query every row with `SELECT *` every 5 minutes → Issue separate `RetrieveMultiple` lookup before every single row write → Delete and recreate the target table on schema ties',
        'Full-table polling and per-row pre-read lookups exhaust Dataverse service protection API limits (`429`) and miss hard-deleted record tombstones.',
    ),
    'seq_sync_delta_bad_order': (
        'Send an invented `deltaLink` token before running an initial sync → Create an Alternate Key on a `Memo` (`Multiline Text`) column → Ignore `@odata.removed` entries → Use synchronous `PreValidation` plug-ins for bulk batch imports',
        '`deltaLink` tokens come from Dataverse responses, Alternate Keys only support indexed types (Decimal, Whole Number, Single Line of Text, Date, Lookup — never Memo), and ignoring `@odata.removed` orphans deleted rows.',
    ),
    'seq_sync_delta_bad_guid': (
        'Force the external mainframe to re-key its primary database with Dataverse GUIDs → Poll `audit` log strings via client-side JavaScript `setInterval` → Run single-row sequential HTTP calls without retry backoff → Omit error logs',
        'External systems keep their natural keys via Dataverse `Alternate Keys`, and sync belongs in back-end services using `Change Tracking` + `Retry-After` backoff.',
    ),

    # 8. Domain 4 (4.5/4.6): Build & Govern an Enterprise Custom Connector with Policy Templates + C# Custom Code
    'seq_custom_conn_ok': (
        'Import OpenAPI spec into a solution-aware Custom Connector → Configure Entra OAuth 2.0 & Connection Reference → Add `Set host URL`/`Set HTTP header` Policy Templates with Environment Variables → Implement `ScriptBase.ExecuteAsync` C# transform & deploy Managed',
        'Enterprise custom connectors live in Dataverse solutions, authenticate via OAuth 2.0 + Connection References, switch stage hosts via Policy Templates + Environment Variables, and reshape payloads in `ScriptBase.ExecuteAsync`.',
    ),
    'seq_custom_conn_bad_default': (
        'Create custom connector outside any solution in Prod → Hardcode static API key directly inside OpenAPI `description` text → Rewrite backend ERP API from scratch to match Power Apps → Copy-paste connector manually across environments',
        'Non-solution connectors break ALM pipelines, plaintext keys in descriptions leak credentials, and `ScriptBase` C# transformations + Policy Templates avoid rewriting backend APIs.',
    ),
    'seq_custom_conn_bad_order': (
        'Deploy connector to Production before defining operations → Use `Anonymous` authentication for confidential payroll APIs → Run 15-minute batch loops inside `ScriptBase.ExecuteAsync` → Bypass DLP connector classification',
        'Custom connector C# `ScriptBase.ExecuteAsync` enforces strict execution limits (5-second script timeout / 1 MB payload) and must be classified under tenant/environment DLP policies.',
    ),
    'seq_custom_conn_bad_iframe': (
        'Upload Postman v1 collection into Plug-in Registration Tool → Store OAuth client secret in a Canvas `Set()` global variable → Skip `x-ms-dynamic-values` → Share maker personal connection directly with 2,000 users',
        'Custom connectors are managed in Power Apps/Power Automate Solutions (or `pac connector`), never Plug-in Registration Tool, and client secrets never belong in Canvas client memory.',
    ),
}
