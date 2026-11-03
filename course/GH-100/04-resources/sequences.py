"""Ordered 4-step workflow sequences (`O` items) for Exam GH-100: GitHub Enterprise Administrator.

Every `seq_*_ok` and `seq_*_w1..w3` label stays strictly <= 240 chars and uses ` → ` separators.
"""

SEQUENCES = {
    # 1. Provisioning GHEC with Enterprise Managed Users (D1)
    'seq_emu_setup_ok': (
        'Create EMU enterprise & save recovery codes → configure SAML/OIDC SSO with admin setup user → enable SCIM user/group provisioning in IdP → sync IdP groups to Enterprise/Org teams',
        'Correct order: establish the EMU enterprise and offline recovery codes, wire SAML/OIDC SSO using the initial setup user, turn on SCIM user/group provisioning, and map IdP groups to teams.',
    ),
    'seq_emu_setup_w1': (
        'Sync IdP groups to Enterprise teams → enable SCIM provisioning → configure SAML/OIDC SSO → create the EMU enterprise account last',
        'Reverses prerequisite dependencies: SCIM and IdP group synchronization cannot run before the EMU enterprise exists and SAML/OIDC SSO is configured.',
    ),
    'seq_emu_setup_w2': (
        'Invite employees personal GitHub.com accounts → convert personal accounts into EMUs in place → enable SCIM → disable 2FA on the IdP',
        'Personal GitHub.com accounts can never be converted in place into EMU accounts; EMUs are brand-new IdP-provisioned accounts.',
    ),
    'seq_emu_setup_w3': (
        'Enable SCIM without configuring SAML/OIDC SSO → share one setup password across engineers → skip recovery codes → assign everyone Enterprise Owner',
        'SCIM on EMUs requires SAML or OIDC SSO first, and sharing setup credentials or granting universal Enterprise Owner violates least privilege.',
    ),

    # 2. Delegating Cross-Org Governance via Enterprise Teams (D1)
    'seq_ent_team_gov_ok': (
        'Create an Enterprise team under People → remove manual members & link an EMU IdP group (<=5,000 users) → grant org memberships, Copilot seats, or custom enterprise roles → reference @org/ent:slug or ruleset bypass',
        'Correct workflow: create the Enterprise team, bind an EMU IdP group (with zero manual members and <=5,000 users), assign org/Copilot/role entitlements, and use @org/ent:slug or ruleset bypasses.',
    ),
    'seq_ent_team_gov_w1': (
        'Add 20 manual members to the Enterprise team → simultaneously attach an IdP group while keeping manual members → add 8,000 IdP users → list @/ent:slug in CODEOWNERS',
        'Fails three platform rules: IdP-synced Enterprise teams cannot retain manual members, IdP sync pauses above 5,000 users, and Enterprise teams do not support CODEOWNERS.',
    ),
    'seq_ent_team_gov_w2': (
        'Create an Organization team in one org → expect it to grant Enterprise Audit Log roles across 50 orgs → sync via SCIM without an IdP → bypass Enterprise Owner policies',
        'An Organization team is scoped to one organization and cannot hold enterprise-level administrative roles across sibling organizations.',
    ),
    'seq_ent_team_gov_w3': (
        'Assign CODEOWNERS to an Enterprise team first → nest three child Enterprise teams underneath it → mark the Enterprise team Secret → add a Team maintainer',
        'Enterprise teams currently do not support CODEOWNERS, nested teams, Secret visibility, or Team maintainers.',
    ),

    # 3. Generating & Submitting GHES Support Diagnostics (D2)
    'seq_ghes_support_ok': (
        'Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal',
        'Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.',
    ),
    'seq_ghes_support_w1': (
        'Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC',
        'Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.',
    ),
    'seq_ghes_support_w2': (
        'Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation',
        'Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.',
    ),
    'seq_ghes_support_w3': (
        'File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket',
        'Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.',
    ),

    # 4. Rolling Out an Enforced Enterprise Security Configuration (D3)
    'seq_sec_config_ok': (
        'Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration',
        'Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.',
    ),
    'seq_sec_config_w1': (
        'Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced',
        'GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.',
    ),
    'seq_sec_config_w2': (
        'Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet',
        'Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.',
    ),
    'seq_sec_config_w3': (
        'Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy',
        'Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.',
    ),

    # 5. Security Incident Response: Purging Leaked Secrets from Git History (D3)
    'seq_secret_purge_ok': (
        'Revoke & rotate the exposed secret at the provider → scrub all branches/tags via git filter-repo → force-push cleaned refs & have devs re-clone → send commit SHAs to GitHub Support to purge cached views',
        'Correct incident response: treat the secret as compromised (revoke/rotate first!), scrub history with `git filter-repo`, force-push cleaned refs, and ask GitHub Support to purge unreachable cached views.',
    ),
    'seq_secret_purge_w1': (
        'Run git rm secrets.env in a new commit and push → assume historical commits are erased → keep the production API key active → skip GitHub Support cache purge',
        'A normal `git rm` commit leaves the secret readable in prior commits and cached PR diffs, and unrotated leaked keys remain exploitable.',
    ),
    'seq_secret_purge_w2': (
        'Archive the repository to hide the leaked key → rotate the key next quarter → use deprecated git filter-branch without force-pushing → tell devs to git pull --merge old history back',
        'Archiving keeps history readable to everyone with Read access, and merging uncleaned local clones reintroduces scrubbed commits.',
    ),
    'seq_secret_purge_w3': (
        'Contact GitHub Support first to rotate your AWS IAM key → wait before revoking in AWS → delete the entire GitHub Organization → recreate repos from developer zip files',
        'GitHub Support cannot rotate third-party cloud credentials; the enterprise admin must revoke/rotate the secret immediately in AWS.',
    ),

    # 6. Migrating Automation from Classic PAT to Enterprise GitHub App (D3)
    'seq_gh_app_rollout_ok': (
        'Create an org-owned GitHub App with least-privilege permissions → store the App private key in a vault & install on selected repos → generate a short-lived JWT to exchange for a 1-hour installation access token → revoke the legacy classic PAT',
        'Correct migration: register a fine-grained GitHub App, safeguard its private key and scope installation repos, mint 1-hour installation tokens via signed JWT, and retire the classic PAT.',
    ),
    'seq_gh_app_rollout_w1': (
        'Create an OAuth App with full repo scope on the CEO account → hardcode the non-expiring OAuth token in YAML → disable OAuth App restrictions → delete audit logs',
        'OAuth Apps use broad user-tied scopes and long-lived tokens rather than actor-independent 1-hour installation tokens.',
    ),
    'seq_gh_app_rollout_w2': (
        'Register a GitHub App → commit its .pem private key to a public repo → use the 10-minute JWT directly as a REST bearer token for 30 days → keep classic PATs unrestricted',
        'App `.pem` keys must never be committed, and a GitHub App JWT (max 10 minutes) only authenticates App endpoints to mint a 1-hour installation token.',
    ),
    'seq_gh_app_rollout_w3': (
        'Create 50 paid machine-user seats → share one classic PAT with admin:org across 50 scripts → turn off 2FA → ignore 5,000 req/hr shared user rate limits',
        'Machine users consume paid Enterprise seats and share a 5,000 req/hr user rate limit instead of GHEC GitHub App installation scaling (15,000 req/hr).',
    ),

    # 7. Configuring Azure Private Networking for GitHub-Hosted Larger Runners (D4)
    'seq_azure_vnet_runner_ok': (
        'Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows',
        'Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.',
    ),
    'seq_azure_vnet_runner_w1': (
        'Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group',
        'Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.',
    ),
    'seq_azure_vnet_runner_w2': (
        'Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows',
        'Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.',
    ),
    'seq_azure_vnet_runner_w3': (
        'Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test',
        'By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.',
    ),

    # 8. Integrating Third-Party Vaults with GitHub Actions via OIDC (D4)
    'seq_oidc_vault_ok': (
        'Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets',
        'Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.',
    ),
    'seq_oidc_vault_w1': (
        'Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs',
        'Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.',
    ),
    'seq_oidc_vault_w2': (
        'Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years',
        'Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.',
    ),
    'seq_oidc_vault_w3': (
        'Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs',
        'The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.',
    ),

    # 9. Implementing Enterprise Audit Log Streaming to SIEM (D3 / D5)
    'seq_audit_stream_ok': (
        'Provision encrypted SIEM/storage sink (Event Hubs, Blob, S3, Splunk) → configure credentials in Enterprise Audit Log Streaming → verify test event & optional Git toggle → set SIEM retention & alerts',
        'Correct audit-streaming setup: prepare the target sink, configure credentials in Enterprise Settings -> Audit log -> Log streaming, validate the test check, and enforce SIEM retention/alerting.',
    ),
    'seq_audit_stream_w1': (
        'Rely solely on the 180-day web UI audit search for 7-year regulatory retention → skip log streaming → poll REST API every 50 ms until rate-limited → store logs in a public Gist',
        'GitHub retains non-Git audit events in the UI/API for a rolling window (up to 180 days; Git events shorter), so multi-year retention requires Audit Log Streaming.',
    ),
    'seq_audit_stream_w2': (
        'Enable Git read/clone event streaming to a public unauthenticated HTTP webhook → skip test verification → grant all Organization Members Enterprise Owner to view logs',
        'Audit log streams support vetted encrypted sinks with strict verification, and audit access should use least-privilege custom roles rather than Enterprise Owner.',
    ),
    'seq_audit_stream_w3': (
        'Stream audit logs from a single repository Settings tab → expect enterprise-wide SAML and billing events to appear → disable SAML SSO → delete historical SIEM buckets',
        'Audit log streaming is configured at the **Enterprise** level (capturing enterprise and member-organization events), not on an individual repository tab.',
    ),

    # 10. Enterprise License & Metered Cost Optimization Cycle (D5)
    'seq_license_opt_ok': (
        'Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts',
        'Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.',
    ),
    'seq_license_opt_w1': (
        'Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets',
        'GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.',
    ),
    'seq_license_opt_w2': (
        'Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually',
        'macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.',
    ),
    'seq_license_opt_w3': (
        'Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support',
        'Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.',
    ),
}
