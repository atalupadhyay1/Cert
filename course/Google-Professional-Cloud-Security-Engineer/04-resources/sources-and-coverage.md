# Official sources and coverage notes

Reviewed October 2026 against the exam guide and the certification page. Product names, preview status, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| Certification page (length, fee, format, languages, prerequisites) | https://cloud.google.com/learn/certification/cloud-security-engineer |
| Exam guide (five sections and their weights) | https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf |
| IAM overview | https://cloud.google.com/iam/docs/overview |
| Service accounts and keys | https://cloud.google.com/iam/docs/service-account-overview |
| Workload Identity Federation | https://cloud.google.com/iam/docs/workload-identity-federation |
| Workforce Identity Federation | https://cloud.google.com/iam/docs/workforce-identity-federation |
| Privileged Access Manager | https://cloud.google.com/iam/docs/pam-overview |
| Cloud NGFW policies | https://cloud.google.com/firewall/docs |
| Cloud Armor | https://cloud.google.com/armor/docs |
| Identity-Aware Proxy | https://cloud.google.com/iap/docs |
| Certificate Authority Service | https://cloud.google.com/certificate-authority-service/docs |
| VPC Service Controls | https://cloud.google.com/vpc-service-controls/docs |
| Cloud VPN | https://cloud.google.com/network-connectivity/docs/vpn |
| Cloud Interconnect | https://cloud.google.com/network-connectivity/docs/interconnect |
| Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| Sensitive Data Protection | https://cloud.google.com/sensitive-data-protection/docs |
| Cloud KMS | https://cloud.google.com/kms/docs |
| Cloud EKM | https://cloud.google.com/kms/docs/ekm |
| Confidential Computing | https://cloud.google.com/confidential-computing/docs |
| Binary Authorization | https://cloud.google.com/binary-authorization/docs |
| Security Command Center | https://cloud.google.com/security-command-center/docs |
| Audit Logs | https://cloud.google.com/logging/docs/audit |
| Assured Workloads | https://cloud.google.com/assured-workloads/docs |
| Access Transparency | https://cloud.google.com/assured-workloads/docs/access-transparency-overview |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Configuring access ~25%; 2) Securing communications and establishing boundary protection ~22%; 3) Ensuring data protection ~23%; 4) Managing operations ~19%; 5) Supporting compliance requirements ~11% |
| Length | 2 hours |
| Fee | $200 USD plus applicable tax |
| Format | 50–60 multiple choice and multiple select questions |
| Case studies | **None.** The certification page and the guide describe no case-study component and no case-study weighting |
| Passing score | **Not published** — the exam reports pass or fail |
| Languages | English and Japanese |
| Prerequisites | **None**; 3+ years of industry experience including 1+ year designing and managing solutions on Google Cloud is recommended |
| Delivery | Online proctored or at a test centre |
| Role scope notice | The certification page describes a role that also covers security automation, securing AI workloads, securing the software supply chain, and enforcing regulatory controls |

The length, fee, question range, languages, and prerequisites above are Google-published; the **passing score is not published**, and this package therefore never states a target percentage or converts a practice score into a pass mark.

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce lab tasks or any interactive console component, that they reproduce case studies (there are none to reproduce), or that completing the course earns the certification.

## Domain coverage and package weights

| Domain | Official weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Configuring access | ~25% | 25 | 25% | 150 |
| 2. Securing communications and boundary protection | ~22% | 22 | 22% | 132 |
| 3. Ensuring data protection | ~23% | 23 | 23% | 138 |
| 4. Managing operations | ~19% | 19 | 19% | 114 |
| 5. Supporting compliance requirements | ~11% | 11 | 11% | 66 |

The five published weights total **exactly 100%**, so they can be copied straight into a 100-item exam and they are: **25 / 22 / 23 / 19 / 11**. No count was adjusted, unlike the Professional-level courses in this repository whose weights summed to 101% and required a one-item correction. `build.py` asserts equality rather than a tolerance band, so a future guide revision that breaks the 100% total will fail the build instead of being absorbed.

## Coverage against the published sections

The guide's bullets were read directly and mapped into 48 local study areas. The table records practice emphasis across all 600 items; counts describe this bank, not official weighting.

| Local ID | Study area | Items | Official bullets it supports |
|---|---|---:|---|
| 1.1 | Cloud Identity, SSO, and Directory Sync | 18 | 1.1 Cloud Identity, single sign-on, and Google Cloud Directory Sync |
| 1.2 | Super Administrator and Lifecycle Automation | 12 | 1.1 super administrator handling and automated user lifecycle |
| 1.3 | Workforce Identity Federation | 12 | 1.1 Workforce Identity Federation for an external workforce |
| 1.4 | Service Account Hygiene and Default Accounts | 18 | 1.2 protecting default service accounts and identifying when one is needed |
| 1.5 | Service Account Keys and Short-Lived Credentials | 18 | 1.2 securing, auditing, and replacing service account keys |
| 1.6 | Workload Identity Federation | 12 | 1.2 Workload Identity Federation for external workloads |
| 1.7 | Service Account Impersonation | 12 | 1.2 service account impersonation and short-lived credentials |
| 1.8 | Password, Session, and 2-Step Verification Policy | 12 | 1.3 password and session policy, SAML and OAuth, enforced 2-step verification |
| 1.9 | Privileged Roles, Separation of Duties, and PAM | 12 | 1.4 privileged roles, separation of duties, and Privileged Access Manager |
| 1.10 | IAM Conditions, Deny Policies, and Access Context Manager | 12 | 1.4 IAM conditions, deny policies, Access Context Manager, and Policy Intelligence |
| 1.11 | Resource Hierarchy and Organization Policies | 12 | 1.5 folders and projects at scale, prebuilt and custom organization policies, inheritance |
| 2.1 | Firewall Rules and Hierarchical Policies | 12 | 2.1 Cloud NGFW rules and hierarchical policies |
| 2.2 | Layer 7 Inspection | 12 | 2.1 application layer inspection on Cloud NGFW |
| 2.3 | Cloud Armor Web Application Firewall | 12 | 2.1 Google Cloud Armor web application firewall and bot management |
| 2.4 | Identity-Aware Proxy | 12 | 2.1 Identity-Aware Proxy for per-request authorisation |
| 2.5 | TLS, Load Balancing, and Certificate Authority Service | 12 | 2.1 load balancer TLS and Certificate Authority Service |
| 2.6 | Secure Web Proxy and Cloud DNS Security | 12 | 2.1 Secure Web Proxy and Cloud DNS security settings |
| 2.7 | Private Addressing and API Restriction | 12 | 2.1 private and public IP addressing, and restricting configured APIs |
| 2.8 | VPC Firewalls, Peering, and Shared VPC | 12 | 2.2 VPC security properties, peering, Shared VPC, and firewall rules |
| 2.9 | VPC Service Controls | 12 | 2.2 VPC Service Controls perimeters and restricted access |
| 2.10 | HA VPN and Cloud Interconnect | 12 | 2.3 HA VPN and Cloud Interconnect to a data centre |
| 2.11 | Private Google Access and Private Service Connect | 6 | 2.3 Private Google Access and Private Service Connect for Google APIs |
| 2.12 | Cloud NAT Egress | 6 | 2.3 Cloud NAT for outbound traffic |
| 3.1 | Sensitive Data Protection Discovery | 18 | 3.1 Sensitive Data Protection discovery and inspection |
| 3.2 | De-identification Templates | 18 | 3.1 redaction, pseudonymisation, and format-preserving encryption |
| 3.3 | Access Control for BigQuery, Cloud Storage, and Cloud SQL | 18 | 3.1 restricting access to BigQuery, Cloud Storage, and Cloud SQL data |
| 3.4 | Secret Manager | 12 | 3.1 securing secrets with Secret Manager |
| 3.5 | Instance Metadata Protection | 12 | 3.1 protecting and managing compute instance metadata |
| 3.6 | Default Encryption and CMEK | 18 | 3.2 default encryption and CMEK use cases |
| 3.7 | Cloud EKM and Key Import | 12 | 3.2 Cloud External Key Manager and key import |
| 3.8 | Key Rotation and Revocation | 12 | 3.2 key rotation and revocation |
| 3.9 | Confidential Computing | 12 | 3.2 Confidential Computing for data in use |
| 3.10 | Storage Lifecycle and Retention | 6 | 3.2 object lifecycle policies for Cloud Storage |
| 4.1 | CVE Scanning in CI/CD | 12 | 4.1 automating CVE scanning in the CI/CD pipeline |
| 4.2 | Binary Authorization | 12 | 4.1 Binary Authorization for GKE and Cloud Run |
| 4.3 | Hardened Images and Patch Management | 12 | 4.1 hardened image creation and VM patch management |
| 4.4 | Posture Management and Drift Detection | 12 | 4.1 posture management, drift detection, and custom modules or constraints |
| 4.5 | Network Logs, Cloud IDS, and Packet Mirroring | 18 | 4.2 network logs, Packet Mirroring, Cloud IDS, and Log Analytics |
| 4.6 | Logging Strategy and Secure Log Access | 12 | 4.2 designing a logging strategy and secure access to logs |
| 4.7 | Audit Logs and Data Access Logs | 12 | 4.2 Audit Logs and data access logs |
| 4.8 | Log Sinks and SIEM Export | 12 | 4.2 log sinks, aggregated sinks, and export to external systems |
| 4.9 | Security Command Center Findings | 12 | 4.2 configuring and monitoring Security Command Center |
| 5.1 | Shared Responsibility Model | 12 | 5.1 evaluating the shared responsibility model |
| 5.2 | Assured Workloads | 12 | 5.1 Assured Workloads for a regulatory environment |
| 5.3 | Access Transparency and Access Approval | 12 | 5.1 Access Transparency and Access Approval |
| 5.4 | Regionalization of Data and Services | 12 | 5.1 regionalization of data and services |
| 5.5 | Mapping Requirements to Controls | 12 | 5.1 mapping compliance requirements to services and controls |
| 5.6 | Scoping the Compliance Boundary | 6 | 5.1 determining the environment in scope for compliance |

These IDs are internal study aids. Google names objectives without this numbering, and no claim is made that the bank is psychometrically calibrated against the live exam.

## Deliberate omissions and disclosures

| Excluded element | Why it is excluded | How the package compensates |
|---|---|---|
| Case studies | The published PCSE format has no case-study component | Nothing is imitated; the absence is stated in the README, landing page, curriculum, and package checks |
| Sequencing items | The published format is multiple choice and multiple select only | No sequencing stems, no `→` options, and `validate.py` rejects them |
| Lab and interactive console tasks | Require a live project | Configuration is presented as text and read, not typed |
| Live item count | The live exam samples 50–60 questions | Each exam is labelled a 100-item expanded bank |
| Passing score | Google does not publish one | No target percentage is stated anywhere |
| AI workload security depth | The guide names section 3.3 but describes it briefly | Items test the security control and the requirement, never product marketing |

## Licensing, capability, and pricing statements

Every item is answerable without a project. Where a scenario depends on a capability that requires a paid edition, a specific region, or an allowlisted feature, the explanation names that dependency rather than implying the capability is free or universal. No item asserts a current price, quota, or regional availability; the only price in the package is the published $200 registration fee, cited as published and subject to change.
