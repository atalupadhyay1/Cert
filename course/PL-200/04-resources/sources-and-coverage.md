# 🔗 Official Microsoft Learn Sources & 43-Skill Coverage (`PL-200`)

## 1. Authoritative Exam & Lifecycle References (Verified October 30, 2026)

| Reference | Official URL | Key Verified Fact |
|---|---|---|
| **Exam PL-200 Study Guide** | `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200` | Final published **December 26, 2024** skills outline (`4` domains: `25–30%`, `25–30%`, `25–30%`, `15–20%`), `700 / 1000` scaled score, 7 exam languages |
| **Functional Consultant Associate Credential** | `https://learn.microsoft.com/en-us/credentials/certifications/power-platform-functional-consultant-associate/` | Associate (`Intermediate`) role-based credential; **no mandatory prerequisite exam**; retired **August 31, 2026** |
| **Retired Microsoft Certification Exams** | `https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams` | Confirms **Exam PL-200** retired **August 31, 2026** (`11:59 PM CST`) and was succeeded by **Exam AB-410: Building Intelligent Applications** (`Intelligent Applications Builder Associate`) |

---

## 2. Complete 43-Skill Documentation Traceability Matrix

Every `Overall Explanation` cell in all `600` questions links directly to its corresponding Microsoft Learn documentation page from `04-resources/sources.py`:

| Skill ID | Official PL-200 Skill Area | Items / Exam | 6-Exam Total | Primary Microsoft Learn Reference |
|---|---|---:|---:|---|
| `1.1` | Standard, Activity, and Virtual tables & table properties | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/types-of-entities` |
| `1.2` | `1:N` and `N:N` (native vs manual intersect) relationships | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships` |
| `1.3` | Table relationship behaviors & cascading rules | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup` |
| `1.4` | Columns, Alternate Keys, Rollups & Power Fx Formula columns | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns` |
| `1.5` | Dataverse Search, Quick Find views & search index | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization` |
| `1.6` | Environment, table, and column-level Auditing & retention | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing` |
| `1.7` | Importing & exporting data (Excel, Dataflows, Fabric/Synapse Link) | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export` |
| `1.8` | Duplicate Detection rules & scheduled Bulk Record Deletion | 3 | 18 | `https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean` |
| `1.9` | Business Units & Modernized Business Units (matrix access) | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds` |
| `1.10` | Custom Security Roles (`Append`/`Append To`, privilege inheritance) | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges` |
| `1.11` | Users, Owner Teams, Access Team Templates & Entra ID Group Teams | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/manage-teams` |
| `1.12` | Column Security Profiles & Hierarchy Security (`Manager` vs `Position`) | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/field-level-security` |
| `2.1` | Model-driven Sitemaps & form types (`Form Order` & `Fallback`) | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/control-access-forms` |
| `2.2` | Specialized form controls (`Editable Grid`, `Form Component Control`) | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control` |
| `2.3` | Dataverse Views (`Public`, `Quick Find`, `Lookup`, `Associated`, `Personal`) | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views` |
| `2.4` | Custom Pages in model-driven apps & `Param("recordId")` | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview` |
| `2.5` | Modern Commanding with Power Fx & Component Libraries | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-overview` |
| `2.6` | Embedded Canvas apps (`ModelDrivenFormIntegration`) & Power BI | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form` |
| `2.7` | Canvas responsive auto-layout containers & Component Libraries | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout` |
| `2.8` | Canvas navigation, variables, collections, delegation & `IfError` | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview` |
| `2.9` | Calling cloud flows from Canvas apps (`Power Apps (V2)` & `Run-only`) | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows` |
| `2.10` | Power Pages webpages, Basic Forms, Lists & Design Studio `Sync` | 2 | 12 | `https://learn.microsoft.com/en-us/power-pages/configure/entity-forms` |
| `2.11` | Power Pages Multi-Step Forms, SharePoint, search & Power BI RLS | 2 | 12 | `https://learn.microsoft.com/en-us/power-pages/configure/configure-web-form-steps` |
| `2.12` | Power Pages Table Permissions, Web Roles, Page Access & Entra External ID | 3 | 18 | `https://learn.microsoft.com/en-us/power-pages/security/table-permissions` |
| `3.1` | Cloud flows vs classic Dataverse workflows vs Business Process Flows | 2 | 12 | `https://learn.microsoft.com/en-us/power-automate/overview-cloud` |
| `3.2` | Connector triggers, webhooks vs polling & Connection References | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference` |
| `3.3` | Cloud flow logic controls (`Scope`, `Concurrency`, `Terminate`, `Compose`) | 3 | 18 | `https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions` |
| `3.4` | Dynamic content, WDL expressions & Trigger Conditions | 3 | 18 | `https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference` |
| `3.5` | Dataverse connector (`Select`, `Filter`, `Expand`, `Relate`, Child Flows) | 3 | 18 | `https://learn.microsoft.com/en-us/power-automate/dataverse/overview` |
| `3.6` | Flow Checker, Static Result testing, Run History & `Run-only users` | 2 | 12 | `https://learn.microsoft.com/en-us/power-automate/fix-flow-failures` |
| `3.7` | Business Process Flows (`<= 30` stages, branching, `<= 5` tables, ordering) | 2 | 12 | `https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview` |
| `3.8` | BPF classic workflow & cloud flow steps + BPF Dataverse table | 2 | 12 | `https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow` |
| `3.9` | Synchronous (`Real-time`) & asynchronous (`Background`) classic workflows | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows` |
| `3.10` | Classic workflow troubleshooting (`System Jobs`) & log retention | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes` |
| `3.11` | Dataverse low-code Power Fx plug-ins (`Dataverse Accelerator`) | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins` |
| `3.12` | Dataverse Business Rules (`Scope` & limits) & Power Fx Functions | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule` |
| `4.1` | `App Checker` vs `Solution Checker` static analysis | 2 | 12 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker` |
| `4.2` | Custom Publishers, Segmented Solutions & `Clone a Patch`/`Clone to Solution` | 3 | 18 | `https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm` |
| `4.3` | Managed vs Unmanaged Solutions, Solution Layers & `Upgrade` vs `Update` | 3 | 18 | `https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm` |
| `4.4` | Sandbox `Full` vs `Minimal` Copy, Backups, DLP & Managed Environments | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/copy-environment` |
| `4.5` | Solution import/export with Environment Variables, Connection Refs & pipelines | 3 | 18 | `https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables` |
| `4.6` | Email Integration (`Server-Side Synchronization`, Mailboxes, Queues, Outlook) | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization` |
| `4.7` | SharePoint Document Management (ACLs) & Microsoft Word Templates (`<= 100` rows) | 2 | 12 | `https://learn.microsoft.com/en-us/power-platform/admin/set-up-dynamics-365-online-to-use-sharepoint-online` |
