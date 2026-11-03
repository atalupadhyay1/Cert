# Microsoft Exam GH-900: GitHub Foundations — Full-Length Mock Exam 2

**Theme:** Design, Documentation & Developer Advocacy — GFM Markdown, GitHub Desktop/Mobile, Wikis/Gists/Pages, github.dev, Saved Replies & Sponsors  
**Credential:** `Microsoft Certified: GitHub Foundations` *(Beginner / Fundamentals · **no prerequisite** · **does not require renewal / never expires**)*  
**Study guide baseline:** `January 2026 (Last updated February 19, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-900 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Docs documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Understand Git and GitHub basics (25–30% official weight · 28 questions)

### 1. A technical writing team at `PrismDocs` moves 600 Markdown guides out of emailed Word attachments into Git. Which two version-control capabilities improve their daily publishing workflow? Select two.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Every developer clone contains the full commit history and branches, enabling offline commits and history inspection
- **D.** Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely
- **E.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 2. Why is losing a single developer's laptop (or experiencing a temporary remote outage) non-catastrophic for commit history in a **Distributed Version Control System (`DVCS`)** like Git?

- **A.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 3. Two writers edit different sections of `docs/authentication.md` on separate branches in parallel. What happens when both branches merge into `main` via Git?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 4. Which Git command (`git ____ --oneline --graph`) displays chronological commit history, condensed commit SHAs, branch pointers, and commit messages in your terminal?

- **A.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 5. A UX content strategist installs Git (`git --version`) on Windows yet hasn't created a `github.com` account. Which task can they perform immediately using **Git alone** without GitHub?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 6. When comparing **Git** and **GitHub**, where do **Issues**, **Discussions**, **GitHub Pages**, **Actions runners**, and **CODEOWNERS** review rules live?

- **A.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 7. Which command-line tool (`gh` — `____ pr create`) did GitHub build specifically to interact with GitHub-only features like Pull Requests, Issues, Releases, and Codespaces from a terminal, complementing `git`?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 8. A university lecturer teaches version control in a classroom without campus Wi-Fi. Proposed solution: Have students run `git init`, `git branch`, `git add`, `git commit`, and `git merge` locally on their laptops during class, then `git push` to GitHub later from home. Does the solution work?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — adding `.env` to `.gitignore` only ignores **untracked** files; a file already committed to Git continues being tracked until `git rm --cached .env` removes it from the index (and any leaked secret is rotated!).
- **C.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 9. A developer advocate updates `examples/quickstart.py` locally and wants those changes committed and pushed to `origin/main` (on an unguarded demo repo). Which four-step Git sequence applies?

- **A.** Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`
- **B.** Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`
- **C.** Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`
- **D.** Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`

### 10. Before running `git add` or `git commit`, which Git command (`git ____`) reports which working-directory files are modified, which files are staged for the next commit, and which files are untracked?

- **A.** Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 11. You want to download a complete local working copy of `https://github.com/solstice-ui/icons.git` onto your laptop for the very first time, automatically configuring the `origin` remote. Which Git command (`git ____ https://github.com/solstice-ui/icons.git`) do you run?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link

### 12. In Git terminology, what does the special reference **`HEAD`** ordinarily point to inside your local repository?

- **A.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message

### 13. Which single Git command (`git ____`) combines `git fetch` followed immediately by integrating (`merge` or `rebase`) upstream remote commits into your current local branch?

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`

### 14. A design-systems agency outgrows individual `GitHub Free` accounts and needs team-based permissions now, plus multi-organization SAML SSO and audit logs next quarter. Which two GitHub account layers address these needs? Select two.

- **A.** Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies
- **D.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **E.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 15. A freelance illustrator wants protected branches, Code Owners, Wikis, and GitHub Pages on **private** repositories owned solely by their personal account without creating an Organization. Which individual upgrade plan unlocks these features?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 16. On **GitHub Free for Organizations**, can teams collaborate on unlimited private repositories with basic Issues and Pull Requests, while upgrading to **GitHub Team** unlocks protected branches, Code Owners, and multiple PR reviewers on private repos?

- **A.** Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 17. Which GitHub offering allows a defense contractor with strict data-sovereignty rules to run a self-managed virtual appliance of GitHub inside its own private cloud or on-premises VMware/Azure environment?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **D.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing

### 18. A documentation advocate updates an API tutorial on `beacon-docs` following **GitHub Flow**. Which four-step workflow applies from branch creation through cleanup?

- **A.** Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge
- **B.** Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review
- **C.** Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks
- **D.** Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch

### 19. Why does **GitHub Flow** work smoothly for non-developers (designers, technical writers, product managers) as well as software engineers? Select two.

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`
- **C.** Create a short-lived descriptive branch off `main` so `main` stays deployable at all times
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 20. In **GitHub Flow**, what fundamental guarantee must the default branch (`main`) satisfy at all times?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** GitHub Flow: keep `main` always deployable, branch off `main`, open an early Pull Request for discussion and CI checks, merge after approval, and deploy
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 21. While a Pull Request is still in **Draft** state, are `CODEOWNERS` automatically spammed with review-request notifications immediately, or only after the author marks the Draft PR **`Ready for review`**?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`

### 22. A developer advocate formats a release-readiness Issue on `CanvasKit` using GitHub Flavored Markdown. Which three formatting constructs render interactive or styled elements on GitHub? Select three.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax
- **D.** Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`
- **E.** Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)
- **F.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 23. Which exact GitHub Flavored Markdown blockquote syntax renders a red/orange **`Warning`** callout banner in `README.md`: `> [!____]`?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)

### 24. While typing a long Issue description in GitHub's web Markdown editor, typing which single character (`____`) opens an interactive command menu to insert Markdown **tables**, **code blocks**, **task lists**, or **saved replies** without memorizing syntax?

- **A.** `@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 25. To highlight added lines in green (`+`) and removed lines in red (`-`) inside a Markdown technical post on GitHub, which language identifier do you place after opening triple backticks: ```` ```____ ````?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams
- **C.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 26. A technical writer working locally in **GitHub Desktop** switches from `feat/oauth-guide` to fix an urgent typo on `main` while having uncommitted edits in three files. How does GitHub Desktop handle uncommitted changes during branch switch?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **C.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **D.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution

### 27. Besides reviewing Pull Requests and triaging Issues, how can **GitHub Mobile** strengthen account sign-in security when logging into `github.com` on a new workstation browser?

- **A.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **D.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization

### 28. You are away from your desk with only an Android phone (**GitHub Mobile**) when a customer spots a broken URL in `README.md` on `docs-portal`. Can you edit `README.md`, commit to a new branch, and open a Pull Request directly inside GitHub Mobile?

- **A.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **B.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **C.** **Dependency graph** parses manifest/lockfiles (`package-lock.json`, `requirements.txt`), powering **Dependabot alerts** and Enterprise **Dependency insights** / SBOM export for license and CVE visibility
- **D.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets

---

## Domain 2 — Work with GitHub repositories (10–15% official weight · 14 questions)

### 29. Your documentation lead wants any Pull Request editing `/docs/api/**` in `prism-sdk` to require approval from `@prism/api-writers` before merging. Which four-step sequence enforces this?

- **A.** Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings
- **B.** Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`
- **C.** Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages
- **D.** Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests

### 30. If `.github/CODEOWNERS` contains both `* @prism/general-reviewers` on line 1 and `/docs/security/** @prism/sec-team` on line 10, which two rules determine how GitHub evaluates and enforces `CODEOWNERS`? Select two.

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **E.** Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch

### 31. If a repository accidentally contains `README.md` in **both** `.github/README.md` and the root `/README.md` (plus `docs/README.md`), which `README.md` takes highest precedence on the repository home page?

- **A.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers
- **B.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage

### 32. A compliance team commits `.github/CODEOWNERS` (`* @prism/compliance`) to `main` on a repository that has **zero** branch protection rules or rulesets configured. Proposed solution: Rely on `.github/CODEOWNERS` alone to block developers with `Write` access from merging unapproved Pull Requests into `main`. Does the solution block unapproved merges?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.

### 33. When creating a new repository from a **Template repository** (`Use this template`), what does checking **`Include all branches`** do compared to default template creation?

- **A.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability

### 34. Before renaming a repository's default branch from legacy `master` to `main` in `Settings -> Branches`, what automatically happens on GitHub.com for existing open Pull Requests and GitHub Actions workflows targeting the old default branch?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 35. Windows and macOS writers keep accidentally committing noisy whole-file `CRLF` vs `LF` line-ending diffs across Markdown and shell scripts. Which root repository file (`____`, e.g., `* text=auto eol=lf`) normalizes line endings consistently across all operating systems?

- **A.** `.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 36. A designer tries to `git push` a `145 MB` uncompressed `.psd` asset directly into a GitHub repository and receives `remote: error: File hero.psd is 145.00 MB; this exceeds GitHub's file size limit of 100.00 MB`. Which Git extension (`git ____ track "*.psd"`) tracks large binaries cleanly via pointer files?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **C.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 37. While viewing any file on GitHub.com, pressing which single keyboard shortcut (`____`) activates the interactive **Repository file finder** so you can fuzzy-search and jump to any file path instantly?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 38. A customer procurement team asks your open-source SDK maintainers for a machine-readable **Software Bill of Materials (`SBOM`)** and proactive CVE remediation. Which two GitHub capabilities satisfy these requirements? Select two.

- **A.** Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **E.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 39. Under `Insights -> ____`, repository maintainers with push access can inspect unique visitors, total page views, top referring websites, and total `git clone` counts over the rolling **14-day** window.

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **D.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)

### 40. Where in the GitHub.com user interface can an individual user opt in or opt out of experimental upcoming UI enhancements before they become generally available (`GA`)?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**

### 41. On an Organization's main profile page (`github.com/solstice-ui`), how can maintainers highlight their **top 6 flagship repositories** at the very top of the page with custom ordering for visitors?

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 42. Where can an Organization store a **single default** `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md` once so every repository in the Organization inherits them automatically unless overridden locally?

- **A.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

---

## Domain 3 — Collaborate using GitHub (10–15% official weight · 14 questions)

### 43. A customer reports a reproducible crash when exporting SVG icons with transparent backgrounds, complete with stack trace and expected fix in v2.4.1. Which GitHub collaboration tool is designed for tracking this actionable bug through fix and release?

- **A.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **B.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **C.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 44. When submitting a formal Pull Request review (`Files changed -> Review changes`), which three review verdicts can a reviewer choose from?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)

### 45. Which Pull Request merge strategy replays each individual commit from the feature branch onto the tip of `main` **without** creating a two-parent merge commit, producing a strictly linear commit history?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)

### 46. Which **GitHub Discussions** category format allows community members to upvote candidate replies and lets the original asker or maintainer mark one specific reply as the verified **`Answer`**?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers
- **C.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **D.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**

### 47. A documentation Pull Request fixes broken links reported across two repositories (`Closes prism/docs#88`) and also addresses local Issue `#19`. Which two mechanisms link Pull Requests so target Issues close upon merge into the default branch? Select two.

- **A.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it
- **E.** Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch

### 48. A contributor writes `Related to #54` in a Pull Request body and merges the PR into `main`. Why does Issue `#54` remain **Open** after the merge?

- **A.** Linking PRs to Issues via closing keywords (`Closes #15`, `Fixes #15`, `Resolves #15` — or `Closes org/repo#15`) in the PR body/commit targeting the default branch, or via the `Development` sidebar
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 49. Where should you commit `____.md` so every new Pull Request opened in the repository automatically pre-fills a Markdown checklist (`[ ] Docs updated`, `[ ] Screenshots attached`, `[ ] Accessibility checked`)?

- **A.** `.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists
- **B.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code

### 50. A newcomer wants to find open beginner-friendly Issues across a repository that have **no one** assigned yet. Which Issue filter query returns exact matches: `is:open is:issue label:"good first issue" ____:assignee`?

- **A.** Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 51. In personal **`Settings -> Notifications`**, an engineer working in Tokyo wants notification pushes/emails paused every evening from `18:00` to `09:00` JST and on weekends. Which built-in notification setting schedules quiet hours or temporary pauses?

- **A.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 52. Your employee personal GitHub account belongs to both `@personal-oss` and corporate `@prism-corp` (which verifies domain `prismcorp.io`). How do you ensure notifications from `@prism-corp` go to `you@prismcorp.io` while open-source notifications go to `you@gmail.com`?

- **A.** `CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 53. In the GitHub web **Notifications** inbox, what is the difference between marking a notification **`Done`** versus **`Unsubscribe`**?

- **A.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 54. Your design-system squad wants to publish `solstice-docs` as a live HTTPS documentation website using **GitHub Pages**. Which four-step workflow deploys and verifies the site?

- **A.** Archive the empty repository before adding files → Disable HTTPS enforcement → Create a Milestone named `Pages` → Expect Milestone creation to deploy a website
- **B.** Commit static site or Markdown docs to the repository → Open `Settings -> Pages` and set `Build and deployment` source → Run the GitHub Pages build/deployment workflow → Verify the published site URL and optional custom domain HTTPS
- **C.** Upload raw site files to a secret Gist → Enable `SECURITY.md` only → Disable GitHub Actions and Pages in Settings → Expect `<owner>.github.io` to publish automatically
- **D.** Point DNS CNAME to `localhost` → Delete repository `Settings` → Store HTML inside Saved Replies → Enable 2FA recovery codes

### 55. A developer advocacy team needs a hosted static tutorial website at `docs.beaconsdk.dev` AND an asynchronous forum for community RFC polls. Which two GitHub capabilities fit best? Select two.

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll
- **C.** Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 56. A conference speaker wants to store a private OAuth client secret (`CLIENT_SECRET=...`) where nobody outside their team can read it, even if the URL leaks in browser history. Proposed solution: Create a **Secret Gist** on `gist.github.com` containing the OAuth client secret. Does the solution protect the secret?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.

---

## Domain 4 — Apply modern development practices (10–15% official weight · 14 questions)

### 57. A documentation repo uses **GitHub Actions** to check broken hyperlinks every night at midnight UTC (`schedule: cron`) and on every Pull Request. Which two components define that workflow? Select two.

- **A.** Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 58. In a GitHub Actions workflow step, what is the difference between `____: actions/checkout@v4` and `run: npm run build`?

- **A.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **GitHub Actions** hierarchy: **Workflow** (`.github/workflows/*.yml`) triggered by **Events** (`push`, `pull_request`), running **Jobs** on **Runners** (`runs-on`) with ordered **Steps** (`uses:` / `run:`)
- **D.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution

### 59. Which GitHub Actions event trigger (`on: ____`) adds a **`Run workflow`** button inside the GitHub.com `Actions` tab (with optional typed input parameters) so maintainers can trigger a workflow manually on demand?

- **A.** **GitHub Actions** hierarchy: **Workflow** (`.github/workflows/*.yml`) triggered by **Events** (`push`, `pull_request`), running **Jobs** on **Runners** (`runs-on`) with ordered **Steps** (`uses:` / `run:`)
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses

### 60. A developer-experience lead trains engineers on 2026 **GitHub Copilot** capabilities. Which three features are part of GitHub Copilot's modern AI toolkit? Select three.

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity
- **C.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **D.** **IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio
- **E.** **Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request
- **F.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 61. Where should a team commit repository-wide natural-language coding conventions (such as *"Always use TypeScript strict types and Vitest instead of Jest"*) so **GitHub Copilot Chat**, **Code Review**, and **Copilot coding agent** follow them automatically: `.github/____.md`?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 62. Which set of IDEs is officially supported for native **GitHub Copilot** extensions?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)

### 63. Verified students, teachers, and maintainers of popular public open-source projects can qualify for complimentary access to which **GitHub Copilot** individual tier?

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **C.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **D.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)

### 64. On **GitHub Copilot Business** and **Copilot Enterprise**, does GitHub use your organization's private source code or prompts to train foundation AI models shared with other customers?

- **A.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **B.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 65. For regulated enterprises on **Copilot Business** and **Copilot Enterprise**, what does a GitHub-designated **Long-Term Support (`LTS`) model** guarantee?

- **A.** **Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 66. Your developer-advocacy team wants workshop attendees to launch a zero-setup **GitHub Codespace** preloaded with Python 3.12, the ` Ruff` VS Code extension, installed `requirements.txt` packages, and port `8000` forwarded. Which four-step sequence sets this up?

- **A.** Install tools manually inside one personal Codespace without editing `.devcontainer/` → Delete the Codespace → Ask teammates to open `github.dev` → Expect `github.dev` to provision that custom Docker container
- **B.** Create `.devcontainer/devcontainer.json` with image and VS Code extensions → Add `postCreateCommand` and `forwardPorts` → Commit `devcontainer.json` to the branch → Launch a cloud Codespace to verify
- **C.** Add Docker settings to `.github/FUNDING.yml` → Enable GitHub Sponsors → Star the repository → Expect `FUNDING.yml` to build a Codespace container
- **D.** Save `devcontainer.json` in a private user Wiki → Disable Codespaces in Organization Settings → Press `.` on the repository → Expect full container terminal execution

### 67. In `.devcontainer/devcontainer.json`, which lifecycle property (`"____": "npm ci"`) runs automatically once right after the Codespace container is created to install project dependencies?

- **A.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets

### 68. When a developer starts a web server on `localhost:3000` inside a **GitHub Codespace**, what is the **default visibility** of the automatically forwarded HTTPS preview URL (`https://<codespace>-3000.app.github.dev`)?

- **A.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **D.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`

### 69. A technical writer reviews a 12-file documentation Pull Request and fixes three Markdown typos across files, whereas a backend engineer needs to compile Go binaries and run database migrations. Which two editor choices match each role? Select two.

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **C.** **`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal
- **D.** **GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 70. While viewing `https://github.com/solstice-ui/docs/pull/142`, a developer wants to compile a C++ native addon and run unit tests in a bash terminal. Proposed solution: Press the `____` (`.`) shortcut to open **`github.dev`** and run `make test` inside `github.dev` without creating a Codespace. Does the solution work?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.

---

## Domain 5 — Manage projects with GitHub (5–10% official weight · 8 questions)

### 71. A design-systems PM manages quarterly component launches across `tokens`, `react-ui`, and `figma-plugin` in one **GitHub Project**. Which two features let stakeholders inspect the exact same backlog as both a sprint Kanban board and an executive timeline? Select two.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 72. During early backlog grooming before engineering repositories are chosen, how can a PM capture rough feature ideas on a **GitHub Project** without cluttering repository Issue trackers yet?

- **A.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **B.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account

### 73. A documentation lead creates a cross-repo **GitHub Project** to schedule biweekly doc sprints and auto-close completed cards. Which four-step workflow configures this?

- **A.** Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache
- **B.** Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts
- **C.** Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts
- **D.** Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards

### 74. Which specialized custom field type in **GitHub Projects** (`filtered via ____:@current`) automatically generates sequential dated sprint buckets (`Iteration 1: Nov 2–Nov 15`, `Iteration 2: Nov 16–Nov 29`) and supports break intervals?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** Project custom fields (`Single select`, `Number`, `Date`, `Text`, and **`Iteration`** sprints with automatic break capacities) plus filter/sort/group view configurations (`slice by`)
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment

### 75. A community manager wants every external user reporting a bug on `solstice-ui` to fill out mandatory dropdown fields for `Browser` and `Version`. Proposed solution: Add a personal **Saved reply** in the manager's account settings instead of creating `.github/ISSUE_TEMPLATE/*.yml` Issue Forms. Does the solution enforce mandatory intake fields for external reporters?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **D.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.

### 76. In an Issue list, selecting `Assignee` or typing `____:@me` filters the backlog to show only work items currently assigned to your signed-in GitHub account.

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 77. How does **Project Insights** (`inside a GitHub Project`) differ from **Repository Insights** (`inside a single repository`)?

- **A.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **B.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 78. A product manager notices the **total items line** in a GitHub Project's **Burn up** chart jumped upward by 18 items mid-iteration while the completed line stayed steady. What does that upward jump immediately reveal?

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks

---

## Domain 6 — Understand privacy, security, and administration (10–15% official weight · 14 questions)

### 79. A freelance contributor joins a client GitHub Organization that mandates two-factor authentication (`2FA`) and wants phishing-resistant passwordless login. Which four-step sequence secures their account?

- **A.** Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes
- **B.** Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication
- **C.** Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility
- **D.** Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in

### 80. An organization owner enables **`Require two-factor authentication for everyone in the organization`**. Which two actions should members complete beforehand so nobody loses access? Select two.

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout
- **D.** Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 81. What happens immediately to Organization Members and Outside Collaborators who do **not** have `2FA` enabled when an Organization Owner turns on mandatory `2FA` enforcement for the organization?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **C.** **Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 82. Which minimum repository role is required for a developer to create feature branches directly in an organization repository, push commits, and merge approved Pull Requests (`without changing repository Settings`)?

- **A.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)

### 83. You hire an external freelance accessibility auditor for two weeks who needs `Read` or `Triage` access to **one** specific private repository (`solstice-web`) without becoming an Organization Member or seeing internal Teams. How should you add them?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 84. Which specialized GitHub Organization role grants cross-repository visibility into **Security Overview**, Dependabot/CodeQL/Secret scanning alerts, and security configurations across the organization without granting `Organization Owner` privileges?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**

### 85. A media conglomerate standardizes on Microsoft Entra ID for identity and adopts GitHub Copilot across 25 squads. Which two administrative controls govern account lifecycle and AI usage centrally? Select two.

- **A.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability
- **D.** Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists
- **E.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 86. How can you visually recognize an **Enterprise Managed User (`EMU`)** username on GitHub.com (`e.g., priya_prism`), and who controls `priya_prism`'s profile name and email address?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 87. On **GitHub Copilot Enterprise** and **Copilot Business**, is **Copilot coding agent** enabled automatically without admin review, or must an enterprise/organization administrator explicitly enable its policy first?

- **A.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 88. A documentation engineering team protects `main` on `docs-site` using a **Repository Ruleset**. Which three rules ensure broken builds or unapproved edits never reach production? Select three.

- **A.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **B.** Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)
- **C.** Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **F.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 89. Why are modern **Repository Rulesets** preferred over legacy single-branch protection rules when governing 80 repositories inside a GitHub Organization?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 90. What happens to existing **Stars** and **Watchers** if an Organization Owner changes a `Public` repository's visibility to **`Private`**?

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Repository visibility levels: **`Public`** (open internet), **`Private`** (explicit users/teams only), and **`Internal`** (GitHub Enterprise only — readable by all enterprise members for **InnerSource**)
- **D.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)

### 91. In a GitHub Organization with `@solstice/design-systems` containing 8 designers, how does **Team code review assignment** avoid overloading one senior designer when `@solstice/design-systems` is requested on Pull Requests?

- **A.** **Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 92. On a public community-facing GitHub Organization experiencing spam comments across Discussions and Issues, which lightweight role lets trusted community helpers hide abusive comments, lock conversations, and block disruptive users temporarily without granting code `Write` or `Owner` rights?

- **A.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **B.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **C.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **D.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies

---

## Domain 7 — Explore the GitHub community (5–10% official weight · 8 questions)

### 93. An enterprise engineering team relies heavily on three open-source JavaScript maintainers and wants to fund them via corporate PO invoicing rather than an employee's personal credit card. Proposed solution: Enroll the company's GitHub Organization in **GitHub Sponsors for companies** using invoiced billing to sponsor those maintainers recurringly. Does GitHub Sponsors support organization/invoiced sponsorships?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **D.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.

### 94. Which built-in GitHub security feature lets maintainers of **public open-source repositories** receive private vulnerability reports from researchers, collaborate on a fix in a temporary private fork, and request a `CVE` ID before publishing a **GitHub Security Advisory**?

- **A.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

### 95. How does **Following** an organization (`e.g., github.com/vercel`) differ from **Watching** one specific repository (`e.g., vercel/next.js`)?

- **A.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 96. Before installing a third-party GitHub App from **GitHub Marketplace** onto your Organization, what trust indicator confirms GitHub has verified the publisher's domain ownership and organization identity?

- **A.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically

### 97. A design-systems team wants every squad inside their GitHub Enterprise to reuse and contribute icons/components to `solstice-icons` via **InnerSource** instead of reinventing duplicate buttons. Which two steps set up InnerSource effectively? Select two.

- **A.** Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 98. Why does **InnerSource** require transparent asynchronous communication in Issues, Pull Requests, and `CONTRIBUTING.md` instead of tribal DMs inside one team's private chat channel?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 99. A technical writer wants to fix a broken code sample in an upstream open-source documentation repository where they only have public `Read` access. Which four-step workflow submits the improvement cleanly?

- **A.** Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor
- **B.** Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream
- **C.** Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights
- **D.** Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge

### 100. Your personal fork `you/icons` is 28 commits behind upstream `solstice-ui/icons:main`. Which one-button web UI control on your fork's main page pulls the latest upstream commits into your fork's `main` branch without terminal commands?

- **A.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

---

## Answer Key and Explanations

### Question 1 — `C, D` (Understand Git and GitHub basics)

Correct answers: C and D (are correct). Every writer's clone holds full local revision history for offline editing, and commit metadata tracks who changed each paragraph and when so faulty edits can be reverted cleanly. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.
- **D:** Correct. Commit metadata provides line-by-line accountability and clean rollback via `git revert`.
- **E:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 2 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Every up-to-date clone of the repository acts as a full backup containing the entire commit graph, branches, and tags—not just the latest checked-out files. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 3 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Git performs a three-way merge combining both non-overlapping edits automatically while flagging a merge conflict only if both branches modified the exact same lines. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 4 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). `git log` (`--oneline --graph`) inspects the repository's commit timeline, authors, timestamps, and branch merge topology locally. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 5 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). They can initialize a local repository (`git init`), create branches, stage changes (`git add`), inspect `git diff`, and record local commits (`git commit`). [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 6 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Those collaboration, hosting, CI/CD, and governance capabilities are cloud/server features of **GitHub**, built on top of underlying **Git** version control. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 7 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). **GitHub CLI (`gh`)** brings GitHub platform workflows (`gh pr create`, `gh issue list`, `gh codespace create`, `gh run watch`) into the terminal alongside standard `git` commands. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 8 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Yes — local Git repository initialization, branching, committing, and merging require zero network connection to GitHub until students run `git push`/`git pull`. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **B:** Incorrect. `.gitignore` has no effect on files already tracked in the Git index; you must untrack via `git rm --cached` and immediately rotate exposed secrets.
- **C:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 9 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Edit `examples/quickstart.py` in the working tree, stage it with `git add`, commit a local snapshot with `git commit -m`, and upload commits with `git push`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. `git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.
- **B:** Incorrect. Committing before editing and staging captures nothing from the intended file modifications.
- **C:** Correct. Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).
- **D:** Incorrect. Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.

### Question 10 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). `git status` summarizes the current branch, remote tracking state, staged index changes, unstaged modifications, and untracked files. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 11 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git clone` creates a local directory, downloads the entire commit/branch history, checks out the default branch, and registers `origin` pointing to the GitHub URL. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.

### Question 12 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `HEAD` points to the tip of your currently checked-out branch (or directly to a specific commit SHA when in "detached `HEAD`" state). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Correct. Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.

### Question 13 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). `git pull` fetches new commits from the tracked remote branch and immediately merges (or rebases with `--rebase`) them into your active local branch. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).

### Question 14 — `A, C` (Understand Git and GitHub basics)

Correct answers: A and C (are correct). A **GitHub Organization** adds nested Teams and role-based repository permissions, while a **GitHub Enterprise** account governs multiple Organizations with SAML/OIDC SSO and enterprise audit logs. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. Organizations centralize multi-developer ownership and team-based RBAC.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. Enterprise accounts unify security, identity, and policy governance across multiple organizations.
- **D:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **E:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 15 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). **GitHub Pro** upgrades an individual Personal account with protected branches, Code Owners, Wikis, Pages, and extra Actions/Codespaces quota on private personal repositories. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Correct. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 16 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Yes — GitHub Free for Organizations supports unlimited collaborators on private repositories, whereas advanced governance features on private repos (Code Owners, protected branches, draft PRs, Pages/Wikis) require **GitHub Team** or **GitHub Enterprise**. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Correct. Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 17 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). **GitHub Enterprise Server (`GHES`)** delivers a self-hosted GitHub instance managed inside the customer's own infrastructure or private cloud. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **D:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.

### Question 18 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Create a descriptive topic branch off `main`, commit edits and open a Pull Request, gather peer review and pass link-checker status checks, then merge into `main` and delete the topic branch. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.
- **B:** Incorrect. Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.
- **C:** Incorrect. GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.
- **D:** Correct. GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.

### Question 19 — `B, C` (Understand Git and GitHub basics)

Correct answers: B and C (are correct). Every change happens on a safe short-lived branch off always-deployable `main`, and Pull Requests provide a single visual discussion/preview/check hub before merging. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Correct. Pull Requests combine asynchronous peer review and automated CI verification prior to merging.
- **C:** Correct. GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 20 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Anything in `main` is **always deployable**—every commit reaching `main` has already been peer-reviewed and validated by automated checks on a Pull Request. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Correct. GitHub Flow is a lightweight, branch-based workflow without complex long-lived `release`/`develop` trees, centered on short-lived branches and Pull Requests.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 21 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). GitHub waits to notify `CODEOWNERS` for review until the author transitions the Draft Pull Request to **`Ready for review`**, reducing premature review noise! [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Correct. Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.

### Question 22 — `C, D, E` (Understand Git and GitHub basics)

Correct answers: C, D, and E (are correct). `- [ ]` / `- [x]` task checkboxes, `> [!IMPORTANT]` / `> [!CAUTION]` blockquote alerts, and fenced code blocks with language or `mermaid` tags. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.
- **D:** Correct. GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.
- **E:** Correct. Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.
- **F:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 23 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Writing `> [!WARNING]` on the first line of a Markdown blockquote (followed by `> Your message` on subsequent lines) renders GitHub's native Warning alert box (`NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`). [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Correct. GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.

### Question 24 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Typing `/` (slash command) at the start of a line or after a space opens GitHub's slash-command palette inside Issue, PR, and Discussion editors. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 25 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Using ```` ```diff ```` colors lines starting with `+` green and lines starting with `-` red for clear before/after patch explanations. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Correct. Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.
- **C:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 26 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). GitHub Desktop automatically offers to **Stash** uncommitted changes on the current branch or **Bring my changes to `main`**, preventing lost work without CLI `git stash` commands. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **C:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **D:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.

### Question 27 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). GitHub Mobile acts as a verified **2FA push / number-matching authenticator** for your signed-in GitHub account. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **B:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **D:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.

### Question 28 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Yes — GitHub Mobile supports browsing repository files, making lightweight text/Markdown edits, committing to a branch, and opening/merging a Pull Request on the go. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **B:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **C:** Incorrect. Enabling the Dependency graph identifies direct/transitive packages, feeds Dependabot vulnerability alerts, and exports NTIA/SPDX Software Bills of Materials (`SBOM`).
- **D:** Incorrect. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.

### Question 29 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Add `.github/CODEOWNERS` mapping `/docs/api/** @prism/api-writers`, merge it into `main`, enable branch protection or a ruleset requiring PR reviews, and enable `Require review from Code Owners`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.
- **B:** Correct. `CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.
- **C:** Incorrect. `README.md` does not trigger automatic review requests or merge enforcement.
- **D:** Incorrect. Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.

### Question 30 — `C, E` (Work with GitHub repositories)

Correct answers: C and E (are correct). `CODEOWNERS` must sit in `.github/`, root, or `docs/` (where the **last matching pattern** in the file wins!), and branch protection / rulesets must require Code Owner review to block merges. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **E:** Correct. GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.

### Question 31 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). GitHub checks `.github/README.md` **first**, then root `/README.md`, and finally `docs/README.md`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.
- **B:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).

### Question 32 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). No — without a branch protection rule or repository ruleset enabling `Require a pull request before merging` and `Require review from Code Owners`, `.github/CODEOWNERS` only requests a review without blocking the merge button! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — without a branch protection rule or repository ruleset enabling `Require a pull request before merging` and `Require review from Code Owners`, `.github/CODEOWNERS` only requests a review without blocking the merge button!
- **D:** Correct. `CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.

### Question 33 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). By default, template creation copies only the template's default branch structure; checking `Include all branches` copies all template branches (such as `gh-pages` or `v2-preview`) into the new clean repository. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Correct. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Incorrect. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.

### Question 34 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). GitHub automatically retargets open Pull Requests and draft releases to the renamed default branch (`main`) and displays local `git branch -m` update instructions to contributors. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 35 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Committing a `.gitattributes` file (`* text=auto` / `*.sh text eol=lf`) enforces consistent line-ending normalization across Windows, macOS, and Linux clones. [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Correct. `.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 36 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). **Git Large File Storage (`Git LFS`)** (`git lfs track "*.psd"`) replaces large binary files inside Git commits with tiny text pointers while storing binary payloads on LFS object storage. [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **C:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 37 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Pressing `t` on a repository page activates GitHub's fuzzy file finder to jump directly to any file path across the tree. [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 38 — `A, C` (Work with GitHub repositories)

Correct answers: A and C (are correct). Enable the **Dependency graph** (which supports one-button SPDX JSON `Export SBOM` under `Insights -> Dependency graph`), and enable **Dependabot alerts & security updates**. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Correct. Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Correct. The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **E:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 39 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). `Insights -> Traffic` displays 14-day unique visitors, popular content paths, referring domains, and unique/total Git clones. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **D:** Correct. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.

### Question 40 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). Open your profile menu (`top-right avatar`) and select **`Feature preview`** to toggle individual user-level beta features on or off. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Correct. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.

### Question 41 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). **Pin** up to 6 public (or member-visible internal/private) repositories on the Organization profile (`Customize pins`) and tag them with descriptive **Topics**. [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 42 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Create a public repository named **`.github`** inside the Organization (`org/.github`) to share default community health files and Issue/PR templates across all org repositories! [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Correct. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 43 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). A **GitHub Issue** tracks actionable bugs, enhancements, and engineering tasks with labels, assignees, milestones, and linked Pull Requests. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **B:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **C:** Incorrect. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 44 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). A reviewer can **`Comment`** (general feedback without explicit approval), **`Approve`** (approve merging changes), or **`Request changes`** (block merge when required reviews are enforced until addressed). [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.

### Question 45 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). **Rebase and merge** rewrites and appends the feature branch's individual commits cleanly onto the tip of the base branch (`main`) with linear history. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.

### Question 46 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). A **Q&A** format Discussion category enables community voting plus **`Mark as answer`** so future visitors spot the solved resolution immediately. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Incorrect. GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.
- **C:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **D:** Correct. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.

### Question 47 — `D, E` (Collaborate using GitHub)

Correct answers: D and E (are correct). Use closing keywords (`Closes #19`, `Fixes prism/docs#88`) in the PR description/commit message, or link up to 10 Issues manually in the PR `Development` sidebar. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Manual `Development` sidebar links work across branches and display clear traceability on both timelines.
- **E:** Correct. Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.

### Question 48 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). `Related to` creates a timeline cross-reference only; automatic closing requires an official closing keyword (`close`/`closes`/`closed`, `fix`/`fixes`/`fixed`, or `resolve`/`resolves`/`resolved`). [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. When a linked Pull Request merges into the default branch, GitHub automatically closes the referenced Issue and cross-references both timelines.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 49 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Create `.github/pull_request_template.md` (or `pull_request_template.md` in root/`docs/`, or multiple templates in `.github/PULL_REQUEST_TEMPLATE/`) to pre-populate new PR descriptions. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.
- **B:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.

### Question 50 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Adding `no:assignee` filters for open Issues that currently have zero assigned owners so contributors avoid duplicating active work. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 51 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Configure notification **Custom routing / notification schedule** (or temporary **Pause notifications** / mobile quiet hours) so non-urgent pings wait until working hours. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 52 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Configure **Custom routing** under `Settings -> Notifications` to route notifications per GitHub Organization to verified organization-specific email addresses! [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. `CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.
- **B:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 53 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). Marking **`Done`** clears the item from your active inbox—and **resurfaces** it automatically if new comments arrive—whereas **`Unsubscribe`** mutes future activity on that thread unless directly `@mentioned`. [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 54 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Commit the static/Markdown docs to the repository, configure `Build and deployment` under `Settings -> Pages`, run the Pages build/deployment workflow, and verify the live HTTPS URL. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Milestones track Issue/PR progress and archived empty repositories cannot commit site content.
- **B:** Correct. GitHub Pages builds from a configured branch/folder or GitHub Actions workflow and serves the site over HTTPS at `<owner>.github.io/<repo>` or a verified custom domain.
- **C:** Incorrect. Secret Gists do not publish GitHub Pages sites when Pages is disabled in repository settings.
- **D:** Incorrect. `localhost` DNS records and Saved Replies have no connection to GitHub Pages hosting.

### Question 55 — `B, C` (Collaborate using GitHub)

Correct answers: B and C (are correct). Host the custom-domain HTTPS static site on **GitHub Pages** and run community polls/Q&A in **GitHub Discussions**. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. GitHub Pages renders repository docs into browsable websites with HTTPS.
- **C:** Correct. Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 56 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). No — **Secret Gists** are merely unlisted from public search; anyone who obtains the Gist URL can view and clone it without authentication! Store secrets in encrypted GitHub Secrets instead. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Correct. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Secret Gists** are merely unlisted from public search; anyone who obtains the Gist URL can view and clone it without authentication! Store secrets in encrypted GitHub Secrets instead.

### Question 57 — `A, D` (Apply modern development practices)

Correct answers: A and D (are correct). A YAML workflow file under `.github/workflows/` declaring `on:` triggers (`pull_request` and `schedule`), and `jobs:` specifying `runs-on:` runners with `steps:`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Correct. GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 58 — `C` (Apply modern development practices)

Correct answer: C (is correct). `uses:` executes a reusable packaged **Action** (from a repository, Marketplace, or Docker image), whereas `run:` executes command-line shell commands directly on the runner OS (`bash`/`pwsh`). [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. In GitHub Actions, jobs run in parallel by default on fresh virtual runner machines (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) unless ordered via `needs:`.
- **D:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.

### Question 59 — `A` (Apply modern development practices)

Correct answer: A (is correct). Configuring `on: workflow_dispatch` enables manual on-demand triggering from the GitHub UI, GitHub CLI (`gh workflow run`), or REST API. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. In GitHub Actions, jobs run in parallel by default on fresh virtual runner machines (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) unless ordered via `needs:`.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.

### Question 60 — `B, D, E` (Apply modern development practices)

Correct answers: B, D, and E (are correct). **Copilot coding agent** opening autonomous cloud draft PRs from Issues, local **IDE Agent Mode** iterating across workspace files and terminal output, and **multi-model selection** across AI providers. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Correct. Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.
- **C:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **D:** Correct. IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.
- **E:** Correct. Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.
- **F:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 61 — `C` (Apply modern development practices)

Correct answer: C (is correct). Committing `.github/copilot-instructions.md` injects persistent repository coding and testing guidelines automatically into Copilot prompts and agent sessions. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Correct. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 62 — `B` (Apply modern development practices)

Correct answer: B (is correct). Visual Studio Code, Visual Studio, JetBrains IDEs (IntelliJ, PyCharm, WebStorm, Rider, etc.), Xcode, and Vim/Neovim (plus Eclipse/Azure Data Studio integrations and Copilot CLI). [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.

### Question 63 — `B` (Apply modern development practices)

Correct answer: B (is correct). Verified GitHub Education students/faculty and eligible popular open-source maintainers receive complimentary access to **GitHub Copilot Pro** (Individual). [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **C:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **D:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.

### Question 64 — `B` (Apply modern development practices)

Correct answer: B (is correct). No — under Copilot Business and Copilot Enterprise privacy commitments, private business prompts, suggestions, and source code are **not** retained to train foundation models for other customers. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **B:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 65 — `A` (Apply modern development practices)

Correct answer: A (is correct). GitHub commits to keeping a designated **LTS model** available for an extended one-year stability window so enterprise workflows do not break from sudden model deprecations. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Correct. Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 66 — `B` (Apply modern development practices)

Correct answer: B (is correct). Create `.devcontainer/devcontainer.json` with Python 3.12 and VS Code extensions, configure `postCreateCommand` and `forwardPorts: [8000]`, commit `devcontainer.json` to the repo, and launch a Codespace to verify. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. Uncommitted manual installs vanish when a Codespace is deleted, and `github.dev` does not run dev containers.
- **B:** Correct. Committing `.devcontainer/devcontainer.json` standardizes runtimes, extensions, startup commands, and port forwarding for every contributor launching a Codespace.
- **C:** Incorrect. `FUNDING.yml` configures sponsor buttons rather than Codespaces dev containers.
- **D:** Incorrect. Wikis do not configure Codespaces, disabling Codespaces blocks creation, and `.` launches browser-only `github.dev`.

### Question 67 — `D` (Apply modern development practices)

Correct answer: D (is correct). `postCreateCommand` executes setup scripts (such as `npm ci` or `pip install -r requirements.txt`) automatically after container creation. [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.

### Question 68 — `C` (Apply modern development practices)

Correct answer: C (is correct). **`Private`** to the authenticated user who owns the Codespace (adjustable to `Private to Organization` or `Public` only if allowed by organization port-visibility policy). [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **D:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).

### Question 69 — `C, D` (Apply modern development practices)

Correct answers: C and D (are correct). Use free browser-based **`github.dev`** (`press .`) for fast multi-file Markdown edits/PR review, and use **GitHub Codespaces** for full cloud VM compilation and terminal execution. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **C:** Correct. `github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.
- **D:** Correct. Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 70 — `B` (Apply modern development practices)

Correct answer: B (is correct). No — pressing `.` opens browser-only `github.dev`, which has no compute VM or integrated terminal to compile C++ or run `make test`; launch a **GitHub Codespace** instead. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Correct. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — pressing `.` opens browser-only `github.dev`, which has no compute VM or integrated terminal to compile C++ or run `make test`; launch a **GitHub Codespace** instead.
- **D:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.

### Question 71 — `B, D` (Manage projects with GitHub)

Correct answers: B and D (are correct). Create multiple saved views (`Table`, `Board`, and `Roadmap`) over custom `Iteration`/`Date` fields, backed by built-in **Project workflows** and **Insights** burn-up charts. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Correct. Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 72 — `D` (Manage projects with GitHub)

Correct answer: D (is correct). Add **`Draft issues`** directly inside the GitHub Project (`+ Add item` -> type title), and convert approved Draft issues into real repository Issues in one action when ready for development! [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **B:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Correct. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.

### Question 73 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Create a GitHub Project with custom `Iteration` and `Priority` fields, link repository Issues/PRs, enable built-in `Item closed -> Done` workflows, and review Project Insights burn-up charts. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.
- **B:** Correct. GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.
- **C:** Incorrect. `SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.
- **D:** Incorrect. Gists do not host Milestones or drive organization GitHub Projects automations.

### Question 74 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). The **`Iteration`** custom field creates repeating time-boxed sprints (plus optional cool-down breaks) filterable via `iteration:@current`. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Correct. `Iteration` fields track time-boxed sprints directly inside GitHub Projects without external agile plugins.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.

### Question 75 — `D` (Manage projects with GitHub)

Correct answer: D (is correct). No — **Saved replies** belong to one user's personal comment toolbar and never render intake forms for external bug reporters; configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/` instead. [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Saved replies** belong to one user's personal comment toolbar and never render intake forms for external bug reporters; configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/` instead.
- **C:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **D:** Correct. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.

### Question 76 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Using `assignee:@me` dynamically resolves `@me` to whichever authenticated user views the filter or saved Project view! [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 77 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Project Insights charts cross-repository work-item progress, custom fields (`Priority`, `Estimate`, `Iteration`), and burn-up trends, whereas Repository Insights shows single-repo Git commits, traffic, forks, and dependency graphs. [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **B:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 78 — `D` (Manage projects with GitHub)

Correct answer: D (is correct). Mid-sprint **scope creep**—18 new Issues/items were added to the active iteration after planning began. [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.

### Question 79 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). Enable `2FA` via TOTP or security key, download and store one-time recovery codes safely, register a phishing-resistant passkey in Security settings, and verify passkey/`2FA` sign-in. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.
- **B:** Incorrect. GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.
- **C:** Incorrect. Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.
- **D:** Correct. Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.

### Question 80 — `C, D` (Understand privacy, security, and administration)

Correct answers: C and D (are correct). Configure WebAuthn **Passkeys** / TOTP security keys on their accounts, and download + safely store one-time **`2FA` recovery codes**. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Recovery codes are essential to regain account access if a phone or hardware key is lost.
- **D:** Correct. Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 81 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Members and outside collaborators without `2FA` enabled are **removed** from the organization (and lose access to its private repositories until they enable `2FA` and are reinstated)! [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **C:** Correct. Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 82 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). The **`Write`** repository role grants read/clone plus push, branch creation, and Pull Request merge permissions without exposing administrative repository settings. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.

### Question 83 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). Invite the freelancer as an **Outside Collaborator** on `solstice-web` only with the `Triage` (or `Read`) repository role. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 84 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). The **`Security Manager`** organization role provides organization-wide security alert visibility and security-setting management under least privilege. [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.

### Question 85 — `C, D` (Understand privacy, security, and administration)

Correct answers: C and D (are correct). Use **Enterprise Managed Users (`EMUs`)** provisioned via Entra ID OIDC/SAML + SCIM, and enforce **organization/enterprise Copilot policies** over models, agents, seats, and public-code matching. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.
- **D:** Correct. EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.
- **E:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 86 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). EMU usernames append an underscore and the enterprise's unique **shortcode** (`_<shortcode>`), and profile/email/membership attributes are controlled exclusively by the enterprise **Identity Provider (`IdP`)**. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Correct. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 87 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). For Copilot Business and Copilot Enterprise organizations, **Copilot coding agent** is governed by admin policy (disabled until enabled by an enterprise/org admin, with optional per-repository opt-outs). [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Correct. Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 88 — `A, B, C` (Understand privacy, security, and administration)

Correct answers: A, B, and C (are correct). Require Pull Requests with approvals + **Code Owner** review, require passing link-check/build **status checks**, and block **force-pushes** and branch deletions. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **B:** Correct. Blocking force-pushes and deletions protects commit history integrity on production branches.
- **C:** Correct. Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **F:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 89 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). Organization-level **Rulesets** can target branches and tags across **multiple repositories** simultaneously using naming patterns/properties, layer cleanly with repo rules, and support explicit bypass lists. [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 90 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Changing a repository from `Public` to `Private` permanently removes external Stars/Watchers, detaches public forks into standalone network roots, and unpublishes public GitHub Pages unless Enterprise private Pages applies! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. `Internal` visibility exists specifically in GitHub Enterprise organizations so all employees across sibling orgs can discover and fork repositories (`InnerSource`) without making code `Public`.
- **D:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.

### Question 91 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). Enabling **Team review auto-assignment** (`Round robin` or `Load balance` algorithm) automatically picks 1–N individual team members fairly instead of pinging all 8 designers on every PR! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Correct. Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 92 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Assigning community leads as Organization **`Moderators`** lets them block/unblock users from the org, manage interaction limits, and hide comments across public repositories. [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **B:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **C:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **D:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.

### Question 93 — `B` (Explore the GitHub community)

Correct answer: B (is correct). Yes — Organizations and Enterprises can sponsor open-source developers and projects directly through GitHub Sponsors (including invoiced billing options for eligible enterprise accounts). [Skill 7.1: Describe the benefits of open source and GitHub Sponsors | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Sponsors and open-source sustainability (https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **C:** Incorrect. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **D:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.

### Question 94 — `C` (Explore the GitHub community)

Correct answer: C (is correct). **Private Vulnerability Reporting** and **GitHub Security Advisories** let open-source maintainers privately triage, patch, and disclose CVEs responsibly at `$0` cost. [Skill 7.2: Explain how GitHub supports and advances open-source projects | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Supporting open-source projects with community profiles and Security Lab / advisories (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)]

- **A:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Correct. GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 95 — `C` (Explore the GitHub community)

Correct answer: C (is correct). Following surfaces high-level public milestones (new repositories, releases) in your dashboard **`Following` feed**, whereas Watching a repository sends active **Notifications** for Issues, PRs, or Releases on that single repo. [Skill 7.3: Identify how to follow users and organizations to stay informed about activity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Following people and organizations on GitHub to track activity (https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)]

- **A:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Correct. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 96 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Look for the **`Verified creator`** badge on the GitHub Marketplace listing and review the exact granular repository/organization permissions requested during installation. [Skill 7.4: Describe the GitHub Marketplace and its purpose | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Marketplace for GitHub Apps and Actions (https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace)]

- **A:** Correct. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).

### Question 97 — `A, C` (Explore the GitHub community)

Correct answers: A and C (are correct). Configure `solstice-icons` with **`Internal`** visibility + `README`/`CONTRIBUTING`/`CODEOWNERS`, and tag it with **Repository Topics** (`#design-system`, `#icons`) while accepting cross-team PRs. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. `Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Correct. Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 98 — `B` (Explore the GitHub community)

Correct answer: B (is correct). Written context in Issues, PRs, and `CONTRIBUTING.md` lets engineers in other time zones and departments understand architectural constraints and contribute self-sufficiently without gatekeeping meetings. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 99 — `B` (Explore the GitHub community)

Correct answer: B (is correct). Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`, fork upstream to your account and create a topic branch, commit and push your fix to your fork, and open a cross-repo Pull Request to upstream. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.
- **B:** Correct. External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.
- **C:** Incorrect. Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.
- **D:** Incorrect. Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.

### Question 100 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Selecting **`Sync fork -> Update branch`** on GitHub.com fetches and merges (or discards conflicting commits on) your fork's branch directly from the upstream repository! [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Correct. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
