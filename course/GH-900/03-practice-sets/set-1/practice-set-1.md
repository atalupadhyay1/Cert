# Microsoft Exam GH-900: GitHub Foundations — Full-Length Mock Exam 1

**Theme:** Product Engineering & Web Platform Teams — Git vs GitHub, GitHub Flow, Key Repo Files, Issues/PRs, Actions, Copilot Agents & 2FA/Passkeys  
**Credential:** `Microsoft Certified: GitHub Foundations` *(Beginner / Fundamentals · **no prerequisite** · **does not require renewal / never expires**)*  
**Study guide baseline:** `January 2026 (Last updated February 19, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-900 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Docs documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Understand Git and GitHub basics (25–30% official weight · 28 questions)

### 1. A web engineering team at `VelocePay` is replacing shared zip-folder backups (`checkout_v2_final_FINAL.zip`) with a Distributed Version Control System (`DVCS`). Which two core benefits do they gain immediately? Select two.

- **A.** Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely
- **B.** Every developer clone contains the full commit history and branches, enabling offline commits and history inspection
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 2. Unlike older Centralized Version Control Systems (`CVCS`) where a central server outage halts all commits and history lookups, why can developers using Git keep committing and inspecting logs while on an airplane offline?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 3. A release commit `a91f4c2` merged to `main` introduces a checkout tax calculation bug, and three newer commits have already landed after it. Which safe Git command (`git ____ a91f4c2`) creates a new inverse commit undoing `a91f4c2` without rewriting shared history?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 4. While investigating why a payment timeout constant changed from `30` to `5` seconds six months ago, which Git feature (`git ____ src/config.ts` or GitHub's web `Blame` view) attributes every individual line of a file to its last modifying commit, author, and commit message?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go

### 5. A junior business analyst preparing for onboarding asks how **Git** differs from **GitHub**. Which statement accurately distinguishes the two?

- **A.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **B.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 6. Which capability is provided natively by **GitHub** as a cloud platform rather than by standalone local **Git** on an isolated laptop?

- **A.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them

### 7. An embedded-firmware team works inside an air-gapped lab with zero internet connectivity for two weeks before syncing to their corporate cloud remote. Proposed solution: Initialize a local repository with `git init`, create branches, and record `git commit` snapshots locally until network access returns. Does the solution work without `github.com` access?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 8. Can a local Git repository push and fetch commits with non-GitHub remotes, or is the `.git` repository format proprietary to `github.com`?

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 9. A developer modifies `src/cart.js` locally on a feature branch and wants to publish those changes cleanly to the remote repository on GitHub. Which four-step Git lifecycle sequence applies?

- **A.** Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`
- **B.** Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`
- **C.** Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`
- **D.** Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`

### 10. In Git's three-state architecture, what is the role of the **staging area** (also called the **index**, populated via `git ____ <file>`) between your working directory and `.git` commit history?

- **A.** Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 11. What uniquely identifies every Git commit (`e.g., 4f8b2d1...`) and guarantees cryptographic integrity across distributed clones?

- **A.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message

### 12. When you run `git switch -c feat/apple-pay` (or `git checkout -b ____`) in a 2 GB repository, why does creating a branch finish in milliseconds without duplicating 2 GB of files?

- **A.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** A lightweight movable pointer to a commit that isolates feature or bugfix work from the default branch (`main`) until merged
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 13. Your teammate pushed commits to `origin/feat/search` and you want to download those remote branch updates to inspect `git log origin/feat/search` **without** merging anything into your active working files yet. Which command (`git ____ origin`) should you run?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits

### 14. A fast-growing fintech scales from 5 engineers to 450 engineers across four business units (`Payments`, `Risk`, `Core`, `Mobile`) requiring nested Teams, SAML SSO, and centralized policy governance. Which two GitHub account structures fit this growth? Select two.

- **A.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **E.** Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies

### 15. Which GitHub account type represents an individual person's identity (`GitHub Free` or `GitHub Pro`) that can own personal repositories and be invited as a member across multiple GitHub Organizations?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 16. Why should a startup store its production repositories inside a **GitHub Organization** rather than inside the founding CTO's **Personal account**?

- **A.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **B.** Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 17. A regulated bank requires single-tenant data residency or self-hosted appliance deployment options alongside cloud SaaS governance across 12 GitHub Organizations. Which two deployment options are included in **GitHub Enterprise**?

- **A.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing

### 18. Your web platform team adopts **GitHub Flow** for continuous delivery on `lumen-web`. Which four-step collaborative sequence follows official GitHub Flow practices?

- **A.** Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks
- **B.** Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch
- **C.** Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge
- **D.** Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review

### 19. Which two principles define **GitHub Flow** compared to heavy multi-month release-branch models? Select two.

- **A.** Create a short-lived descriptive branch off `main` so `main` stays deployable at all times
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`
- **E.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically

### 20. You want teammates to comment on your early API refactoring approach and trigger CI checks, while preventing anyone from accidentally merging the incomplete branch into `main`. Which Pull Request state (`Create ____ pull request`) should you open?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 21. While merging `main` into your feature branch, Git pauses and inserts `<<<<<<< HEAD`, `=======`, and `>>>>>>> main` inside `package.json`. What do those markers indicate?

- **A.** Resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in affected files, stage the clean file (`git add`), and complete the merge commit
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 22. An engineering lead standardizes Pull Request descriptions across `KestrelCloud` using GitHub Flavored Markdown (`GFM`). Which three Markdown capabilities are natively rendered on GitHub? Select three.

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax
- **D.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **E.** Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`
- **F.** Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)

### 23. In a GitHub Issue body, which Markdown syntax renders an unchecked interactive task-list checkbox that displays a completion progress bar (`e.g., 2 of 5 tasks`) on the Issues list: `____ Write unit tests`?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 24. You want to embed an interactive architecture flowchart inside `README.md` without committing static `.png` screenshots by writing diagram syntax inside ```` ```____ ````. Which fenced code block identifier renders diagrams natively on GitHub?

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** `.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking

### 25. Inside a Pull Request comment, typing `____` followed by an Issue number (`e.g., 108`) automatically creates a hoverable link to that Issue or Pull Request in the same repository. Which single character triggers Issue/PR autolinking?

- **A.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **B.** `@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 26. A UX designer on macOS wants to clone a design-tokens repository, visually compare side-by-side diffs, stage only 4 specific lines out of a modified CSS file, and commit to a branch **without** typing terminal Git commands. Which official tool fits best?

- **A.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 27. While commuting on a train with an iPhone, an engineering manager needs to review a 6-line hotfix Pull Request diff, leave an approval review, merge the PR, and clear notification inbox items. Which official GitHub app is purpose-built for this?

- **A.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **B.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **C.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **D.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 28. Can **GitHub Desktop** attribute a single commit to two pairing teammates (`Co-authored-by: Name <email>`) directly from the commit summary footer without manual trailer formatting?

- **A.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **D.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)

---

## Domain 2 — Work with GitHub repositories (10–15% official weight · 14 questions)

### 29. Your platform security lead wants every Pull Request modifying `/terraform/**` in `kestrel-infra` to automatically request and **require** approval from `@kestrel/cloud-sre` before merging into `main`. Which four-step sequence enforces this?

- **A.** Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`
- **B.** Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests
- **C.** Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings
- **D.** Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages

### 30. A team commits a `CODEOWNERS` file, yet Pull Requests modifying owned files neither request reviews nor block merging. Which two requirements must be verified? Select two.

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **C.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **E.** Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch

### 31. An open-source developer publishes a utility library in a `Public` GitHub repository without adding a `____` file (`e.g., MIT` or `Apache-2.0`). Under GitHub Terms of Service and copyright law, what may external companies legally do with that code?

- **A.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage

### 32. Which special community health file (`____.md` placed in root, `.github/`, or `docs/`) populates the repository `Security -> Policy` tab to instruct researchers how to disclose vulnerabilities privately?

- **A.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **B.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request

### 33. Your platform team built a golden starter microservice repository (`node-service-starter`) with standard `.github/workflows/`, `Dockerfile`, and linting configs. How should product squads (`gh repo create my-svc --____ org/node-service-starter`) spin up 15 independent new services with **clean 1-commit histories**?

- **A.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link

### 34. Over six months, `lumen-api` accumulates 340 stale merged feature branches on GitHub after Pull Requests merge. Which single checkbox in `Settings -> General -> Pull Requests` cleans up future merged branches automatically?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings
- **D.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**

### 35. Which repository root file (`____`) uses glob patterns like `node_modules/`, `dist/`, and `*.log` to stop Git from staging untracked local build artifacts?

- **A.** `.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** No — adding `.env` to `.gitignore` only ignores **untracked** files; a file already committed to Git continues being tracked until `git rm --cached .env` removes it from the index (and any leaked secret is rotated!).
- **D.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers

### 36. A developer accidentally committed and pushed a local `config.local.json` file two commits ago and now wants Git to stop tracking future edits to it. Proposed solution: Append `config.local.json` to `.gitignore` and commit `.gitignore` without running `git rm --cached`. Does Git stop tracking `config.local.json`?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.
- **D.** No — adding `.env` to `.gitignore` only ignores **untracked** files; a file already committed to Git continues being tracked until `git rm --cached .env` removes it from the index (and any leaked secret is rotated!).

### 37. In GitHub's web interface (`Add file -> Create new file`), how do you create a new nested directory `docs/architecture/` containing `overview.md` when `docs/architecture/` does not exist yet?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **D.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`

### 38. An engineering director wants automated visibility into open-source packages across `VelocePay` repositories plus automated Pull Requests whenever a transitive `npm` dependency discloses a CVE. Which two features work together to deliver this? Select two.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)

### 39. Under a repository's **`Insights`** tab, which view summarizes merged Pull Requests, open Pull Requests, closed Issues, new Issues, and active commit authors over the past `24 hours`, `3 days`, `1 week`, or `1 month`?

- **A.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **B.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 40. A developer wants to bookmark 45 interesting open-source Rust and Go libraries grouped into custom categories (`CLI Tools`, `Web Frameworks`) **without** receiving Issue/PR notification emails from them. Which GitHub feature should they use?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 41. A legacy v1 SDK repository (`veloce-sdk-v1`) has reached end-of-support. You must freeze all code pushes, Issues, and Pull Requests while preserving historical releases, stars, and existing `git clone` URLs for legacy customers. What should you do?

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link

### 42. To maintain high collaboration quality on an active repository, adding `____.md` displays a banner link (`Please review the guidelines for contributing to this repository`) whenever a contributor opens a new Pull Request or Issue.

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

---

## Domain 3 — Collaborate using GitHub (10–15% official weight · 14 questions)

### 43. Your developer-relations team wants a dedicated space on the repository for open-ended community Q&A, feature polls, and monthly architecture RFCs—with `Mark as answer`—without cluttering the engineering bug tracker. Which feature should they enable?

- **A.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **B.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **C.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 44. While reviewing a Pull Request diff on GitHub.com, you spot a typo on line 42 and want the author to apply your exact corrected code line in a single button action (`Commit suggestion`). Which fenced Markdown block do you insert in your review comment: ```` ```____ ````?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **D.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms

### 45. When merging a feature Pull Request containing 19 noisy `"fix lint"` and `"wip"` commits into `main`, which Pull Request merge option condenses all 19 branch commits into **one** clean commit on `main`?

- **A.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 46. An open-ended brainstorm in **GitHub Discussions** reaches consensus that a concrete pagination bug exists in `api/orders`. How can a maintainer turn that Discussion thread into a tracked engineering work item without retyping context?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **C.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 47. A developer picks up bug Issue `#42` (`Cart total rounding error`) and wants Issue `#42` to close automatically the moment the approved fix lands on `main`. Which four-step workflow achieves this?

- **A.** Write `Mentioning #42` in a commit on a non-default experimental branch → Never open a Pull Request → Delete the feature branch → Expect Issue `#42` to close automatically
- **B.** Close Issue `#42` manually before writing code → Commit directly to a fork wiki → Open an unlinked Discussion post → Archive the repository
- **C.** Triage the Issue with labels, milestone, and assignee → Create a feature branch and commit the fix → Open a Pull Request containing `Closes #42` in its description → Merge the approved Pull Request into the default branch
- **D.** Create a secret Gist with `Fixes #42` → Star the repository → Watch releases only → Expect Gist save to close Issue `#42`

### 48. Which two methods officially link a Pull Request to an Issue on GitHub so merging the Pull Request closes the Issue automatically? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch

### 49. Maintainers complain that external bug reports omit OS version and reproduction steps. Placing YAML **Issue Forms** inside `.github/____/bug_report.yml` enforces required dropdowns and text inputs before an Issue can be submitted.

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** `.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists

### 50. In GitHub's Pull Requests search bar, which filter query lists all **open** Pull Requests where **your** review has been requested: `is:open is:pr ____:@me`?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`

### 51. A staff architect wants notifications from `kestrel-core` **only** when a new **Release** is published or a **Security alert** fires—ignoring hundreds of daily Issue/PR comments. Which repository **Watch** setting achieves this?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 52. Why did you suddenly start receiving email notifications on Issue `#219` in a repository where your Watch setting is the default **`Participating and @mentions`**?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 53. In GitHub's web **Notifications** inbox (`github.com/notifications`), you were CC'd on a noisy 90-comment thread that is no longer relevant to your team. Which action stops **all future notifications** from that specific Issue thread?

- **A.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks

### 54. An open-source documentation squad wants to publish a public searchable HTML documentation site from their repository AND host an interactive community Q&A forum alongside the repo. Which two GitHub features should they combine? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **E.** Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues

### 55. An engineer wants to share a staging database connection string containing a password solely with two teammates inside their organization. Proposed solution: Create a **Secret Gist** on `gist.github.com` and paste the URL into Slack. Does the solution keep the credential private to authenticated organization members?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 56. Which repository-attached feature provides a multi-page Markdown knowledge base (`Home`, sidebar navigation, and its own clonable `<repo>.wiki.git` backing repository) for long-form internal runbooks and design guides?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues

---

## Domain 4 — Apply modern development practices (10–15% official weight · 14 questions)

### 57. You want every push and Pull Request on `veloce-web` to automatically run `npm ci && npm test` on Ubuntu using **GitHub Actions**. Which four-step workflow creates and verifies this CI pipeline?

- **A.** Place `ci.yml` inside `docs/workflows/` → Omit `on:` triggers and `runs-on:` runner labels → Save as a personal Gist → Expect repository Pull Requests to run CI automatically
- **B.** Open `github.dev` with `.` key → Run `npm test` directly inside `github.dev` browser tab → Save output in a Wiki page → Expect automatic status checks on Pull Requests
- **C.** Create an Issue template in `.github/ISSUE_TEMPLATE/` → Assign `@copilot` to a Milestone → Star the repository → Expect Issue templates to execute unit tests on Linux runners
- **D.** Create `.github/workflows/ci.yml` → Define `on: [push, pull_request]` triggers → Configure `jobs` with `runs-on: ubuntu-latest` and test `steps` → Commit `ci.yml` and inspect logs in the `Actions` tab

### 58. Which two structural rules are mandatory for a valid **GitHub Actions** CI workflow file? Select two.

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`

### 59. In a GitHub Actions deployment workflow, how do you pass an encrypted API token named `NPM_PUBLISH_TOKEN` stored in Repository Secrets into an environment variable without hardcoding it: `NODE_AUTH_TOKEN: ${{ ____.NPM_PUBLISH_TOKEN }}`?

- **A.** Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers
- **B.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 60. Following the January 2026 GitHub Foundations blueprint, which three AI capabilities are available in modern **GitHub Copilot** workflows? Select three.

- **A.** **IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **E.** **Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request
- **F.** **Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity

### 61. How does **GitHub Copilot coding agent (cloud agent)** on GitHub.com differ operationally from **Agent Mode** inside Visual Studio Code?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **Copilot coding agent** works asynchronously on assigned GitHub Issues in an Actions sandbox to open draft PRs, whereas **IDE Agent Mode** edits local files and runs local terminal tasks autonomously
- **C.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`
- **D.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution

### 62. Why does **GitHub Copilot Chat** provide **multi-model support** (allowing developers to choose among models from OpenAI, Anthropic, Google, etc., or use auto model selection)?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** **Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 63. A CTO compares **GitHub Copilot Pro (Individuals)** against **GitHub Copilot Business** for 80 company developers. Which governance capability requires **Copilot Business** (or Enterprise) rather than standalone Individual accounts?

- **A.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **B.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 64. Your enterprise already runs **GitHub Enterprise Cloud** and wants Copilot Chat on `github.com` grounded in indexed internal repositories, Markdown **Copilot Knowledge Bases**, Pull Request diff summaries, and a larger monthly AI credit allowance. Which plan provides these capabilities?

- **A.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **B.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits

### 65. Does a company on **GitHub Team** (or free organization) have to purchase full **GitHub Enterprise Cloud** seats before buying **GitHub Copilot Business** for its developers?

- **A.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 66. Which configuration file path (`____/devcontainer.json`) tells **GitHub Codespaces** which Docker image, Node/Python runtime features, VS Code extensions, and `postCreateCommand` scripts to provision automatically?

- **A.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers
- **B.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 67. To speed up onboarding on a large monorepo where `npm install` and Rust compilation normally take 18 minutes on first boot, which **GitHub Codespaces** feature pre-runs container builds and caches ready-to-attach snapshots on every push to `main`?

- **A.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies

### 68. To prevent cloud billing surprises when developers close their laptop browser tabs without manually stopping a running 16-core **GitHub Codespace**, which built-in safeguard suspends compute billing automatically?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains

### 69. A developer asks when to press `.` to open **`github.dev`** versus launching a **GitHub Codespace**. Which two statements accurately contrast them? Select two.

- **A.** **`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal
- **B.** **GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 70. A QA engineer opens a repository in **`github.dev`** by pressing `.` and wants to start a PostgreSQL container and run `pytest` integration tests in an integrated Linux shell without leaving `github.dev`. Proposed solution: Open the terminal pane inside `github.dev` and run `docker compose up && pytest` directly on `github.dev` compute. Does the solution work?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.

---

## Domain 5 — Manage projects with GitHub (5–10% official weight · 8 questions)

### 71. A product squad tracks Q4 delivery across four microservice repositories (`web`, `api`, `ios`, `infra`) using **GitHub Projects**. Which two capabilities are natively supported? Select two.

- **A.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **B.** Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts
- **C.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields

### 72. Which **GitHub Projects** layout plots items horizontally across a calendar timeline (`month`, `quarter`, or `iteration` horizon) using start/target `Date` or `Iteration` fields to communicate executive delivery schedules?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **C.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account
- **D.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)

### 73. An engineering manager sets up a brand-new organization **GitHub Project** to manage two-week agile sprints with automated card movement and velocity tracking. Which four-step sequence completes setup?

- **A.** Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache
- **B.** Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts
- **C.** Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts
- **D.** Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards

### 74. Inside a single repository `veloce-ios`, you want to group 24 Issues and Pull Requests targeting `v3.2 App Store Launch` (due November 30) and display an automatic **completion percentage bar** (`e.g., 75% complete`). Which native repository feature fits best?

- **A.** **Labels** categorize Issues/PRs (`bug`, `priority:high`), **Milestones** track completion percentage toward a repository release target date, and **Project built-in workflows** auto-update `Status` when items close or PRs merge
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 75. An open-source lead creates 5 **Saved replies** in their personal GitHub settings (`Settings -> Saved replies`) and expects all 12 co-maintainers to see those exact Saved replies automatically in their own comment toolbars. Proposed solution: Create personal Saved replies once and rely on repository inheritance to share them across all maintainers. Does the solution work?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.
- **D.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.

### 76. Up to how many **Assignees** can be assigned to a single GitHub Issue or Pull Request on public and paid organization repositories to designate clear owners responsible for moving the work forward?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 77. In **GitHub Projects -> Insights**, which default historical chart plots open versus closed/done work items over time across a sprint or milestone to reveal scope creep and completion trajectory?

- **A.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **B.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **C.** **Dependency graph** parses manifest/lockfiles (`package-lock.json`, `requirements.txt`), powering **Dependabot alerts** and Enterprise **Dependency insights** / SBOM export for license and CVE visibility
- **D.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)

### 78. On GitHub Team and GitHub Enterprise plans, besides the default Burn up chart, what can a scrum master configure in **Project Insights** to compare story-point totals (`Sum of Estimate`) grouped by `Assignee` or `Priority`?

- **A.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **B.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues

---

## Domain 6 — Understand privacy, security, and administration (10–15% official weight · 14 questions)

### 79. A newly hired developer hardens their GitHub account to meet organization security compliance and resist credential-phishing attacks. Which four-step setup sequence follows GitHub security best practices?

- **A.** Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication
- **B.** Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes
- **C.** Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility
- **D.** Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in

### 80. Which two practices protect a GitHub user against both domain-spoofing phishing attacks and permanent lockout if a mobile authenticator phone breaks? Select two.

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**
- **C.** Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 81. Why is a **Passkey** (or FIDO2 hardware security key) stronger against real-time adversary-in-the-middle phishing sites than a 6-digit SMS or TOTP code?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** **Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 82. A non-coding product manager in your GitHub Organization needs to label, milestone, assign, close, and reopen Issues and Pull Requests on `kestrel-mobile` **without** permission to push code or change repository settings. Which repository role enforces least privilege?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 83. A senior tech lead needs to manage repository labels, branch protection rules, Pages, and Actions settings on `kestrel-api`, while being blocked from destructive actions such as **deleting** or **transferring** the repository. Which repository role fits best?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)

### 84. Your finance controller needs to update corporate credit cards, download monthly Actions/Copilot invoices, and monitor spending limits on your GitHub Organization **without** seeing any private source code. Which organization role should you assign?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 85. An enterprise CISO deploying GitHub Enterprise Cloud with Copilot wants strict corporate IdP lifecycle control over employee accounts plus central governance over AI coding agents and models. Which two enterprise controls address this? Select two.

- **A.** Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability
- **B.** Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **E.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them

### 86. A developer signed in with a corporate **Enterprise Managed User (`alice_veloce`)** account wants to publish an open-source personal side project as a `Public` repository under `alice_veloce` and submit PRs to external public repos. Proposed solution: Change repository visibility to `Public` under the EMU account. Does GitHub allow this?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 87. To satisfy legal compliance on **GitHub Copilot Business**, an organization owner configures `Suggestions matching public code` to **`____`**. Which setting filters out Copilot completions exceeding ~150 characters that match public GitHub code verbatim?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions

### 88. You harden the `main` branch of `veloce-ledger` using a **Repository Ruleset / Branch protection rule**. Which three protections prevent unreviewed, broken, or history-destroying pushes to `main`? Select three.

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`
- **F.** Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)

### 89. In a **GitHub Enterprise** account containing 6 sibling Organizations, which repository visibility level lets every authenticated enterprise member across all 6 Organizations read and fork `design-system` while keeping it 100% hidden from the public internet?

- **A.** Repository visibility levels: **`Public`** (open internet), **`Private`** (explicit users/teams only), and **`Internal`** (GitHub Enterprise only — readable by all enterprise members for **InnerSource**)
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 90. A developer accidentally stages an AWS secret key in `deploy.sh` and runs `git push origin feat/s3`. GitHub immediately rejects the push on the command line citing a detected high-confidence secret. Which security feature blocked the leak before it reached the repository?

- **A.** **Secret scanning with Push Protection** (blocks commits containing leaked credentials before they land on GitHub) paired with **Dependabot alerts & security updates** (opens automated PRs upgrading vulnerable dependencies)
- **B.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 91. To enforce least privilege when onboarding 200 employees into a GitHub Organization, what should Organization Owners set **`Member privileges -> Base permissions`** to so new members only access private repositories explicitly granted to their Teams?

- **A.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 92. In a GitHub Organization, parent team `@kestrel/backend` has `Read` access on `shared-proto`, and child team `@kestrel/payments-api` is nested underneath `@kestrel/backend`. What repository access do members of `@kestrel/payments-api` inherit automatically?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

---

## Domain 7 — Explore the GitHub community (5–10% official weight · 8 questions)

### 93. An open-source maintainer enables **GitHub Sponsors** and commits `.github/____.yml` so a `Sponsor` heart button appears at the top of their repository linking to GitHub Sponsors and Open Collective. Which configuration filename triggers the `Sponsor` button?

- **A.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 94. How does GitHub help maintainers attract newcomers to public open-source repositories via the **Community Standards** checklist and `github.com/topics`?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 95. You want to stay informed when a respected open-source maintainer or framework **Organization** creates new public repositories or stars projects in your dashboard **`Following`** feed—without getting emails on every Issue comment. What should you do?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 96. Where on GitHub can organization admins browse, verify (`Verified creator`), and install third-party **GitHub Apps** and reusable **GitHub Actions** (such as code coverage reporters, linters, and security scanners) with unified billing?

- **A.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 97. An enterprise VP of Engineering launches an **InnerSource** initiative across 12 internal product divisions on GitHub Enterprise Cloud. Which two practices establish healthy InnerSource collaboration? Select two.

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files
- **E.** Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**

### 98. In an **InnerSource** model inside a private enterprise, what is the role of **"trusted committers"** (often enforced via `CODEOWNERS`) on a shared internal platform library?

- **A.** **InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 99. You discover a documentation bug in an external public open-source repository where you do **not** have `Write` access. Which four-step workflow submits your fix cleanly to the upstream maintainers?

- **A.** Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream
- **B.** Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor
- **C.** Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge
- **D.** Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights

### 100. An engineer wants to fix a bug in an upstream open-source CLI tool and open a Pull Request back to the upstream repository. Proposed solution: Use **`Use this template`** (instead of **`Fork`**) to copy the repository, commit the fix, and open a Pull Request back to upstream `main`. Does the solution work?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.

---

## Answer Key and Explanations

### Question 1 — `A, B` (Understand Git and GitHub basics)

Correct answers: A and B (are correct). A DVCS gives every developer a complete local history for offline commits/inspection and records author/timestamp commit metadata for blame auditing and safe reverts. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Correct. Commit metadata provides line-by-line accountability and clean rollback via `git revert`.
- **B:** Correct. Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 2 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Because Git is distributed, every cloned working copy contains the full `.git` object database, commit graph, and branch history locally on disk. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 3 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git revert a91f4c2` generates a brand-new commit that cleanly inverses the changes introduced by `a91f4c2`, preserving a linear, auditable shared history on `main`. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 4 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Git `blame` annotates each line of a file with the commit SHA, author, and timestamp that last touched that line so engineers can trace historical rationale. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.

### Question 5 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Git is the open-source distributed version control engine running locally via CLI or GUI clients, whereas GitHub is the cloud collaboration platform hosting Git repositories and adding Pull Requests, Issues, Actions, and governance. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **B:** Incorrect. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 6 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Pull Requests with required Code Owner approvals, Issues, Discussions, GitHub Actions cloud runners, and organization RBAC are GitHub platform features built around Git repositories. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.

### Question 7 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Yes — Git is an independent distributed version control tool whose branching, staging, diffing, and committing operations run 100% locally without internet access. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.

### Question 8 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). The `.git` format is open-source and vendor-neutral; any standard Git repository can configure multiple remotes (`git remote add`) across GitHub Enterprise Cloud, GitHub Enterprise Server, or any Git server. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 9 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Changes begin in the local working directory, move to the staging index via `git add`, become an immutable local commit via `git commit -m`, and upload to GitHub via `git push`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. `git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.
- **B:** Incorrect. Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.
- **C:** Correct. Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).
- **D:** Incorrect. Committing before editing and staging captures nothing from the intended file modifications.

### Question 10 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). The staging area (`git add`) lets you selectively craft which modified files or hunks from your working directory will be bundled into the very next `git commit` snapshot. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 11 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Git computes a cryptographic `SHA` hash over the commit's root tree snapshot, parent commit hash(es), author/committer metadata, and commit message. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.

### Question 12 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). In Git, a branch is simply a tiny 41-byte movable pointer referencing an existing commit SHA rather than a physical duplicate copy of project directories. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Correct. Git branches are lightweight commit pointers rather than full folder copies, letting teams develop features safely without destabilizing `main`.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 13 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `git fetch origin` safely downloads new commits and remote-tracking branch refs from GitHub without altering your local working tree or current branch (`git pull` fetches **and** merges/rebases). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.

### Question 14 — `C, E` (Understand Git and GitHub basics)

Correct answers: C and E (are correct). Organizations provide shared repository ownership, nested Teams, and repository roles, while a GitHub Enterprise account governs multiple Organizations with centralized SSO, policies, and billing. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. Organizations centralize multi-developer ownership and team-based RBAC.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **E:** Correct. Enterprise accounts unify security, identity, and policy governance across multiple organizations.

### Question 15 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). A Personal account represents an individual user on GitHub.com who authenticates with their own credentials/2FA and participates across personal and organization repositories. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 16 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). An Organization ensures company repositories remain owned by the business with multiple Organization Owners, nested Teams, and granular roles even if an individual employee leaves. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **B:** Correct. Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 17 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). GitHub Enterprise offers cloud-hosted **GitHub Enterprise Cloud** (including data-residency `GHE.com` options) and self-hosted **GitHub Enterprise Server (`GHES`)**. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.

### Question 18 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). GitHub Flow branches off `main`, opens a Pull Request for peer review and automated CI status checks, merges into `main` once approved, and deletes the short-lived topic branch. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.
- **B:** Correct. GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.
- **C:** Incorrect. Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.
- **D:** Incorrect. Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.

### Question 19 — `A, D` (Understand Git and GitHub basics)

Correct answers: A and D (are correct). Keep `main` continuously deployable by branching short-lived work off `main`, and open Pull Requests early for peer code review and automated CI validation before merging. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Correct. GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. Pull Requests combine asynchronous peer review and automated CI verification prior to merging.
- **E:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).

### Question 20 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Opening a **Draft Pull Request** shares early commits and runs workflows while blocking merge actions until you explicitly mark it `Ready for review`. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 21 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Both branches modified overlapping lines in `package.json`, creating a merge conflict that you must edit to the desired final state, `git add`, and commit. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Correct. When two branches modify the same lines differently, Git inserts standard conflict markers that must be edited out, staged, and committed (or resolved in GitHub’s web conflict editor).
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 22 — `C, E, F` (Understand Git and GitHub basics)

Correct answers: C, E, and F (are correct). GitHub Flavored Markdown natively renders `- [ ]` / `- [x]` task lists, `> [!NOTE]` / `> [!WARNING]` alerts, and language-tagged fenced code blocks including live `mermaid` diagrams. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Correct. GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.
- **D:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **E:** Correct. GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.
- **F:** Correct. Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.

### Question 23 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Writing `- [ ] Write unit tests` (hyphen, space, brackets containing a space, and space before text; `- [x]` when checked) renders an interactive GFM task list item. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Correct. GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 24 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Tagging a fenced code block with ```` ```mermaid ```` instructs GitHub's Markdown renderer to draw flowcharts, sequence diagrams, and state diagrams directly in the browser. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Correct. Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. `.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.

### Question 25 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Prefixing an Issue or Pull Request number with `#` (`#108`) automatically links to that item and records a cross-reference in its timeline. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **B:** Correct. GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 26 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). **GitHub Desktop** provides a visual GUI on macOS and Windows for cloning, partial line-level staging, branch switching, stash management, and visual merge-conflict resolution. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 27 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). **GitHub Mobile** (`iOS` and `Android`) lets users triage notifications, review and approve/merge Pull Requests, manage Issues, and approve GitHub 2FA sign-in prompts on mobile devices. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **B:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **C:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **D:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 28 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Yes — GitHub Desktop includes a built-in `Add co-authors` button below the commit message box that formats `Co-authored-by:` commit trailers automatically. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **D:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.

### Question 29 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Add `.github/CODEOWNERS` mapping `/terraform/** @kestrel/cloud-sre`, merge it into `main`, enable branch protection / rulesets requiring PR reviews, and turn on `Require review from Code Owners`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Correct. `CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.
- **B:** Incorrect. Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.
- **C:** Incorrect. GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.
- **D:** Incorrect. `README.md` does not trigger automatic review requests or merge enforcement.

### Question 30 — `C, E` (Work with GitHub repositories)

Correct answers: C and E (are correct). Ensure `CODEOWNERS` resides in `.github/`, the repository root, or `docs/` on the target branch (with write-enabled owners), and enable `Require review from Code Owners` in branch protection or rulesets. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **C:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **E:** Correct. GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.

### Question 31 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Without a `LICENSE` file, default copyright reserves all rights—others may view and fork the repo on GitHub per Terms of Service, cannot legally copy, modify, or redistribute the code in commercial products. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).

### Question 32 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). `SECURITY.md` defines the repository's security policy and links external researchers to private reporting channels rather than public Issues. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **B:** Correct. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.

### Question 33 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Mark `node-service-starter` as a **Template repository** in Settings (`--template` in GitHub CLI or `Use this template` in web UI) so squads generate new independent repositories with clean commit history. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Correct. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.

### Question 34 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Enabling **`Automatically delete head branches`** deletes merged topic branches automatically right after their Pull Request merges (while still allowing one-button restore if needed). [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.
- **D:** Incorrect. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.

### Question 35 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). A `.gitignore` file specifies intentionally untracked files and directories that Git should ignore during `git status` and `git add`. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Correct. `.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Incorrect. `.gitignore` has no effect on files already tracked in the Git index; you must untrack via `git rm --cached` and immediately rotate exposed secrets.
- **D:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.

### Question 36 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). No — `.gitignore` applies only to **untracked** files; already-tracked files remain in the Git index until removed with `git rm --cached config.local.json` (and any exposed credentials must be rotated!). [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `.gitignore` applies only to **untracked** files; already-tracked files remain in the Git index until removed with `git rm --cached config.local.json` (and any exposed credentials must be rotated!).
- **C:** Incorrect. `CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.
- **D:** Correct. `.gitignore` has no effect on files already tracked in the Git index; you must untrack via `git rm --cached` and immediately rotate exposed secrets.

### Question 37 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Type `docs/architecture/` in the filename input box—every `/` character automatically creates a nested subdirectory banner before you type `overview.md` and commit. [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **D:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.

### Question 38 — `C, E` (Work with GitHub repositories)

Correct answers: C and E (are correct). Enable the **Dependency graph** to parse manifest/lockfiles and enable **Dependabot alerts / security updates** to flag CVEs and open automated upgrade Pull Requests. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Correct. Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Correct. The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.

### Question 39 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Repository **`Pulse`** (`Insights -> Pulse`) provides a concise activity snapshot of PR throughput, Issue activity, and contributor commits for the selected window. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Correct. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **B:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 40 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). **Starring** repositories and organizing starred repos into personal **Lists** bookmarks projects cleanly without subscribing to repository notification streams. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Correct. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 41 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). **Archive** the repository (`Settings -> General -> Danger Zone -> Archive this repository`) so it becomes visibly read-only while preserving every commit, release, and URL. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.

### Question 42 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Adding `CONTRIBUTING.md` (in root, `.github/`, or `docs/`) surfaces coding standards, test requirements, and PR etiquette right inside the new-Issue and new-PR UI. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Correct. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 43 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). **GitHub Discussions** provides threaded categories, polls, Q&A with accepted answers, and one-step promotion of validated ideas into actionable GitHub Issues. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **B:** Incorrect. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **C:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 44 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Wrapping replacement code inside a ```` ```suggestion ```` block renders an interactive diff preview that the PR author can commit directly from the Pull Request review thread. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **D:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.

### Question 45 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). **Squash and merge** combines all commits from the head branch into a single cohesive commit appended to the base branch (`main`). [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 46 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Use **`Create issue from discussion`** directly on the Discussion post, which pre-populates a new GitHub Issue and cross-links both threads automatically. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **C:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 47 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Triage Issue `#42` with labels/milestone/assignee, commit the fix on a feature branch, open a Pull Request referencing `Closes #42` targeting `main`, and merge the approved Pull Request. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Only supported closing keywords merged into the default branch (or explicitly linked PRs) close an issue automatically.
- **B:** Incorrect. Closing the issue prematurely loses active tracking, and wiki edits or Discussions do not merge code changes.
- **C:** Correct. Including a closing keyword (`Closes #42`, `Fixes #42`, `Resolves #42`) in a Pull Request targeting the default branch automatically closes Issue `#42` upon merge.
- **D:** Incorrect. Gists are separate repositories and cannot auto-close repository Issues via closing keywords.

### Question 48 — `B, E` (Collaborate using GitHub)

Correct answers: B and E (are correct). Write a closing keyword (`Closes #N`, `Fixes #N`, `Resolves #N`) in the PR description targeting the default branch, or link the Issue manually in the Pull Request's `Development` sidebar. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Correct. Manual `Development` sidebar links work across branches and display clear traceability on both timelines.
- **C:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Correct. Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.

### Question 49 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Storing `.yml` Issue Form definitions in `.github/ISSUE_TEMPLATE/` renders validated web forms with required fields, dropdowns, and automatic labels. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Correct. YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.

### Question 50 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Using `is:open is:pr review-requested:@me` (alongside `assignee:@me` or `author:@me`) filters open Pull Requests awaiting your code review. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.

### Question 51 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Select **`Watch -> Custom`** on `kestrel-core` and check only `Releases` and `Security alerts` (rather than `All Activity`). [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 52 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Under `Participating and @mentions`, GitHub automatically subscribes you to a thread whenever someone `@mentions` your username or a `@org/team` you belong to, or when you comment/are assigned. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 53 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Selecting **`Unsubscribe`** (`Mute thread`) on that notification item unsubscribes you from future updates on that thread unless you are directly `@mentioned` again. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.

### Question 54 — `B, E` (Collaborate using GitHub)

Correct answers: B and E (are correct). Publish the static documentation website with **GitHub Pages** and enable **GitHub Discussions** for threaded Q&A with accepted answers. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Correct. GitHub Pages renders repository docs into browsable websites with HTTPS.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **E:** Correct. Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.

### Question 55 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). No — Secret Gists are merely unlisted from search engines; anyone who obtains the URL can view and clone the Gist without signing in! Never put credentials in Gists. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Correct. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — Secret Gists are merely unlisted from search engines; anyone who obtains the URL can view and clone the Gist without signing in! Never put credentials in Gists.

### Question 56 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). A **GitHub Wiki** attaches a multi-page Markdown documentation portal directly to the repository without mixing prose runbooks into application source code folders. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.

### Question 57 — `D` (Apply modern development practices)

Correct answer: D (is correct). Create `.github/workflows/ci.yml`, configure `on: [push, pull_request]`, define a job with `runs-on: ubuntu-latest` and checkout/test steps, and commit `ci.yml` to inspect logs in `Actions`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. Workflow YAML files outside `.github/workflows/` are ignored by GitHub Actions, and `on:` plus `runs-on:` are required keys.
- **B:** Incorrect. `github.dev` has no compute terminal to execute `npm test` or report Pull Request status checks.
- **C:** Incorrect. Issue templates structure bug reports and never provision Actions runners or run unit tests.
- **D:** Correct. GitHub Actions workflows live as YAML files in `.github/workflows/`, trigger on defined events, execute job steps on specified runners, and report status in the `Actions` tab.

### Question 58 — `B, E` (Apply modern development practices)

Correct answers: B and E (are correct). Store the YAML workflow inside `.github/workflows/` with `on:` event triggers, and define `jobs:` specifying a `runs-on:` runner environment and `steps:`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Correct. GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Correct. Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.

### Question 59 — `A` (Apply modern development practices)

Correct answer: A (is correct). Referencing `${{ secrets.NPM_PUBLISH_TOKEN }}` injects the encrypted secret at runtime and automatically redacts (`***`) accidental log output. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.
- **B:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 60 — `A, E, F` (Apply modern development practices)

Correct answers: A, E, and F (are correct). Assigning Issues to **Copilot coding agent** for autonomous cloud draft PRs, using synchronous **IDE Agent Mode** for multi-file local edits/commands, and switching LLMs via **multi-model support**. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **E:** Correct. Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.
- **F:** Correct. Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.

### Question 61 — `B` (Apply modern development practices)

Correct answer: B (is correct). Copilot coding agent runs asynchronously in an ephemeral GitHub Actions cloud environment when assigned to an Issue/prompt and opens a draft PR, whereas IDE Agent Mode edits files and runs terminal commands locally inside your open IDE session. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. The January 2026 GH-900 blueprint distinguishes asynchronous **Copilot coding agent** on GitHub (assigned to Issues, opening PRs) from synchronous local **Agent Mode** inside your IDE, plus **MCP** servers and custom agents.
- **C:** Incorrect. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.
- **D:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.

### Question 62 — `C` (Apply modern development practices)

Correct answer: C (is correct). Different AI models optimize for low-latency everyday coding versus deep architectural reasoning or large context windows, letting developers match model strengths (and AI credit rates) to each task within org policy. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Correct. Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 63 — `A` (Apply modern development practices)

Correct answer: A (is correct). Centralized organization seat assignment, organization-wide policy controls (such as blocking public-code matches and governing models/agents), and commercial IP indemnity require Copilot Business or Enterprise. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **B:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 64 — `D` (Apply modern development practices)

Correct answer: D (is correct). **GitHub Copilot Enterprise** builds on Copilot Business for GitHub Enterprise Cloud customers, adding organization repository indexing, Knowledge Bases, PR summaries, and higher AI credit pools. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **B:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.

### Question 65 — `C` (Apply modern development practices)

Correct answer: C (is correct). No — **GitHub Copilot Business** can be purchased for organizations without requiring GitHub Enterprise Cloud (whereas **Copilot Enterprise** requires GitHub Enterprise Cloud). [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 66 — `B` (Apply modern development practices)

Correct answer: B (is correct). `.devcontainer/devcontainer.json` (or `.devcontainer.json`) declaratively defines the reproducible container environment for every Codespace launched on the repository. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.
- **B:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 67 — `D` (Apply modern development practices)

Correct answer: D (is correct). **Codespaces Prebuilds** run via GitHub Actions ahead of time so developers attach to an already-built, warm container environment in seconds. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.

### Question 68 — `B` (Apply modern development practices)

Correct answer: B (is correct). Codespaces enforces an automatic **idle timeout** (default `30 minutes`, configurable by user/org policy) that stops the compute VM while retaining disk state until the retention period expires. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).

### Question 69 — `A, B` (Apply modern development practices)

Correct answers: A and B (are correct). `github.dev` runs free in the browser with zero compute terminal for quick edits/PR browsing, while **GitHub Codespaces** provisions a cloud container VM with a full terminal, debugger, and port forwarding. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Correct. `github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.
- **B:** Correct. Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 70 — `D` (Apply modern development practices)

Correct answer: D (is correct). No — `github.dev` runs purely in the browser without any backing compute VM or shell execution; the engineer must select `Continue working on -> Create new codespace` to run containers and `pytest`. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `github.dev` runs purely in the browser without any backing compute VM or shell execution; the engineer must select `Continue working on -> Create new codespace` to run containers and `pytest`.
- **B:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Correct. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).

### Question 71 — `B, E` (Manage projects with GitHub)

Correct answers: B and E (are correct). Render the same cross-repository items across **Table**, **Board**, and **Roadmap** views with custom `Iteration` fields, and automate transitions with built-in **Project workflows** and **Insights** charts. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **B:** Correct. Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.
- **C:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Correct. GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.

### Question 72 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). The **`Roadmap`** layout renders Project items along a zoomable timeline calendar anchored to Date or Iteration fields. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **C:** Correct. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.
- **D:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.

### Question 73 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). Create the organization Project with custom `Iteration` and `Priority` fields, link repository Issues/PRs, enable built-in `Item closed -> Done` workflows, and monitor delivery in Project Insights charts. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.
- **B:** Incorrect. `SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.
- **C:** Correct. GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.
- **D:** Incorrect. Gists do not host Milestones or drive organization GitHub Projects automations.

### Question 74 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). A repository **Milestone** groups Issues and Pull Requests toward a target release date and automatically calculates open-vs-closed completion percentage. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Correct. Labels classify type/priority, Milestones measure progress toward a release goal inside a repository, and built-in Project workflows eliminate manual card dragging.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 75 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). No — **Saved replies** are scoped to an individual user's personal GitHub account rather than shared automatically at the repository level (for shared intake templates, use `.github/ISSUE_TEMPLATE/` or document team snippets). [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Saved replies** are scoped to an individual user's personal GitHub account rather than shared automatically at the repository level (for shared intake templates, use `.github/ISSUE_TEMPLATE/` or document team snippets).
- **C:** Correct. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.
- **D:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).

### Question 76 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). GitHub allows assigning up to **10** users to an Issue or Pull Request so co-owners are clearly accountable while avoiding "everyone owns it so nobody owns it" ambiguity. [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 77 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). The built-in **Burn up** (`Status over time`) chart in Project Insights tracks total scope alongside completed items across your chosen date or iteration range. [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **B:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **C:** Incorrect. Enabling the Dependency graph identifies direct/transitive packages, feeds Dependabot vulnerability alerts, and exports NTIA/SPDX Software Bills of Materials (`SBOM`).
- **D:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.

### Question 78 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Create **custom charts** (`Bar`, `Column`, `Line`, or `Stacked area`) filtered by view queries and aggregated (`Count`, `Sum`, `Average`, `Min`, `Max`) over custom `Number` fields! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **B:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.

### Question 79 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Enable `2FA` via TOTP or security key, download and store one-time recovery codes safely, register a phishing-resistant passkey in Account Security settings, and test passkey/`2FA` sign-in. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.
- **B:** Incorrect. Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.
- **C:** Incorrect. Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.
- **D:** Correct. Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.

### Question 80 — `B, C` (Understand privacy, security, and administration)

Correct answers: B and C (are correct). Register WebAuthn/FIDO2 **Passkeys** bound cryptographically to `github.com`, and store downloaded one-time **`2FA` recovery codes** in a secure password vault. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Correct. Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.
- **C:** Correct. Recovery codes are essential to regain account access if a phone or hardware key is lost.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 81 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). WebAuthn passkeys cryptographically bind authentication assertions to the exact browser origin (`github.com`), refusing to sign challenges on lookalike phishing domains (`g1thub-login.com`). [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Correct. Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 82 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). The **`Triage`** role grants full Issue and Pull Request management (`labels`, `assignees`, `milestones`, `close`/`reopen`) with zero code write or settings access. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 83 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). The **`Maintain`** role lets repository leads manage day-to-day repository configuration and branch protections without destructive `Admin` privileges (`delete` / `transfer` / security access changes). [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.

### Question 84 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Assign the **`Billing manager`** organization role, which grants access strictly to billing settings and invoices with zero access to organization repositories. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 85 — `A, B` (Understand privacy, security, and administration)

Correct answers: A and B (are correct). Deploy **Enterprise Managed Users (`EMUs`)** synced via SCIM/OIDC from the corporate IdP, and configure central **Copilot enterprise/organization policies** governing seats, models, public-code filters, and agents. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Correct. Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.
- **B:** Correct. EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **E:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.

### Question 86 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). No — **Enterprise Managed User (`EMU`)** accounts are strictly locked to enterprise-internal collaboration and cannot create `Public` repositories, personal Gists, or contribute to external repositories (use a separate personal GitHub.com account for personal OSS). [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Correct. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Enterprise Managed User (`EMU`)** accounts are strictly locked to enterprise-internal collaboration and cannot create `Public` repositories, personal Gists, or contribute to external repositories (use a separate personal GitHub.com account for personal OSS).

### Question 87 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Setting `Suggestions matching public code` to **`Block`** suppresses completions matching public code (and controls whether Copilot coding agent / IDE features may emit matching snippets). [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Correct. Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.

### Question 88 — `B, E, F` (Understand privacy, security, and administration)

Correct answers: B, E, and F (are correct). Require Pull Requests with approvals + **Code Owner** review, require passing **status checks** before merging, and block **force-pushes** and branch deletions on `main`. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.
- **F:** Correct. Blocking force-pushes and deletions protects commit history integrity on production branches.

### Question 89 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). **`Internal`** repository visibility grants implicit read (and fork) access to all members of the parent GitHub Enterprise while remaining completely private from external internet users. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. `Internal` visibility exists specifically in GitHub Enterprise organizations so all employees across sibling orgs can discover and fork repositories (`InnerSource`) without making code `Public`.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 90 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). **Secret scanning Push Protection** inspects incoming commits during `git push` and blocks known credential patterns before they ever enter remote commit history. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. Secret scanning Push Protection stops credential leaks proactively at `git push` time (free on all public repos and available via GitHub Secret Protection / GHAS on private repos).
- **B:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 91 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). Set Organization **Base permissions** to **`No permission`** (or `Read` only where InnerSource read-all is desired), granting `Write`/`Maintain` strictly via Team assignments. [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 92 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). Child teams **inherit** parent team permissions down the hierarchy, so `@kestrel/payments-api` automatically receives `Read` access on `shared-proto` (and `@kestrel/backend` mentions notify child members). [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Correct. Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 93 — `C` (Explore the GitHub community)

Correct answer: C (is correct). Adding `.github/FUNDING.yml` displays the repository `Sponsor` button, and GitHub charges `0%` platform fees on sponsorships from personal accounts. [Skill 7.1: Describe the benefits of open source and GitHub Sponsors | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Sponsors and open-source sustainability (https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)]

- **A:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 94 — `C` (Explore the GitHub community)

Correct answer: C (is correct). GitHub provides a Community Profile checklist (`README`, `LICENSE`, `CODE_OF_CONDUCT`, `CONTRIBUTING`, `SECURITY`, Issue/PR templates) and surfaces issues labeled **`good first issue`** and **`help wanted`** to prospective contributors. [Skill 7.2: Explain how GitHub supports and advances open-source projects | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Supporting open-source projects with community profiles and Security Lab / advisories (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Correct. GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 95 — `D` (Explore the GitHub community)

Correct answer: D (is correct). **Follow** that user or Organization on their GitHub profile page so their public milestones and new repositories appear in your personal dashboard `Following` feed. [Skill 7.3: Identify how to follow users and organizations to stay informed about activity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Following people and organizations on GitHub to track activity (https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Correct. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 96 — `A` (Explore the GitHub community)

Correct answer: A (is correct). **GitHub Marketplace** (`github.com/marketplace`) catalogs free and paid GitHub Apps and Actions vetted for personal and organization installation. [Skill 7.4: Describe the GitHub Marketplace and its purpose | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Marketplace for GitHub Apps and Actions (https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace)]

- **A:** Correct. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 97 — `D, E` (Explore the GitHub community)

Correct answers: D and E (are correct). Publish shared components as **`Internal`** repositories with `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` ("trusted committers"), and add **Repository Topics** while welcoming cross-team Pull Requests. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Correct. `Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.
- **E:** Correct. Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.

### Question 98 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Trusted committers steward architectural quality, mentor contributors from sibling business units, review incoming cross-team Pull Requests promptly, and maintain `CONTRIBUTING.md` onboarding docs. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.
- **B:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 99 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`, fork the repo and create a topic branch, commit and push your fix to your fork, and open a cross-repo Pull Request to upstream. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Correct. External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.
- **B:** Incorrect. Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.
- **C:** Incorrect. Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.
- **D:** Incorrect. Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.

### Question 100 — `D` (Explore the GitHub community)

Correct answer: D (is correct). No — creating a repository from a **Template** starts an independent repository with a brand-new, unrelated commit history that cannot submit a Pull Request back to upstream; use **`Fork`** instead! [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — creating a repository from a **Template** starts an independent repository with a brand-new, unrelated commit history that cannot submit a Pull Request back to upstream; use **`Fork`** instead!
- **B:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Correct. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
