# Official Sources, Lifecycle Disclosures & 34-Skill Coverage Matrix (Exam AZ-400)

## 1. Authoritative Primary Sources (Retrieved October 29, 2026)

1. **Official AZ-400 Study Guide (`Skills measured as of July 27, 2026`, updated `06/26/2026`):**
   `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400`
2. **Official Exam AZ-400 Overview Page:**
   `https://learn.microsoft.com/en-us/credentials/certifications/exams/az-400/`
3. **Official `Microsoft Certified: DevOps Engineer Expert` Certification Page (Prerequisite Rules):**
   `https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/`
4. **Official Microsoft Skills Hub Announcement (October 15, 2026 — `AZ-401` Beta & `AZ-400` February 1, 2027 Retirement):**
   `https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-agentic-devops-engineer-expert/4528356`
5. **Official Exam Duration, Split-Screen Microsoft Learn Access & Scoring (`700 / 1000`):**
   `https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience`

---

## 2. Lifecycle, Prerequisite & Scope Hygiene Notes

- **Expert Certification Prerequisite:** Earning `Microsoft Certified: DevOps Engineer Expert` requires passing **AZ-400** PLUS holding an active **AZ-104** (`Azure Administrator Associate`) or an active **AZ-204** (`Azure Developer Associate`, earned before its July 31, 2026 retirement).
- **Scheduled Retirement & Transition:** On October 15, 2026, Microsoft announced **Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions** (`Agentic DevOps Engineer Expert`, prereqs `GH-300` or `AZ-104`) and scheduled **Exam AZ-400 and `DevOps Engineer Expert` to retire on February 1, 2027**.
- **Removed Legacy Artifacts:** Obsolete pre-2024 TFS 2013/TFVC migration trivia, retired Log Analytics MMA (`OMSAgent`) workspace-key setups, and third-party plugin trivia outside the **July 27, 2026** blueprint have been replaced by modern Azure DevOps + GitHub Enterprise, Managed DevOps Pools, Workload Identity Federation (OIDC), GHAS/GHAzDO, Defender for Cloud DevOps Security, Bicep Deployment Stacks, Azure Machine Configuration, Azure Deployment Environments, and Azure Monitor Agent (AMA) Data Collection Rules.

---

## 3. Complete 34-Skill Coverage Matrix (`100` Questions/Set × `6` Sets = `600` Questions)

| Skill ID | Official Functional Group & Sub-Objective (July 27, 2026) | Per Set | 6-Set Total |
|---|---|---:|---:|
| **1.1** | Traceability & flow of work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI) | 4 | 24 |
| **1.2** | DevOps metrics & queries (Cycle Time, Lead Time, CFD, Velocity/Burndown, DORA MTTR/CFR, WIQL, Analytics OData) | 4 | 24 |
| **1.3** | Collaboration & communication (Wikis, Mermaid, auto release notes, OpenAPI, Webhooks, `AB#` links, Teams apps) | 4 | 24 |
| **2.1** | Branching strategies (trunk-based, feature, release, tag-based emergency hotfix, `git revert`) | 4 | 24 |
| **2.2** | PR workflows & merge restrictions (Azure Repos policies, squash/no-ff/semi-linear, GitHub rulesets, Merge Queue, `CODEOWNERS`) | 4 | 24 |
| **2.3** | Large files & Git scaling (`Git LFS`, `Scalar`, partial/shallow clone, `sparse-checkout`, submodules vs packages) | 3 | 18 |
| **2.4** | Repo permissions, signed annotated tags, `git reflog` recovery, and secret history purging (`git filter-repo` + rotation) | 2 | 12 |
| **3.1** | Package management tools (`Azure Artifacts` multi-protocol & Universal Packages, `GitHub Packages` `ghcr.io`/npm/Maven) | 2 | 12 |
| **3.2** | Package feeds, Upstream Sources, and feed promotion views (`@Local`, `@Prerelease`, `@Release`) | 3 | 18 |
| **3.3** | Dependency & artifact versioning (`SemVer 2.0.0`, `CalVer`, feed version immutability) | 3 | 18 |
| **3.4** | Quality & release gates (`Query Azure Monitor alerts`, `Query Work Items`, `Invoke REST API`/`Azure Function`) | 3 | 18 |
| **3.5** | Pipeline testing strategy (shift-left pyramid, `Azure Load Testing` `AzureLoadTest@1` `failureCriteria`) | 2 | 12 |
| **3.6** | Test execution, dynamic parallel slicing, `PublishTestResults@2` (`succeededOrFailed()`), and PR diff code coverage | 2 | 12 |
| **3.7** | `GitHub Actions` vs `Azure Pipelines` selection, Azure Pipelines GitHub App integration, and HMAC webhooks | 2 | 12 |
| **3.8** | Hosted, self-hosted, ephemeral ARC (`--ephemeral`), VMSS, and VNet-injected `Managed DevOps Pools` agents/runners | 3 | 18 |
| **3.9** | YAML trigger rules (`trigger`/`pr` path filters, cron `schedule`, `workflow_dispatch`, `repository_dispatch`, `resources.pipelines`) | 3 | 18 |
| **3.10** | Multi-stage YAML execution order, fan-out/fan-in `dependsOn`, compile/runtime/macro variables, and `strategy: matrix` | 3 | 18 |
| **3.11** | Reusable pipeline templates (`extends:` vs `template:`, GitHub `workflow_call` Reusable Workflows vs Composite Actions) | 2 | 12 |
| **3.12** | YAML Environments (Approvals, Business Hours, Branch Control, `lockBehavior: sequential`, `Required template` checks) | 2 | 12 |
| **3.13** | Progressive exposure deployments (Blue-Green, Canary traffic weights, Deployment Rings, A/B testing) | 3 | 18 |
| **3.14** | Dependency ordering, Expand-and-Contract DB rollouts, zero-downtime App Service slot warm-up/swaps, and rollback/hotfix | 3 | 18 |
| **3.15** | Dynamic feature flags with `Azure App Configuration Feature Manager` (`Microsoft.Targeting`, `Microsoft.TimeWindow`) | 2 | 12 |
| **3.16** | Container/binary/script & SQL deployments (state-based `SqlAzureDacpacDeployment@1` vs idempotent EF/Flyway migrations) | 3 | 18 |
| **3.17** | Infrastructure as Code testing & deployment (`Bicep` linting, ACR Private Module Registry, `what-if`, `Deployment Stacks`) | 3 | 18 |
| **3.18** | Desired State Configuration (`Azure Automation State Configuration`, `Azure Machine Configuration`) & `Azure Deployment Environments` | 3 | 18 |
| **3.19** | Pipeline health (`Flaky Test Management`, failure rate, duration) and migrating Classic UI pipelines/task groups to YAML | 2 | 12 |
| **3.20** | Pipeline optimization (`Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true`, tiered retention leases) | 3 | 18 |
| **4.1** | AuthN/AuthZ (Managed Identities, Workload Identity Federation, GitHub Apps, `GITHUB_TOKEN`, fine-grained PATs, fork PR safety) | 4 | 24 |
| **4.2** | Access levels & permissions (`Stakeholder` vs `Basic` vs `Basic + Test Plans`, GitHub `Outside collaborator`, explicit `Deny` rule) | 3 | 18 |
| **4.3** | Sensitive automation data (Key Vault Variable Groups, OIDC `id-token: write` & env `subject`, `Secure Files`, `issecret=true` masking) | 4 | 24 |
| **4.4** | Automated DevSecOps scanning (`GHAS` / `GHAzDO` Push Protection, `CodeQL`, `Dependabot`, `Defender for Cloud DevOps`, Trivy, DAST, OSS licenses) | 3 | 18 |
| **5.1** | DevOps environment monitoring (Workspace `Application Insights`, Release Annotations, `VM Insights` AMA/DCR, `Container/Storage/Network Insights`) | 3 | 18 |
| **5.2** | `GitHub Insights` (Actions Usage/Queue Metrics, Dependency Graph) and CI/CD failure event alerts (Teams apps, Action Groups) | 3 | 18 |
| **5.3** | Analyzing infra KPIs, W3C distributed tracing (`Application Map`), Smart Detection, and `KQL` (`percentile()`, `InsightsMetrics`, `KubeEvents`) | 3 | 18 |
| **Total** | **5 Functional Groups · 34 Local Skills** | **100** | **600** |
