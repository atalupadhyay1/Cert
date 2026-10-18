"""Builder for SAA-C03 Set 1 — Diagnostic Mixed (200q) + RetailCo case study.

Distribution: 60 Secure / 52 Resilient / 48 High-Performing / 40 Cost-Optimized
Multi-select: 20% = 40 questions
Case-study: 10 questions referencing RetailCo
"""

import csv

# Domain strings (must match exactly)
SECURE = "Design Secure Architectures"
RESILIENT = "Design Resilient Architectures"
HIGH_PERF = "Design High-Performing Architectures"
COST_OPT = "Design Cost-Optimized Architectures"


def make_row(
    question, qtype, opts, correct, overall, domain,
    case_study=False,
):
    """Build a row. opts is a list of (text, explanation) tuples. correct is 1-based string like '1' or '1,3'."""
    # pad opts to 6
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
# DESIGN SECURE ARCHITECTURES (60 questions)
# ============================================================

# --- IAM (10) ---
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
    "overall": "IAM evaluation logic: by default all requests are denied, an Allow permits, and an explicit Deny always overrides any Allow. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html",
})
QUESTIONS.append({
    "q": "Which of the following is the BEST single mechanism for granting cross-account access to AWS resources?",
    "type": "multiple-choice",
    "opts": [
        ("Use an IAM role with a trust policy in the target account", "Role assumption is the standard and most flexible cross-account pattern."),
        ("Use resource-based policies (e.g., bucket policy) on the target resource", "Resource policies are valid but only work for specific resource types and don't scale as broadly as roles. Valid option but not the BEST single answer in this scenario."),
        ("Share long-lived IAM user access keys between accounts", "Sharing static keys is a security antipattern and is not the recommended mechanism."),
        ("Use AWS Resource Access Manager (RAM)", "RAM is valid for sharing specific resource types (subnets, transit gateways), not a general cross-account access pattern. Valid option but not the BEST single answer in this scenario."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Cross-account access can be granted via IAM role assumption, resource-based policies, and AWS RAM. Sharing IAM user keys is an antipattern. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html",
})
QUESTIONS.append({
    "q": "Which policy type sets MAXIMUM permissions for member accounts in an AWS Organization, even if the account's IAM policy allows more?",
    "type": "multiple-choice",
    "opts": [
        ("Identity-based policy", "Identity-based policies grant, not restrict."),
        ("Service control policy (SCP)", "SCPs define the maximum permissions an account can use, regardless of IAM grants."),
        ("Session policy", "Session policies restrict a single role session, not the entire account."),
        ("Permissions boundary", "Permissions boundaries are attached to principals, not enforced org-wide by default."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "Service control policies (SCPs) are the guardrails in AWS Organizations that define the maximum permissions for member accounts. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
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
    "q": "Which of the following is the SINGLE BEST practice for managing IAM users in a typical AWS account?",
    "type": "multiple-choice",
    "opts": [
        ("Enable MFA for privileged users", "MFA is the single most important security baseline for privileged users."),
        ("Rotate access keys regularly", "Rotating keys is important, but the best practice is to eliminate them in favor of roles. Valid option but not the BEST single answer in this scenario."),
        ("Share root user credentials with the team", "The root user must be locked away; never share."),
        ("Use IAM Identity Center (SSO) instead of individual IAM users", "Identity Center is the recommended pattern for workforce access. Valid option but not the BEST single answer in this scenario."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Best practices: enable MFA, rotate keys, prefer IAM Identity Center, and never use the root user for daily work. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
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
    "q": "Which of the following is the BEST single rotation option for a customer managed CMK?",
    "type": "multiple-choice",
    "opts": [
        ("Automatic annual rotation for CMKs", "Customer managed CMKs can be configured for automatic annual rotation, the recommended pattern."),
        ("Manual rotation by creating a new CMK alias", "Manual rotation is possible by creating a new key and aliasing, but it is more operational overhead. Valid option but not the BEST single answer in this scenario."),
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
    "q": "What is the SIMPLEST way to encrypt all objects stored in an S3 bucket with a customer managed KMS key?",
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
    "q": "Which of the following is the SINGLE BEST way to share a private S3 object with a third party for a limited time without making the object public?",
    "type": "multiple-choice",
    "opts": [
        ("Generate a presigned URL with an expiration time", "Presigned URLs grant time-limited access without changing bucket policy."),
        ("Use the object's S3 URI with a public bucket", "Public bucket exposure is not the right pattern."),
        ("Use S3 Object Lambda to transform the object on read", "Object Lambda is for code-on-read transformation, not sharing."),
        ("Use S3 access point with a VPC origin", "Access points with VPC origin restrict sharing to a VPC, useful for some private sharing patterns. Valid option but not the BEST single answer in this scenario."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Generate a presigned URL with a short expiration. For time-limited sharing this is the right pattern; no public access is granted. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html",
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
    "q": "Which S3 security feature provides object-level audit logging for every API call?",
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
    "q": "Which of the following is the SINGLE required setting to enable S3 Cross-Region Replication?",
    "type": "multiple-choice",
    "opts": [
        ("Versioning enabled on both source and destination buckets", "Replication fundamentally requires versioning on both buckets."),
        ("An IAM role that S3 assumes to replicate objects", "An IAM role is required, but versioning is more fundamental. Valid option but not the BEST single answer in this scenario."),
        ("Both buckets in the same AWS account", "Replication works across accounts as well; same-account is not required."),
        ("The destination bucket must be in a different region for CRR", "CRR specifically requires a different region; SRR is same-region. Valid option but not the BEST single answer in this scenario."),
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
    "q": "Which feature records ALL network traffic passing through a VPC, used for security analysis and troubleshooting?",
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
    "q": "Which of the following are valid components of a VPC for connectivity? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Internet gateway", "IGWs provide public internet access."),
        ("NAT gateway", "NAT gateways allow outbound internet for private subnets."),
        ("Virtual private gateway", "A VGW is the AWS side of a VPN connection."),
        ("Transit gateway", "Transit Gateway connects multiple VPCs and on-prem networks."),
    ],
    "correct": "1,2,3,4",
    "domain": SECURE,
    "overall": "All four are valid VPC connectivity components. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
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
    "q": "Which AWS service protects web applications from common exploits like SQL injection and cross-site scripting at layer 7?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Shield", "Shield is for DDoS at L3/L4 (and L7 for Shield Advanced)."),
        ("AWS WAF", "WAF is the layer 7 web ACL for SQLi, XSS, and other exploits."),
        ("AWS Network Firewall", "Network Firewall is for VPC traffic, not web apps."),
        ("Amazon GuardDuty", "GuardDuty is a threat detection service."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS WAF inspects HTTP/HTTPS requests and can block common Layer 7 exploits like SQL injection and XSS. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "Which of the following are features of AWS Shield Advanced? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Always-on network flow monitoring", "Shield Advanced includes always-on detection."),
        ("DDoS cost protection for scaling charges", "Shield Advanced provides cost protection for usage spikes during attacks."),
        ("24/7 access to the AWS DDoS Response Team (DRT)", "Shield Advanced includes 24/7 DRT support."),
        ("Free for all AWS customers by default", "Shield Standard is free; Shield Advanced is paid."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "Shield Advanced provides always-on detection, cost protection, and DRT access. Shield Standard is the free default. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html",
})
QUESTIONS.append({
    "q": "Which service uses machine learning and threat intelligence to detect compromised accounts, exfiltration, and recon in your AWS environment?",
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
    "q": "Which service records the configuration history of AWS resources and evaluates them against rules for compliance?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudTrail", "CloudTrail records API calls, not configuration history."),
        ("AWS Config", "Config records configuration state and evaluates rules."),
        ("Amazon CloudWatch", "CloudWatch is for metrics and logs."),
        ("AWS Systems Manager", "SSM manages EC2 and ops items."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Config records configuration history of resources and evaluates them against managed or custom rules. Reference: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid CloudTrail configurations? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("A multi-region trail that records events in all enabled regions", "CloudTrail supports multi-region trails."),
        ("An organization trail that records events for all member accounts", "CloudTrail Lake and Organizations support org-wide trails."),
        ("Log file integrity validation", "CloudTrail supports log file integrity validation."),
        ("Built-in intrusion detection on every API call", "CloudTrail is a log source, not an IDS; GuardDuty consumes it."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "CloudTrail supports multi-region, organization trails, and log file integrity validation; it is not an IDS. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html",
})
QUESTIONS.append({
    "q": "Which service automatically rotates database credentials for RDS and Aurora, with no application code change?",
    "type": "multiple-choice",
    "opts": [
        ("AWS KMS", "KMS manages keys, not credentials."),
        ("AWS Secrets Manager with RDS integration", "Secrets Manager can rotate RDS credentials automatically."),
        ("AWS Systems Manager Parameter Store only", "Parameter Store supports manual rotation and some Lambda-based rotation, not native RDS integration."),
        ("AWS IAM", "IAM does not store database credentials."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Secrets Manager integrates with RDS and Aurora to automatically rotate database credentials. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed directory in AWS, including AD Connector for on-prem Active Directory integration?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Cognito", "Cognito is for end-user identity, not enterprise AD."),
        ("AWS Directory Service", "Directory Service offers Managed Microsoft AD, AD Connector, and Simple AD."),
        ("AWS IAM Identity Center", "Identity Center is for workforce SSO, not an AD."),
        ("AWS SSO only", "SSO is now called IAM Identity Center."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "AWS Directory Service provides Managed Microsoft AD, AD Connector, and Simple AD. Reference: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html",
})
QUESTIONS.append({
    "q": "Which service provides user pools and identity pools for mobile and web app authentication, and integrates with social IdPs and SAML/OIDC?",
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
    "q": "Which of the following is the SINGLE core feature of AWS IAM Identity Center?",
    "type": "multiple-choice",
    "opts": [
        ("Single sign-on to AWS accounts and business applications", "SSO to AWS accounts and SaaS apps is the defining feature of IAM Identity Center."),
        ("Integration with SAML 2.0 and OIDC identity sources", "IdP integration is important but the SSO capability is the core. Valid option but not the BEST single answer in this scenario."),
        ("Built-in Active Directory replacement", "Identity Center is not a directory."),
        ("Permission sets to map groups to AWS roles", "Permission sets are the access-control mechanism, downstream of SSO. Valid option but not the BEST single answer in this scenario."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "IAM Identity Center provides SSO, integrates with SAML/OIDC, and uses permission sets to map groups to AWS roles. Reference: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html",
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
    "q": "Which service automates the collection of evidence for audits, generating reports for PCI, ISO, and SOC?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Audit Manager", "Audit Manager automates evidence collection and report generation for audits."),
        ("AWS Security Hub", "Security Hub is for security findings aggregation."),
        ("AWS Trusted Advisor", "Trusted Advisor gives best-practice checks."),
        ("AWS Artifact", "Artifact provides compliance reports, not automated evidence collection."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Audit Manager continuously collects evidence and generates audit-ready reports for frameworks like PCI, ISO, and SOC. Reference: https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html",
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
    "q": "Which SINGLE AWS service is the foundation for high availability of a stateless web application?",
    "type": "multiple-choice",
    "opts": [
        ("Auto Scaling group across multiple Availability Zones", "ASG multi-AZ is the HA foundation for stateless apps."),
        ("Application Load Balancer across AZs", "ALB distributes across multi-AZ targets. Valid option but not the BEST single answer in this scenario."),
        ("Single-AZ RDS Multi-AZ deployment", "RDS Multi-AZ is for the database tier, not the web tier."),
        ("AWS Global Accelerator", "Global Accelerator is for global performance, not single-region HA."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Stateless web tier HA: ASG + ALB across multiple AZs. RDS Multi-AZ is for the database. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides synchronous replication to a standby in a different Availability Zone with automatic failover?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replica", "Read replicas are async and not for HA."),
        ("RDS Multi-AZ deployment", "Multi-AZ provides synchronous replication and automatic failover."),
        ("Aurora Global Database", "Global Database is cross-region, not the basic Multi-AZ."),
        ("RDS Proxy", "RDS Proxy is a connection pooler, not a failover mechanism."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "RDS Multi-AZ uses synchronous replication to a standby in another AZ with automatic failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html",
})
QUESTIONS.append({
    "q": "Which statement correctly describes the difference between RDS read replicas and RDS Multi-AZ?",
    "type": "multiple-choice",
    "opts": [
        ("Read replicas provide synchronous replication and automatic failover", "Multi-AZ provides sync replication and failover, not read replicas."),
        ("Read replicas are asynchronous and used for read scaling; Multi-AZ is for HA and failover", "Read replicas scale reads; Multi-AZ provides HA."),
        ("Both are identical", "They serve different purposes."),
        ("Multi-AZ is for reads", "Multi-AZ is for HA, not read scaling."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Read replicas are async and scale reads; Multi-AZ is sync replication for HA and automatic failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "Which combination of AWS services provides the SIMPLEST multi-AZ static website with high availability?",
    "type": "multiple-choice",
    "opts": [
        ("S3 with cross-region replication and Route 53", "S3 itself is multi-AZ and highly available; static website hosting on S3 is the simplest pattern."),
        ("EC2 + Auto Scaling + ALB", "EC2-based static sites are over-engineered."),
        ("Lambda + DynamoDB only", "Lambda is for compute, not serving static assets."),
        ("CloudFront + S3 only with no failover", "Without Route 53 failover or origin failover, the design is incomplete."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 is inherently multi-AZ; static website hosting on S3 is the simplest HA pattern. Add Route 53 and CRR for regional failover. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html",
})
QUESTIONS.append({
    "q": "Which Elastic Load Balancing feature performs health checks on registered targets and routes only to healthy ones?",
    "type": "multiple-choice",
    "opts": [
        ("Connection draining", "Connection draining is the deregistration delay."),
        ("Health checks", "Health checks determine target health and route only to healthy ones."),
        ("Sticky sessions", "Sticky sessions bind user to instance."),
        ("Cross-zone load balancing", "Cross-zone load balancing is about traffic distribution."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "ELB health checks determine target health, and traffic is routed only to healthy targets. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html",
})
QUESTIONS.append({
    "q": "Which AWS service automatically replaces unhealthy EC2 instances in an Auto Scaling group and maintains a desired capacity?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Lambda", "Lambda does not manage EC2 instances."),
        ("Amazon EC2 Auto Scaling with health checks", "Auto Scaling replaces unhealthy instances automatically."),
        ("AWS Systems Manager only", "SSM can run commands, not replace instances."),
        ("AWS OpsWorks", "OpsWorks is a configuration management service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "EC2 Auto Scaling replaces unhealthy instances automatically based on health checks. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html",
})
QUESTIONS.append({
    "q": "Which of the following is the SINGLE recommended scaling policy type in EC2 Auto Scaling?",
    "type": "multiple-choice",
    "opts": [
        ("Target tracking scaling", "Target tracking is the recommended policy type, similar to a thermostat maintaining a temperature."),
        ("Step scaling", "Step scaling reacts to alarm breaches with adjustable steps, useful for more complex patterns. Valid option but not the BEST single answer in this scenario."),
        ("Simple scaling", "Simple scaling adds/removes a fixed number of instances per alarm, basic pattern. Valid option but not the BEST single answer in this scenario."),
        ("Predictive scaling only via Lambda", "Predictive scaling is a native ASG feature, not a Lambda function."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ASG supports target tracking, step, simple, and predictive scaling. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html",
})
QUESTIONS.append({
    "q": "Which ALB feature preserves the source IP of the client when traffic reaches the backend, important for IP-based allowlisting?",
    "type": "multiple-choice",
    "opts": [
        ("Cross-zone load balancing", "Cross-zone is for traffic distribution across AZs."),
        ("Sticky sessions with cookie", "Sticky sessions route to same instance, not preserve source IP."),
        ("Client IP preservation (default for ALB)", "ALB preserves the client IP in the X-Forwarded-For header."),
        ("NLB only", "NLB preserves the client IP by default; ALB also does with XFF."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "Application Load Balancer preserves the client IP and forwards it in X-Forwarded-For. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-request-routing.html",
})
QUESTIONS.append({
    "q": "Which load balancer type is BEST for static IP addresses and extreme TCP/UDP performance?",
    "type": "multiple-choice",
    "opts": [
        ("Application Load Balancer", "ALB is HTTP/HTTPS layer 7."),
        ("Network Load Balancer", "NLB is layer 4 with static IPs and millions of connections."),
        ("Gateway Load Balancer", "GWLB is for third-party virtual appliances."),
        ("Classic Load Balancer", "CLB is legacy."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Network Load Balancer (NLB) is layer 4 with static IP addresses and high throughput. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automatic failover for DNS records based on health checks, redirecting users away from unhealthy endpoints?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("Amazon Route 53 with failover routing policy", "Route 53 failover routing switches to a backup on health check failure."),
        ("AWS Global Accelerator", "Global Accelerator uses anycast IPs but is not a DNS failover."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon Route 53 with failover routing policy performs DNS-based failover based on health checks. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
})
QUESTIONS.append({
    "q": "Which disaster recovery strategy has the LOWEST RTO and RPO but the HIGHEST cost, with a full secondary environment running and serving traffic?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup and restore has the highest RTO and lowest cost."),
        ("Pilot light", "Pilot light keeps only critical data and a minimum of services running."),
        ("Warm standby", "Warm standby has a scaled-down but running environment."),
        ("Multi-site active-active", "Multi-site active-active is the lowest RTO/RPO and highest cost."),
    ],
    "correct": "4",
    "domain": RESILIENT,
    "overall": "Multi-site active-active: full secondary running, lowest RTO/RPO, highest cost. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which DR strategy keeps a minimal version of the core services running in the DR region (e.g., database with replication) and scales up only when needed?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup/restore from cold storage has the highest RTO."),
        ("Pilot light", "Pilot light keeps a minimal core in the DR region ready to scale up."),
        ("Warm standby", "Warm standby runs a reduced environment, not minimal."),
        ("Multi-site", "Multi-site runs a full environment."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Pilot light: minimal core services running in the DR region, ready to scale up on demand. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which DR strategy has the LOWEST cost, but RTO is measured in HOURS, with data backed up to S3 and restored on demand?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup and restore is the lowest cost with the highest RTO."),
        ("Pilot light", "Pilot light is a step up from backup."),
        ("Warm standby", "Warm standby has lower RTO than pilot light."),
        ("Multi-site", "Multi-site has near-zero RTO."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Backup and restore is the lowest cost and the slowest RTO (hours). Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service replicates Aurora data across regions with sub-second replication lag and supports cross-region disaster recovery?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ", "Multi-AZ is single-region."),
        ("Aurora Global Database", "Aurora Global Database replicates across regions with sub-second lag."),
        ("Aurora read replica", "Read replicas are within a region."),
        ("DynamoDB Streams", "Streams are not replication."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Aurora Global Database provides cross-region replication with sub-second lag for DR. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature provides multi-region replication with multi-master writes for global applications?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Streams", "Streams are change-data capture, not replication."),
        ("DynamoDB Global Tables", "Global Tables provide multi-region, multi-master replication."),
        ("DynamoDB DAX", "DAX is an in-memory cache."),
        ("DynamoDB Accelerator Streams", "Not a real feature."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB Global Tables provide multi-region, multi-master replication for global applications. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
})
QUESTIONS.append({
    "q": "Which of the following are key DR concepts? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("RTO (Recovery Time Objective)", "RTO is how quickly you must recover."),
        ("RPO (Recovery Point Objective)", "RPO is the maximum acceptable data loss."),
        ("MTTR (Mean Time To Recovery)", "MTTR is the average recovery time."),
        ("MTU (Maximum Transmission Unit)", "MTU is a network concept unrelated to DR."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "RTO, RPO, and MTTR are all key DR metrics. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which combination of Route 53 routing policies provides the BEST multi-region active-active failover for a global application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Latency-based routing", "Latency routing directs users to the lowest-latency region."),
        ("Geolocation routing", "Geolocation routes by user location."),
        ("Weighted routing", "Weighted routing splits traffic across regions."),
        ("Simple routing", "Simple routing returns all records in random order; not for active-active."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "For multi-region active-active, use latency, geolocation, or weighted routing. Simple routing is not appropriate. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html",
})
QUESTIONS.append({
    "q": "Which service provides anycast IPs and improves global application availability and performance with health checks and instant regional failover?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53", "Route 53 is DNS-based."),
        ("AWS Global Accelerator", "Global Accelerator provides anycast IPs with health-check-based failover."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("AWS Direct Connect", "DX is a private network link."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS Global Accelerator provides anycast static IPs and instant regional failover based on health checks. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which combination provides cross-region, low-latency DNS for a global application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Route 53 latency-based routing", "Latency routing picks the lowest-latency region."),
        ("Amazon CloudFront with Route 53", "CloudFront caches content; Route 53 resolves origin."),
        ("Amazon API Gateway with multi-region endpoints", "API Gateway multi-region is for API failover."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs, not for global DNS."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use Route 53 latency routing and CloudFront for low-latency global DNS and content delivery. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a centralized dashboard for monitoring and managing AWS Backup across accounts and regions?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup Audit Manager", "AWS Backup provides centralized management and audit."),
        ("Amazon CloudWatch only", "CloudWatch is for metrics and logs."),
        ("AWS Config only", "Config tracks configuration changes."),
        ("AWS Systems Manager only", "SSM is for ops items."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup provides centralized backup management, compliance monitoring, and audit across accounts and regions. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a managed message QUEUE for decoupling producers and consumers, with standard and FIFO queue types?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS", "SNS is a pub/sub notification service."),
        ("Amazon SQS", "SQS is a managed message queue with standard and FIFO."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
        ("Amazon Kinesis", "Kinesis is a streaming data service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon SQS is the managed message queue with standard (best-effort ordering, at-least-once) and FIFO (exactly-once, ordered) types. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a managed pub/sub NOTIFICATION service that pushes messages to multiple subscribers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS", "SQS is a queue, not a pub/sub."),
        ("Amazon SNS", "SNS is the pub/sub notification service."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
        ("AWS Step Functions", "Step Functions orchestrates workflows."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon SNS is a pub/sub notification service that pushes to multiple subscribers (HTTP, SQS, Lambda, email, SMS). Reference: https://docs.aws.amazon.com/sns/latest/dg/welcome.html",
})
QUESTIONS.append({
    "q": "Which service is a serverless event bus that connects applications using events from AWS services, SaaS apps, and custom sources?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EventBridge", "EventBridge is the serverless event bus with SaaS integration."),
        ("Amazon SQS", "SQS is a queue."),
        ("Amazon SNS", "SNS is a notification service."),
        ("Amazon Kinesis Data Streams", "Kinesis is streaming."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon EventBridge is a serverless event bus for application integration with rules, schedules, and SaaS events. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for fan-out to multiple downstream consumers? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon SNS topic subscribed by multiple SQS queues", "SNS fan-out to SQS is the canonical pattern."),
        ("Amazon SNS topic with Lambda subscribers", "Lambda can subscribe directly to an SNS topic."),
        ("Single SQS queue with no fan-out", "A single SQS queue is not fan-out."),
        ("Direct calls to many services in a tight loop", "Tight-loop calls couple services."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Fan-out pattern: SNS topic with multiple subscribers (SQS queues, Lambda, HTTP endpoints). Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html",
})
QUESTIONS.append({
    "q": "Which service captures real-time streaming data with shards, retention up to 365 days, and fan-out to multiple consumers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis Data Streams is real-time streaming with shards and retention."),
        ("Amazon SQS", "SQS is a queue with at most 14-day retention."),
        ("Amazon SNS", "SNS is pub/sub notifications."),
        ("AWS Step Functions", "Step Functions is workflow orchestration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Kinesis Data Streams captures real-time streaming data with shards and configurable retention. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "Which service is a fully managed workflow orchestrator for coordinating distributed components using state machines?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Step Functions", "Step Functions coordinates distributed components using state machines."),
        ("Amazon SQS", "SQS is a queue, not an orchestrator."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
        ("AWS Lambda", "Lambda is a single function execution."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Step Functions coordinates distributed components and microservices using visual workflows. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html",
})
QUESTIONS.append({
    "q": "Which pattern BEST handles spikey, asynchronous workloads where order matters but exactly-once delivery is not required?",
    "type": "multiple-choice",
    "opts": [
        ("SQS Standard queue with Lambda consumers", "SQS Standard + Lambda scales to spikey async workloads."),
        ("Direct synchronous calls", "Sync calls do not absorb spikes."),
        ("S3 only", "S3 is storage, not a queue."),
        ("EC2 with cron", "Cron-based polling is inefficient."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS Standard with Lambda is the canonical pattern for spikey async workloads. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html",
})
QUESTIONS.append({
    "q": "Which combination is the BEST pattern for processing S3 events in a fault-tolerant, decoupled way? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 event notifications to an SQS queue with a DLQ", "SQS + DLQ handles failures and retries."),
        ("S3 event notifications to SNS topic with multiple SQS subscribers", "Fan-out via SNS to multiple SQS queues."),
        ("S3 event notifications to EventBridge for advanced filtering", "EventBridge adds rules-based filtering."),
        ("Polling S3 every second from EC2", "Polling is inefficient and not the best pattern."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use S3 event notifications with SQS, SNS fan-out, or EventBridge for decoupled, fault-tolerant processing. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html",
})
QUESTIONS.append({
    "q": "Which combination of SQS and Lambda provides the BEST fault-tolerance for message processing? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("SQS visibility timeout longer than Lambda timeout", "Visibility timeout must be longer than the Lambda timeout to prevent duplicate processing."),
        ("SQS dead-letter queue for failed messages", "DLQ captures messages that fail repeatedly."),
        ("Lambda reserved concurrency", "Reserved concurrency throttles Lambda invocations; useful but not fault-tolerance per se."),
        ("Lambda sync invocation with no DLQ", "Sync invocation without a DLQ loses failed messages."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "SQS + Lambda: visibility timeout > Lambda timeout, configure DLQ for failed messages. Reference: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html",
})
QUESTIONS.append({
    "q": "Which S3 replication type is asynchronous and replicates new objects to a bucket in a different region?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication (CRR)", "CRR replicates to a different region asynchronously."),
        ("S3 Same-Region Replication (SRR)", "SRR is in the same region."),
        ("S3 Batch Replication", "Batch is for existing objects."),
        ("S3 Live Replication", "Not a real feature."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Cross-Region Replication (CRR) asynchronously replicates new objects to a destination bucket in a different region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which S3 feature replicates existing objects (not just new ones) on demand?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle", "Lifecycle transitions and expires objects."),
        ("S3 Batch Replication", "S3 Batch Replication replicates existing objects on demand."),
        ("S3 Inventory", "Inventory is a listing."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Batch Replication replicates existing objects that were not replicated by standard replication. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides centralized backup across AWS services (EBS, RDS, DynamoDB, EFS) with policy-based retention?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup", "AWS Backup is the centralized backup service across many AWS resources."),
        ("Amazon CloudWatch", "CloudWatch is monitoring."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS Config", "Config tracks configuration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup centralizes and automates backup across services with policies and retention. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides point-in-time recovery within the retention period (up to 35 days)?",
    "type": "multiple-choice",
    "opts": [
        ("Automated backups", "Automated backups enable point-in-time recovery up to 35 days."),
        ("Manual snapshots only", "Manual snapshots are user-initiated, not continuous."),
        ("Multi-AZ", "Multi-AZ is for HA, not point-in-time recovery."),
        ("Read replicas", "Read replicas scale reads."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "RDS automated backups enable point-in-time recovery to any second within the retention period (up to 35 days). Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html",
})
QUESTIONS.append({
    "q": "Which Amazon CloudWatch feature provides a single dashboard with metrics from multiple AWS accounts and regions?",
    "type": "multiple-choice",
    "opts": [
        ("CloudWatch cross-account cross-region dashboards", "CloudWatch supports cross-account and cross-region dashboards."),
        ("AWS Organizations alone", "Organizations is for account management."),
        ("AWS Config alone", "Config is for configuration."),
        ("AWS Systems Manager alone", "SSM is for ops items."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch cross-account cross-region dashboards aggregate metrics into a single dashboard. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html",
})
QUESTIONS.append({
    "q": "Which AWS service aggregates logs from multiple accounts and regions for centralized analysis?",
    "type": "multiple-choice",
    "opts": [
        ("CloudWatch Logs with cross-account subscriptions", "CloudWatch Logs subscriptions deliver to a central account."),
        ("AWS Config", "Config is for resource configuration."),
        ("AWS CloudTrail alone", "CloudTrail is a log source, not a log aggregator."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch Logs subscriptions can deliver logs to a central account for aggregation and analysis. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html",
})
QUESTIONS.append({
    "q": "Which service is the AWS-native implementation of the Well-Architected Framework's Reliability Pillar?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Well-Architected Tool", "The AWS Well-Architected Tool reviews workloads against the framework."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
        ("AWS Config only", "Config is for configuration compliance."),
        ("AWS Service Catalog", "Service Catalog is for IT service governance."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "The AWS Well-Architected Tool helps you review workloads against the framework, including the Reliability Pillar. Reference: https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which of the following are key design principles of the Reliability Pillar? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Automatically recover from failure", "Automated recovery is a reliability principle."),
        ("Test recovery procedures", "Regular recovery testing is essential."),
        ("Scale horizontally to improve availability", "Horizontal scaling is a reliability pattern."),
        ("Manage change via automation", "Automation reduces manual error."),
    ],
    "correct": "1,2,3,4",
    "domain": RESILIENT,
    "overall": "Reliability Pillar principles include automated recovery, testing, horizontal scaling, and change management via automation. Reference: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/reliability-pillar.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides infrastructure-as-code templates to define and provision AWS resources in a repeatable way?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudFormation", "CloudFormation is the AWS-native IaC service."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS Config", "Config tracks configuration."),
        ("AWS CodeDeploy", "CodeDeploy is for application deployments."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS CloudFormation defines AWS resources in JSON/YAML templates for repeatable, version-controlled provisioning. Reference: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which service is a regional, low-latency, fully managed in-memory key-value store supporting Redis and Memcached?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database, not in-memory cache."),
        ("Amazon ElastiCache", "ElastiCache is the managed Redis and Memcached service."),
        ("Amazon MemoryDB", "MemoryDB is a Redis-compatible durable in-memory database."),
        ("AWS Cloud Map", "Cloud Map is a service discovery service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon ElastiCache is the managed in-memory key-value store supporting Redis and Memcached. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html",
})
QUESTIONS.append({
    "q": "Which service complements ElastiCache by providing an in-memory cache specifically for DynamoDB to reduce read latency from milliseconds to microseconds?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is a CDN, not a DynamoDB cache."),
        ("Amazon DynamoDB Accelerator (DAX)", "DAX is the in-memory cache for DynamoDB."),
        ("Amazon ElastiCache", "ElastiCache is general-purpose, not DynamoDB-specific."),
        ("AWS PrivateLink", "PrivateLink is for private connectivity."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB Accelerator (DAX) is the in-memory cache for DynamoDB, reducing read latency from ms to µs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy is BEST for active-passive failover between two regions?",
    "type": "multiple-choice",
    "opts": [
        ("Latency-based routing", "Latency routing is for active-active."),
        ("Failover routing", "Failover routing is designed for active-passive."),
        ("Weighted routing", "Weighted routing splits traffic; not for failover."),
        ("Geolocation routing", "Geolocation routes by user location."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Failover routing policy directs traffic to a primary and falls over to a secondary based on health checks. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy splits traffic between two regions in a fixed ratio (e.g., 70/30) for canary or A/B testing?",
    "type": "multiple-choice",
    "opts": [
        ("Latency routing", "Latency routing picks lowest latency."),
        ("Weighted routing", "Weighted routing splits traffic by ratios."),
        ("Failover routing", "Failover is active-passive."),
        ("Geolocation routing", "Geolocation routes by user location."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Weighted routing policy routes traffic in ratios you specify; useful for canary or A/B. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy routes based on the geographic location of the user (continent, country, US state)?",
    "type": "multiple-choice",
    "opts": [
        ("Geolocation routing", "Geolocation routes by user location."),
        ("Latency routing", "Latency routes by network latency."),
        ("Geoproximity routing", "Geoproximity uses bias to shift traffic."),
        ("Failover routing", "Failover is for active-passive."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Geolocation routing routes based on the user's continent, country, or US state. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geolocation.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature lets you use a percentage bias to shift traffic between regions, even to nearby regions, with traffic flow rules?",
    "type": "multiple-choice",
    "opts": [
        ("Geoproximity routing with traffic flow", "Geoproximity uses a bias to shift traffic."),
        ("Latency routing", "Latency routing is automatic based on network latency."),
        ("Weighted routing", "Weighted is for fixed ratios."),
        ("Multivalue answer routing", "Multivalue returns up to 8 healthy records."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Geoproximity routing uses a bias value to shift traffic toward or away from a region. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature lets you return up to 8 healthy records in response to a single DNS query, for client-side load balancing?",
    "type": "multiple-choice",
    "opts": [
        ("Multivalue answer routing", "Multivalue returns up to 8 healthy records."),
        ("Weighted routing", "Weighted is for fixed ratios."),
        ("Failover routing", "Failover is for active-passive."),
        ("Latency routing", "Latency returns a single record."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Multivalue answer routing returns up to 8 healthy records, enabling client-side load balancing. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html",
})
QUESTIONS.append({
    "q": "Which feature of Auto Scaling groups replaces unhealthy instances automatically based on health check status?",
    "type": "multiple-choice",
    "opts": [
        ("Health check replacement", "ASG replaces unhealthy instances automatically based on health checks."),
        ("Lifecycle hooks only", "Lifecycle hooks pause actions, do not replace."),
        ("Termination policies only", "Termination policies select which instance to terminate."),
        ("Scaling policies", "Scaling policies adjust capacity."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Auto Scaling groups use health checks (EC2 or ELB) to detect and replace unhealthy instances. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html",
})
QUESTIONS.append({
    "q": "Which ASG termination policy BALANCES instances across Availability Zones before selecting an instance to terminate?",
    "type": "multiple-choice",
    "opts": [
        ("Default", "The default termination policy is to balance across AZs."),
        ("OldestInstance", "OldestInstance terminates the oldest, not AZ-balanced."),
        ("NewestInstance", "NewestInstance terminates the newest."),
        ("OldestLaunchConfiguration", "OldestLaunchConfiguration terminates by launch config age."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "The default ASG termination policy balances instances across AZs before selecting. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html",
})
QUESTIONS.append({
    "q": "Which ASG feature drains existing connections before terminating an instance, used with ELB?",
    "type": "multiple-choice",
    "opts": [
        ("Connection draining (deregistration delay) on ELB", "ELB connection draining drains existing connections."),
        ("Termination protection", "Termination protection is a separate EC2 API."),
        ("Lifecycle hooks", "Lifecycle hooks pause actions but do not drain ELB connections."),
        ("Health check grace period", "Grace period is when ASG waits before terminating unhealthy."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ELB connection draining (now called deregistration delay) drains in-flight requests before instance termination. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#deregistration-delay",
})
QUESTIONS.append({
    "q": "Which service provides a logically isolated section of the AWS Cloud where you can launch resources in a defined virtual network?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon VPC", "Amazon VPC is the logically isolated virtual network."),
        ("AWS Direct Connect", "Direct Connect is a private network link."),
        ("Amazon Route 53", "Route 53 is a DNS service."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs and on-prem networks."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon VPC provides a logically isolated section of the AWS Cloud for your resources. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
})
QUESTIONS.append({
    "q": "Which VPC component connects a VPC to your on-premises network via an IPsec VPN tunnel over the public internet?",
    "type": "multiple-choice",
    "opts": [
        ("Internet gateway", "An internet gateway is for public internet access."),
        ("Virtual private gateway + customer gateway + VPN connection", "A VPN uses VGW on the AWS side and CGW on-prem."),
        ("AWS Direct Connect", "Direct Connect is a dedicated private fiber link."),
        ("NAT gateway", "NAT gateway is for outbound internet from private subnets."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Site-to-site VPN uses a Virtual Private Gateway on AWS and a Customer Gateway on-prem, with an IPsec tunnel over the internet. Reference: https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is OPTIMIZED for high-performance databases and in-memory caches with the BEST memory-to-CPU ratio?",
    "type": "multiple-choice",
    "opts": [
        ("C family (compute optimized)", "C family is compute-optimized, not memory."),
        ("M family (general purpose)", "M family is balanced, not memory-optimized."),
        ("R family (memory optimized)", "R family has the best memory-to-CPU ratio for in-memory workloads."),
        ("I family (storage optimized)", "I family is storage-optimized."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "R family is memory-optimized for high-performance databases and in-memory caches. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/rtypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is OPTIMIZED for compute-intensive workloads such as batch processing, scientific modeling, and gaming servers?",
    "type": "multiple-choice",
    "opts": [
        ("C family (compute optimized)", "C family is compute-optimized."),
        ("M family (general purpose)", "M family is balanced."),
        ("R family (memory optimized)", "R family is memory-optimized."),
        ("X family", "X family is for SAP HANA, ultra-high memory."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "C family is compute-optimized for batch, scientific modeling, and gaming. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/ctypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 placement group is BEST for a tightly coupled HPC application that needs the LOWEST network latency?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster placement groups pack instances close together for low-latency HPC."),
        ("Partition placement group", "Partition groups spread across racks, isolating failure domains."),
        ("Spread placement group", "Spread groups put instances on distinct hardware, for critical instances."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Cluster placement group: instances in one AZ with low-latency, high-bandwidth networking for HPC. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which EC2 placement group is BEST for a group of CRITICAL instances where each must be on DISTINCT underlying hardware?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster packs instances close together."),
        ("Spread placement group", "Spread puts each instance on distinct hardware."),
        ("Partition placement group", "Partition spreads across racks but groups instances within partitions."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Spread placement group: each instance on distinct hardware, reducing correlated failures for critical workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which placement group type divides hardware into logical partitions, with each partition isolated from failures of other partitions, useful for HDFS, Hadoop, and Cassandra?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster packs close for low latency."),
        ("Spread placement group", "Spread is for distinct hardware per instance."),
        ("Partition placement group", "Partition groups instances into partitions across racks."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Partition placement groups isolate failure domains at the rack level for distributed big-data workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which EC2 Nitro feature provides high-performance EBS I/O, with up to 64,000 IOPS and 1,000 MB/s on gp3?",
    "type": "multiple-choice",
    "opts": [
        ("EBS-optimized instances", "EBS-optimized instances provide dedicated EBS bandwidth and IOPS."),
        ("Instance store", "Instance store is local, not EBS."),
        ("EBS snapshot", "Snapshots are for backup, not I/O."),
        ("EBS encryption", "Encryption does not change I/O performance guarantees."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS-optimized instances provide dedicated EBS bandwidth and IOPS, decoupled from general network. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service is the foundation of a highly scalable, event-driven, serverless application?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Lambda", "Lambda is the serverless compute service and the foundation of event-driven architectures."),
        ("Amazon API Gateway", "API Gateway exposes HTTP APIs to Lambda but is not the compute foundation. Valid option but not the BEST single answer in this scenario."),
        ("Amazon DynamoDB", "DynamoDB is the serverless NoSQL database, a great choice for state. Valid option but not the BEST single answer in this scenario."),
        ("Amazon EC2 with cron jobs", "EC2 cron jobs are not serverless."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Lambda is the serverless compute foundation; pair it with API Gateway and DynamoDB for a fully serverless stack. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature allows a function to be triggered by events from many AWS services without writing integration code?",
    "type": "multiple-choice",
    "opts": [
        ("Event source mappings", "Event source mappings poll streams and queues."),
        ("Lambda destinations", "Destinations send to async targets on success/failure."),
        ("Lambda triggers built-in for many services", "Many services (S3, DynamoDB Streams, EventBridge) directly invoke Lambda."),
        ("Lambda layers", "Layers package code/dependencies."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Many AWS services (S3, DynamoDB Streams, EventBridge, SNS) directly invoke Lambda functions as event sources. Reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html",
})
QUESTIONS.append({
    "q": "Which service runs containers without managing servers or clusters, integrating with the broader AWS ecosystem?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS with EC2 launch type", "ECS with EC2 requires managing EC2 instances."),
        ("AWS Fargate", "Fargate runs containers without managing servers."),
        ("Amazon EKS with self-managed nodes", "EKS with self-managed nodes is not serverless."),
        ("AWS Lambda", "Lambda is for functions, not containers."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "AWS Fargate is the serverless compute engine for containers with ECS and EKS. Reference: https://docs.aws.amazon.com/fargate/latest/userguide/what-is-fargate.html",
})
QUESTIONS.append({
    "q": "Which AWS service runs batch computing jobs across many EC2 instances, with managed job scheduling and dynamic scaling?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Batch", "AWS Batch dynamically provisions compute for batch jobs."),
        ("AWS Lambda", "Lambda has a 15-minute max execution time."),
        ("Amazon ECS", "ECS is for long-running services, not batch jobs typically."),
        ("AWS Step Functions alone", "Step Functions orchestrates but does not run jobs."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Batch runs batch computing workloads on EC2, Spot, or Fargate with managed job scheduling. Reference: https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type provides the HIGHEST IOPS and is BEST for I/O-intensive databases such as Oracle and SAP HANA?",
    "type": "multiple-choice",
    "opts": [
        ("gp3", "gp3 is general-purpose SSD."),
        ("io2 Block Express", "io2 Block Express provides the highest IOPS."),
        ("st1", "st1 is throughput-optimized HDD."),
        ("sc1", "sc1 is cold HDD."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "io2 Block Express provides up to 256,000 IOPS and 4,000 MB/s for I/O-intensive workloads. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST balance of price and performance for most general workloads, allowing independent provisioning of IOPS and throughput?",
    "type": "multiple-choice",
    "opts": [
        ("gp2", "gp2 ties IOPS to volume size."),
        ("gp3", "gp3 decouples IOPS and throughput from volume size."),
        ("io1", "io1 is for high-I/O workloads, not general."),
        ("st1", "st1 is throughput-optimized HDD."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "gp3 lets you provision IOPS and throughput independently of volume size, at a lower price than gp2. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST choice for BIG DATA, log processing, and data warehouses with HIGH THROUGHPUT but low IOPS requirements?",
    "type": "multiple-choice",
    "opts": [
        ("gp3", "gp3 is balanced SSD."),
        ("io2", "io2 is high-IOPS SSD."),
        ("st1", "st1 is throughput-optimized HDD for big data."),
        ("sc1", "sc1 is cold HDD for infrequent access."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "st1 is throughput-optimized HDD for big data, log processing, and data warehouses. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/throughput-optimized.html",
})
QUESTIONS.append({
    "q": "Which EBS feature can you use to INCREASE the IOPS of a gp2 volume by combining multiple volumes into a single logical volume?",
    "type": "multiple-choice",
    "opts": [
        ("EBS snapshots", "Snapshots are for backup."),
        ("EBS volume striping across multiple volumes using RAID 0", "RAID 0 across multiple EBS volumes increases IOPS and throughput."),
        ("EBS encryption", "Encryption is unrelated to IOPS."),
        ("EBS volume modification", "Modification changes size or type but does not stripe."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "RAID 0 (striping) across multiple EBS volumes linearly increases IOPS and throughput. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/raid-config.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature increases S3 PUT throughput the most when uploading a single large file?",
    "type": "multiple-choice",
    "opts": [
        ("S3 multipart upload", "Multipart upload splits large files into parts for parallel upload, the most common throughput optimization."),
        ("S3 Transfer Acceleration with CloudFront edge", "Transfer Acceleration speeds up cross-region uploads via CloudFront edges. Valid option but not the BEST single answer in this scenario."),
        ("S3 byte-range fetches", "Byte-range fetches parallelize GETs, not uploads. Valid option but not the BEST single answer in this scenario."),
        ("S3 Object Lock", "Object Lock is for immutability, not throughput."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Use multipart upload, Transfer Acceleration, and byte-range fetches to maximize S3 throughput. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class provides MILLISECOND retrieval and is the BEST fit for archive data accessed once per quarter?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Standard-IA", "Standard-IA is for infrequent millisecond access."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive has hours retrieval."),
        ("S3 Glacier Flexible Retrieval", "Flexible Retrieval is minutes to hours."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "S3 Standard-IA provides millisecond retrieval for infrequent access at lower storage cost. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for data accessed once per YEAR with retrieval times in HOURS?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard-IA", "Standard-IA is millisecond retrieval."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest-cost storage with hours retrieval."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects between tiers."),
        ("S3 One Zone-IA", "One Zone-IA is for infrequent access but millisecond retrieval."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "S3 Glacier Deep Archive has the lowest storage cost and retrieval times of 12-48 hours. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which storage class automatically moves objects between access tiers based on usage patterns, with no retrieval charges?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering monitors access and moves objects automatically."),
        ("S3 Standard", "Standard is the default tier; not automatic."),
        ("S3 Glacier", "Glacier has retrieval charges."),
        ("S3 Standard-IA", "Standard-IA has retrieval charges."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Intelligent-Tiering automatically moves objects between Frequent, Infrequent, Archive, and Deep Archive access tiers, with no retrieval charges. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which SINGLE characteristic is the BEST description of Amazon EFS?",
    "type": "multiple-choice",
    "opts": [
        ("Shared NFS file system for thousands of EC2 instances", "EFS is a shared NFS file system for thousands of EC2 instances."),
        ("Regional, multi-AZ by default", "EFS is regional and multi-AZ; this is also a key characteristic. Valid option but not the BEST single answer in this scenario."),
        ("Lowest-cost general-purpose file system", "EFS IA is low-cost, but EFS Standard is the higher-performance tier; not the lowest-cost."),
        ("Object storage, accessed via HTTP", "EFS is a file system, not object storage; access is via NFS."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EFS is a shared, regional, multi-AZ NFS file system. Reference: https://docs.aws.amazon.com/efs/latest/ug/what-is-efs.html",
})
QUESTIONS.append({
    "q": "Which file system is the BEST fit for high-performance computing workloads requiring low-latency parallel access to data (e.g., ML training, video rendering)?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EFS", "EFS is a general-purpose NFS file system."),
        ("Amazon FSx for Lustre", "FSx for Lustre is high-performance, parallel, low-latency file system."),
        ("Amazon EBS", "EBS is block storage for a single instance."),
        ("Amazon S3", "S3 is object storage, not a file system."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon FSx for Lustre provides high-performance, parallel file system for HPC, ML, and video rendering. Reference: https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature provides an in-memory cache that reduces read latency from milliseconds to microseconds?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Streams", "Streams are change-data capture."),
        ("DynamoDB DAX", "DAX is the in-memory cache for DynamoDB."),
        ("DynamoDB Global Tables", "Global Tables provide multi-region replication."),
        ("DynamoDB Accelerator Streams", "Not a real feature."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "DynamoDB Accelerator (DAX) is the in-memory cache for DynamoDB, reducing read latency from ms to µs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB design principle is MOST important for achieving consistent performance at scale?",
    "type": "multiple-choice",
    "opts": [
        ("Use monotonically increasing partition keys (e.g., timestamp)", "Monotonically increasing keys create hot partitions; this is the wrong pattern."),
        ("Choose partition keys with high cardinality and uniform access patterns", "High-cardinality keys with uniform access prevent hot partitions."),
        ("Use a single partition key for all items", "Single keys create hot partitions."),
        ("Use the smallest possible item size", "Item size matters but uniform access is more important for partition distribution."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "High-cardinality, uniformly distributed partition keys are essential to avoid hot partitions in DynamoDB. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature AUTOMATICALLY redistributes partitions to handle hot partitions, without operator intervention?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB adaptive capacity", "Adaptive capacity automatically redistributes throughput to hot partitions."),
        ("DynamoDB streams", "Streams are change-data capture."),
        ("DynamoDB transactions", "Transactions provide ACID across items."),
        ("DynamoDB TTL", "TTL expires items."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "DynamoDB adaptive capacity automatically redistributes throughput to frequently accessed partitions, mitigating hot partition issues. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html",
})
QUESTIONS.append({
    "q": "Which combination of read options in DynamoDB provides STRONGLY CONSISTENT reads? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Specify ConsistentRead=true on GetItem", "ConsistentRead=true gives strong consistency."),
        ("Specify ConsistentRead=true on Query", "ConsistentRead=true on Query gives strong consistency."),
        ("Default GetItem is strongly consistent", "Default is eventually consistent; specify ConsistentRead=true."),
        ("Default Scan is strongly consistent", "Default Scan is eventually consistent."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "DynamoDB default reads are eventually consistent. Use ConsistentRead=true on GetItem, Query, or Scan for strong consistency. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides automatic scaling of compute and memory for unpredictable workloads, billed per second?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replicas", "Read replicas scale reads, not compute."),
        ("Amazon Aurora Serverless", "Aurora Serverless auto-scales compute and memory, billed per second."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon Aurora Serverless v2 auto-scales compute and memory capacity based on application load, billed per second. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html",
})
QUESTIONS.append({
    "q": "Which service provides graph database capabilities for highly connected data such as social networks and fraud detection?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Neptune", "Neptune is the managed graph database."),
        ("Amazon DynamoDB", "DynamoDB is a key-value and document database."),
        ("Amazon Aurora", "Aurora is a relational database."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Neptune is the managed graph database for highly connected data. Reference: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which service provides a fully managed time-series database for IoT and operational applications?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Timestream", "Timestream is the managed time-series database."),
        ("Amazon Neptune", "Neptune is graph."),
        ("Amazon DynamoDB", "DynamoDB is key-value."),
        ("Amazon Aurora", "Aurora is relational."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Timestream is the managed time-series database optimized for IoT and operational telemetry. Reference: https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a fully managed, in-memory, Redis-compatible database with multi-AZ durability?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ElastiCache for Redis", "ElastiCache for Redis is in-memory but not durable across AZs by default."),
        ("Amazon MemoryDB for Redis", "MemoryDB for Redis is in-memory with multi-AZ durability."),
        ("Amazon DynamoDB", "DynamoDB is on-disk NoSQL."),
        ("Amazon Aurora", "Aurora is relational."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon MemoryDB for Redis is a Redis-compatible, durable, in-memory database with multi-AZ replication. Reference: https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb-for-redis.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for a serverless REST API with sub-100ms latency? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon API Gateway", "API Gateway is the managed REST API service."),
        ("AWS Lambda", "Lambda is the compute layer."),
        ("Amazon DynamoDB with DAX", "DynamoDB with DAX for fast reads."),
        ("Amazon EC2 with Auto Scaling", "EC2 with ASG is not serverless and adds cold-start variability."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "API Gateway + Lambda + DynamoDB with DAX is a high-performance serverless REST pattern. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "Which Aurora feature replicates data across AWS Regions with sub-second replication lag for global low-latency reads?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora read replicas", "Read replicas are within a region."),
        ("Aurora Global Database", "Aurora Global Database replicates across regions with sub-second lag."),
        ("Aurora Backtrack", "Backtrack is in-place time-travel within a cluster."),
        ("Aurora Multi-Master", "Multi-Master is multi-writer within a region."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Aurora Global Database replicates to up to 5 secondary regions with sub-second lag. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a GLOBAL content delivery network (CDN) that caches content at edge locations for low-latency delivery?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is the AWS global CDN."),
        ("Amazon S3", "S3 is object storage, not a CDN."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
        ("AWS Global Accelerator", "Global Accelerator is for anycast TCP/UDP, not HTTP caching."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon CloudFront is the AWS global CDN with edge caching for low-latency content delivery. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "Which CloudFront feature reduces latency for end users by maintaining persistent connections to origins?",
    "type": "multiple-choice",
    "opts": [
        ("Origin Shield", "Origin Shield adds an extra caching layer to reduce origin load."),
        ("Keep-alive connections", "CloudFront maintains keep-alive connections to origins."),
        ("Lambda@Edge", "Lambda@Edge runs code at the edge."),
        ("Field-level encryption", "Field-level encryption is for security, not latency."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "CloudFront maintains persistent keep-alive connections to origins, reducing latency for repeated requests. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "Which CloudFront feature adds an additional caching layer between CloudFront edge locations and the origin, reducing origin load?",
    "type": "multiple-choice",
    "opts": [
        ("Origin Shield", "Origin Shield is the additional caching layer."),
        ("Origin Access Identity", "OAI/OAC restrict S3 origin access."),
        ("Lambda@Edge", "Lambda@Edge is for code at the edge."),
        ("CloudFront Functions", "CloudFront Functions run lightweight JavaScript at the edge."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "CloudFront Origin Shield adds an extra caching layer to reduce origin load and improve cache hit ratio. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html",
})
QUESTIONS.append({
    "q": "Which combination of features can a CloudFront distribution use to authenticate the request and pass a custom header to the origin? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudFront signed URLs", "Signed URLs grant time-limited access to specific objects."),
        ("CloudFront signed cookies", "Signed cookies grant access to multiple restricted objects."),
        ("Origin Access Control (OAC) for S3 origins", "OAC restricts S3 origin access to CloudFront."),
        ("Public S3 bucket without OAC", "Public S3 bypasses the secure pattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use signed URLs, signed cookies, and OAC to authenticate requests and protect origins. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content.html",
})
QUESTIONS.append({
    "q": "Which service provides anycast static IPs and improves global application performance for non-HTTP traffic (TCP/UDP)?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is HTTP/HTTPS."),
        ("AWS Global Accelerator", "Global Accelerator is for TCP/UDP with anycast IPs."),
        ("Amazon Route 53", "Route 53 is DNS."),
        ("AWS Direct Connect", "DX is a private link."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "AWS Global Accelerator provides anycast static IPs for TCP/UDP performance across regions. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which SINGLE AWS service is the BEST choice for a private, dedicated connection between on-prem and AWS?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Direct Connect (DX)", "Direct Connect is a private, dedicated fiber link with predictable pricing."),
        ("AWS Site-to-Site VPN over the internet", "VPN is an IPsec tunnel over the public internet, not a dedicated link. Valid option but not the BEST single answer in this scenario."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs and on-prem networks, but is a hub, not a connection. Valid option but not the BEST single answer in this scenario."),
        ("Amazon Cognito", "Cognito is for identity, not networking."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Direct Connect, Site-to-Site VPN, and Transit Gateway are the main on-prem-to-AWS networking options. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for a fully managed service mesh for microservices running on ECS, EKS, or EC2?",
    "type": "multiple-choice",
    "opts": [
        ("AWS App Mesh", "App Mesh is the managed service mesh."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS App Mesh is the managed service mesh for microservices, with Envoy-based sidecars. Reference: https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html",
})
QUESTIONS.append({
    "q": "Which service provides a fully managed data warehouse for OLAP, with columnar storage and massively parallel query execution?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Redshift", "Redshift is the managed data warehouse for OLAP."),
        ("Amazon Aurora", "Aurora is a relational OLTP database."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL OLTP database."),
        ("Amazon Neptune", "Neptune is a graph database."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Redshift is the fully managed data warehouse for OLAP workloads, using columnar storage and MPP. Reference: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html",
})
QUESTIONS.append({
    "q": "Which service provides serverless interactive query of data in S3 using standard SQL, with no infrastructure to manage?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Athena", "Athena queries S3 data using standard SQL with no infrastructure."),
        ("Amazon Redshift", "Redshift is a data warehouse cluster."),
        ("Amazon EMR", "EMR is a managed Hadoop/Spark platform."),
        ("Amazon Kinesis Data Analytics", "KDA is for streaming SQL."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Athena is the serverless interactive query service for S3 data, using standard SQL. Reference: https://docs.aws.amazon.com/athena/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for building generative AI applications using foundation models from leading providers, with a single API?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Bedrock", "Amazon Bedrock provides foundation models from multiple providers via a single API."),
        ("Amazon SageMaker", "SageMaker is for building/training ML models."),
        ("Amazon Q", "Amazon Q is a generative AI assistant for work."),
        ("Amazon Comprehend", "Comprehend is for NLP insights, not generative AI."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Bedrock provides foundation models from Anthropic, Meta, Mistral, Stability AI, and Amazon via a single API for building generative AI applications. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html",
})
QUESTIONS.append({
    "q": "Which ElastiCache engine is the BEST choice when you need advanced data structures such as sorted sets, hashes, and pub/sub?",
    "type": "multiple-choice",
    "opts": [
        ("Memcached", "Memcached is a simple key-value cache."),
        ("Redis", "Redis supports advanced data structures, pub/sub, streams, and persistence."),
        ("Valkey", "Valkey is a Redis fork with similar features."),
        ("Both Redis and Valkey are good choices, but Memcached is not", "Memcached lacks advanced structures."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Redis (and the compatible Valkey) supports sorted sets, hashes, lists, streams, and pub/sub. Memcached is a simple key-value cache. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Components.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid uses of CloudFront cache behaviors? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Serve /api/* from a different origin than /*", "Cache behaviors per path pattern allow different origins and TTLs."),
        ("Forward specific query strings to the origin", "CloudFront can forward query strings to origin."),
        ("Use a different CloudFront function per path", "Cache behaviors can attach different functions."),
        ("Cache private content with signed URLs only", "Signed URLs are the right pattern for private content."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "CloudFront cache behaviors allow per-path origins, query string forwarding, function association, and signed URL access. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid CloudFront origin types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon S3 bucket", "S3 is a CloudFront origin."),
        ("Application Load Balancer or EC2", "ALB/EC2 are HTTP origins."),
        ("AWS Elemental MediaStore and MediaPackage", "MediaStore and MediaPackage are origins for video."),
        ("On-prem HTTP server", "On-prem HTTP server via custom origin is allowed."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "CloudFront supports S3, ALB, EC2, MediaStore/Package, and on-prem HTTP origins. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid performance optimization techniques for Lambda? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Provisioned concurrency to eliminate cold starts", "Provisioned concurrency keeps functions warm."),
        ("Right-size memory allocation to balance duration and cost", "More memory = more CPU and often shorter duration."),
        ("Use layers to share code and dependencies", "Layers reduce deployment package size and improve cold start."),
        ("Disable function logging to improve performance", "Logging is important and disabling is an antipattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use provisioned concurrency, right-size memory, and use layers. Disabling logging is an antipattern. Reference: https://docs.aws.amazon.com/lambda/latest/operatorguide/performance.html",
})
QUESTIONS.append({
    "q": "Which service is the AWS-native container orchestrator that is compatible with upstream Kubernetes?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS", "ECS is AWS-native, not Kubernetes."),
        ("Amazon EKS", "EKS is the managed Kubernetes service."),
        ("AWS Fargate", "Fargate is the serverless compute engine for containers."),
        ("Amazon EC2", "EC2 is the compute service."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon EKS is a managed Kubernetes service compatible with upstream Kubernetes. Reference: https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html",
})
QUESTIONS.append({
    "q": "Which service is the AWS-native container orchestrator with deep AWS integration?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS", "ECS is the AWS-native container orchestrator."),
        ("Amazon EKS", "EKS is Kubernetes."),
        ("AWS Fargate", "Fargate is the serverless engine for containers."),
        ("Amazon Lightsail", "Lightsail is a simplified compute service."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon ECS is the AWS-native container orchestrator with deep AWS integration. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which EC2 pricing model offers up to 72% discount for a 1- or 3-year COMMITMENT with a specific instance family?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand Instances", "On-Demand is full price with no commitment."),
        ("Reserved Instances (Standard)", "Standard RIs offer up to 72% discount for 1-3 year terms."),
        ("Spot Instances", "Spot is up to 90% but with interruption risk."),
        ("Savings Plans only", "Savings Plans offer up to 72% but with cross-family flexibility; the question is RI-specific."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Standard Reserved Instances offer up to 72% discount for 1- or 3-year terms with a specific instance family. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html",
})
QUESTIONS.append({
    "q": "Which EC2 pricing model offers up to 90% discount but can be interrupted with 2 minutes notice?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand is full price."),
        ("Reserved Instances", "RIs are committed with no interruption."),
        ("Spot Instances", "Spot offers up to 90% discount but with interruption risk."),
        ("Savings Plans", "Savings Plans do not interrupt."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Spot Instances offer up to 90% discount but can be interrupted by AWS with 2 minutes notice. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "Which EC2 pricing model offers up to 72% discount with FLEXIBILITY across instance families, regions, and OS?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand is full price."),
        ("Compute Savings Plans", "Compute Savings Plans offer up to 66% with full flexibility across families, regions, and OS."),
        ("Standard Reserved Instances", "Standard RIs require a specific instance family."),
        ("EC2 Instance Savings Plans", "EC2 Instance Savings Plans offer up to 72% within a single region and family."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Compute Savings Plans offer up to 66% discount with the most flexibility (any family, any region, any OS, any compute). EC2 Instance Savings Plans offer up to 72% within a region. Reference: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html",
})
QUESTIONS.append({
    "q": "Which SINGLE EC2 pricing model is the BEST fit for fault-tolerant, interruptible workloads?",
    "type": "multiple-choice",
    "opts": [
        ("Spot Instances", "Spot offers up to 90% discount for fault-tolerant workloads."),
        ("Spot Fleet with diversification", "Spot Fleet launches a mix of instance types to reduce interruption. Valid option but not the BEST single answer in this scenario."),
        ("On-Demand Instances for the same workload", "On-Demand is more expensive; not optimal for fault-tolerant batch."),
        ("Reserved Instances for the same workload", "RIs are not for fault-tolerant, short-lived batch."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Spot and Spot Fleet are the BEST choices for fault-tolerant, batch workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html",
})
QUESTIONS.append({
    "q": "Which Reserved Instance type can be MODIFIED (instance family, OS, scope) to adapt to changing needs?",
    "type": "multiple-choice",
    "opts": [
        ("Standard RI", "Standard RIs cannot be modified (except for AZ)."),
        ("Convertible RI", "Convertible RIs can be modified for flexibility."),
        ("Scheduled RI", "Scheduled RIs are time-bound."),
        ("Dedicated RI", "Dedicated RIs are for Dedicated Hosts."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Convertible RIs can be modified to a different instance family, OS, or scope during the term. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/convertible-reserved-instances.html",
})
QUESTIONS.append({
    "q": "Which AWS tool analyzes your past On-Demand usage and recommends Reserved Instance or Savings Plan commitments to reduce cost?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer RI and Savings Plan recommendations", "Cost Explorer recommendations suggest RI/SP purchases."),
        ("AWS Trusted Advisor", "Trusted Advisor also shows RI recommendations, but Cost Explorer is more detailed."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates future cost."),
        ("AWS Budgets", "Budgets alert on spend."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Explorer provides detailed RI and Savings Plan purchase recommendations based on your past usage. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-ri-recommendations.html",
})
QUESTIONS.append({
    "q": "Which EC2 capacity option reserves capacity in a specific AZ for a defined duration, ensuring availability for disaster recovery scenarios?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand Capacity Reservations", "On-Demand Capacity Reservations reserve capacity in a specific AZ for any duration."),
        ("Reserved Instances", "RIs are billing discounts, not capacity reservations per se."),
        ("Spot Instances", "Spot does not reserve capacity."),
        ("Savings Plans", "Savings Plans are billing discounts."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "On-Demand Capacity Reservations reserve EC2 capacity in a specific AZ for any duration, ensuring availability. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html",
})
QUESTIONS.append({
    "q": "Which combination of pricing models BEST optimizes cost for a workload that runs steady state for 8 hours/day and a spiky batch that runs overnight? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Savings Plans for the steady 8-hour workload", "Savings Plans cover steady state at a discount."),
        ("Spot for the overnight batch", "Spot is ideal for fault-tolerant overnight batch."),
        ("On-Demand for both", "On-Demand for steady state is more expensive than Savings Plans."),
        ("Reserved Instances without Savings Plans", "Savings Plans are more flexible than RIs."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "Mix Savings Plans for steady state with Spot for the overnight batch. Reference: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost-optimization-pillar.html",
})
QUESTIONS.append({
    "q": "Which SINGLE cost benefit BEST describes Compute Savings Plans?",
    "type": "multiple-choice",
    "opts": [
        ("Up to 66% discount on Compute Savings Plans across families", "Compute SPs offer up to 66% with the most flexibility across families."),
        ("Up to 72% discount on EC2 Instance Savings Plans within a family", "EC2 Instance SPs offer up to 72% within a family; this is a different SP type. Valid option but not the BEST single answer in this scenario."),
        ("Apply automatically to eligible usage", "SPs apply automatically; this is a feature, not the headline benefit. Valid option but not the BEST single answer in this scenario."),
        ("Reduce cost for AWS Lambda and Fargate invocations under Compute SPs", "Compute SPs also cover Lambda and Fargate, but the discount level is the core benefit. Valid option but not the BEST single answer in this scenario."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Savings Plans offer up to 66%/72% discounts, apply automatically, and Compute SPs cover Lambda and Fargate. Reference: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html",
})
QUESTIONS.append({
    "q": "Which EC2 purchase option offers the LOWEST hourly price but with interruption risk?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand is the standard price with no discount."),
        ("Reserved Instances", "RIs are discounted with commitment."),
        ("Spot", "Spot is the lowest price but interruptible."),
        ("Dedicated Hosts", "Dedicated Hosts are most expensive per hour."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Spot offers the lowest price, up to 90% off On-Demand. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the MOST cost-effective for data archived for 7-10 years with hours retrieval?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible Retrieval has lower cost and minutes-hours retrieval."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest cost, hours retrieval, for 7-10+ year archives."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering is for unknown access patterns."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 Glacier Deep Archive is the lowest-cost storage class, with 12-48 hour retrieval. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 feature automatically moves objects to a CHEAPER storage class when they have not been accessed for a defined period?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle", "S3 Lifecycle rules transition objects to cheaper classes or expire them."),
        ("S3 Replication", "Replication copies objects to another bucket."),
        ("S3 Versioning", "Versioning keeps multiple object versions."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Lifecycle rules automatically transition objects to other storage classes or expire them. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class automatically moves objects between access tiers based on usage patterns, with no retrieval charges, ideal for unknown access patterns?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects to cheaper tiers."),
        ("S3 Standard-IA", "Standard-IA has retrieval charges."),
        ("S3 Glacier", "Glacier has retrieval charges."),
        ("S3 One Zone-IA", "One Zone-IA has retrieval charges and is for single-AZ."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Intelligent-Tiering automatically moves objects between Frequent, Infrequent, Archive, and Deep Archive tiers. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which combination of services reduces data transfer OUT cost from S3? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront with S3 origin", "CloudFront reduces data transfer out from origin to edge locations."),
        ("S3 Transfer Acceleration", "Transfer Acceleration uses CloudFront edges but is for uploads."),
        ("S3 VPC gateway endpoint for in-VPC access", "VPC endpoints avoid NAT data transfer charges for in-VPC access."),
        ("Reading directly from S3 over the public internet", "Direct reads over the internet are not optimized for cost."),
    ],
    "correct": "1,3",
    "domain": COST_OPT,
    "overall": "CloudFront and S3 VPC endpoints help reduce data transfer costs. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html",
})
QUESTIONS.append({
    "q": "Which of the following are free or low-cost S3 request patterns? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Uploads to S3 from EC2 in the same region", "S3 data uploads to S3 from EC2 in the same region are free."),
        ("Transitions between S3 storage classes", "Lifecycle transitions between storage classes are free."),
        ("DELETE requests on S3", "DELETE requests are free."),
        ("GET requests from CloudFront to S3", "CloudFront-to-S3 origin fetches are billed at S3 rates, but CloudFront can cache to reduce them."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "S3 uploads, lifecycle transitions, and deletes are free. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/aws-usage-report-understand.html",
})
QUESTIONS.append({
    "q": "Which VPC feature avoids NAT gateway and internet gateway data transfer charges for accessing S3 from a private subnet?",
    "type": "multiple-choice",
    "opts": [
        ("S3 VPC gateway endpoint", "Gateway endpoints keep S3 traffic inside the AWS network, avoiding NAT data transfer charges."),
        ("Internet gateway", "An internet gateway is for public access."),
        ("NAT gateway", "NAT gateway is what you want to avoid for S3."),
        ("VPN connection", "VPN is for on-prem access."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 gateway endpoints route traffic to S3 inside the AWS network, avoiding NAT data transfer charges. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid data transfer cost optimization strategies? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use CloudFront to cache content at edge locations", "CloudFront reduces origin data transfer."),
        ("Use VPC endpoints for S3 and DynamoDB", "VPC endpoints avoid NAT data transfer charges."),
        ("Co-locate compute and data in the same AZ where possible", "Same-AZ data transfer is free."),
        ("Use Direct Connect instead of VPN for high-volume data", "DX has predictable data transfer pricing for high volumes."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "CloudFront, VPC endpoints, AZ co-location, and Direct Connect are all data transfer cost optimization strategies. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST choice for data accessed less than once a quarter with millisecond retrieval requirements?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Standard-IA", "Standard-IA is for infrequent millisecond access at lower cost."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive has hours retrieval."),
        ("S3 One Zone-IA", "One Zone-IA is for data that can be lost in an AZ destruction."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Standard-IA is the BEST choice for infrequent millisecond access. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST cost-optimized pattern for serving a global, read-heavy static website? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon S3 for storage", "S3 is the cheapest static asset storage."),
        ("Amazon CloudFront for caching", "CloudFront reduces origin load and data transfer."),
        ("Amazon EC2 with Auto Scaling", "EC2 is over-engineered for static assets."),
        ("Amazon S3 Glacier for static assets", "Glacier has slow retrieval; wrong for static assets."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "S3 + CloudFront is the cost-optimized static website pattern. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 storage classes for archive workloads? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval is for archive with millisecond retrieval."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible Retrieval is for archive with minutes-hours retrieval."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest-cost class with hours retrieval."),
        ("S3 Standard", "Standard is not an archive class."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Glacier Instant Retrieval, Flexible Retrieval, and Deep Archive are the archive classes. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which AWS tool analyzes your EC2 utilization and recommends rightsizing to a smaller instance type to reduce cost?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Compute Optimizer", "Compute Optimizer uses ML to recommend right-sized instances."),
        ("AWS Cost Explorer", "Cost Explorer is for spend analysis and RI recommendations."),
        ("AWS Trusted Advisor", "Trusted Advisor also flags underutilized instances."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates future cost."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer uses ML to recommend right-sized EC2 instances, EBS volumes, Lambda functions, and ECS services. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid cost optimization techniques for EC2? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size instances based on Compute Optimizer recommendations", "Right-sizing reduces overprovisioning."),
        ("Use Spot Instances for fault-tolerant workloads", "Spot offers up to 90% discount."),
        ("Use Savings Plans for steady-state workloads", "Savings Plans discount predictable usage."),
        ("Run all workloads 24/7", "Running 24/7 wastes spend; turn off idle workloads."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Right-size, use Spot, and use Savings Plans; don't run idle workloads 24/7. Reference: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost-optimization-pillar.html",
})
QUESTIONS.append({
    "q": "Which combination of managed services is the MOST cost-effective for a serverless web application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Lambda for compute", "Lambda bills per request and GB-second."),
        ("Amazon DynamoDB on-demand for unpredictable workloads", "DynamoDB on-demand scales with usage."),
        ("Amazon S3 for static content", "S3 is cheap and scales with usage."),
        ("Reserved EC2 instances for the same workload", "Reserved EC2 is not cost-effective for serverless apps."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Lambda, DynamoDB on-demand, and S3 are cost-effective for serverless apps. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "Which service provides visualizations of your AWS spend over time, broken down by service, linked account, and tag?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer visualizes spend and forecasts."),
        ("AWS Budgets", "Budgets alert on spend thresholds."),
        ("AWS Cost and Usage Report", "CUR is a detailed line-item report."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Explorer provides cost visualization, forecasting, and filtering by service, account, tag, and region. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-ce.html",
})
QUESTIONS.append({
    "q": "Which of the following are features of AWS Cost Explorer? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Visualize spend by service, account, region, tag", "Cost Explorer supports many grouping dimensions."),
        ("Forecast future spend", "Cost Explorer forecasts based on past usage."),
        ("Recommend Reserved Instance and Savings Plan purchases", "CE provides RI and SP recommendations."),
        ("Apply IAM policies to control access", "IAM policies control access to Cost Explorer."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Cost Explorer visualizes, forecasts, and recommends. IAM is separate. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service lets you set custom cost and usage budgets with alerts when thresholds are exceeded?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Budgets", "AWS Budgets lets you set spend and usage budgets with alerts."),
        ("AWS Cost Explorer", "Cost Explorer visualizes and forecasts."),
        ("AWS Trusted Advisor", "Trusted Advisor flags best-practice issues."),
        ("AWS Config", "Config tracks configuration."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Budgets provides custom cost, usage, reservation, and Savings Plans budgets with alerts. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
})
QUESTIONS.append({
    "q": "Which AWS service uses ML to detect anomalous spend and notify you of unusual cost spikes?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Anomaly Detection", "Cost Anomaly Detection uses ML to detect spend anomalies."),
        ("AWS Budgets", "Budgets alert on thresholds, not anomalies."),
        ("AWS Cost Explorer", "Cost Explorer is for visualization and analysis."),
        ("AWS Trusted Advisor", "Trusted Advisor checks best practices."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Anomaly Detection uses ML to detect and alert on unusual spend patterns. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html",
})
QUESTIONS.append({
    "q": "Which AWS feature lets you assign AWS costs to specific resources, projects, or teams by tagging resources?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Allocation Tags", "Cost allocation tags let you categorize spend."),
        ("AWS Organizations", "Organizations provides consolidated billing."),
        ("AWS Trusted Advisor", "Trusted Advisor checks best practices."),
        ("AWS Config", "Config tracks configuration."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Cost allocation tags let you categorize resources for cost reporting. Activate tags in the Billing console. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Organizations provides a SINGLE bill for all member accounts, with potential volume discounts?",
    "type": "multiple-choice",
    "opts": [
        ("Consolidated billing", "Consolidated billing rolls up all member accounts into a single payer."),
        ("Service control policies (SCPs)", "SCPs are permission guardrails, not billing."),
        ("AWS Resource Access Manager", "RAM shares resources across accounts."),
        ("AWS Control Tower", "Control Tower is for multi-account governance."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Consolidated billing in AWS Organizations combines usage across accounts for volume pricing. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the MOST cost-effective for hosting a containerized microservice with unpredictable traffic? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Fargate Spot for compute", "Fargate Spot offers up to 70% discount for fault-tolerant containers."),
        ("AWS Fargate with Savings Plans", "Savings Plans also apply to Fargate."),
        ("Amazon EC2 with on-demand for the same workload", "EC2 on-demand is more expensive and not cost-effective for unpredictable traffic."),
        ("Amazon EKS managed node groups with on-demand", "Managed node groups on on-demand are not cost-effective for unpredictable traffic."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "Fargate Spot and Fargate with Savings Plans are cost-effective for unpredictable container traffic. Reference: https://docs.aws.amazon.com/fargate/latest/userguide/what-is-fargate.html",
})
QUESTIONS.append({
    "q": "Which combination of services reduces NAT gateway data transfer charges for S3 and DynamoDB access from private subnets? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 VPC gateway endpoint", "Gateway endpoint avoids NAT for S3."),
        ("DynamoDB VPC gateway endpoint", "Gateway endpoint avoids NAT for DynamoDB."),
        ("NAT gateway with no endpoints", "NAT gateway incurs data transfer charges."),
        ("Internet gateway for S3 access", "Internet gateway is not for in-VPC S3 access."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "S3 and DynamoDB gateway endpoints avoid NAT gateway data transfer charges. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a PRIVATE connection between on-prem and AWS that can be more cost-effective than high-volume VPN for predictable data transfer?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Direct Connect", "Direct Connect is a dedicated private fiber link with predictable pricing."),
        ("AWS Site-to-Site VPN", "VPN is over the public internet; per-hour charges apply."),
        ("AWS Transit Gateway", "Transit Gateway is a hub for VPCs and on-prem networks."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Direct Connect provides a private, dedicated connection with predictable pricing for high-volume data. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid cost optimization techniques for Amazon EBS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size EBS volumes to actual usage", "Right-sizing reduces wasted GB-months."),
        ("Use gp3 instead of gp2 for better price-performance", "gp3 is generally cheaper for the same baseline performance."),
        ("Delete unused EBS volumes and snapshots", "Unattached volumes and old snapshots still incur cost."),
        ("Always use io2 Block Express", "io2 is the most expensive SSD; not always the right choice."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Right-size, use gp3, and delete unused volumes. io2 is not always the right choice. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/optimizing-cost.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST cost-optimized pattern for serving a static website with low global traffic? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon S3 for storage", "S3 static website hosting is very cheap."),
        ("Amazon CloudFront for caching", "CloudFront is pay-as-you-go with free tier."),
        ("Reserved EC2 instances for the same workload", "EC2 is more expensive for static sites."),
        ("Amazon S3 Glacier for storage", "Glacier has slow retrieval; wrong for static sites."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "S3 + CloudFront is the cost-optimized static website pattern. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html",
})
QUESTIONS.append({
    "q": "Which combination of services reduces cost for an EC2 workload that runs only on weekdays from 9 AM to 6 PM? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use Auto Scaling with scheduled scaling to scale down off-hours", "Scheduled scaling reduces capacity and cost off-hours."),
        ("Use Spot Instances for additional cost savings", "Spot reduces per-hour cost."),
        ("Use Savings Plans if usage is steady", "SPs apply automatically to baseline usage."),
        ("Leave the instances running 24/7", "Leaving instances running 24/7 wastes cost."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use scheduled scaling, Spot, and Savings Plans to optimize cost for time-bound workloads. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated recommendations to reduce cost, improve security, and increase reliability, in your AWS account?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Trusted Advisor", "Trusted Advisor checks cost optimization, security, fault tolerance, performance limits, and service quotas."),
        ("AWS Cost Explorer", "Cost Explorer is for spend analysis."),
        ("AWS Budgets", "Budgets alert on spend thresholds."),
        ("AWS Config", "Config is for configuration compliance."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Trusted Advisor provides automated checks for cost optimization, security, fault tolerance, performance, and service quotas. Reference: https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST cost-optimized pattern for an event-driven, serverless, bursty workload? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Lambda with on-demand concurrency", "Lambda on-demand scales and bills per invocation."),
        ("Amazon SQS for buffering", "SQS Standard buffers traffic and avoids throttling."),
        ("Amazon DynamoDB on-demand", "DynamoDB on-demand scales with usage."),
        ("Reserved EC2 instances for the same workload", "Reserved EC2 is not cost-effective for bursty serverless workloads."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Lambda + SQS + DynamoDB on-demand is the cost-optimized serverless pattern. Reference: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid strategies for optimizing AWS Lambda cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size memory allocation to balance duration and cost", "Memory affects both performance and cost."),
        ("Use Provisioned Concurrency only for the function", "Provisioned concurrency is for predictable performance, not cost optimization."),
        ("Use Lambda SnapStart to reduce cold start duration", "SnapStart reduces cold start time and thus cost."),
        ("Use Compute Savings Plans to cover baseline usage", "Compute SPs apply to Lambda usage."),
    ],
    "correct": "1,3,4",
    "domain": COST_OPT,
    "overall": "Right-size memory, use SnapStart, and use Compute Savings Plans to optimize Lambda cost. Reference: https://docs.aws.amazon.com/lambda/latest/operatorguide/performance.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a detailed line-item report of your AWS usage and cost, suitable for advanced analytics?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost and Usage Report (CUR)", "CUR is the most detailed cost and usage report."),
        ("AWS Cost Explorer", "Cost Explorer is the high-level visualization."),
        ("AWS Budgets", "Budgets alert on spend."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost and Usage Report (CUR) is the most detailed line-item report, deliverable to S3 for analysis in Athena or QuickSight. Reference: https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to migrate from a single-region monolith to a multi-region active-active architecture for its e-commerce platform. Which database strategy provides MULTI-REGION, MULTI-MASTER replication for the product catalog?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ with read replicas", "Multi-AZ + read replicas are within a single region."),
        ("DynamoDB Global Tables", "DynamoDB Global Tables provide multi-region, multi-master replication."),
        ("Aurora Global Database with secondary writer", "Aurora Global has a single primary writer."),
        ("Single-AZ RDS", "Single-AZ is not HA, not multi-region."),
    ],
    "correct": "2",
    "domain": SECURE,
    "overall": "DynamoDB Global Tables provide multi-region, multi-master replication, ideal for active-active product catalogs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to replicate static assets (product images) to a second region for DR with the LEAST operational overhead. Which S3 feature is the BEST choice?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication (CRR)", "CRR asynchronously replicates objects to another region."),
        ("S3 Batch Operations", "Batch is for one-time operations on existing objects."),
        ("S3 Object Lock", "Object Lock is for immutability."),
        ("S3 Inventory", "Inventory is a listing report."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 CRR automatically replicates new and updated objects to a destination bucket in a different region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to protect the public e-commerce site from SQL injection, XSS, and bot attacks. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS WAF with managed rule groups for SQLi and XSS", "WAF is the layer 7 web ACL for SQLi and XSS."),
        ("Amazon CloudFront in front of the application", "CloudFront provides edge caching and WAF integration."),
        ("AWS Shield Standard for L3/L4 DDoS protection", "Shield Standard is always-on at no charge."),
        ("Amazon S3 only", "S3 is storage, not for web app protection."),
    ],
    "correct": "1,2,3",
    "domain": SECURE,
    "overall": "WAF + CloudFront + Shield Standard is the standard public web app protection stack. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants the LOWEST-COST DDoS protection with always-on detection for its public e-commerce site. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Shield Standard", "Shield Standard is free, always-on L3/L4 protection."),
        ("AWS Shield Advanced", "Shield Advanced is paid and adds DRT, cost protection."),
        ("AWS WAF alone", "WAF is for L7, not L3/L4 DDoS."),
        ("Amazon GuardDuty", "GuardDuty is threat detection, not DDoS protection."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Shield Standard is the free, always-on baseline DDoS protection for all AWS customers. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to encrypt all S3 objects (product images, user uploads) with a customer managed KMS key, with no application changes. Which S3 feature should RetailCo enable?",
    "type": "multiple-choice",
    "opts": [
        ("S3 default bucket encryption with SSE-KMS and a CMK", "Default encryption with SSE-KMS and a CMK encrypts all new objects automatically."),
        ("Manual client-side encryption in the application", "Manual client-side requires app changes."),
        ("S3 Object Lock", "Object Lock is for immutability, not encryption."),
        ("S3 Block Public Access only", "Block Public Access is for access control, not encryption."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "Default bucket encryption with SSE-KMS and a customer managed CMK encrypts all new objects automatically. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to direct users to the lowest-latency region for its product catalog API. Which Route 53 routing policy is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Latency-based routing", "Latency routing directs users to the lowest-latency region."),
        ("Weighted routing", "Weighted is for fixed ratios, not latency."),
        ("Failover routing", "Failover is active-passive."),
        ("Simple routing", "Simple is for single records."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 latency-based routing directs users to the region with the lowest measured network latency. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to reduce S3 storage cost for product images that are accessed frequently for 30 days and then rarely thereafter. Which combination is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Lifecycle rule to transition to Standard-IA after 30 days", "Lifecycle transition reduces cost after 30 days."),
        ("S3 Lifecycle rule to transition to Glacier after 90 days", "Further transition to Glacier reduces cost more."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering moves objects automatically based on access."),
        ("Keep all objects in S3 Standard forever", "Standard is the most expensive tier."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use S3 Lifecycle or Intelligent-Tiering to move objects to cheaper tiers after the hot period. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to ensure its web application can handle Black Friday traffic spikes. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon EC2 Auto Scaling with target tracking", "ASG target tracking scales on a metric like CPU."),
        ("Amazon CloudFront in front of the application", "CloudFront caches and absorbs spikes."),
        ("Amazon ElastiCache to offload database reads", "ElastiCache reduces RDS load on spikes."),
        ("Single EC2 instance with a fixed size", "Single instance is not scalable."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Auto Scaling, CloudFront, and ElastiCache together handle traffic spikes. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to track user behavior in real time, generate personalized recommendations, and store them in a low-latency key-value store. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis ingests real-time clickstream events."),
        ("AWS Lambda for real-time processing", "Lambda processes events in real time."),
        ("Amazon DynamoDB for low-latency reads", "DynamoDB is the low-latency key-value store."),
        ("Amazon S3 Glacier for real-time recommendations", "Glacier is not low-latency; wrong choice."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Kinesis + Lambda + DynamoDB is the standard real-time clickstream pattern. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "In the RetailCo scenario, RetailCo wants to manage its multi-account AWS environment with centralized security guardrails and consolidated billing. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Organizations", "Organizations provides consolidated billing and SCPs."),
        ("AWS Config only", "Config tracks configuration."),
        ("AWS Trusted Advisor", "Trusted Advisor checks best practices."),
        ("Amazon Cognito", "Cognito is for identity, not account management."),
    ],
    "correct": "1",
    "domain": SECURE,
    "overall": "AWS Organizations provides multi-account management with consolidated billing and SCPs. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html",
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
    assert counts[SECURE] == 60, f"Secure={counts[SECURE]}"
    assert counts[RESILIENT] == 52, f"Resilient={counts[RESILIENT]}"
    assert counts[HIGH_PERF] == 48, f"HighPerforming={counts[HIGH_PERF]}"
    assert counts[COST_OPT] == 40, f"CostOpt={counts[COST_OPT]}"
    assert multi == 38, f"Multi-select={multi}"

    out = "/home/user/Cert/course/AWS-SAA-C03-03-practice-sets/set-1/practice-set-1.csv"
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
