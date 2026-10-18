"""Builder for SAA-C03 Set 2 — Domain 1 Secure Architectures deep dive (200q) + HealthFirst case study.

Set 2 is a deep dive on Domain 1 (Secure Architectures, 30% of the real exam).
- 200 questions total
- 20% multi-select = 40 questions
- 20 case-study questions referencing HealthFirst
- Distribution: ~80% Secure, plus 20% Resilient/High-Performing/Cost-Opt for realism (multi-domain scenarios)
"""

import csv

# Domain strings (must match exactly)
SECURE = "Design Secure Architectures"
RESILIENT = "Design Resilient Architectures"
HIGH_PERF = "Design High-Performing Architectures"
COST_OPT = "Design Cost-Optimized Architectures"


def make_row(question, qtype, opts, correct, overall, domain):
    """Build a row. opts is a list of (text, explanation) tuples. correct is 1-based string like '1' or '1,3'."""
    while len(opts) < 6:
        opts.append(("", ""))
    row = [question, qtype]
    for text, expl in opts:
        row.extend([text, expl])
    row.append(correct)
    row.append(overall)
    row.append(domain)
    return row


QUESTIONS = []

# ============================================================
# IAM (35 questions)
# ============================================================

# --- IAM core (15) ---
QUESTIONS.append({
    "q": "Which IAM entity is the BEST choice for granting an EC2 instance temporary AWS credentials to call AWS APIs without embedding long-lived access keys?",
    "type": "multiple-choice",
    "opts": [
        ("IAM user with access keys", "IAM users have long-lived static keys, which is the antipattern the question is trying to avoid."),
        ("IAM role attached to the EC2 instance", "IAM roles for EC2 deliver temporary credentials via the instance metadata service, no keys to manage."),
        ("IAM group with permission policy", "IAM groups are collections of users, not assignable to EC2 instances."),
        ("AWS service control policy (SCP)", "SCPs set permission boundaries across an AWS Organization, not credentials for a single EC2 instance."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Attach an IAM role to the EC2 instance. The instance obtains temporary credentials via IMDSv2; no long-lived keys are stored on the host. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html",
})
QUESTIONS.append({
    "q": "Which IAM evaluation logic correctly applies when an explicit Deny is set in an identity-based policy?",
    "type": "multiple-choice",
    "opts": [
        ("An explicit Deny overrides any Allow", "Correct — an explicit Deny always wins, regardless of any Allow elsewhere."),
        ("An Allow overrides a Deny if the Allow is more specific", "Specificity does not override an explicit Deny."),
        ("IAM rejects all Deny statements in identity-based policies", "Deny is a first-class IAM statement."),
        ("Deny is evaluated only when there is no matching Allow", "Order of evaluation does not depend on Allow presence."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM evaluation logic: by default all requests are denied, an Allow permits, and an explicit Deny always overrides any Allow. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html",
})
QUESTIONS.append({
    "q": "Which IAM policy evaluation rule correctly describes what happens when no Allow statement matches a request?",
    "type": "multiple-choice",
    "opts": [
        ("The request is implicitly denied", "Default-deny: a request is denied unless an explicit Allow matches."),
        ("The request is allowed if no Deny matches", "A request is denied unless explicitly allowed."),
        ("The request is allowed at root", "Root has no implicit allow."),
        ("The request is sent for manual approval", "IAM has no manual approval flow."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM is default-deny: a request is denied unless it is explicitly allowed by an applicable policy. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html",
})
QUESTIONS.append({
    "q": "Which type of IAM policy is embedded directly inside a single IAM identity and cannot be reused across identities?",
    "type": "multiple-choice",
    "opts": [
        ("AWS managed policy", "AWS managed policies are reusable and managed by AWS."),
        ("Customer managed policy", "Customer managed policies are reusable within your account."),
        ("Inline policy", "Inline policies are 1:1 with a single identity."),
        ("Service control policy", "SCPs are attached to OUs/accounts, not identities."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "Inline policies are embedded in a single IAM identity (user, group, or role) and are deleted when the identity is deleted. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html",
})
QUESTIONS.append({
    "q": "A developer needs read-only access to all S3 buckets in the account. Which is the SIMPLEST policy to attach?",
    "type": "multiple-choice",
    "opts": [
        ("AWS managed policy AmazonS3ReadOnlyAccess", "The AWS managed read-only policy is the simplest one-step grant."),
        ("A custom inline policy listing every bucket", "Listing every bucket is not required for read access."),
        ("AdministratorAccess with a Deny on s3:DeleteObject", "Overly broad; not the simplest answer."),
        ("S3 bucket policy on each bucket", "Bucket policies scale poorly and are not the simplest pattern."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS managed policies are the simplest way to grant common permissions like S3 read-only. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html",
})
QUESTIONS.append({
    "q": "Which statement correctly describes how IAM roles are assumed across accounts using a trust policy?",
    "type": "multiple-choice",
    "opts": [
        ("The trust policy in the trusting account specifies who can assume the role", "The trust policy lives on the role in the trusting account and defines the principals allowed to assume it."),
        ("The role's permission policy controls who can assume it", "The permission policy controls what the role can do once assumed, not who can assume it."),
        ("A role cannot be assumed across accounts", "Cross-account role assumption is a primary IAM pattern."),
        ("Trust policies are written in YAML only", "Trust policies are JSON."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "The trust policy on the role in the trusting account specifies which principals (accounts, users, services) may assume the role. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
})
QUESTIONS.append({
    "q": "Which SINGLE IAM practice is MOST critical for an application using long-lived IAM access keys to access S3?",
    "type": "multiple-choice",
    "opts": [
        ("Rotate access keys regularly (e.g., every 90 days)", "Regular rotation limits the blast radius of a leaked key."),
        ("Store access keys in AWS Secrets Manager and retrieve at runtime", "Centralized secret storage with rotation and audit."),
        ("Embed the access key in the application source code", "Embedding keys in source is a critical security antipattern."),
        ("Apply least-privilege IAM policies scoped to required actions and resources", "Least-privilege reduces the impact of key compromise."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Best practice: rotate keys, store in Secrets Manager, apply least privilege. Avoid embedding keys in source. Better: replace keys with IAM roles entirely. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which IAM role type is designed specifically for workloads running OUTSIDE AWS (on-premises, other clouds) to obtain short-lived AWS credentials using X.509 certificates?",
    "type": "multiple-choice",
    "opts": [
        ("IAM Role for EC2", "EC2 roles are for instances running in AWS."),
        ("IAM Roles Anywhere", "Roles Anywhere extends IAM roles to external workloads via X.509."),
        ("AWS service-linked role", "Service-linked roles are for AWS services to call other AWS services."),
        ("Cross-account role", "Cross-account roles are for one AWS account to access another."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "IAM Roles Anywhere issues short-lived credentials to external workloads using X.509 certificates, eliminating long-lived keys. Reference: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html",
})
QUESTIONS.append({
    "q": "Which IAM Access Analyzer feature analyzes access patterns and generates least-privilege policies based on actual service usage?",
    "type": "multiple-choice",
    "opts": [
        ("IAM Access Analyzer policy generation", "Access Analyzer policy generation creates policies from observed CloudTrail activity."),
        ("IAM Policy Simulator", "Policy Simulator tests whether a policy grants or denies specific actions."),
        ("AWS CloudTrail Insights", "CloudTrail Insights detects unusual API activity."),
        ("AWS Config", "Config is for resource configuration compliance."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM Access Analyzer policy generation reviews CloudTrail logs and generates least-privilege IAM policies based on actual access patterns. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html",
})
QUESTIONS.append({
    "q": "Which IAM Access Analyzer feature continuously monitors resources (S3 buckets, IAM roles, KMS keys, SQS queues) for any access granted to an external principal?",
    "type": "multiple-choice",
    "opts": [
        ("Policy validation", "Policy validation checks for syntax and policy best practices."),
        ("Finding generation", "Access Analyzer findings flag resources accessible from outside the zone of trust."),
        ("Unused access analysis", "Unused access analysis flags permissions that are granted but not used."),
        ("Password policy analysis", "Access Analyzer does not analyze password policies."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "IAM Access Analyzer finding generation continuously monitors resources for any policy that grants access to an external principal. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html",
})
QUESTIONS.append({
    "q": "Which SINGLE element is REQUIRED in the trust policy to allow a SAML IdP to federate a user to AWS console?",
    "type": "multiple-choice",
    "opts": [
        ("A SAML 2.0 identity provider configured in IAM", "SAML IdP is required for SAML federation."),
        ("An IAM role with a trust policy allowing the SAML IdP", "The role's trust policy allows the IdP to assume it."),
        ("AWS WAF", "WAF is for web app traffic, not identity federation."),
        ("An IAM user with a login profile and password", "Federated users do not need an IAM user."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "SAML federation requires a SAML IdP in IAM and an IAM role whose trust policy allows the IdP. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html",
})
QUESTIONS.append({
    "q": "Which IAM role trust policy element is REQUIRED to allow an AWS service (such as EC2 or Lambda) to assume the role?",
    "type": "multiple-choice",
    "opts": [
        ("Principal set to the service (e.g., ec2.amazonaws.com)", "Service principals must be in the trust policy to allow service role assumption."),
        ("Statement Sid starting with AWS", "Sid is optional and not service-specific."),
        ("Effect: Allow on sts:AssumeRole with the service principal", "Yes, with the service principal as Principal in the trust policy."),
        ("Condition with aws:SourceAccount", "SourceAccount is optional and for additional security."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "Service role trust policies must have Effect: Allow on sts:AssumeRole and Principal set to the service principal. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html",
})
QUESTIONS.append({
    "q": "Which feature lets you delegate permissions to a specific principal for a LIMITED time, without modifying the IAM key policy?",
    "type": "multiple-choice",
    "opts": [
        ("KMS grant", "KMS grants delegate permissions to a CMK for a limited time."),
        ("IAM role", "Roles are not bound to a CMK."),
        ("IAM policy", "IAM policies are not delegated to a key."),
        ("Resource-based policy", "Resource-based policies are static, not time-bounded."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "KMS grants delegate permissions to use a CMK to another principal for a limited time, without modifying the key policy. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/grants.html",
})
QUESTIONS.append({
    "q": "Which IAM policy type is attached to an AWS Organization OU and limits the MAXIMUM permissions that member accounts can use?",
    "type": "multiple-choice",
    "opts": [
        ("Service control policy (SCP)", "SCPs are the guardrails in AWS Organizations."),
        ("Identity-based policy", "Identity-based policies grant, not restrict."),
        ("Session policy", "Session policies restrict a single role session, not the entire account."),
        ("Permissions boundary", "Permissions boundaries are attached to principals."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Service control policies (SCPs) are the guardrails in AWS Organizations that define the maximum permissions for member accounts. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
})
QUESTIONS.append({
    "q": "Which SINGLE approach is the BEST pattern for granting cross-account access to AWS resources?",
    "type": "multiple-choice",
    "opts": [
        ("Use an IAM role with a trust policy in the target account", "Role assumption is the standard cross-account pattern."),
        ("Use resource-based policies (e.g., bucket policy) on the target resource", "Resource policies can grant cross-account access directly."),
        ("Share long-lived IAM user access keys between accounts", "Sharing static keys is a security antipattern and is not the recommended mechanism."),
        ("Use AWS Resource Access Manager (RAM)", "RAM shares supported resources across accounts."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Cross-account access can be granted via IAM role assumption, resource-based policies, and AWS RAM. Sharing IAM user keys is an antipattern. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html",
})
QUESTIONS.append({
    "q": "Which SINGLE practice is the BEST baseline for managing IAM users?",
    "type": "multiple-choice",
    "opts": [
        ("Enable MFA for privileged users", "MFA is a security baseline for privileged users."),
        ("Rotate access keys regularly", "Long-lived keys should be rotated and ideally eliminated in favor of roles."),
        ("Share root user credentials with the team", "The root user must be locked away; never share."),
        ("Use IAM Identity Center (SSO) instead of individual IAM users", "IAM Identity Center centralizes workforce access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Best practices: enable MFA, rotate keys, prefer IAM Identity Center, and never use the root user for daily work. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature of AWS IAM Identity Center is the core workforce SSO capability?",
    "type": "multiple-choice",
    "opts": [
        ("AWS IAM Identity Center", "IAM Identity Center is the centralized SSO service for AWS and SaaS apps."),
        ("Amazon Cognito", "Cognito is for end-user identity, not workforce SSO."),
        ("AWS Directory Service", "Directory Service provides managed AD, not workforce SSO."),
        ("AWS IAM", "IAM does not provide centralized SSO."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS IAM Identity Center is the centralized SSO service for workforce access to AWS accounts and SaaS apps. Reference: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Organizations allows you to group accounts into a logical hierarchy and apply policies to the group?",
    "type": "multiple-choice",
    "opts": [
        ("Organizational unit (OU)", "OUs are containers for accounts that share policies."),
        ("Service control policy (SCP) alone", "SCPs are attached to OUs, not the other way around."),
        ("AWS Control Tower", "Control Tower is for multi-account governance; OU is the underlying construct."),
        ("AWS Resource Access Manager", "RAM shares resources, not policies."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Organizational units (OUs) group accounts in AWS Organizations and allow policies to be applied to the group. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service provides user pools for end-user authentication with social IdP support?",
    "type": "multiple-choice",
    "opts": [
        ("Single sign-on to AWS accounts and business applications", "SSO to AWS accounts and SaaS apps."),
        ("Integration with SAML 2.0 and OIDC identity sources", "IdP integration via SAML and OIDC."),
        ("Built-in Active Directory replacement", "Identity Center is not a directory."),
        ("Permission sets to map groups to AWS roles", "Permission sets drive role-based access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM Identity Center provides SSO, integrates with SAML/OIDC, and uses permission sets to map groups to AWS roles. Reference: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides user pools for end-user authentication (B2C/B2B) and identity pools for AWS credential exchange?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Cognito", "Cognito user pools and identity pools are the standard for B2C and B2B app auth."),
        ("AWS Directory Service", "Directory Service is for enterprise AD, not consumer identity."),
        ("AWS IAM", "IAM is for AWS resource access, not consumer app sign-in."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon Cognito provides user pools (authN) and identity pools (authZ to AWS resources) for web and mobile apps. Reference: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed Microsoft Active Directory in AWS, including AD Connector for integrating with on-premises AD?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Directory Service", "Directory Service offers Managed Microsoft AD, AD Connector, and Simple AD."),
        ("Amazon Cognito", "Cognito is for end-user identity, not enterprise AD."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO, not an AD."),
        ("AWS SSO", "AWS SSO is now IAM Identity Center."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Directory Service provides Managed Microsoft AD, AD Connector, and Simple AD. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html",
})
QUESTIONS.append({
    "q": "Which SINGLE element is REQUIRED to enable SAML 2.0 federation for AWS console access?",
    "type": "multiple-choice",
    "opts": [
        ("Create a SAML identity provider in IAM", "The SAML IdP is the bridge between the corporate IdP and AWS."),
        ("Create an IAM role with a trust policy allowing the SAML provider", "The role allows federated users to act in AWS."),
        ("Create a Cognito user pool", "Cognito is for app auth, not SAML console federation."),
        ("Use the root user to share credentials", "Sharing root user credentials is a security antipattern."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "SAML console federation requires a SAML IdP in IAM and an IAM role with a trust policy for the IdP. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS IAM allows you to grant a USER temporary privileges to act as another principal without sharing long-lived credentials?",
    "type": "multiple-choice",
    "opts": [
        ("IAM role assumption", "Users assume roles to get temporary credentials."),
        ("IAM user delegation", "IAM user delegation is not an AWS feature."),
        ("Access key sharing", "Sharing access keys is an antipattern."),
        ("Resource policy", "Resource policies are attached to resources, not users."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM role assumption provides users with temporary credentials to act as a different principal. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html",
})
QUESTIONS.append({
    "q": "Which IAM Access Analyzer unused access analysis report helps you identify permissions that have NOT been used in a specified period?",
    "type": "multiple-choice",
    "opts": [
        ("Findings for unused access", "Access Analyzer reports unused access at user and account level."),
        ("Findings for external access", "External access findings flag resources accessible from outside."),
        ("Findings for policy validation", "Policy validation checks syntax and best practices."),
        ("Findings for credential exposure", "Access Analyzer does not monitor credential exposure."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM Access Analyzer unused access analysis identifies permissions that have not been used in a specified period. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-unused-access.html",
})
QUESTIONS.append({
    "q": "Which SINGLE IAM condition key is used to restrict API calls to those from a specific VPC endpoint?",
    "type": "multiple-choice",
    "opts": [
        ("Require MFA on individual IAM users", "Per-user MFA enforcement."),
        ("Use an SCP to require MFA for sensitive actions", "SCPs can require MFA conditions in member accounts."),
        ("Disable MFA enforcement globally", "Disabling MFA is a security antipattern."),
        ("Use IAM Identity Center to enforce MFA at the IdP", "IdP-side MFA enforcement."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Enforce MFA per-user, via SCP, or at the IdP. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
})
QUESTIONS.append({
    "q": "Which IAM feature sets a MAXIMUM set of permissions that an IAM user or role can assume, even if their identity policy grants more?",
    "type": "multiple-choice",
    "opts": [
        ("Permissions boundary", "Permissions boundaries define the maximum permissions an identity can have."),
        ("Service control policy", "SCPs are for organization-level guardrails."),
        ("Session policy", "Session policies restrict a single role session."),
        ("Identity-based policy", "Identity-based policies grant, not restrict."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "An IAM permissions boundary is an advanced feature that sets the maximum permissions an IAM user or role can have. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
})
QUESTIONS.append({
    "q": "Which SINGLE scenario is the BEST use case for IAM permissions boundaries?",
    "type": "multiple-choice",
    "opts": [
        ("Delegating admin to set permissions within a maximum boundary", "Common pattern: developers set identity policies; boundary defines the max."),
        ("Restricting a privileged user to specific roles only", "Boundaries limit the maximum permissions."),
        ("Replacing all other forms of access control", "Boundaries are a layer, not a replacement."),
        ("Allowing access to any AWS service by default", "Boundaries restrict; they don't grant."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Permissions boundaries are useful for delegating admin and restricting privileged users. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
})
QUESTIONS.append({
    "q": "Which IAM feature allows passing a JSON policy as a parameter when assuming a role, to FURTHER restrict what the role session can do?",
    "type": "multiple-choice",
    "opts": [
        ("Session policy", "Session policies restrict a single role session."),
        ("Identity-based policy", "Identity policies are not passed at assume-role time."),
        ("Resource policy", "Resource policies are attached to resources, not sessions."),
        ("Boundary policy", "Boundary policies are attached to identities."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Session policies are advanced policies passed when assuming a role that further restrict the session's permissions. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session",
})
QUESTIONS.append({
    "q": "Which AWS feature allows you to enable MFA for the AWS account ROOT user, with up to 8 MFA devices?",
    "type": "multiple-choice",
    "opts": [
        ("IAM MFA for root user", "Root MFA is the highest-leverage security control in AWS."),
        ("AWS WAF", "WAF is for web app traffic."),
        ("AWS Shield", "Shield is for DDoS protection."),
        ("AWS GuardDuty", "GuardDuty is a threat detection service."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Enable MFA for the root user with up to 8 devices (U2F security key, hardware, virtual). Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa",
})
QUESTIONS.append({
    "q": "Which SINGLE rotation option is the BEST choice for a customer managed CMK?",
    "type": "multiple-choice",
    "opts": [
        ("Virtual MFA device (e.g., Google Authenticator, Authy)", "Virtual MFA apps are supported."),
        ("U2F security key (e.g., YubiKey)", "U2F security keys are supported."),
        ("Hardware MFA token (e.g., Gemalto)", "Hardware TOTP tokens are supported."),
        ("SMS-based one-time password", "SMS-based MFA is not supported in AWS IAM."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS supports virtual MFA, U2F security keys, and hardware TOTP tokens. SMS is not supported. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides credential reports that list all IAM users in your account and the status of their credentials (password, access keys, MFA)?",
    "type": "multiple-choice",
    "opts": [
        ("IAM credential report", "IAM credential reports provide a periodic CSV of all user credentials."),
        ("AWS Config", "Config tracks resource configuration."),
        ("AWS CloudTrail", "CloudTrail records API calls."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM credential reports provide a periodic CSV listing all IAM users and their credential status. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS STS API is the BEST choice for obtaining temporary credentials via AssumeRole?",
    "type": "multiple-choice",
    "opts": [
        ("AssumeRole", "AssumeRole is for cross-account or role chaining."),
        ("AssumeRoleWithSAML", "AssumeRoleWithSAML is for SAML federation."),
        ("AssumeRoleWithWebIdentity", "AssumeRoleWithWebIdentity is for OIDC federation."),
        ("GetSessionToken", "GetSessionToken returns short-lived credentials for an IAM user or root user."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS STS supports AssumeRole, AssumeRoleWithSAML, AssumeRoleWithWebIdentity, GetSessionToken, and GetFederationToken. Reference: https://docs.aws.amazon.com/STS/latest/APIReference/API_Operations.html",
})
QUESTIONS.append({
    "q": "Which feature lets you REQUIRE that IAM users or roles can only be used when the request comes from a specific IP range, VPC endpoint, or AWS service?",
    "type": "multiple-choice",
    "opts": [
        ("IAM policy Condition element", "IAM Condition keys can enforce IP, VPC, and other constraints."),
        ("SCP without conditions", "SCPs without conditions apply blanket deny or allow."),
        ("Permissions boundary", "Boundaries are for max-permission, not context."),
        ("Session policy alone", "Session policies alone are not enough; Condition is more flexible."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "The IAM policy Condition element enforces context-aware access (IP, VPC, MFA, time, etc.). Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html",
})
QUESTIONS.append({
    "q": "Which condition key restricts API calls to those made from within a specific VPC or VPC endpoint?",
    "type": "multiple-choice",
    "opts": [
        ("aws:SourceVpce", "aws:SourceVpce restricts to calls from a specific VPC endpoint."),
        ("aws:SourceIp", "aws:SourceIp restricts to specific IPs."),
        ("aws:CalledVia", "aws:CalledVia identifies which service made the call on behalf of the user."),
        ("aws:RequestedRegion", "aws:RequestedRegion restricts by region."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "aws:SourceVpce restricts API calls to those originating from a specific VPC endpoint. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcevpce",
})
QUESTIONS.append({
    "q": "Which SINGLE pattern of envelope encryption is the BEST for protecting a large dataset?",
    "type": "multiple-choice",
    "opts": [
        ("Set short session durations for assumed roles", "Short session durations limit the window of exposure."),
        ("Use long-lived access keys", "Long-lived keys have a long exposure window."),
        ("Disable CloudTrail logging", "Disabling logging is a security antipattern."),
        ("Disable MFA enforcement", "Disabling MFA removes a critical control."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Set short session durations (e.g., 1 hour) for assumed roles to limit the window of exposure for compromised credentials. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage.html",
})
QUESTIONS.append({
    "q": "Which KMS key type offers the MOST control over rotation, aliasing, and key policy, and is the BEST choice for sensitive workloads?",
    "type": "multiple-choice",
    "opts": [
        ("AWS managed key (aws/* service key)", "AWS managed keys are managed by AWS; you cannot change their key policy or rotation in detail."),
        ("Customer managed key (CMK)", "CMKs give you full control over key policy, rotation, and grants."),
        ("AWS owned key", "AWS owned keys are not visible in your account; you cannot manage them."),
        ("Plaintext key in Secrets Manager", "Plaintext is not a KMS option."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Customer managed CMKs give you control over key policies, rotation, and grants — the right choice for sensitive workloads. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms-keys",
})
QUESTIONS.append({
    "q": "Which encryption pattern uses a customer master key to encrypt a data key, which is then used to encrypt the data?",
    "type": "multiple-choice",
    "opts": [
        ("Client-side hashing", "Hashing is one-way, not encryption."),
        ("Envelope encryption", "Envelope encryption uses a KMS CMK to wrap a data encryption key."),
        ("Server-side transparent encryption", "Uses AWS-managed keys transparently, not the described pattern."),
        ("Tokenization", "Tokenization replaces the value with a token, not encryption."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Envelope encryption: a KMS CMK wraps (encrypts) a data key, and the data key encrypts the actual data, providing both performance and key management benefits. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping",
})
QUESTIONS.append({
    "q": "Which SINGLE option is the BEST for rotating a customer managed CMK?",
    "type": "multiple-choice",
    "opts": [
        ("Automatic annual rotation for CMKs", "Customer managed CMKs can be configured for automatic annual rotation."),
        ("Manual rotation by creating a new CMK alias", "Manual rotation is possible by creating a new key and aliasing."),
        ("Rotating AWS managed keys", "AWS managed keys are rotated automatically by AWS; you cannot configure them."),
        ("Rotating AWS owned keys", "AWS owned keys are not visible to you; rotation is fully AWS-managed."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Customer managed CMKs can be configured for automatic annual rotation, or rotated manually. AWS managed and AWS owned keys are not user-controllable. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html",
})
QUESTIONS.append({
    "q": "Which KMS grant element allows a principal to use a CMK for a specific action without modifying the key policy?",
    "type": "multiple-choice",
    "opts": [
        ("Key policy", "Key policy is the primary resource policy, not a grant."),
        ("Grant", "Grants are programmatic, time-bounded delegations attached to a key."),
        ("IAM policy", "IAM policies are identity-based, not key-level grants."),
        ("SCP", "SCPs are org-wide, not per-key."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "KMS grants provide programmatic, time-bounded, action-scoped access to a CMK without modifying the key policy. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/grants.html",
})
QUESTIONS.append({
    "q": "Which SINGLE approach is the BEST for enabling encryption at rest for an EXISTING unencrypted RDS instance?",
    "type": "multiple-choice",
    "opts": [
        ("Enable default bucket encryption with SSE-KMS and a CMK", "Default bucket encryption with SSE-KMS using a CMK encrypts all new objects automatically."),
        ("Encrypt each object manually in the application", "Manual encryption is error-prone and not the simplest option."),
        ("Use SSE-S3 with AES256", "SSE-S3 uses AWS-managed S3 keys, not a customer managed KMS key."),
        ("Disable server-side encryption and use client-side only", "Client-side only is not the simplest option."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Configure default bucket encryption with SSE-KMS and select a customer managed CMK to encrypt all new objects automatically. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html",
})
QUESTIONS.append({
    "q": "Which SINGLE characteristic is the BEST description of AWS KMS HSM-backed keys?",
    "type": "multiple-choice",
    "opts": [
        ("FIPS 140-3 Level 3 validated", "CloudHSM-backed custom key stores are FIPS 140-3 Level 3 validated."),
        ("Single-tenant key storage in hardware", "HSM keys reside in a single-tenant HSM cluster."),
        ("Free of charge", "CloudHSM and CMKs are billed per key and API call."),
        ("Generate and use keys without leaving the HSM", "Custom key store keys never leave the HSM boundary."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Custom key stores backed by CloudHSM provide FIPS 140-3 Level 3, single-tenant HSM key storage, where keys never leave the HSM. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html",
})
QUESTIONS.append({
    "q": "Which AWS service lets you audit KMS key usage to detect who used which key and when?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch Logs only", "CloudWatch Logs is for application logs, not KMS API calls."),
        ("AWS CloudTrail", "CloudTrail records all KMS API calls including Decrypt, Encrypt, GenerateDataKey."),
        ("AWS Config only", "Config records configuration changes, not all API calls."),
        ("Amazon Athena only", "Athena is a query engine."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS CloudTrail captures all KMS API calls for audit and compliance. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html",
})
QUESTIONS.append({
    "q": "Which KMS API call is used to decrypt ciphertext that is less than 4 KB?",
    "type": "multiple-choice",
    "opts": [
        ("Decrypt", "Decrypt handles data keys and small ciphertext up to 4 KB."),
        ("GenerateDataKey", "Generates a data key, does not decrypt."),
        ("ReEncrypt", "Re-encrypts with a different key, doesn't decrypt directly."),
        ("DescribeKey", "Returns metadata, no decrypt."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "The KMS Decrypt API decrypts ciphertext up to 4 KB; for larger data, decrypt the data key instead and use it locally. Reference: https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html",
})
QUESTIONS.append({
    "q": "Which SINGLE practice is the BEST baseline for AWS KMS key management?",
    "type": "multiple-choice",
    "opts": [
        ("Use least-privilege key policies", "Restrict the key policy to only the principals that need to use the key."),
        ("Enable automatic key rotation for CMKs", "Annual rotation limits exposure if a key is compromised."),
        ("Embed KMS keys in application source code", "Embedding keys in source is a critical security antipattern."),
        ("Use aliases for key management", "Aliases simplify key management without breaking applications."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Best practices: least-privilege key policies, enable rotation, use aliases. Never embed keys in source. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which SINGLE option is the BEST choice for storing application secrets?",
    "type": "multiple-choice",
    "opts": [
        ("Key policy with cross-account grants", "Key policy can grant cross-account access via principal ARNs."),
        ("Default key policy is global", "Default key policies are account-scoped, not global."),
        ("KMS grants without trust", "Grants must specify the grantee principal."),
        ("KMS key access list", "There is no such KMS concept."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Key policies can grant cross-account access to other AWS accounts by including the account ARN in the Principal element. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html",
})
QUESTIONS.append({
    "q": "Which SINGLE combination is the BEST fit for customer-managed, FIPS 140-3 Level 3 key storage?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudHSM", "CloudHSM provides FIPS 140-3 Level 3 HSMs in your account."),
        ("AWS KMS custom key store", "Custom key stores integrate CloudHSM clusters with KMS."),
        ("AWS Secrets Manager alone", "Secrets Manager uses KMS, but does not provide HSM key storage by itself."),
        ("AWS Trusted Advisor", "Trusted Advisor does not provide key storage."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS CloudHSM + KMS custom key store provides FIPS 140-3 Level 3 HSM-backed CMKs. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html",
})
QUESTIONS.append({
    "q": "Which KMS API call returns a plaintext data key AND a ciphertext copy of the data key, for use in envelope encryption?",
    "type": "multiple-choice",
    "opts": [
        ("GenerateDataKey", "GenerateDataKey returns both plaintext and ciphertext of the data key."),
        ("Encrypt", "Encrypt encrypts data; does not return a plaintext data key."),
        ("Decrypt", "Decrypt decrypts; does not generate a data key."),
        ("CreateAlias", "CreateAlias is for naming, not data keys."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "GenerateDataKey returns both plaintext and ciphertext of the data key, enabling envelope encryption. Reference: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html",
})
QUESTIONS.append({
    "q": "Which KMS API call returns ONLY the ciphertext of a data key, suitable for users that should never see the plaintext?",
    "type": "multiple-choice",
    "opts": [
        ("GenerateDataKeyWithoutPlaintext", "Returns only the ciphertext, never the plaintext."),
        ("GenerateDataKey", "Returns both plaintext and ciphertext."),
        ("Encrypt", "Encrypt is for general encryption, not data key generation."),
        ("Decrypt", "Decrypt decrypts, not generate."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "GenerateDataKeyWithoutPlaintext returns only the ciphertext of the data key, suitable for users that should never see the plaintext. Reference: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html",
})
QUESTIONS.append({
    "q": "Which SINGLE control is the BEST to prevent accidental KMS key deletion?",
    "type": "multiple-choice",
    "opts": [
        ("Set a pending window for key deletion (7-30 days)", "Pending window allows time to cancel accidental deletion."),
        ("Use resource policies and IAM policies to restrict who can schedule deletion", "Restrict via IAM and key policy."),
        ("Disable deletion for the CMK permanently via console", "Deletion cannot be permanently disabled; only delayed."),
        ("Enable MFA delete for the CMK", "MFA delete adds an extra layer of protection for key deletion."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use a pending deletion window, restrict via IAM, and enable MFA delete. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html",
})
QUESTIONS.append({
    "q": "Which SINGLE S3 encryption option uses customer-supplied keys?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudHSM", "CloudHSM provides single-tenant, FIPS 140-3 Level 3 HSM clusters."),
        ("AWS KMS", "KMS is multi-tenant shared HSMs; CloudHSM is single-tenant."),
        ("AWS Macie", "Macie is for data classification."),
        ("AWS Secrets Manager", "Secrets Manager is for secrets, not HSMs."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS CloudHSM provides single-tenant HSM clusters with FIPS 140-3 Level 3 validation. Reference: https://docs.aws.amazon.com/cloudhsm/latest/userguide/what-is-cloudhsm.html",
})
QUESTIONS.append({
    "q": "Which combination of encryption options provides ENCRYPTION AT REST and IN TRANSIT for an RDS database? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Enable storage encryption on the RDS instance with a KMS key", "Storage encryption is at-rest encryption."),
        ("Use TLS to connect to the database endpoint", "TLS is in-transit encryption."),
        ("Enable IAM database authentication with no encryption", "IAM auth does not provide encryption at rest."),
        ("Configure automated minor version upgrades", "Upgrades are unrelated to encryption."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "RDS supports encryption at rest via storage encryption and encryption in transit via TLS. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
})
QUESTIONS.append({
    "q": "Which of the following are required to enable encryption at rest for an EXISTING unencrypted RDS DB instance?",
    "type": "multiple-choice",
    "opts": [
        ("Add a new encrypted replica and promote it", "Encryption is set at create time on the original instance; you must create an encrypted copy and promote."),
        ("Modify the existing instance in-place", "You cannot enable encryption in-place on an existing instance."),
        ("Stop and start the instance", "Stop/start does not change encryption state."),
        ("Enable encryption via the console toggle", "No in-place toggle exists; you must create a snapshot copy with encryption and restore."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "RDS encryption is set at create time. To encrypt an existing instance, snapshot it, copy the snapshot with encryption, and restore. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automatic rotation of KMS-encrypted secrets with audit logging, and supports RDS integration?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager", "Secrets Manager integrates with RDS for automatic rotation and audit logging."),
        ("AWS KMS alone", "KMS manages keys, not rotation of secrets."),
        ("AWS Systems Manager Parameter Store only", "Parameter Store supports manual rotation and some Lambda-based rotation, not native RDS."),
        ("AWS IAM", "IAM does not store database credentials."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Secrets Manager integrates with RDS and Aurora to automatically rotate database credentials with audit logging. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets.html",
})
QUESTIONS.append({
    "q": "Which SINGLE option is the BEST for storing application secrets like DB credentials?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager", "Secrets Manager for rotation, fine-grained access, and audit."),
        ("AWS Systems Manager Parameter Store (SecureString)", "Parameter Store SecureString with KMS for parameter values."),
        ("Environment variables in plaintext source code", "Plaintext env vars in source code is a security antipattern."),
        ("AWS KMS directly as a secrets store", "KMS is for encryption keys, not secret strings."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use Secrets Manager or Parameter Store SecureString for application secrets. Avoid plaintext env vars and never misuse KMS as a secrets store. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which SINGLE S3 feature is the BEST for restricting S3 access to a specific VPC?",
    "type": "multiple-choice",
    "opts": [
        ("Standard tier", "Standard tier does not support KMS encryption."),
        ("Advanced tier", "Advanced tier supports larger parameters and KMS encryption."),
        ("Basic tier", "Parameter Store does not have a basic tier."),
        ("Custom tier", "Parameter Store does not have a custom tier."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Parameter Store Advanced tier supports KMS encryption for sensitive values. Reference: https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-organize.html",
})
QUESTIONS.append({
    "q": "Which AWS service encrypts data in transit between a client and a load balancer using TLS, and provides free public certificates?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Private Certificate Authority", "Private CA is for internal certificates, not free public ones."),
        ("AWS Certificate Manager (ACM)", "ACM provides free public TLS certificates and integrates with ELB, CloudFront, and API Gateway."),
        ("AWS KMS", "KMS is for encryption keys, not TLS certs."),
        ("AWS Secrets Manager", "Secrets Manager is for secrets, not TLS certs."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Certificate Manager provides public TLS certificates free of charge, integrated with Elastic Load Balancing, CloudFront, and API Gateway. Reference: https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html",
})
QUESTIONS.append({
    "q": "Which service issues private TLS certificates for resources inside your VPC or on-prem connected network?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Certificate Manager public", "ACM public issues public certificates only."),
        ("AWS Private Certificate Authority", "AWS Private CA issues private certificates for internal use."),
        ("AWS Secrets Manager", "Secrets Manager is for secrets."),
        ("AWS KMS", "KMS is for encryption keys."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Private Certificate Authority issues private TLS certificates for resources inside your organization. Reference: https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service is the BEST choice for end-to-end TLS termination at the application layer?",
    "type": "multiple-choice",
    "opts": [
        ("Application Load Balancer with ACM certificate", "ALB terminates TLS with an ACM cert."),
        ("Network Load Balancer with ACM certificate", "NLB terminates TLS at L4 with an ACM cert."),
        ("AWS CloudFront with ACM certificate", "CloudFront terminates TLS at edge with an ACM cert."),
        ("AWS Direct Connect", "Direct Connect is a private link, not for TLS termination."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "ALB, NLB, and CloudFront can all terminate TLS using ACM certificates. Reference: https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed PostgreSQL-compatible and MySQL-compatible relational database with automatic encryption at rest using a customer managed KMS key?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon RDS", "RDS supports encryption at rest with a CMK."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database."),
        ("Amazon Neptune", "Neptune is a graph database."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon RDS supports encryption at rest using a customer managed CMK. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
})
QUESTIONS.append({
    "q": "Which SINGLE S3 security feature complements bucket policies and IAM?",
    "type": "multiple-choice",
    "opts": [
        ("Enable encryption when creating a new EBS volume", "Encryption is set at create time."),
        ("Copy an unencrypted snapshot and enable encryption with a CMK", "Snapshot copy supports encryption change."),
        ("Modify the volume in-place to enable encryption", "In-place modification is not supported."),
        ("Use the AWS CLI to encrypt an existing volume in-place", "In-place encryption is not supported for EBS."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "EBS encryption is set at create time or via snapshot copy. In-place modification is not supported. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html",
})
QUESTIONS.append({
    "q": "Which S3 feature blocks any public access at the account or bucket level, regardless of bucket policy or ACL?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Block Public Access", "Block Public Access is the override that prevents public access regardless of other policies."),
        ("S3 bucket policy with Deny", "A Deny in a bucket policy does not override public access granted by other means in all cases."),
        ("S3 ACL only", "ACLs alone cannot guarantee no public access."),
        ("S3 Versioning", "Versioning protects objects, not access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Block Public Access provides a final override that blocks any public access, no matter the bucket policy or ACL. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html",
})
QUESTIONS.append({
    "q": "Which combination is the BEST way to share a private S3 object with a third party for a limited time without making the object public? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Generate a presigned URL with an expiration time", "Presigned URLs grant time-limited access without changing bucket policy."),
        ("Use the object's S3 URI with a public bucket", "Public bucket exposure is not the right pattern."),
        ("Use S3 Object Lambda to transform the object on read", "Object Lambda is for code-on-read transformation, not sharing."),
        ("Use S3 access point with a VPC origin", "Access points with VPC origin restrict sharing to a VPC, useful for some private sharing patterns."),
    ],
    "correct": "1,4",
    "domain": SECURE,
    "overall": "Use a presigned URL or a VPC-restricted access point for time-limited, private sharing. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html",
})
QUESTIONS.append({
    "q": "Which S3 encryption option uses customer-supplied keys (where you provide and manage the encryption key) and is the LEAST convenient?",
    "type": "multiple-choice",
    "opts": [
        ("SSE-S3 (AES-256)", "SSE-S3 uses AWS-managed S3 keys."),
        ("SSE-KMS", "SSE-KMS uses KMS keys managed by you or AWS."),
        ("SSE-C", "SSE-C requires you to provide and manage the key on every request."),
        ("Client-side encryption", "Client-side is not S3-side SSE-C, though the question is about SSE-C."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "SSE-C requires the client to send the encryption key with every request; you retain full key control but must manage keys yourself. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html",
})
QUESTIONS.append({
    "q": "Which S3 feature REPLICATES objects to a destination bucket asynchronously for compliance and DR?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle rules", "Lifecycle transitions or expires objects; not replication."),
        ("S3 Cross-Region Replication (CRR) or Same-Region Replication (SRR)", "Replication asynchronously copies new and updated objects to another bucket."),
        ("S3 Batch Operations", "Batch runs one-time jobs over many objects."),
        ("S3 Inventory", "Inventory is a CSV/ORC report."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "S3 Replication (CRR or SRR) asynchronously replicates new and updated objects to a destination bucket. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which SINGLE S3 event type triggers when an object is created via PUT, POST, or COPY?",
    "type": "multiple-choice",
    "opts": [
        ("S3 server access logs", "Server access logs provide detailed request-level logs to a target bucket."),
        ("S3 storage class analysis", "Storage class analysis informs lifecycle decisions."),
        ("S3 event notifications only", "Event notifications trigger on a subset of events; they are not full audit logs."),
        ("S3 Inventory", "Inventory is a listing, not access logs."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 server access logs record every request made to a bucket, which is the right tool for object-level audit logging. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html",
})
QUESTIONS.append({
    "q": "Which SINGLE setting is the MOST fundamental requirement to enable S3 Cross-Region Replication?",
    "type": "multiple-choice",
    "opts": [
        ("Versioning enabled on both source and destination buckets", "Replication requires versioning."),
        ("An IAM role that S3 assumes to replicate objects", "S3 needs permission to read from source and write to destination."),
        ("Both buckets in the same AWS account", "Replication works across accounts as well."),
        ("The destination bucket must be in a different region for CRR", "CRR specifically requires a different region; SRR is same-region."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "CRR requires versioning on both buckets, an IAM role, and the destination bucket in a different region; same-account is not required. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which S3 object lock mode ensures an object cannot be deleted or overwritten by any user, including the root user, until a retention date?",
    "type": "multiple-choice",
    "opts": [
        ("Governance mode", "Governance mode allows special users to bypass retention."),
        ("Compliance mode", "Compliance mode prevents deletion by anyone, even the root user, until retention expires."),
        ("Legal hold", "Legal hold is independent of retention and can be removed by users with permission."),
        ("Standard mode", "Standard mode is not an S3 Object Lock mode."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "S3 Object Lock Compliance mode is the strongest: no user, including root, can delete or overwrite the object until the retention period ends. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "Which S3 feature uses a bucket policy to enforce that all objects written to a bucket must include specific tags or be encrypted?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle", "Lifecycle manages storage class transitions and expiration."),
        ("S3 Object Ownership", "Object Ownership controls ACL inheritance."),
        ("S3 PUT requests with conditional policy checks (via IAM or bucket policy)", "A bucket policy can require encryption or specific tags on PutObject."),
        ("S3 Storage Lens", "Storage Lens provides analytics dashboards."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "Use a bucket policy with conditions on PutObject such as `s3:x-amz-server-side-encryption` or `s3:x-amz-tagging` to enforce encryption or tags. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides query-in-place analytics on objects without moving the data, with fine-grained access control via IAM?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Select", "S3 Select runs SQL on individual objects."),
        ("S3 Object Lambda", "S3 Object Lambda transforms objects on read with custom code."),
        ("Amazon Athena", "Athena queries S3 data using standard SQL with IAM-based access."),
        ("AWS Glue", "Glue is a serverless data integration service."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "Amazon Athena provides query-in-place analytics on S3 with IAM-based access control. Reference: https://docs.aws.amazon.com/athena/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature is the BEST pattern for restricting S3 access to a specific VPC?",
    "type": "multiple-choice",
    "opts": [
        ("S3 VPC gateway endpoint", "A gateway endpoint keeps S3 traffic inside the AWS network from a specific VPC."),
        ("S3 bucket policy restricting to the VPC endpoint", "A bucket policy can allow only traffic from a specific VPC endpoint."),
        ("Public S3 bucket", "Public S3 is the opposite of the desired pattern."),
        ("Internet gateway only", "An internet gateway is not for in-VPC S3 access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use an S3 VPC gateway endpoint combined with a bucket policy that restricts access to the endpoint. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html",
})
QUESTIONS.append({
    "q": "Which S3 feature transforms objects on read using AWS Lambda functions, useful for redacting sensitive data before serving?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Object Lambda", "S3 Object Lambda invokes Lambda on S3 GET to transform the object."),
        ("S3 Select", "S3 Select runs SQL on a single object; not for transformation."),
        ("S3 Batch Operations", "Batch is for one-time operations."),
        ("S3 Event Notifications", "Event notifications trigger on writes, not reads."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Object Lambda invokes Lambda functions on S3 GETs to transform or redact the object before returning. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 security features that complement bucket policies and IAM? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Access Points with distinct policies", "Access points provide per-prefix policies."),
        ("S3 Access Grants for IAM Identity Center integration", "Access Grants integrate with IAM Identity Center for per-user access."),
        ("S3 public buckets for sensitive data", "Public buckets for sensitive data are an antipattern."),
        ("S3 Block Public Access", "Block Public Access is the final override."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "S3 Access Points, Access Grants, and Block Public Access are all security features. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html",
})
QUESTIONS.append({
    "q": "Which feature allows you to replicate existing objects (not just new ones) in S3 on demand, useful for initial bulk replication?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Batch Replication", "S3 Batch Replication replicates existing objects on demand."),
        ("S3 Cross-Region Replication", "Standard replication only handles new objects."),
        ("S3 Object Lock", "Object Lock is for immutability."),
        ("S3 Inventory", "Inventory is a report."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Batch Replication replicates existing objects that were not replicated by standard replication. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for S3 Object Lock? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("WORM (write-once-read-many) compliance for regulated data", "Object Lock provides WORM storage."),
        ("Ransomware protection by making objects immutable", "Object Lock prevents deletion even by privileged users in compliance mode."),
        ("Encrypted storage of sensitive data", "Object Lock is about immutability, not encryption."),
        ("Cost reduction on long-term storage", "Object Lock does not reduce cost; lifecycle rules do."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "S3 Object Lock provides WORM compliance and ransomware protection via immutability. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "Which SINGLE VPC networking component is a stateful ENI-level firewall?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Access Points", "S3 Access Points provide per-application access policies."),
        ("S3 Object Lambda", "S3 Object Lambda transforms objects, not access control."),
        ("S3 Multi-Region Access Points", "Multi-Region Access Points span regions, not access policies."),
        ("S3 Storage Lens", "Storage Lens is analytics."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Access Points provide distinct access policies per application per prefix. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html",
})
QUESTIONS.append({
    "q": "Which S3 feature automatically moves objects between access tiers based on usage patterns, with no retrieval charges, AND supports security controls like Object Lock?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering moves objects between tiers automatically."),
        ("S3 Standard-IA", "Standard-IA is a single tier with retrieval charges."),
        ("S3 Glacier", "Glacier has retrieval charges and no automatic tiering."),
        ("S3 One Zone-IA", "One Zone-IA is a single infrequent tier."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Intelligent-Tiering automatically moves objects between Frequent, Infrequent, Archive, and Deep Archive tiers. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which SINGLE option is the BEST default S3 encryption choice for new buckets with no key management?",
    "type": "multiple-choice",
    "opts": [
        ("SSE-S3 (AES-256)", "SSE-S3 uses AWS-managed S3 keys for AES-256 encryption."),
        ("SSE-KMS (with AWS managed or customer managed keys)", "SSE-KMS uses KMS keys."),
        ("SSE-C (customer-provided keys)", "SSE-C requires you to provide and manage keys."),
        ("Client-side encryption", "Client-side encryption encrypts before upload."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 supports SSE-S3, SSE-KMS, SSE-C, and client-side encryption for data at rest. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryption.html",
})
QUESTIONS.append({
    "q": "Which S3 feature lets you track changes to objects in your bucket and replicate only changed objects to another bucket?",
    "type": "multiple-choice",
    "opts": [
        ("S3 event notifications on ObjectCreated:Put", "Event notifications can drive replication triggers."),
        ("S3 Versioning with replication", "Versioning + replication replicates changed objects automatically."),
        ("S3 Inventory", "Inventory is a listing, not change tracking."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "S3 Versioning combined with replication automatically replicates new and changed objects. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 Access Grants use cases? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Per-user access to S3 data from an application", "Access Grants provide per-user access."),
        ("Integration with IAM Identity Center for workforce SSO", "Access Grants integrate with IAM Identity Center."),
        ("Direct public access to all objects", "Direct public access is not the use case for Access Grants."),
        ("Replacing S3 bucket policies", "Access Grants complement bucket policies, not replace."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "S3 Access Grants provide per-user access to S3 and integrate with IAM Identity Center. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html",
})
QUESTIONS.append({
    "q": "Which SINGLE VPC feature provides private connectivity to S3 and DynamoDB?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon GuardDuty with S3 protection", "GuardDuty analyzes CloudTrail S3 API events for threats."),
        ("AWS Config only", "Config tracks configuration changes."),
        ("Amazon Macie only", "Macie discovers sensitive data, not exfiltration."),
        ("AWS CloudTrail alone", "CloudTrail records events; GuardDuty interprets them."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon GuardDuty S3 Protection analyzes CloudTrail S3 data events for threats and exfiltration. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html",
})
QUESTIONS.append({
    "q": "Which AWS networking component is a STATEFUL virtual firewall that controls traffic at the ENI level?",
    "type": "multiple-choice",
    "opts": [
        ("Network ACL", "NACLs are stateless and operate at the subnet level."),
        ("Security group", "Security groups are stateful and operate at the ENI level."),
        ("Internet gateway", "An internet gateway is for routing, not firewalling."),
        ("VPC peering connection", "Peering connects VPCs, not for firewalling."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Security groups are stateful, ENI-level virtual firewalls. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html",
})
QUESTIONS.append({
    "q": "Which component is STATELESS, operates at the SUBNET level, and is evaluated separately for inbound and outbound rules?",
    "type": "multiple-choice",
    "opts": [
        ("Security group", "Security groups are stateful and ENI-level."),
        ("Network ACL (NACL)", "NACLs are stateless and operate at the subnet level."),
        ("Route table", "Route tables direct traffic, not filter."),
        ("NAT gateway", "NAT gateway performs address translation, not filtering."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Network ACLs are stateless, subnet-level firewalls with separate inbound and outbound rules. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html",
})
QUESTIONS.append({
    "q": "Which VPC endpoint type does NOT require a NAT gateway, gateway endpoint, or internet gateway to reach S3 or DynamoDB?",
    "type": "multiple-choice",
    "opts": [
        ("Internet gateway", "An internet gateway sends traffic to the public internet."),
        ("Gateway endpoint (S3, DynamoDB)", "Gateway endpoints provide private connectivity to S3 and DynamoDB without NAT or IGW."),
        ("VPN connection", "VPN is for on-prem connectivity."),
        ("AWS Direct Connect", "DX is for on-prem dedicated connectivity."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Gateway endpoints (S3 and DynamoDB) provide private connectivity inside the AWS network — no NAT, IGW, or DX required. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
})
QUESTIONS.append({
    "q": "Which VPC endpoint type uses AWS PrivateLink and supports most AWS services and your own services powered by Network Load Balancers?",
    "type": "multiple-choice",
    "opts": [
        ("Gateway endpoint", "Gateway endpoints are S3 and DynamoDB only."),
        ("Interface endpoint (powered by PrivateLink)", "Interface endpoints use PrivateLink and support many AWS services."),
        ("Internet gateway", "An IGW is for public internet."),
        ("Customer gateway", "Customer gateway is for VPN."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Interface VPC endpoints (powered by AWS PrivateLink) provide private connectivity to most AWS services and your own services. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service is the BEST fit for centralized, multi-account DNS firewall rule management?",
    "type": "multiple-choice",
    "opts": [
        ("VPC Flow Logs", "VPC Flow Logs capture IP traffic information for the VPC."),
        ("AWS CloudTrail", "CloudTrail records API calls, not network packets."),
        ("AWS Config", "Config records resource configuration changes."),
        ("CloudWatch metrics", "Metrics are numeric time series, not packet capture."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "VPC Flow Logs capture information about IP traffic going to and from network interfaces in a VPC. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component is the BEST choice for connecting a VPC to your on-prem network via an IPsec VPN?",
    "type": "multiple-choice",
    "opts": [
        ("Internet gateway", "IGWs provide public internet access."),
        ("NAT gateway", "NAT gateways allow outbound internet for private subnets."),
        ("Virtual private gateway", "A VGW is the AWS side of a VPN connection."),
        ("Transit gateway", "Transit Gateway connects multiple VPCs and on-prem networks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "All four are valid VPC connectivity components. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid traffic filter options for VPC security groups? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("A specific IP CIDR", "Security groups accept CIDR-based rules."),
        ("Another security group as source", "Security group referencing is a key feature for app-tier rules."),
        ("Port ranges", "Port ranges are allowed in security group rules."),
        ("Time-of-day constraints", "Time-of-day filtering is not a security group feature; use NACLs or WAF."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Security groups support CIDR, other security groups, and port ranges. Time-of-day filtering is not natively supported. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html",
})
QUESTIONS.append({
    "q": "Which AWS network firewall feature inspects traffic at layer 7 and matches against defined rules?",
    "type": "multiple-choice",
    "opts": [
        ("Security group", "Security groups are layer 3-4 only."),
        ("AWS Network Firewall with Suricata-compatible rules", "Network Firewall supports Suricata-compatible IDS/IPS rules at layer 7."),
        ("NAT gateway", "NAT gateway is for address translation."),
        ("Internet gateway", "IGW routes, does not filter at L7."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Network Firewall supports stateful Suricata-compatible IDS/IPS rules that can inspect traffic at layer 7. Reference: https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html",
})
QUESTIONS.append({
    "q": "Which service filters and routes DNS queries from a VPC to custom DNS resolvers, blocking queries to known malicious domains?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 Resolver DNS Firewall", "DNS Firewall inspects DNS queries and blocks resolutions to bad domains."),
        ("AWS WAF", "WAF filters HTTP/HTTPS, not DNS."),
        ("AWS Shield", "Shield is for DDoS protection at L3/L4."),
        ("AWS Network Firewall", "Network Firewall is for IP traffic, not DNS-specific."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Route 53 Resolver DNS Firewall filters DNS queries and can block resolutions to known malicious domains. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component provides a managed, highly available NAT service?",
    "type": "multiple-choice",
    "opts": [
        ("Use multiple Availability Zones for high availability", "Multi-AZ is the foundation of VPC HA."),
        ("Use private subnets for backend resources", "Backend resources should be in private subnets."),
        ("Place databases in public subnets", "Public subnets should not host databases."),
        ("Use security groups as the primary firewall", "Security groups are the primary per-resource firewall."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Best practices: multi-AZ, private subnets for backends, security groups as primary firewall. Databases in public subnets is an antipattern. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html",
})
QUESTIONS.append({
    "q": "Which approach to VPC subnet design BEST supports separating workloads by security tier (web, app, data)?",
    "type": "multiple-choice",
    "opts": [
        ("Use a single subnet for all tiers", "A single subnet does not enable tier separation."),
        ("Use separate subnets in different Availability Zones per tier (web, app, data)", "Tier-based subnets in multi-AZ enable fine-grained security groups and NACLs."),
        ("Use one subnet per account", "Account-level separation is a coarse pattern; subnet separation is more efficient."),
        ("Use a single public subnet for everything", "A single public subnet is an antipattern."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Best practice: web/app/data subnets in multiple AZs, with security groups and NACLs providing tier isolation. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html",
})
QUESTIONS.append({
    "q": "Which VPC feature provides dedicated, private connectivity from a VPC to supported AWS services without traversing the public internet?",
    "type": "multiple-choice",
    "opts": [
        ("Internet gateway", "An internet gateway is for public access."),
        ("AWS PrivateLink", "PrivateLink provides private connectivity to AWS services and your own services."),
        ("NAT gateway", "NAT gateway is for outbound internet from private subnets."),
        ("VPC peering", "VPC peering connects VPCs, not services."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS PrivateLink provides dedicated, private connectivity from a VPC to supported AWS services without traversing the public internet. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html",
})
QUESTIONS.append({
    "q": "Which SINGLE benefit is the BEST description of AWS PrivateLink?",
    "type": "multiple-choice",
    "opts": [
        ("Traffic stays within the AWS network", "PrivateLink keeps traffic on the AWS backbone."),
        ("Reduces exposure to the public internet", "No public internet traversal."),
        ("Requires a public IP address on the consumer", "PrivateLink does not require a public IP."),
        ("Simplifies network architecture", "PrivateLink eliminates the need for complex peering or transit."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "PrivateLink keeps traffic in the AWS network, reduces public internet exposure, and simplifies architecture. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html",
})
QUESTIONS.append({
    "q": "Which VPC flow log setting captures the LEAST information (only the ENI, source/dest IPs, and accept/reject status)?",
    "type": "multiple-choice",
    "opts": [
        ("Reject", "Reject logs only rejected traffic."),
        ("Accept", "Accept logs only accepted traffic."),
        ("All", "All logs both accept and reject traffic."),
        ("Custom format", "Custom format lets you pick specific fields."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "All captures both accept and reject; specific fields can be customized. The default format includes accept/reject status. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html",
})
QUESTIONS.append({
    "q": "Which SINGLE destination is the BEST for VPC Flow Logs for long-term archival?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch Logs", "VPC Flow Logs can be sent to CloudWatch Logs."),
        ("Amazon S3", "VPC Flow Logs can be sent to S3 for archival."),
        ("AWS Kinesis Data Firehose", "VPC Flow Logs can be sent to Kinesis Data Firehose for streaming."),
        ("Amazon SQS directly", "VPC Flow Logs cannot be sent to SQS directly; use Firehose."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "VPC Flow Logs support CloudWatch Logs, S3, and Kinesis Data Firehose as destinations. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed distributed denial-of-service (DDoS) protection service for applications running on AWS, with always-on detection and 24/7 DRT support?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Shield Standard", "Shield Standard is free and always-on but does not include DRT."),
        ("AWS Shield Advanced", "Shield Advanced includes 24/7 DRT and cost protection."),
        ("AWS WAF only", "WAF is for L7, not DDoS protection per se."),
        ("Amazon CloudFront alone", "CloudFront is a CDN, not DDoS protection as a service."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Shield Advanced provides 24/7 access to the AWS DDoS Response Team (DRT) and cost protection. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid features of AWS Shield Standard? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Always-on network flow monitoring", "Shield Standard includes always-on detection at no cost."),
        ("DDoS cost protection for scaling charges", "Cost protection is a Shield Advanced feature, not Standard."),
        ("Automatic protection for all AWS customers", "Shield Standard is automatic for all customers."),
        ("24/7 access to the AWS DDoS Response Team (DRT)", "DRT is a Shield Advanced feature, not Standard."),
    ],
    "correct": "1,3",
    "domain": SECURE,
    "overall": "Shield Standard provides always-on detection and automatic protection for all AWS customers. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST practice for a public-facing web application to protect against common web exploits and DDoS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront", "CloudFront provides edge caching and absorbs L3/L4 attacks."),
        ("AWS WAF with managed rule groups", "WAF blocks SQLi, XSS, and other web exploits."),
        ("AWS Shield Advanced for high-risk applications", "Shield Advanced adds DRT and cost protection for high-risk apps."),
        ("Direct EC2 with public IP", "Direct EC2 with public IP is not the best practice."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "CloudFront + WAF + Shield Advanced is the comprehensive public web app protection stack. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides centralized, automated security findings aggregation across GuardDuty, Inspector, Macie, and other sources, with compliance standards?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Security Hub", "Security Hub aggregates findings and provides compliance standards."),
        ("AWS Config alone", "Config tracks resource configuration."),
        ("AWS Audit Manager", "Audit Manager automates evidence collection."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Security Hub aggregates findings from multiple services and provides compliance standards like CIS and PCI DSS. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated evidence collection for audit reports, supporting frameworks like PCI DSS, ISO 27001, and SOC 2?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Audit Manager", "Audit Manager automates evidence collection for audit reports."),
        ("AWS Security Hub", "Security Hub is for findings aggregation."),
        ("AWS Artifact", "Artifact provides AWS-issued reports, not automated evidence."),
        ("AWS Config alone", "Config is for resource configuration compliance."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Audit Manager continuously collects evidence and generates audit-ready reports for PCI, ISO, and SOC. Reference: https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service uses machine learning and threat intelligence to detect compromised accounts, exfiltration, and recon in your AWS environment?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Config", "Config tracks configuration changes."),
        ("Amazon GuardDuty", "GuardDuty is the threat detection service using ML and threat intel."),
        ("AWS CloudTrail", "CloudTrail records API calls; GuardDuty consumes them."),
        ("Amazon Macie", "Macie discovers sensitive data in S3."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Amazon GuardDuty analyzes CloudTrail, VPC Flow Logs, and DNS logs to detect threats using ML and threat intel. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html",
})
QUESTIONS.append({
    "q": "Which service discovers and classifies sensitive data (PII, PHI, financial) in S3 buckets?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Macie", "Macie uses ML to discover and classify sensitive data in S3."),
        ("Amazon GuardDuty", "GuardDuty is for threat detection."),
        ("AWS Config", "Config is for configuration compliance."),
        ("Amazon Inspector", "Inspector is for EC2/Container vulnerability scanning."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon Macie uses ML to discover and classify sensitive data such as PII in S3 buckets. Reference: https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html",
})
QUESTIONS.append({
    "q": "Which service performs vulnerability scanning for EC2 instances and container images, and reports on unintended network exposure?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Inspector", "Inspector scans EC2 instances and container images for vulnerabilities."),
        ("Amazon GuardDuty", "GuardDuty is for threat detection, not CVE scanning."),
        ("AWS Config", "Config evaluates configuration rules."),
        ("Amazon Macie", "Macie classifies S3 data."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon Inspector performs continuous vulnerability scanning for EC2 instances and container images. Reference: https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html",
})
QUESTIONS.append({
    "q": "Which service records every AWS API call and console sign-in as an event for audit, governance, and compliance?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch Logs", "CloudWatch Logs is for application logs."),
        ("AWS CloudTrail", "CloudTrail records API calls and console logins."),
        ("AWS Config", "Config records configuration state changes."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS CloudTrail records every API call made in your account and is the primary audit log source. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service uses ML and threat intelligence to detect compromised accounts?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudTrail", "CloudTrail records API calls, not configuration history."),
        ("AWS Config", "Config records configuration state and evaluates rules."),
        ("Amazon CloudWatch", "CloudWatch is for metrics and logs."),
        ("AWS Systems Manager", "SSM manages EC2 and ops items."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Config records configuration history of resources and evaluates them against managed or custom rules. Reference: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html",
})
QUESTIONS.append({
    "q": "Which SINGLE configuration is the BEST for CloudTrail in a single AWS account?",
    "type": "multiple-choice",
    "opts": [
        ("A multi-region trail that records events in all enabled regions", "CloudTrail supports multi-region trails."),
        ("An organization trail that records events for all member accounts", "CloudTrail Lake and Organizations support org-wide trails."),
        ("Log file integrity validation", "CloudTrail supports log file integrity validation."),
        ("Built-in intrusion detection on every API call", "CloudTrail is a log source, not an IDS; GuardDuty consumes it."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "CloudTrail supports multi-region, organization trails, and log file integrity validation; it is not an IDS. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html",
})
QUESTIONS.append({
    "q": "Which of the following are the CUSTOMER'S responsibility under the AWS Shared Responsibility Model? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Configuring S3 bucket policies and access controls", "Customers configure S3 access."),
        ("Patching the guest OS on an EC2 instance", "Customer patches the OS in EC2."),
        ("Maintaining the physical security of AWS data centers", "Physical security is AWS's responsibility."),
        ("Managing IAM users and their permissions", "IAM is customer responsibility."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Customers are responsible for security IN the cloud: data, IAM, OS, network config, and applications. AWS is responsible for security OF the cloud. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-overview-introduction/aws-shared-responsibility-model.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a unified compliance view across accounts, showing which accounts comply with standards like PCI DSS and HIPAA?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Audit Manager", "Audit Manager automates evidence collection for audits."),
        ("AWS Security Hub", "Security Hub aggregates security findings and provides compliance status."),
        ("AWS Config alone", "Config evaluates rules but does not aggregate compliance standards."),
        ("Amazon Inspector", "Inspector scans for vulnerabilities."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Security Hub aggregates findings from GuardDuty, Inspector, Macie, and others, and provides a compliance view against standards like CIS, PCI DSS, and the AWS best practices. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides on-demand access to AWS compliance reports and agreements, such as SOC 2 and ISO 27001?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Artifact", "Artifact is the self-service portal for AWS compliance reports."),
        ("AWS Audit Manager", "Audit Manager automates evidence; it does not host the AWS-issued reports."),
        ("AWS Security Hub", "Security Hub is findings, not reports."),
        ("AWS Config", "Config is for resource configuration."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Artifact provides on-demand access to AWS compliance reports and BAA/online agreements. Reference: https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service records every API call for audit?",
    "type": "multiple-choice",
    "opts": [
        ("IAM policy Condition with aws:MultiFactorAuthPresent", "Use Condition to require MFA."),
        ("SCP requiring MFA for sensitive actions", "SCPs can require MFA in member accounts."),
        ("Bypass MFA for root user", "Bypassing MFA is an antipattern."),
        ("Disable MFA enforcement", "Disabling MFA is a security antipattern."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use IAM Condition or SCP to require MFA for sensitive operations. Bypassing or disabling MFA is an antipattern. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-multifactor",
})
QUESTIONS.append({
    "q": "Which AWS service detects anomalous API activity such as unusual DeleteTrail or DisableKey calls that might indicate an attack?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudTrail Insights", "CloudTrail Insights detects unusual API activity."),
        ("Amazon GuardDuty", "GuardDuty detects broader threats; Insights focuses on API anomalies."),
        ("AWS Config", "Config evaluates configuration rules."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS CloudTrail Insights detects unusual API activity such as spikes in DeleteTrail or DisableKey calls. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights.html",
})
QUESTIONS.append({
    "q": "Which SINGLE way is the BEST baseline for encrypting data in transit on AWS?",
    "type": "multiple-choice",
    "opts": [
        ("TLS via ACM on ELB/CloudFront/API Gateway", "TLS via ACM is the standard pattern."),
        ("S3 endpoint policy requiring HTTPS", "Bucket policies can require TLS connections."),
        ("RDS with TLS connections", "RDS supports TLS connections to the database endpoint."),
        ("Plaintext HTTP for public web apps", "Plaintext HTTP is an antipattern for public web apps."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use TLS via ACM, S3 bucket policies requiring HTTPS, and RDS TLS connections. Plaintext HTTP is an antipattern. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-overview-introduction/aws-shared-responsibility-model.html",
})
QUESTIONS.append({
    "q": "Which AWS WAF rule action BLOCKS the request and returns a custom HTTP response, typically used to stop SQLi and XSS?",
    "type": "multiple-choice",
    "opts": [
        ("Allow", "Allow is the default permissive action."),
        ("Count", "Count observes the request but takes no action."),
        ("Block", "Block denies the request and returns a 403."),
        ("Captcha", "Captcha is a separate action for human verification."),
    ],
    "correct": "3",
    "domain": SECURE,
    "overall": "AWS WAF rule actions: Allow (default), Block (returns 403), Count (observe only), and Captcha (challenge). Reference: https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-rule-action.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component is the top-level resource in AWS WAF?",
    "type": "multiple-choice",
    "opts": [
        ("Web ACL", "A web ACL is the top-level WAF resource containing rules."),
        ("Rule groups (managed and custom)", "Rule groups contain rules and can be shared."),
        ("Rules with conditions and actions", "Rules match conditions and apply actions."),
        ("Suricata rules", "WAF does not use Suricata; AWS Network Firewall does."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "WAF uses Web ACLs containing rules, rule groups, and rule actions. Suricata is for Network Firewall. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service provides automated evidence collection for audit reports?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 Resolver DNS Firewall", "DNS Firewall is the centralized DNS firewall."),
        ("AWS Network Firewall", "Network Firewall is for IP traffic, not DNS-specific."),
        ("AWS WAF", "WAF is for HTTP/HTTPS."),
        ("AWS Shield", "Shield is for DDoS protection."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Route 53 Resolver DNS Firewall provides centralized DNS firewall rule management for VPCs. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid features of AWS WAF? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Rate-based rules to limit requests per IP", "Rate-based rules throttle abusive clients."),
        ("Managed rule groups for OWASP Top 10", "AWS-managed rule groups cover OWASP Top 10."),
        ("Bot control and fraud prevention", "AWS WAF Bot Control and Fraud Prevention are available."),
        ("TLS termination", "WAF does not terminate TLS; the ALB or CloudFront does."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "WAF supports rate-based rules, managed rule groups, and bot control. TLS termination is the responsibility of the load balancer. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for cross-account, multi-region logging aggregation for compliance? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudTrail organization trail", "Org trail records events for all member accounts."),
        ("CloudWatch Logs subscriptions to a central account", "Subscriptions aggregate logs to a central account."),
        ("S3 with cross-region replication and Object Lock", "S3 CRR + Object Lock provides durable, immutable archival."),
        ("Local logs only without aggregation", "Local logs only do not meet multi-account aggregation requirements."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use org trail, CloudWatch Logs subscriptions, and S3 CRR + Object Lock for cross-account, multi-region log aggregation. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
})
QUESTIONS.append({
    "q": "Which AWS service is designed for sensitive data discovery and classification, with PII detection in S3 buckets?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Macie", "Macie discovers and classifies sensitive data in S3."),
        ("Amazon GuardDuty", "GuardDuty is for threat detection."),
        ("AWS Config", "Config is for configuration compliance."),
        ("Amazon Inspector", "Inspector is for vulnerability scanning."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon Macie is the AWS service for sensitive data discovery and classification, particularly PII in S3. Reference: https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature is the BEST description of Amazon Macie?",
    "type": "multiple-choice",
    "opts": [
        ("Automated sensitive data discovery in S3", "Macie scans S3 buckets for sensitive data."),
        ("Policy findings for unencrypted buckets", "Macie generates policy findings for security issues."),
        ("Vulnerability scanning for EC2", "Macie is for S3 data, not EC2 vulnerabilities."),
        ("Custom data identifiers for proprietary data", "Custom data identifiers allow scanning for proprietary data types."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Macie scans S3 for sensitive data, generates policy findings, and supports custom data identifiers. Reference: https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service should be used to enforce baseline security controls across all accounts?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Control Tower", "Control Tower provides multi-account governance with baseline controls."),
        ("AWS Config alone", "Config is for resource configuration."),
        ("AWS CloudTrail alone", "CloudTrail is for API logging."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Control Tower provides multi-account landing zone with baseline security controls via guardrails. Reference: https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html",
})
QUESTIONS.append({
    "q": "Which AWS service enforces an org-wide baseline of detective controls and runs automated security checks against AWS best practices?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Security Hub with AWS Foundational Security Best Practices standard", "Security Hub runs the FSBP standard by default."),
        ("Amazon CloudWatch only", "CloudWatch is metrics and logs."),
        ("AWS Trusted Advisor only", "Trusted Advisor checks cost and security best practices, but Security Hub standardizes the controls."),
        ("AWS Config only", "Config is for resource configuration rules."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Security Hub runs the AWS Foundational Security Best Practices standard as a default detective control set. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature is the BEST description of AWS Security Hub?",
    "type": "multiple-choice",
    "opts": [
        ("Aggregated findings from GuardDuty, Inspector, Macie, IAM Access Analyzer", "Security Hub aggregates from many services."),
        ("Compliance standards like CIS, PCI DSS, AWS best practices", "Security Hub runs compliance standards."),
        ("Automated remediation with EventBridge", "EventBridge can drive remediation from Security Hub findings."),
        ("Built-in DDoS protection at L7", "Security Hub does not provide DDoS protection; use Shield."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Security Hub aggregates findings, runs compliance standards, and integrates with EventBridge for remediation. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for cross-account, multi-region audit logging for compliance? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudTrail organization trail", "Org trail centralizes audit logs for all accounts."),
        ("S3 bucket with Object Lock for immutability", "Object Lock prevents tampering with audit logs."),
        ("KMS encryption for the log bucket", "KMS encryption protects logs at rest."),
        ("Local logs only in each account", "Local logs do not provide centralized audit."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use org trail, S3 with Object Lock, and KMS encryption for centralized, immutable, encrypted audit logs. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for managing secrets such as database credentials with automatic rotation?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager", "Secrets Manager supports automatic rotation and audit."),
        ("AWS Systems Manager Parameter Store only", "Parameter Store supports manual rotation and some Lambda-based rotation, not native RDS."),
        ("Amazon S3 with SSE-KMS", "S3 is object storage, not a secrets store."),
        ("AWS KMS", "KMS manages encryption keys, not application secrets."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Secrets Manager is the dedicated service for storing and automatically rotating secrets such as database credentials. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service enables HIPAA-eligible workloads and provides a BAA?",
    "type": "multiple-choice",
    "opts": [
        ("RDS storage encryption with a CMK", "RDS storage encryption protects PHI at rest."),
        ("S3 default bucket encryption with SSE-KMS and a CMK", "S3 encryption protects PHI at rest."),
        ("EBS encryption with a CMK", "EBS encryption protects data at rest."),
        ("Plaintext RDS database", "Plaintext databases do not meet encryption requirements."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Encrypt RDS storage, S3 objects, and EBS volumes with a CMK to protect PHI at rest. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
})
QUESTIONS.append({
    "q": "Which service enables HIPAA-eligible workloads and provides a Business Associate Addendum (BAA) for covered workloads?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Artifact", "AWS Artifact is where you sign the BAA with AWS."),
        ("AWS Shield", "Shield is for DDoS protection."),
        ("AWS WAF", "WAF is for web app protection."),
        ("Amazon Cognito", "Cognito is for identity."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Artifact is where you sign the BAA with AWS to enable HIPAA-eligible workloads. Reference: https://docs.aws.amazon.com/artifact/latest/ug/hipaa-eligible-services.html",
})
QUESTIONS.append({
    "q": "Which combination of services is REQUIRED to meet a 7-year audit log retention requirement for PHI access? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 with Object Lock in Compliance mode for 7 years", "Object Lock provides immutable retention."),
        ("S3 Lifecycle policy to transition to Glacier after 1 year for cost", "Lifecycle reduces cost while keeping data accessible."),
        ("KMS encryption on the audit log bucket", "Encryption protects log data at rest."),
        ("Local EC2 instance logs only", "Local EC2 logs do not meet 7-year retention requirements."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use S3 Object Lock for immutability, Lifecycle for cost, and KMS for encryption to meet 7-year retention. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a HIPAA-eligible, fully managed ElastiCache for Redis with encryption at rest and in transit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ElastiCache for Redis", "ElastiCache for Redis is HIPAA-eligible with encryption support."),
        ("Amazon MemoryDB for Redis", "MemoryDB for Redis is also HIPAA-eligible with multi-AZ durability."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database, not ElastiCache."),
        ("Amazon Neptune", "Neptune is a graph database."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon ElastiCache for Redis is HIPAA-eligible and supports encryption at rest and in transit. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-hipaa.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid controls to encrypt data in transit for an internal microservices architecture? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("TLS with ACM certificates on the ALB", "TLS with ACM is the standard pattern."),
        ("mTLS using App Mesh or service mesh", "mTLS is mutual TLS for service-to-service auth."),
        ("VPC endpoint policies", "VPC endpoints encrypt the path to AWS services."),
        ("Plaintext HTTP for internal services", "Plaintext is an antipattern even for internal services."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use TLS via ACM, mTLS via service mesh, and VPC endpoint policies for in-transit encryption. Reference: https://docs.aws.amazon.com/app-mesh/latest/userguide/mutual-tls.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service provides automated, ML-based anomaly detection on AWS spend?",
    "type": "multiple-choice",
    "opts": [
        ("AWS App Mesh", "App Mesh supports mTLS via Envoy sidecars."),
        ("AWS Cloud Map", "Cloud Map is for service discovery."),
        ("Amazon API Gateway", "API Gateway is for north-south traffic."),
        ("AWS Step Functions", "Step Functions is for workflow orchestration."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS App Mesh provides mTLS for service-to-service auth via Envoy-based sidecars. Reference: https://docs.aws.amazon.com/app-mesh/latest/userguide/mutual-tls.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to enforce least-privilege access in AWS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("IAM Access Analyzer policy generation", "Access Analyzer generates least-privilege policies from observed usage."),
        ("IAM Access Analyzer unused access analysis", "Identifies granted permissions that are never used."),
        ("Grant AdministratorAccess to all developers", "Broad admin is an antipattern."),
        ("Use SCPs to enforce permission boundaries", "SCPs provide account-level guardrails."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Use Access Analyzer (policy generation + unused access) and SCPs to enforce least privilege. Granting admin to all developers is an antipattern. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated, ML-based anomaly detection on your AWS spend, useful for detecting compromised credentials used to spin up expensive resources?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Anomaly Detection", "Cost Anomaly Detection uses ML to detect spend anomalies."),
        ("AWS Budgets", "Budgets alert on thresholds, not anomalies."),
        ("AWS Cost Explorer", "Cost Explorer is for visualization and analysis."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Cost Anomaly Detection uses ML to detect and alert on unusual spend patterns, including from compromised credentials. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides a defense-in-depth security architecture for a public-facing web application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudFront with Origin Access Control", "CloudFront + OAC restricts origin access."),
        ("AWS WAF with managed rule groups", "WAF blocks common web exploits."),
        ("AWS Shield Advanced", "Shield Advanced adds DRT and cost protection."),
        ("Direct EC2 with public IP and no firewall", "Direct EC2 with public IP is an antipattern."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "CloudFront + OAC + WAF + Shield Advanced provides defense-in-depth. Direct EC2 with public IP is an antipattern. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed threat intelligence feed for known malicious IP addresses, and integrates with WAF and Network Firewall?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Shield Threat Landscape", "Shield Advanced includes threat intelligence."),
        ("Amazon GuardDuty threat intelligence", "GuardDuty uses AWS-managed threat intelligence."),
        ("AWS WAF Managed Rules", "WAF managed rules include reputation lists."),
        ("AWS Network Firewall with AWS managed rule groups", "Network Firewall managed rule groups include threat intel."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Amazon GuardDuty uses AWS-managed threat intelligence from CrowdStrike and other sources. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service provides a managed way to distribute and rotate IAM access keys?",
    "type": "multiple-choice",
    "opts": [
        ("Service control policies (SCPs)", "SCPs are org-wide permission guardrails."),
        ("Tag policies", "Tag policies enforce tagging standards."),
        ("Backup policies", "Backup policies enforce backup standards."),
        ("AI policies", "AWS Organizations does not have AI policies."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Organizations supports SCPs, tag policies, and backup policies. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed way to distribute and rotate IAM access keys for use with AWS services, with audit logging?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager with rotation", "Secrets Manager handles rotation and audit."),
        ("AWS Systems Manager Parameter Store only", "Parameter Store supports manual rotation; Secrets Manager has native rotation."),
        ("AWS KMS directly", "KMS is for keys, not secret rotation."),
        ("AWS IAM", "IAM does not manage application secrets."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Secrets Manager is the best practice for distributing and rotating secrets with audit logging. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for encrypting data AT REST in a multi-tier application with EC2, RDS, S3, and EBS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("EBS encryption with a CMK", "EBS encryption is at-rest protection for EC2 volumes."),
        ("RDS storage encryption with a CMK", "RDS encryption is at-rest protection for the database."),
        ("S3 default bucket encryption with SSE-KMS and a CMK", "S3 encryption is at-rest protection for object storage."),
        ("Plaintext EBS volumes", "Plaintext EBS volumes do not provide encryption."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Encrypt EBS, RDS, and S3 with a customer managed KMS key to protect data at rest across all tiers. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-overview-introduction/aws-shared-responsibility-model.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid features of AWS CloudHSM? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("FIPS 140-3 Level 3 validation", "CloudHSM is FIPS 140-3 Level 3 validated."),
        ("Single-tenant HSM access", "CloudHSM provides single-tenant HSM clusters."),
        ("Integration with KMS via custom key stores", "KMS custom key stores integrate with CloudHSM."),
        ("Free of charge", "CloudHSM is a paid service."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "CloudHSM is FIPS 140-3 Level 3, single-tenant, and integrates with KMS. Reference: https://docs.aws.amazon.com/cloudhsm/latest/userguide/what-is-cloudhsm.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated key rotation, key aliasing, and key policy management, with CloudTrail audit logs for every key use?",
    "type": "multiple-choice",
    "opts": [
        ("AWS KMS", "KMS provides key management with CloudTrail audit."),
        ("AWS CloudHSM alone", "CloudHSM does not provide aliasing or rotation natively."),
        ("AWS Secrets Manager", "Secrets Manager manages secrets, not encryption keys."),
        ("AWS SSM Parameter Store", "Parameter Store is for configuration values."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS KMS provides automated key rotation, aliasing, and policy management with CloudTrail audit. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service provides managed key rotation, aliasing, and audit logging for every key use?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudTrail with organization trail", "Org trail centralizes audit logs across accounts."),
        ("Amazon GuardDuty delegated admin", "GuardDuty delegated admin runs GuardDuty across all accounts."),
        ("AWS Security Hub with delegated admin", "Security Hub aggregates findings across accounts."),
        ("AWS Config alone", "Config is for resource configuration; Security Hub provides cross-account aggregation."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use CloudTrail, GuardDuty, and Security Hub with delegated admin for end-to-end multi-account security. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs to ensure all PHI (Protected Health Information) is encrypted at rest in their RDS PostgreSQL database. Which combination is the BEST approach? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Enable storage encryption on the RDS instance with a customer managed CMK at create time", "RDS encryption is set at create time with a CMK."),
        ("Restrict KMS key access via key policy to only the RDS service and authorized principals", "Key policy controls who can use the key."),
        ("Modify the existing unencrypted RDS instance in-place to enable encryption", "In-place modification is not supported; must create encrypted copy."),
        ("Disable encryption to improve performance", "Disabling encryption violates HIPAA and the customer's compliance requirements."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Enable RDS storage encryption with a CMK at create time, and restrict KMS key access via key policy. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs ALL access to PHI to be logged and retained for 7 years per HIPAA. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS CloudTrail organization trail writing to S3 with Object Lock in Compliance mode for 7 years", "Org trail + Object Lock Compliance provides immutable 7-year audit."),
        ("S3 Lifecycle policy to transition logs to Glacier after 1 year for cost", "Lifecycle reduces cost while keeping data accessible for 7 years."),
        ("KMS encryption on the audit log bucket with restricted key policy", "KMS encryption protects logs at rest."),
        ("Local application logs on EC2 with weekly manual backup", "Local EC2 logs do not meet 7-year immutable retention."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use CloudTrail org trail, S3 with Object Lock Compliance, S3 Lifecycle to Glacier, and KMS encryption. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to encrypt the on-premises-to-AWS Direct Connect link, which currently has no encryption. Which AWS service provides encryption for traffic over Direct Connect?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Site-to-Site VPN over Direct Connect (DX VPN)", "DX VPN provides IPsec encryption over the Direct Connect link."),
        ("AWS Direct Connect MACsec", "MACsec is a layer 2 encryption for Direct Connect connections."),
        ("AWS PrivateLink", "PrivateLink is for in-VPC service connectivity."),
        ("AWS Transit Gateway", "Transit Gateway is a hub, not an encryption service."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Direct Connect supports MACsec (layer 2) and DX VPN (IPsec) for encrypting traffic over the private link. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-macsec.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to ensure that the on-premises-to-AWS link is encrypted for HIPAA compliance. Which combination of encryption options should they use? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Direct Connect with MACsec", "MACsec provides layer 2 encryption over Direct Connect."),
        ("Site-to-Site VPN over Direct Connect (DX VPN)", "DX VPN provides IPsec over Direct Connect."),
        ("Plaintext Direct Connect without encryption", "Plaintext Direct Connect does not meet HIPAA encryption requirements."),
        ("Internet gateway with no encryption", "Internet gateway with no encryption is an antipattern for PHI."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Use MACsec or DX VPN to encrypt Direct Connect traffic for HIPAA. Plaintext is an antipattern. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-macsec.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, which SINGLE combination is BEST to ensure all PHI in RDS is encrypted at rest?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch Logs in a single account", "CloudWatch Logs is per-account and not ideal for 7-year retention."),
        ("Amazon S3 with Object Lock Compliance mode in a dedicated log archive account", "S3 Object Lock Compliance is the right tool for immutable, long-term retention."),
        ("Amazon EBS volumes in a single account", "EBS is for compute, not archival."),
        ("AWS Snowball", "Snowball is for physical data transfer, not ongoing logs."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use S3 with Object Lock Compliance mode in a dedicated log archive account for centralized 7-year audit retention. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants a DR strategy that meets RPO 15 min and RTO 1 hour for the patient portal. Which combination of services provides this? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Aurora Global Database with cross-region replication", "Aurora Global Database provides sub-second RPO across regions."),
        ("Multi-region active-active with Route 53 latency routing", "Active-active meets sub-1-hour RTO."),
        ("Single-AZ RDS without DR", "Single-AZ does not meet DR requirements."),
        ("Backup to Amazon S3 only with weekly restore", "Weekly backup does not meet 15-minute RPO."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Aurora Global Database + multi-region active-active with Route 53 meets RPO 15 min and RTO 1 hour. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to detect and respond to unauthorized access to PHI in S3 buckets. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Macie for sensitive data discovery", "Macie discovers and classifies PHI in S3."),
        ("Amazon GuardDuty S3 Protection for threat detection", "GuardDuty S3 Protection detects anomalous S3 API activity."),
        ("AWS CloudTrail S3 data events", "CloudTrail S3 data events record object-level API calls."),
        ("Disabling all S3 logging", "Disabling logging is a security antipattern."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use Macie, GuardDuty S3 Protection, and CloudTrail S3 data events for PHI detection and response. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs to enforce that PHI is NEVER uploaded to S3 buckets without encryption. Which S3 feature should they use?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Block Public Access", "Block Public Access is for public access, not encryption enforcement."),
        ("S3 bucket policy with s3:x-amz-server-side-encryption condition on PutObject", "Bucket policy can enforce encryption on uploads."),
        ("S3 Object Lock", "Object Lock is for immutability, not encryption."),
        ("S3 Inventory", "Inventory is a listing report."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Use a bucket policy with s3:x-amz-server-side-encryption condition to enforce encryption on PutObject. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to give 1.5M patients secure access to the portal via web and mobile apps with social login support. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Cognito", "Cognito provides user pools for B2C auth with social IdP support."),
        ("AWS IAM", "IAM is for AWS resource access, not consumer auth."),
        ("AWS Directory Service", "Directory Service is for enterprise AD."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Amazon Cognito user pools provide authentication for B2C apps with social IdP and SAML/OIDC support. Reference: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, which SINGLE service is BEST for the central log archive with 7-year immutable retention?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Directory Service with AD Connector", "AD Connector allows on-prem AD users to access AWS services."),
        ("Amazon Cognito", "Cognito is for end-user identity, not enterprise AD."),
        ("AWS IAM users with passwords", "IAM users for thousands of clinicians is not scalable."),
        ("AWS Secrets Manager", "Secrets Manager is for secrets, not identity."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Directory Service AD Connector allows on-premises AD users to access AWS without syncing users. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs to provide secure, time-limited access for an external auditor to read specific S3 buckets containing PHI reports. Which S3 feature is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Public S3 bucket", "Public buckets are an antipattern for PHI."),
        ("S3 presigned URL with a 1-hour expiration", "Presigned URLs grant time-limited access without making the bucket public."),
        ("S3 Object Lock with public read", "Object Lock is for immutability, not external sharing."),
        ("AWS WAF", "WAF is for web app traffic, not S3 sharing."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "S3 presigned URLs with short expiration provide time-limited access for external auditors. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to scan nightly lab-result uploads from partner labs via SFTP, and trigger a Lambda function for processing. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Transfer Family for SFTP", "Transfer Family is the managed SFTP service."),
        ("S3 event notifications to Lambda", "S3 events trigger Lambda on object creation."),
        ("Direct Lambda invocation from a public SFTP server", "Direct Lambda invocation is not a pattern; S3 events drive Lambda."),
        ("AWS Snowball", "Snowball is for physical data transfer, not nightly SFTP."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Use AWS Transfer Family for managed SFTP and S3 event notifications to drive Lambda processing. Reference: https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs a network architecture that isolates the patient portal web tier from the database tier. Which combination of subnets and security groups is the BEST practice? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Public subnets in multiple AZs for the ALB", "Public subnets host the ALB."),
        ("Private subnets in multiple AZs for the web tier", "Web tier in private subnets improves security."),
        ("Database subnets (private) for RDS", "Database subnets are isolated and private."),
        ("Database in the same security group as the web tier", "Same security group is an antipattern; use separate SGs."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use tiered subnets: public for ALB, private for web, database subnets for RDS, each with its own security group. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants the patient portal's database connections to be encrypted in transit, with the application authenticating via IAM database authentication. Which combination is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Enable TLS on the RDS endpoint", "TLS encrypts database traffic in transit."),
        ("Enable IAM database authentication on RDS", "IAM database authentication eliminates password management."),
        ("Disable TLS to reduce overhead", "Disabling TLS is an antipattern for HIPAA."),
        ("Embed DB passwords in application code", "Embedding passwords is a security antipattern."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Enable TLS and IAM database authentication on RDS for secure, passwordless connectivity. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, which SINGLE service is BEST for giving 1.5M patients secure portal access with social login?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon GuardDuty S3 Protection", "GuardDuty S3 Protection analyzes S3 API activity for threats."),
        ("AWS WAF", "WAF is for web app traffic, not S3."),
        ("Amazon Macie", "Macie is for sensitive data discovery, not exfiltration detection."),
        ("AWS Config", "Config tracks configuration changes."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "GuardDuty S3 Protection detects unusual S3 API activity that may indicate exfiltration. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst needs to apply different security policies to different OUs (e.g., Production, Development, Log Archive). Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Organizations with OUs and SCPs", "Organizations with OUs and SCPs is the multi-account governance pattern."),
        ("AWS Config only", "Config is for resource configuration."),
        ("AWS Security Hub only", "Security Hub aggregates findings, not account structure."),
        ("AWS Control Tower only", "Control Tower is for landing zone, not custom OU policies."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use AWS Organizations with OUs and SCPs to apply different policies to different account groups. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to grant a 3rd-party auditor READ-ONLY access to a single S3 bucket containing PHI reports, with all access logged. Which combination is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Create a dedicated IAM user for the auditor with read-only policy", "Dedicated IAM user with read-only access."),
        ("Enable S3 server access logs to a logging bucket", "S3 server access logs record every request."),
        ("Share the AWS root user credentials with the auditor", "Sharing root credentials is a critical security antipattern."),
        ("Skip logging to simplify access", "Skipping logging is an antipattern for HIPAA."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Create a dedicated IAM user with read-only access and enable S3 server access logs. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants to encrypt EBS volumes on EC2 instances running the patient portal. Which is the SIMPLEST approach?",
    "type": "multiple-choice",
    "opts": [
        ("Enable EBS encryption by default in the region", "Region-level default encryption automatically encrypts new EBS volumes."),
        ("Manually encrypt each volume via the CLI on every launch", "Manual encryption is error-prone."),
        ("Disable encryption to improve performance", "Disabling encryption violates HIPAA."),
        ("Use instance store only without EBS", "Instance store is ephemeral; not appropriate for databases."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Enable EBS encryption by default in the region to automatically encrypt new EBS volumes. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, HealthFirst wants a service that automatically rotates the database password used by the patient portal application. Which service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager with RDS rotation", "Secrets Manager can automatically rotate RDS passwords."),
        ("AWS Systems Manager Parameter Store alone", "Parameter Store supports manual rotation, not native RDS."),
        ("AWS KMS alone", "KMS is for encryption keys, not password rotation."),
        ("Hardcoded passwords in the application", "Hardcoded passwords are a security antipattern."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Secrets Manager with RDS rotation automatically rotates database passwords. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets.html",
})
QUESTIONS.append({
    "q": "In the HealthFirst scenario, which SINGLE service is BEST for federating clinician access from existing Active Directory?",
    "type": "multiple-choice",
    "opts": [
        ("CloudTrail with log file integrity validation", "Integrity validation detects log tampering."),
        ("S3 with Object Lock Compliance mode for 7 years", "Object Lock prevents log deletion even by root."),
        ("Mutable logs in a local EBS volume", "Mutable logs do not meet immutability requirements."),
        ("Disabling CloudTrail to reduce cost", "Disabling CloudTrail is a critical security antipattern for HIPAA."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Use CloudTrail with integrity validation and S3 Object Lock Compliance for tamper-proof, 7-year audit logs. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html",
})
QUESTIONS.append({
    "q": "Which IAM feature allows you to test whether a given IAM policy grants or denies a specific action for a specific principal?",
    "type": "multiple-choice",
    "opts": [
        ("IAM Policy Simulator", "Policy Simulator tests policy effects without executing actions."),
        ("IAM Access Analyzer", "Access Analyzer analyzes access, not single policy simulation."),
        ("AWS CloudTrail", "CloudTrail records past API calls."),
        ("AWS Config", "Config tracks resource configuration."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM Policy Simulator tests whether a policy grants or denies specific actions for a principal. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html",
})
QUESTIONS.append({
    "q": "Which IAM role type is automatically created by AWS services to allow them to call other AWS services on your behalf, with a trust policy predefined by AWS?",
    "type": "multiple-choice",
    "opts": [
        ("Service-linked role", "Service-linked roles are predefined by AWS services and cannot be modified."),
        ("Service role", "Service roles are custom roles you create for AWS services."),
        ("Cross-account role", "Cross-account roles are for one account accessing another."),
        ("IAM user", "IAM users are for individuals, not services."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Service-linked roles are predefined by AWS services and include the service's trust policy. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html",
})
QUESTIONS.append({
    "q": "Which combination of features is BEST for an application running on EC2 to access S3 without long-lived credentials? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("IAM role attached to the EC2 instance", "IAM role provides temporary credentials via IMDS."),
        ("Instance metadata service v2 (IMDSv2)", "IMDSv2 is the more secure metadata service."),
        ("Embed IAM access keys in the application", "Embedded access keys are an antipattern."),
        ("Hardcode the S3 access key in user data", "Hardcoded keys are an antipattern."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Use an IAM role with IMDSv2 for EC2 to access S3 without long-lived keys. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to enforce least-privilege in AWS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use AWS managed policies that match common job functions", "Job-function managed policies are a starting point for least-privilege."),
        ("Use IAM Access Analyzer policy generation", "Access Analyzer generates policies from observed usage."),
        ("Grant AdministratorAccess to all developers for convenience", "Broad admin is an antipattern."),
        ("Use customer managed policies scoped to specific actions and resources", "Scoped policies are the gold standard for least-privilege."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Use job-function policies, Access Analyzer, and scoped customer managed policies. Broad admin is an antipattern. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS CloudTrail helps you detect changes to IAM policies that grant elevated permissions?",
    "type": "multiple-choice",
    "opts": [
        ("CloudTrail Insights", "CloudTrail Insights detects unusual API activity."),
        ("CloudTrail event history search", "Event history lets you search and review past API calls."),
        ("AWS Config", "Config tracks resource configuration changes."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "CloudTrail event history allows you to search and review IAM policy changes for audit. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html",
})
QUESTIONS.append({
    "q": "Which IAM action is used to allow a service to ASSUME a role on your behalf, granting temporary credentials?",
    "type": "multiple-choice",
    "opts": [
        ("sts:AssumeRole", "sts:AssumeRole is the action for assuming a role."),
        ("iam:PassRole", "iam:PassRole is for passing a role to a service."),
        ("sts:GetSessionToken", "GetSessionToken is for IAM user credentials."),
        ("iam:CreateRole", "iam:CreateRole creates a role definition."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "sts:AssumeRole is the STS action that allows a principal to assume a role and receive temporary credentials. Reference: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html",
})
QUESTIONS.append({
    "q": "Which IAM action is used to pass a role to an AWS service, such as EC2 or Lambda, so the service can assume the role on your behalf?",
    "type": "multiple-choice",
    "opts": [
        ("sts:AssumeRole", "AssumeRole is for the service to actually use the role."),
        ("iam:PassRole", "iam:PassRole is required for the user to pass the role to the service."),
        ("iam:CreateRole", "CreateRole defines the role."),
        ("iam:AttachRolePolicy", "AttachRolePolicy attaches policies to the role."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "iam:PassRole is required for the user to pass a role to an AWS service; the service then calls sts:AssumeRole. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html",
})
QUESTIONS.append({
    "q": "Which SINGLE capability is the BEST description of AWS IAM Access Analyzer?",
    "type": "multiple-choice",
    "opts": [
        ("Identify resources shared with external principals", "Access Analyzer finds external access findings."),
        ("Generate least-privilege IAM policies from observed usage", "Access Analyzer generates policies from CloudTrail."),
        ("Scan S3 buckets for PHI", "S3 PHI scanning is Macie's job, not Access Analyzer."),
        ("Identify unused permissions", "Access Analyzer unused access analysis flags unused permissions."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Access Analyzer identifies external access, generates policies, and flags unused access. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html",
})
QUESTIONS.append({
    "q": "Which IAM feature allows you to require that all requests include a specific tag, such as requiring all EC2 instances to have a CostCenter tag?",
    "type": "multiple-choice",
    "opts": [
        ("aws:RequestTag condition key", "aws:RequestTag checks for tags on the resource being created or modified."),
        ("aws:ResourceTag condition key", "aws:ResourceTag checks for tags on existing resources."),
        ("aws:PrincipalTag condition key", "aws:PrincipalTag checks for tags on the principal making the request."),
        ("aws:TagKeys condition key", "aws:TagKeys checks for which tag keys are present."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "aws:RequestTag checks for tags on the resource being created or modified. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag",
})
QUESTIONS.append({
    "q": "Which condition key allows you to require that the requester has authenticated with MFA within the last few minutes?",
    "type": "multiple-choice",
    "opts": [
        ("aws:MultiFactorAuthPresent", "aws:MultiFactorAuthPresent checks for recent MFA authentication."),
        ("aws:MultiFactorAuthAge", "aws:MultiFactorAuthAge checks how long ago MFA was used."),
        ("aws:TokenIssueTime", "TokenIssueTime is for session policies."),
        ("aws:SourceVpce", "SourceVpce is for VPC endpoint constraints."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "aws:MultiFactorAuthAge allows you to require that MFA was used within a specified time window. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-multifactorauthage",
})
QUESTIONS.append({
    "q": "Which AWS service provides a temporary, limited-privilege credentials mechanism for workloads running OUTSIDE AWS using OIDC tokens?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Security Token Service (STS) with AssumeRoleWithWebIdentity", "AssumeRoleWithWebIdentity exchanges OIDC tokens for AWS credentials."),
        ("AWS Cognito", "Cognito provides user pools, not direct OIDC federation."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO."),
        ("AWS Directory Service", "Directory Service is for AD."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "STS AssumeRoleWithWebIdentity exchanges OIDC tokens from providers like Google, Facebook, or Auth0 for AWS temporary credentials. Reference: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html",
})
QUESTIONS.append({
    "q": "Which combination of services enables cross-account, OIDC-based authentication for a mobile app to call AWS APIs? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("OIDC identity provider (e.g., Google, Facebook)", "An OIDC IdP issues tokens to the mobile app."),
        ("An IAM role with a trust policy allowing the OIDC provider", "The role's trust policy allows the IdP to assume it."),
        ("AWS STS AssumeRoleWithWebIdentity", "STS exchanges the OIDC token for AWS credentials."),
        ("AWS root user credentials", "Root credentials are an antipattern for application auth."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use OIDC IdP, IAM role with trust policy, and STS AssumeRoleWithWebIdentity. Reference: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides automatic detection and remediation of public buckets, exposed access keys, and unintended cross-account access?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Macie", "Macie is for sensitive data discovery."),
        ("AWS Config with managed rules", "Config with managed rules like s3-bucket-public-read-prohibited can detect public buckets."),
        ("AWS CloudTrail alone", "CloudTrail records events; detection is not its primary role."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Config with managed rules like s3-bucket-public-read-prohibited detects public buckets and can trigger auto-remediation. Reference: https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html",
})
QUESTIONS.append({
    "q": "Which S3 encryption option provides the BEST integration with AWS KMS for audit logging in CloudTrail?",
    "type": "multiple-choice",
    "opts": [
        ("SSE-S3", "SSE-S3 uses S3-managed keys and is not logged in CloudTrail per object."),
        ("SSE-KMS", "SSE-KMS calls are logged in CloudTrail for audit."),
        ("SSE-C", "SSE-C is customer-managed and not logged in CloudTrail."),
        ("Client-side encryption", "Client-side is not logged in CloudTrail."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "SSE-KMS makes KMS Decrypt/Encrypt calls that are logged in CloudTrail for audit. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for storing sensitive data in S3 with row-level access control for different user groups? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Access Grants for per-user access", "Access Grants provide per-user access to S3."),
        ("IAM Identity Center integration with S3 Access Grants", "Identity Center + Access Grants for workforce SSO."),
        ("Public S3 bucket with no access control", "Public buckets with sensitive data are an antipattern."),
        ("Disabling S3 Block Public Access for the bucket", "Disabling Block Public Access is an antipattern."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Use S3 Access Grants with IAM Identity Center for per-user, group-based access to S3 data. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides a single endpoint that spans multiple regions, with automatic failover, for global applications?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Multi-Region Access Points", "Multi-Region Access Points span multiple regions with failover."),
        ("S3 Access Points", "Standard Access Points are per-region."),
        ("S3 Transfer Acceleration", "Transfer Acceleration speeds uploads, not failover."),
        ("CloudFront in front of S3", "CloudFront is a CDN, not a multi-region S3 endpoint."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Multi-Region Access Points provide a single global endpoint that spans multiple regions with automatic failover. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 security controls? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Block Public Access", "Block Public Access is the final override."),
        ("S3 Access Points with distinct policies", "Access Points provide per-application access."),
        ("S3 server access logs", "Server access logs provide object-level audit."),
        ("S3 Lifecycle policies", "Lifecycle is for storage class transitions, not security."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Block Public Access, Access Points, and server access logs are all security controls. Lifecycle is for cost, not security. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html",
})
QUESTIONS.append({
    "q": "Which S3 event type triggers when an object is created via the PUT, POST, or COPY API?",
    "type": "multiple-choice",
    "opts": [
        ("ObjectCreated:Put", "ObjectCreated:Put triggers on PUT, POST, or COPY API calls."),
        ("ObjectCreated:Get", "ObjectCreated:Get is not a valid event type."),
        ("ObjectRemoved:Delete", "ObjectRemoved:Delete is for deletes."),
        ("ObjectAccessed:Read", "ObjectAccessed:Read is not a standard event."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "ObjectCreated:Put triggers on PUT, POST, or COPY API calls to create an object. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html",
})
QUESTIONS.append({
    "q": "Which S3 encryption option requires the LEAST operational overhead and is the BEST choice for new buckets where you do not need customer managed keys?",
    "type": "multiple-choice",
    "opts": [
        ("SSE-S3 (AES-256)", "SSE-S3 is the simplest and is now default for new buckets."),
        ("SSE-KMS", "SSE-KMS requires KMS key management."),
        ("SSE-C", "SSE-C requires you to manage keys on every request."),
        ("Client-side encryption", "Client-side requires application changes."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "SSE-S3 is the simplest, with no key management overhead. It is now the default for new buckets. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html",
})
QUESTIONS.append({
    "q": "Which S3 feature automatically classifies and moves objects between access tiers based on changing access patterns, with no operational overhead?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects between tiers."),
        ("S3 Standard-IA only", "Standard-IA is a single tier."),
        ("S3 Glacier only", "Glacier is a single tier with retrieval charges."),
        ("S3 One Zone-IA only", "One Zone-IA is a single tier."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "S3 Intelligent-Tiering automatically moves objects between Frequent, Infrequent, Archive, and Deep Archive access tiers. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid KMS key policies? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Default key policy", "Default policy allows the root account full access."),
        ("Custom key policy", "Custom policies replace the default."),
        ("Policy that disables all access", "Disabling all access would render the key unusable."),
        ("Policy without any Allow statements", "An all-Deny policy would make the key unusable."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "KMS key policies can be default or custom. Disabling all access is not a valid pattern. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html",
})
QUESTIONS.append({
    "q": "Which KMS API call generates a data key for client-side encryption, returning both plaintext and ciphertext?",
    "type": "multiple-choice",
    "opts": [
        ("GenerateDataKey", "GenerateDataKey returns both plaintext and ciphertext data keys."),
        ("Encrypt", "Encrypt is for general encryption, not data key generation."),
        ("Decrypt", "Decrypt is for decrypting ciphertext."),
        ("DescribeKey", "DescribeKey returns metadata."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "GenerateDataKey returns both plaintext and ciphertext data keys for envelope encryption. Reference: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html",
})
QUESTIONS.append({
    "q": "Which KMS feature allows you to import your own key material into a KMS CMK?",
    "type": "multiple-choice",
    "opts": [
        ("Importing key material", "KMS supports importing your own key material for BYOK."),
        ("AWS managed keys", "AWS managed keys do not support custom key material import."),
        ("AWS owned keys", "AWS owned keys are not visible to you."),
        ("CloudHSM alone", "CloudHSM uses its own key material, separate from KMS CMKs."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "KMS supports importing your own key material (BYOK) into a customer managed CMK. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html",
})
QUESTIONS.append({
    "q": "Which AWS service allows you to BYOK (Bring Your Own Key) from your on-premises HSMs to AWS KMS?",
    "type": "multiple-choice",
    "opts": [
        ("AWS KMS with imported key material", "KMS supports importing key material from on-prem HSMs."),
        ("AWS CloudHSM with custom key store", "CloudHSM is a separate service, not KMS import."),
        ("AWS Secrets Manager", "Secrets Manager is for secrets, not BYOK."),
        ("AWS Parameter Store", "Parameter Store is for configuration."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS KMS allows BYOK by importing key material from on-prem HSMs into a customer managed CMK. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html",
})
QUESTIONS.append({
    "q": "Which combination of features is required to use AWS KMS with a customer managed CMK across MULTIPLE AWS accounts? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Cross-account key policy grants", "Key policy must grant access to other accounts."),
        ("IAM policies in the consuming accounts allowing kms:*", "IAM policies in the consuming account must allow KMS actions."),
        ("Disable cross-account access", "Disabling cross-account access prevents the pattern."),
        ("Use only AWS managed keys", "AWS managed keys cannot be shared cross-account."),
    ],
    "correct": "1,2",
    "domain": SECURE,
    "overall": "Cross-account KMS requires key policy grants and IAM policies in the consuming account. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, regional secret store with automatic rotation and fine-grained access control via IAM?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Secrets Manager", "Secrets Manager is the managed secret store with rotation."),
        ("AWS Systems Manager Parameter Store Standard", "Parameter Store Standard is free but lacks rotation and IAM."),
        ("AWS KMS", "KMS is for encryption keys, not secrets."),
        ("AWS IAM", "IAM is for AWS resource access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Secrets Manager is the regional managed secret store with rotation, IAM access control, and audit. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid features of AWS Network Firewall? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Stateless and stateful rule groups", "Network Firewall supports both rule types."),
        ("Suricata-compatible IDS/IPS rules", "Suricata rules are supported for stateful inspection."),
        ("TLS termination at the firewall", "Network Firewall does not terminate TLS; use ALB/NLB."),
        ("Centralized firewall policies across VPCs", "Firewall policies can be shared across VPCs."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Network Firewall supports stateless and stateful rules, Suricata IDS/IPS, and centralized policies. TLS termination is the responsibility of the load balancer. Reference: https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides VPC-level traffic mirroring for deep packet inspection by third-party security appliances?",
    "type": "multiple-choice",
    "opts": [
        ("VPC Traffic Mirroring", "VPC Traffic Mirroring copies network traffic for analysis."),
        ("VPC Flow Logs", "VPC Flow Logs record metadata, not full packets."),
        ("AWS Network Firewall", "Network Firewall inspects traffic but does not mirror it to external appliances."),
        ("AWS Direct Connect", "Direct Connect is a private link, not a mirroring service."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "VPC Traffic Mirroring copies network traffic from ENIs to security appliances for deep packet inspection. Reference: https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to block public internet access to EC2 instances? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Place instances in private subnets with no route to an internet gateway", "Private subnets with no IGW route are unreachable from the internet."),
        ("Use a security group that denies all inbound", "A security group with no inbound rules blocks inbound traffic."),
        ("Disable the EC2 instance", "Disabling the instance stops it; not the right pattern for ongoing access control."),
        ("Assign a public IP but no security group rules", "A public IP without ingress rules is unreachable."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Use private subnets, restrictive security groups, and avoid public IPs to block internet access. Disabling is not a long-term pattern. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html",
})
QUESTIONS.append({
    "q": "Which AWS feature provides a managed, highly available NAT service in a VPC?",
    "type": "multiple-choice",
    "opts": [
        ("NAT gateway", "NAT gateway is the AWS-managed NAT service."),
        ("NAT instance", "NAT instances are self-managed EC2 instances; legacy pattern."),
        ("Internet gateway", "An internet gateway is for public subnets, not NAT."),
        ("Egress-only internet gateway", "Egress-only IGW is for IPv6 outbound only."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "NAT gateway is the AWS-managed, highly available NAT service. NAT instances are legacy. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid best practices for VPC network security? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use security groups as the primary firewall", "Security groups are the primary per-resource firewall."),
        ("Use NACLs for stateless subnet-level rules", "NACLs provide subnet-level stateless filtering."),
        ("Open all ports in security groups for convenience", "Open all ports is a critical security antipattern."),
        ("Use AWS Network Firewall for advanced inspection", "Network Firewall provides IDS/IPS and L7 inspection."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "Use security groups, NACLs, and Network Firewall for layered VPC security. Open all ports is an antipattern. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html",
})
QUESTIONS.append({
    "q": "Which feature allows you to connect a VPC to AWS services (S3, DynamoDB, etc.) via a private network path, with no NAT gateway or internet gateway required?",
    "type": "multiple-choice",
    "opts": [
        ("VPC endpoint", "VPC endpoints provide private connectivity to AWS services."),
        ("Internet gateway", "An internet gateway is for public access."),
        ("NAT gateway", "NAT gateway is for outbound internet from private subnets."),
        ("AWS Direct Connect", "Direct Connect is for on-prem connectivity."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "VPC endpoints provide private connectivity to AWS services without NAT, IGW, or DX. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed Active Directory in AWS, with native integration to RDS, FSx, and AWS Managed Microsoft AD?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Directory Service for Microsoft Active Directory", "Managed Microsoft AD is a fully managed AD in AWS."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO."),
        ("Amazon Cognito", "Cognito is for B2C identity."),
        ("AWS IAM", "IAM is for AWS resource access."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Directory Service for Microsoft Active Directory provides a managed AD in AWS. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid features of AWS Directory Service AD Connector? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Allows on-prem AD users to access AWS services without syncing users", "AD Connector proxies to on-prem AD."),
        ("Provides read-only access to on-prem AD", "AD Connector is read-only proxy to on-prem AD."),
        ("Replaces on-prem AD entirely", "AD Connector does not replace on-prem AD; it connects to it."),
        ("Requires VPC peering to on-prem", "AD Connector requires network connectivity to on-prem AD (VPN or DX)."),
    ],
    "correct": "1,2,4",
    "domain": SECURE,
    "overall": "AD Connector proxies to on-prem AD for AWS access without syncing users. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides centralized identity management for a hybrid AWS + on-prem environment with Microsoft AD? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Managed Microsoft AD", "Managed Microsoft AD in AWS."),
        ("AD Connector for on-prem AD users", "AD Connector for on-prem AD integration."),
        ("IAM Identity Center with AD integration", "Identity Center can integrate with Managed AD for SSO."),
        ("Hardcoded credentials in EC2 user data", "Hardcoded credentials are a critical security antipattern."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Use Managed Microsoft AD + AD Connector + IAM Identity Center for hybrid identity. Reference: https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed directory in AWS with a subset of Microsoft AD features, useful for low-cost AD needs?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Directory Service Simple AD", "Simple AD is a low-cost subset of AD."),
        ("AWS Directory Service Managed Microsoft AD", "Managed Microsoft AD is the full AD, more expensive."),
        ("Amazon Cognito", "Cognito is for B2C, not AD."),
        ("AWS IAM", "IAM is not an AD."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Directory Service Simple AD provides a low-cost AD-compatible directory in AWS. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated security checks against the CIS AWS Foundations Benchmark?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Security Hub with CIS AWS Foundations Benchmark standard", "Security Hub runs the CIS standard."),
        ("AWS Config alone", "Config is for resource configuration rules."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
        ("Amazon Inspector", "Inspector is for vulnerability scanning."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Security Hub runs the CIS AWS Foundations Benchmark standard. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-cis.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides automated, multi-account security findings aggregation and remediation? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Security Hub with delegated admin", "Security Hub centralizes findings across accounts."),
        ("Amazon EventBridge for automated remediation", "EventBridge drives remediation workflows."),
        ("AWS Lambda for remediation actions", "Lambda executes remediation actions."),
        ("Disable GuardDuty to reduce noise", "Disabling GuardDuty is an antipattern."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Security Hub + EventBridge + Lambda is the standard auto-remediation pattern. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated security remediation playbooks that you can invoke in response to findings?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Systems Manager Automation runbooks", "SSM Automation runbooks perform remediation steps."),
        ("AWS CloudFormation alone", "CloudFormation is for infrastructure, not remediation per se."),
        ("AWS Lambda alone", "Lambda is a compute service, not a playbook service."),
        ("AWS Step Functions alone", "Step Functions is a workflow service."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Systems Manager Automation runbooks are the standard remediation playbook service. Reference: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed way to send AWS Security Hub findings to a SIEM such as Splunk or QRadar?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EventBridge with Security Hub integration", "EventBridge delivers findings to external targets via partners."),
        ("AWS Config", "Config tracks resource configuration, not Security Hub findings."),
        ("AWS CloudTrail", "CloudTrail is an event source, not a delivery mechanism."),
        ("Direct Security Hub API", "Direct API is not the managed integration pattern."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "EventBridge integrates with Security Hub findings to deliver to SIEMs via partner integrations. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html",
})



# ============================================================
# Build the CSV
# ============================================================

def build_csv():
    rows = []
    for q in QUESTIONS:
        rows.append(make_row(
            question=q["q"],
            qtype=q["type"],
            opts=q["opts"],
            correct=q["correct"],
            overall=q["overall"],
            domain=q["domain"],
        ))
    return rows


def main():
    rows = build_csv()
    assert len(rows) == 200, f"Expected 200, got {len(rows)}"

    counts = {SECURE: 0, RESILIENT: 0, HIGH_PERF: 0, COST_OPT: 0}
    multi = 0
    for q in QUESTIONS:
        counts[q["domain"]] += 1
        if q["type"] == "multi-select":
            multi += 1
    print(f"Domain counts: {counts}")
    print(f"Multi-select: {multi} ({multi*100/200:.1f}%)")
    # Set 2 is a Secure deep dive; Secure should be the heavy domain
    assert counts[SECURE] >= 150, f"Secure={counts[SECURE]} (expected >= 150 for D1 deep dive)"
    assert multi == 40, f"Multi-select={multi}"

    out = "/home/user/Cert/course/AWS-SAA-C03-03-practice-sets/set-2/practice-set-2.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        header = ["Question", "Question Type"]
        for i in range(1, 7):
            header.extend([f"Answer Option {i}", f"Explanation {i}"])
        header.extend(["Correct Answers", "Overall Explanation", "Domain"])
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print(f"Wrote {out} with {len(rows)} rows")


if __name__ == "__main__":
    main()
