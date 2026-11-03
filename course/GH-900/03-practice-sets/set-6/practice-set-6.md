# Microsoft Exam GH-900: GitHub Foundations — Full-Length Mock Exam 6

**Theme:** Open-Source Ecosystems & Global Collaboration — Fork-and-PR Workflows, Repository Templates, Discussions, Marketplace, Following & Archiving  
**Credential:** `Microsoft Certified: GitHub Foundations` *(Beginner / Fundamentals · **no prerequisite** · **does not require renewal / never expires**)*  
**Study guide baseline:** `January 2026 (Last updated February 19, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-900 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Docs documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Understand Git and GitHub basics (25–30% official weight · 28 questions)

### 1. An international open-source scientific Python ecosystem (`PyHelios`) accepts commits from 1,400 contributors across 60 countries. Which two version-control foundations make massive decentralized collaboration safe? Select two.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely
- **C.** Every developer clone contains the full commit history and branches, enabling offline commits and history inspection
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 2. A researcher boarding an 11-hour transpacific flight clones `pyhelios/core` before takeoff. Which operations can they complete **100% offline** in Git during the flight (`git branch`, `git commit`, `git log`, `git diff`) versus needing Wi-Fi?

- **A.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **B.** Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`

### 3. In an open-source repository adhering to the **Developer Certificate of Origin (`DCO`)**, passing which flag on `git commit` (`git commit ____ -m "Fix FFT boundary"`) appends `Signed-off-by: Name <email>` to certify contributor rights?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 4. Which Git command (`git ____ src/fft.py`) prints each line of `src/fft.py` annotated with the commit SHA, author name, and date that last modified that line?

- **A.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **D.** Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery

### 5. If an open-source project mirrors its exact Git repository onto both `github.com` and an university Git server, why are all commit SHAs identical across both hosts while **Issues**, **Discussions**, and **Actions** live specifically on GitHub?

- **A.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **B.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 6. Which local Git file inside a cloned repository (`____/config`) stores local repository settings such as `remote "origin"` URLs and branch tracking entries?

- **A.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **B.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 7. A university lab wants contributors without browser UI context-switching to open Pull Requests and check CI status directly from bash alongside `git`. Proposed solution: Install official **GitHub CLI (`gh`)**, run `gh auth login`, and use `gh pr create` and `gh pr checks`. Does the solution work?

- **A.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **B.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.

### 8. When cloning a public repository from GitHub (`git clone https://github.com/pyhelios/core.git`) onto a clean machine solely to read and run the code locally, do you even need a GitHub account to run `git clone`?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance

### 9. An open-source contributor adds a docstring example in `pyhelios/optics.py` locally and pushes their branch to their fork on GitHub. Which four-step Git workflow applies?

- **A.** Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`
- **B.** Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`
- **C.** Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`
- **D.** Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`

### 10. When you create a brand-new file `examples/demo.py` in your working directory that Git has never seen before, how does `git status` classify `examples/demo.py` before you run `git add`?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **D.** Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)

### 11. You just ran `git commit -m "Typo in mesage"` locally (**not pushed yet**) and want to fix the commit message typo immediately (`git commit ____ -m "Fix message"`). Which flag replaces your last unpushed local commit?

- **A.** A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link

### 12. Why is creating 5 experimental branches in Git nearly instantaneous (`milliseconds`) and tiny on disk even in a `2 GB` repository?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **C.** A lightweight movable pointer to a commit that isolates feature or bugfix work from the default branch (`main`) until merged
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 13. When working on a fork where `origin` points to `github.com/you/core.git` and `upstream` points to `github.com/pyhelios/core.git`, which command (`git fetch ____`) downloads upstream maintainers' latest commits without overwriting your local branch?

- **A.** `git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits
- **B.** Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`
- **C.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 14. A global open-source foundation hosts 45 community projects across multiple GitHub Organizations and manages corporate sponsor governance under an Enterprise umbrella. Which two account types structure this? Select two.

- **A.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)
- **B.** Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies
- **C.** Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **E.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 15. What does the green square heatmap on a developer's **Personal GitHub profile** (**Contribution graph**) visualize by default (with an optional setting to include anonymized private contributions)?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 16. Why should an open-source project with 3 maintainers transfer ownership from `@founder-alice/pyhelios` (**Personal account**) into `@pyhelios/core` (**GitHub Organization**, free for public repos!)?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 17. When transferring a repository from `@founder-alice/pyhelios` to `@pyhelios/pyhelios` on GitHub, what happens to existing `git clone` URLs and web links pointing to the old `@founder-alice/pyhelios` URL?

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing
- **D.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships

### 18. A global contributor adds Dark Mode math plots to `pyhelios` following **GitHub Flow**. Which four-step workflow applies?

- **A.** Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review
- **B.** Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge
- **C.** Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch
- **D.** Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks

### 19. Why does **GitHub Flow** work just as cleanly for asynchronous global contributors across 12 time zones as for co-located teams? Select two.

- **A.** Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`
- **B.** Create a short-lived descriptive branch off `main` so `main` stays deployable at all times
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically

### 20. An open-source newcomer opens a **Draft Pull Request** (`WIP: Add GPU backend`) to verify Linux/macOS CI workflows and ask an architectural question before finishing unit tests. Does a Draft PR trigger `on: pull_request` CI workflows by default?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 21. When your fork's feature branch falls behind `upstream/main` and shows no conflicts on GitHub, what single button on your fork's repo page (`____ fork -> Update branch`) updates your fork's `main` branch in the browser?

- **A.** Resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in affected files, stage the clean file (`git add`), and complete the merge commit
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 22. Maintainers overhaul `pyhelios/README.md` and `CONTRIBUTING.md` in GitHub Flavored Markdown. Which three GFM features render release checklists, beginner tips, and architecture flowcharts? Select three.

- **A.** Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`
- **B.** Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax
- **C.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **E.** Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)
- **F.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically

### 23. In `README.md`, you want to embed a logo image that automatically switches between `logo-dark.svg` and `logo-light.svg` when a visitor toggles GitHub **Dark Mode** vs **Light Mode**. Which HTML element supported in GFM achieves theme-aware images?

- **A.** Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 24. When you paste a full GitHub link to a specific Issue comment or code line (`e.g., https://github.com/pyhelios/core/blob/9f2a1d.../optics.py#L10-L18`) on its own line inside an Issue or PR body, what does GitHub render automatically?

- **A.** `@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 25. In GitHub Flavored Markdown, how do you insert a clickable **footnote** citation (`Here is a claim[^1]` paired with `____: Citation URL` at the bottom of the document)?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)

### 26. A university student contributing to open source for the first time wants to clone their fork, switch branches, commit notebooks, and push to GitHub on macOS using a free official graphical app rather than terminal commands. Which client fits?

- **A.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go

### 27. An open-source maintainer traveling by train wants to answer a contributor's `GitHub Discussion` question, mark a helpful community reply as the accepted answer, and label 4 new Issues. Which official mobile client supports this?

- **A.** **GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies
- **D.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 28. Can you browse repository `README.md` files, release notes, and repository file trees directly inside **GitHub Mobile**, or does GitHub Mobile show only Notifications?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets

---

## Domain 2 — Work with GitHub repositories (10–15% official weight · 14 questions)

### 29. Maintainers of `pyhelios` require `@pyhelios/cuda-maintainers` to review and approve every Pull Request modifying `/src/cuda/**`. Which four-step sequence enforces this?

- **A.** Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages
- **B.** Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings
- **C.** Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests
- **D.** Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`

### 30. A community maintainer adds `CODEOWNERS` to `pyhelios` (`a public repository`). Which two facts apply to `CODEOWNERS` location and enforcement? Select two.

- **A.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **B.** Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **E.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`

### 31. Compare two popular open-source `LICENSE` choices on GitHub: **`MIT`** (permissive) versus **`GNU GPLv3`** (strong copyleft). What key obligation distinguishes `GPLv3` from `MIT`?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage

### 32. When a first-time contributor opens the `New Pull Request` or `New Issue` screen on a repository containing `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`, where does GitHub surface links to those files automatically?

- **A.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request

### 33. A hackathon organizer publishes `hackathon-starter-kit` and wants 80 student teams to create independent project repositories with clean 1-commit histories (`not linked as 80 forks of each other`). Proposed solution: Tell all 80 student teams to select **`Fork`** instead of configuring `hackathon-starter-kit` as a **Template repository**. Does Forking give clean 1-commit independent repos?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 34. A macOS contributor wants `.DS_Store` ignored across **every** Git repository on their laptop without adding `.DS_Store` into 50 upstream projects' `.gitignore` files (`git config --global core.____ ~/.gitignore_global`). Which global Git setting handles personal OS files?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking
- **C.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 35. When maintainers rename a repository's default branch from `master` to `main` in GitHub **`Settings -> Branches`**, how does GitHub assist open Pull Requests and contributors?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 36. While viewing a Markdown file (`docs/tutorial.md`) on GitHub.com that renders formatted headings and Mermaid diagrams, which button in the file header displays the unrendered plain-text Markdown source directly?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`
- **D.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`

### 37. While reading Python or TypeScript source code in GitHub's web file viewer, selecting any function or class identifier opens the **Symbols** pane (`____ to definition / Find all references`). What powers this browser code navigation?

- **A.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`

### 38. Open-source maintainers of `pyhelios` want to see **which downstream public repositories depend on `pyhelios`** (`Dependents`) AND receive automated PRs when `numpy`/`scipy` disclose CVEs. Which two features enable this? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)
- **C.** Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests
- **D.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 39. An open-source maintainer checks `Repository -> Insights -> Traffic` and notices **`14-day`** metrics for `Git clones` and `Visitors`. Why does `Traffic` report both `Total` and **`Unique`** counts?

- **A.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks

### 40. Why do open-source researchers **Star** 200 interesting libraries on GitHub instead of clicking **`Watch -> All Activity`** on all 200 libraries?

- **A.** **Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities

### 41. Why is **deleting** a popular retired open-source repository (`5,000 downstream package imports`) dangerous compared to **Archiving** it? (`Including namespace hijacking / repo-jacking concerns!`)

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **D.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability

### 42. How many **Pinned** repositories (or Gists) can a developer feature prominently at the top of their **Personal GitHub profile** to showcase their best open-source work?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

---

## Domain 3 — Collaborate using GitHub (10–15% official weight · 14 questions)

### 43. When reviewing a documentation Pull Request from a first-time contributor who misspelled three function names on lines `22–24`, how can a maintainer offer a **1-button commitable fix** inside their review comment?

- **A.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **B.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 44. When a community member resolves another user's question inside a **`Q&A`** **GitHub Discussion** and their reply is marked **`Mark as answer`**, how does that help future users searching Google or GitHub?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** **GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**
- **C.** **Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 45. A heated flamewar erupts on a closed Issue `#401`, derailing constructive work. Which moderation action (`____ conversation` as `Off-topic`, `Too heated`, `Resolved`, or `Spam`) freezes new non-collaborator comments while preserving the historical record?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only

### 46. To highlight up to **3** high-visibility Issues (such as *"v3.0 Roadmap Feedback"* or *"Known Windows Installer Workaround"*) at the very top of a repository's **Issues** tab, which maintainer action pins them above chronological Issues?

- **A.** **GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms
- **B.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **C.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **D.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains

### 47. An open-source contributor resolves bug Issue `#42` in `pyhelios/core` and wants `#42` closed automatically when maintainers merge the Pull Request into `main`. Which four-step workflow applies?

- **A.** Triage the Issue with labels, milestone, and assignee → Create a feature branch and commit the fix → Open a Pull Request containing `Closes #42` in its description → Merge the approved Pull Request into the default branch
- **B.** Write `Mentioning #42` in a commit on a non-default experimental branch → Never open a Pull Request → Delete the feature branch → Expect Issue `#42` to close automatically
- **C.** Close Issue `#42` manually before writing code → Commit directly to a fork wiki → Open an unlinked Discussion post → Archive the repository
- **D.** Create a secret Gist with `Fixes #42` → Star the repository → Watch releases only → Expect Gist save to close Issue `#42`

### 48. A contributor in `pyhelios/docs` opens a Pull Request that fixes documentation Issue `#19` tracked inside sibling repository `pyhelios/core`. Which two ways link and auto-close `pyhelios/core#19` upon merge? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it
- **D.** Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 49. Why do large open-source projects prefer YAML **Issue Forms** (`.github/ISSUE_TEMPLATE/bug_report.yml`) over plain Markdown Issue templates (`.github/ISSUE_TEMPLATE/bug_report.md`)?

- **A.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** `.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists
- **D.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.

### 50. A newcomer wants to search across **all of GitHub** for open Python Issues labeled `"good first issue"` that have **zero assignees** (`is:open is:issue language:Python label:"good first issue" ____:assignee`). Which negation qualifier excludes already-claimed Issues?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`

### 51. An open-source consumer uses `pyhelios` in production and wants an email **only** whenever `pyhelios` publishes a new version (`v2.6.0`), without receiving 300 daily Issue/PR notifications. Which `Watch` setting achieves this?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 52. When going on a two-week vacation, how can a maintainer pause GitHub notifications temporarily or mark finished threads cleanly in the web Notifications inbox?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)

### 53. If you reply to a GitHub Issue notification email directly from your email client, where does your reply appear?

- **A.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage

### 54. An open-source project wants free HTTPS hosting for its Sphinx API documentation website (`docs.pyhelios.org`) plus a searchable community Q&A forum right in the repo. Which two GitHub features provide this at `$0` for public repos? Select two.

- **A.** Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll
- **B.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **C.** Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`
- **D.** Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues
- **E.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 55. When configuring a custom domain (`docs.pyhelios.org`) for **GitHub Pages**, which file (`____` committed at the publishing root or managed by GitHub Actions Pages deployment) records the custom domain alongside your DNS `CNAME`/`A` records?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains
- **D.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`

### 56. A student wants to keep private lecture notes and exam solutions completely hidden so even classmates who stumble across the URL cannot view them without permission. Proposed solution: Save the solutions in a **Secret Gist** on `gist.github.com`. Does a Secret Gist block anyone who has the URL?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.

---

## Domain 4 — Apply modern development practices (10–15% official weight · 14 questions)

### 57. Maintainers set up a `pytest` workflow in **GitHub Actions** on `pyhelios/core` to test every push and Pull Request automatically. Which four-step workflow applies?

- **A.** Place `ci.yml` inside `docs/workflows/` → Omit `on:` triggers and `runs-on:` runner labels → Save as a personal Gist → Expect repository Pull Requests to run CI automatically
- **B.** Open `github.dev` with `.` key → Run `npm test` directly inside `github.dev` browser tab → Save output in a Wiki page → Expect automatic status checks on Pull Requests
- **C.** Create an Issue template in `.github/ISSUE_TEMPLATE/` → Assign `@copilot` to a Milestone → Star the repository → Expect Issue templates to execute unit tests on Linux runners
- **D.** Create `.github/workflows/ci.yml` → Define `on: [push, pull_request]` triggers → Configure `jobs` with `runs-on: ubuntu-latest` and test `steps` → Commit `ci.yml` and inspect logs in the `Actions` tab

### 58. To prevent untrusted first-time fork Pull Requests from abusing CI runners or exfiltrating secrets on a public open-source repo, which two foundational **GitHub Actions** mechanics govern `.github/workflows/` execution? Select two.

- **A.** Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)
- **B.** Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 59. Why are repository **`Secrets`** **not** passed to `pull_request` workflows triggered from **external forks** on a public open-source repository?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **D.** Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers

### 60. Open-source maintainers use **GitHub Copilot** to clear documentation debt, refactor modules locally, and benchmark different LLMs on scientific algorithms. Which three capabilities support these tasks? Select three.

- **A.** **Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** **Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity
- **D.** **IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio
- **E.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **F.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 61. In a polyglot open-source monorepo (`/python/**` using `NumPy` docstrings and `/rust/**` using `cargo clippy` idioms), how can maintainers guide **GitHub Copilot coding agent** and **IDE Agent Mode** with repository-specific instructions?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **C.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **D.** **Copilot coding agent** works asynchronously on assigned GitHub Issues in an Actions sandbox to open draft PRs, whereas **IDE Agent Mode** edits local files and runs local terminal tasks autonomously

### 62. In **GitHub Copilot CLI** / terminal integration (`gh copilot` / Copilot in terminal), what practical help does Copilot give a newcomer confused by cryptic `git` or `tar` flags?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** **GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`
- **C.** `SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues
- **D.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 63. How can verified **students**, **teachers** (`GitHub Education`), and **maintainers of popular open-source repositories** access **GitHub Copilot Pro**?

- **A.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)

### 64. Which individual plan above `Copilot Pro` (`$10/mo`) gives power-user solo developers maximum monthly premium requests and full access across all frontier AI models (`$39/mo` individual tier)?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **C.** **Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 65. Why does **multi-model support** in **GitHub Copilot** let developers switch models mid-workflow inside Copilot Chat or Agent Mode?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** **Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance
- **D.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases

### 66. An open-source library requires `CMake`, `FFTW`, and `Python 3.12` (`45 minutes of painful laptop setup` that scares away newcomers). How do maintainers give every contributor a **1-button ready-to-compile environment** in 15 seconds?

- **A.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **B.** **`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution
- **C.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 67. Does every personal GitHub Free / Pro account include a monthly free usage quota of **GitHub Codespaces** core-hours and storage for open-source and personal learning?

- **A.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal
- **B.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **C.** **GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`
- **D.** **GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies

### 68. What do **GitHub Codespaces Prebuilds** (`configured via GitHub Actions`) accomplish for large open-source or enterprise repositories with heavy compile/dependency steps?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets
- **C.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **D.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them

### 69. A translator fixes typos across 8 Spanish localization `.md` files in `pyhelios/docs`, while a kernel contributor compiles Cython extensions and runs `pytest`. Which two browser-accessible tools fit best? Select two.

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** **`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal
- **E.** Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal

### 70. A student contributor opens `https://github.dev/pyhelios/core` on a Chromebook and wants to run `python -m pytest` inside `github.dev` to verify their math fix. Proposed solution: Open the terminal panel inside `github.dev` and run `python -m pytest` without creating a Codespace. Will `python -m pytest` run inside `github.dev`?

- **A.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **B.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **C.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

---

## Domain 5 — Manage projects with GitHub (5–10% official weight · 8 questions)

### 71. Open-source core maintainers publish a transparent public `PyHelios 3.0` **GitHub Project** spanning `core`, `docs`, and `website`. Which two Project capabilities keep community contributors aligned? Select two.

- **A.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields
- **D.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **E.** Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts

### 72. Before converting a rough roadmap brainstorm item on a **GitHub Project** board into a real repository Issue (`which would notify repository watchers`), which lightweight Project-only item type (`____ issue`) can maintainers add directly on a Project board?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** **GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account
- **C.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **D.** `README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage

### 73. Maintainers configure a public `PyHelios` release **GitHub Project** with sprint/release buckets, automated PR/Issue closure updates, and progress charts. Which four-step sequence applies?

- **A.** Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache
- **B.** Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts
- **C.** Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards
- **D.** Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts

### 74. When viewing a **Milestone** (`v3.0.0`, filterable via `____:"v3.0.0"`) inside `pyhelios/core`, how does GitHub calculate the green Milestone completion percentage bar (`e.g., 75% complete`)?

- **A.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **B.** **Labels** categorize Issues/PRs (`bug`, `priority:high`), **Milestones** track completion percentage toward a repository release target date, and **Project built-in workflows** auto-update `Status` when items close or PRs merge
- **C.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 75. Lead maintainer Priya adds 6 helpful **Saved replies** in her personal GitHub account settings and expects co-maintainer Mateo's comment toolbar to automatically list her 6 Saved replies too. Proposed solution: Share triage responses across 10 maintainers solely by adding personal **Saved replies** under Priya's user settings. Will Mateo see Priya's Saved replies?

- **A.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.
- **B.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.

### 76. On a public open-source repository, setting `Assignees`, `Labels`, or `Milestones` directly requires at least **`____`** repository access (so external contributors without that role cannot self-assign via the gear icon).

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 77. What is the difference between **Repository `____`** (`Pulse`, `Contributors`, `Traffic`, `Dependency graph`) and **GitHub Projects `Insights`** (`Burn up`, custom `Status`/`Iteration` charts)?

- **A.** Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** **Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 78. In a **GitHub Project `Table`** view grouped by `Priority` with a `Number` field called `Effort Days`, which built-in column summary option (`____`) totals effort days per group header automatically?

- **A.** Project custom fields (`Single select`, `Number`, `Date`, `Text`, and **`Iteration`** sprints with automatic break capacities) plus filter/sort/group view configurations (`slice by`)
- **B.** Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields
- **C.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **D.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)

---

## Domain 6 — Understand privacy, security, and administration (10–15% official weight · 14 questions)

### 79. Because GitHub requires **`2FA`** for maintainers and contributors publishing widely depended-upon open-source code, a maintainer hardens their personal account against credential stuffing and phishing. Which four-step sequence applies?

- **A.** Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication
- **B.** Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility
- **C.** Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in
- **D.** Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes

### 80. Supply-chain attackers target open-source package maintainers with fake login domains (`g1thub-login.com`). Which two security practices prevent account takeover AND permanent lockout? Select two.

- **A.** Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**
- **B.** Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **E.** Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout

### 81. Under personal `Settings -> Security log`, what can an individual GitHub user audit if they suspect unusual activity on their account?

- **A.** **Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in
- **B.** **Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes

### 82. An open-source project welcomes 5 enthusiastic community members to help label incoming bug reports, close duplicates, and convert questions to Discussions—**before** they have earned direct code push access. Which repository role was created specifically for open-source community triagers?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)

### 83. Senior co-maintainers of `pyhelios/core` need to configure branch protection, manage Topics, and push releases, **without** holding the power to delete `pyhelios/core` or transfer it away from the `@pyhelios` Organization. Which role fits?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

### 84. In an open-source GitHub Organization facing occasional internet trolls across 30 public repositories, which specialized Organization role (`____`) lets designated community stewards block abusive users and hide disruptive comments across org repos without holding `Organization Owner`?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** `LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code
- **C.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues
- **D.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**

### 85. A global software sponsor employs 2,000 corporate engineers using **Enterprise Managed Users (`EMUs`)** for internal IP while governing **GitHub Copilot** centrally. Which two rules apply? Select two.

- **A.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **B.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **C.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails
- **D.** Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability
- **E.** Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists

### 86. An engineer logged into their corporate **Enterprise Managed User (`EMU`)** account (`priya_corp`) tries to fork `pyhelios/core` (`a public open-source repo on github.com`) and submit an external Pull Request directly from `priya_corp`. Proposed solution: Submit the upstream open-source Pull Request using the `priya_corp` EMU account. Will GitHub permit `priya_corp` to push or open PRs on external public repositories?

- **A.** No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.
- **B.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **C.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 87. When an organization admin configures **MCP server policies** under GitHub Enterprise / Organization Copilot settings, why is explicit admin governance over external MCP registries important?

- **A.** **Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability
- **B.** Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases
- **C.** Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 88. Maintainers configure a **Repository Ruleset** protecting `main` and release tags (`v*`) on `pyhelios/core` (`available free on public repositories!`). Which three rules safeguard open-source releases? Select three.

- **A.** Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`
- **D.** Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges
- **F.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license

### 89. Compare all three GitHub repository visibility levels: **`Public`**, **`Internal`**, and **`Private`**. Which exact audience can read each level?

- **A.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **B.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **C.** Repository visibility levels: **`Public`** (open internet), **`Private`** (explicit users/teams only), and **`Internal`** (GitHub Enterprise only — readable by all enterprise members for **InnerSource**)
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 90. An open-source maintainer creates a tag ruleset matching `refs/tags/beta-*`, leaving release tags `refs/tags/v*` unmatched, and expects contributors with `Write` access to be blocked from deleting `v2.4.0`. Proposed solution: Leave `refs/tags/v*` outside any tag protection / Repository Ruleset target pattern. Does the solution protect `v2.4.0` from deletion?

- **A.** Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.
- **B.** No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.
- **C.** No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.
- **D.** No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.

### 91. When someone requests a review from `@pyhelios/optics-maintainers` (`a GitHub Team of 8 busy maintainers`), which Team setting automatically picks **2** maintainers via **`Round robin`** or **`Load balance`** instead of notifying all 8 every time?

- **A.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **B.** Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships
- **C.** **Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 92. During a heated Reddit/Hacker News viral spike on a public repository, maintainers want to temporarily block brand-new <24-hour-old GitHub accounts from spamming Issues for 24 hours. Which built-in repository/organization moderation feature enforces this?

- **A.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **B.** Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**
- **C.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists
- **D.** Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues

---

## Domain 7 — Explore the GitHub community (5–10% official weight · 8 questions)

### 93. When an open-source project adds `.github/____.yml` (referencing `github: [pyhelios]` or `open_collective: pyhelios`), what appears in the repository's sidebar and header on GitHub.com?

- **A.** **GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions

### 94. Which enterprise-grade GitHub security and CI capabilities does GitHub provide completely **free (`$0`)** on **public open-source repositories** to strengthen the global software supply chain?

- **A.** GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)
- **B.** GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically
- **C.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **D.** Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists

### 95. Where on `github.com` (`https://github.com/____` and `https://github.com/trending`) can developers discover rising open-source repositories filtered by programming language and daily/weekly/monthly momentum?

- **A.** **Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions
- **B.** Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)
- **C.** **Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment
- **D.** Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails

### 96. On **GitHub Marketplace**, what does the **`Verified creator`** checkmark badge next to an Action or App publisher (`such as aws-actions/configure-aws-credentials`) indicate?

- **A.** **Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses
- **B.** **GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts
- **C.** Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically
- **D.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes

### 97. A global enterprise learns from open-source communities like `PyHelios` and launches an internal **InnerSource** program across 25 countries. Which two open-source mechanisms translate directly into InnerSource? Select two.

- **A.** Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files
- **B.** Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**
- **C.** Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them
- **E.** Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges

### 98. Why does **asynchronous written communication** (`recording architectural context in Issues, Discussions, ADR Markdown docs, and Pull Requests` rather than unrecorded hallway chats) form a core pillar of both Open Source and **InnerSource**?

- **A.** **InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary
- **B.** Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license
- **C.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **D.** Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them

### 99. A doctoral student contributes a performance optimization to `pyhelios/core` (`where they do not hold Write access`). Which four-step open-source workflow applies?

- **A.** Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream
- **B.** Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge
- **C.** Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights
- **D.** Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor

### 100. Why should you ALWAYS create a dedicated **topic branch** (`fix/fft-overflow`) inside your personal **Fork** rather than committing your open-source patch directly onto your fork's **`main`** branch?

- **A.** **GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes
- **B.** Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only
- **C.** Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability
- **D.** No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.

---

## Answer Key and Explanations

### Question 1 — `B, C` (Understand Git and GitHub basics)

Correct answers: B and C (are correct). Every contributor works against a full local Git repository history, and attributed commit SHAs allow maintainers to audit authorship (`git blame`) and cleanly `git revert` regressions. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. Commit metadata provides line-by-line accountability and clean rollback via `git revert`.
- **C:** Correct. Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 2 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Branching, staging, committing, diffing, viewing history, and merging local branches all work **100% offline**; only network sync operations (`git fetch`, `git pull`, `git push`) wait until landing! [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **B:** Correct. Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.

### Question 3 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Passing `-s` (`--signoff`, distinct from uppercase `-S` cryptographic GPG/SSH signing!) appends a `Signed-off-by:` trailer line required by DCO bots. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 4 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `git blame src/fft.py` attributes every line of a file to the exact commit SHA and author who last changed it. [Skill 1.1: Describe the purpose and benefits of version control | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About version control and Git (https://docs.github.com/en/get-started/using-git/about-git)]

- **A:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **D:** Correct. Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.

### Question 5 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Commit SHAs belong to the portable **Git** object model, whereas Issues, Pull Requests, Discussions, Projects, and Actions are **GitHub** cloud collaboration services layered around Git. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **B:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 6 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `.git/config` inside the repository's `.git` directory stores repository-scoped Git configuration (`while ~/.gitconfig stores user-global Git settings`). [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **B:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 7 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Yes — **GitHub CLI (`gh`)** brings Pull Request creation, review, CI status checks (`gh pr checks`), and Issue triage straight into the command line. [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **B:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **C:** Correct. The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.
- **D:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).

### Question 8 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). No — anonymous `git clone` over HTTPS works on any `Public` GitHub repository using standard `git` without signing in (authentication is only required to push or interact with GitHub features). [Skill 1.2: Explain the difference between Git and GitHub | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to Git and GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/introduction-to-github/)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Correct. Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.

### Question 9 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). Edit `optics.py` in the working directory, stage it with `git add`, create a local snapshot with `git commit -m`, and upload commits with `git push`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Committing before editing and staging captures nothing from the intended file modifications.
- **B:** Incorrect. `git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.
- **C:** Incorrect. Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.
- **D:** Correct. Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).

### Question 10 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). `git status` lists `examples/demo.py` under **`Untracked files`** until you explicitly stage it into the index via `git add`. [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **D:** Correct. Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).

### Question 11 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Running `git commit --amend` rewrites the tip commit on your local branch (`safe before pushing; avoid amending already-shared public commits`). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.

### Question 12 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). A Git branch is simply a **41-byte file containing a 40-character commit SHA pointer** (`plus newline`)—Git never duplicates working files when creating a branch! [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **C:** Correct. Git branches are lightweight commit pointers rather than full folder copies, letting teams develop features safely without destabilizing `main`.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 13 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Running `git fetch upstream` downloads new commits from the canonical upstream repository into `upstream/main` safely (or select **`Sync fork`** in the GitHub web UI!). [Skill 1.3: Identify key Git concepts such as repositories, commits, and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub glossary: repositories, commits, and branches (https://docs.github.com/en/get-started/learning-about-github/github-glossary)]

- **A:** Correct. Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.
- **B:** Incorrect. Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.
- **C:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 14 — `B, C` (Understand Git and GitHub basics)

Correct answers: B and C (are correct). **GitHub Organizations** manage project repositories, maintainer Teams, and community roles, while a **GitHub Enterprise** account unifies multi-organization policies and administration. [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.
- **B:** Correct. Enterprise accounts unify security, identity, and policy governance across multiple organizations.
- **C:** Correct. Organizations centralize multi-developer ownership and team-based RBAC.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **E:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 15 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). It visualizes daily open-source/repository contributions—commits to default/`gh-pages` branches, opened Issues, Discussions, Pull Requests, and submitted PR reviews! [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 16 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). A **GitHub Organization** supports multiple co-equal **Organization Owners**, maintainer **Teams** (`@pyhelios/triagers`), `CODEOWNERS` teams, and Organization Projects—eliminating single-person bus-factor bottlenecks! [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 17 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). GitHub **automatically redirects** both web traffic and Git (`HTTPS`/`SSH`) requests from the old URL to the new repository location (`as long as @founder-alice doesn't create a new repo with that old name`)! [Skill 1.4: Describe GitHub accounts, organizations, and enterprise options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Types of GitHub accounts and GitHub plans (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Correct. An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.
- **D:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.

### Question 18 — `C` (Understand Git and GitHub basics)

Correct answer: C (is correct). Create a descriptive branch from `main`, commit changes and open a Pull Request, complete maintainer review and automated CI checks, then merge into `main` and delete the branch. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.
- **B:** Incorrect. Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.
- **C:** Correct. GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.
- **D:** Incorrect. GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.

### Question 19 — `A, B` (Understand Git and GitHub basics)

Correct answers: A and B (are correct). Short-lived topic branches isolate work cleanly off `main`, and asynchronous Pull Request diffs + automated CI checks let maintainers review safely from any time zone. [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Correct. Pull Requests combine asynchronous peer review and automated CI verification prior to merging.
- **B:** Correct. GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).

### Question 20 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). Yes — `on: pull_request` GitHub Actions workflows run automatically on Draft Pull Requests so authors get early CI feedback without pinging Code Owners prematurely! [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 21 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Selecting **`Sync fork` -> `Update branch`** on GitHub.com brings your fork's branch up to date with upstream without needing command-line `git fetch upstream`! [Skill 1.5: Explain the GitHub Flow for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub flow collaborative branching workflow (https://docs.github.com/en/get-started/using-github/github-flow)]

- **A:** Correct. When two branches modify the same lines differently, Git inserts standard conflict markers that must be edited out, staged, and committed (or resolved in GitHub’s web conflict editor).
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 22 — `A, B, E` (Understand Git and GitHub basics)

Correct answers: A, B, and E (are correct). `- [ ]` task lists, `> [!TIP]` / `> [!NOTE]` callout alerts, and ```` ```mermaid ```` diagram blocks. [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.
- **B:** Correct. GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.
- **C:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **E:** Correct. Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.
- **F:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.

### Question 23 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). Using a `<picture>` element with `<source media="(prefers-color-scheme: dark)" srcset="...">` renders theme-aware Dark/Light images cleanly in GitHub Flavored Markdown! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 24 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). GitHub automatically unfurls same-GitHub code permalink URLs into an **embedded syntax-highlighted code snippet preview** directly inside the Issue or Pull Request! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Correct. GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 25 — `D` (Understand Git and GitHub basics)

Correct answer: D (is correct). GFM supports native Markdown **footnotes** using `[^1]` inline markers paired with `[^1]: Footnote text` definitions rendered automatically at the bottom of the page! [Skill 1.6: Identify uses of Markdown for clear communication in issues and pull requests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Basic writing and formatting syntax in GitHub Flavored Markdown (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **C:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Correct. GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.

### Question 26 — `A` (Understand Git and GitHub basics)

Correct answer: A (is correct). **GitHub Desktop** provides an approachable, free GUI for Windows and macOS tailored to Git and GitHub workflows. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Correct. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.

### Question 27 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). **GitHub Mobile** (`iOS` and `Android`) supports full Issue triage, Discussions replies, Pull Request reviews, and Notifications on the go. [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.
- **B:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.
- **D:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 28 — `B` (Understand Git and GitHub basics)

Correct answer: B (is correct). GitHub Mobile lets you browse full repository `README.md` docs, source trees, commits, Releases, Issues, Pull Requests, Discussions, and Actions runs! [Skill 1.7: Recognize when to use GitHub Desktop and GitHub Mobile | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Desktop and GitHub Mobile overview (https://docs.github.com/en/desktop/overview/about-github-desktop)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Correct. GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.

### Question 29 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Add `.github/CODEOWNERS` mapping `/src/cuda/** @pyhelios/cuda-maintainers`, merge it into `main`, enable branch protection/rulesets requiring PR reviews, and enable `Require review from Code Owners`. [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. `README.md` does not trigger automatic review requests or merge enforcement.
- **B:** Incorrect. GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.
- **C:** Incorrect. Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.
- **D:** Correct. `CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.

### Question 30 — `B, E` (Work with GitHub repositories)

Correct answers: B and E (are correct). `CODEOWNERS` must reside in `.github/`, root, or `docs/`, and branch protection or Repository Rulesets must require Pull Requests + **Code Owner** review to block unapproved merges! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **B:** Correct. GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **E:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.

### Question 31 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). **`MIT`** allows reuse in proprietary closed-source software provided copyright/license notices are kept, whereas **`GPLv3`** requires distributed derivative works to also be licensed and shared under `GPLv3`! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).

### Question 32 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). GitHub displays a helpful banner above the New Issue / New Pull Request composer linking first-time contributors directly to **`Contributing guidelines`** and the **`Code of Conduct`**! [Skill 2.1: Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files (https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)]

- **A:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Correct. GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.

### Question 33 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). No — Forking copies prior history and links all 80 student repos inside one fork network; enable **`Template repository`** so students select **`Use this template`** instead! [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — Forking copies prior history and links all 80 student repos inside one fork network; enable **`Template repository`** so students select **`Use this template`** instead!
- **B:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Correct. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 34 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). Configuring `git config --global core.excludesfile ~/.gitignore_global` ignores personal OS/editor artifacts (`.DS_Store`, `.idea/`) across every repository on your machine! [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. `.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.
- **C:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 35 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). GitHub **automatically retargets open Pull Requests**, updates draft releases/branch protection rules on that branch, and displays exact `git branch -m` local update commands to contributors! [Skill 2.2: Identify how to create, organize, and maintain repositories using templates and branches | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating a repository from a template and managing branches (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Correct. Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.
- **D:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 36 — `C` (Work with GitHub repositories)

Correct answer: C (is correct). **`Code` / `Blame` / `Raw` toggles let you switch from rendered `Preview` to syntax-highlighted Markdown source lines (`Code`) or plain unformatted text (`Raw`)! [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.
- **D:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.

### Question 37 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). GitHub's built-in **Code view / Symbols navigation** indexes definitions and references across the file and repository right in the browser without cloning! [Skill 2.3: Explain how to add and manage files within a repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Creating, moving, and managing files in a GitHub repository (https://docs.github.com/en/repositories/working-with-files/managing-files)]

- **A:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Correct. Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.

### Question 38 — `B, C` (Work with GitHub repositories)

Correct answers: B and C (are correct). The **Dependency graph** (`Insights -> Dependency graph -> Dependents` + package tracking) and **Dependabot alerts / security updates**. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Correct. The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.
- **C:** Correct. Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.
- **D:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 39 — `A` (Work with GitHub repositories)

Correct answer: A (is correct). Because automated CI pipelines may clone or fetch the repo thousands of times per day; **`Unique cloners`** and **`Unique visitors`** measure distinct human/machine reach over the rolling 14-day window. [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Correct. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **B:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.

### Question 40 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Starring bookmarks repositories (and organizes them into **Lists**) with **zero inbox notification flood**, whereas `Watch -> All Activity` subscribes to every Issue, PR, and comment! [Skill 2.4: Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing repository graphs, stars, feature preview, and dependency insights (https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)]

- **A:** Incorrect. Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.
- **B:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.

### Question 41 — `D` (Work with GitHub repositories)

Correct answer: D (is correct). Deleting breaks downstream builds, documentation links, and citations—whereas **Archiving** freezes the repository safely as read-only while keeping the `owner/repo` namespace and releases intact! [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **D:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.

### Question 42 — `B` (Work with GitHub repositories)

Correct answer: B (is correct). GitHub users (and Organizations) can pin up to **6** repositories or Gists on their profile overview! [Skill 2.5: Recognize best practices for repository maintenance and collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Best practices for repositories and archiving repositories (https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Correct. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 43 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Insert a ```` ```suggestion ```` fenced block inside the inline review comment so the contributor (or maintainer) can apply it directly via **`Commit suggestion`** (or batch multiple suggestions in `Files changed` -> `Add suggestion to batch`)! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **B:** Incorrect. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 44 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). GitHub highlights the accepted answer right below the top question with a green **`Answered`** badge so readers don't have to dig through 50 replies! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Correct. Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.
- **C:** Incorrect. Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 45 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). Repository maintainers (`Triage`+) can **Lock conversation** on an Issue, Pull Request, or Discussion (temporarily or permanently) to stop unproductive comments cleanly. [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.

### Question 46 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Select **`Pin issue`** in the right sidebar of up to **3** Issues per repository so contributors see them immediately before filing duplicates! [Skill 3.1: Describe how to use issues, pull requests, and discussions for collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Communicating on GitHub with Issues, Pull Requests, and Discussions (https://docs.github.com/en/get-started/quickstart/communicating-on-github)]

- **A:** Correct. Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.
- **B:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **C:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **D:** Incorrect. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).

### Question 47 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). Triage/confirm Issue `#42`, commit the fix on a fork topic branch, open a Pull Request referencing `Fixes #42` targeting `pyhelios:main`, and merge the approved PR into `main`. [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Correct. Including a closing keyword (`Closes #42`, `Fixes #42`, `Resolves #42`) in a Pull Request targeting the default branch automatically closes Issue `#42` upon merge.
- **B:** Incorrect. Only supported closing keywords merged into the default branch (or explicitly linked PRs) close an issue automatically.
- **C:** Incorrect. Closing the issue prematurely loses active tracking, and wiki edits or Discussions do not merge code changes.
- **D:** Incorrect. Gists are separate repositories and cannot auto-close repository Issues via closing keywords.

### Question 48 — `C, D` (Collaborate using GitHub)

Correct answers: C and D (are correct). Write `Fixes pyhelios/core#19` (`owner/repo#number` closing keyword) in the PR description targeting the default branch, or link `pyhelios/core#19` in the PR's **`Development`** sidebar! [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Manual `Development` sidebar links work across branches and display clear traceability on both timelines.
- **D:** Correct. Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 49 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). YAML Issue Forms render native browser UI fields (`input`, `textarea`, `dropdown`, `checkboxes`) with **`required: true` client validation**, stopping contributors from deleting template sections and submitting empty bug reports! [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.
- **D:** Incorrect. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.

### Question 50 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Adding **`no:assignee`** excludes Issues that already have someone assigned so newcomers pick genuinely unclaimed tasks! [Skill 3.2: Explain how to link pull requests to issues and manage templates, filters, and assignments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Linking a pull request to an issue and configuring issue/PR templates (https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.

### Question 51 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Open **`Watch -> Custom`**, check **`Releases`** alone, and select Apply! [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 52 — `D` (Collaborate using GitHub)

Correct answer: D (is correct). Mark completed threads **`Done`** (`e` shortcut) so they archive out of the active inbox while auto-resurfacing only if new activity arrives (and configure notification schedule/email pause settings in `Settings -> Notifications`)! [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.

### Question 53 — `B` (Collaborate using GitHub)

Correct answer: B (is correct). GitHub parses valid email replies and posts your message directly as a **new Markdown comment** on that Issue, Pull Request, or Discussion thread (remind users to strip confidential email footers!). [Skill 3.3: Identify the purpose of notifications and how to configure them for workflow management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring notifications and managing subscriptions on GitHub (https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)]

- **A:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **B:** Correct. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).

### Question 54 — `A, D` (Collaborate using GitHub)

Correct answers: A and D (are correct). **GitHub Pages** (with free custom domain + Let's Encrypt HTTPS support) and **GitHub Discussions**. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Correct. GitHub Pages renders repository docs into browsable websites with HTTPS.
- **B:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **C:** Incorrect. Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.
- **D:** Correct. Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.
- **E:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 55 — `C` (Collaborate using GitHub)

Correct answer: C (is correct). GitHub Pages stores custom domain configuration via a `CNAME` record/setting in `Settings -> Pages` and automatically provisions a free Let's Encrypt TLS certificate when **`Enforce HTTPS`** is checked. [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).
- **D:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).

### Question 56 — `A` (Collaborate using GitHub)

Correct answer: A (is correct). No — **Secret Gists** are publicly accessible to anyone with the URL without authentication; store truly private files inside a **`Private` GitHub repository** instead! [Skill 3.4: Describe how to use Gists, Wikis, and GitHub Pages to document and share information | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Sharing content with Gists, Wikis, and GitHub Pages (https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)]

- **A:** Correct. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Secret Gists** are publicly accessible to anyone with the URL without authentication; store truly private files inside a **`Private` GitHub repository** instead!
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).

### Question 57 — `D` (Apply modern development practices)

Correct answer: D (is correct). Create `.github/workflows/ci.yml`, configure `on: [push, pull_request]`, define `jobs` with `runs-on: ubuntu-latest` and `pytest` `steps`, and commit `ci.yml` to monitor runs in `Actions`. [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. Workflow YAML files outside `.github/workflows/` are ignored by GitHub Actions, and `on:` plus `runs-on:` are required keys.
- **B:** Incorrect. `github.dev` has no compute terminal to execute `npm test` or report Pull Request status checks.
- **C:** Incorrect. Issue templates structure bug reports and never provision Actions runners or run unit tests.
- **D:** Correct. GitHub Actions workflows live as YAML files in `.github/workflows/`, trigger on defined events, execute job steps on specified runners, and report status in the `Actions` tab.

### Question 58 — `A, B` (Apply modern development practices)

Correct answers: A and B (are correct). Workflows live in `.github/workflows/*.yml` running isolated `jobs:`/`steps:` on ephemeral `runs-on:` VMs (and for public fork PRs, GitHub strips repository secrets and gates first-time contributors behind maintainer **`Approve and run`**!). [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Correct. GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.
- **B:** Correct. Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 59 — `D` (Apply modern development practices)

Correct answer: D (is correct). Because any internet user can fork a public repo and modify scripts in a PR—withholding encrypted secrets (and passing a `Read-only` `GITHUB_TOKEN`) stops malicious PRs from stealing `PYPI_API_TOKEN` credentials! [Skill 4.1: Describe the purpose and capabilities of GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Understanding GitHub Actions workflows, events, jobs, and runners (https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **D:** Correct. GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.

### Question 60 — `A, C, D` (Apply modern development practices)

Correct answers: A, C, and D (are correct). Assigning Issues to **Copilot coding agent** for draft PRs, running **IDE Agent Mode** for multi-file local edits + `pytest` terminal loops, and switching models via **multi-model support**. [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Correct. Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Correct. Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.
- **D:** Correct. IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.
- **E:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **F:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 61 — `D` (Apply modern development practices)

Correct answer: D (is correct). Add **`.github/copilot-instructions.md`** (plus path-scoped `.github/instructions/*.instructions.md` files) so Copilot coding agent and IDE Agent Mode follow exact project conventions! [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **C:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **D:** Correct. The January 2026 GH-900 blueprint distinguishes asynchronous **Copilot coding agent** on GitHub (assigned to Issues, opening PRs) from synchronous local **Agent Mode** inside your IDE, plus **MCP** servers and custom agents.

### Question 62 — `B` (Apply modern development practices)

Correct answer: B (is correct). Copilot explains complex shell commands in plain English and translates natural-language tasks (*"find all `.py` files modified in the last 3 days"*) into ready-to-review shell commands! [Skill 4.2: Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support (https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.
- **C:** Incorrect. `SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.
- **D:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 63 — `A` (Apply modern development practices)

Correct answer: A (is correct). Verified students, faculty, and eligible maintainers of popular public open-source projects receive complimentary access to **GitHub Copilot Pro** (`$0`)! [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.

### Question 64 — `C` (Apply modern development practices)

Correct answer: C (is correct). **GitHub Copilot Pro+** (`$39/month` for individuals) provides higher premium request allowances and expanded access across available frontier models for individual accounts. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **C:** Correct. Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 65 — `C` (Apply modern development practices)

Correct answer: C (is correct). Different models excel at distinct engineering workloads—fast lightweight models handle quick boilerplate/autocomplete, while deep reasoning models tackle complex multi-file architecture debugging. [Skill 4.3: Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise) (https://docs.github.com/en/copilot/get-started/plans)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Correct. Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.
- **D:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.

### Question 66 — `A` (Apply modern development practices)

Correct answer: A (is correct). Commit `.devcontainer/devcontainer.json` (plus optional **Codespaces Prebuilds**) and add an **`Open in GitHub Codespaces`** badge to `README.md`! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **B:** Incorrect. `github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.
- **C:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 67 — `D` (Apply modern development practices)

Correct answer: D (is correct). Yes — GitHub includes a monthly free allowance of Codespaces compute hours (`e.g., 120 core-hours on Free, 180 on Pro`) and storage (`15–20 GB`) for personal accounts, with spending limits defaulted safely to `$0` until raised! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.
- **B:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **C:** Incorrect. Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).
- **D:** Correct. Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.

### Question 68 — `B` (Apply modern development practices)

Correct answer: B (is correct). Prebuilds pre-assemble the container image, cloned repo, and `onCreate`/`updateContent` dependencies ahead of time so new Codespaces boot in seconds rather than waiting minutes to build! [Skill 4.4: Describe GitHub Codespaces and how to set up, customize, and use dev containers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: GitHub Codespaces overview and devcontainer.json configuration (https://docs.github.com/en/codespaces/overview)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.
- **C:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **D:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.

### Question 69 — `B, D` (Apply modern development practices)

Correct answers: B and D (are correct). Press `.` to open **`github.dev`** for instant zero-compute multi-file Markdown translation commits, and launch **GitHub Codespaces** for Cython compilation and `pytest` execution. [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Correct. Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Correct. `github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.
- **E:** Incorrect. `github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.

### Question 70 — `A` (Apply modern development practices)

Correct answer: A (is correct). No — `github.dev` has no backing compute VM or Python runtime (`selecting the Terminal panel explicitly prompts you to Continue Working on GitHub Codespaces`!). [Skill 4.5: Explain when to use the github.dev editor and how it differs from Codespaces | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: The github.dev web-based editor vs GitHub Codespaces (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)]

- **A:** Correct. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — `github.dev` has no backing compute VM or Python runtime (`selecting the Terminal panel explicitly prompts you to Continue Working on GitHub Codespaces`!).
- **C:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 71 — `C, E` (Manage projects with GitHub)

Correct answers: C and E (are correct). Publish `Table`, `Board`, and `Roadmap` views grouped by Milestone/`Iteration`, and automate card transitions via **Project workflows** plus **Project Insights**. [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Correct. GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.
- **D:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **E:** Correct. Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.

### Question 72 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Add a **`Draft issue`** directly inside the GitHub Project—it stays scoped inside the Project until a maintainer selects **`Convert to issue`** and picks a target repository! [Skill 5.1: Describe GitHub Projects and layout options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Projects and Table, Board, and Roadmap layout views (https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Correct. A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.
- **C:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **D:** Incorrect. GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).

### Question 73 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). Create the Organization Project with custom `Iteration` and `Priority` fields, add repository Issues/PRs, enable built-in `Item closed -> Done` workflows, and monitor Project Insights burn-up charts. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.
- **B:** Correct. GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.
- **C:** Incorrect. Gists do not host Milestones or drive organization GitHub Projects automations.
- **D:** Incorrect. `SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.

### Question 74 — `B` (Manage projects with GitHub)

Correct answer: B (is correct). GitHub calculates Milestone progress directly from the ratio of **closed** Issues and Pull Requests (`30 closed`) to **total** Issues and Pull Requests (`40 total`) assigned to that Milestone. [Skill 5.2: Explain how to configure projects, labels, milestones, and workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Managing custom fields, iterations, labels, milestones, and built-in workflows (https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)]

- **A:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **B:** Correct. Labels classify type/priority, Milestones measure progress toward a release goal inside a repository, and built-in Project workflows eliminate manual card dragging.
- **C:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 75 — `D` (Manage projects with GitHub)

Correct answer: D (is correct). No — **Saved replies** are strictly **per-user personal account** settings (`not shared across repository collaborators or organization members`)! [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.
- **B:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **Saved replies** are strictly **per-user personal account** settings (`not shared across repository collaborators or organization members`)!
- **D:** Correct. Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.

### Question 76 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). Setting `Assignees`, `Labels`, or `Milestones` directly requires at least **`Triage`** access (many open-source repos therefore run a lightweight GitHub Action allowing `/assign` comment commands for contributors!). [Skill 5.3: Identify how to use saved replies and assignees to streamline communication | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Using saved replies and assigning issues and pull requests (https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Correct. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 77 — `C` (Manage projects with GitHub)

Correct answer: C (is correct). **Repository `Insights`** measures code/commit/traffic/dependency activity inside **one repository**, whereas **GitHub Projects `Insights`** charts planning fields (`Status`, `Iteration`, `Story Points`) across items in a **Project**! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Incorrect. Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Correct. Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 78 — `A` (Manage projects with GitHub)

Correct answer: A (is correct). Configuring column aggregation (**`Sum`** — alongside `Count`, `Average`, `Min`, or `Max`) displays rolled-up totals right on each group header! [Skill 5.4: Describe how project insights can be used to track progress and productivity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Viewing insights and custom charts in GitHub Projects (https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)]

- **A:** Correct. `Iteration` fields track time-boxed sprints directly inside GitHub Projects without external agile plugins.
- **B:** Incorrect. Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.
- **C:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **D:** Incorrect. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.

### Question 79 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Open-source maintainers turn on `2FA` first, store one-time recovery codes safely against device loss, register an origin-bound WebAuthn passkey, and confirm phishing-resistant sign-in. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Incorrect. GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.
- **B:** Incorrect. Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.
- **C:** Correct. Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.
- **D:** Incorrect. Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.

### Question 80 — `A, E` (Understand privacy, security, and administration)

Correct answers: A and E (are correct). Use origin-bound WebAuthn **Passkeys** / hardware FIDO2 keys (which refuse to sign challenges on spoofed domains!), and store offline **`2FA` recovery codes** in a password manager. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Correct. Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.
- **B:** Incorrect. Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **E:** Correct. Recovery codes are essential to regain account access if a phone or hardware key is lost.

### Question 81 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). The personal **Security log** records recent authentication events, IP/country metadata, PAT/SSH key additions, `2FA` updates, and repository permission changes for your account. [Skill 6.1: Describe how to secure accounts with two-factor authentication (2FA) and passkeys | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Configuring two-factor authentication (2FA) and passkeys on GitHub (https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)]

- **A:** Correct. Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.
- **B:** Incorrect. Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.

### Question 82 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). The **`Triage`** repository role lets trusted community helpers manage Issues, Pull Request labels, and Discussions without granting `Write` push access to code! [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.

### Question 83 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Assign the **`Maintain`** repository role (`manage repository configuration without destructive Admin or collaborator-grant actions`). [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 84 — `D` (Understand privacy, security, and administration)

Correct answer: D (is correct). The **`Moderator`** organization role empowers Code of Conduct stewards to block/unblock users, manage interaction limits, and minimize abusive comments across public org repositories! [Skill 6.2: Identify access permissions and roles for repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Repository roles and organization roles for access management (https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.
- **C:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.
- **D:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.

### Question 85 — `D, E` (Understand privacy, security, and administration)

Correct answers: D and E (are correct). Corporate **EMUs** are provisioned via IdP/SCIM and blocked from creating public repos or pushing to external OSS repos (`engineers use separate personal accounts for approved OSS work`), while admins govern Copilot policies centrally. [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **B:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **C:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.
- **D:** Correct. Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.
- **E:** Correct. EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.

### Question 86 — `A` (Understand privacy, security, and administration)

Correct answer: A (is correct). No — **EMU** accounts can contribute only to repositories **inside** their own enterprise (`read-only viewing of public github.com repos if using github.com EMUs; zero external forks/PRs`); use a separate personal GitHub account per company OSPO policy! [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Correct. By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.
- **B:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — **EMU** accounts can contribute only to repositories **inside** their own enterprise (`read-only viewing of public github.com repos if using github.com EMUs; zero external forks/PRs`); use a separate personal GitHub account per company OSPO policy!
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 87 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Because MCP servers grant AI agents access to external tools, APIs, and data sources—centralized MCP policies ensure agents connect only to vetted, trusted tool servers! [Skill 6.3: Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About Enterprise Managed Users (EMUs) and organization Copilot policy management (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users)]

- **A:** Incorrect. Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.
- **B:** Incorrect. Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.
- **C:** Correct. Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 88 — `A, C, D` (Understand privacy, security, and administration)

Correct answers: A, C, and D (are correct). Require Pull Requests with approvals + **Code Owner** review, require passing CI **status checks**, and block **force-pushes** plus deletions on `main` and `v*` release tags! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Correct. Blocking force-pushes and deletions protects commit history integrity on production branches.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Correct. Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.
- **D:** Correct. Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.
- **F:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!

### Question 89 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). `Public` = everyone on the internet; `Internal` = all members across a **GitHub Enterprise** (`InnerSource`); `Private` = only explicitly granted users and Teams! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **B:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **C:** Correct. `Internal` visibility exists specifically in GitHub Enterprise organizations so all employees across sibling orgs can discover and fork repositories (`InnerSource`) without making code `Public`.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 90 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). No — a Repository Ruleset protects only branches/tags matching its configured target ref patterns (`add refs/tags/v* and block deletions/updates to make release tags immutable`)! [Skill 6.4: Describe repository privacy options, visibility settings, and branch protection rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Setting repository visibility, branch protection rules, and rulesets (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub workflow, security, or collaboration requirement. No — a Repository Ruleset protects only branches/tags matching its configured target ref patterns (`add refs/tags/v* and block deletions/updates to make release tags immutable`)!
- **B:** Correct. `CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.
- **C:** Incorrect. `github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).
- **D:** Incorrect. Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.

### Question 91 — `C` (Understand privacy, security, and administration)

Correct answer: C (is correct). Enabling **Team code review assignment** (`Auto assignment` using `Round robin` rotation or `Load balance` active-review weighting) distributes review load fairly across maintainers! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **B:** Incorrect. Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.
- **C:** Correct. Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 92 — `B` (Understand privacy, security, and administration)

Correct answer: B (is correct). **Temporary interaction limits** (`Limit to existing users`, `Limit to prior contributors`, or `Limit to repository collaborators` for 24 hours up to 6 months) throttle spam bursts immediately! [Skill 6.5: Recognize how to manage organization settings, teams, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Organizing members into nested teams and managing organization settings (https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)]

- **A:** Incorrect. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **B:** Correct. Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.
- **C:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.
- **D:** Incorrect. Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.

### Question 93 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Committing `.github/FUNDING.yml` enables the pink heart **`Sponsor`** button on the repository linking contributors and companies directly to your **GitHub Sponsors** profile or approved funding platforms! [Skill 7.1: Describe the benefits of open source and GitHub Sponsors | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Sponsors and open-source sustainability (https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)]

- **A:** Correct. Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.

### Question 94 — `A` (Explore the GitHub community)

Correct answer: A (is correct). **GitHub Actions** hosted runners, **GitHub Advanced Security** (`CodeQL` code scanning, **Secret scanning + Push protection**, Private Vulnerability Reporting), **Dependabot**, **Repository Rulesets**, and **GitHub Pages**! [Skill 7.2: Explain how GitHub supports and advances open-source projects | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Supporting open-source projects with community profiles and Security Lab / advisories (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)]

- **A:** Correct. GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.
- **B:** Incorrect. GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.
- **C:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **D:** Incorrect. Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.

### Question 95 — `C` (Explore the GitHub community)

Correct answer: C (is correct). **GitHub Explore** (`github.com/explore`) and **GitHub Trending** (`github.com/trending`) showcase trending repositories, curated collections, and active topics across the open-source ecosystem. [Skill 7.3: Identify how to follow users and organizations to stay informed about activity | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Following people and organizations on GitHub to track activity (https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)]

- **A:** Incorrect. EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.
- **B:** Incorrect. Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.
- **C:** Correct. Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.
- **D:** Incorrect. `Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.

### Question 96 — `B` (Explore the GitHub community)

Correct answer: B (is correct). GitHub has verified the identity and domain ownership of the partner organization publishing that Marketplace Action or GitHub App. [Skill 7.4: Describe the GitHub Marketplace and its purpose | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: About GitHub Marketplace for GitHub Apps and Actions (https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace)]

- **A:** Incorrect. Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.
- **B:** Correct. GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.
- **C:** Incorrect. GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).
- **D:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.

### Question 97 — `A, B` (Explore the GitHub community)

Correct answers: A and B (are correct). Transparent **`Internal`** Enterprise repositories equipped with `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS`, plus **Repository Topics** and asynchronous fork/branch Pull Request reviews. [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. `Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.
- **B:** Correct. Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.
- **C:** Incorrect. Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.
- **E:** Incorrect. Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.

### Question 98 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Written context in Issues, Discussions, and PRs lets engineers across global time zones and future hires understand *why* decisions were made and contribute self-servingly! [Skill 7.5: Explain how InnerSource applies open-source principles within organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Introduction to InnerSource practices on GitHub (Microsoft Learn) (https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/)]

- **A:** Correct. InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.
- **B:** Incorrect. Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!
- **C:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **D:** Incorrect. `Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.

### Question 99 — `A` (Explore the GitHub community)

Correct answer: A (is correct). Read `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`, fork `pyhelios/core` to their personal account and create a topic branch, commit and push the optimization to their fork, and open a Pull Request to `pyhelios:main`. [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Correct. External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.
- **B:** Incorrect. Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.
- **C:** Incorrect. Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.
- **D:** Incorrect. Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.

### Question 100 — `C` (Explore the GitHub community)

Correct answer: C (is correct). Keeping your fork's `main` branch clean lets you `Sync fork` cleanly with `upstream/main` anytime and work on **multiple independent Pull Requests simultaneously** without cross-contaminating branches! [Skill 7.6: Recognize when to use forks, templates, and discoverable repositories to promote collaboration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900 | Reference: Forking a repository vs templates and improving repository discoverability with topics (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)]

- **A:** Incorrect. Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.
- **B:** Incorrect. Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.
- **C:** Correct. Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.
- **D:** Incorrect. Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.
