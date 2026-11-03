# Curriculum Outline — Microsoft / GitHub Exam GH-900: GitHub Foundations

## Course Structure Overview

- **Course Format:** Udemy Practice Test-Only Course (`6` full-length practice exams × `100` questions = `600` unique questions)
- **Target Credential:** `GitHub Foundations` (`Beginner` / Fundamentals · **no prerequisite** · **never expires / does not require renewal**)
- **Official Study-Guide Baseline:** **January 2026** (*Last updated February 19, 2026* — [Microsoft Learn GH-900 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900))
- **Certification Status:** **Active** (`Retirement date: none`)
- **Timing & Closed-Book Guidance:** Live GH-900 provides **100 minutes** of exam time (`120 minutes` total seat duration), is **strictly closed-book** (split-screen Microsoft Learn access is NOT available on Fundamentals or GitHub exams), and contains **zero case studies and zero live labs**. Set Udemy's timer to **100 minutes** per 100-question exam (`60 sec/question` live pace) or **75 minutes** for a high-speed drill.

---

## Key 2026 Topics Emphasized in the January 2026 GH-900 Blueprint

1. **GitHub Copilot Agents, Agent Mode & Multi-Model Support (`4.2`, `4.3`, `6.3`):** Distinguishes **GitHub Copilot coding agent** (asynchronous cloud agent assigned to GitHub Issues that works in an isolated **GitHub Actions**-powered environment and opens a **draft Pull Request** for human review) from **IDE Agent Mode** (synchronous multi-file autonomous coding + local terminal loops inside VS Code / Visual Studio / JetBrains / Xcode), plus **`.github/copilot-instructions.md`**, **Model Context Protocol (`MCP`)** servers, **multi-model selection**, and plan boundaries across **Copilot Free / Pro / Pro+**, **Copilot Business** (`$19`, org policy & IP indemnity without requiring GHEC), and **Copilot Enterprise** (`$39`, requires GHEC, Knowledge Bases & org indexing).
2. **Modern Authentication, Rulesets & Enterprise Identity (`6.1`–`6.5`):** Covers **WebAuthn Passkeys** + offline **`2FA` recovery codes**, **Fine-grained PATs**, **Secret Scanning Push Protection**, the 5-tier repository role model (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), **Enterprise Managed Users (`EMUs`)** (`Entra ID`/`Okta` SSO + SCIM lifecycle, `GHE.com` data residency, zero public repos/Gists/external OSS PRs), **`Internal`** repository visibility, and **Repository Rulesets** (`Evaluate` dry-run mode, multi-repo inheritance).
3. **GitHub Projects v2, Supply-Chain Insights & Cloud Editors (`2.4`, `4.4`, `4.5`, `5.1`–`5.4`):** Covers **GitHub Projects** (`Table`, `Board`, `Roadmap`, `Iteration` fields, built-in workflows, `Burn up` Insights), **Dependency graph** (`SPDX` SBOM export + Enterprise Dependency Insights + **Dependabot**), and **GitHub Codespaces** (`.devcontainer/devcontainer.json` cloud VMs) versus zero-compute **`github.dev`** (`.` browser editor).

---

## Six-Exam Progression & Organizational Themes

| Exam | Udemy Practice-Test Title | Organizational Context & Core Focus | Questions | Recommended Timer |
| :---: | :--- | :--- | :---: | :---: |
| **1** | `Full-Length Mock Exam 1: Product Engineering & Web Platform` | `VelaCart Commerce` — Git vs GitHub, GitHub Flow, Repo files, Actions, Copilot Agents, Projects, Passkeys & EMUs | `100` | `100 min` |
| **2** | `Full-Length Mock Exam 2: Design, Documentation & DevRel` | `Solstice Design Systems` — GFM Markdown, Desktop/Mobile, Git LFS, PR suggestions, Pages/Wikis/Gists, `github.dev` & Sponsors | `100` | `100 min` |
| **3** | `Full-Length Mock Exam 3: Cloud SaaS & Platform Engineering` | `StratusGrid Cloud` — Merge Queue, `CODEOWNERS`, Actions Matrix/Environments, MCP, Codespaces, SCIM EMUs & Ruleset `Evaluate` | `100` | `100 min` |
| **4** | `Full-Length Mock Exam 4: Agile Product Management & Release Ops` | `OrbitPulse Releases` — Git tags/bisect, Sub-issues/Transfers, Projects WIP & templates, Fine-grained PATs & Stale approvals | `100` | `100 min` |
| **5** | `Full-Length Mock Exam 5: Regulated FinTech & Enterprise Governance` | `AegisLedger FinTech` — Verified signed commits, `GHES` vs `GHEC`, `SPDX` SBOMs, Actions OIDC, Copilot exclusions & SOX Rulesets | `100` | `100 min` |
| **6** | `Full-Length Mock Exam 6: Open-Source Ecosystems & Global Collab` | `PyHelios Open Source` — Fork sync, `MIT` vs `GPLv3`, YAML Issue Forms, fork CI safety, Prebuilds, `FUNDING.yml` & InnerSource | `100` | `100 min` |

---

## Complete 36-Skill Blueprint Allocation (Identical Across Every Exam)

### Domain 1 — Understand Git and GitHub basics (`25–30%` Official → `28` Questions / Exam)
- `1.1` Identify the core features and benefits of version control and Git (`4`)
- `1.2` Explain the differences between Git and GitHub (`4`)
- `1.3` Describe basic Git concepts such as repositories, commits, and branches (`5`)
- `1.4` Differentiate between GitHub's Personal, Organization, and Enterprise plans (`4`)
- `1.5` Describe GitHub Flow and how it supports collaborative development (`4`)
- `1.6` Use Markdown to format text in issues, pull requests, and files (`4`)
- `1.7` Understand the functions of GitHub Desktop and GitHub Mobile (`3`)

### Domain 2 — Work with GitHub repositories (`10–15%` Official → `14` Questions / Exam)
- `2.1` Describe the purpose of key repository files (`README`, `LICENSE`, `CONTRIBUTING`, `CODEOWNERS`, `SECURITY`) (`4`)
- `2.2` Create a new repository using templates and manage branches (`3`)
- `2.3` Add, move, and organize files in a repository (`2`)
- `2.4` Navigate repository insights, stars, feature previews, and dependency insights (`3`)
- `2.5` Apply repository maintenance best practices, including archiving (`2`)

### Domain 3 — Collaborate using GitHub (`10–15%` Official → `14` Questions / Exam)
- `3.1` Explain the role of issues, pull requests, and discussions (`4`)
- `3.2` Link issues and pull requests, use templates, and filter search results (`4`)
- `3.3` Manage notifications and subscriptions effectively (`3`)
- `3.4` Share content with Gists, wikis, and GitHub Pages (`3`)

### Domain 4 — Apply modern development practices (`10–15%` Official → `14` Questions / Exam)
- `4.1` Understand the basics of GitHub Actions and workflow files (`3`)
- `4.2` Describe GitHub Copilot features, including agents, Agent Mode, and multi-model support (`3`)
- `4.3` Differentiate between GitHub Copilot Individual, Business, and Enterprise (`3`)
- `4.4` Configure and use GitHub Codespaces (`3`)
- `4.5` Use `github.dev` for browser-based editing (`2`)

### Domain 5 — Manage projects with GitHub (`5–10%` Official → `8` Questions / Exam)
- `5.1` Describe GitHub Projects and available layout views (`2`)
- `5.2` Configure custom fields, labels, milestones, and workflows (`2`)
- `5.3` Use saved replies and assign tasks (`2`)
- `5.4` Track progress using Project insights (`2`)

### Domain 6 — Understand privacy, security, and administration (`10–15%` Official → `14` Questions / Exam)
- `6.1` Secure accounts using 2FA and passkeys (`3`)
- `6.2` Explain repository and organization roles for access management (`3`)
- `6.3` Describe Enterprise Managed Users (`EMUs`) and org-level Copilot management (`3`)
- `6.4` Set repository visibility and apply branch protection rules (`3`)
- `6.5` Manage teams and organizational settings (`2`)

### Domain 7 — Explore the GitHub community (`5–10%` Official → `8` Questions / Exam)
- `7.1` Describe the benefits of open source and GitHub Sponsors (`1`)
- `7.2` Understand how GitHub supports open-source projects (`1`)
- `7.3` Follow users and organizations to track activity (`1`)
- `7.4` Discover and apply tools from GitHub Marketplace (`1`)
- `7.5` Explain the principles of InnerSource (`2`)
- `7.6` Differentiate forks and templates and use repository topics (`2`)
