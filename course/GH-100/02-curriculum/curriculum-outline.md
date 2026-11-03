# 🗺️ Curriculum Outline — Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator (`GitHub Administration`)

Aligned strictly to Microsoft Learn's **July 2026** (*Last updated May 5, 2026*) **Exam GH-100: GitHub Enterprise Administrator** study guide (`5 domains`, `39 skills`, `6 × 100 = 600` original scenario questions).

---

## 🎯 Exam Conditions & Candidate Profile

- **Credential Earned:** **Microsoft Certified: GitHub Administration** (*Intermediate* — **valid for 2 years**, eligible for online recertification on Microsoft Learn)
- **Prerequisite:** **None** (*working familiarity with Git repositories, Pull Requests, and YAML workflows at GH-900 level recommended*)
- **Timing & Passing Standard:** **100 minutes** exam time (**120 minutes** total seat duration) · **700 / 1000** scaled score · **$99 USD** via Pearson VUE (`English` only)
- **Open-Book Policy:** **Strictly closed-book** — split-screen **Microsoft Learn / GitHub Docs access is NOT available** on GitHub exams
- **Case Studies / Live Labs:** **None** (`0` multi-tabbed case studies, `0` live labs — `100%` standalone questions)

---

## 📐 5-Domain / 39-Skill Blueprint Matrix (`100` Questions/Exam · `600` Total)

### Domain 1 — Manage GitHub identities and access (`15–20%` → **19 Qs/exam · 114 total**)
| Skill ID | Official July 2026 Skill Statement | Qs / Exam | 6-Exam Total | Core Administrative Decisions Tested |
|---|---|---:|---:|---|
| **1.1** | Configure and manage Enterprise Managed Users (`EMUs`) vs. personal accounts | 2 | 12 | `<handle>_<shortcode>` accounts, IdP ownership, **Guest Collaborators** (`no Internal repo access`), zero public repos/Gists, `GEI` + mannequin reclamation (no in-place personal conversion) |
| **1.2** | Implement authentication mechanisms (`SAML SSO`, `2FA`) | 2 | 12 | Enterprise vs Org SAML SSO, `/saml/consume` ACS URL, immutable `NameID`, vaulting **SAML recovery codes**, `2FA` enforcement immediate removal, FIDO2/WebAuthn passkeys |
| **1.3** | Configure and troubleshoot `SCIM` provisioning and team synchronization | 2 | 12 | `SCIM 2.0` (`RFC 7643/7644`) full lifecycle vs personal-account **Team Synchronization** (`Entra ID`/`Okta` Org teams only; cannot invite non-members or remove org membership) |
| **1.4** | Choose and configure Identity Providers (`IdP`) | 2 | 12 | **Entra ID OIDC** + **Conditional Access (`CAP`)** IP validation on EMUs, Entra/Okta/PingFederate paved-path setups, GHES native **LDAP** (`LDAPSync`) + `/login?built_in=true` emergency fallback |
| **1.5** | Contrast authentication vs. authorization across GitHub | 2 | 12 | Valid token/SSH authentication vs SAML SSO authorization (`Configure SSO -> Authorize`), SSH CA short-lived certs, additive repository RBAC (`most permissive wins`) |
| **1.6** | Manage organization and repository roles and permissions | 2 | 12 | `Read` → `Triage` → `Write` → `Maintain` → `Admin`, up to `5` Custom repository roles, `Security Manager`, `Billing Manager`, `Moderator`, Custom organization & enterprise roles |
| **1.7** | Design and govern team structure and hierarchy | 3 | 18 | **Enterprise teams** (`@/ent:<slug>`, `<=2,500` teams, `<=5,000` EMU IdP users, `<=1,000` orgs, `0` manual members before IdP sync, Copilot/enterprise roles/ruleset bypass; **NO** `CODEOWNERS`/nesting/Secret/Team Maintainers) vs nested Org teams; `Base permissions = None` |
| **1.8** | Audit user access and permissions | 2 | 12 | Enterprise `People -> Export`, Audit Log `hashed_token`, `Outside collaborators`, GHES `/stafftools`, `Rule Insights`, REST `/permission` & `affiliation=direct` |
| **1.9** | Configure enterprise and organization policies and rulesets | 2 | 12 | Enforced Enterprise policies, required **Custom Properties**, Enterprise/Org **Repository Rulesets** (`Evaluate` dry-run mode, `~DEFAULT_BRANCH`, status-check integration pinning, layered `most restrictive wins`) |

### Domain 2 — Administer GitHub Enterprise environment (`10–15%` → **14 Qs/exam · 84 total**)
| Skill ID | Official July 2026 Skill Statement | Qs / Exam | 6-Exam Total | Core Administrative Decisions Tested |
|---|---|---:|---:|---|
| **2.1** | Differentiate admin tasks vs. GitHub Support escalations | 2 | 12 | Internal Ruleset/IdP/IP-allowlist/disk fixes vs Support server-side PR cache purges, `90-day` repo restores, GHEC packfile recovery, and up to `20` entitled Support contacts |
| **2.2** | Generate and submit support bundles and diagnostics | 2 | 12 | `ghe-diagnostics`, `ghe-support-bundle -x` (`extended 7–8d rotated logs`) over SSH port `122` / `:8443`, `ghe-support-upload`, redaction, and never opening public SSH to Support |
| **2.3** | Establish and enforce development process standards | 2 | 12 | `<org>/.github` default community health files (`SECURITY.md`, PR templates), `.github/workflow-templates/*.properties.json`, YAML Issue Forms (`blank_issues_enabled: false`), InnerSource, GHES `ghe-maintenance -s` & `.hpkg` hotpatches |
| **2.4** | Recommend workflow, branching, and release strategies | 2 | 12 | **Merge Queue** (`on: merge_group`), `CODEOWNERS` (`last match wins`), signed commits (`GPG`/`SSH`/`X.509`), linear Squash history, Tag Rulesets, `.github/release.yml`, Immutable releases |
| **2.5** | Evaluate GitHub deployment scenarios (`GHEC`, `GHES`, `EMUs`, `Data Residency`) | 2 | 12 | 4 deployment models (`GHEC+personal`, `GHEC+EMU`, **`GHEC with Data Residency <ent>.ghe.com + EMU`**, `GHES`), GHES HA (`ghe-repl-promote`), Geo-replication, Clustering, online `ghe-backup` (`backup-utils`), GitHub Connect privacy |
| **2.6** | Explain licensing models and billing structure | 2 | 12 | Per-user Enterprise seat deduplication across orgs & GitHub Connect GHES, Visual Studio Enterprise/Pro linkage, Copilot Business vs Enterprise, standalone `Secret Protection` vs `Code Security`, `50k` minutes & `50 GB` included |
| **2.7** | Monitor and manage license usage across environments | 2 | 12 | Pending invitations & outside collaborators (`1` seat each), suspended GHES / Billing Manager (`0` seats), verified-email GitHub Connect matching, manual offline GHES `.json` sync, pre-enablement GHAS seat estimator |

### Domain 3 — Implement secure software development and compliance (`25–30%` → **29 Qs/exam · 174 total**)
| Skill ID | Official July 2026 Skill Statement | Qs / Exam | 6-Exam Total | Core Administrative Decisions Tested |
|---|---|---:|---:|---|
| **3.1** | Configure enterprise security policies | 3 | 18 | **Enterprise/Org Security Configurations** (`Enforced` locks settings except `Not set`; auto-applies to **newly created** repos, **NOT** **transferred** repos!), tiered PCI vs docs configs |
| **3.2** | Strengthen security posture and protect sensitive data | 3 | 18 | **SSH Certificate Authorities (`Ed25519`, short `valid_before`)**, CIDR IP allow lists (+ GitHub App IP inheritance), Push Rulesets (`file paths`, `extensions`, `max size`, `MAX_PATH`), private GitHub Pages, disabling private forks/deploy keys |
| **3.3** | Manage audit logs and compliance reporting | 3 | 18 | `180-day` UI/REST cap vs **Audit Log Streaming** (up to `2` concurrent sinks: `S3`, `Blob`, `Event Hubs`, `GCS`, `Datadog`, `Splunk`; **`Stream Git events`**; append-only `@timestamp`), **Security Overview** (`Risk` & `Coverage`) |
| **3.4** | Configure code scanning and secret scanning | 3 | 18 | **CodeQL** (`Default` vs `Advanced` `build-mode: manual`, weekly scheduled zero-day scans, `SARIF v2.1.0`, Copilot Autofix), **Secret Scanning Push Protection + Partner Validity Checks + Delegated Bypass**, Custom regex dry-runs & AI Copilot generic password detection |
| **3.5** | Manage dependency security (`Dependabot`, `Advisories`) | 3 | 18 | `Dependabot security updates` vs `version updates` (`groups:`, `github-actions` SHA bumps, Auto-triage rules, Compatibility scores), **Dependabot on Actions/self-hosted VNet runners**, `dependency-review-action` (`deny-licenses`), Private Vulnerability Reporting, `SPDX` SBOM & Dependency Submission API |
| **3.6** | Develop and execute a security response plan | 3 | 18 | **Revoke & rotate leaked credentials immediately first**, rewrite history across all refs via **`git filter-repo`** (`not git rm / git revert / Squash merge`), force-push + fresh clones, **GitHub Support** PR cache purge (`or ghe-repo-gc` on GHES) |
| **3.7** | Establish policies for Personal Access Tokens (`PATs`) | 3 | 18 | Block **`PAT (classic)`** (`ghp_`), require **Owner approval** + max lifetime (`<=30–90d`) on **Fine-grained PATs** (`github_pat_`, single org target), `Active tokens` central revocation, `1-year` inactivity revocation |
| **3.8** | Manage API rate limits and performance | 3 | 18 | `5,000 req/hr` shared user PAT bucket vs **`15,000 req/hr` GHEC GitHub App installation & `GITHUB_TOKEN`** (`12,500` non-GHEC App cap; `60/hr` unauthenticated IP; `10/min` code search), GraphQL `5,000` vs `10,000 pts/hr`, `ETag` `304` (`0` quota), **`Retry-After`** & `<100` concurrent Secondary rate limits |
| **3.9** | Govern GitHub Apps vs. OAuth Apps | 3 | 18 | **GitHub App** (`<=10m` RS256 JWT `iat = now - 60s` -> `1h` installation token `ghs_`, down-scoped `/access_tokens`, actor-independent, centralized webhooks) vs coarse user-bound OAuth Apps (`gho_`) |
| **3.10** | Control app approval and installation workflows | 2 | 12 | `Third-party Access` approval queues, OAuth App access restrictions, `Accept new permissions` gate, **GitHub App manager** delegation, Enterprise-internal App visibility, zero-downtime `.pem` rotation, instant `Suspend` kill-switch |

### Domain 4 — Manage GitHub Actions (`20–25%` → **24 Qs/exam · 144 total**)
| Skill ID | Official July 2026 Skill Statement | Qs / Exam | 6-Exam Total | Core Administrative Decisions Tested |
|---|---|---:|---:|---|
| **4.1** | Enable enterprise reuse of actions and workflows | 3 | 18 | `Internal`/`Private` repos with `Access = Accessible from repositories in the enterprise`, `on: workflow_call` (`<=4` nested levels, caller context, `outputs`), Composite Actions (`shell:`), JavaScript vs Linux-only Docker actions, SLSA **Artifact Attestations** |
| **4.2** | Configure organization-level policies for Actions | 3 | 18 | `Allow select actions and reusable workflows`, **40-character commit SHA pinning**, `Read-only` `GITHUB_TOKEN`, disabling Actions PR self-approval, fork PR `Require approval for all external contributors`, blocking `pull_request_target` Pwn-Requests, Ruleset **Required Workflows** |
| **4.3** | Design and manage runner deployment (`hosted` vs. `self-hosted`) | 3 | 18 | Enterprise -> Org -> Repo -> Workflow **Runner Groups** (`never public repos`), **Larger runners** (CPU/RAM/GPU/static IPs), `--ephemeral` / `generate-jitconfig` VMs, Kubernetes **`ARC` (`gha-runner-scale-set`)** authenticated via GitHub App (`dind` / k8s mode) |
| **4.4** | Configure private networking for Actions | 3 | 18 | **Azure Private Networking** (`GitHub.Network/networkSettings` + GitHub **Network Configurations** on **Linux & Windows Larger runners ONLY** — **NOT** standard `ubuntu-latest` or `arm64` macOS Larger runners), NSG/Azure Firewall egress, standard Linux multi-cloud IP pool (`api.github.com/meta`) |
| **4.5** | Troubleshoot runner issues | 3 | 18 | `_diag/Runner_*.log` (listener/network) vs `_diag/Worker_*.log` (job steps), `ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`, `.env` `https_proxy`/`no_proxy`, `NODE_EXTRA_CA_CERTS` & `GIT_SSL_CAINFO`, outbound `443` long-polling, cloned `.runner` session conflicts, `30-day` agent deprecation, GHES Actions S3/Blob storage |
| **4.6** | Control secret scope and access hierarchy | 3 | 18 | **`Environment > Repository > Organization`** precedence (for both `secrets.*` and `vars.*`!), **Deployment Environments** (`<=6` Required Reviewers, `Prevent self-review`, Wait timers, `Selected branches/tags`, **Custom deployment protection rules**), Dependabot secret isolation |
| **4.7** | Manage organization and repository secrets configuration | 3 | 18 | `1,000` Org / `100` Repo / `100` Env write-only secrets, **`48 KB`** max size, reserved `GITHUB_*` prefix, client-side **LibSodium sealed-box** API encryption (`gh secret set`), plain-text `vars.*`, `::add-mask::`, isolated `Actions`/`Dependabot`/`Codespaces` stores, Terraform IaC |
| **4.8** | Integrate third-party vaults and dynamic secrets (`OIDC`) | 3 | 18 | **`permissions: id-token: write`**, `https://token.actions.githubusercontent.com` (and tenant-specific `.ghe.com`/GHES issuers), strict **`sub`** (`repo:<org>/<repo>:environment:production`), **`aud`**, **`job_workflow_ref`**, and **`runner_environment`** claims across HashiCorp Vault, Azure Key Vault, AWS STS, and GCP |

### Domain 5 — Monitor and optimize GitHub usage (`10–15%` → **14 Qs/exam · 84 total**)
| Skill ID | Official July 2026 Skill Statement | Qs / Exam | 6-Exam Total | Core Administrative Decisions Tested |
|---|---|---:|---:|---|
| **5.1** | Analyze audit logs and API usage metrics | 3 | 18 | **Organization API Insights** (`View organization API insights` custom permission, actor/route rate-limit drill-downs), Audit Log `action:`/`hashed_token:`/`actor_ip` queries, JSON/CSV exports, replacing tight REST polling with Webhooks/`ETag`/GraphQL `rateLimit`, cron jittering |
| **5.2** | Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | 3 | 18 | `githubstatus.com` component webhooks, GHES `:8443` Management Console & port `122` SSH, **`ghe-diagnostics`**, `ghe-repl-status`, `ghe-governor`, Prometheus `/metrics`, SNMP, `syslog` forwarding, SAML HAR/NTP triage, `exit code 137` OOM fixes, `10s` webhook timeouts, Premium Support SLAs |
| **5.3** | Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | 3 | 18 | **Copilot Seat API** (`last_activity_at`) & **Copilot Metrics API** (`>=5` active user privacy threshold, language breakdowns), **Security Overview** (`Coverage` vs `Risk`), GHES `90-day` Dormant Users & Activity dashboard, Actions Usage/Performance Queue metrics, archiving stale cron repos |
| **5.4** | Interpret usage reports for metered products | 3 | 18 | **Enhanced Billing Cost Centers** (`1` active cost center per resource) & **75/90/100% hard-stop Budgets**, **90-day rolling unique GHAS committers** (`0` seats for readers & `dependabot[bot]`), `1x / 2x / 10x` OS runner multipliers, Larger runners billed from minute 1 vs `$0` self-hosted compute, shared Actions/Packages storage, Codespaces core-hours + stopped storage |
| **5.5** | Recommend strategies for license and resource optimization | 2 | 12 | Reclaiming dormant GHES / departed SCIM EMU seats (**preserving 100% of historical commits & PR reviews!**), canceling stale invites, GitHub Connect deduplication, `actions/cache@v4` (`10 GB`), `retention-days` artifact caps, `concurrency: cancel-in-progress`, right-sizing Linux runners |

---

## 🏢 Six Enterprise Scenario Themes

1. **Practice Set 1 (`KestrelPay Global` — Multi-Org Payments FinTech):** Multi-org EMU deployment, SAML/OIDC Conditional Access, Enterprise teams, Custom RBAC roles, and layered Repository Rulesets.
2. **Practice Set 2 (`HelioBio Sciences` — Hybrid Cloud & Wet-Lab Genomics):** Hybrid `GHEC Data Residency` + self-hosted `GHES` appliances, `/stafftools`, `ghe-support-bundle -x`, Geo-replication, and GitHub Connect.
3. **Practice Set 3 (`VanguardGrid Energy` — Critical Utility Infrastructure):** Enforced Enterprise Security Configurations, Push Rulesets, CodeQL/Dependabot, `git filter-repo` secret incident response, PAT policies, and `15k` App rate limits.
4. **Practice Set 4 (`StratusRail Logistics` — Freight Rail CI/CD & Private Cloud):** Enterprise `workflow_call` reuse, Ruleset Required Workflows, Kubernetes `ARC` scale sets, Azure Private Networking for Larger runners, and OIDC Vaults.
5. **Practice Set 5 (`ZephyrAero Avionics` — Regulated DO-178C Aerospace):** Dual Audit Log Streaming, API Insights, SARIF/SPDX SBOM compliance, Copilot & GHAS utilization analytics, Cost Centers, and seat FinOps.
6. **Practice Set 6 (`MeridianVault Banking` — Global Tier-1 Retail & Investment Bank):** Full-spectrum July 2026 capstone spanning `GEI` EMU migration, PCI/SOX Security Configurations, GitHub Apps, `ARC` + Azure VNet Larger runners, OIDC `runner_environment` gates, and enterprise FinOps.
