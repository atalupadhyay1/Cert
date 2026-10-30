# Official Microsoft Learn Sources & 42-Skill Coverage Matrix (`PL-500`)

## Primary Official References (Verified October 30, 2026)

- **Official Exam PL-500 Study Guide (`Skills measured as of July 8, 2024`):** <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500>
- **Power Automate RPA Developer Associate Credential Page:** <https://learn.microsoft.com/en-us/credentials/certifications/power-automate-rpa-developer-associate/>
- **Microsoft Retired Certification Exams Notice (`PL-500` retired June 30, 2026):** <https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams>
- **Power Automate Documentation Hub (Cloud Flows, Desktop Flows, Work Queues, Custom Actions, Hosted RPA, DLP & ALM):** <https://learn.microsoft.com/en-us/power-automate/>

> **Lifecycle Note:** Microsoft retired Exam `PL-500`, its certification, renewal assessment, and courseware `PL-500T00` on **June 30, 2026** (`11:59 PM CST`) without a 1:1 replacement RPA exam (broader Business Applications developer/AI skilling transitioned to **Exams AB-400 / AB-410** and Power Automate **Applied Skills**).

---

## 42-Skill Traceability Table (`100` Items/Exam × `6` Exams = `600` Items)

| Skill ID | Domain | Official Study-Guide Skill | Per Exam | 6-Set Total | Primary Microsoft Learn Reference |
|---|---:|---|---:|---:|---|
| `1.1` | 1 | Differentiate cloud vs desktop flows, triggers, & hybrid RPA | 3 | 18 | `power-automate/overview-cloud` |
| `1.2` | 1 | Differentiate Win32, web, terminal (`3270`/`5250`), & VDI options | 3 | 18 | `power-automate/desktop-flows/virtual-desktops` |
| `1.3` | 1 | Differentiate desktop flow run methods (`ms-powerautomate:`) & concurrency | 2 | 12 | `power-automate/desktop-flows/run-pad-flow-url` |
| `1.4` | 1 | Recommend Attended vs Unattended & cloud vs desktop HTTP | 3 | 18 | `power-automate/desktop-flows/run-unattended-desktop-flows` |
| `1.5` | 1 | Assess Work Queues applicability & design `.NET` custom actions | 3 | 18 | `power-automate/desktop-flows/work-queues` |
| `1.6` | 1 | Integrate Canvas apps, Model-driven apps, & Microsoft Dataverse | 2 | 12 | `power-automate/dataverse/overview` |
| `1.7` | 1 | Design connectors, Custom Connectors, Connections, & Connection Refs | 2 | 12 | `power-apps/maker/data-platform/create-connection-reference` |
| `1.8` | 1 | Differentiate AI Builder document/data models & desktop OCR | 3 | 18 | `power-automate/desktop-flows/actions-reference/ocr` |
| `1.9` | 1 | Recommend & design with Document Automation Toolkit | 2 | 12 | `ai-builder/doc-automation` |
| `1.10` | 1 | Design scripting (`PowerShell`, `VBScript`, `Python`, `DOS`) in PAD | 2 | 12 | `power-automate/desktop-flows/actions-reference/system` |
| `1.11` | 1 | Recommend `ExecuteScript()` web JavaScript & DOM CSS/XPath | 3 | 18 | `power-automate/desktop-flows/actions-reference/webautomation` |
| `2.1` | 2 | Develop cloud flows invoking attended & unattended desktop flows | 2 | 12 | `power-automate/desktop-flows/trigger-desktop-flows` |
| `2.2` | 2 | Develop & invoke modular solution Child cloud flows | 2 | 12 | `power-automate/create-child-flows` |
| `2.3` | 2 | Call external REST APIs in cloud flows (auth & pagination) | 2 | 12 | `azure/connectors/connectors-native-http` |
| `2.4` | 2 | Implement cloud Trigger Conditions, Concurrency, & `Split On` | 2 | 12 | `power-automate/use-expressions-in-conditions` |
| `2.5` | 2 | Implement cloud ISO 8601 action Timeouts & Retry Policies | 2 | 12 | `power-automate/retry-policy` |
| `2.6` | 2 | Implement cloud Data Operations (`Compose`, `Parse JSON`, `Select`, `Filter`) | 2 | 12 | `power-automate/data-operations` |
| `2.7` | 2 | Parse `JSON`, `XML` (`xpath`/`xml`), & `CSV` in cloud flows | 2 | 12 | `azure/logic-apps/workflow-definition-language-functions-reference` |
| `2.8` | 2 | Implement UI elements, dynamic `%Variable%` selectors, fallbacks, & terminals | 3 | 18 | `power-automate/desktop-flows/build-custom-selectors` |
| `2.9` | 2 | Implement `Datatables`, `Lists`, & `Custom Objects` in PAD | 2 | 12 | `power-automate/desktop-flows/variable-data-types` |
| `2.10` | 2 | Implement `Subflows` & app lifecycle (`Stop flow` vs `Exit subflow`) | 2 | 12 | `power-automate/desktop-flows/subflows` |
| `2.11` | 2 | Call REST (`Encode request body = Off`) & SOAP APIs in PAD | 2 | 12 | `power-automate/desktop-flows/actions-reference/web` |
| `2.12` | 2 | Implement PAD action `On error` retries & `Wait` content timeouts | 2 | 12 | `power-automate/desktop-flows/errors` |
| `2.13` | 2 | Automate Excel, SQL, PDF, & JSON/XML/CSV parsing in PAD | 2 | 12 | `power-automate/desktop-flows/actions-reference/variables` |
| `2.14` | 2 | Build, sign, package (`.cab`), & upload `.NET` Custom Actions | 2 | 12 | `power-automate/desktop-flows/create-custom-actions` |
| `2.15` | 2 | Implement loops, flow control, WDL expressions, & variables | 2 | 12 | `power-automate/desktop-flows/actions-reference/loops` |
| `2.16` | 2 | Implement `Secure Inputs/Outputs`, `Sensitive` vars, & queue `Priority` | 2 | 12 | `power-automate/desktop-flows/manage-variables` |
| `2.17` | 2 | Implement System Exception blocks vs Business Exception routines | 3 | 18 | `power-automate/desktop-flows/errors` |
| `2.18` | 2 | Implement `Work Queues` (enqueue, lease, update, delayed requeue) | 3 | 18 | `power-automate/desktop-flows/work-queues-actions` |
| `2.19` | 2 | Build Custom Connectors, auth, policy templates, & C# `ScriptBase` | 3 | 18 | `connectors/custom-connectors/write-code` |
| `2.20` | 2 | Manage Key Vault/CyberArk `Credentials`, Gateways, & Solutions | 3 | 18 | `power-automate/desktop-flows/credentials-management` |
| `2.21` | 2 | Test, debug (`Static Result`, Breakpoints), & externalize configs | 3 | 18 | `power-automate/desktop-flows/debugging` |
| `3.1` | 3 | Implement Power Platform ALM, Managed `Upgrade`, & `Solution Layers` | 3 | 18 | `power-automate/alm` |
| `3.2` | 3 | Differentiate stage `Credentials`, `Connection References`, & bindings | 2 | 12 | `power-automate/desktop-flows/alm` |
| `3.3` | 3 | Prepare VMs (`Sign out`), Windows Server `RDSH`, & `Hosted RPA` | 3 | 18 | `power-automate/desktop-flows/hosted-rpa` |
| `3.4` | 3 | Assess Power Platform DLP & **Desktop Flow module/action DLP** | 3 | 18 | `power-platform/admin/dlp-desktop-flows` |
| `3.5` | 3 | Configure DLP endpoint filtering & Custom Connector URL patterns | 2 | 12 | `power-platform/admin/dlp-custom-connector-parity` |
| `3.6` | 3 | Share cloud flows, desktop flows (`User` vs `Co-owner`), & machine pools | 3 | 18 | `power-automate/desktop-flows/manage-machines` |
| `3.7` | 3 | Configure RPA security roles & Service Principals vs Windows accounts | 2 | 12 | `power-automate/desktop-flows/governance` |
| `3.8` | 3 | Register machines via `Power Automate machine runtime` & groups | 2 | 12 | `power-automate/desktop-flows/manage-machines` |
| `3.9` | 3 | Load-balance unattended desktop flows across Machine Groups | 2 | 12 | `power-automate/desktop-flows/monitor-desktop-flow-queues` |
| `3.10` | 3 | Operate Run Queues (`Priority`, `Move to top`, `Cancel`) & Run History | 2 | 12 | `power-automate/desktop-flows/monitor-desktop-flows` |
