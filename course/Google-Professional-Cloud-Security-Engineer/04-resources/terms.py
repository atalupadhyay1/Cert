"""Option bank for the Professional Cloud Security Engineer practice course.

One label and one meaning per answer or distractor. Keys are stable and
referenced by questions/*.txt; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ------------------------------------------------------------- identity and access
t('cloud_identity', 'Federate the workforce to Cloud Identity and enforce it as the identity source',
  'Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once.')
t('gcds', 'Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync',
  'GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative.')
t('sso_saml', 'Configure single sign-on with a third-party identity provider over SAML',
  'SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session.')
t('super_admin', 'Assign the super administrator role to a dedicated break-glass account with hardware keys',
  'A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account.')
t('super_admin_daily', 'Give every platform lead the super administrator role for convenience',
  'Daily use of the super administrator role removes the separation that makes directory recovery accountable.')
t('admin_sdk_lifecycle', 'Drive joiner, mover, and leaver flows through the Admin SDK Directory API',
  'Automating the lifecycle through the API removes the manual step where access is left behind.')
t('manual_lifecycle', 'Have a team member update accounts by hand when the HR export arrives',
  'A manual update depends on someone remembering, which is exactly where stale access survives.')
t('workforce_federation', 'Federate the partner workforce with Workforce Identity Federation',
  'Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users.')
t('workforce_pool_keys', 'Create a Cloud Identity user per contractor and issue long-lived passwords',
  'A local user per contractor multiplies the accounts that must be reviewed and revoked.')
t('sa_dedicated', 'Create a dedicated service account per workload with only the roles it needs',
  'A per-workload service account bounds the blast radius and makes audit records attributable.')
t('default_sa', 'Run the workload as the default Compute Engine service account',
  'The default service account is shared by every workload on the project, so its grants reach all of them.')
t('sa_key', 'Create a service account key and embed it in the application configuration',
  'A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller.')
t('short_lived_token', 'Issue a short-lived access token through impersonation or metadata',
  'A short-lived token expires on its own, so a leaked value has a bounded window of use.')
t('wif', 'Configure Workload Identity Federation for the external workload',
  'Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk.')
t('wif_key_file', 'Export a service account key and mount it into the external workload',
  'A mounted key file is a long-lived secret sitting inside the system you do not fully control.')
t('wif_attribute_condition', 'Restrict the Workload Identity pool with an attribute condition on the subject',
  'An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens.')
t('impersonation', 'Grant the caller the Service Account Token Creator role on the target account',
  'Impersonation lets a principal act as the service account without holding a key for it.')
t('impersonation_key', 'Hand the caller a JSON key for the service account instead',
  'A handed-out key cannot be scoped to one action and outlives the task that needed it.')
t('password_policy', 'Enforce a password policy with a minimum length and a reuse ban',
  'A password policy raises the cost of credential guessing without depending on the user to choose well.')
t('session_control', 'Set a session length and reauthentication policy for the admin console',
  'A session control limits how long a stolen browser session stays useful.')
t('two_step', 'Enforce 2-step verification for the whole organisation',
  'Enforced 2-step verification turns a stolen password into a partial factor rather than a login.')
t('two_step_optin', 'Let each user decide whether to enrol in 2-step verification',
  'Optional enrolment leaves the accounts that most need the second factor without one.')
t('predefined_role', 'Grant the predefined role that matches the task',
  'A predefined role carries the permissions the task needs and nothing broader.')
t('custom_role', 'Build a custom role containing exactly the permissions the task uses',
  'A custom role is justified when no predefined role is narrow enough, at the cost of maintenance.')
t('basic_role', 'Grant the basic Editor role to the team',
  'The basic roles span every service in the project and cannot express least privilege.')
t('iam_condition', 'Add an IAM condition that limits the grant to a time window and a resource prefix',
  'An IAM condition narrows an existing grant to stated circumstances instead of creating a second role.')
t('deny_policy', 'Attach an IAM deny policy to the organisation',
  'A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced.')
t('acm', 'Write an Access Context Manager access level and bind it to the perimeter',
  'Access Context Manager describes the request context, such as network origin, that a policy can require.')
t('pam', 'Grant the role through Privileged Access Manager with an approval and a time limit',
  'Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears.')
t('jit_standing', 'Grant the privileged role permanently and review it once a year',
  'Permanent privilege is live for every hour of the year, including the hours nobody is watching.')
t('policy_intelligence', 'Read the Policy Analyzer output before removing an unused grant',
  'Policy Intelligence shows who actually used a permission, so a removal is evidence-based.')
t('group_binding', 'Grant the role to a group and manage membership',
  'A group binding keeps the policy small and makes the reviewer look at membership instead of bindings.')
t('role_recommender', 'Apply the Role Recommender suggestion for the oversized role',
  'Role Recommender proposes a narrower role from the permissions the principal actually used.')
t('org_policy', 'Enforce the constraint with an organization policy',
  'An organization policy applies to every project beneath it, so a new project cannot opt out.')
t('org_policy_project', 'Ask each project owner to disable the setting',
  'A per-project request has to be repeated for every new project and is forgotten under pressure.')
t('folder_structure', 'Create a folder per environment and attach the policy at the folder',
  'A folder boundary means one attachment covers every current and future project inside it.')
t('inheritance', 'Rely on policy inheritance from the organisation node',
  'Inheritance carries a grant or constraint down the hierarchy, so the child cannot loosen it.')
t('domain_restricted_sharing', 'Set the domain restricted sharing constraint on the organisation',
  'Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain.')

# ------------------------------------------------------ network and boundary protection
t('ngfw_hierarchical', 'Deploy a hierarchical firewall policy at the organisation or folder level',
  'A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed.')
t('ngfw_project', 'Rely on the default VPC firewall rules in each project',
  'Project-level rules are editable by the project owner and are evaluated after the hierarchy.')
t('ngfw_l7', 'Enable layer 7 inspection on the firewall policy for the egress rule',
  'Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name.')
t('ngfw_l4_only', 'Filter on address and port only and allow the rest',
  'A layer 4 rule cannot see the destination host name inside an allowed connection.')
t('cloud_armor', 'Attach a Cloud Armor security policy to the backend service',
  'Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend.')
t('armor_bot', 'Enable Cloud Armor bot management on the policy',
  'Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run.')
t('waf_app', 'Add a web application firewall rule in the application framework',
  'In-application filtering happens after the request has already consumed backend capacity.')
t('iap', 'Put Identity-Aware Proxy in front of the application',
  'IAP authenticates and authorises each request against IAM before it reaches the backend.')
t('vpn_only', 'Publish the application only through a VPN concentrator',
  'A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app.')
t('lb_tls', 'Terminate TLS at the load balancer with a managed certificate',
  'Terminating at the load balancer gives one managed certificate and a single policy point.')
t('tls_passthrough', 'Pass encrypted traffic straight through to the instance',
  'Pass-through moves certificate lifecycle and cipher policy onto every backend separately.')
t('cas', 'Issue internal certificates from Certificate Authority Service',
  'Certificate Authority Service issues and revokes private certificates with an auditable authority.')
t('self_signed', 'Generate a self-signed certificate on each instance',
  'Self-signed certificates cannot be validated by a client that has no prior trust in them.')
t('secure_web_proxy', 'Route the egress through Secure Web Proxy',
  'Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload.')
t('open_egress', 'Allow all egress and rely on the application to be careful',
  'Unrestricted egress lets a compromised workload reach anything the internet offers.')
t('dns_dnssec', 'Turn on DNSSEC for the public zone',
  'DNSSEC signs the answers so a resolver can detect a forged response.')
t('dns_response_policy', 'Use a Cloud DNS response policy to block the known-bad domain',
  'A response policy overrides resolution for named domains inside the network.')
t('private_ip_only', 'Deploy the instances with internal IP addresses only',
  'An internal-only address means the workload cannot be reached from the internet at all.')
t('api_restriction', 'Restrict the project to the APIs it needs and review them on a schedule',
  'Disabling unused APIs removes an attack surface that no code enables on purpose.')
t('vpc_sc', 'Create a service perimeter with VPC Service Controls',
  'A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant.')
t('vpc_sc_iam_only', 'Rely on IAM to prevent data leaving the project',
  'An IAM grant still permits a copy out of the project; only a perimeter stops the movement.')
t('vpc_peering', 'Peer the two VPC networks and scope the firewall rules to the peer',
  'Peering gives private reachability while firewall rules still decide which flows are allowed.')
t('shared_vpc', 'Host the workload in a Shared VPC service project',
  'Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project.')
t('n_tier_isolation', 'Give each tier its own subnet and allow only the flows between adjacent tiers',
  'Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range.')
t('vpn_ha', 'Build an HA VPN tunnel pair with two interfaces',
  'An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address.')
t('vpn_single', 'Build a single classic VPN tunnel',
  'A single tunnel has no redundancy, so one maintenance window drops the path.')
t('interconnect', 'Provision a Dedicated Interconnect with two attachments',
  'Dedicated Interconnect gives a private circuit with attachments that survive a single link failure.')
t('pga', 'Enable Private Google Access on the subnet',
  'Private Google Access lets an instance with only an internal address reach Google APIs.')
t('psc', 'Publish the service through a Private Service Connect endpoint',
  'A Private Service Connect endpoint gives the consumer a private address for a service in another VPC.')
t('pga_onprem', 'Configure Private Google Access for on-premises hosts over the hybrid route',
  'The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path.')
t('cloud_nat', 'Place Cloud NAT in front of the private instances',
  'Cloud NAT gives the instances outbound connectivity while they keep no external address.')
t('nat_instance', 'Run a NAT instance on a Compute Engine virtual machine',
  'A single NAT instance is a bottleneck and a single point of failure for every outbound flow.')
t('restricted_vip', 'Use restricted.googleapis.com for the API traffic',
  'Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate.')

# ------------------------------------------------------------------ data protection
t('sdp_discovery', 'Run a Sensitive Data Protection discovery scan over the storage and warehouse',
  'A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables.')
t('sdp_manual_sample', 'Ask the team to report which tables they believe hold personal data',
  'A self-reported inventory misses the tables nobody remembered to mention.')
t('sdp_inspect_template', 'Save a Sensitive Data Protection inspect template and reuse it',
  'A saved template keeps the detection rules identical across scans, so results stay comparable.')
t('sdp_redact', 'Redact the matched values with a de-identification template',
  'Redaction replaces the matched value entirely, so the field keeps its shape and loses the data.')
t('sdp_pseudo', 'Replace the value with a pseudonym from a crypto key',
  'Pseudonymisation keeps a stable token so records still join, while the original value is not stored.')
t('sdp_fpe', 'Apply format-preserving encryption to the card number field',
  'Format-preserving encryption keeps the column type and length, so legacy code still reads it.')
t('sdp_plain_hash', 'Replace the value with an unsalted hash',
  'An unsalted hash of a low-entropy value can be reversed with a precomputed table.')
t('dlp_deidentify_template', 'Reuse a stored de-identification template across pipelines',
  'A stored template prevents two pipelines from de-identifying the same column differently.')
t('bq_iam_dataset', 'Grant authorised views or dataset-level IAM rather than table reads',
  'Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed.')
t('bq_table_export', 'Grant the analyst the ability to export the whole table to a bucket',
  'An export right hands over every row, including the columns the analyst should not see.')
t('gcs_iam', 'Grant the bucket role to a group with uniform bucket-level access',
  'Uniform bucket-level access makes IAM the only decision point, so no object ACL can widen it.')
t('gcs_acl_public', 'Set an allUsers object ACL on the specific file',
  'An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy.')
t('sql_iam', 'Use Cloud SQL IAM database authentication for the application',
  'IAM database authentication removes the stored database password and ties each connection to an identity.')
t('sql_password', 'Put the database password in the application config file',
  'A password in a config file is copied into every environment and outlives its owner.')
t('secret_manager', 'Store the credential in Secret Manager and grant the workload the secret accessor role',
  'Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy.')
t('secret_env', 'Set the credential as a plain environment variable in the deployment',
  'An environment variable is visible in the process listing and in the deployment history.')
t('metadata_server', 'Require the metadata server header on every request',
  'Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server.')
t('os_login', 'Enable OS Login and turn off project-wide SSH keys',
  'OS Login ties each login to an identity and removes the shared key that never expires.')
t('gme_encryption', 'Rely on Google default encryption at rest',
  'Google default encryption protects the bytes at rest and needs no key management from the customer.')
t('cmek', 'Encrypt the dataset with a customer-managed key in Cloud KMS',
  'A customer-managed key lets the customer disable the key and stop every read of the data.')
t('ekm', 'Hold the key in Cloud External Key Manager outside Google Cloud',
  'Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself.')
t('key_import', 'Import the wrapping key into Cloud KMS',
  'Key import brings existing key material under KMS control so the old key can still unwrap old objects.')
t('key_rotation', 'Set a rotation period on the key',
  'Rotation issues new key versions on a schedule, which bounds how long one version protects new data.')
t('key_revocation', 'Disable the key version and re-wrap the data',
  'Disabling the version is the mechanism that makes the protected bytes unreadable immediately.')
t('key_in_code', 'Generate the key in the application and store it beside the data',
  'A key stored beside the data gives an attacker both halves of the protection.')
t('confidential_vm', 'Run the workload on a Confidential VM',
  'A Confidential VM keeps memory encrypted while in use, so the host cannot read the data.')
t('confidential_gke', 'Run the pod in a Confidential GKE node pool',
  'Confidential GKE extends in-use memory protection to each pod on the node.')
t('lifecycle_retention', 'Attach an object lifecycle rule that keeps the required retention',
  'A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met.')
t('bucket_lock', 'Apply a retention policy with bucket lock',
  'Bucket lock makes the retention period immutable, so not even an owner can delete early.')
t('bucket_public', 'Make the bucket public but unlisted',
  'An unlisted public bucket is still readable by anyone who learns the object name.')

# ------------------------------------------------------------------- operations
t('cve_scan', 'Add an Artifact Analysis scan to the CI pipeline',
  'Scanning in the pipeline stops the image before it is deployed, not after.')
t('cve_scan_prod', 'Scan the running image in production once a quarter',
  'A quarterly production scan finds the vulnerable image after it has already run.')
t('binary_auth', 'Enforce a Binary Authorization policy that requires an attested image',
  'Binary Authorization refuses to admit an image that lacks the attestation the policy demands.')
t('binary_auth_warn', 'Deploy with Binary Authorization in dry-run mode only',
  'Dry-run records the violation and still admits the image.')
t('hardened_image', 'Build the base image from a hardened source with a documented baseline',
  'A hardened baseline removes the packages and accounts that a general-purpose image ships.')
t('patch_mgmt', 'Schedule patch jobs across the fleet with VM Manager',
  'VM Manager applies and reports operating-system patches on a schedule, with a record of each host.')
t('manual_patch', 'Let each team patch its own instances when convenient',
  'An unmanaged schedule leaves hosts at different patch levels with no fleet view.')
t('sha_custom_module', 'Deploy a Security Health Analytics custom module for the check',
  'A custom module turns a local configuration rule into a recurring finding in Security Command Center.')
t('custom_org_policy', 'Write a custom organization policy constraint for the rule',
  'A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it.')
t('drift_detect', 'Compare the deployed configuration with the intended state on a schedule',
  'A scheduled comparison detects the change that happened outside the pipeline.')
t('flow_logs', 'Enable VPC Flow Logs on the subnets',
  'Flow logs record the accepted and rejected five-tuples for later analysis.')
t('packet_mirroring', 'Mirror the production traffic to a collector with Packet Mirroring',
  'Packet Mirroring copies the packets so a deep inspection appliance can read the payload.')
t('cloud_ids', 'Deploy Cloud IDS on the network',
  'Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises.')
t('log_analytics', 'Query the logs through Log Analytics',
  'Log Analytics turns the sink destination into a queryable store for the correlation.')
t('logging_strategy', 'Route security logs to a dedicated project with its own retention',
  'A dedicated log project keeps the evidence away from the principals who generate it.')
t('log_disable', 'Lower the log volume by disabling data access logs',
  'Disabling data access logs removes the record that shows who read the data.')
t('audit_admin', 'Read the Admin Activity audit log for the change',
  'Admin Activity records the configuration change and the identity that made it, and is always on.')
t('data_access_logs', 'Enable Data Access audit logs for the service',
  'Data Access logs record the read and write of the data itself, and must be turned on per service.')
t('log_sink', 'Create a log sink that routes the entries to the destination',
  'A sink is the routing rule that decides where entries are written.')
t('aggregated_sink', 'Create an aggregated sink at the organisation level',
  'An aggregated sink includes the entries from every project beneath the node in one destination.')
t('project_sink_only', 'Create a sink in each project and hope nobody adds a project',
  'A per-project sink misses every project created after the last one was configured.')
t('siem_export', 'Export the entries to the external SIEM through Pub/Sub',
  'Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation.')
t('siem_pull', 'Give the SIEM a service account key so it can pull the logs',
  'A pulled key sits in a third-party system and cannot be narrowed to one destination.')
t('scc_premium', 'Review the Security Command Center findings for the project',
  'Security Command Center collects the findings from the detectors that are enabled for the tier.')
t('scc_ignore', 'Close the finding as a false positive without a comment',
  'An unexplained closure destroys the record that the finding was ever reviewed.')
t('scc_notify', 'Publish new findings to Pub/Sub for the response pipeline',
  'A notification channel lets the response automation react to a finding as it is created.')

# ------------------------------------------------------------------ compliance
t('shared_responsibility', 'Document which controls Google operates and which the customer must implement',
  'The shared responsibility split decides what the customer actually has to evidence.')
t('shared_all_google', 'Assume Google secures every layer once the data is in the cloud',
  'The provider secures the infrastructure, not the configuration the customer writes on top of it.')
t('assured_workloads', 'Create the folder as an Assured Workloads environment',
  'Assured Workloads applies the personnel and location controls the regime requires to the folder.')
t('assured_manual', 'Record the regime in a spreadsheet and configure each control by hand',
  'A manual mapping drifts the moment a new project is created without the same settings.')
t('access_transparency', 'Turn on Access Transparency and read its logs',
  'Access Transparency records the occasions when a Google operator accesses customer content.')
t('access_approval', 'Require Access Approval before an operator may read the content',
  'Access Approval turns the operator access into a request the customer must grant.')
t('regionalization', 'Constrain the resources to the required region with a location organization policy',
  'A location constraint blocks the resource from being created outside the permitted region.')
t('global_default', 'Leave the default multi-region setting',
  'A multi-region default places the copy outside the region the regulator named.')
t('compliance_mapping', 'Map each requirement to the control that satisfies it and the evidence it produces',
  'A mapping shows the auditor which control answers which clause and where the evidence lives.')
t('compliance_assertion', 'State in the policy document that the environment is compliant',
  'An assertion without the control and the evidence is not something an auditor can test.')
t('scope_boundary', 'Draw the compliance boundary around the projects and services that hold the regulated data',
  'A written boundary decides which resources are in scope and which are out, before the audit begins.')
t('scope_everything', 'Declare the whole organisation in scope for every regime',
  'An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter.')
t('evidence_retention', 'Keep the audit evidence for the period the regime requires',
  'A retention period for evidence is itself a control, because an expired record proves nothing.')
t('control_owner', 'Name an owner for each control',
  'A named owner is what turns a control list into something that is actually operated.')
