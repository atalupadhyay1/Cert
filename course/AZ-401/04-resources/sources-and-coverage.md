# Official Primary Sources & Blueprint Coverage Matrix (`AZ-401`)

All 600 questions in `course/AZ-401/` are 100% original scenarios authored directly from official Microsoft Learn and GitHub Docs specifications retrieved **October 29, 2026**. Zero recalled exam content and zero Microsoft copyrighted case-study names (`Contoso`, `Fabrikam`, `Litware`, `Tailwind Traders`, `Wide World Importers`, `Parts Unlimited`, etc.) appear anywhere in the repository.

---

## Official Exam & Certification References

- **Official AZ-401 Study Guide (Last updated October 13, 2026):** `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401`
- **Official Exam AZ-401 Page (`Designing and Implementing Microsoft Agentic DevOps Solutions (beta)`):** `https://learn.microsoft.com/en-us/credentials/certifications/exams/az-401/`
- **Official Certification Page (`Microsoft Certified: Agentic DevOps Engineer Expert (beta)`):** `https://learn.microsoft.com/en-us/credentials/certifications/agentic-devops-engineer-expert/`
- **Official Microsoft Launch & Prerequisite Announcement (October 15, 2026):** `https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-agentic-devops-engineer-expert/4528356`
  - **Beta & Predecessor Lifecycle:** Public beta runs through **November 9, 2026**; General Availability targeted **December 2026**; succeeds **Exam AZ-400** (`DevOps Engineer Expert`), which retires **February 1, 2027**.
  - **Expert Certification Prerequisite:** Passing **Exam AZ-401** (`700 / 1000` scaled score) **plus** holding an active **`Microsoft Certified: GitHub Copilot` (`Exam GH-300`)** **or** **`Microsoft Certified: Azure Administrator Associate` (`Exam AZ-104`)** credential.

---

## Primary Technical Documentation by Domain

1. **Processes, Communications, Agentic Primitives & MCP Servers (`15–20%` -> `17` Qs/set):**
   - Azure DevOps MCP Server (`@azure-devops/mcp` & `https://mcp.dev.azure.com/{organization}`): `https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/`
   - Configuring MCP Servers & `copilot-setup-steps.yml` for GitHub Copilot Coding Agent: `https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp` & `https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment`
   - Custom Instructions (`copilot-instructions.md`, `.instructions.md` `applyTo`), `AGENTS.md`, Custom Agents (`.agent.md`), and Agent Skills (`SKILL.md`): `https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents` & `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills`
2. **Source Control, Worktrees, Copilot Rulesets & Migrations (`10–15%` -> `13` Qs/set):**
   - Copilot Cloud Agent Governance, Firewall, Rulesets & Human PR Approval Safeguards: `https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations` & `https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/Configure-automatic-code-review-by-Copilot`
   - Migrating Repositories from Azure DevOps to GitHub (`gh ado2gh`): `https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github`
   - Git Worktrees & `git filter-repo`: `https://git-scm.com/docs/git-worktree` & `https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository`
3. **Build & Release Pipelines, `gh-aw`, Deployments & Bicep IaC (`35–40%` -> `38` Qs/set):**
   - GitHub Agentic Workflows (`gh-aw`, `.md` -> `gh aw compile` -> `.lock.yml`, `safe-outputs`): `https://github.github.com/gh-aw/introduction/overview/`
   - Azure Pipelines, Managed DevOps Pools, Artifacts Feed Views & Azure Load Testing: `https://learn.microsoft.com/en-us/azure/devops/pipelines/` & `https://learn.microsoft.com/en-us/azure/load-testing/`
   - Bicep `what-if`, ARM Deployment Stacks, Azure Deployment Environments (ADE) & Machine Configuration: `https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks` & `https://learn.microsoft.com/en-us/azure/deployment-environments/`
4. **Security & Compliance Plan (`15–20%` -> `16` Qs/set):**
   - Workload Identity Federation (OIDC) in GitHub Actions & Azure Pipelines: `https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation`
   - GitHub Advanced Security (GHAS / GHAzDO) & Microsoft Defender for Cloud DevOps Security: `https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview`
5. **Instrumentation Strategy, Azure SRE Agent & Observability Agent (`15–20%` -> `16` Qs/set):**
   - Azure SRE Agent (`sre.azure.com`, ServiceNow/PagerDuty/Azure Monitor, Incident Response Plans, Autonomy & Cooldown): `https://learn.microsoft.com/en-us/azure/sre-agent/overview`
   - Azure Copilot Observability Agent (RBAC Interactive Investigations, AMW Association & Autonomous Azure Monitor Issues): `https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview`
   - GitHub Copilot Agent Session Logs & CLI Hooks (`audit.jsonl`): `https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/track-copilot-sessions` & `https://docs.github.com/en/copilot/how-tos/copilot-cli/use-hooks`

---

## Complete 27-Skill Per-Exam Coverage Table (`100` Items × `6` Sets = `600` Items)

| Skill ID | Official AZ-401 Sub-Skill Mapping (`October 13, 2026` Baseline) | Per Set | 6-Set Total |
|---|---|---:|---:|
| `1.1` | Traceability, flow of work (Plan/Build/Deploy/Operate), feedback notifications & Azure Boards | 5 | 30 |
| `1.2` | Business KPIs -> DevOps success metrics (DORA/Flow) & AI-assisted WIQL/Analytics queries | 4 | 24 |
| `1.3` | AI-assisted docs (Wikis, Mermaid, CODEOWNERS) & agentic primitives (`copilot-instructions`, `SKILL.md`, `copilot-setup-steps`) | 4 | 24 |
| `1.4` | Azure DevOps & GitHub MCP servers, webhook/skill integrations & Copilot Cloud Agent for Boards | 4 | 24 |
| `2.1` | Branching strategies (Trunk-Based, Feature, Release, Git Flow, GitHub Flow & `git worktree`) | 3 | 18 |
| `2.2` | PR workflows, merge restrictions & branch protection / rulesets for GitHub Copilot | 4 | 24 |
| `2.3` | Repo permissions, signed tags, deep-link traceability & automated Git / Copilot CLI hooks | 3 | 18 |
| `2.4` | Repo-to-repo migration (`gh ado2gh`) & Git history recovery/removal (`reflog`, `revert`, `filter-repo`) | 3 | 18 |
| `3.1` | Azure Artifacts & GitHub Packages feeds, upstream sources & `@Local`/`@Prerelease`/`@Release` views | 3 | 18 |
| `3.2` | SemVer, CalVer & immutable pipeline/OCI `@sha256` artifact versioning | 3 | 18 |
| `3.3` | Automated quality and release gates implemented with GitHub Copilot & MCP servers | 2 | 12 |
| `3.4` | Unit, Testcontainers, Playwright & Azure Load Testing strategies/tasks with Copilot & MCP | 2 | 12 |
| `3.5` | Code coverage & PR diff coverage analysis implemented with GitHub Copilot & MCP servers | 2 | 12 |
| `3.6` | Azure Pipelines vs GitHub Actions selection & Hosted / Managed DevOps Pool / ARC runner infra | 3 | 18 |
| `3.7` | Multi-stage YAML pipelines with Copilot, triggers, parallelism, `extends` templates, KV groups & checks | 5 | 30 |
| `3.8` | GitHub Agentic Workflows (`gh-aw` `.md` frontmatter, `gh aw compile` -> `.lock.yml`, `safe-outputs`) | 4 | 24 |
| `3.9` | Blue-Green, Canary, Rings, App Config Feature Flags, A/B, zero-downtime, hotfix & DB/container deploys | 6 | 36 |
| `3.10` | Bicep IaC, ARM `what-if`, Deployment Stacks (`denyWriteAndDelete`), ADE & Machine Configuration | 4 | 24 |
| `3.11` | Pipeline health (`p95`, flaky tests), lockfile caching, PR concurrency cancellation & retention leases | 4 | 24 |
| `4.1` | Managed Identities vs Service Principals, GitHub Apps/Tokens & secretless OIDC federation | 5 | 30 |
| `4.2` | ADO service connections, Stakeholder/Basic/Test Plans access, project token scope & agent firewall | 3 | 18 |
| `4.3` | Key Vault RBAC/tasks, `Secure Files`, GitHub Environment/`COPILOT_MCP_*` secrets & log masking | 4 | 24 |
| `4.4` | GHAS/GHAzDO Push Protection, CodeQL, Dependency Review, Copilot built-in scans & Defender DevOps | 4 | 24 |
| `5.1` | Flow/DORA dashboards, Log Analytics & Sentinel audit streaming, GitHub Insights & pipeline alerts | 4 | 24 |
| `5.2` | Azure Copilot Observability Agent (RBAC interactive chat, AMW prerequisite & autonomous Monitor Issues) | 4 | 24 |
| `5.3` | Azure SRE Agent (`Monitor`/`PagerDuty`/`ServiceNow` `assignment_group`, Response Plans, `Review` & cooldown) | 4 | 24 |
| `5.4` | Metrics, W3C `traceparent` App Insights traces, Copilot cloud/CLI agent logs & NL/KQL `percentile()` | 4 | 24 |
| **Total** | **5 Domains (`17 / 13 / 38 / 16 / 16`) · 27 Skills** | **100** | **600** |
