# Curriculum Outline — Microsoft Exam PL-400 (`AB-400` Transition Blueprint)

Aligned to Microsoft Learn's **October 16, 2026** skills outline for **`Microsoft Certified: Power Platform Developer Associate`** (**Exam PL-400: Microsoft Power Platform Developer**, retiring **October 30, 2026** at 11:59 PM CST after registration closed October 16, 2026, and transitioning directly to **Exam AB-400: Extending Microsoft Power Platform Solutions with Code and AI** on the identical 4-domain blueprint; passing scaled score **`700 / 1000`**; no prerequisite exam required).

---

## Six Full-Length Practice Exams (`6 × 100 = 600` Questions)

| Practice Test | Industry Focus & 4 Original Enterprise Case Studies (`3` Qs Each) | D1 (15–20%) | D2 (25–30%) | D3 (35–40%) | D4 (10–15%) | Total |
|---|---|---:|---:|---:|---:|---:|
| **Mock Exam 1** | **Commercial Banking & Wealth:** Crestline Commercial Bank · LoanBridge Underwriting · VaultSure Escrow · Kestrel Wealth Advisory | 18 | 28 | 39 | 15 | **100** |
| **Mock Exam 2** | **Healthcare & Specialty Pharmacy:** Veridian Health Network · CarePath Triage · OrthoPulse Clinics · BioLink Specialty Pharmacy | 18 | 28 | 39 | 15 | **100** |
| **Mock Exam 3** | **Field Robotics, Wind Energy & Fleet:** ApexGrid Field Robotics · TurbineCare Energy · MetroLift Elevators · CryoTech Fleet Services | 18 | 28 | 39 | 15 | **100** |
| **Mock Exam 4** | **Omnichannel Retail & Wholesale:** Lumina Luxe Retail · SwiftCart Returns · PalletCore Wholesale · Atelier Direct Brands | 18 | 28 | 39 | 15 | **100** |
| **Mock Exam 5** | **Public Sector, Maritime Port & Transit:** CivicBridge Permitting · HarborGate Port Authority · TransitLink Metro · GreenPark Inspections | 18 | 28 | 39 | 15 | **100** |
| **Mock Exam 6** | **Aerospace Manufacturing & Defense MRO:** StratosAero Manufacturing · Avionix Precision Parts · OrbitLine Defense Supply · JetStream MRO Operations | 18 | 28 | 39 | 15 | **100** |
| **Course Total** | **24 Original Enterprise Case Studies (`72` Case Items + `528` Standalone Items)** | **108** | **168** | **234** | **90** | **600** |

---

## Per-Skill Question Quota Across Every Mock Exam (`36` Skills = `100` / Exam)

### Domain 1 — Build Microsoft Power Platform solutions (`18` / exam · `108` total)
| Skill | Official Topic Coverage | Per Exam | 6-Exam Total |
|---|---|---:|---:|
| `1.1` | Technical architecture, Entra OBO vs S2S Application Users, Power Fx formula & rollup columns vs custom code | 2 | 12 |
| `1.2` | Business-logic placement (synchronous plug-in vs Entity Business Rule vs Client JS) & deterministic vs AI methods | 2 | 12 |
| `1.3` | Standard tables vs Virtual tables vs Cosmos DB Elastic tables (`ttlinseconds`) vs direct connectors | 2 | 12 |
| `1.4` | Managed Environments, DLP policies, Modernized Business Units (matrix), Access Team Templates & Column Security | 2 | 12 |
| `1.5` | UX & AI platform selection: Power Apps code apps, generative pages (`/genpage`), PCF vs web resources, MCP UI widgets, Foundry vs Copilot Studio | 2 | 12 |
| `1.6` | Reusable segmented solutions, Data Source/Secret environment variables, Solution Checker, Application Insights & Monitor alerts | 3 | 18 |
| `1.7` | Solution dependencies, unmanaged active layer remediation, Managed Upgrade vs Update & Azure Key Vault secrets | 3 | 18 |
| `1.8` | Power Platform Pipelines extensibility (`OnApprovalStarted`) & Git CI/CD with PAC CLI / Build Tools (`--packagetype Both`) | 2 | 12 |

### Domain 2 — Extend the user experience (`28` / exam · `168` total)
| Skill | Official Topic Coverage | Per Exam | 6-Exam Total |
|---|---|---:|---:|
| `2.1` | Model-driven JavaScript (`executionContext.getFormContext`, sync/async `OnSave` `preventDefault`, `SaveMode`, `addPreSearch`, `addTabStateChange`) | 3 | 18 |
| `2.2` | Client scripting with `Xrm.WebApi` (`@odata.bind`, `$select`/`$expand`, and `Xrm.WebApi.online.execute` for Custom APIs) | 2 | 12 |
| `2.3` | Modern command buttons (Power Fx `Visible` + ES6 JS) & `Xrm.Navigation` (`sidePanes`, `navigateTo` modals, confirm dialogs, notifications) | 3 | 18 |
| `2.4` | PCF `ControlManifest.Input.xml` (`bound` vs `input`), lifecycle (`init`/`updateView`/`getOutputs`/`destroy`), and virtual React controls | 4 | 24 |
| `2.5` | PCF `.cdsproj` `Release` packaging, `<uses-feature>` (`Device.captureImage`, `Utility`, `WebAPI`), dataset paging/sorting & `trackContainerResize` | 4 | 24 |
| `2.6` | Power Apps code apps (`pa app init`, `@microsoft/power-apps`, `add data-source`, Entra SQL connections & generated service boundaries) | 4 | 24 |
| `2.7` | Code apps invoking Dataverse APIs (`add dataverse-api`), cloud flows (`add flow`), environment variables & Copilot Studio agents | 3 | 18 |
| `2.8` | Code app Content Security Policy (`Set-CodeAppContentSecurityPolicy`, `connect-src`, same-tenant `frame-ancestors`) & Application Insights | 3 | 18 |
| `2.9` | Packaging, sharing (`pa app push | share` + Dataverse security roles), debugging (Monitor/DevTools) & Vite code-splitting | 2 | 12 |

### Domain 3 — Extend Microsoft Power Platform (`39` / exam · `234` total)
| Skill | Official Topic Coverage | Per Exam | 6-Exam Total |
|---|---|---:|---:|
| `3.1` | C# `IPlugin` stages (`PreValidation` 10, `PreOperation` 20 `Target` mutation, sync/async `PostOperation` 40), Filtering Attributes & `SharedVariables` | 3 | 18 |
| `3.2` | Pre/Post Entity Images, explicit `ColumnSet` queries & stateless thread-safe `IPlugin` design | 3 | 18 |
| `3.3` | Dataverse Custom APIs (`IsFunction`, `IsPrivate`, `AllowedCustomProcessingStepType`), `InvalidPluginExecutionException` & Business Events catalog | 3 | 18 |
| `3.4` | NuGet `.nupkg` plug-in packages (`pluginpackage`) & Power Platform Managed Identity v2 (`IManagedIdentityService.AcquireToken`) | 3 | 18 |
| `3.5` | Dataverse Web API `$batch` atomic changesets, `Prefer` headers, `@odata.bind` & `QueryExpression` `PagingCookie` pagination | 3 | 18 |
| `3.6` | HTTP `429` `Retry-After` resilience, optimistic concurrency (`If-Match` / `IfRowVersionMatches`), `CreateMultiple`/`UpdateMultiple` & `BypassBusinessLogicExecution` | 3 | 18 |
| `3.7` | Asynchronous Dataverse background operations (`Prefer: respond-async`), `.NET` `ServiceClient.Clone()` & Dataverse SDK for Python | 3 | 18 |
| `3.8` | Offloading >2-minute / high-memory workloads to Azure Functions (Service Bus, Event Hubs, HTTP webhook & timer triggers) | 3 | 18 |
| `3.9` | Secretless Azure Functions authentication to Dataverse via Managed Identities + least-privilege Application Users | 2 | 12 |
| `3.10` | Power Automate WDL expressions (`coalesce`, `?` safe navigation), Dataverse trigger filtering/conditions & action retry policies | 3 | 18 |
| `3.11` | `Try`/`Catch` `Scope` error handling (`result()` + `Terminate`), solution-aware SPN child flows & Copilot Studio agent flows | 4 | 24 |
| `3.12` | Integrating custom Microsoft Foundry agents with Dataverse MCP (`/api/mcp`) and publishing **Work IQ** reusable skills | 3 | 18 |
| `3.13` | Connecting Foundry & web apps to Copilot Studio agents via `@microsoft/agents-copilotstudio-client` / `.NET` `CopilotClient` & OAuth consent cards | 3 | 18 |

### Domain 4 — Develop integrations (`15` / exam · `90` total)
| Skill | Official Topic Coverage | Per Exam | 6-Exam Total |
|---|---|---:|---:|
| `4.1` | Publishing Dataverse events via Plug-in Registration Tool & `IServiceEndpointNotificationService` (Webhooks, Service Bus, Event Hubs) | 3 | 18 |
| `4.2` | Event-listening architectures: Asynchronous `PostOperation` transactional outbox, Service Bus sessions/DLQ, Event Hubs streaming & Event Grid | 2 | 12 |
| `4.3` | Incremental data synchronization with Dataverse Change Tracking (`Prefer: odata.track-changes`, `@odata.deltaLink`, `@odata.removed`) | 2 | 12 |
| `4.4` | Active Alternate Keys & conditional idempotent upserts (`PATCH` / `UpsertRequest`, `If-None-Match: *`, `If-Match: *`) | 3 | 18 |
| `4.5` | Solution-aware custom connectors from OpenAPI/APIM/Functions, Entra OAuth 2.0, Connection References & runtime Policy Templates | 3 | 18 |
| `4.6` | OpenAPI extensions (`x-ms-dynamic-values`, `x-ms-dynamic-schema`, `x-ms-visibility`) & inline C# custom code (`ScriptBase.ExecuteAsync`) | 2 | 12 |
