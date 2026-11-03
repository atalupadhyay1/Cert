# Microsoft Exam GH-900: GitHub Foundations — Full-Length Mock Exam 5

**Theme:** Regulated FinTech & Enterprise Governance — SECURITY.md, Dependency Insights, Secret Protection, Multi-Model Copilot Policies, EMUs & InnerSource  
**Credential:** `Microsoft Certified: GitHub Foundations` *(Beginner / Fundamentals · **no prerequisite** · **does not require renewal / never expires**)*  
**Study guide baseline:** `January 2026 (Last updated February 19, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-900 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Docs documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Understand Git and GitHub basics (25–30% official weight · 28 questions)

### 1. A regulated payments institution (`AegisLedger`) faces annual SOC 2 and PCI-DSS software change-control audits. Which two Git version-control properties satisfy auditor traceability and safe incident recovery? Select two.

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Every developer clone contains the full commit history and branches, enabling offline commits and history inspection

### 2. When Git calculates the SHA hash of a commit object (`git rev-parse ____`), why does changing even a single character in a file 50 commits ago alter every descendant commit SHA?

- **A.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 3. To prove cryptographically on GitHub (`displaying a green Verified badge next to commits`) that a commit genuinely came from an engineer's workstation rather than a spoofed `git config user.email`, what should engineers enable (`git commit ____`)?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

### 4. Which Git command (`git ____ -n 5 --oneline`) displays a compact 5-line summary of the five most recent commits on the current branch?

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 5. Compliance counsel asks whether **Git** (`git-scm.com`) is owned exclusively by GitHub and stops working if a company's internet link drops for 4 hours. What is the accurate answer?

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 6. Which official command-line tool (`____ pr create`, `____ issue list`) brings **GitHub**-specific platform workflows (Pull Requests, Issues, Releases, Actions runs, Codespaces) right into your workstation terminal?

- **A.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 7. An enterprise requires commits created via GitHub's web UI (`such as merging Pull Requests or editing README.md in the browser`) to carry cryptographic **`Verified`** signatures alongside signed local commits. Proposed solution: Merge Pull Requests on `github.com`, where GitHub automatically signs web-created commits using GitHub's own verified GPG key. Does GitHub automatically sign commits made through its web UI?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 8. When authenticating `git clone git@github.com:aegisledger/core.git` from a developer laptop without HTTPS tokens, which cryptographic protocol (`port ____`) verifies workstation identity against public keys registered in GitHub Settings?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 9. A treasury engineer modifies `src/ledger/settlement.java` locally on `fix/rounding-scale` and publishes the commit to GitHub. Which four-step Git sequence applies?

- **A.** Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`
- **B.** Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`
- **C.** Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`
- **D.** Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`

### 10. You modified `config/dev.yaml` in your working directory (not staged yet) and want to discard those local edits cleanly (`git ____ config/dev.yaml`) back to `HEAD`. Which modern Git command restores the working-tree file?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)

### 11. Which Git command (`git ____ <commit-sha>`) inspects the commit author, timestamp, log message, **and** full patch diff of one specific commit SHA?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link

### 12. In Git, what does the special symbolic reference **`____`** (`stored in .git/HEAD`) point to during normal development?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** A lightweight movable pointer to a commit that isolates feature or bugfix work from the default branch (`main`) until merged
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 13. When teammates delete merged feature branches on GitHub (`origin`), stale remote-tracking refs (`origin/feat/old`) can linger locally until you run `git fetch ____` (`--prune`). Which flag cleans up deleted remote-tracking refs?

- **A.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution

### 14. A regulated financial group separates Retail Banking, Wealth Management, and Core Risk into distinct GitHub Organizations yet requires one central CISO policy layer, IP allow lists, and SAML/OIDC SSO. Which two account tiers accomplish this? Select two.

- **A.** Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **E.** Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)

### 15. A defense-regulated clearinghouse has a strict air-gapped mandate forbidding source code from leaving its own on-premises VMware / sovereign AWS VPC infrastructure. Which GitHub Enterprise deployment option satisfies self-hosted infrastructure control?

- **A.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them

### 16. Does a **GitHub Enterprise** subscription allow customers to run **both** cloud-hosted **GitHub Enterprise Cloud (`GHEC`)** and self-hosted **GitHub Enterprise Server (`GHES`)** with unified license syncing (`GitHub Connect`)?

- **A.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 17. In a GitHub Organization, which specialized administrative role (`____ manager`) allows a finance controller to view invoices, update payment methods, and monitor Actions/Codespaces spending **without** gaining read access to private source code?

- **A.** Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 18. A compliance engineer adds an IBAN checksum validator to `aegis-payments` using **GitHub Flow**. Which four-step workflow applies?

- **A.** Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review
- **B.** Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch
- **C.** Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge
- **D.** Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks

### 19. Regulators ask how **GitHub Flow** enforces separation of duties (`four-eyes principle`) when shipping daily changes to `main`. Which two practices provide this control? Select two.

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`
- **D.** Create a short-lived descriptive branch off `main` so `main` stays deployable at all times
- **E.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 20. When merging a 12-commit feature Pull Request on GitHub, compare **`Create a merge commit`**, **`Squash and merge`**, and **`Rebase and merge`**. Which option combines all 12 branch commits into **one** single commit on `main`?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** GitHub Flow: keep `main` always deployable, branch off `main`, open an early Pull Request for discussion and CI checks, merge after approval, and deploy

### 21. Why do regulated teams disable `Create a merge commit` or `Rebase and merge` selectively in `Repository Settings -> Pull Requests` so only **`Squash and merge`** (with PR title + `#PR` reference) is permitted?

- **A.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`

### 22. A risk architect documents a PCI-DSS tokenization flow inside a repository's `docs/architecture.md` using GitHub Flavored Markdown. Which three GFM features render audit checklists, warning callouts, and data-flow diagrams? Select three.

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)
- **E.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **F.** Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax

### 23. In GitHub Flavored Markdown, wrapping mathematical formulas inside `$...$` (inline) or `$$...$$` (`or a ____ code block`) renders scientific/financial equations natively using which syntax?

- **A.** Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 24. In a Pull Request comment across two repositories in the same organization (`aegisledger/core` referencing Issue `#95` inside `aegisledger/audit`), what exact cross-repository shorthand (`____#95`) creates an automatic bidirectional reference?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** `@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 25. In GitHub Flavored Markdown, placing double tildes around text (`____deprecated endpoint____`, i.e., `~~deprecated endpoint~~`) applies which visual text formatting?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 26. A risk analyst prefers reviewing local file diffs side-by-side and unchecking accidental debug edits line-by-line before committing on macOS without memorizing `git add -p`. Which official GUI client provides visual line-level partial staging?

- **A.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization

### 27. Besides triaging Issues and reviewing PRs, what security role can **GitHub Mobile** fulfill when an engineer signs into `github.com` on a laptop browser?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **C.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **D.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go

### 28. If an engineer runs into a rebase/merge conflict inside **GitHub Desktop**, how does GitHub Desktop assist before completing the merge?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **D.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization

---

## Domain 2 — Work with GitHub repositories (10–15% official weight · 14 questions)

### 29. PCI-DSS compliance mandates that `@aegis/pci-auditors` approve every Pull Request modifying `/card-vault/**` in `aegis-payments`. Which four-step sequence enforces this?

- **A.** Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages
- **B.** Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests
- **C.** Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`
- **D.** Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings

### 30. In a repository containing two overlapping rules in `.github/CODEOWNERS` (line 1: `* @aegis/general-devs` and line 20: `/card-vault/** @aegis/pci-auditors`), which rule wins for `/card-vault/token.go` and what two conditions enforce `CODEOWNERS`? Select two.

- **A.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **B.** Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch
- **C.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **E.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 31. Instead of repeating the exact same `SECURITY.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` across 200 repositories in `@aegisledger`, which special organization-wide repository (`aegisledger/____`) supplies default community health files automatically?

- **A.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **B.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **C.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 32. For a strictly proprietary `Private` or `Internal` corporate banking repository that is **never** distributed outside the company, should engineers attach an open-source `MIT` `LICENSE` file out of habit?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 33. A compliance platform team wants 25 new regulated payment microservices generated from `aegis-java-compliance-starter` (`copying both main and sandbox-examples branches`) to have clean 1-commit histories and zero fork-network linkage. Proposed solution: Have all 25 teams **Fork** `aegis-java-compliance-starter` instead of enabling `Template repository` (`with Include all branches`). Does Forking produce clean 1-commit unlinked repositories?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 34. Developers on Windows (`CRLF`) and Linux (`LF`) keep polluting Pull Request diffs with whole-file line-ending changes. Which repository root configuration file (`____`, e.g., `* text=auto`) standardizes line endings and linguist/diff behavior across OSes?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** `.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 35. Why should teams designate `main` as the **default branch** and protect it rather than switching the default branch every sprint (`sprint-41`, `sprint-42`)?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 36. While auditing `src/aml/sanctions.py` in GitHub's web file viewer, selecting the **`____`** toggle next to `Code` and `Raw` reveals the exact commit SHA, author, and Pull Request link behind every single line of the file.

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 37. In GitHub's single-file web editor, can a developer commit directly to `main` if `main` has branch protection requiring Pull Requests?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 38. Executive Order / FinTech supply-chain auditors request a downloadable machine-readable **Software Bill of Materials (`SBOM`)** (`SPDX JSON`) plus automated vulnerability alerts on `aegis-payments`. Which two features provide this? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)

### 39. Which open industry standard format does GitHub export when you select **`Export SBOM`** under `Repository -> Insights -> Dependency graph`?

- **A.** **Dependency graph** parses manifest/lockfiles (`package-lock.json`, `requirements.txt`), powering **Dependabot alerts** and Enterprise **Dependency insights** / SBOM export for license and CVE visibility
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks

### 40. An engineer wants early opt-in access to pre-release GitHub UI enhancements (`such as revamped Merge Experience or experimental Command Palette features`) on their user account without affecting teammates. Where do they toggle opt-in betas?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 41. Bank regulators require retaining 7 years of code, Pull Request review comments, and release tags for retired payment gateway `gateway-2019`, while guaranteeing zero new commits or Issues can be added. Which Repository Settings action satisfies both requirements?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 42. On an Organization's main landing page (`github.com/aegisledger`), how can admins highlight the 6 golden starter templates and core SDKs at the very top for internal engineers (`visible only to org members` vs `public`)?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

---

## Domain 3 — Collaborate using GitHub (10–15% official weight · 14 questions)

### 43. In a regulated repository with `Require approval of the most recent reviewable push` enabled, can the **same developer who pushed the last commit** to a Pull Request approve their own push to satisfy required reviews?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)

### 44. Which review submission state (`Comment`, `Approve`, or `____`) explicitly blocks merging a Pull Request when branch protection requires all review conversations/blocking reviews to be addressed?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 45. An internal Architecture Review Board (`ARB`) debates cloud database trade-offs across 6 squads before creating any engineering sprint tasks. Why is **GitHub Discussions** superior to filing premature Issues for open-ended RFCs?

- **A.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **B.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 46. When closing a duplicate or invalid Issue on GitHub, what is the difference between **`Close as completed`** (`purple icon`) and **`Close as not planned`** (`gray slash icon`)?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms

### 47. A security engineer fixes audit finding Issue `#42` on `aegis-auth` and wants `#42` closed automatically upon merging into `main`. Which four-step workflow applies?

- **A.** Close Issue `#42` manually before writing code → Commit directly to a fork wiki → Open an unlinked Discussion post → Archive the repository
- **B.** Write `Mentioning #42` in a commit on a non-default experimental branch → Never open a Pull Request → Delete the feature branch → Expect Issue `#42` to close automatically
- **C.** Create a secret Gist with `Fixes #42` → Star the repository → Watch releases only → Expect Gist save to close Issue `#42`
- **D.** Triage the Issue with labels, milestone, and assignee → Create a feature branch and commit the fix → Open a Pull Request containing `Closes #42` in its description → Merge the approved Pull Request into the default branch

### 48. Which two native GitHub mechanisms create an auditable link between remediation Pull Request `#510` and compliance Issue `#42` that automatically closes `#42` on merge? Select two.

- **A.** Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch
- **E.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 49. Where should a team store `.github/____.md` (or `.github/PULL_REQUEST_TEMPLATE/*.md`) so every newly opened Pull Request pre-populates a PCI-DSS compliance checklist (`- [ ] Threat model updated`, `- [ ] Unit tests added`)?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.
- **C.** `.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 50. An auditor wants to list every merged Pull Request in `aegis-payments` that lacked a peer approval (`review:____`) during Q3 (`merged:2026-07-01..2026-09-30`). Which `review:` search qualifier finds PRs with no approvals?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 51. In an Enterprise Organization, compliance requires notification emails for `@aegisledger` private repositories to deliver **only** to corporate `@aegisledger.com` email addresses—never to an engineer's personal `@gmail.com` address. Which Organization/Notification feature controls this?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 52. On a specific noisy Pull Request `#899` where you left one early comment, 40 bots keep commenting every hour and you no longer need updates on `#899` alone (`without ignoring the whole repository`). Which sidebar button silences just thread `#899`?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 53. Which repository `Watch -> Custom` checkbox lets a security officer receive instant alerts **only** for **`Security alerts`** and **`Releases`** on 80 repositories without getting flooded by daily Issue/PR chatter?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 54. An enterprise compliance engineering team on **GitHub Enterprise Cloud** publishes internal runbooks as a private access-controlled static portal and runs an internal Q&A desk. Which two features handle this natively? Select two.

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll

### 55. A contractor wants to paste a production PostgreSQL connection string (`postgres://admin:S3cret@db.internal:5432/prod`) somewhere "private" on GitHub to share with a coworker. Proposed solution: Create a **Secret Gist** on `gist.github.com` and Slack the URL. Is a Secret Gist access-controlled and safe for credentials?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 56. On `GitHub Free` personal accounts, can you publish a **GitHub Pages** site from a `Private` repository, or does private-repo Pages publishing require a paid plan (`Pro`, `Team`, or `Enterprise`)—and note that standard `Pro`/`Team` Pages sites are still **publicly** accessible on the internet unless using **GitHub Enterprise Cloud** access control?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

---

## Domain 4 — Apply modern development practices (10–15% official weight · 14 questions)

### 57. A FinTech platform requires CI workflows inside `.github/workflows/` to run inside a private VPC network reaching internal HSM appliances that are unreachable from public internet runners. Which two GitHub Actions concepts work together? Select two.

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)
- **C.** Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`
- **D.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 58. Instead of storing static long-lived cloud keys (`AWS_SECRET_ACCESS_KEY`) in GitHub Secrets, which modern GitHub Actions authentication mechanism exchanges short-lived cryptographic tokens (`id-token: write`) directly with AWS IAM, Azure Entra ID, or GCP?

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 59. If the exact same secret name `SIGNING_CERT` is defined at the **Organization** level, the **Repository** level, and the **`production` Environment** level, which value takes highest precedence inside a job targeting `environment: production`?

- **A.** Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers
- **B.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 60. An enterprise AI architecture board reviews **GitHub Copilot** capabilities for regulated engineering teams. Which three capabilities are natively available (subject to admin policy)? Select three.

- **A.** **IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** **Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity
- **D.** **Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **F.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 61. An architecture lead wants **GitHub Copilot** (including Copilot coding agent and IDE Agent Mode) to always enforce `BigDecimal` instead of `double` for currency fields and include OWASP parameterized SQL queries on `aegis-ledger`. Which repository feature encodes these persistent repo-wide rules alongside MCP tools?

- **A.** **Copilot coding agent** works asynchronously on assigned GitHub Issues in an Actions sandbox to open draft PRs, whereas **IDE Agent Mode** edits local files and runs local terminal tasks autonomously
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 62. Before a human peer reviewer inspects a Pull Request on `github.com`, how can authors request an automated AI security/logic pass directly inside the Pull Request **`Reviewers`** picker?

- **A.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 63. Legal counsel asks whether code prompts and completions from **GitHub Copilot Business** and **Copilot Enterprise** seats are retained by GitHub to train foundational public AI models for other companies. What is GitHub's contractual default?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **C.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 64. In **GitHub Copilot** policy settings, which toggle prevents Copilot from returning code completions (> ~150 characters) that verbatim match public code on GitHub (`helping legal teams mitigate open-source license contamination`)?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits

### 65. If a bank's AI Risk Committee approves Anthropic Claude Sonnet and OpenAI GPT models while disallowing preview/beta models across 500 **Copilot Enterprise** seats, where does the Enterprise Owner enforce that allowlist?

- **A.** **Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 66. Security architects standardize **GitHub Codespaces** on `aegis-core` so zero source code ever sits on unencrypted personal laptops. Which four-step configuration sequence applies?

- **A.** Create `.devcontainer/devcontainer.json` with image and VS Code extensions → Add `postCreateCommand` and `forwardPorts` → Commit `devcontainer.json` to the branch → Launch a cloud Codespace to verify
- **B.** Save `devcontainer.json` in a private user Wiki → Disable Codespaces in Organization Settings → Press `.` on the repository → Expect full container terminal execution
- **C.** Add Docker settings to `.github/FUNDING.yml` → Enable GitHub Sponsors → Star the repository → Expect `FUNDING.yml` to build a Codespace container
- **D.** Install tools manually inside one personal Codespace without editing `.devcontainer/` → Delete the Codespace → Ask teammates to open `github.dev` → Expect `github.dev` to provision that custom Docker container

### 67. Why do regulated financial institutions often mandate **GitHub Codespaces** (paired with organization policies restricting port visibility to `Private` / `Internal`) for external contractors instead of local `git clone`?

- **A.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **D.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go

### 68. Where do developers store personal API tokens needed inside their **GitHub Codespaces** terminal (`Settings -> Codespaces -> ____`) so secrets inject securely as environment variables without ever touching `.devcontainer/devcontainer.json`?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 69. Compliance reviewers inspect Pull Request diffs in **`github.dev`** while developers run integration test suites in **GitHub Codespaces**. Which two distinctions accurately contrast the two tools? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding
- **C.** **`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 70. A penetration tester wants to spin up `docker compose up` with Postgres and Redis containers inside **`github.dev`** (`https://github.dev/aegisledger/core`). Proposed solution: Press `.` to open `github.dev` and run `docker compose up` in `github.dev`. Does `github.dev` execute Docker containers?

- **A.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

---

## Domain 5 — Manage projects with GitHub (5–10% official weight · 8 questions)

### 71. A regulatory remediation PMO tracks 140 audit findings across 12 repositories in a private **GitHub Project**. Which two features provide multi-perspective tracking and automated status hygiene? Select two.

- **A.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **B.** Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts
- **E.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 72. Can an Organization **GitHub Project** have its visibility set to **`Private`** so even other Organization Members cannot view the Project board unless explicitly invited (`Read`, `Write`, or `Admin`)?

- **A.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields

### 73. Compliance engineering sets up an audit-remediation **GitHub Project** with sprint iterations, automatic closure syncing, and burn-up metrics. Which four-step workflow applies?

- **A.** Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts
- **B.** Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts
- **C.** Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache
- **D.** Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards

### 74. To keep long-completed audit items from slowing down active sprint views in **GitHub Projects** without deleting audit records, which built-in Project workflow automatically moves items untouched in `Done` for 14+ days into the Project archive?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **Labels** categorize Issues/PRs (`bug`, `priority:high`), **Milestones** track completion percentage toward a repository release target date, and **Project built-in workflows** auto-update `Status` when items close or PRs merge
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 75. An AppSec reviewer routinely posts a 12-line *"Threat Model Sign-Off Checklist"* comment on security-sensitive Pull Requests across 30 repositories. Which personal GitHub feature inserts that exact Markdown checklist in two keystrokes?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.

### 76. Why do engineering leads assign a clear human **`Assignee`** on every `sev:1` compliance Issue even when `@aegis/security` was `@mentioned` in the description?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 77. Which historical chart in **GitHub Projects -> Insights** plots daily item counts stacked by `Status` (`Backlog`, `In Progress`, `In Review`, `Done`) over a selected time window (`Burn up / Current & historical`) to expose scope creep?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)

### 78. Which five data types can you select when adding a new **Custom field** to a **GitHub Project** (`Text`, `Number`, `Date`, `Single select`, and `____`)?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Project custom fields (`Single select`, `Number`, `Date`, `Text`, and **`Iteration`** sprints with automatic break capacities) plus filter/sort/group view configurations (`slice by`)
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields

---

## Domain 6 — Understand privacy, security, and administration (10–15% official weight · 14 questions)

### 79. Before granting an auditor access to `@aegisledger`, the Organization enforces mandatory `2FA` (`Require two-factor authentication for everyone in your organization`). Which four-step account hardening sequence should the auditor complete first?

- **A.** Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication
- **B.** Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes
- **C.** Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in
- **D.** Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility

### 80. When an Organization Owner enables **`Require two-factor authentication for everyone in your organization`**, what happens to existing members without `2FA` enabled, and which two credentials protect members best? Select two.

- **A.** Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **E.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically

### 81. What built-in GitHub security scanner blocks a `git push` **in real time before commit upload finishes** if a developer accidentally commits a live AWS access key, Stripe live key, or GitHub PAT?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 82. A Compliance Auditor needs to inspect source code, read Pull Request review comments, view security advisories, or clone `aegis-payments` read-only—and must **not** modify Issues, labels, or code. Which repository role applies?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)

### 83. In a large enterprise with 80 engineering squads, the CISO wants 6 AppSec engineers to view security alerts (`Dependabot`, `CodeQL`, `Secret scanning`) and manage security configurations across **every** repository in the Organization **without** making them full `Organization Owners`. Which dedicated Organization role fits?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 84. When inviting an external penetration-testing consultant to inspect **one** specific private repository (`aegis-mobile`) without letting them see internal Organization Teams or `Internal` repositories, how should you add them?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**

### 85. A regulated FinTech deploys **GitHub Enterprise Cloud with Enterprise Managed Users (`EMUs`)** and **GitHub Copilot Enterprise**. Which two enterprise governance guarantees apply? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **E.** Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability

### 86. A bank engineer signed in with their corporate **Enterprise Managed User (`EMU`)** account (`alex_aegis`) wants to push a personal weekend hobby blog to a public repository under `alex_aegis` and open a Pull Request on `torvalds/linux`. Proposed solution: Use the `alex_aegis` EMU account to create a public repository and contribute to `torvalds/linux`. Will GitHub allow this?

- **A.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 87. To prevent **GitHub Copilot** from reading `.env.production` or `/secrets-fixtures/**` files even inside authorized repositories on Business/Enterprise plans, which administrative repository/org setting excludes specified file paths from Copilot context?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions

### 88. An Enterprise Owner defines an **Organization-level Repository Ruleset** enforcing SOX change-management controls across all `*-ledger` repositories (`main` and `release/*`). Which three rules enforce compliance? Select three.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)
- **E.** Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`
- **F.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 89. Why do enterprise administrators increasingly prefer **Repository Rulesets** over legacy single-branch **Branch protection rules**?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**

### 90. A bank repository Admin enables branch protection on `main` requiring 2 PR approvals, yet leaves **`Do not allow bypassing the above settings`** (`Include administrators`) **unchecked**. Proposed solution: Assume repository `Admins` are also blocked from merging unapproved emergency PRs under that default configuration. Are repository `Admins` blocked when bypass restrictions are unchecked?

- **A.** No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.
- **B.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **C.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 91. In a regulated FinTech Organization hosting sensitive PCI repositories alongside general tooling, what should `Organization Settings -> Member privileges -> Base permissions` be set to (`None`, `Read`, `Write`, or `Admin`)?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**

### 92. When child team `@aegis/cards-backend` is nested underneath parent team `@aegis/payments-division` (`which holds Read on aegis-shared-schemas`), does `@aegis/cards-backend` automatically inherit `Read` on `aegis-shared-schemas`?

- **A.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** **Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

---

## Domain 7 — Explore the GitHub community (5–10% official weight · 8 questions)

### 93. A corporate Open Source Program Office (`OSPO`) wants to fund 25 critical open-source libraries on **GitHub Sponsors** through a single annual corporate procurement invoice rather than 25 individual employee credit-card charges. Does GitHub Sponsors support organization-level invoiced sponsorship?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)

### 94. When an open-source maintainer discovers a critical vulnerability in their **public** repository, which free GitHub feature lets them collaborate with the reporter in a **temporary private fork**, request a **`CVE` ID** (`GitHub is a CVE Numbering Authority`), and publish a coordinated advisory?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **C.** GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

### 95. How does **Following an Organization** (`e.g., @openfga` or `@cncf`) on GitHub help security and platform architects stay informed without receiving hundreds of Issue emails?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 96. When an Organization Member wants to install a third-party **GitHub App** from **GitHub Marketplace** onto `@aegisledger` private repositories, what governance safeguard prevents shadow-IT OAuth/App sprawl?

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts

### 97. A regulated bank builds an internal **InnerSource** portal for shared fraud-detection SDKs across 3 divisions inside its GitHub Enterprise. Which two practices balance open internal reuse with strict compliance? Select two.

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**
- **C.** Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 98. In an **InnerSource** model, who serves as the **"Trusted Committer"** (`maintainer`) responsible for reviewing cross-division Pull Requests and upholding architectural quality on a shared internal library?

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** **InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 99. An OSPO-approved engineer contributes a TLS 1.3 cipher fix to an upstream open-source Java library (`from their personal non-EMU account`). Which four-step workflow applies?

- **A.** Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights
- **B.** Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge
- **C.** Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor
- **D.** Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream

### 100. Inside a GitHub Enterprise Organization, an admin wants to allow employees to fork `Internal` repositories into internal orgs for InnerSource **while blocking forks to external personal accounts**. Is granular fork policy supported?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability

---

## Answer Key and Explanations

### Question 1 — `B, E` (Understand Git and GitHub basics)

Correct answers: B and E (are correct). Full local history across clones protects against central data loss, while immutable commit SHAs, author attribution (`git blame`), and `git revert` provide auditable change control. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Correct. Commit metadata provides line-by-line accountability and clean rollback via `git revert`.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.

### Question 2 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Each Git commit hash cryptographically incorporates its parent commit SHA(s) plus the root tree hash, forming a tamper-evident Merkle DAG! [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 3 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Configure cryptographic **commit signing** (`git commit -S` via **GPG**, **SSH**, or **S/MIME** X.509 keys uploaded to GitHub) so GitHub verifies signatures with a **`Verified`** badge! [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 4 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git log -n 5 --oneline` prints each recent commit's abbreviated SHA and subject line on a single line. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 5 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). No — **Git** is an open-source distributed VCS originally created by Linus Torvalds (`GPLv2`) that operates locally offline for commits, diffs, logs, and branches independent of GitHub.com. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 6 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). **GitHub CLI (`gh`)** (`cli.github.com`) lets developers interact with GitHub Issues, Pull Requests, Actions, Releases, and Codespaces directly from the terminal alongside `git`. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 7 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Yes — commits and Pull Request merges performed directly via the GitHub web interface (and authorized GitHub API flows) are automatically signed by GitHub and display **`Verified`**. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **C:** Incorrect. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 8 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). **SSH** (`port 22`, or SSH over HTTPS port `443` via `ssh.github.com`) authenticates Git operations using your local private SSH key (`e.g., ~/.ssh/id_ed25519`) matched against the public key in GitHub Settings. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 9 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Modify `settlement.java` in the working directory, stage it with `git add`, record a local snapshot with `git commit -m`, and upload commits to GitHub with `git push`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).
- **B:** Incorrect. Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.
- **C:** Incorrect. Committing before editing and staging captures nothing from the intended file modifications.
- **D:** Incorrect. `git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.

### Question 10 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `git restore config/dev.yaml` discards unstaged working-directory modifications and restores the file to match the index/`HEAD`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).

### Question 11 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git show <commit-sha>` displays the metadata header and unified diff introduced by that specific commit. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.

### Question 12 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `HEAD` points to your currently checked-out local branch reference (which in turn points to the latest commit SHA on that branch). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Git branches are lightweight commit pointers rather than full folder copies, letting teams develop features safely without destabilizing `main`.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 13 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Running `git fetch --prune` (or `git fetch -p`) removes stale local `origin/*` remote-tracking references that no longer exist on the GitHub remote. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.

### Question 14 — `A, E` (Understand Git and GitHub basics)

Correct answers: A and E (are correct). Use separate **GitHub Organizations** for business-unit repositories and Teams, governed under a single **GitHub Enterprise** account for centralized SSO, audit streaming, and policies. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. Enterprise accounts unify security, identity, and policy governance across multiple organizations.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **E:** Correct. Organizations centralize multi-developer ownership and team-based RBAC.

### Question 15 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). **GitHub Enterprise Server (`GHES`)** deploys as a self-hosted virtual appliance inside the customer's own data center or private cloud while keeping familiar GitHub workflows. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.

### Question 16 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Yes — GitHub Enterprise licensing encompasses both **Enterprise Cloud (`GHEC`)** and **Enterprise Server (`GHES`)**, supporting hybrid deployments and unified license tracking. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 17 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Assigning the **Billing manager** role grants access solely to billing settings and usage reports without exposing repository source code. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 18 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Create a descriptive branch off `main`, commit the validator and open a Pull Request, pass automated CI checks and peer review, then merge into `main` and delete the branch. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.
- **B:** Correct. GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.
- **C:** Incorrect. Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.
- **D:** Incorrect. GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.

### Question 19 — `C, D` (Understand Git and GitHub basics)

Correct answers: C and D (are correct). Every change happens on a dedicated short-lived branch (never direct pushes to `main`), and protected Pull Requests enforce independent peer review plus automated CI checks before merge. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Correct. Pull Requests combine asynchronous peer review and automated CI verification prior to merging.
- **D:** Correct. GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.
- **E:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 20 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). **`Squash and merge`** condenses all commits from the topic branch into one atomic commit on `main`, keeping `main` history clean and concise. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. GitHub Flow is a lightweight, branch-based workflow without complex long-lived `release`/`develop` trees, centered on short-lived branches and Pull Requests.

### Question 21 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Restricting allowed merge methods enforces a uniform linear commit history on `main` where every commit maps 1-to-1 to a reviewed Pull Request (`#1234`). [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.

### Question 22 — `B, D, F` (Understand Git and GitHub basics)

Correct answers: B, D, and F (are correct). `- [ ]` task lists, `> [!WARNING]` / `> [!CAUTION]` alerts, and ```` ```mermaid ```` diagram blocks. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Correct. GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.
- **E:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **F:** Correct. GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.

### Question 23 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). GitHub Flavored Markdown supports **LaTeX / MathJax** mathematical expressions wrapped in `$...$`, `$$...$$`, or ```` ```math ```` fenced blocks! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 24 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Writing `owner/repository#number` (`aegisledger/audit#95`) links directly across repositories and records a cross-reference event on Issue `#95`'s timeline! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Correct. GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 25 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Wrapping text in double tildes (`~~...~~`) renders **strikethrough** formatting (`useful when marking superseded scope items without deleting audit context`). [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 26 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). **GitHub Desktop** lets users select individual diff lines or hunks to include or exclude them from a commit visually. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.

### Question 27 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). GitHub Mobile acts as a verified **two-factor authentication (`2FA`) push-approval / number-matching** authenticator for `github.com` sign-ins! [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **C:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **D:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.

### Question 28 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). GitHub Desktop lists the exact conflicted files with a 1-button shortcut to open them in your configured external editor (such as VS Code) and tracks remaining conflict markers until all are resolved! [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **D:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.

### Question 29 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Add `.github/CODEOWNERS` mapping `/card-vault/** @aegis/pci-auditors`, merge it into `main`, enable branch protection/rulesets requiring PR reviews, and enable `Require review from Code Owners`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. `README.md` does not trigger automatic review requests or merge enforcement.
- **B:** Incorrect. Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.
- **C:** Correct. `CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.
- **D:** Incorrect. GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.

### Question 30 — `A, B` (Work with GitHub repositories)

Correct answers: A and B (are correct). Order matters in `CODEOWNERS` (**the last matching pattern wins** -> `@aegis/pci-auditors`); valid `CODEOWNERS` resides in `.github/`, root, or `docs/` and requires branch protection/rulesets with Code Owner review enabled! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **B:** Correct. GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.
- **C:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **E:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 31 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Creating a public **`.github`** repository (`aegisledger/.github`) provides organization-wide default community health files and Issue/PR templates to any repo that lacks its own override! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Correct. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **B:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **C:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 32 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). No — attaching `MIT` grants broad open-source redistribution rights; proprietary internal repositories either omit an open-source license or include a proprietary/internal company copyright header per legal policy. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 33 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). No — Forking copies the entire historical commit graph and couples all 25 repositories inside one fork network; configure `aegis-java-compliance-starter` as a **Template repository** instead! [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — Forking copies the entire historical commit graph and couples all 25 repositories inside one fork network; configure `aegis-java-compliance-starter` as a **Template repository** instead!
- **C:** Correct. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 34 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Committing a **`.gitattributes`** file (`* text=auto`) normalizes line endings consistently across Windows, macOS, and Linux clones! [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Correct. `.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 35 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Keeping a stable default branch (`main`) ensures Pull Requests, `CODEOWNERS`, security scanning (`CodeQL`/`Dependabot`), Issue auto-close keywords, and status badges always anchor to one authoritative baseline. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 36 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Selecting **`Blame`** (`git blame` view, including `View blame prior to this change` buttons!) traces line-by-line authorship and historical context directly in the browser. [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 37 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). No — when `main` requires Pull Requests (`including for admins` if configured), GitHub's web editor automatically prompts to **`Create a new branch for this commit and start a pull request`**! [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 38 — `B, E` (Work with GitHub repositories)

Correct answers: B and E (are correct). Enable the **Dependency graph** (`Insights -> Dependency graph -> Export SBOM`) and enable **Dependabot alerts / security updates**. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Correct. Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Correct. The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.

### Question 39 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). GitHub exports a standards-compliant **`SPDX`** (`Software Package Data Exchange`) JSON Software Bill of Materials listing direct and transitive dependencies. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Correct. Enabling the Dependency graph identifies direct/transitive packages, feeds Dependabot vulnerability alerts, and exports NTIA/SPDX Software Bills of Materials (`SBOM`).
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.

### Question 40 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Open **`Feature preview`** from the top-right user profile menu on `github.com` to enable or disable per-user beta UI features at any time. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Correct. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 41 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). **Archive** `gateway-2019` (`Settings -> Danger Zone -> Archive this repository`) so all code, commits, Issues, and PR audit trails remain read-only and immutable. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 42 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Configure **Pinned repositories** on the Organization overview (GitHub Organizations support pinning both public repos for visitors and member-only private/internal repos for signed-in org members!). [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 43 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). No — enabling `Require approval of the most recent reviewable push` ensures someone **other than** the last pusher must approve the latest changes (`enforcing strict separation of duties`). [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.

### Question 44 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Submitting a review with **`Request changes`** places a formal merge block on the Pull Request until that reviewer subsequently approves or a privileged maintainer dismisses the stale review with justification. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 45 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Discussions keep open-ended architectural debates organized by category/threads without inflating engineering bug/backlog Issue metrics—and convert cleanly into Issues once actionable! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **B:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 46 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). `Close as completed` signals the work was resolved/shipped, whereas `Close as not planned` distinguishes duplicates, won't-fix items, or out-of-scope requests in search (`reason:"not planned"`) and Project charts! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.

### Question 47 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Triage Issue `#42` with labels/milestone/assignee, commit the fix on a feature branch, open a Pull Request referencing `Resolves #42` targeting `main`, and merge the approved PR into `main`. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Closing the issue prematurely loses active tracking, and wiki edits or Discussions do not merge code changes.
- **B:** Incorrect. Only supported closing keywords merged into the default branch (or explicitly linked PRs) close an issue automatically.
- **C:** Incorrect. Gists are separate repositories and cannot auto-close repository Issues via closing keywords.
- **D:** Correct. Including a closing keyword (`Closes #42`, `Fixes #42`, `Resolves #42`) in a Pull Request targeting the default branch automatically closes Issue `#42` upon merge.

### Question 48 — `A, D` (Collaborate using GitHub)

Correct answers: A and D (are correct). Write `Closes #42` / `Fixes #42` / `Resolves #42` in the PR body targeting the default branch, or link Issue `#42` in the PR's **`Development`** sidebar. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. Manual `Development` sidebar links work across branches and display clear traceability on both timelines.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.
- **E:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 49 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Creating `.github/pull_request_template.md` automatically pre-fills every new Pull Request description with your standardized review and compliance checklist. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.
- **C:** Correct. YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 50 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Searching `is:pr is:merged review:none` (whereas `review:approved` finds approved PRs and `review:changes_requested` finds blocked PRs) surfaces unreviewed merges immediately. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Correct. GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 51 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Organizations verify `@aegisledger.com` and enable **`Restrict email notifications to only approved or verified domains`**, while users map `@aegisledger` notification routing to their verified corporate email! [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 52 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Select **`Unsubscribe`** in the right sidebar of Issue/PR `#899` to mute notifications for that single thread while keeping repository-wide notifications intact. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 53 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Selecting `Watch -> Custom` and checking **`Security alerts`** and **`Releases`** subscribes strictly to advisory/release events. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 54 — `B, E` (Collaborate using GitHub)

Correct answers: B and E (are correct). Deploy **GitHub Pages** with **private/enterprise access control** enabled, and enable **GitHub Discussions** (`Q&A` category) on the internal repository. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Correct. Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Correct. GitHub Pages renders repository docs into browsable websites with HTTPS.

### Question 55 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). No — **Secret Gists** are **not private**: anyone with the URL can view and clone them without signing in, and credentials must never be stored in Gists! [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Correct. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Secret Gists** are **not private**: anyone with the URL can view and clone them without signing in, and credentials must never be stored in Gists!

### Question 56 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Publishing Pages from a private repo requires `Pro`/`Team`/`Enterprise`, and **restricting reader access** (`private Pages`) requires **GitHub Enterprise Cloud**—on `Pro`/`Team`, Pages sites are publicly reachable on the web! [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 57 — `B, C` (Apply modern development practices)

Correct answers: B and C (are correct). Author YAML workflows inside `.github/workflows/` triggered by `on:` events, and target private **`self-hosted` / Enterprise larger VNet-integrated runners** in `runs-on:`! [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.
- **C:** Correct. Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.
- **D:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 58 — `B` (Apply modern development practices)

Correct answer: B (is correct). Configuring **OpenID Connect (`OIDC`)** federation in GitHub Actions mints short-lived, job-scoped JWT tokens trusted by your cloud provider with **zero stored long-lived secrets**! [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Correct. GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 59 — `A` (Apply modern development practices)

Correct answer: A (is correct). GitHub Actions secret precedence goes from **most specific to least specific**: **`Environment` overrides `Repository`, which overrides `Organization`**! [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.
- **B:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 60 — `A, C, D` (Apply modern development practices)

Correct answers: A, C, and D (are correct). **Copilot coding agent** opening draft PRs in an isolated Actions environment, **IDE Agent Mode** iterating across local workspace files and tests, and **multi-model selection** across admin-approved models. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.
- **D:** Correct. Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **F:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 61 — `A` (Apply modern development practices)

Correct answer: A (is correct). Committing **`.github/copilot-instructions.md`** injects repository-specific coding and security rules into Copilot Chat, IDE Agent Mode, code review, and coding agent sessions! [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. The January 2026 GH-900 blueprint distinguishes asynchronous **Copilot coding agent** on GitHub (assigned to Issues, opening PRs) from synchronous local **Agent Mode** inside your IDE, plus **MCP** servers and custom agents.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 62 — `A` (Apply modern development practices)

Correct answer: A (is correct). Request **`Copilot`** as a reviewer (**GitHub Copilot code review**), which posts inline review comments and actionable `Suggested changes` on the Pull Request diff! [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 63 — `C` (Apply modern development practices)

Correct answer: C (is correct). For **Copilot Business** and **Copilot Enterprise**, GitHub **does not** use customer prompts, suggestions, or private repository code to train foundational AI models! [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **C:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **D:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 64 — `D` (Apply modern development practices)

Correct answer: D (is correct). Setting **`Suggestions matching public code`** (`duplication detection filter`) to **`Block`** suppresses verbatim matches against public GitHub code (and logs code references when allowed). [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.

### Question 65 — `A` (Apply modern development practices)

Correct answer: A (is correct). Under **Enterprise Settings -> AI Controls -> Copilot -> Models**, admins explicitly enable or disable individual AI models across all member organizations! [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Correct. Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.
- **B:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 66 — `A` (Apply modern development practices)

Correct answer: A (is correct). Create `.devcontainer/devcontainer.json` with JDK 21 and security linters, configure `postCreateCommand` and `forwardPorts`, commit `devcontainer.json`, and launch cloud Codespaces per branch. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Correct. Committing `.devcontainer/devcontainer.json` standardizes runtimes, extensions, startup commands, and port forwarding for every contributor launching a Codespace.
- **B:** Incorrect. Wikis do not configure Codespaces, disabling Codespaces blocks creation, and `.` launches browser-only `github.dev`.
- **C:** Incorrect. `FUNDING.yml` configures sponsor buttons rather than Codespaces dev containers.
- **D:** Incorrect. Uncommitted manual installs vanish when a Codespace is deleted, and `github.dev` does not run dev containers.

### Question 67 — `C` (Apply modern development practices)

Correct answer: C (is correct). Source code stays inside cloud VMs governed by corporate policies, idle timeouts, and instant seat revocation—eliminating persistent source-code clones on contractor laptops! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **D:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.

### Question 68 — `C` (Apply modern development practices)

Correct answer: C (is correct). Configure encrypted **Codespaces secrets** (at User, Repository, or Organization scope), which mount securely as environment variables inside authorized Codespaces! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 69 — `B, C` (Apply modern development practices)

Correct answers: B and C (are correct). `github.dev` is a zero-compute browser editor (`press .` on any PR/repo) with no terminal, whereas **GitHub Codespaces** provisions a cloud VM with full terminal, compiler, and Docker execution. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Correct. Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.
- **C:** Correct. `github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 70 — `B` (Apply modern development practices)

Correct answer: B (is correct). No — `github.dev` runs purely in browser memory without a VM, kernel, or Docker daemon; launch a **GitHub Codespace** to run `docker compose up`. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **B:** Correct. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `github.dev` runs purely in browser memory without a VM, kernel, or Docker daemon; launch a **GitHub Codespace** to run `docker compose up`.

### Question 71 — `B, D` (Manage projects with GitHub)

Correct answers: B and D (are correct). Switch seamlessly across `Table`, `Board`, and `Roadmap` views over shared custom fields, and enable **Project workflows** plus **Project Insights** burn-up charts. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **B:** Correct. GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.
- **E:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 72 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Yes — Organization Projects support **`Private`** (invited collaborators/teams only) vs **`Internal`/`Organization`** visibility, independent of repository roles (note: viewers still only see underlying private repo Issue details if they also hold `Read` access on those repos!). [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Correct. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.

### Question 73 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Create the Organization Project with custom `Iteration` and `Severity` fields, add repository Issues/PRs, enable built-in `Item closed -> Done` workflows, and monitor Project Insights burn-up charts. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. `SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.
- **B:** Correct. GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.
- **C:** Incorrect. Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.
- **D:** Incorrect. Gists do not host Milestones or drive organization GitHub Projects automations.

### Question 74 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). The built-in **`Auto-archive items`** workflow archives stale/closed Project cards cleanly while keeping them restorable at any time. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Labels classify type/priority, Milestones measure progress toward a release goal inside a repository, and built-in Project workflows eliminate manual card dragging.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 75 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). **Saved replies** (`Settings -> Saved replies`) let reviewers insert personal standardized Markdown checklists across any Issue, Pull Request, or Discussion. [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.

### Question 76 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). Assignees establish unambiguous single-threaded ownership (`searchable via assignee:username` and visible on Project boards), preventing bystander diffusion of responsibility. [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 77 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). The default **Burn up** (`Historical` stacked area/line) chart in **Project Insights** visualizes completed work (`Done`) against total scope over time! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.

### Question 78 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). GitHub Projects supports five custom field types: **`Text`**, **`Number`**, **`Date`**, **`Single select`**, and **`Iteration`**. [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. `Iteration` fields track time-boxed sprints directly inside GitHub Projects without external agile plugins.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.

### Question 79 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Enable `2FA` via TOTP or FIDO2 security key, download and store one-time recovery codes safely, register a phishing-resistant passkey, and verify passkey/`2FA` sign-in. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.
- **B:** Incorrect. Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.
- **C:** Correct. Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.
- **D:** Incorrect. Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.

### Question 80 — `A, C` (Understand privacy, security, and administration)

Correct answers: A and C (are correct). Members lacking `2FA` are immediately removed from the organization; members protect accounts best by registering phishing-resistant **Passkeys**/security keys and saving **`2FA` recovery codes** offline! [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Correct. Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Correct. Recovery codes are essential to regain account access if a phone or hardware key is lost.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **E:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).

### Question 81 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Enabling **GitHub Secret Scanning Push Protection** intercepts high-confidence secrets during `git push` and blocks the push before credentials ever reach the remote repository! [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 82 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Grant the **`Read`** repository role (`view and clone code, Issues, and PRs with zero write or triage mutations`). [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.

### Question 83 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). Assign the built-in **`Security Manager`** organization role, granting organization-wide security alert visibility and security-setting administration without full `Organization Owner` privileges! [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 84 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Invite the consultant as an **Outside collaborator** (`Repository collaborator`) on `aegis-mobile` alone rather than adding them as an **Organization Member**! [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.

### Question 85 — `C, E` (Understand privacy, security, and administration)

Correct answers: C and E (are correct). Corporate IdP (`Entra ID`/`Okta`/`PingFederate`) controls user lifecycle via SSO + SCIM while blocking public repo/Gist leakage, and Enterprise AI Controls govern Copilot models, seats, and agents. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **E:** Correct. Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.

### Question 86 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). No — **EMU** accounts are strictly confined inside their enterprise (`no public repos, no Gists, no external PRs`); personal open-source work requires a separate personal GitHub account on an approved personal workflow. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Correct. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **EMU** accounts are strictly confined inside their enterprise (`no public repos, no Gists, no external PRs`); personal open-source work requires a separate personal GitHub account on an approved personal workflow.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 87 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Configure **Copilot content exclusions** (`excluding sensitive file paths/globs` in Repository or Organization Copilot settings) so Copilot ignores matching files across completions and Chat! [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Correct. Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.

### Question 88 — `B, D, E` (Understand privacy, security, and administration)

Correct answers: B, D, and E (are correct). Require Pull Requests with approvals + **Code Owner** review, require passing CI/CodeQL **status checks**, and block **force-pushes** plus branch deletions (plus optional required signed commits!). [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Blocking force-pushes and deletions protects commit history integrity on production branches.
- **E:** Correct. Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.
- **F:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 89 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Repository Rulesets layer cleanly (multiple rulesets apply simultaneously with **most restrictive wins**), span **organization-wide** repo patterns via fnmatch, support **`Evaluate`** dry-run mode, and protect both **branches and tags**! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.

### Question 90 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). No — unless you enforce rules on administrators (`Do not allow bypassing` / omitting Admin from Ruleset bypass actors), repository `Admins` can still bypass branch protection! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. `CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.
- **B:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **C:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — unless you enforce rules on administrators (`Do not allow bypassing` / omitting Admin from Ruleset bypass actors), repository `Admins` can still bypass branch protection!

### Question 91 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Set **Base permissions** to **`None`** (`least privilege`) so Organization Members gain access strictly to private repositories explicitly granted to their **GitHub Teams**! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.

### Question 92 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Yes — in nested GitHub Teams, **child teams inherit parent team access permissions** downward automatically! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Correct. Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 93 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Yes — organizations on GitHub can fund maintainers via **GitHub Sponsors for companies** using centralized organization billing (including invoiced billing for eligible enterprise customers). [Skill 7.1: Describe the benefits of open source and GitHub Sponsors | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Sponsors and open-source sustainability (https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Correct. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.

### Question 94 — `C` (Explore the GitHub community)

Correct answer: C (is correct). **GitHub Repository Security Advisories** (paired with **Private Vulnerability Reporting**) provide private patch collaboration, integrated CVE issuance, and coordinated Dependabot alert broadcasting at `$0` for public repos! [Skill 7.2: Explain how GitHub supports and advances open-source projects | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Supporting open-source projects with community profiles and Security Lab / advisories (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **C:** Correct. GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 95 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Following an Organization surfaces high-signal public events—such as **new public repository launches** and major releases—directly in your personal `Following` dashboard feed! [Skill 7.3: Identify how to follow users and organizations to stay informed about activity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Following people and organizations on GitHub to track activity (https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 96 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Non-owner members cannot install unapproved GitHub Apps across the org—instead they submit an **installation/OAuth app approval request** reviewed by an **Organization Owner**! [Skill 7.4: Describe the GitHub Marketplace and its purpose | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Marketplace for GitHub Apps and Actions (https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.

### Question 97 — `B, C` (Explore the GitHub community)

Correct answers: B and C (are correct). Publish SDKs as **`Internal`** Enterprise repositories with `README.md`, `CONTRIBUTING.md`, and enforced **`CODEOWNERS`**, and organize discovery via **Repository Topics** and cross-team Pull Requests. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.
- **C:** Correct. `Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 98 — `B` (Explore the GitHub community)

Correct answer: B (is correct). Designated domain maintainers (enforced via **`CODEOWNERS`** and `Maintain`/`Write` team roles) mentor internal contributors and gate merges to `main`, mirroring open-source maintainers! [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Correct. InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 99 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` (and CLA requirements), fork upstream and create a topic branch, commit and push the fix to the fork, and open a Pull Request to upstream. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.
- **B:** Incorrect. Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.
- **C:** Incorrect. Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.
- **D:** Correct. External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.

### Question 100 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Yes — Enterprise and Organization repository policies let admins restrict private/internal repository forking strictly to organizations within the Enterprise (blocking personal external forks)! [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Correct. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.
