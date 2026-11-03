"""Canonical option and distractor catalog for Exam GH-900: GitHub Foundations (6 x 100 = 600 questions).

Every entry maps `key -> (option_label, explanation_note)` with `len(option_label) <= 245`
and zero banned phrases or Microsoft/GitHub sample company names.
"""

from sequences import SEQUENCES

TERMS = {
    # --- Domain 1: Understand Git and GitHub basics ---
    'vcs_distributed_benefits': (
        'Distributed Version Control System (`DVCS`) preserving full commit history, offline branching, blame attribution, and safe rollback across every clone',
        'Git is a distributed VCS where every developer clone holds full repository history, enabling offline commits, lightweight branching, auditability, and instant revert of regressions.',
    ),
    'vcs_revert_audit_collab': (
        'Parallel team development with conflict detection, complete who/when/why commit audit trails, and non-destructive `git revert` recovery',
        'Version control lets multiple contributors work concurrently without overwriting files while tracking exact line authorship and safely reverting faulty changes.',
    ),
    'git_vs_github_core': (
        'Git is the open-source distributed version control CLI/engine tracking local snapshots; GitHub is the cloud collaboration platform hosting Git repositories plus PRs, Issues, Actions, and security governance',
        'Git runs locally (or on any server) to manage commits and branches, whereas GitHub adds cloud hosting, Pull Requests, Issues, Discussions, Actions CI/CD, Copilot, and enterprise access control.',
    ),
    'git_three_trees_staging': (
        'Working directory (modified files), Staging area / index (`git add`), and Local repository `.git` commit history (`git commit`)',
        'Git separates uncommitted edits in the working tree from staged changes in the index (`git add`) and permanent SHA-1/SHA-256 commit snapshots in `.git` (`git commit`).',
    ),
    'git_commit_sha_snapshot': (
        'A commit (`SHA` hash) records an immutable point-in-time snapshot of staged project changes, parent commit pointer(s), author metadata, and commit message',
        'Each Git commit uniquely hashes its tree state, parent commit(s), author/committer timestamps, and message so history tampering is cryptographically detectable.',
    ),
    'git_branch_pointer_isolation': (
        'A lightweight movable pointer to a commit that isolates feature or bugfix work from the default branch (`main`) until merged',
        'Git branches are lightweight commit pointers rather than full folder copies, letting teams develop features safely without destabilizing `main`.',
    ),
    'git_clone_fetch_pull_push': (
        '`git clone` copies a remote repo locally; `git fetch` downloads remote refs without merging; `git pull` fetches and integrates; `git push` uploads local commits',
        'Understanding `clone` (initial copy), `fetch` (safe download without workspace merge), `pull` (`fetch` + `merge`/rebase), and `push` (upload commits) is foundational to Git/GitHub sync.',
    ),
    'git_merge_conflict_markers': (
        'Resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in affected files, stage the clean file (`git add`), and complete the merge commit',
        'When two branches modify the same lines differently, Git inserts standard conflict markers that must be edited out, staged, and committed (or resolved in GitHub’s web conflict editor).',
    ),
    'acct_personal_user': (
        'Personal account (`Individual` — `GitHub Free` or `GitHub Pro`) representing one human identity across open-source and organization memberships',
        'Every person signs in to an individual personal account (except Enterprise Managed Users) and can be invited into multiple organizations.',
    ),
    'acct_organization_shared': (
        'Organization account (`GitHub Free`, `GitHub Team`, or `GitHub Enterprise`) providing shared repository ownership, nested teams, and role-based permissions',
        'Organizations decouple repository ownership from a single employee’s personal account and add team hierarchies, organization roles, and centralized billing/security.',
    ),
    'acct_enterprise_hec_ghes': (
        'GitHub Enterprise account (`Enterprise Cloud` SaaS on GitHub.com/GHE.com and self-hosted `Enterprise Server`) centrally governing multiple organizations, SAML/OIDC SSO, and billing',
        'An Enterprise account sits above multiple organizations to enforce unified SAML/OIDC SSO, Enterprise Managed Users, Copilot/Actions policies, audit logs, and consolidated licensing.',
    ),
    'github_flow_branch_pr': (
        'GitHub Flow: keep `main` always deployable, branch off `main`, open an early Pull Request for discussion and CI checks, merge after approval, and deploy',
        'GitHub Flow is a lightweight, branch-based workflow without complex long-lived `release`/`develop` trees, centered on short-lived branches and Pull Requests.',
    ),
    'github_flow_draft_pr': (
        'Open a **Draft Pull Request** early to share work-in-progress diffs, trigger CI feedback, and block accidental merging until marked `Ready for review`',
        'Draft Pull Requests signal that changes are still in progress and cannot be merged until the author marks the PR ready for review.',
    ),
    'md_task_lists_alerts': (
        'GitHub Flavored Markdown task lists (`- [ ]` / `- [x]`) and callout alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)',
        'GFM renders interactive checkable task items (`- [ ]`) that roll up progress in Issues/PRs and styled blockquote alerts (`> [!NOTE]`, etc.) for critical callouts.',
    ),
    'md_fenced_code_diff_mermaid': (
        'Triple-backtick fenced code blocks with language identifiers (```` ```python ````, ```` ```diff ````, ```` ```mermaid ````) for syntax highlighting and live diagrams',
        'Specifying a language tag after triple backticks highlights syntax—and `mermaid` renders flowcharts/sequence diagrams directly inside READMEs, Issues, and PRs.',
    ),
    'md_mentions_autolinks_slash': (
        '`@username` / `@org/team` mentions, `#123` Issue/PR autolinks, and `/` slash commands for inserting tables, task lists, and code blocks rapidly',
        'GFM autolinks `#issue` numbers, notifies `@mentions`, and supports `/` slash commands inside Issue/PR comment editors.',
    ),
    'client_github_desktop': (
        '**GitHub Desktop**: visual cross-platform GUI (`macOS`/`Windows`) for cloning, interactive line-level partial staging, visual diffs, branch switching, and conflict resolution without CLI memorization',
        'GitHub Desktop gives developers and non-developers an intuitive visual Git client for commits, cherry-picking, stashing, and PR creation on macOS and Windows.',
    ),
    'client_github_mobile': (
        '**GitHub Mobile** (`iOS`/`Android`): triage notifications, review diffs, approve/merge Pull Requests, comment on Issues/Discussions, and make quick single-file edits on the go',
        'GitHub Mobile focuses on rapid triage, mobile-friendly diff review, push notifications, 2FA sign-in verification, and lightweight unblocking while away from a workstation.',
    ),

    # --- Domain 2: Work with GitHub repositories ---
    'repo_file_readme': (
        '`README.md` (in repository root, `.github/`, or `docs/`): rendered automatically on the repository landing page to explain project purpose, setup, and usage',
        'GitHub automatically displays `README.md` below the file tree to onboard visitors and contributors (`root`, `.github/`, or `docs/`).',
    ),
    'repo_file_license': (
        '`LICENSE` (`LICENSE.md` / `LICENSE.txt`): defines exact legal permissions, conditions, and limitations for reusing, modifying, and distributing repository code',
        'Without an explicit `LICENSE` file, default copyright law reserves all rights—making public code legally unsafe for others to reuse as open source.',
    ),
    'repo_file_contributing_coc': (
        '`CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`: surface contributor workflow rules and behavioral standards automatically when someone opens an Issue or Pull Request',
        'GitHub links `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` directly in the new-Issue/new-PR composer to guide healthy contributions.',
    ),
    'repo_file_codeowners': (
        '`CODEOWNERS` (in `.github/`, root, or `docs/`): maps gitignore-style file patterns (e.g., `/infra/** @org/sre-team`) to auto-requested Pull Request reviewers',
        '`CODEOWNERS` automatically requests reviews from designated individuals or teams with write access whenever matching paths change in a Pull Request.',
    ),
    'repo_file_security_md': (
        '`SECURITY.md` (security policy): instructs researchers how to report vulnerabilities privately (including **Private Vulnerability Reporting**) instead of filing public Issues',
        '`SECURITY.md` appears in the repository `Security` tab so discoverers disclose security flaws responsibly rather than exposing zero-days publicly.',
    ),
    'repo_gitignore_gitattributes': (
        '`.gitignore` excludes untracked build artifacts/secrets (`node_modules/`, `.env`) from staging, while `.gitattributes` normalizes line endings (`LF`/`CRLF`) and Git LFS tracking',
        '`.gitignore` prevents untracked generated/sensitive files from being staged (already-tracked files require `git rm --cached`), while `.gitattributes` governs path attributes.',
    ),
    'repo_template_clean_history': (
        '**Template repository**: generates a brand-new repository copying directory structure and files (optionally all branches) with a **single clean initial commit** and no fork link',
        'Unlike forking, creating a repository from a template starts fresh commit history for scaffolding new microservices, docs sites, or starter kits.',
    ),
    'repo_default_branch_mgmt': (
        'Default branch (`main`) serves as the base target for new clones, Pull Requests, and `Closes #N` auto-closing keywords; stale merged branches can be auto-deleted via repository settings',
        'Enabling `Automatically delete head branches` keeps branch lists tidy after Pull Requests merge into the default branch.',
    ),
    'repo_web_file_ops': (
        'Web UI file management: `Add file -> Create new file` (typing `/` creates nested folders), drag/upload files (`<= 25 MB` browser / `100 MB` Git push limit; use **Git LFS** for large binaries), edit, rename, and view `Blame`/`History`',
        'Typing `docs/guide/intro.md` in GitHub’s web file creator automatically creates nested directories, while GitHub blocks pushes of single files exceeding `100 MB` without Git LFS.',
    ),
    'repo_insights_pulse_traffic': (
        'Repository **Insights** tab (`Pulse`, `Contributors`, `Traffic` 14-day clones/views, `Commits`, `Code frequency`, `Network`, `Forks`, and `Community Standards` checklist)',
        'Repository Insights visualizes recent merged/open PRs (`Pulse`), 14-day visitor/clone counts (`Traffic`), contributor velocity, and missing community health files.',
    ),
    'repo_stars_lists_previews': (
        '**Stars & Lists** bookmark repositories and signal community appreciation (without triggering full notification floods), while **Feature preview** lets users opt in early to upcoming GitHub UI capabilities',
        'Starring bookmarks a project (organizable into personal Lists) without subscribing to every Issue comment like `Watch -> All Activity` does; `Feature preview` toggles beta user features.',
    ),
    'repo_dependency_graph_insights': (
        '**Dependency graph** parses manifest/lockfiles (`package-lock.json`, `requirements.txt`), powering **Dependabot alerts** and Enterprise **Dependency insights** / SBOM export for license and CVE visibility',
        'Enabling the Dependency graph identifies direct/transitive packages, feeds Dependabot vulnerability alerts, and exports NTIA/SPDX Software Bills of Materials (`SBOM`).',
    ),
    'repo_archive_pin_topics': (
        '**Archive repository** to make a deprecated project strictly read-only while preserving historical code/PRs/stars, and add **Topics** + **Pinned repositories** for discoverability',
        'Archiving communicates clearly that a repository is unmaintained and read-only without breaking existing clones, links, or audit history.',
    ),

    # --- Domain 3: Collaborate using GitHub ---
    'collab_issues_tracking': (
        '**GitHub Issues**: track actionable bugs, feature requests, and tasks using labels, milestones, assignees, sub-issues/task lists, and Issue forms',
        'Issues capture discrete, trackable work items that link directly to Pull Requests and GitHub Projects.',
    ),
    'collab_pull_requests_review': (
        '**Pull Requests (`PRs`)**: propose branch changes with line-by-line diff comments, `Approve` / `Request changes` / `Comment` reviews, **Suggested changes** (```` ```suggestion ````), and merge strategies (`Merge commit`, `Squash`, `Rebase`)',
        'Pull Requests combine code review, inline commitable `suggestion` blocks, automated CI/security checks, and configurable merge methods.',
    ),
    'collab_discussions_forum': (
        '**GitHub Discussions**: threaded Q&A, RFC brainstorming, polls, and announcements outside the actionable bug backlog, with **`Mark as answer`** and one-action **`Create issue from discussion`**',
        'Discussions keep open-ended questions, polls, and community conversations separate from actionable Issues while allowing maintainers to promote validated ideas into Issues.',
    ),
    'collab_link_pr_keywords': (
        'Linking PRs to Issues via closing keywords (`Closes #15`, `Fixes #15`, `Resolves #15` — or `Closes org/repo#15`) in the PR body/commit targeting the default branch, or via the `Development` sidebar',
        'When a linked Pull Request merges into the default branch, GitHub automatically closes the referenced Issue and cross-references both timelines.',
    ),
    'collab_templates_yaml_forms': (
        '`.github/ISSUE_TEMPLATE/*.yml` **Issue Forms** (structured dropdowns, required inputs, auto-labels) plus `.github/pull_request_template.md` checklists',
        'YAML Issue Forms validate required reproduction fields at submission time, while `pull_request_template.md` pre-populates PR test/security checklists.',
    ),
    'collab_search_filters': (
        'Issue/PR filter qualifiers such as `is:open is:pr review:required`, `assignee:@me`, `label:"good first issue"`, `no:milestone`, and `author:octocat`',
        'GitHub’s search bar filters Issues and Pull Requests precisely by state, type, review status, label, milestone, author, and `@me` dynamic user tokens.',
    ),
    'collab_notifications_watch': (
        'Per-repository **Watch** levels (`Participating and @mentions`, `All Activity`, `Ignore`, or `Custom` for Releases/Security alerts only) plus Web/Email/Mobile routing and `Inbox` triage (`Done`, `Save`, `Unsubscribe`)',
        'Tuning Watch settings and notification routing prevents alert fatigue while ensuring critical `@mentions`, review requests, and security alerts surface immediately.',
    ),
    'collab_gists_public_secret': (
        '**GitHub Gists**: lightweight Git-backed single- or multi-file code snippets/notes in **Public** (discoverable) or **Secret** (unlisted URL, **still accessible to anyone with the link**) modes',
        'Every Gist is a clonable/forkable mini Git repository; critically, Secret Gists are unlisted from search—**not** private/authenticated—so secrets must never be stored in them.',
    ),
    'collab_wikis_longform': (
        '**GitHub Wikis**: repository-attached Markdown documentation portal for long-form architecture guides, handbooks, and design pages editable in the browser or cloned as `<repo>.wiki.git`',
        'Wikis host multi-page narrative project documentation alongside the repository without cluttering application source directories (note: on GitHub Free, Wikis require public repos; private-repo Wikis require Pro/Team/Enterprise).',
    ),
    'collab_github_pages_static': (
        '**GitHub Pages**: hosts static HTML/CSS/JS, Markdown/Jekyll, or GitHub Actions-built documentation/project sites directly from a repository with free HTTPS and custom domains',
        'GitHub Pages turns documentation or frontend static builds into live websites (`<user>.github.io` or `<org>.github.io/<repo>`).',
    ),

    # --- Domain 4: Apply modern development practices ---
    'actions_core_primitives': (
        '**GitHub Actions** hierarchy: **Workflow** (`.github/workflows/*.yml`) triggered by **Events** (`push`, `pull_request`), running **Jobs** on **Runners** (`runs-on`) with ordered **Steps** (`uses:` / `run:`)',
        'In GitHub Actions, jobs run in parallel by default on fresh virtual runner machines (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) unless ordered via `needs:`.',
    ),
    'actions_secrets_ci_cd': (
        'Store sensitive API keys/tokens in encrypted **Actions Secrets** (`${{ secrets.DEPLOY_TOKEN }}`) masked in logs, and automate CI testing, container builds, and environment deployments with required reviewers',
        'GitHub Actions handles CI/CD, issue triage, and scheduled automation while masking encrypted repository/environment/organization secrets in workflow logs.',
    ),
    'copilot_inline_chat_ide': (
        '**GitHub Copilot** inline completions and **Copilot Chat** across supported IDEs (`VS Code`, `Visual Studio`, `JetBrains IDEs`, `Xcode`, `Vim/Neovim`), CLI, and GitHub.com using repository context and `.github/copilot-instructions.md`',
        'GitHub Copilot accelerates coding, unit-test generation, debugging, and PR summaries across major IDEs, GitHub.com, Mobile, and CLI.',
    ),
    'copilot_agents_agent_mode': (
        '**Copilot coding agent** works asynchronously on assigned GitHub Issues in an Actions sandbox to open draft PRs, whereas **IDE Agent Mode** edits local files and runs local terminal tasks autonomously',
        'The January 2026 GH-900 blueprint distinguishes asynchronous **Copilot coding agent** on GitHub (assigned to Issues, opening PRs) from synchronous local **Agent Mode** inside your IDE, plus **MCP** servers and custom agents.',
    ),
    'copilot_multimodel_support': (
        '**Multi-model support in GitHub Copilot**: switch AI models per task (fast low-latency vs deep reasoning models from OpenAI, Anthropic, Google, etc., or auto model selection) subject to organization model policies and Base/LTS model governance',
        'Copilot lets developers select the best model for speed vs complex reasoning (or use auto-selection), while admins govern permitted models in Copilot Business/Enterprise.',
    ),
    'copilot_plans_ind_biz_ent': (
        '**Copilot Individual (`Free`/`Pro`)** serves solo devs; **Copilot Business** adds org seats, policies, and IP indemnity; **Copilot Enterprise** adds Enterprise Cloud codebase indexing, Knowledge Bases, PR summaries, and extra AI credits',
        'Comparing Copilot plans is a core GH-900 objective: Individual/Pro targets solo devs, Business adds org admin/policy/privacy controls (no Enterprise Cloud required), and Enterprise unlocks org codebase indexing, Knowledge Bases, and richer GitHub.com AI features on GitHub Enterprise Cloud.',
    ),
    'codespaces_cloud_vm': (
        '**GitHub Codespaces**: cloud-hosted Docker development environment running on a dedicated VM with full compute terminal, port forwarding, prebuilds, and configurable idle timeout / retention policies',
        'Codespaces spins up a complete cloud VM + container in seconds, accessible in browser VS Code, desktop VS Code, or SSH, billed by vCPU core-hours and storage GB-months.',
    ),
    'codespaces_devcontainer_json': (
        '`.devcontainer/devcontainer.json`: declarative configuration defining container image/Dockerfile, Dev Container Features, VS Code `extensions`, `forwardPorts`, `postCreateCommand`, and Codespaces secrets',
        'Committing `.devcontainer/devcontainer.json` eliminates "works on my machine" drift by codifying every runtime dependency and tool.',
    ),
    'github_dev_browser_editor': (
        '**`github.dev` web-based editor** (opened by pressing `.` on any GitHub repository/PR or changing `.com` to `.dev`): free, instant browser-only lightweight VS Code editor **without** compute terminal, Docker build, or debugger execution',
        '`github.dev` runs entirely in the browser at zero compute cost for fast multi-file edits and PR reviews; whenever you need a terminal to compile/test code, upgrade to **GitHub Codespaces**.',
    ),

    # --- Domain 5: Manage projects with GitHub ---
    'projects_v2_layouts': (
        '**GitHub Projects** (`Table`, `Board`, and `Roadmap` layouts): flexible spreadsheet-like tables, Kanban status columns, and timeline/date roadmaps spanning multiple repositories in an organization or personal account',
        'A single GitHub Project can aggregate Issues, Pull Requests, and draft items across many repositories and render the exact same underlying items as a Table, Kanban Board, or Roadmap.',
    ),
    'projects_custom_fields_iter': (
        'Project custom fields (`Single select`, `Number`, `Date`, `Text`, and **`Iteration`** sprints with automatic break capacities) plus filter/sort/group view configurations (`slice by`)',
        '`Iteration` fields track time-boxed sprints directly inside GitHub Projects without external agile plugins.',
    ),
    'projects_labels_milestones_wf': (
        '**Labels** categorize Issues/PRs (`bug`, `priority:high`), **Milestones** track completion percentage toward a repository release target date, and **Project built-in workflows** auto-update `Status` when items close or PRs merge',
        'Labels classify type/priority, Milestones measure progress toward a release goal inside a repository, and built-in Project workflows eliminate manual card dragging.',
    ),
    'projects_saved_replies_assignees': (
        '**Saved replies** (account-level reusable Markdown templates insertable in Issues, PRs, and Discussions) paired with **Assignees** (up to 10 responsible owners per Issue/PR) to clarify ownership and standardize responses',
        'Saved replies belong to a user’s personal settings so maintainers insert consistent, polite triage responses in two keystrokes, while Assignees designate clear accountability.',
    ),
    'projects_insights_charts': (
        '**Project Insights**: built-in historical **Burn up / status over time** charts and custom Bar, Column, Line, and Stacked Area charts (`X-axis` grouped by Status/Iteration/Assignee) to measure velocity and bottlenecks',
        'Project Insights visualizes current and historical item flow across iterations, labels, and assignees to spot scope creep and blocked work.',
    ),

    # --- Domain 6: Understand privacy, security, and administration ---
    'sec_2fa_totp_webauthn': (
        '**Two-Factor Authentication (`2FA`)** via TOTP authenticator app or FIDO2/WebAuthn security key + offline **recovery codes**, plus **Passkeys** for phishing-resistant passwordless sign-in',
        'Passkeys bind cryptographic credentials to `github.com` (blocking phishing sites) and satisfy both password and 2FA requirements in one biometric/PIN gesture, while recovery codes prevent account lockout.',
    ),
    'sec_repo_roles_five': (
        'Five organization repository roles (least to most privilege): **`Read`** → **`Triage`** (manage Issues/PRs, no push) → **`Write`** (push/merge) → **`Maintain`** (settings, no delete) → **`Admin`** (full control)',
        'Choosing `Triage` for non-developer PMs/support and `Maintain` for tech leads enforces least privilege without granting destructive `Admin` rights.',
    ),
    'sec_org_roles_owners_members': (
        'Organization roles: **Organization Owners** (complete control), **Members** ( governed by **Base permissions** — best practice `No permission` or `Read`), **Billing Managers**, **Security Managers**, **Moderators**, and **Outside Collaborators**',
        'Setting an organization’s Base permissions to `None` or `Read` ensures new members only gain write access through explicit Team assignments.',
    ),
    'sec_emu_idp_lifecycle': (
        '**Enterprise Managed Users (`EMUs`)**: provision accounts (`_shortcode`), SSO auth, and teams from your IdP (`Entra ID`/`Okta`) via SAML/OIDC + SCIM—blocking public repos, personal Gists, and external contributions',
        'EMUs ensure corporate accounts cannot push code to personal public repositories or retain access once deactivated in the corporate Identity Provider.',
    ),
    'sec_copilot_org_policies': (
        'Organization & Enterprise **Copilot policies**: manage seats, block public-code matches, control permitted AI models, and govern **Copilot coding agent**, **IDE Agent Mode**, MCP servers, and custom instructions',
        'Admins centrally govern Copilot seat licensing, public-code filter policies, allowed LLMs, and agentic capabilities at the Enterprise and Organization levels.',
    ),
    'sec_repo_visibility_three': (
        'Repository visibility levels: **`Public`** (open internet), **`Private`** (explicit users/teams only), and **`Internal`** (GitHub Enterprise only — readable by all enterprise members for **InnerSource**)',
        '`Internal` visibility exists specifically in GitHub Enterprise organizations so all employees across sibling orgs can discover and fork repositories (`InnerSource`) without making code `Public`.',
    ),
    'sec_branch_protection_rulesets': (
        '**Branch protection rules & Repository Rulesets**: block force-pushes/deletes on `main`, require PR approvals + **Code Owner** review, require passing **status checks**, signed commits, and optional **Merge Queue**',
        'Repository Rulesets modernize branch/tag protection with layering across an entire organization, bypass lists, and Dry Run (`Evaluate`) mode on Enterprise.',
    ),
    'sec_secret_scanning_dependabot': (
        '**Secret scanning with Push Protection** (blocks commits containing leaked credentials before they land on GitHub) paired with **Dependabot alerts & security updates** (opens automated PRs upgrading vulnerable dependencies)',
        'Secret scanning Push Protection stops credential leaks proactively at `git push` time (free on all public repos and available via GitHub Secret Protection / GHAS on private repos).',
    ),
    'sec_nested_teams_sync': (
        '**Nested Organization Teams** inheriting permissions from parent to child teams, **`@org/team-name`** mentions/review load-balancing, and **IdP Group Sync** automating team membership',
        'Child teams inherit parent team repository access automatically, simplifying RBAC and `@org/team` PR review assignment.',
    ),

    # --- Domain 7: Explore the GitHub community ---
    'comm_oss_benefits_sponsors': (
        '**GitHub Sponsors**: enables individuals and companies (via card or invoiced corporate billing) to fund open-source maintainers/projects with **zero GitHub platform fees** (`FUNDING.yml` displays the `Sponsor` button)',
        'Adding `.github/FUNDING.yml` adds a `Sponsor` button to the repository so users and organizations financially sustain critical open-source maintainers.',
    ),
    'comm_oss_support_programs': (
        'GitHub open-source enablement: free `Actions`, `Dependabot`, `Secret scanning`, `CodeQL`, and **Private Vulnerability Reporting** on public repos, plus **Community Standards** (`good first issue` / `help wanted`)',
        'GitHub provides enterprise-grade security scanning, CI/CD runners, and contributor onboarding tools (`good first issue` discovery) at `$0` for public open-source repositories.',
    ),
    'comm_follow_activity_feed': (
        '**Follow** users and **Organizations** on GitHub so their public repository creations, stars, releases, and open-source activity appear in your personalized dashboard **`Following` feed** without subscribing to every issue comment',
        'Following a developer or organization curates your dashboard `Following` feed, distinct from `Watching` a single repository’s notification stream.',
    ),
    'comm_github_marketplace': (
        '**GitHub Marketplace**: central catalog to discover, evaluate (`Verified creator` badges), and install **GitHub Apps** and reusable **GitHub Actions** (free and paid plans) into personal or organization accounts',
        'GitHub Marketplace distributes vetted CI/CD Actions, code-quality bots, security scanners, and chat integrations with unified GitHub billing.',
    ),
    'comm_innersource_principles': (
        '**InnerSource**: applying open-source practices (**`Internal`** discoverable repositories, `README`/`CONTRIBUTING`/`CODEOWNERS`, cross-team fork-and-PR contributions, transparent asynchronous review) **inside** a private enterprise boundary',
        'InnerSource breaks down corporate engineering silos by letting internal teams discover, reuse, and submit Pull Requests to shared internal components safely.',
    ),
    'comm_fork_vs_template_topics': (
        'Use **Forks** to propose upstream Pull Requests (`Sync fork`), **Templates** to scaffold independent new projects with fresh history, and **Repository Topics** (`#react`, `#cli`) for search discoverability',
        'Forks preserve upstream commit lineage and PR linkage, Templates clone starter structure with fresh history, and Topics index repositories on `github.com/topics`.',
    ),

    # --- Proposed-solution evaluation options ---
    'sol_yes': (
        'Yes — the proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement.',
        'The proposed configuration satisfies every stated GitHub workflow, collaboration, and security requirement in the scenario.',
    ),
    'sol_no_secret_gist': (
        'No — Secret Gists are only unlisted from public search; anyone who obtains the URL can view and clone the Gist without authentication, so credentials must go in encrypted GitHub Secrets instead.',
        'Secret Gists are NOT private/access-controlled; never store tokens, keys, or private customer data in a Secret Gist.',
    ),
    'sol_no_github_dev_terminal': (
        'No — the browser-only `github.dev` editor has no compute backend or integrated terminal to install packages, start servers, or execute test suites; launch a **GitHub Codespace** instead.',
        '`github.dev` cannot execute shell commands, compilers, or containers; full compute requires GitHub Codespaces (or local clone).',
    ),
    'sol_no_template_vs_fork': (
        'No — creating a repository from a **Template** starts an unlinked repository with unrelated commit history that cannot open a cross-repository Pull Request back to upstream; create a **Fork** instead.',
        'Template copies do not share commit ancestry with the source repository; external/cross-repo Pull Requests require a Fork.',
    ),
    'sol_no_codeowners_unprotected': (
        'No — adding `.github/CODEOWNERS` alone only auto-requests reviewers; without enabling branch protection / rulesets with **`Require review from Code Owners`**, contributors with write access can still merge without Code Owner approval.',
        '`CODEOWNERS` requires branch protection or a repository ruleset with `Require review from Code Owners` to enforce blocking merge gates.',
    ),
    'sol_no_emu_public_repo': (
        'No — **Enterprise Managed User (`EMU`)** accounts are restricted to enterprise-internal collaboration and **cannot** create public repositories, personal Gists, or push to external public repositories.',
        'By design, EMU accounts cannot publish public repositories or push to external GitHub.com repositories.',
    ),
    'sol_no_saved_replies_scope': (
        'No — **Saved replies** are personal user-account settings rather than repository-enforced forms; to require structured bug fields from every external reporter, configure YAML **Issue Forms** in `.github/ISSUE_TEMPLATE/`.',
        'Saved replies belong only to an individual user’s account; structured Issue intake across all contributors requires repository Issue Forms/templates.',
    ),
    'sol_no_gitignore_tracked': (
        'No — adding `.env` to `.gitignore` only ignores **untracked** files; a file already committed to Git continues being tracked until `git rm --cached .env` removes it from the index (and any leaked secret is rotated!).',
        '`.gitignore` has no effect on files already tracked in the Git index; you must untrack via `git rm --cached` and immediately rotate exposed secrets.',
    ),

    # --- High-plausibility anti-pattern distractors (`bad_*`) ---
    'bad_git_equals_github': (
        'Git and GitHub are identical software products built by the same team, and Git commands (`git commit`, `git branch`) require an active internet connection to `github.com`',
        'Git is an independent local/distributed VCS created by Linus Torvalds that works completely offline; GitHub is a cloud platform hosting Git repositories.',
    ),
    'bad_force_push_main_daily': (
        'Have every developer commit directly onto `main` and run `git push --force origin main` whenever remote history diverges',
        'Force-pushing onto shared `main` overwrites teammates’ commits and bypasses Pull Request code review and CI gates.',
    ),
    'bad_no_license_means_mit': (
        'Omit the `LICENSE` file because any public repository on GitHub automatically defaults to the permissive MIT open-source license',
        'Public visibility on GitHub only allows viewing and forking on GitHub under Terms of Service; without a `LICENSE` file, default copyright reserves all rights!',
    ),
    'bad_admin_for_triage_pm': (
        'Grant every product manager, support agent, and external contractor the repository `Admin` role so they can apply labels to Issues',
        'Applying labels, milestones, and assignees without code push access requires only the least-privilege **`Triage`** role—never `Admin`.',
    ),
    'bad_public_issue_zeroday': (
        'Instruct security researchers in `README.md` to open public GitHub Issues containing full exploit proof-of-concept payloads before a patch exists',
        'Zero-day vulnerabilities must be reported privately via `SECURITY.md` / Private Vulnerability Reporting rather than exposed in public Issues.',
    ),
    'bad_secret_gist_api_keys': (
        'Store production cloud API keys inside a **Secret Gist** so only authenticated organization Owners can read them',
        'Secret Gists are publicly reachable by anyone who knows or guesses the URL; store secrets only in encrypted GitHub Actions/Codespaces/Dependabot Secrets.',
    ),
    'bad_copilot_free_org_sso': (
        'Assign **GitHub Copilot Individual (`Free`/`Pro`)** seats centrally via SAML SSO SCIM groups with organization-wide IP indemnity and Enterprise Knowledge Bases',
        'Organization seat assignment, IP indemnity, and policy controls require **Copilot Business** or **Copilot Enterprise**, not Copilot Individual.',
    ),
    'bad_copilot_biz_requires_hec': (
        '**GitHub Copilot Business** can only be purchased if the organization first upgrades to **GitHub Enterprise Cloud** (`$21/user/mo`)',
        'Copilot Business does **not** require GitHub Enterprise Cloud (organizations on GitHub Free/Team can subscribe to Copilot Business), whereas **Copilot Enterprise** requires GitHub Enterprise Cloud.',
    ),
    'bad_github_dev_runs_docker': (
        'Press `.` to open `github.dev` and run `docker compose up` plus Python pytest suites directly inside `github.dev`’s built-in Linux VM terminal',
        '`github.dev` runs purely in the client browser with zero compute VM or shell terminal; running Docker or tests requires **GitHub Codespaces**.',
    ),
    'bad_watch_all_for_bookmark': (
        'Set **Watch -> All Activity** on 200 open-source repositories solely to bookmark them for later reading without receiving emails',
        '`Watch -> All Activity` subscribes you to every single Issue, PR, and comment notification; use **Stars** (and **Lists**) to bookmark repositories quietly.',
    ),
    'bad_internal_repo_free_personal': (
        'Create **`Internal`** visibility repositories under a free personal individual GitHub account so friends can view them',
        '`Internal` repository visibility is exclusively available to organizations belonging to a **GitHub Enterprise** account, never personal accounts.',
    ),
    'bad_shared_password_no_2fa': (
        'Share one `team-bot` personal account password across 15 developers over chat and disable `2FA` so nobody gets prompted for codes',
        'Shared passwords without 2FA destroy individual auditability and violate GitHub account security policies; use individual accounts with 2FA/Passkeys and GitHub Apps.',
    ),
    'bad_delete_repo_instead_archive': (
        'Permanently delete a retired open-source repository and recreate an empty repo with the same name to mark it read-only',
        'Deleting a repository destroys Issues, PR history, Stars, and allows namespace hijacking risks; **Archive** the repository instead to preserve read-only history.',
    ),
    'bad_upload_500mb_browser': (
        'Upload a `500 MB` compiled video binary directly through GitHub’s web browser file uploader onto `main`',
        'Browser uploads cap at `25 MB` per file and standard Git pushes block files over `100 MB`; large binaries belong in **Git Large File Storage (`Git LFS`)** or Release assets.',
    ),
    'bad_sponsors_platform_cut_30': (
        'GitHub Sponsors deducts a mandatory `30%` platform commission from individual credit-card sponsorships and grants sponsors `Write` access automatically',
        'GitHub charges `0%` platform fees on sponsorships to maintainers from personal accounts, and sponsoring never grants repository permissions.',
    ),
    'bad_actions_yaml_root_folder': (
        'Commit workflow YAML files directly in the repository root (`/ci.yml`) or `/scripts/ci.yml` so GitHub Actions detects them automatically',
        'GitHub Actions **only** discovers workflow YAML files placed inside exact `.github/workflows/*.yml` (or `.yaml`).',
    ),
    'bad_projects_single_repo_only': (
        'Classic single-repository kanban boards that cannot include Issues from sibling repositories or custom Iteration/Date fields',
        'Modern **GitHub Projects** live at the organization or user level, aggregate items across multiple repositories, and support custom Iteration, Number, Date, and Single-select fields.',
    ),

    # --- Atomic multi-select (`M2` / `M3`) building-block options ---
    'ms_vcs_full_local_history': (
        'Every developer clone contains the full commit history and branches, enabling offline commits and history inspection',
        'Distributed Git clones carry complete commit and branch history locally without requiring network connectivity for local operations.',
    ),
    'ms_vcs_audit_and_revert': (
        'Commits record author, timestamp, and message metadata so teams can audit changes (`git blame`) and revert regressions safely',
        'Commit metadata provides line-by-line accountability and clean rollback via `git revert`.',
    ),
    'ms_ghflow_short_branch': (
        'Create a short-lived descriptive branch off `main` so `main` stays deployable at all times',
        'GitHub Flow keeps `main` continuously deployable by isolating every change on a short-lived branch.',
    ),
    'ms_ghflow_pr_review_ci': (
        'Open a Pull Request early to run automated status checks and gather peer code review before merging into `main`',
        'Pull Requests combine asynchronous peer review and automated CI verification prior to merging.',
    ),
    'ms_md_task_checkbox': (
        'Render interactive task checkboxes using `- [ ]` (incomplete) and `- [x]` (completed) list syntax',
        'GFM task lists track sub-step progress directly inside Issue and Pull Request descriptions.',
    ),
    'ms_md_alert_callout': (
        'Highlight critical callouts using blockquote alert syntax such as `> [!NOTE]`, `> [!IMPORTANT]`, or `> [!WARNING]`',
        'GFM alert syntax renders color-coded callout banners in READMEs, Issues, Discussions, and Pull Requests.',
    ),
    'ms_md_fenced_lang_mermaid': (
        'Format syntax-highlighted code or live diagrams using fenced triple backticks with a language tag (```` ```ts ````, ```` ```mermaid ````)',
        'Language-tagged code fences render syntax highlighting and native Mermaid diagrams across GitHub.',
    ),
    'ms_acct_org_teams_roles': (
        'Use a **GitHub Organization** to group members into nested Teams with shared repository ownership and granular roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`)',
        'Organizations centralize multi-developer ownership and team-based RBAC.',
    ),
    'ms_acct_ent_sso_multi_org': (
        'Use a **GitHub Enterprise** account to govern multiple Organizations under unified SAML/OIDC SSO, Enterprise Managed Users, and centralized billing/policies',
        'Enterprise accounts unify security, identity, and policy governance across multiple organizations.',
    ),
    'ms_repo_codeowners_path': (
        'Store `CODEOWNERS` inside `.github/`, the repository root, or `docs/` on the target base branch',
        'GitHub inspects only `.github/CODEOWNERS`, `/CODEOWNERS`, or `docs/CODEOWNERS` on the branch targeted by the Pull Request.',
    ),
    'ms_repo_codeowners_protect': (
        'Enable branch protection or a repository ruleset with `Require a pull request before merging` and `Require review from Code Owners`',
        'Without branch protection or ruleset enforcement, `CODEOWNERS` requests reviews without blocking unapproved merges.',
    ),
    'ms_repo_dep_graph_enable': (
        'Enable the **Dependency graph** so GitHub parses manifest and lockfiles (`package-lock.json`, ` Cargo.lock`, `requirements.txt`)',
        'The Dependency graph inventories direct and transitive open-source packages declared in repository manifests.',
    ),
    'ms_repo_dependabot_alerts': (
        'Enable **Dependabot alerts** and **Dependabot security updates** to notify maintainers of CVEs and open automated patch Pull Requests',
        'Dependabot matches Dependency graph entries against the GitHub Advisory Database and proposes version-bump PRs.',
    ),
    'ms_collab_closes_keyword': (
        'Include a supported closing keyword (`Closes #N`, `Fixes #N`, or `Resolves #N`) in the Pull Request description targeting the default branch',
        'Merging a Pull Request with a closing keyword into the default branch automatically closes the linked Issue.',
    ),
    'ms_collab_dev_sidebar_link': (
        'Link the Issue manually from the Pull Request’s **`Development`** sidebar (up to 10 issues) so merging into any target branch closes it',
        'Manual `Development` sidebar links work across branches and display clear traceability on both timelines.',
    ),
    'ms_collab_pages_static_site': (
        'Use **GitHub Pages** to publish public/enterprise static documentation websites (`<org>.github.io/<repo>`) built via Actions or Jekyll',
        'GitHub Pages renders repository docs into browsable websites with HTTPS.',
    ),
    'ms_collab_discussions_qa': (
        'Use **GitHub Discussions** for open-ended community Q&A, polls, and RFCs with `Mark as answer` rather than cluttering bug Issues',
        'Discussions keep conversational Q&A searchable and separate from actionable engineering Issues.',
    ),
    'ms_actions_workflow_dir': (
        'Define workflows in YAML files stored under `.github/workflows/` with `on:` event triggers (`push`, `pull_request`, `schedule`)',
        'GitHub Actions discovers `.yml`/`.yaml` files exclusively in `.github/workflows/`.',
    ),
    'ms_actions_jobs_runners': (
        'Specify one or more `jobs:` configured with `runs-on:` (`ubuntu-latest`, `windows-latest`, `macos-latest`, or `self-hosted`) and ordered `steps:`',
        'Each job executes its `uses:` actions and `run:` commands on a fresh runner virtual environment.',
    ),
    'ms_copilot_cloud_agent_pr': (
        '**Copilot coding agent (cloud agent)**: assign a GitHub Issue to `@copilot` so it works asynchronously in an Actions-powered environment and opens a draft Pull Request',
        'Copilot coding agent runs asynchronously on GitHub to research, edit, test, and open draft PRs for human review.',
    ),
    'ms_copilot_ide_agent_mode': (
        '**IDE Agent Mode**: let Copilot autonomously plan multi-file edits, run local terminal commands, and iterate on compiler/test errors inside VS Code or Visual Studio',
        'IDE Agent Mode operates synchronously inside the developer’s local IDE workspace.',
    ),
    'ms_copilot_multimodel_pick': (
        '**Multi-model selector**: switch between low-latency models and deep-reasoning models in Copilot Chat (or use auto model selection) per task complexity',
        'Multi-model support matches model speed, reasoning depth, and AI credit usage to each coding task.',
    ),
    'ms_codespaces_full_vm': (
        '**GitHub Codespaces** provisions a cloud VM running a customizable `.devcontainer/devcontainer.json` Docker container with full terminal, debugger, and port forwarding',
        'Codespaces provides full Linux compute for compiling, testing, and running multi-service apps.',
    ),
    'ms_github_dev_zero_compute': (
        '**`github.dev`** opens instantly in the browser (`press .`) for free lightweight multi-file editing and PR review without a compute VM or terminal',
        '`github.dev` is ideal for rapid Markdown/code edits and diff browsing when shell execution is unnecessary.',
    ),
    'ms_proj_table_board_roadmap': (
        'Switch seamlessly between **Table**, **Board**, and **Roadmap** views backed by custom **`Iteration`**, `Single select`, `Number`, and `Date` fields',
        'GitHub Projects renders live cross-repository Issues and PRs across Table, Kanban Board, and timeline Roadmap layouts.',
    ),
    'ms_proj_auto_workflows_insights': (
        'Automate card transitions with built-in **Project workflows** (`Item closed -> Done`, `PR merged`) and track historical progress in **Project Insights** burn-up charts',
        'Built-in workflows and Project Insights eliminate manual status updates and visualize sprint velocity.',
    ),
    'ms_sec_passkey_webauthn': (
        'Register phishing-resistant **Passkeys** (WebAuthn/FIDO2) for passwordless sign-in alongside TOTP / hardware security-key **`2FA`**',
        'Passkeys protect against credential-harvesting phishing domains while satisfying strong authentication.',
    ),
    'ms_sec_recovery_codes_safe': (
        'Download and store one-time **`2FA` recovery codes** in an encrypted password manager or offline vault to prevent account lockout',
        'Recovery codes are essential to regain account access if a phone or hardware key is lost.',
    ),
    'ms_sec_emu_idp_scim': (
        'Provision **Enterprise Managed Users (`EMUs`)** from your corporate IdP (`Entra ID` / `Okta`) via OIDC/SAML + SCIM so corporate accounts cannot create public repos or Gists',
        'EMUs lock account lifecycle, authentication, and data boundaries strictly to the enterprise IdP.',
    ),
    'ms_sec_copilot_policy_admin': (
        'Enforce organization/enterprise **Copilot policies** governing seat assignment, public-code duplication blocking, permitted AI models, and Copilot coding agent availability',
        'Centralized Copilot governance lets admins control AI features, models, and IP guardrails across organizations.',
    ),
    'ms_sec_branch_pr_checks': (
        'Require Pull Request reviews (including Code Owners) and passing **required status checks** before merging into `main`',
        'Protected branches and rulesets prevent untested or unreviewed commits from reaching `main`.',
    ),
    'ms_sec_block_force_push_del': (
        'Block force-pushes and branch deletions on `main` (and optionally require signed commits and linear history / Merge Queue)',
        'Blocking force-pushes and deletions protects commit history integrity on production branches.',
    ),
    'ms_comm_innersource_internal': (
        'Publish shared libraries as **`Internal`** repositories in GitHub Enterprise with clear `README.md`, `CONTRIBUTING.md`, and `CODEOWNERS` files',
        '`Internal` visibility plus contributor docs makes internal libraries discoverable across every team in the enterprise.',
    ),
    'ms_comm_fork_topics_market': (
        'Add descriptive **Repository Topics** for internal/public discovery, accept cross-team **Fork / branch Pull Requests**, and vet reusable workflows from **GitHub Marketplace**',
        'Topics, PR-based collaboration, and vetted Marketplace Actions accelerate reuse across teams and open-source communities.',
    ),
}

TERMS.update(SEQUENCES)
