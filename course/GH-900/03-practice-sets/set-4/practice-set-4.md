# Microsoft Exam GH-900: GitHub Foundations — Full-Length Mock Exam 4

**Theme:** Agile Product Management & Release Operations — GitHub Projects (Table/Board/Roadmap), Iterations, Milestones, Project Workflows & Insights  
**Credential:** `Microsoft Certified: GitHub Foundations` *(Beginner / Fundamentals · **no prerequisite** · **does not require renewal / never expires**)*  
**Study guide baseline:** `January 2026 (Last updated February 19, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-900 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Docs documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Understand Git and GitHub basics (25–30% official weight · 28 questions)

### 1. A release-operations team at `OrbitPulse` coordinates 18 product squads shipping weekly releases. Which two version-control guarantees protect release stability? Select two.

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Every developer clone contains the full commit history and branches, enabling offline commits and history inspection

### 2. Which Git feature (`git ____ -a v2.5.0 -m "Release 2.5.0"`) marks an immutable, human-readable version milestone on a specific release commit SHA (unlike a branch pointer that keeps moving forward)?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone

### 3. A product manager asks why version control eliminates overwriting a colleague's edits compared to saving files over a shared cloud folder (`final_v4_pm_edits.docx`). What mechanism prevents silent overwrites?

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery

### 4. While bisecting when a mobile login regression first appeared between known-good `v2.1.0` and broken `HEAD`, which built-in Git command (`git ____ start`) performs an automated binary search across commit history?

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 5. In an agile planning workshop, a scrum master asks whether **GitHub Projects**, **Milestones**, and **Pull Request review rules** are built into the local `git` binary. How should you answer?

- **A.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)

### 6. Which terminal command (`git ____`) initializes a brand-new empty `.git` directory inside an existing local project folder on macOS or Linux before any GitHub remote exists?

- **A.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 7. A data-science team prototypes notebooks locally using `git init` and `git commit` for a week before legal approves creating a private repository in their company's GitHub Organization. Proposed solution: Work locally with Git first, then run `git remote add origin <github-url>` and `git push -u origin main` once the GitHub repo is created. Does the solution preserve all week-1 commits?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.

### 8. When you create a **GitHub Release** (`v3.0.0`) in the GitHub web UI with auto-generated release notes and attached `.zip`/`.dmg` binaries, what underlying **Git** object does GitHub create or bind to?

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 9. A release engineer updates `CHANGELOG.md` locally on `release/v4.1` and publishes the commit to GitHub. Which four-step Git workflow sequence applies?

- **A.** Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`
- **B.** Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`
- **C.** Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`
- **D.** Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`

### 10. Which flag on `git add` (`git add ____`) interactively steps hunk-by-hunk through a modified file so you can stage bugfix lines into Commit 1 while leaving refactoring lines unstaged for Commit 2?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 11. Why does writing clear, concise **commit messages** (`50-char imperative subject line + optional body explaining WHY`) matter for release management on GitHub?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **D.** A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message

### 12. After `feat/onboarding-wizard` has been merged into `main`, which local Git command (`git branch ____ feat/onboarding-wizard`) safely deletes the local branch **only** if its commits are already fully merged?

- **A.** A lightweight movable pointer to a commit that isolates feature or bugfix work from the default branch (`main`) until merged
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 13. You have uncommitted local edits in `src/nav.tsx` and need to switch immediately to `main` to inspect a hotfix (`git ____` -> switch branch -> `git ____ pop`). Which Git command temporarily shelves dirty working-tree changes onto a local stack?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits

### 14. An agile product company organizes 14 cross-functional squads into GitHub Teams and acquires a sister company with its own GitHub Organization. Which two GitHub account structures fit their operating model? Select two.

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)
- **C.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **D.** Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies
- **E.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them

### 15. On **GitHub Team** vs **GitHub Free** for Organizations, which Project and repository features become available on **private** repositories when upgrading to **GitHub Team**?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions

### 16. Where can an Enterprise Owner inspect an immutable stream of administrative and security events (`repo.create`, `org.add_member`, `protected_branch.destroy`) across **all** Organizations in the enterprise?

- **A.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing

### 17. If a developer leaves Employer A (`@employer-a` org) and joins Employer B (`@employer-b` org) while using a standard **Personal GitHub account** (non-EMU), what happens when `@employer-a` removes them from `@employer-a`?

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 18. A squad implements a new checkout promo banner on `orbit-storefront` following **GitHub Flow**. Which four-step workflow applies?

- **A.** Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge
- **B.** Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch
- **C.** Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review
- **D.** Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks

### 19. In a continuous-deployment environment practicing **GitHub Flow**, which two habits keep daily production deployments low-risk? Select two.

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Create a short-lived descriptive branch off `main` so `main` stays deployable at all times

### 20. A developer opened a standard Pull Request, then realized product requirements changed mid-review and wants to prevent accidental merges while rewriting logic. Can an already-open Pull Request be converted back into a **Draft**?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 21. In a Pull Request merge conflict showing `<<<<<<< feature/promo`, `=======`, and `>>>>>>> main`, which section contains the changes coming from your **current head/feature branch** versus the target **base branch** (`main`)?

- **A.** Resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in affected files, stage the clean file (`git add`), and complete the merge commit
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 22. A TPM writes a quarterly launch Issue template in GitHub Flavored Markdown. Which three GFM elements create interactive launch checklists, highlighted release callouts, and dependency diagrams? Select three.

- **A.** Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`
- **E.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **F.** Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)

### 23. Which five official alert keywords are supported inside GitHub Flavored Markdown blockquotes (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, and `> [!____]`)?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)

### 24. In an Issue comment, you want to quote three lines from a customer's bug description verbatim as a styled vertical-bar quotation (`____ Customer reported HTTP 502 on checkout`). Which leading character creates a Markdown blockquote?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** `@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 25. When an inline code span itself needs to display a single backtick character inside Markdown (`e.g., showing template literal syntax`), how do you wrap it cleanly without breaking formatting?

- **A.** Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 26. A product operations analyst updates JSON feature-flag catalogs weekly on Windows and wants a guided visual button (`Create Pull Request` / `Preview Pull Request`) without touching `git` CLI commands. Which official desktop tool provides this?

- **A.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **B.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution

### 27. While walking between conference sessions, a TPM needs to check a **GitHub Project** status item, comment `@orbit/qa` on a release blocker Issue, and assign the Issue to an engineer. Which official tool handles this natively on mobile?

- **A.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies

### 28. On **GitHub Mobile**, can you filter your Notifications inbox by `Unread`, `Focused`, `Mentioned`, or `Review requested` and swipe to mark items `Done` or `Save`?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

---

## Domain 2 — Work with GitHub repositories (10–15% official weight · 14 questions)

### 29. Release governance requires every Pull Request modifying `/release-notes/**` or `CHANGELOG.md` in `orbit-core` to obtain required review from `@orbit/release-ops`. Which four-step sequence enforces this?

- **A.** Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests
- **B.** Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages
- **C.** Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`
- **D.** Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings

### 30. If a developer submits a syntax error on line 14 of `.github/CODEOWNERS` (or references a non-existent `@orbit/typo-team`), how does GitHub surface the problem and what two rules govern valid enforcement? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch
- **C.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **E.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

### 31. What happens when you create a brand-new Personal repository whose exact name matches your **GitHub username** (`e.g., veloria/veloria`) and commit a public `README.md` inside it?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **C.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 32. What is the distinct purpose of `CODE_OF_CONDUCT.md` compared to `CONTRIBUTING.md` in a GitHub repository?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 33. A PMO team creates a standardized `quarterly-launch-playbook` repository containing Markdown checklists and `.github/ISSUE_TEMPLATE/` forms. How should teams spin up a fresh copy every quarter without inheriting prior quarters' commit history?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability

### 34. On a repository's **Branches** page (`github.com/<org>/<repo>/branches`), what distinguishes **`Active`** branches from **`Stale`** branches?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 35. A QA lead notices `test-results/report.html` was committed to `main` last month and keeps showing dirty diffs on every test run. Proposed solution: Add `test-results/` to `.gitignore` alone without running `git rm -r --cached test-results/`. Will Git stop tracking `test-results/report.html`?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — adding `.env` to `.gitignore` only ignores **untracked** files; a file already committed to Git continues being tracked until `git rm --cached .env` removes it from the index (and any leaked secret is rotated!).
- **C.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 36. While reading `src/pricing.ts` on GitHub.com, you want to send a teammate a link to lines `45–60` that will **never shift** even if 100 new lines are added above line 45 tomorrow. Pressing `____` on that file page converts the URL from `/blob/main/...` to an immutable commit SHA permalink!

- **A.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 37. If you delete a file inside a repository using GitHub's web UI (`Delete file -> Commit changes`), is the file permanently erased from past Git history?

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`

### 38. Release managers require zero critical CVEs before cutting `v4.0`. Which two repository capabilities inventory open-source libraries and automatically propose version-bump Pull Requests? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests
- **C.** Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)
- **D.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **E.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 39. Under `Repository -> Insights -> ____`, which visual timeline displays the branching and merging commit graph across the base repository and active forks?

- **A.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 40. How many custom **Lists** (`e.g., Release Tooling`, `Design Inspiration`, `Observability`) can a GitHub user create to categorize their **Starred** repositories on their profile?

- **A.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **B.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 41. An engineering team deprecates `orbit-v1-monolith` and wants everyone visiting the repo to see a yellow banner stating *"This repository has been archived by the owner. It is now read-only."* while keeping old Issue links working. Proposed solution: Add a deprecation note pointing to `orbit-v2` in `README.md`, then **Archive** `orbit-v1-monolith` in Repository Settings. Does the solution meet all requirements?

- **A.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **B.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

### 42. Why is enabling `Automatically delete head branches` alongside squash-merging Pull Requests considered a core **repository maintenance** best practice?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request

---

## Domain 3 — Collaborate using GitHub (10–15% official weight · 14 questions)

### 43. A product manager wants customers to vote between three proposed dashboard widget layouts before committing engineering capacity to build one. Which GitHub Discussions category type (`____`) provides native multiple-choice community voting?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **C.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 44. A user mistakenly files a usage question (*"How do I format dates in locale fr-CA?"*) as a bug **Issue** `#312` instead of asking in **Discussions**. Which Issue sidebar action (`Convert to ____`) moves `#312` cleanly without losing the user's text?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **D.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains

### 45. In a Pull Request's **`Files changed`** tab, checking the **`____`** checkbox in the top-right corner of each reviewed file header collapses reviewed files and tracks personal review progress.

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 46. A contributor opens an Issue in `orbit-docs` that actually belongs in `orbit-api` inside the **same** GitHub Organization. Which sidebar action (`____ issue`) moves the Issue while preserving comments, labels, and assignees?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 47. A frontend engineer fixes accessibility bug Issue `#42` on `orbit-web` and wants `#42` closed automatically when the PR lands on `main`. Which four-step workflow applies?

- **A.** Triage the Issue with labels, milestone, and assignee → Create a feature branch and commit the fix → Open a Pull Request containing `Closes #42` in its description → Merge the approved Pull Request into the default branch
- **B.** Close Issue `#42` manually before writing code → Commit directly to a fork wiki → Open an unlinked Discussion post → Archive the repository
- **C.** Write `Mentioning #42` in a commit on a non-default experimental branch → Never open a Pull Request → Delete the feature branch → Expect Issue `#42` to close automatically
- **D.** Create a secret Gist with `Fixes #42` → Star the repository → Watch releases only → Expect Gist save to close Issue `#42`

### 48. A release manager audits traceability between Sprint 14 Pull Requests and Issues. Which two methods create formal close-on-merge links between a Pull Request and up to 10 Issues? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch
- **C.** Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 49. When authoring a YAML **Issue Form** (`.github/ISSUE_TEMPLATE/feature_request.yml`), which top-level key (`____: ["enhancement", "needs-triage"]`) automatically applies repository labels to every Issue created from that form?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** `.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists
- **C.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 50. A release manager wants to see every open Issue in `orbit-api` scheduled for Milestone `"v4.2 Release"` that carries label `"sev:1"`. Which search bar query matches this: `is:open is:issue ____:"v4.2 Release" label:"sev:1"`?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 51. What is the **default** repository Watch state for repositories you have **not** manually changed in an organization (`ensuring you get notified only when you comment, open an item, are assigned, or are @mentioned`)?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 52. In GitHub's web Notifications inbox (`github.com/notifications`), how can a TPM create a custom sidebar filter tab showing **only** notifications mentioning `@orbit/release-ops` or `reason:assign`?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 53. Which notification channel option in `Settings -> Notifications` controls whether Dependabot vulnerability alerts reach you via **Web**, **Email**, and **CLI** (`gh`)?

- **A.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 54. A release-ops team publishes public release documentation sites and hosts Q&A threads for integrators. Which two GitHub features handle static site hosting and community Q&A natively? Select two.

- **A.** Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll

### 55. For a repository `orbit-sdk` owned by organization `orbitpulse` (`without a custom domain configured`), what default URL structure does **GitHub Pages** publish a Project Pages site to?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains

### 56. By default on a public repository with **Wikis** enabled, if maintainers want **only** repository collaborators (`Write+`) to edit Wiki pages rather than any signed-in GitHub user, which checkbox in `Settings -> Features -> Wikis` must be enabled?

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

---

## Domain 4 — Apply modern development practices (10–15% official weight · 14 questions)

### 57. Release engineering sets up an automated Playwright smoke-test workflow in **GitHub Actions** on `orbit-web`. Which four-step workflow applies?

- **A.** Open `github.dev` with `.` key → Run `npm test` directly inside `github.dev` browser tab → Save output in a Wiki page → Expect automatic status checks on Pull Requests
- **B.** Create `.github/workflows/ci.yml` → Define `on: [push, pull_request]` triggers → Configure `jobs` with `runs-on: ubuntu-latest` and test `steps` → Commit `ci.yml` and inspect logs in the `Actions` tab
- **C.** Create an Issue template in `.github/ISSUE_TEMPLATE/` → Assign `@copilot` to a Milestone → Star the repository → Expect Issue templates to execute unit tests on Linux runners
- **D.** Place `ci.yml` inside `docs/workflows/` → Omit `on:` triggers and `runs-on:` runner labels → Save as a personal Gist → Expect repository Pull Requests to run CI automatically

### 58. A TPM asks why **GitHub Actions** can automate non-CI project tasks too (such as labeling stale Issues on `issues:` events or generating release notes on `release: [published]`). Which two core elements make this work? Select two.

- **A.** Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 59. Where can a maintainer add a live green **`passing`** / **`failing`** CI status badge image in `README.md` generated directly from a GitHub Actions workflow?

- **A.** **GitHub Actions** hierarchy: **Workflow** (`.github/workflows/*.yml`) triggered by **Events** (`push`, `pull_request`), running **Jobs** on **Runners** (`runs-on`) with ordered **Steps** (`uses:` / `run:`)
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically

### 60. During sprint grooming, squads identify well-scoped tech-debt Issues suitable for AI acceleration alongside complex local refactors. Which three **GitHub Copilot** capabilities support both modes? Select three.

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio
- **C.** **Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request
- **D.** **Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **F.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 61. When **Copilot coding agent** finishes working on an assigned Issue and opens a draft Pull Request, can Copilot coding agent **approve and merge its own Pull Request** into a protected `main` branch without human review?

- **A.** **Copilot coding agent** works asynchronously on assigned GitHub Issues in an Actions sandbox to open draft PRs, whereas **IDE Agent Mode** edits local files and runs local terminal tasks autonomously
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 62. On `github.com` (with **Copilot**), when opening a large Pull Request description, which built-in AI button writes an instant bulleted summary of changed files and affected modules (`Copilot ____`)?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`

### 63. A startup with 25 engineers on **GitHub Team** wants centralized Copilot billing, seat assignment/revocation when contractors roll off, and admin policy management—without upgrading to GitHub Enterprise Cloud. Which plan fits?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **D.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)

### 64. How are AI model requests metered across **GitHub Copilot Business** (`1,900` included credits/seat/mo) and **Copilot Enterprise** (`3,900` included credits/seat/mo) when developers invoke premium models or cloud agents?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 65. In **GitHub Copilot Chat**, what does choosing **`Auto`** in the model selector do instead of pinning one fixed model manually?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** **Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 66. A product manager wants to preview a frontend Pull Request live in a browser (`npm run dev` on port `5173`) **without** installing Node.js, Git, or VS Code on their MacBook Air. Which one-button feature on the Pull Request `Code` dropdown spins up a cloud container running that exact PR branch?

- **A.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets

### 67. What is the difference between **stopping** a GitHub Codespace (`idle timeout`) and **deleting** a GitHub Codespace (`retention period`)?

- **A.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **D.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`

### 68. In `.devcontainer/devcontainer.json`, which array property (`"____": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode"]` under `customizations.vscode`) installs required VS Code extensions automatically for every contributor?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 69. A release manager fixes two typos across `CHANGELOG.md` and `docs/upgrade.md` in one commit, while an engineer debugs a failing Docker microservice. Which two environments match these tasks? Select two.

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** **`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal
- **E.** **GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding

### 70. A QA engineer wants to run `npx playwright test` in a headless Chromium browser against `orbit-web` without installing anything locally. Proposed solution: Open `orbit-web` in **`github.dev`** (`by pressing .`) and run `npx playwright test` inside `github.dev`. Does the solution execute Playwright tests?

- **A.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

---

## Domain 5 — Manage projects with GitHub (5–10% official weight · 8 questions)

### 71. An agile PMO replaces external spreadsheet trackers with **GitHub Projects** across 14 squads. Which two core capabilities let squads run daily standups and leadership review quarterly roadmaps off the exact same live data? Select two.

- **A.** Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **E.** Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields

### 72. In a **GitHub Project `Board`** view, which configuration setting sets a **column limit** (`e.g., max 5 items in In Progress`) to highlight Kanban work-in-progress (`WIP`) bottlenecks visually?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account
- **C.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **D.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields

### 73. A release train engineer configures a new multi-repository **GitHub Project** for two-week sprints, auto-closed cards, and burn-up reporting. Which four-step sequence applies?

- **A.** Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts
- **B.** Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts
- **C.** Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache
- **D.** Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards

### 74. How does a **Repository Milestone** differ in scope from an **Organization GitHub Project**?

- **A.** **Labels** categorize Issues/PRs (`bug`, `priority:high`), **Milestones** track completion percentage toward a repository release target date, and **Project built-in workflows** auto-update `Status` when items close or PRs merge
- **B.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 75. A new scrum master wants to assign Issue `#88` to 25 people simultaneously so the whole department gets credit. Proposed solution: Add all 25 individual usernames into the `Assignees` field of Issue `#88`. Does GitHub allow 25 Assignees on one Issue?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 76. Inside an Issue or Pull Request comment box, pressing `Ctrl + .` (or selecting the reply arrow icon / `/` menu) inserts what reusable personal content?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 77. In **GitHub Projects -> Insights**, can you apply search filter queries (`e.g., iteration:@current -label:chore`) directly onto a custom chart so chore tasks are excluded from feature velocity metrics?

- **A.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)

### 78. If an organization consistently sets up the same 6 views, 5 custom fields (`Priority`, `Size`, `Iteration`, `Target Release`, `Risk`), and built-in workflows for every new product launch, how can admins avoid rebuilding Projects from scratch?

- **A.** Project custom fields (`Single select`, `Number`, `Date`, `Text`, and **`Iteration`** sprints with automatic break capacities) plus filter/sort/group view configurations (`slice by`)
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

---

## Domain 6 — Understand privacy, security, and administration (10–15% official weight · 14 questions)

### 79. A release manager secures their GitHub account with two-factor authentication (`2FA`), offline backup recovery codes, and a synced passkey. Which four-step sequence applies?

- **A.** Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility
- **B.** Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in
- **C.** Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes
- **D.** Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication

### 80. Which two authentication safeguards ensure phishing-resistant daily login AND emergency self-service recovery if a hardware device is lost? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **E.** Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout

### 81. When generating a **Personal Access Token (`PAT`)** for a release script that only needs `Contents: Read-only` on **one** repository (`orbit-web`) for 30 days, why should you choose a **Fine-grained PAT** over a **PAT (classic)**?

- **A.** **Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 82. Customer-support specialists at `OrbitPulse` escalate confirmed customer bugs into engineering repositories, apply severity labels, and close duplicate Issues—and must **never** push branches or merge code. Which repository role should `@orbit/support-tier2` receive?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)

### 83. Which repository role is the **minimum** role allowed to delete a repository, transfer it to another owner, manage collaborator access, or edit repository security settings?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 84. If an Organization Member belongs to Team A (`Read` on `orbit-api`) **and** Team B (`Write` on `orbit-api`), which effective permission does that member receive on `orbit-api`?

- **A.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **B.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 85. An enterprise release-ops VP standardizes identity via Entra ID and rolls out GitHub Copilot across 18 squads. Which two enterprise controls lock down user accounts and AI agent policies? Select two.

- **A.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists
- **E.** Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability

### 86. If your GitHub Enterprise uses **OIDC SSO** with **Enterprise Managed Users (`EMUs`)** backed by Microsoft Entra ID, whose **Conditional Access Policies (`CAP`)** (such as device compliance and IP restrictions) does GitHub validate automatically?

- **A.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 87. An organization owner enables **Copilot coding agent** at the organization level, yet wants to prevent Copilot coding agent from running on one ultra-sensitive `merger-acquisitions` repository. Is per-repository opt-out supported?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions

### 88. Release managers configure a **Repository Ruleset** protecting `release/*` and `main` branches. Which three rules guarantee auditability and build quality? Select three.

- **A.** Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **F.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`

### 89. A contributor gets 1 approval on their Pull Request, then pushes a brand-new commit modifying 300 lines right before hitting Merge. Which branch protection / ruleset option automatically invalidates prior approvals whenever new code is pushed: **`Dismiss ____ pull request approvals when new commits are pushed`**?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 90. A release lead commits `.github/CODEOWNERS` listing `* @orbit/release-ops` on `orbit-api`, yet leaves `main` without any branch protection rule or Repository Ruleset. Proposed solution: Rely on committing `.github/CODEOWNERS` alone without enabling `Require a pull request before merging` + `Require review from Code Owners` on `main`. Does the solution block unapproved merges?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 91. Who inside a non-Owner GitHub Team can add/remove members from that specific Team and update the Team's description or review auto-assignment settings without holding `Organization Owner`?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 92. In `Organization Settings -> Member privileges`, if an Organization Owner unchecks `Allow members to create public repositories`, what risk does that immediately eliminate?

- **A.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

---

## Domain 7 — Explore the GitHub community (5–10% official weight · 8 questions)

### 93. On **GitHub Sponsors**, can a sponsor choose between a **recurring monthly** sponsorship tier and a **one-time** sponsorship contribution (with optional private vs public attribution)?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 94. Which two standard GitHub Issue labels are indexed globally across GitHub (`and highlighted on a repo's Contribute landing page github.com/<owner>/<repo>/contribute`) to match newcomers with approachable open-source Issues?

- **A.** GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 95. When you **Follow** a developer on GitHub, do they gain read access to your **private** repositories, or do you merely subscribe to their **public** activity in your dashboard feed?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 96. Inside `.github/workflows/release.yml`, when reusing a community **GitHub Action** discovered on **GitHub Marketplace** (`uses: softprops/action-gh-release@____`), what pinning practice protects supply-chain security best?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts

### 97. An agile enterprise adopts **InnerSource** for its internal mobile UI kit so 14 squads can contribute missing components instead of blocking on one central team. Which two practices make this succeed? Select two.

- **A.** Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **E.** Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**

### 98. Even though all **`Internal`** repositories inside a corporate GitHub Enterprise belong to the same legal company, why do mature **InnerSource** programs still include a `CONTRIBUTING.md` and explicit internal usage expectations in every shared repo?

- **A.** **InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 99. A release engineer contributes a changelog parser fix to an external open-source repository where they do not hold write access. Which four-step workflow applies?

- **A.** Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream
- **B.** Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge
- **C.** Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights
- **D.** Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor

### 100. A developer wants to start a proprietary internal commercial SaaS application using a public MIT-licensed template boilerplate (`mit-nextjs-starter`) and **never** merge upstream changes or expose their repo in the public fork network. Proposed solution: Select **`Use this template`** to generate a clean `Private` repository (retaining the required MIT copyright notice). Does the solution work?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

---

## Answer Key and Explanations

### Question 1 — `C, E` (Understand Git and GitHub basics)

Correct answers: C and E (are correct). Distributed clones retain full commit and tag history locally, and signed/attributed commits let release managers audit every change (`git blame`/`git log`) and run clean `git revert` rollbacks. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Commit metadata provides line-by-line accountability and clean rollback via `git revert`.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.

### Question 2 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Creating an annotated **Git tag** (`git tag -a v2.5.0`) pins an immutable version label to a specific release commit (`used by GitHub Releases`). [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.

### Question 3 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Git tracks base parent commits and rejects non-fast-forward pushes (`fetch first`), requiring explicit merge/rebase integration if a teammate pushed newer changes first. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.

### Question 4 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). `git bisect` binary-searches commit history (`O(log N)` steps) between a good commit and a bad commit to pinpoint the exact commit that introduced a regression. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 5 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). No — `git` manages local/distributed commits, branches, merges, and tags; **GitHub Projects**, **Milestones**, **Issues**, and **Pull Request** governance are **GitHub** platform features. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.

### Question 6 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Running `git init` creates the hidden `.git` metadata directory locally, turning an ordinary folder into a version-controlled Git repository. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 7 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Yes — linking a local Git repository to a newly created empty GitHub remote via `git remote add origin` and `git push` transfers the entire local commit history intact. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **B:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.

### Question 8 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Every GitHub Release is anchored to a **Git tag** (`e.g., v3.0.0`) pointing to a specific commit SHA in the repository. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 9 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Edit `CHANGELOG.md` in the working directory, stage it via `git add`, record a snapshot locally via `git commit -m`, and upload to GitHub via `git push`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).
- **B:** Incorrect. Committing before editing and staging captures nothing from the intended file modifications.
- **C:** Incorrect. `git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.
- **D:** Incorrect. Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.

### Question 10 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git add -p` (`--patch`) lets developers review and stage individual change hunks interactively for clean, atomic commits. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Correct. Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 11 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Clear commit messages power readable `git log` history, Pull Request timelines, `git blame` context, and automated GitHub Release changelog generation. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **D:** Correct. Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.

### Question 12 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Lowercase `git branch -d <branch>` safely deletes a local branch only after verifying its commits are merged (whereas `-D` force-deletes unmerged branches). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Git branches are lightweight commit pointers rather than full folder copies, letting teams develop features safely without destabilizing `main`.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 13 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `git stash` (`and git stash pop`) shelves uncommitted tracked changes cleanly so you can switch branches and re-apply your work afterward. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.

### Question 14 — `B, D` (Understand Git and GitHub basics)

Correct answers: B and D (are correct). Use **GitHub Organizations** for shared repositories, Teams, and repository roles, unified under one **GitHub Enterprise** account for multi-org SSO, billing, and policies. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Correct. Organizations centralize multi-developer ownership and team-based RBAC.
- **C:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **D:** Correct. Enterprise accounts unify security, identity, and policy governance across multiple organizations.
- **E:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.

### Question 15 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Protected branches, `CODEOWNERS`, required/multiple PR reviewers, Draft PRs, Pages, Wikis, and custom **GitHub Projects Insights charts** unlock for private repositories on GitHub Team! [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.

### Question 16 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). The **Enterprise Audit Log** (`Settings -> Audit log`, streamable to SIEMs on GitHub Enterprise) records administrative, permission, and policy actions across all member organizations. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.

### Question 17 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). They immediately lose access to `@employer-a`'s private/internal repositories and org resources while keeping their personal GitHub account and public open-source profile intact. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **D:** Correct. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 18 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Create a descriptive branch from `main`, commit changes and open a Pull Request, complete peer review and automated status checks, then merge into `main` and delete the feature branch. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.
- **B:** Correct. GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.
- **C:** Incorrect. Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.
- **D:** Incorrect. GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.

### Question 19 — `B, E` (Understand Git and GitHub basics)

Correct answers: B and E (are correct). Isolate every change on a small, short-lived branch off `main`, and validate every change via Pull Request peer review plus automated CI checks before merging. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Correct. Pull Requests combine asynchronous peer review and automated CI verification prior to merging.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.

### Question 20 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Yes — selecting **`Convert to draft`** under the Reviewers sidebar transitions an open Pull Request back to Draft state until marked `Ready for review` again! [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 21 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Lines between `<<<<<<< feature/promo` and `=======` come from your feature branch, while lines between `=======` and `>>>>>>> main` come from `main`. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Correct. When two branches modify the same lines differently, Git inserts standard conflict markers that must be edited out, staged, and committed (or resolved in GitHub’s web conflict editor).
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 22 — `A, D, F` (Understand Git and GitHub basics)

Correct answers: A, D, and F (are correct). `- [ ]` / `- [x]` task checkboxes, `> [!IMPORTANT]` / `> [!NOTE]` callout alerts, and ```` ```mermaid ```` diagram blocks. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.
- **E:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **F:** Correct. Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.

### Question 23 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). The five supported GFM alert types are **`NOTE`**, **`TIP`**, **`IMPORTANT`**, **`WARNING`**, and **`CAUTION`**. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Correct. GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.

### Question 24 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Starting a line with `>` (`greater-than` symbol, or highlighting text and pressing `r` in an Issue/PR thread to quote-reply!) formats a Markdown blockquote. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 25 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Wrap the inline code span in **double backticks** with spaces (` `` `hello` `` `), or use triple-backtick/tilde (`~~~`) fenced blocks for multi-line snippets containing triple backticks! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 26 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). **GitHub Desktop** guides Windows and macOS users visually through cloning, branching, diff previewing, committing, pushing, and opening Pull Requests. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **B:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.

### Question 27 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). **GitHub Mobile** (`iOS`/`Android`) lets PMs and engineers browse Issues, Projects, Pull Requests, Discussions, and Notifications from their phone or tablet. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **B:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.

### Question 28 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Yes — GitHub Mobile mirrors GitHub's notification inbox filters and supports customizable swipe gestures for fast mobile triage. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 29 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Add `.github/CODEOWNERS` mapping those paths to `@orbit/release-ops`, merge `CODEOWNERS` into `main`, enable branch protection/rulesets requiring PR reviews, and enable `Require review from Code Owners`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.
- **B:** Incorrect. `README.md` does not trigger automatic review requests or merge enforcement.
- **C:** Correct. `CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.
- **D:** Incorrect. GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.

### Question 30 — `B, C` (Work with GitHub repositories)

Correct answers: B and C (are correct). GitHub highlights `CODEOWNERS` syntax/permission errors directly in the editor/PR banner; valid files must sit in `.github/`, root, or `docs/` and pair with branch protection/rulesets requiring Code Owner review. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Correct. GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.
- **C:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **E:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 31 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). GitHub treats `<username>/<username>` as a special **Profile README** repository and renders its `README.md` prominently at the top of your personal GitHub profile page! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **C:** Correct. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 32 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). `CODE_OF_CONDUCT.md` defines respectful community behavior standards and harassment enforcement reporting, whereas `CONTRIBUTING.md` explains technical setup, testing, branching, and PR steps. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Correct. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 33 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Configure `quarterly-launch-playbook` as a **Template repository** so each quarter's launch repo starts from a clean initial commit via `Use this template`. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Incorrect. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.

### Question 34 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). GitHub classifies branches with commits in the last 3 months as `Active` and branches untouched for over **3 months** as `Stale` so maintainers can prune abandoned branches safely. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Correct. Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 35 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). No — `.gitignore` ignores only untracked paths; already-committed files remain tracked until removed from the index with `git rm --cached` and committed. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `.gitignore` ignores only untracked paths; already-committed files remain tracked until removed from the index with `git rm --cached` and committed.
- **B:** Correct. `.gitignore` has no effect on files already tracked in the Git index; you must untrack via `git rm --cached` and immediately rotate exposed secrets.
- **C:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 36 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Pressing **`y`** on any file view on GitHub.com updates the browser URL to the exact canonical commit SHA (`/blob/8a3f9c.../...#L45-L60`), creating a permanent permalink! [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 37 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). No — deleting a file via a normal commit only omits it from the **new** commit onward; prior versions remain recoverable in Git commit history (purging leaked data from history requires history rewrite + support/secret rotation). [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.

### Question 38 — `B, C` (Work with GitHub repositories)

Correct answers: B and C (are correct). Enable the **Dependency graph** and enable **Dependabot alerts + Dependabot security/version updates**. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Correct. Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.
- **C:** Correct. The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.
- **D:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **E:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 39 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). `Insights -> Network` renders an interactive commit/branch topology graph across the root repository and its fork network. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 40 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). GitHub users can organize Starred repositories into up to **32** custom Lists (`public` Lists on your Stars tab). [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **B:** Incorrect. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 41 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Yes — updating `README.md` with migration guidance right before **Archiving** preserves every historical Issue/PR permalink while making the repository read-only. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **B:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.

### Question 42 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). It keeps `git log main` concise (one atomic commit per feature/fix) and prevents hundreds of dead topic branches from cluttering branch selectors and local `git fetch` refs. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.

### Question 43 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). The **`Polls`** category inside **GitHub Discussions** lets maintainers run structured community/team polls right alongside the repository. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Incorrect. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **C:** Correct. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 44 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Select **`Convert to discussion`** in the Issue sidebar, which moves `#312` cleanly into the chosen Discussions category while redirecting the original Issue URL! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **D:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).

### Question 45 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Marking files **`Viewed`** collapses reviewed files and tracks your personal progress (`e.g., 14 / 20 files viewed` — automatically unchecking only files modified by subsequent commits!). [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 46 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Select **`Transfer issue`** in the right sidebar to transfer the Issue seamlessly to another repository within the same Organization! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 47 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Triage Issue `#42` with labels/milestone/assignee, commit the fix on a topic branch, open a Pull Request referencing `Fixes #42` targeting `main`, and merge the approved PR into `main`. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. Including a closing keyword (`Closes #42`, `Fixes #42`, `Resolves #42`) in a Pull Request targeting the default branch automatically closes Issue `#42` upon merge.
- **B:** Incorrect. Closing the issue prematurely loses active tracking, and wiki edits or Discussions do not merge code changes.
- **C:** Incorrect. Only supported closing keywords merged into the default branch (or explicitly linked PRs) close an issue automatically.
- **D:** Incorrect. Gists are separate repositories and cannot auto-close repository Issues via closing keywords.

### Question 48 — `B, C` (Collaborate using GitHub)

Correct answers: B and C (are correct). Include supported closing keywords (`Closes #10, Fixes #11`) in the PR description targeting `main`, or link Issues manually in the PR's **`Development`** sidebar. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Correct. Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.
- **C:** Correct. Manual `Development` sidebar links work across branches and display clear traceability on both timelines.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 49 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). The `labels:` (and optional `assignees:` / `projects:`) property in a YAML Issue Form attaches triage metadata automatically upon submission. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.
- **C:** Incorrect. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 50 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Using `milestone:"v4.2 Release"` (with quotes around multi-word names) filters Issues and Pull Requests belonging to that exact Milestone. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Correct. GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 51 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). **`Participating and @mentions`** is GitHub's default notification subscription level, preventing notification overload until you engage with a thread or opt into `All Activity`/`Custom`. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 52 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Use **`Custom filters` -> `Create new filter`** in the Notifications sidebar (`e.g., reason:team-mention OR reason:assign`) to save reusable one-tap inbox views! [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 53 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Under `Settings -> Notifications -> System -> Dependabot alerts`, users configure Web, Email, and command-line alert preferences for vulnerable dependencies. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 54 — `A, E` (Collaborate using GitHub)

Correct answers: A and E (are correct). **GitHub Pages** hosts the static documentation site over HTTPS, and **GitHub Discussions** hosts categorized community Q&A with accepted answers. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Correct. Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. GitHub Pages renders repository docs into browsable websites with HTTPS.

### Question 55 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). GitHub Pages publishes Project sites at `https://<owner>.github.io/<repository>/` (`https://orbitpulse.github.io/orbit-sdk/`), whereas an organization root site repo named `orbitpulse.github.io` publishes at `https://orbitpulse.github.io/`. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).

### Question 56 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Keep **`Restrict editing to collaborators only`** checked so external users can read Wiki documentation without modifying pages unreviewed! [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Correct. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 57 — `B` (Apply modern development practices)

Correct answer: B (is correct). Create `.github/workflows/ci.yml`, define `on: [push, pull_request]`, configure `jobs` with `runs-on: ubuntu-latest` and test `steps`, and commit `ci.yml` to inspect run logs in `Actions`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. `github.dev` has no compute terminal to execute `npm test` or report Pull Request status checks.
- **B:** Correct. GitHub Actions workflows live as YAML files in `.github/workflows/`, trigger on defined events, execute job steps on specified runners, and report status in the `Actions` tab.
- **C:** Incorrect. Issue templates structure bug reports and never provision Actions runners or run unit tests.
- **D:** Incorrect. Workflow YAML files outside `.github/workflows/` are ignored by GitHub Actions, and `on:` plus `runs-on:` are required keys.

### Question 58 — `A, D` (Apply modern development practices)

Correct answers: A and D (are correct). YAML workflows in `.github/workflows/` subscribe to any GitHub webhook `on:` event (`issues`, `pull_request`, `release`, `schedule`) and run `jobs:`/`steps:` on `runs-on:` runners. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Correct. GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 59 — `A` (Apply modern development practices)

Correct answer: A (is correct). Open the workflow in the **`Actions`** tab, open the `...` menu -> **`Create status badge`**, and copy the generated Markdown badge snippet into `README.md`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. In GitHub Actions, jobs run in parallel by default on fresh virtual runner machines (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) unless ordered via `needs:`.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).

### Question 60 — `B, C, D` (Apply modern development practices)

Correct answers: B, C, and D (are correct). Assigning Issues to **Copilot coding agent** for background draft PRs, using **IDE Agent Mode** for multi-file local refactors, and picking optimal LLMs via **multi-model support**. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Correct. IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.
- **C:** Correct. Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.
- **D:** Correct. Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **F:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 61 — `A` (Apply modern development practices)

Correct answer: A (is correct). No — Copilot coding agent opens a **draft Pull Request** with transparent commit/session logs so a human developer with write/review rights inspects, iterates, approves, and merges the PR! [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. The January 2026 GH-900 blueprint distinguishes asynchronous **Copilot coding agent** on GitHub (assigned to Issues, opening PRs) from synchronous local **Agent Mode** inside your IDE, plus **MCP** servers and custom agents.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 62 — `D` (Apply modern development practices)

Correct answer: D (is correct). **Copilot Pull Request summaries** (`Summary` inside the PR description toolbar) analyze the branch diff and generate structured reviewer context automatically. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Correct. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.

### Question 63 — `C` (Apply modern development practices)

Correct answer: C (is correct). **GitHub Copilot Business** supports organizations on GitHub Free/Team with full seat management, policy controls, and IP indemnity. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **D:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.

### Question 64 — `B` (Apply modern development practices)

Correct answer: B (is correct). Each seat contributes to a shared monthly pool of **GitHub AI credits** (with model-dependent token/credit rates, plus optional metered overage billing if enabled by admins). [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 65 — `C` (Apply modern development practices)

Correct answer: C (is correct). **Auto model selection** automatically picks an appropriate available model balancing response speed, capability, and availability for your prompt. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Correct. Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 66 — `D` (Apply modern development practices)

Correct answer: D (is correct). Launching a **GitHub Codespace** directly on the Pull Request branch boots the configured `.devcontainer/devcontainer.json` environment and forwards port `5173` over HTTPS in the browser! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.

### Question 67 — `C` (Apply modern development practices)

Correct answer: C (is correct). Stopping suspends vCPU compute billing while preserving uncommitted files/containers on storage; deleting removes the Codespace and all uncommitted local changes permanently. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **D:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).

### Question 68 — `B` (Apply modern development practices)

Correct answer: B (is correct). `customizations.vscode.extensions` pre-installs exact VS Code extensions inside every Codespace built from that repository. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 69 — `D, E` (Apply modern development practices)

Correct answers: D and E (are correct). Open **`github.dev`** (`press .`) for instant zero-cost multi-file Markdown editing in the browser, and launch **GitHub Codespaces** for full cloud VM container debugging. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Correct. `github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.
- **E:** Correct. Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.

### Question 70 — `B` (Apply modern development practices)

Correct answer: B (is correct). No — `github.dev` runs purely in the client browser with zero compute VM or terminal runtime; use **GitHub Codespaces** or **GitHub Actions** to execute `npx playwright test`! [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **B:** Correct. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `github.dev` runs purely in the client browser with zero compute VM or terminal runtime; use **GitHub Codespaces** or **GitHub Actions** to execute `npx playwright test`!
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 71 — `A, E` (Manage projects with GitHub)

Correct answers: A and E (are correct). Configure `Table`, `Board`, and `Roadmap` views backed by live `Iteration`/`Date` custom fields, and enable **Project workflows** plus **Project Insights** charts. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Correct. Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **E:** Correct. GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.

### Question 72 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Setting a **Column limit** on any Board status column displays an visual indicator whenever item count exceeds your team's WIP cap! [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.
- **C:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **D:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.

### Question 73 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Create the organization Project with custom `Iteration` and `Priority` fields, link repository Issues/PRs, enable built-in `Item closed -> Done` workflows, and track burn-up in Project Insights. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. `SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.
- **B:** Correct. GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.
- **C:** Incorrect. Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.
- **D:** Incorrect. Gists do not host Milestones or drive organization GitHub Projects automations.

### Question 74 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). A **Milestone** is scoped to a **single repository** (`tracking open/closed % toward one repo release`), whereas an **Organization GitHub Project** spans Issues and PRs across **many repositories** with custom fields and multiple views. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Correct. Labels classify type/priority, Milestones measure progress toward a release goal inside a repository, and built-in Project workflows eliminate manual card dragging.
- **B:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 75 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). No — GitHub caps **`Assignees`** at a maximum of **10** users per Issue or Pull Request (mention `@org/department-team` in a comment if broadcasting to 25 people!). [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — GitHub caps **`Assignees`** at a maximum of **10** users per Issue or Pull Request (mention `@org/department-team` in a comment if broadcasting to 25 people!).
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Correct. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 76 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Your configured **Saved replies**, accelerating repetitive triage and review communication with consistent Markdown formatting. [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 77 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Yes — every custom chart in **Project Insights** supports its own filter bar query (`iteration:@current`, `assignee:`, `-label:`) saved with that chart! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.

### Question 78 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Mark a configured GitHub Project as a **Project template** inside the Organization so teams spin up pre-configured Projects (`views`, `custom fields`, `workflows`, and `insights` included) in seconds! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Correct. `Iteration` fields track time-boxed sprints directly inside GitHub Projects without external agile plugins.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 79 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). Release managers harden accounts by turning on `2FA` first, saving one-time recovery codes in an encrypted vault, adding a synced passkey in Security settings, and testing passkey sign-in. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.
- **B:** Correct. Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.
- **C:** Incorrect. Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.
- **D:** Incorrect. GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.

### Question 80 — `C, E` (Understand privacy, security, and administration)

Correct answers: C and E (are correct). Register WebAuthn/FIDO2 **Passkeys** for phishing-resistant login, and store downloaded one-time **`2FA` recovery codes** in an encrypted vault. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **E:** Correct. Recovery codes are essential to regain account access if a phone or hardware key is lost.

### Question 81 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). Fine-grained PATs scope permissions down to **specific repositories**, **minimum resource permissions**, mandatory **expiration dates**, and optional organization admin approval—unlike broad `repo`-scoped classic PATs! [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Correct. Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 82 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Grant the **`Triage`** repository role (`manage Issues and PR metadata without code push access`). [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.

### Question 83 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Only the **`Admin`** repository role (or an `Organization Owner`) can perform destructive actions like deleting/transferring a repository or changing collaborator permissions. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 84 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). GitHub repository roles are additive (**most permissive wins**): combining `Read` and `Write` grants effective **`Write`** access on `orbit-api`. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **B:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 85 — `D, E` (Understand privacy, security, and administration)

Correct answers: D and E (are correct). Enforce **Enterprise Managed Users (`EMUs`)** provisioned via Entra ID OIDC/SAML + SCIM, and manage **organization/enterprise Copilot policies** over models, seats, public-code blocking, and agents. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Correct. EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.
- **E:** Correct. Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.

### Question 86 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). GitHub validates your corporate IdP's **Conditional Access Policies (`CAP`)** during OIDC authentication and session refresh! [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **B:** Correct. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 87 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Yes — organization owners and repository admins can **opt out** specific repositories from Copilot coding agent even when the agent is enabled for the organization. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.

### Question 88 — `A, C, F` (Understand privacy, security, and administration)

Correct answers: A, C, and F (are correct). Require Pull Requests with approvals + **Code Owner** review, require passing **status checks**, and block **force-pushes** plus branch deletions. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. Blocking force-pushes and deletions protects commit history integrity on production branches.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Correct. Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **F:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.

### Question 89 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Enabling **`Dismiss stale pull request approvals when new commits are pushed`** ensures newly pushed commits cannot piggyback on an earlier approval unreviewed! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 90 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). No — `CODEOWNERS` only auto-requests reviewers until paired with branch protection or a Repository Ruleset requiring Code Owner review on `main`! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Correct. `CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `CODEOWNERS` only auto-requests reviewers until paired with branch protection or a Repository Ruleset requiring Code Owner review on `main`!
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 91 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Users granted the **`Team maintainer`** role on that specific Team can manage its membership, child teams, and review settings under least privilege. [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 92 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). It prevents employees from accidentally creating a new `Public` internet-exposed repository inside the corporate GitHub Organization! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **B:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 93 — `B` (Explore the GitHub community)

Correct answer: B (is correct). Yes — GitHub Sponsors supports both recurring monthly tiers and one-time sponsorships, and lets sponsors choose whether their sponsorship appears publicly or stays private. [Skill 7.1: Describe the benefits of open source and GitHub Sponsors | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Sponsors and open-source sustainability (https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 94 — `A` (Explore the GitHub community)

Correct answer: A (is correct). **`good first issue`** (for first-time contributors) and **`help wanted`** (for issues where maintainers actively welcome external Pull Requests). [Skill 7.2: Explain how GitHub supports and advances open-source projects | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Supporting open-source projects with community profiles and Security Lab / advisories (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)]

- **A:** Correct. GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 95 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Following is purely a public activity-feed subscription—followed users gain **zero** permissions on your private repositories! [Skill 7.3: Identify how to follow users and organizations to stay informed about activity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Following people and organizations on GitHub to track activity (https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)]

- **A:** Correct. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 96 — `D` (Explore the GitHub community)

Correct answer: D (is correct). Pin third-party Marketplace Actions to a full **40-character commit SHA** (or verified immutable version tag from a trusted creator) so upstream tag mutations cannot inject malicious code! [Skill 7.4: Describe the GitHub Marketplace and its purpose | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Marketplace for GitHub Apps and Actions (https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.

### Question 97 — `A, E` (Explore the GitHub community)

Correct answers: A and E (are correct). Configure the UI kit as an **`Internal`** repository with `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS`, and apply **Repository Topics** while welcoming cross-team Pull Requests. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. `Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **E:** Correct. Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.

### Question 98 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Clear `CONTRIBUTING.md` docs specify test coverage bars, SLA expectations (`whether the owning team supports 24/7 pager alerts vs community effort`), and PR conventions across teams. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 99 — `A` (Explore the GitHub community)

Correct answer: A (is correct). To submit a changelog parser fix externally, check `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` first, fork the repo and create a topic branch, push commits to your fork, and open a Pull Request against upstream. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Correct. External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.
- **B:** Incorrect. Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.
- **C:** Incorrect. Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.
- **D:** Incorrect. Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.

### Question 100 — `C` (Explore the GitHub community)

Correct answer: C (is correct). Yes — generating a repository from a **Template** creates a brand-new standalone `Private` repository with clean 1-commit history outside the public fork network. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
