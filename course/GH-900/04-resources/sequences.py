"""Four-step ordered workflow sequences ('→') for Exam GH-900: GitHub Foundations.

All option labels stay <= 245 characters and model authentic GitHub workflows without drag-and-drop UI wording.
"""

SEQUENCES = {
    # 1. Local Git working tree -> staging -> commit -> push (Skill 1.3)
    'seq_git_local_ok': (
        'Edit files in the local working directory → Stage changes with `git add` → Record a snapshot locally with `git commit -m` → Upload commits to GitHub with `git push`',
        'Git moves changes cleanly from the working tree to the staging index (`git add`), commits an immutable local snapshot (`git commit`), and publishes commits to the remote (`git push`).',
    ),
    'seq_git_local_w1': (
        'Edit files in the local working directory → Upload files directly with `git push` → Stage changes with `git add` → Record a snapshot with `git commit -m`',
        '`git push` only transfers already committed local snapshots; unstaged working-tree edits are ignored until `git add` and `git commit` run.',
    ),
    'seq_git_local_w2': (
        'Record a snapshot with `git commit -m` → Edit files in the working directory → Stage changes with `git add` → Upload commits with `git push`',
        'Committing before editing and staging captures nothing from the intended file modifications.',
    ),
    'seq_git_local_w3': (
        'Stage changes with `git add` → Upload staged files with `git push` → Edit files in the working directory → Record a snapshot with `git commit -m`',
        'Staged index changes cannot be pushed to a remote repository before `git commit` creates a commit object.',
    ),

    # 2. GitHub Flow collaborative workflow (Skill 1.5)
    'seq_github_flow_ok': (
        'Create a descriptive branch from the default branch → Commit changes and open a Pull Request → Review code, pass status checks, and address feedback → Merge into the default branch and delete the topic branch',
        'GitHub Flow isolates work on a short-lived branch, opens a Pull Request for discussion and automated checks, merges into `main`, and cleans up the merged branch.',
    ),
    'seq_github_flow_w1': (
        'Commit directly onto `main` without a branch → Open a Pull Request after deploying → Create a topic branch from `main` → Delete `main` after review',
        'Committing unreviewed work directly to `main` and deleting the default branch violates GitHub Flow branch isolation.',
    ),
    'seq_github_flow_w2': (
        'Create a descriptive branch from `main` → Delete the topic branch immediately → Open a Pull Request from the deleted branch → Run status checks after merge',
        'Deleting the topic branch before opening and merging a Pull Request discards the branch reference needed for review.',
    ),
    'seq_github_flow_w3': (
        'Merge empty branch into `main` first → Commit feature code directly on `main` → Request Pull Request review after production release → Disable status checks',
        'GitHub Flow requires code review and passing checks on a Pull Request before changes enter the default branch.',
    ),

    # 3. Enforcing CODEOWNERS reviews (Skill 2.1 / 6.4)
    'seq_codeowners_ok': (
        'Add `.github/CODEOWNERS` mapping file paths to `@org/team` handles → Merge `CODEOWNERS` into the target branch → Enable branch protection or a ruleset requiring pull request reviews → Enable `Require review from Code Owners`',
        '`CODEOWNERS` must reside on the base branch in `.github/`, root, or `docs/`, and branch protection or rulesets must require Code Owner review to block merges.',
    ),
    'seq_codeowners_w1': (
        'Enable `Require review from Code Owners` on an unprotected repo → Keep `CODEOWNERS` untracked on a laptop → Grant every contributor Admin role → Merge without Pull Requests',
        'Untracked local `CODEOWNERS` files are invisible to GitHub, and Admin bypass or direct pushes skip pull request review.',
    ),
    'seq_codeowners_w2': (
        'Place `CODEOWNERS.txt` inside `src/assets/` → Archive the repository → Open a Gist for review → Disable pull request reviews in branch settings',
        'GitHub only reads exact `CODEOWNERS` in `.github/`, root, or `docs/`, and archiving makes the repository read-only.',
    ),
    'seq_codeowners_w3': (
        'Delete all organization teams → Map paths in `README.md` instead of `CODEOWNERS` → Force-push directly to `main` → Enable GitHub Pages',
        '`README.md` does not trigger automatic review requests or merge enforcement.',
    ),

    # 4. Issue triage -> linked PR -> auto-close (Skill 3.2)
    'seq_issue_pr_link_ok': (
        'Triage the Issue with labels, milestone, and assignee → Create a feature branch and commit the fix → Open a Pull Request containing `Closes #42` in its description → Merge the approved Pull Request into the default branch',
        'Including a closing keyword (`Closes #42`, `Fixes #42`, `Resolves #42`) in a Pull Request targeting the default branch automatically closes Issue `#42` upon merge.',
    ),
    'seq_issue_pr_link_w1': (
        'Close Issue `#42` manually before writing code → Commit directly to a fork wiki → Open an unlinked Discussion post → Archive the repository',
        'Closing the issue prematurely loses active tracking, and wiki edits or Discussions do not merge code changes.',
    ),
    'seq_issue_pr_link_w2': (
        'Write `Mentioning #42` in a commit on a non-default experimental branch → Never open a Pull Request → Delete the feature branch → Expect Issue `#42` to close automatically',
        'Only supported closing keywords merged into the default branch (or explicitly linked PRs) close an issue automatically.',
    ),
    'seq_issue_pr_link_w3': (
        'Create a secret Gist with `Fixes #42` → Star the repository → Watch releases only → Expect Gist save to close Issue `#42`',
        'Gists are separate repositories and cannot auto-close repository Issues via closing keywords.',
    ),

    # 5. Publishing documentation with GitHub Pages via Actions (Skill 3.4)
    'seq_pages_deploy_ok': (
        'Commit static site or Markdown docs to the repository → Open `Settings -> Pages` and set `Build and deployment` source → Run the GitHub Pages build/deployment workflow → Verify the published site URL and optional custom domain HTTPS',
        'GitHub Pages builds from a configured branch/folder or GitHub Actions workflow and serves the site over HTTPS at `<owner>.github.io/<repo>` or a verified custom domain.',
    ),
    'seq_pages_deploy_w1': (
        'Upload raw site files to a secret Gist → Enable `SECURITY.md` only → Disable GitHub Actions and Pages in Settings → Expect `<owner>.github.io` to publish automatically',
        'Secret Gists do not publish GitHub Pages sites when Pages is disabled in repository settings.',
    ),
    'seq_pages_deploy_w2': (
        'Point DNS CNAME to `localhost` → Delete repository `Settings` → Store HTML inside Saved Replies → Enable 2FA recovery codes',
        '`localhost` DNS records and Saved Replies have no connection to GitHub Pages hosting.',
    ),
    'seq_pages_deploy_w3': (
        'Archive the empty repository before adding files → Disable HTTPS enforcement → Create a Milestone named `Pages` → Expect Milestone creation to deploy a website',
        'Milestones track Issue/PR progress and archived empty repositories cannot commit site content.',
    ),

    # 6. Creating a GitHub Actions CI workflow (Skill 4.1)
    'seq_actions_ci_ok': (
        'Create `.github/workflows/ci.yml` → Define `on: [push, pull_request]` triggers → Configure `jobs` with `runs-on: ubuntu-latest` and test `steps` → Commit `ci.yml` and inspect logs in the `Actions` tab',
        'GitHub Actions workflows live as YAML files in `.github/workflows/`, trigger on defined events, execute job steps on specified runners, and report status in the `Actions` tab.',
    ),
    'seq_actions_ci_w1': (
        'Place `ci.yml` inside `docs/workflows/` → Omit `on:` triggers and `runs-on:` runner labels → Save as a personal Gist → Expect repository Pull Requests to run CI automatically',
        'Workflow YAML files outside `.github/workflows/` are ignored by GitHub Actions, and `on:` plus `runs-on:` are required keys.',
    ),
    'seq_actions_ci_w2': (
        'Open `github.dev` with `.` key → Run `npm test` directly inside `github.dev` browser tab → Save output in a Wiki page → Expect automatic status checks on Pull Requests',
        '`github.dev` has no compute terminal to execute `npm test` or report Pull Request status checks.',
    ),
    'seq_actions_ci_w3': (
        'Create an Issue template in `.github/ISSUE_TEMPLATE/` → Assign `@copilot` to a Milestone → Star the repository → Expect Issue templates to execute unit tests on Linux runners',
        'Issue templates structure bug reports and never provision Actions runners or run unit tests.',
    ),

    # 7. Customizing GitHub Codespaces with dev containers (Skill 4.4)
    'seq_codespace_dev_ok': (
        'Create `.devcontainer/devcontainer.json` with image and VS Code extensions → Add `postCreateCommand` and `forwardPorts` → Commit `devcontainer.json` to the branch → Launch a cloud Codespace to verify',
        'Committing `.devcontainer/devcontainer.json` standardizes runtimes, extensions, startup commands, and port forwarding for every contributor launching a Codespace.',
    ),
    'seq_codespace_dev_w1': (
        'Install tools manually inside one personal Codespace without editing `.devcontainer/` → Delete the Codespace → Ask teammates to open `github.dev` → Expect `github.dev` to provision that custom Docker container',
        'Uncommitted manual installs vanish when a Codespace is deleted, and `github.dev` does not run dev containers.',
    ),
    'seq_codespace_dev_w2': (
        'Add Docker settings to `.github/FUNDING.yml` → Enable GitHub Sponsors → Star the repository → Expect `FUNDING.yml` to build a Codespace container',
        '`FUNDING.yml` configures sponsor buttons rather than Codespaces dev containers.',
    ),
    'seq_codespace_dev_w3': (
        'Save `devcontainer.json` in a private user Wiki → Disable Codespaces in Organization Settings → Press `.` on the repository → Expect full container terminal execution',
        'Wikis do not configure Codespaces, disabling Codespaces blocks creation, and `.` launches browser-only `github.dev`.',
    ),

    # 8. Configuring & automating GitHub Projects (Skill 5.2 / 5.4)
    'seq_project_auto_ok': (
        'Create a GitHub Project with custom `Iteration` and `Priority` fields → Link repository Issues and Pull Requests → Enable built-in `Item closed -> Done` workflows → View Project Insights burn-up charts',
        'GitHub Projects combines custom fields (`Iteration`, `Single select`), linked Issues/PRs, built-in status automations, and Insights charts for end-to-end tracking.',
    ),
    'seq_project_auto_w1': (
        'Create a static Markdown table in `SECURITY.md` → Turn off Issues on all repositories → Add Saved Replies → Expect `SECURITY.md` to auto-generate sprint velocity charts',
        '`SECURITY.md` documents vulnerability reporting and provides neither dynamic project views nor Insights charts.',
    ),
    'seq_project_auto_w2': (
        'Archive the organization repositories → Create a Milestone inside a secret Gist → Follow external users → Expect Milestone creation in a Gist to move Project board cards',
        'Gists do not host Milestones or drive organization GitHub Projects automations.',
    ),
    'seq_project_auto_w3': (
        'Delete all repository labels → Export raw commits via `git clone --bare` → Disable Actions and Projects in Organization Settings → View Roadmap charts in GitHub Mobile offline cache',
        'Disabling Projects in Organization Settings prevents creating or viewing GitHub Projects.',
    ),

    # 9. Securing an account with 2FA and Passkeys (Skill 6.1)
    'seq_2fa_passkey_ok': (
        'Enable `2FA` with a TOTP app or security key → Download and store one-time `2FA` recovery codes safely → Register a phishing-resistant passkey in Security settings → Verify passkey or `2FA` sign-in',
        'Enabling 2FA first, safeguarding recovery codes against device loss, and adding a WebAuthn passkey delivers strong, phishing-resistant account security.',
    ),
    'seq_2fa_passkey_w1': (
        'Commit plaintext passwords into `README.md` → Share one shared personal account across five engineers → Disable `2FA` to simplify CI scripts → Skip recovery codes',
        'Sharing personal accounts, committing passwords, and disabling 2FA violate core GitHub security principles.',
    ),
    'seq_2fa_passkey_w2': (
        'Delete recovery codes immediately without saving → Turn off `2FA` before registering SMS → Publish personal access tokens in a public Gist → Enable public visibility',
        'Publicly exposing PATs triggers automatic token revocation/compromise, and discarding recovery codes risks permanent lockout.',
    ),
    'seq_2fa_passkey_w3': (
        'Set repository visibility to Public → Add `@everyone` to `CODEOWNERS` → Create a GitHub Pages site → Expect GitHub Pages to enforce account-level passkey authentication',
        'GitHub Pages hosts static websites and has no role in account-level 2FA or passkey setup.',
    ),

    # 10. Open-source fork-and-pull-request contribution (Skill 7.6)
    'seq_fork_oss_ok': (
        'Read upstream `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` → Fork upstream to your account and create a topic branch → Commit and push your fix to your fork → Open a cross-repo Pull Request to upstream',
        'External contributors without write access read contribution guidelines, work on a topic branch in their fork, and open a Pull Request back to the upstream repository.',
    ),
    'seq_fork_oss_w1': (
        'Clone upstream over HTTPS without forking → Push commits directly to upstream `main` without write permissions → Archive upstream → Merge your own PR as a First-time contributor',
        'Users without write permissions receive `403 Permission denied` when pushing directly to an upstream repository.',
    ),
    'seq_fork_oss_w2': (
        'Use `Create repository from template` instead of `Fork` → Commit changes to the unlinked template copy → Open a Pull Request back to upstream with unrelated commit histories → Auto-merge',
        'Repositories created from templates start with a brand-new unrelated commit history and are not linked forks for upstream PRs.',
    ),
    'seq_fork_oss_w3': (
        'Report a public zero-day exploit in a public Discussion → Force-push over upstream tags → Delete `LICENSE` → Sponsor yourself to gain `Admin` rights',
        'Security vulnerabilities belong in private reporting per `SECURITY.md`, and sponsorship never grants repository `Admin` permissions.',
    ),
}
