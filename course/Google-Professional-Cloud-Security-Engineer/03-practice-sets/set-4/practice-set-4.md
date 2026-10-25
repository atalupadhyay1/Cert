# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 4

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. An insurer treats its HR system as the record of truth and wants joiners to appear without a ticket. What should be scheduled?

- A. Restrict the project to the APIs it needs and review them on a schedule
- B. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- C. Create a service account key and embed it in the application configuration
- D. Assign the super administrator role to a dedicated break-glass account with hardware keys

### 2. Claims adjusters must sign in with the carrier portal credentials they already hold. What should be configured?

- A. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- B. Create a service account key and embed it in the application configuration
- C. Configure single sign-on with a third-party identity provider over SAML
- D. Let each user decide whether to enrol in 2-step verification

### 3. Removing a person from one directory must remove every cloud grant they held. What should hold the identities?

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Give every platform lead the super administrator role for convenience
- C. Create a service account key and embed it in the application configuration
- D. Federate the workforce to Cloud Identity and enforce it as the identity source

### 4. People who change teams keep their old project grants for weeks. What should be automated?

- A. Assign the super administrator role to a dedicated break-glass account with hardware keys
- B. Have a team member update accounts by hand when the HR export arrives
- C. Grant the role to a group and manage membership
- D. Drive joiner, mover, and leaver flows through the Admin SDK Directory API

### 5. Which account may still reset the tenant when a bad SSO configuration locks every administrator out?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Assign the super administrator role to a dedicated break-glass account with hardware keys
- C. Give every platform lead the super administrator role for convenience
- D. Grant the predefined role that matches the task

### 6. A partner must use its own directory, and its members must not reach resources outside the agreed domain. Which two controls apply? Select two.

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Federate the partner workforce with Workforce Identity Federation
- C. Create a service account key and embed it in the application configuration
- D. Set the domain restricted sharing constraint on the organisation
- E. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 7. Contractors hold local passwords that the security team has to rotate itself. What is the weakness?

- A. Set the domain restricted sharing constraint on the organisation
- B. Configure Workload Identity Federation for the external workload
- C. Federate the partner workforce with Workforce Identity Federation
- D. Create a Cloud Identity user per contractor and issue long-lived passwords

### 8. A batch fleet needs per-workload identity and the narrowest grant that still runs each job. Which two changes apply? Select two.

- A. Run the workload as the default Compute Engine service account
- B. Grant the role to a group and manage membership
- C. Grant the predefined role that matches the task
- D. Grant the basic Editor role to the team
- E. Create a dedicated service account per workload with only the roles it needs

### 9. A retired pipeline's account still holds a write role and nobody knows whether it is used. What should be read first?

- A. Grant the basic Editor role to the team
- B. Create a service account key and embed it in the application configuration
- C. Grant the role to a group and manage membership
- D. Read the Policy Analyzer output before removing an unused grant

### 10. Every project's default compute account carries Editor without anyone granting it. What is the exposure?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Run the workload as the default Compute Engine service account
- C. Create a dedicated service account per workload with only the roles it needs
- D. Create a service account key and embed it in the application configuration

### 11. An engineer downloaded a credential to test locally and never deleted it. What is in circulation?

- A. Create a service account key and embed it in the application configuration
- B. Issue a short-lived access token through impersonation or metadata
- C. Configure Workload Identity Federation for the external workload
- D. Grant the caller the Service Account Token Creator role on the target account

### 12. A workload needs a credential that stops working on its own with nobody rotating it. What should it use?

- A. Issue a short-lived access token through impersonation or metadata
- B. Create a service account key and embed it in the application configuration
- C. Set the credential as a plain environment variable in the deployment
- D. Enforce a password policy with a minimum length and a reuse ban

### 13. Two people act as the same account and the log shows only the account name. What makes the human visible?

- A. Enforce 2-step verification for the whole organisation
- B. Create a service account key and embed it in the application configuration
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Set the credential as a plain environment variable in the deployment

### 14. An external cluster must call the API, and only one namespace of that cluster may do so. Which two settings apply? Select two.

- A. Federate the partner workforce with Workforce Identity Federation
- B. Create a service account key and embed it in the application configuration
- C. Configure Workload Identity Federation for the external workload
- D. Set the credential as a plain environment variable in the deployment
- E. Restrict the Workload Identity pool with an attribute condition on the subject

### 15. The external provider is trusted wholesale, so any workload it hosts can impersonate the account. What is missing?

- A. Configure Workload Identity Federation for the external workload
- B. Restrict the Workload Identity pool with an attribute condition on the subject
- C. Set the domain restricted sharing constraint on the organisation
- D. Create a service account key and embed it in the application configuration

### 16. A migration vendor needs the pipeline's permissions for one weekend. What should be granted?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Create a service account key and embed it in the application configuration
- C. Set the credential as a plain environment variable in the deployment
- D. Issue a short-lived access token through impersonation or metadata

### 17. A partner was sent a key file so it could act as the account. What is the objection?

- A. Hand the caller a JSON key for the service account instead
- B. Issue a short-lived access token through impersonation or metadata
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Configure Workload Identity Federation for the external workload

### 18. The same password must not be reused across the tenant. What should be enforced?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Restrict the project to the APIs it needs and review them on a schedule
- C. Let each user decide whether to enrol in 2-step verification
- D. Set a session length and reauthentication policy for the admin console

### 19. Console sessions must end after eight hours without activity. What should be set?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Let each user decide whether to enrol in 2-step verification
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Set a session length and reauthentication policy for the admin console

### 20. A production change must be approved by a second person before the right is granted. What should be used?

- A. Grant the basic Editor role to the team
- B. Grant the privileged role permanently and review it once a year
- C. Grant the role through Privileged Access Manager with an approval and a time limit
- D. Grant the role to a group and manage membership

### 21. An engineer keeps Owner so that they can approve their own emergency change. What practice is that?

- A. Grant the predefined role that matches the task
- B. Grant the privileged role permanently and review it once a year
- C. Grant the role to a group and manage membership
- D. Grant the role through Privileged Access Manager with an approval and a time limit

### 22. A grant must apply only from the corporate range, and it must stop at quarter end. Which two controls apply? Select two.

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Grant the predefined role that matches the task
- D. Attach an IAM deny policy to the organisation
- E. Create a service perimeter with VPC Service Controls

### 23. A prohibition must survive any allow that is written later. What should be attached?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Attach an IAM deny policy to the organisation
- C. Enforce the constraint with an organization policy
- D. Write an Access Context Manager access level and bind it to the perimeter

### 24. Seventy projects will be generated from a template under one policy. Where should the policy sit?

- A. Have a team member update accounts by hand when the HR export arrives
- B. Create a sink in each project and hope nobody adds a project
- C. Create a folder per environment and attach the policy at the folder
- D. Ask each project owner to disable the setting

### 25. A constraint must prevent any project from disabling audit logging. What should enforce it?

- A. Ask each project owner to disable the setting
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Enforce the constraint with an organization policy
- D. Create a folder per environment and attach the policy at the folder

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. The organisation must deny one port, and a project must still allow its own health check. Which two layers apply? Select two.

- A. Create a service perimeter with VPC Service Controls
- B. Allow all egress and rely on the application to be careful
- C. Deploy a hierarchical firewall policy at the organisation or folder level
- D. Rely on the default VPC firewall rules in each project
- E. Attach a Cloud Armor security policy to the backend service

### 27. Traffic is permitted by default because nobody removed the permissive rule. What is being described?

- A. Deploy the instances with internal IP addresses only
- B. Allow all egress and rely on the application to be careful
- C. Create a service perimeter with VPC Service Controls
- D. Deploy a hierarchical firewall policy at the organisation or folder level

### 28. Only one SaaS tenant may be called on port 443 from the build subnet. What should be enabled?

- A. Enable layer 7 inspection on the firewall policy for the egress rule
- B. Route the egress through Secure Web Proxy
- C. Filter on address and port only and allow the rest
- D. Attach a Cloud Armor security policy to the backend service

### 29. A rule matches on address and port while the team expects host matching. What explains the result?

- A. Put Identity-Aware Proxy in front of the application
- B. Filter on address and port only and allow the rest
- C. Deploy Cloud IDS on the network
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 30. A credential-stuffing run must be throttled per client address. What should be configured?

- A. Rely on the default VPC firewall rules in each project
- B. Put Identity-Aware Proxy in front of the application
- C. Attach a Cloud Armor security policy to the backend service
- D. Add a web application firewall rule in the application framework

### 31. Recognised good crawlers must pass while unknown automation is challenged. What should be enabled?

- A. Enable Cloud Armor bot management on the policy
- B. Attach a Cloud Armor security policy to the backend service
- C. Add a web application firewall rule in the application framework
- D. Terminate TLS at the load balancer with a managed certificate

### 32. Requests must be authenticated before reaching the application, and the application must not be reachable around that check. Which two controls apply? Select two.

- A. Terminate TLS at the load balancer with a managed certificate
- B. Attach a Cloud Armor security policy to the backend service
- C. Deploy the instances with internal IP addresses only
- D. Put Identity-Aware Proxy in front of the application
- E. Publish the application only through a VPN concentrator

### 33. IAP sits in front of the service but the backend also answers on a public address. What is missing?

- A. Put Identity-Aware Proxy in front of the application
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Attach a Cloud Armor security policy to the backend service
- D. Deploy the instances with internal IP addresses only

### 34. Every internal service must present a certificate from one controlled authority. What should be introduced?

- A. Enable Private Google Access on the subnet
- B. Generate a self-signed certificate on each instance
- C. Issue internal certificates from Certificate Authority Service
- D. Terminate TLS at the load balancer with a managed certificate

### 35. A managed certificate must renew without anyone noticing. What should terminate the connection?

- A. Pass encrypted traffic straight through to the instance
- B. Filter on address and port only and allow the rest
- C. Generate a self-signed certificate on each instance
- D. Terminate TLS at the load balancer with a managed certificate

### 36. Browsing must follow an allowlist, and a known-bad domain must not resolve. Which two services apply? Select two.

- A. Use a Cloud DNS response policy to block the known-bad domain
- B. Allow all egress and rely on the application to be careful
- C. Turn on DNSSEC for the public zone
- D. Route the egress through Secure Web Proxy
- E. Run a NAT instance on a Compute Engine virtual machine

### 37. The outbound path must not depend on one virtual machine. What should be used instead?

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Allow all egress and rely on the application to be careful
- C. Place Cloud NAT in front of the private instances
- D. Terminate TLS at the load balancer with a managed certificate

### 38. An instance with only an internal address must still reach Google APIs. What should be enabled?

- A. Build a single classic VPN tunnel
- B. Publish the service through a Private Service Connect endpoint
- C. Place Cloud NAT in front of the private instances
- D. Enable Private Google Access on the subnet

### 39. A deprecated API is still enabled on the project months after the migration. What should be reviewed?

- A. Restrict the project to the APIs it needs and review them on a schedule
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Create a service perimeter with VPC Service Controls
- D. Enforce the constraint with an organization policy

### 40. The web tier can reach the database tier directly today. What should be redesigned?

- A. Rely on the default VPC firewall rules in each project
- B. Allow all egress and rely on the application to be careful
- C. Give each tier its own subnet and allow only the flows between adjacent tiers
- D. Peer the two VPC networks and scope the firewall rules to the peer

### 41. Six teams need one network under central control and their own projects. What should be built?

- A. Place Cloud NAT in front of the private instances
- B. Peer the two VPC networks and scope the firewall rules to the peer
- C. Host the workload in a Shared VPC service project
- D. Run a NAT instance on a Compute Engine virtual machine

### 42. A regulated dataset needs a boundary, and the build agents must still reach the API from inside it. Which two choices apply? Select two.

- A. Use restricted.googleapis.com for the API traffic
- B. Enable Private Google Access on the subnet
- C. Create a service perimeter with VPC Service Controls
- D. Rely on IAM to prevent data leaving the project
- E. Allow all egress and rely on the application to be careful

### 43. A team trusted the perimeter to replace IAM and the data still moved between projects. What was misunderstood?

- A. Rely on IAM to prevent data leaving the project
- B. Create a service perimeter with VPC Service Controls
- C. Attach an IAM deny policy to the organisation
- D. Grant authorised views or dataset-level IAM rather than table reads

### 44. The office link must survive one tunnel going down during maintenance. What should be built?

- A. Build a single classic VPN tunnel
- B. Build an HA VPN tunnel pair with two interfaces
- C. Place Cloud NAT in front of the private instances
- D. Provision a Dedicated Interconnect with two attachments

### 45. Ten gigabits on a private circuit with two attachments is required. What should be provisioned?

- A. Build a single classic VPN tunnel
- B. Build an HA VPN tunnel pair with two interfaces
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Provision a Dedicated Interconnect with two attachments

### 46. An on-premises host must reach a Google API with no internet egress. What should be configured?

- A. Configure Private Google Access for on-premises hosts over the hybrid route
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Place Cloud NAT in front of the private instances
- D. Publish the service through a Private Service Connect endpoint

### 47. Egress must be managed and logged with no instance to maintain. What should be deployed?

- A. Place Cloud NAT in front of the private instances
- B. Terminate TLS at the load balancer with a managed certificate
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Allow all egress and rely on the application to be careful

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. Nobody knows which warehouse tables hold health data. What should be run?

- A. Replace the value with an unsalted hash
- B. Make the bucket public but unlisted
- C. Ask the team to report which tables they believe hold personal data
- D. Run a Sensitive Data Protection discovery scan over the storage and warehouse

### 49. Two scans of the same column disagree about which rows match. What should be shared?

- A. Ask the team to report which tables they believe hold personal data
- B. Set the credential as a plain environment variable in the deployment
- C. Reuse a stored de-identification template across pipelines
- D. Save a Sensitive Data Protection inspect template and reuse it

### 50. The data catalogue is maintained by asking each team to report its own tables. What is the weakness?

- A. Ask the team to report which tables they believe hold personal data
- B. Replace the value with an unsalted hash
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Run a Sensitive Data Protection discovery scan over the storage and warehouse

### 51. Two pipelines must join on a stable token while a support console shows only the last four digits. Which two methods apply? Select two.

- A. Generate the key in the application and store it beside the data
- B. Redact the matched values with a de-identification template
- C. Replace the value with an unsalted hash
- D. Apply format-preserving encryption to the card number field
- E. Replace the value with a pseudonym from a crypto key

### 52. A national identifier must be replaced so that the column cannot be reversed later. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Apply format-preserving encryption to the card number field
- C. Replace the value with an unsalted hash
- D. Replace the value with a pseudonym from a crypto key

### 53. Card numbers must stay sixteen digits for a legacy validator while remaining unreadable. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Replace the value with an unsalted hash
- C. Apply format-preserving encryption to the card number field
- D. Replace the value with a pseudonym from a crypto key

### 54. Analysts must not read raw identifiers, and the application must connect without a stored password. Which two controls apply? Select two.

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Use Cloud SQL IAM database authentication for the application
- C. Grant the analyst the ability to export the whole table to a bucket
- D. Put the database password in the application config file
- E. Set an allUsers object ACL on the specific file

### 55. Every object carries its own ACL and a reviewer cannot tell who may read the bucket. What should be enabled?

- A. Set an allUsers object ACL on the specific file
- B. Make the bucket public but unlisted
- C. Grant the bucket role to a group with uniform bucket-level access
- D. Allow all egress and rely on the application to be careful

### 56. A developer hardcoded a database password so that the connection would work. What is the flaw?

- A. Use Cloud SQL IAM database authentication for the application
- B. Put the database password in the application config file
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Set the credential as a plain environment variable in the deployment

### 57. A secret must be versioned so a rollback restores the previous value. What should hold it?

- A. Put the database password in the application config file
- B. Store the credential in Secret Manager and grant the workload the secret accessor role
- C. Set the credential as a plain environment variable in the deployment
- D. Generate the key in the application and store it beside the data

### 58. A credential is found inside a published container image layer. How was it supplied?

- A. Set the credential as a plain environment variable in the deployment
- B. Generate the key in the application and store it beside the data
- C. Put the database password in the application config file
- D. Store the credential in Secret Manager and grant the workload the secret accessor role

### 59. A forged request from the application reaches the metadata endpoint. What should reject it?

- A. Enable OS Login and turn off project-wide SSH keys
- B. Place Cloud NAT in front of the private instances
- C. Deploy the instances with internal IP addresses only
- D. Require the metadata server header on every request

### 60. SSH access outlives employment because of a project-wide key. What should be enabled?

- A. Create a service account key and embed it in the application configuration
- B. Require the metadata server header on every request
- C. Enable OS Login and turn off project-wide SSH keys
- D. Enforce a password policy with a minimum length and a reuse ban

### 61. One regulator requires customer-held keys, and a second tenant requires the material to stay outside Google. Which two choices apply? Select two.

- A. Import the wrapping key into Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Rely on Google default encryption at rest
- D. Encrypt the dataset with a customer-managed key in Cloud KMS
- E. Generate the key in the application and store it beside the data

### 62. Payment data must be protected by a key the customer can disable. What should be configured?

- A. Hold the key in Cloud External Key Manager outside Google Cloud
- B. Generate the key in the application and store it beside the data
- C. Rely on Google default encryption at rest
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 63. The customer HSM must be the only holder of the key material. What should be used?

- A. Import the wrapping key into Cloud KMS
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Generate the key in the application and store it beside the data

### 64. One workload must use a key held by an external manager, and a legacy dataset must move to KMS without re-encryption. Which two choices apply? Select two.

- A. Import the wrapping key into Cloud KMS
- B. Generate the key in the application and store it beside the data
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Rely on Google default encryption at rest
- E. Set a rotation period on the key

### 65. A key from another provider must come under KMS control without rewriting the stored objects. What should be done?

- A. Set a rotation period on the key
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Import the wrapping key into Cloud KMS

### 66. The crypto standard demands a fresh version each quarter, tracked automatically. What should be configured?

- A. Set a rotation period on the key
- B. Disable the key version and re-wrap the data
- C. Generate the key in the application and store it beside the data
- D. Import the wrapping key into Cloud KMS

### 67. A tenant's key must stop decrypting immediately after an incident. What should be done?

- A. Import the wrapping key into Cloud KMS
- B. Rely on Google default encryption at rest
- C. Disable the key version and re-wrap the data
- D. Set a rotation period on the key

### 68. Memory encryption is required for a virtual machine that handles card data. What should be used?

- A. Run the workload on a Confidential VM
- B. Enable OS Login and turn off project-wide SSH keys
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Rely on Google default encryption at rest

### 69. Pod memory must be protected in a cluster that several teams share. What should be used?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Run the pod in a Confidential GKE node pool
- C. Enable OS Login and turn off project-wide SSH keys
- D. Run the workload on a Confidential VM

### 70. Objects must be removed after the retention period without anyone remembering. What should be attached?

- A. Make the bucket public but unlisted
- B. Attach an object lifecycle rule that keeps the required retention
- C. Set an allUsers object ACL on the specific file
- D. Apply a retention policy with bucket lock

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A scanner must fail the pipeline on a critical finding, and the registry must be re-checked afterwards. Which two checks apply? Select two.

- A. Deploy with Binary Authorization in dry-run mode only
- B. Allow all egress and rely on the application to be careful
- C. Let each team patch its own instances when convenient
- D. Scan the running image in production once a quarter
- E. Add an Artifact Analysis scan to the CI pipeline

### 72. A vulnerability was found in an image that had been running for months. Which scan would have caught it?

- A. Enforce a Binary Authorization policy that requires an attested image
- B. Add an Artifact Analysis scan to the CI pipeline
- C. Let each team patch its own instances when convenient
- D. Scan the running image in production once a quarter

### 73. Only attested images may run in the cluster. What should be enforced?

- A. Attach a Cloud Armor security policy to the backend service
- B. Enforce a Binary Authorization policy that requires an attested image
- C. Deploy the instances with internal IP addresses only
- D. Deploy with Binary Authorization in dry-run mode only

### 74. Admission control needs a trial period that records but does not block. What should be used?

- A. Deploy with Binary Authorization in dry-run mode only
- B. Deploy Cloud IDS on the network
- C. Add an Artifact Analysis scan to the CI pipeline
- D. Scan the running image in production once a quarter

### 75. The base image must be minimal with no unused accounts. What should be built?

- A. Scan the running image in production once a quarter
- B. Build the base image from a hardened source with a documented baseline
- C. Let each team patch its own instances when convenient
- D. Schedule patch jobs across the fleet with VM Manager

### 76. Hosts must be patched and reported across the fleet. What should be introduced?

- A. Schedule patch jobs across the fleet with VM Manager
- B. Let each team patch its own instances when convenient
- C. Compare the deployed configuration with the intended state on a schedule
- D. Build the base image from a hardened source with a documented baseline

### 77. A console change created an open bucket and nobody noticed. What should be added?

- A. Deploy a Security Health Analytics custom module for the check
- B. Lower the log volume by disabling data access logs
- C. Compare the deployed configuration with the intended state on a schedule
- D. Write a custom organization policy constraint for the rule

### 78. The same unsafe setting returns after every manual fix. What should be written?

- A. Lower the log volume by disabling data access logs
- B. Write a custom organization policy constraint for the rule
- C. Compare the deployed configuration with the intended state on a schedule
- D. Deploy a Security Health Analytics custom module for the check

### 79. Denied flows must be recorded for review, and an inline sensor must alert on threats. Which two services apply? Select two.

- A. Mirror the production traffic to a collector with Packet Mirroring
- B. Lower the log volume by disabling data access logs
- C. Give the SIEM a service account key so it can pull the logs
- D. Enable VPC Flow Logs on the subnets
- E. Deploy Cloud IDS on the network

### 80. A packet capture is needed for a forensic review. What should be used?

- A. Deploy Cloud IDS on the network
- B. Enable VPC Flow Logs on the subnets
- C. Query the logs through Log Analytics
- D. Mirror the production traffic to a collector with Packet Mirroring

### 81. Investigators need SQL over eighteen months of security entries without exporting them. What should be used?

- A. Lower the log volume by disabling data access logs
- B. Query the logs through Log Analytics
- C. Give the SIEM a service account key so it can pull the logs
- D. Create a sink in each project and hope nobody adds a project

### 82. The auditor must read logs that the operator cannot delete. What should change?

- A. Create a sink in each project and hope nobody adds a project
- B. Route security logs to a dedicated project with its own retention
- C. Give the SIEM a service account key so it can pull the logs
- D. Lower the log volume by disabling data access logs

### 83. Data access logs were turned off to save money. What is no longer available?

- A. Lower the log volume by disabling data access logs
- B. Enable Data Access audit logs for the service
- C. Apply a retention policy with bucket lock
- D. Route security logs to a dedicated project with its own retention

### 84. An investigator asks who changed a firewall rule. Which log answers?

- A. Enable Data Access audit logs for the service
- B. Enable VPC Flow Logs on the subnets
- C. Create a log sink that routes the entries to the destination
- D. Read the Admin Activity audit log for the change

### 85. An investigator asks who opened a specific object. Which log answers?

- A. Enable VPC Flow Logs on the subnets
- B. Enable Data Access audit logs for the service
- C. Create a log sink that routes the entries to the destination
- D. Read the Admin Activity audit log for the change

### 86. Every project including future ones must reach the SIEM, and no long-lived key may be stored there. Which two choices apply? Select two.

- A. Create a sink in each project and hope nobody adds a project
- B. Export the entries to the external SIEM through Pub/Sub
- C. Create an aggregated sink at the organisation level
- D. Set the credential as a plain environment variable in the deployment
- E. Give the SIEM a service account key so it can pull the logs

### 87. A per-project sink misses every project created after it was configured. What is being described?

- A. Create an aggregated sink at the organisation level
- B. Create a log sink that routes the entries to the destination
- C. Export the entries to the external SIEM through Pub/Sub
- D. Create a sink in each project and hope nobody adds a project

### 88. Findings from every detector must appear in one console. What should be reviewed?

- A. Deploy a Security Health Analytics custom module for the check
- B. Compare the deployed configuration with the intended state on a schedule
- C. Review the Security Command Center findings for the project
- D. Query the logs through Log Analytics

### 89. A finding must open a ticket without a person checking the console. What should be configured?

- A. Publish new findings to Pub/Sub for the response pipeline
- B. Give the SIEM a service account key so it can pull the logs
- C. Close the finding as a false positive without a comment
- D. Lower the log volume by disabling data access logs

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. The contract must state who patches the guest system, and which control evidences it. Which two artefacts apply? Select two.

- A. Assume Google secures every layer once the data is in the cloud
- B. Map each requirement to the control that satisfies it and the evidence it produces
- C. State in the policy document that the environment is compliant
- D. Document which controls Google operates and which the customer must implement
- E. Declare the whole organisation in scope for every regime

### 91. A reseller states that cloud hosting transfers all security duty away from the customer. What is wrong?

- A. Declare the whole organisation in scope for every regime
- B. Assume Google secures every layer once the data is in the cloud
- C. Document which controls Google operates and which the customer must implement
- D. State in the policy document that the environment is compliant

### 92. A regime requires support personnel to sit in one country. What should be created?

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Ask each project owner to disable the setting
- C. Create the folder as an Assured Workloads environment
- D. Constrain the resources to the required region with a location organization policy

### 93. The controls are re-created by hand in every new project. What fails first?

- A. Keep the audit evidence for the period the regime requires
- B. Create the folder as an Assured Workloads environment
- C. Ask each project owner to disable the setting
- D. Record the regime in a spreadsheet and configure each control by hand

### 94. Procurement needs proof that Google staff visits to customer content are disclosed to the customer. What should be enabled?

- A. Enable Data Access audit logs for the service
- B. Read the Admin Activity audit log for the change
- C. Turn on Access Transparency and read its logs
- D. Require Access Approval before an operator may read the content

### 95. Nobody outside the customer may open the data without the customer agreeing first. What should be required?

- A. Turn on Access Transparency and read its logs
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Require Access Approval before an operator may read the content
- D. Create a service perimeter with VPC Service Controls

### 96. Data must stay in one country for every new resource. What should be enforced?

- A. Constrain the resources to the required region with a location organization policy
- B. Leave the default multi-region setting
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Declare the whole organisation in scope for every regime

### 97. Storage was created without a location choice and the regulator asked for one nation. What was the cause?

- A. Declare the whole organisation in scope for every regime
- B. Record the regime in a spreadsheet and configure each control by hand
- C. Leave the default multi-region setting
- D. Constrain the resources to the required region with a location organization policy

### 98. A clause has a control and the auditor wants the evidence named beside it. What should be produced?

- A. Declare the whole organisation in scope for every regime
- B. State in the policy document that the environment is compliant
- C. Assume Google secures every layer once the data is in the cloud
- D. Map each requirement to the control that satisfies it and the evidence it produces

### 99. Every control on the list works, but nobody is named as answerable for it. What is missing?

- A. Name an owner for each control
- B. State in the policy document that the environment is compliant
- C. Declare the whole organisation in scope for every regime
- D. Keep the audit evidence for the period the regime requires

### 100. The audit must state which projects it covers before testing starts. What should be written?

- A. Draw the compliance boundary around the projects and services that hold the regulated data
- B. State in the policy document that the environment is compliant
- C. Declare the whole organisation in scope for every regime
- D. Record the regime in a spreadsheet and configure each control by hand

---

## Answer key and explanations

### Question 1 — B

Answer: Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync. GCDS pushes the accounts from the existing directory on a schedule. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: GCDS pushes the accounts from the existing directory on a schedule.
- **B:** Correct. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. In this case: GCDS pushes the accounts from the existing directory on a schedule.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: GCDS pushes the accounts from the existing directory on a schedule.
- **D:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: GCDS pushes the accounts from the existing directory on a schedule.

### Question 2 — C

Answer: Configure single sign-on with a third-party identity provider over SAML. SAML SSO keeps authentication with the existing provider. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: SAML SSO keeps authentication with the existing provider.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: SAML SSO keeps authentication with the existing provider.
- **C:** Correct. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. In this case: SAML SSO keeps authentication with the existing provider.
- **D:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: SAML SSO keeps authentication with the existing provider.

### Question 3 — D

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory the grants resolve against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Cloud Identity is the directory the grants resolve against.
- **B:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: Cloud Identity is the directory the grants resolve against.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Cloud Identity is the directory the grants resolve against.
- **D:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory the grants resolve against.

### Question 4 — D

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK lifecycle automation applies the move when the record changes. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: The Admin SDK lifecycle automation applies the move when the record changes.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK lifecycle automation applies the move when the record changes.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The Admin SDK lifecycle automation applies the move when the record changes.
- **D:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK lifecycle automation applies the move when the record changes.

### Question 5 — B

Answer: Assign the super administrator role to a dedicated break-glass account with hardware keys. A dedicated break-glass super administrator is reserved for that recovery. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A dedicated break-glass super administrator is reserved for that recovery.
- **B:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: A dedicated break-glass super administrator is reserved for that recovery.
- **C:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A dedicated break-glass super administrator is reserved for that recovery.
- **D:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: A dedicated break-glass super administrator is reserved for that recovery.

### Question 6 — B, D

Answers: Federate the partner workforce with Workforce Identity Federation; Set the domain restricted sharing constraint on the organisation. Federation accepts the partner provider, and domain restricted sharing bounds the grants. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Federation accepts the partner provider, and domain restricted sharing bounds the grants.
- **B:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Federation accepts the partner provider, and domain restricted sharing bounds the grants.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation accepts the partner provider, and domain restricted sharing bounds the grants.
- **D:** Correct. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. In this case: Federation accepts the partner provider, and domain restricted sharing bounds the grants.
- **E:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Federation accepts the partner provider, and domain restricted sharing bounds the grants.

### Question 7 — D

Answer: Create a Cloud Identity user per contractor and issue long-lived passwords. A local account per contractor multiplies what must be reviewed and revoked. A local user per contractor multiplies the accounts that must be reviewed and revoked. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.
- **B:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.
- **C:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.
- **D:** Correct. A local user per contractor multiplies the accounts that must be reviewed and revoked. In this case: A local account per contractor multiplies what must be reviewed and revoked.

### Question 8 — C, E

Answers: Create a dedicated service account per workload with only the roles it needs; Grant the predefined role that matches the task. A dedicated account per workload gives identity, and a predefined role bounds the grant. A per-workload service account bounds the blast radius and makes audit records attributable. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A dedicated account per workload gives identity, and a predefined role bounds the grant.
- **B:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: A dedicated account per workload gives identity, and a predefined role bounds the grant.
- **C:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: A dedicated account per workload gives identity, and a predefined role bounds the grant.
- **D:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A dedicated account per workload gives identity, and a predefined role bounds the grant.
- **E:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A dedicated account per workload gives identity, and a predefined role bounds the grant.

### Question 9 — D

Answer: Read the Policy Analyzer output before removing an unused grant. Policy Analyser shows whether the grant was used at all. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Policy Analyser shows whether the grant was used at all.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Policy Analyser shows whether the grant was used at all.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Policy Analyser shows whether the grant was used at all.
- **D:** Correct. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. In this case: Policy Analyser shows whether the grant was used at all.

### Question 10 — B

Answer: Run the workload as the default Compute Engine service account. The default account is shared, so its grants reach every workload on the project. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.
- **B:** Correct. In this case: The default account is shared, so its grants reach every workload on the project.
- **C:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.

### Question 11 — A

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key has no expiry unless one is set. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key has no expiry unless one is set.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key has no expiry unless one is set.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key has no expiry unless one is set.
- **D:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key has no expiry unless one is set.

### Question 12 — A

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token expires by itself. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: A short-lived token expires by itself.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token expires by itself.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token expires by itself.
- **D:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A short-lived token expires by itself.

### Question 13 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation records the person who acted as the account. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: Impersonation records the person who acted as the account.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation records the person who acted as the account.
- **C:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation records the person who acted as the account.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation records the person who acted as the account.

### Question 14 — C, E

Answers: Configure Workload Identity Federation for the external workload; Restrict the Workload Identity pool with an attribute condition on the subject. Federation removes the key, and an attribute condition limits the namespace. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: Federation removes the key, and an attribute condition limits the namespace.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation removes the key, and an attribute condition limits the namespace.
- **C:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Federation removes the key, and an attribute condition limits the namespace.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Federation removes the key, and an attribute condition limits the namespace.
- **E:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: Federation removes the key, and an attribute condition limits the namespace.

### Question 15 — B

Answer: Restrict the Workload Identity pool with an attribute condition on the subject. An attribute condition restricts which external identities may act. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **B:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: An attribute condition restricts which external identities may act.
- **C:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An attribute condition restricts which external identities may act.

### Question 16 — A

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation gives the acting right without exporting a credential. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation gives the acting right without exporting a credential.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation gives the acting right without exporting a credential.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation gives the acting right without exporting a credential.
- **D:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation gives the acting right without exporting a credential.

### Question 17 — A

Answer: Hand the caller a JSON key for the service account instead. A handed-out key cannot be scoped and outlives the task. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A handed-out key cannot be scoped and outlives the task.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A handed-out key cannot be scoped and outlives the task.
- **C:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A handed-out key cannot be scoped and outlives the task.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A handed-out key cannot be scoped and outlives the task.

### Question 18 — A

Answer: Enforce a password policy with a minimum length and a reuse ban. A password policy includes a reuse ban. A password policy raises the cost of credential guessing without depending on the user to choose well. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A password policy raises the cost of credential guessing without depending on the user to choose well. In this case: A password policy includes a reuse ban.
- **B:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: A password policy includes a reuse ban.
- **C:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A password policy includes a reuse ban.
- **D:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: A password policy includes a reuse ban.

### Question 19 — D

Answer: Set a session length and reauthentication policy for the admin console. A session length policy forces reauthentication. A session control limits how long a stolen browser session stays useful. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A session length policy forces reauthentication.
- **B:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A session length policy forces reauthentication.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A session length policy forces reauthentication.
- **D:** Correct. A session control limits how long a stolen browser session stays useful. In this case: A session length policy forces reauthentication.

### Question 20 — C

Answer: Grant the role through Privileged Access Manager with an approval and a time limit. Privileged Access Manager gates the grant on the approval. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Privileged Access Manager gates the grant on the approval.
- **B:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager gates the grant on the approval.
- **C:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Privileged Access Manager gates the grant on the approval.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager gates the grant on the approval.

### Question 21 — B

Answer: Grant the privileged role permanently and review it once a year. Standing privilege removes the separation the approval was meant to create. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Standing privilege removes the separation the approval was meant to create.
- **B:** Correct. Permanent privilege is live for every hour of the year, including the hours nobody is watching. In this case: Standing privilege removes the separation the approval was meant to create.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Standing privilege removes the separation the approval was meant to create.
- **D:** Incorrect for this question. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Why the correct answer wins: Standing privilege removes the separation the approval was meant to create.

### Question 22 — A, B

Answers: Write an Access Context Manager access level and bind it to the perimeter; Add an IAM condition that limits the grant to a time window and a resource prefix. An access level describes the request context, and the condition adds the expiry. Access Context Manager describes the request context, such as network origin, that a policy can require. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An access level describes the request context, and the condition adds the expiry.
- **B:** Correct. Access Context Manager describes the request context, such as network origin, that a policy can require. In this case: An access level describes the request context, and the condition adds the expiry.
- **C:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: An access level describes the request context, and the condition adds the expiry.
- **D:** Incorrect for this question. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Why the correct answer wins: An access level describes the request context, and the condition adds the expiry.
- **E:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An access level describes the request context, and the condition adds the expiry.

### Question 23 — B

Answer: Attach an IAM deny policy to the organisation. A deny policy is evaluated above every allow beneath it. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **B:** Correct. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. In this case: A deny policy is evaluated above every allow beneath it.
- **C:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **D:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.

### Question 24 — C

Answer: Create a folder per environment and attach the policy at the folder. A folder carries one attachment for every project inside it. A folder boundary means one attachment covers every current and future project inside it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A folder carries one attachment for every project inside it.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A folder carries one attachment for every project inside it.
- **C:** Correct. A folder boundary means one attachment covers every current and future project inside it. In this case: A folder carries one attachment for every project inside it.
- **D:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A folder carries one attachment for every project inside it.

### Question 25 — C

Answer: Enforce the constraint with an organization policy. An organization policy binds every project beneath it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: An organization policy binds every project beneath it.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: An organization policy binds every project beneath it.
- **C:** Correct. In this case: An organization policy binds every project beneath it.
- **D:** Incorrect for this question. A folder boundary means one attachment covers every current and future project inside it. Why the correct answer wins: An organization policy binds every project beneath it.

### Question 26 — C, D

Answers: Deploy a hierarchical firewall policy at the organisation or folder level; Rely on the default VPC firewall rules in each project. The hierarchical policy carries the deny, and the project rule adds the local allow. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The hierarchical policy carries the deny, and the project rule adds the local allow.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The hierarchical policy carries the deny, and the project rule adds the local allow.
- **C:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: The hierarchical policy carries the deny, and the project rule adds the local allow.
- **D:** Correct. Project-level rules are editable by the project owner and are evaluated after the hierarchy. In this case: The hierarchical policy carries the deny, and the project rule adds the local allow.
- **E:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: The hierarchical policy carries the deny, and the project rule adds the local allow.

### Question 27 — B

Answer: Allow all egress and rely on the application to be careful. An allow-all rule lets a workload reach anything the internet offers. Unrestricted egress lets a compromised workload reach anything the internet offers. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: An allow-all rule lets a workload reach anything the internet offers.
- **B:** Correct. Unrestricted egress lets a compromised workload reach anything the internet offers. In this case: An allow-all rule lets a workload reach anything the internet offers.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An allow-all rule lets a workload reach anything the internet offers.
- **D:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: An allow-all rule lets a workload reach anything the internet offers.

### Question 28 — A

Answer: Enable layer 7 inspection on the firewall policy for the egress rule. Layer 7 inspection reads the destination host. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the destination host.
- **B:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: Layer 7 inspection reads the destination host.
- **C:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the destination host.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Layer 7 inspection reads the destination host.

### Question 29 — B

Answer: Filter on address and port only and allow the rest. A layer 4 rule cannot see the host name inside an allowed connection. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A layer 4 rule cannot see the host name inside an allowed connection.
- **B:** Correct. In this case: A layer 4 rule cannot see the host name inside an allowed connection.
- **C:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: A layer 4 rule cannot see the host name inside an allowed connection.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A layer 4 rule cannot see the host name inside an allowed connection.

### Question 30 — C

Answer: Attach a Cloud Armor security policy to the backend service. Cloud Armor applies the rate limit at the edge. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Cloud Armor applies the rate limit at the edge.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Cloud Armor applies the rate limit at the edge.
- **C:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: Cloud Armor applies the rate limit at the edge.
- **D:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Cloud Armor applies the rate limit at the edge.

### Question 31 — A

Answer: Enable Cloud Armor bot management on the policy. Bot management separates the known crawler from the unknown automation. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. In this case: Bot management separates the known crawler from the unknown automation.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Bot management separates the known crawler from the unknown automation.
- **C:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Bot management separates the known crawler from the unknown automation.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Bot management separates the known crawler from the unknown automation.

### Question 32 — C, D

Answers: Put Identity-Aware Proxy in front of the application; Deploy the instances with internal IP addresses only. IAP authorises each request, and an internal address closes the bypass. IAP authenticates and authorises each request against IAM before it reaches the backend. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: IAP authorises each request, and an internal address closes the bypass.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP authorises each request, and an internal address closes the bypass.
- **C:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: IAP authorises each request, and an internal address closes the bypass.
- **D:** Correct. IAP authenticates and authorises each request against IAM before it reaches the backend. In this case: IAP authorises each request, and an internal address closes the bypass.
- **E:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP authorises each request, and an internal address closes the bypass.

### Question 33 — D

Answer: Deploy the instances with internal IP addresses only. An internal-only address removes the path that skips the check. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: An internal-only address removes the path that skips the check.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: An internal-only address removes the path that skips the check.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: An internal-only address removes the path that skips the check.
- **D:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal-only address removes the path that skips the check.

### Question 34 — C

Answer: Issue internal certificates from Certificate Authority Service. Certificate Authority Service issues the private certificates. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Certificate Authority Service issues the private certificates.
- **B:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues the private certificates.
- **C:** Correct. In this case: Certificate Authority Service issues the private certificates.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Certificate Authority Service issues the private certificates.

### Question 35 — D

Answer: Terminate TLS at the load balancer with a managed certificate. The load balancer renews and serves the managed certificate. Terminating at the load balancer gives one managed certificate and a single policy point. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: The load balancer renews and serves the managed certificate.
- **B:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: The load balancer renews and serves the managed certificate.
- **C:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: The load balancer renews and serves the managed certificate.
- **D:** Correct. Terminating at the load balancer gives one managed certificate and a single policy point. In this case: The load balancer renews and serves the managed certificate.

### Question 36 — A, D

Answers: Route the egress through Secure Web Proxy; Use a Cloud DNS response policy to block the known-bad domain. The proxy enforces the allowlist, and the response policy overrides the resolution. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. A response policy overrides resolution for named domains inside the network. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A response policy overrides resolution for named domains inside the network. In this case: The proxy enforces the allowlist, and the response policy overrides the resolution.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The proxy enforces the allowlist, and the response policy overrides the resolution.
- **C:** Incorrect for this question. DNSSEC signs the answers so a resolver can detect a forged response. Why the correct answer wins: The proxy enforces the allowlist, and the response policy overrides the resolution.
- **D:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: The proxy enforces the allowlist, and the response policy overrides the resolution.
- **E:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The proxy enforces the allowlist, and the response policy overrides the resolution.

### Question 37 — C

Answer: Place Cloud NAT in front of the private instances. Cloud NAT is managed and removes the single host. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT is managed and removes the single host.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT is managed and removes the single host.
- **C:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT is managed and removes the single host.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT is managed and removes the single host.

### Question 38 — D

Answer: Enable Private Google Access on the subnet. Private Google Access carries the API traffic for internal-only instances. Private Google Access lets an instance with only an internal address reach Google APIs. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Private Google Access carries the API traffic for internal-only instances.
- **B:** Incorrect for this question. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. Why the correct answer wins: Private Google Access carries the API traffic for internal-only instances.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Private Google Access carries the API traffic for internal-only instances.
- **D:** Correct. Private Google Access lets an instance with only an internal address reach Google APIs. In this case: Private Google Access carries the API traffic for internal-only instances.

### Question 39 — A

Answer: Restrict the project to the APIs it needs and review them on a schedule. The enabled API list should shrink to what the workload calls. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: The enabled API list should shrink to what the workload calls.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: The enabled API list should shrink to what the workload calls.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The enabled API list should shrink to what the workload calls.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: The enabled API list should shrink to what the workload calls.

### Question 40 — C

Answer: Give each tier its own subnet and allow only the flows between adjacent tiers. Tier subnets let the rules express which tier may call which. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Tier subnets let the rules express which tier may call which.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Tier subnets let the rules express which tier may call which.
- **C:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Tier subnets let the rules express which tier may call which.
- **D:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Tier subnets let the rules express which tier may call which.

### Question 41 — C

Answer: Host the workload in a Shared VPC service project. Shared VPC centralises the network in the host project. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **B:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **C:** Correct. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. In this case: Shared VPC centralises the network in the host project.
- **D:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Shared VPC centralises the network in the host project.

### Question 42 — A, C

Answers: Create a service perimeter with VPC Service Controls; Use restricted.googleapis.com for the API traffic. The perimeter sets the boundary, and restricted virtual IPs keep the API path inside. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. In this case: The perimeter sets the boundary, and restricted virtual IPs keep the API path inside.
- **B:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: The perimeter sets the boundary, and restricted virtual IPs keep the API path inside.
- **C:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: The perimeter sets the boundary, and restricted virtual IPs keep the API path inside.
- **D:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: The perimeter sets the boundary, and restricted virtual IPs keep the API path inside.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The perimeter sets the boundary, and restricted virtual IPs keep the API path inside.

### Question 43 — A

Answer: Rely on IAM to prevent data leaving the project. An IAM grant inside the perimeter still allows the copy. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. In this case: An IAM grant inside the perimeter still allows the copy.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An IAM grant inside the perimeter still allows the copy.
- **C:** Incorrect for this question. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Why the correct answer wins: An IAM grant inside the perimeter still allows the copy.
- **D:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: An IAM grant inside the perimeter still allows the copy.

### Question 44 — B

Answer: Build an HA VPN tunnel pair with two interfaces. An HA VPN pair keeps the path up across one failure. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: An HA VPN pair keeps the path up across one failure.
- **B:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: An HA VPN pair keeps the path up across one failure.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An HA VPN pair keeps the path up across one failure.
- **D:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: An HA VPN pair keeps the path up across one failure.

### Question 45 — D

Answer: Provision a Dedicated Interconnect with two attachments. Dedicated Interconnect gives the private circuit with redundant attachments. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.
- **B:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.
- **D:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: Dedicated Interconnect gives the private circuit with redundant attachments.

### Question 46 — A

Answer: Configure Private Google Access for on-premises hosts over the hybrid route. The on-premises variant of Private Google Access carries that traffic privately. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. In this case: The on-premises variant of Private Google Access carries that traffic privately.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The on-premises variant of Private Google Access carries that traffic privately.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: The on-premises variant of Private Google Access carries that traffic privately.
- **D:** Incorrect for this question. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. Why the correct answer wins: The on-premises variant of Private Google Access carries that traffic privately.

### Question 47 — A

Answer: Place Cloud NAT in front of the private instances. Cloud NAT provides the managed outbound path. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT provides the managed outbound path.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT provides the managed outbound path.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT provides the managed outbound path.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT provides the managed outbound path.

### Question 48 — D

Answer: Run a Sensitive Data Protection discovery scan over the storage and warehouse. A discovery scan profiles where the sensitive data sits. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.
- **B:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.
- **C:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.
- **D:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: A discovery scan profiles where the sensitive data sits.

### Question 49 — D

Answer: Save a Sensitive Data Protection inspect template and reuse it. A saved inspect template keeps the rules identical. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A saved inspect template keeps the rules identical.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A saved inspect template keeps the rules identical.
- **C:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A saved inspect template keeps the rules identical.
- **D:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A saved inspect template keeps the rules identical.

### Question 50 — A

Answer: Ask the team to report which tables they believe hold personal data. A self-reported inventory misses what nobody remembered. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A self-reported inventory misses what nobody remembered.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **C:** Incorrect for this question. A saved template keeps the detection rules identical across scans, so results stay comparable. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **D:** Incorrect for this question. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Why the correct answer wins: A self-reported inventory misses what nobody remembered.

### Question 51 — B, E

Answers: Replace the value with a pseudonym from a crypto key; Redact the matched values with a de-identification template. The pseudonym keeps the join, and redaction limits the console. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: The pseudonym keeps the join, and redaction limits the console.
- **B:** Correct. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. In this case: The pseudonym keeps the join, and redaction limits the console.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: The pseudonym keeps the join, and redaction limits the console.
- **D:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: The pseudonym keeps the join, and redaction limits the console.
- **E:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: The pseudonym keeps the join, and redaction limits the console.

### Question 52 — D

Answer: Replace the value with a pseudonym from a crypto key. A pseudonym replaces the value and keeps a stable token. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: A pseudonym replaces the value and keeps a stable token.
- **B:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: A pseudonym replaces the value and keeps a stable token.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A pseudonym replaces the value and keeps a stable token.
- **D:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: A pseudonym replaces the value and keeps a stable token.

### Question 53 — C

Answer: Apply format-preserving encryption to the card number field. Format-preserving encryption keeps the length and the type. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Format-preserving encryption keeps the length and the type.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Format-preserving encryption keeps the length and the type.
- **C:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: Format-preserving encryption keeps the length and the type.
- **D:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Format-preserving encryption keeps the length and the type.

### Question 54 — A, B

Answers: Grant authorised views or dataset-level IAM rather than table reads; Use Cloud SQL IAM database authentication for the application. Authorised views limit the columns, and IAM database authentication removes the password. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. IAM database authentication removes the stored database password and ties each connection to an identity. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Authorised views limit the columns, and IAM database authentication removes the password.
- **B:** Correct. IAM database authentication removes the stored database password and ties each connection to an identity. In this case: Authorised views limit the columns, and IAM database authentication removes the password.
- **C:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Authorised views limit the columns, and IAM database authentication removes the password.
- **D:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Authorised views limit the columns, and IAM database authentication removes the password.
- **E:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Authorised views limit the columns, and IAM database authentication removes the password.

### Question 55 — C

Answer: Grant the bucket role to a group with uniform bucket-level access. Uniform bucket-level access makes IAM the only decision point. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **B:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **C:** Correct. In this case: Uniform bucket-level access makes IAM the only decision point.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.

### Question 56 — B

Answer: Put the database password in the application config file. A password in code is copied into every environment and outlives its owner. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAM database authentication removes the stored database password and ties each connection to an identity. Why the correct answer wins: A password in code is copied into every environment and outlives its owner.
- **B:** Correct. In this case: A password in code is copied into every environment and outlives its owner.
- **C:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: A password in code is copied into every environment and outlives its owner.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A password in code is copied into every environment and outlives its owner.

### Question 57 — B

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager keeps each version and lets you pin one. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager keeps each version and lets you pin one.
- **B:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager keeps each version and lets you pin one.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager keeps each version and lets you pin one.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager keeps each version and lets you pin one.

### Question 58 — B

Answer: Generate the key in the application and store it beside the data. A value baked into the image travels with every copy of that image. A key stored beside the data gives an attacker both halves of the protection. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A value baked into the image travels with every copy of that image.
- **B:** Correct. A key stored beside the data gives an attacker both halves of the protection. In this case: A value baked into the image travels with every copy of that image.
- **C:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: A value baked into the image travels with every copy of that image.
- **D:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: A value baked into the image travels with every copy of that image.

### Question 59 — D

Answer: Require the metadata server header on every request. Requiring the metadata header blocks the simplest forgery. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **D:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: Requiring the metadata header blocks the simplest forgery.

### Question 60 — C

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login removes the shared key and ties the login to a live identity. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.
- **B:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.
- **C:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: OS Login removes the shared key and ties the login to a live identity.
- **D:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.

### Question 61 — B, D

Answers: Encrypt the dataset with a customer-managed key in Cloud KMS; Hold the key in Cloud External Key Manager outside Google Cloud. A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second. A customer-managed key lets the customer disable the key and stop every read of the data. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second.
- **B:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second.
- **C:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second.
- **D:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second.
- **E:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key gives the first tenant control, and Cloud EKM keeps material outside for the second.

### Question 62 — D

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key can be disabled by its owner. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **C:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **D:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key can be disabled by its owner.

### Question 63 — C

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM delegates the key material to the external manager. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM delegates the key material to the external manager.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM delegates the key material to the external manager.
- **C:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM delegates the key material to the external manager.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM delegates the key material to the external manager.

### Question 64 — A, C

Answers: Hold the key in Cloud External Key Manager outside Google Cloud; Import the wrapping key into Cloud KMS. Cloud EKM covers the external holder, and key import moves the legacy material. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Cloud EKM covers the external holder, and key import moves the legacy material.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM covers the external holder, and key import moves the legacy material.
- **C:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM covers the external holder, and key import moves the legacy material.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Cloud EKM covers the external holder, and key import moves the legacy material.
- **E:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Cloud EKM covers the external holder, and key import moves the legacy material.

### Question 65 — D

Answer: Import the wrapping key into Cloud KMS. Key import brings the existing material into KMS. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Key import brings the existing material into KMS.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Key import brings the existing material into KMS.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Key import brings the existing material into KMS.
- **D:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Key import brings the existing material into KMS.

### Question 66 — A

Answer: Set a rotation period on the key. A rotation schedule creates and tracks the versions. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: A rotation schedule creates and tracks the versions.
- **B:** Incorrect for this question. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Why the correct answer wins: A rotation schedule creates and tracks the versions.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A rotation schedule creates and tracks the versions.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: A rotation schedule creates and tracks the versions.

### Question 67 — C

Answer: Disable the key version and re-wrap the data. Disabling the version makes the protected bytes unreadable. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Disabling the version makes the protected bytes unreadable.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Disabling the version makes the protected bytes unreadable.
- **C:** Correct. In this case: Disabling the version makes the protected bytes unreadable.
- **D:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Disabling the version makes the protected bytes unreadable.

### Question 68 — A

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted in use. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted in use.
- **B:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.

### Question 69 — B

Answer: Run the pod in a Confidential GKE node pool. A Confidential GKE node pool protects each pod's memory. Confidential GKE extends in-use memory protection to each pod on the node. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential GKE node pool protects each pod's memory.
- **B:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential GKE node pool protects each pod's memory.
- **C:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential GKE node pool protects each pod's memory.
- **D:** Incorrect for this question. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Why the correct answer wins: A Confidential GKE node pool protects each pod's memory.

### Question 70 — B

Answer: Attach an object lifecycle rule that keeps the required retention. A lifecycle rule deletes on the stated schedule. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A lifecycle rule deletes on the stated schedule.
- **B:** Correct. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. In this case: A lifecycle rule deletes on the stated schedule.
- **C:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: A lifecycle rule deletes on the stated schedule.
- **D:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: A lifecycle rule deletes on the stated schedule.

### Question 71 — D, E

Answers: Add an Artifact Analysis scan to the CI pipeline; Scan the running image in production once a quarter. The build scan fails the pipeline, and the later scan re-checks what was stored. Scanning in the pipeline stops the image before it is deployed, not after. A quarterly production scan finds the vulnerable image after it has already run. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: The build scan fails the pipeline, and the later scan re-checks what was stored.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The build scan fails the pipeline, and the later scan re-checks what was stored.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: The build scan fails the pipeline, and the later scan re-checks what was stored.
- **D:** Correct. A quarterly production scan finds the vulnerable image after it has already run. In this case: The build scan fails the pipeline, and the later scan re-checks what was stored.
- **E:** Correct. Scanning in the pipeline stops the image before it is deployed, not after. In this case: The build scan fails the pipeline, and the later scan re-checks what was stored.

### Question 72 — D

Answer: Scan the running image in production once a quarter. A production scan checks the running images rather than the build output. A quarterly production scan finds the vulnerable image after it has already run. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: A production scan checks the running images rather than the build output.
- **B:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: A production scan checks the running images rather than the build output.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A production scan checks the running images rather than the build output.
- **D:** Correct. A quarterly production scan finds the vulnerable image after it has already run. In this case: A production scan checks the running images rather than the build output.

### Question 73 — B

Answer: Enforce a Binary Authorization policy that requires an attested image. Binary Authorization refuses an image without the attestation. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Binary Authorization refuses an image without the attestation.
- **B:** Correct. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. In this case: Binary Authorization refuses an image without the attestation.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Binary Authorization refuses an image without the attestation.
- **D:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: Binary Authorization refuses an image without the attestation.

### Question 74 — A

Answer: Deploy with Binary Authorization in dry-run mode only. Dry-run records the violation and admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Dry-run records the violation and admits the image.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Dry-run records the violation and admits the image.
- **C:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: Dry-run records the violation and admits the image.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Dry-run records the violation and admits the image.

### Question 75 — B

Answer: Build the base image from a hardened source with a documented baseline. A hardened baseline removes what a general-purpose image carries. A hardened baseline removes the packages and accounts that a general-purpose image ships. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **B:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline removes what a general-purpose image carries.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **D:** Incorrect for this question. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.

### Question 76 — A

Answer: Schedule patch jobs across the fleet with VM Manager. VM Manager applies and reports the patches. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: VM Manager applies and reports the patches.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: VM Manager applies and reports the patches.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: VM Manager applies and reports the patches.
- **D:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: VM Manager applies and reports the patches.

### Question 77 — C

Answer: Compare the deployed configuration with the intended state on a schedule. A scheduled comparison finds the change that bypassed the pipeline. A scheduled comparison detects the change that happened outside the pipeline. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **C:** Correct. A scheduled comparison detects the change that happened outside the pipeline. In this case: A scheduled comparison finds the change that bypassed the pipeline.
- **D:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.

### Question 78 — B

Answer: Write a custom organization policy constraint for the rule. A custom constraint blocks the change instead of reporting it. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.
- **B:** Correct. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. In this case: A custom constraint blocks the change instead of reporting it.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.
- **D:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.

### Question 79 — D, E

Answers: Enable VPC Flow Logs on the subnets; Deploy Cloud IDS on the network. Flow logs record the decisions, and Cloud IDS raises the threat finding. Flow logs record the accepted and rejected five-tuples for later analysis. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the decisions, and Cloud IDS raises the threat finding.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the decisions, and Cloud IDS raises the threat finding.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Flow logs record the decisions, and Cloud IDS raises the threat finding.
- **D:** Correct. Flow logs record the accepted and rejected five-tuples for later analysis. In this case: Flow logs record the decisions, and Cloud IDS raises the threat finding.
- **E:** Correct. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. In this case: Flow logs record the decisions, and Cloud IDS raises the threat finding.

### Question 80 — D

Answer: Mirror the production traffic to a collector with Packet Mirroring. Packet Mirroring copies the packets to a collector. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **C:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **D:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Packet Mirroring copies the packets to a collector.

### Question 81 — B

Answer: Query the logs through Log Analytics. Log Analytics makes the sink destination directly queryable. Log Analytics turns the sink destination into a queryable store for the correlation. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Log Analytics makes the sink destination directly queryable.
- **B:** Correct. Log Analytics turns the sink destination into a queryable store for the correlation. In this case: Log Analytics makes the sink destination directly queryable.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Log Analytics makes the sink destination directly queryable.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: Log Analytics makes the sink destination directly queryable.

### Question 82 — B

Answer: Route security logs to a dedicated project with its own retention. A dedicated log project keeps the evidence away from the operator. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A dedicated log project keeps the evidence away from the operator.
- **B:** Correct. In this case: A dedicated log project keeps the evidence away from the operator.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A dedicated log project keeps the evidence away from the operator.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A dedicated log project keeps the evidence away from the operator.

### Question 83 — A

Answer: Lower the log volume by disabling data access logs. Disabling the logs removes the record of who read the data. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Disabling the logs removes the record of who read the data.
- **B:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **C:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **D:** Incorrect for this question. A dedicated log project keeps the evidence away from the principals who generate it. Why the correct answer wins: Disabling the logs removes the record of who read the data.

### Question 84 — D

Answer: Read the Admin Activity audit log for the change. Admin Activity records the change and the identity. Admin Activity records the configuration change and the identity that made it, and is always on. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the change and the identity.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the change and the identity.
- **C:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the change and the identity.
- **D:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Admin Activity records the change and the identity.

### Question 85 — B

Answer: Enable Data Access audit logs for the service. Data Access records the read and must be enabled per service. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Data Access records the read and must be enabled per service.
- **B:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Data Access records the read and must be enabled per service.
- **C:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Data Access records the read and must be enabled per service.
- **D:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Data Access records the read and must be enabled per service.

### Question 86 — B, C

Answers: Create an aggregated sink at the organisation level; Export the entries to the external SIEM through Pub/Sub. An aggregated sink covers the projects, and Pub/Sub export needs no stored key. An aggregated sink includes the entries from every project beneath the node in one destination. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink covers the projects, and Pub/Sub export needs no stored key.
- **B:** Correct. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. In this case: An aggregated sink covers the projects, and Pub/Sub export needs no stored key.
- **C:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: An aggregated sink covers the projects, and Pub/Sub export needs no stored key.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: An aggregated sink covers the projects, and Pub/Sub export needs no stored key.
- **E:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink covers the projects, and Pub/Sub export needs no stored key.

### Question 87 — D

Answer: Create a sink in each project and hope nobody adds a project. A per-project sink has to be repeated for each new project. A per-project sink misses every project created after the last one was configured. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An aggregated sink includes the entries from every project beneath the node in one destination. Why the correct answer wins: A per-project sink has to be repeated for each new project.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: A per-project sink has to be repeated for each new project.
- **C:** Incorrect for this question. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Why the correct answer wins: A per-project sink has to be repeated for each new project.
- **D:** Correct. A per-project sink misses every project created after the last one was configured. In this case: A per-project sink has to be repeated for each new project.

### Question 88 — C

Answer: Review the Security Command Center findings for the project. Security Command Center collects the findings for the enabled tier. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **B:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **C:** Correct. In this case: Security Command Center collects the findings for the enabled tier.
- **D:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.

### Question 89 — A

Answer: Publish new findings to Pub/Sub for the response pipeline. A notification channel publishes the finding to the response tool. A notification channel lets the response automation react to a finding as it is created. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A notification channel lets the response automation react to a finding as it is created. In this case: A notification channel publishes the finding to the response tool.
- **B:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A notification channel publishes the finding to the response tool.
- **C:** Incorrect for this question. An unexplained closure destroys the record that the finding was ever reviewed. Why the correct answer wins: A notification channel publishes the finding to the response tool.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A notification channel publishes the finding to the response tool.

### Question 90 — B, D

Answers: Document which controls Google operates and which the customer must implement; Map each requirement to the control that satisfies it and the evidence it produces. The split assigns the layer, and the mapping ties it to the evidence. The shared responsibility split decides what the customer actually has to evidence. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The split assigns the layer, and the mapping ties it to the evidence.
- **B:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: The split assigns the layer, and the mapping ties it to the evidence.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The split assigns the layer, and the mapping ties it to the evidence.
- **D:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The split assigns the layer, and the mapping ties it to the evidence.
- **E:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The split assigns the layer, and the mapping ties it to the evidence.

### Question 91 — B

Answer: Assume Google secures every layer once the data is in the cloud. The provider secures the infrastructure, not the configuration written on top. The provider secures the infrastructure, not the configuration the customer writes on top of it. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **B:** Correct. The provider secures the infrastructure, not the configuration the customer writes on top of it. In this case: The provider secures the infrastructure, not the configuration written on top.
- **C:** Incorrect for this question. The shared responsibility split decides what the customer actually has to evidence. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.

### Question 92 — C

Answer: Create the folder as an Assured Workloads environment. Assured Workloads applies the personnel controls to the folder. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **B:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **C:** Correct. In this case: Assured Workloads applies the personnel controls to the folder.
- **D:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.

### Question 93 — D

Answer: Record the regime in a spreadsheet and configure each control by hand. A manual mapping drifts when a project is created without the same settings. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **B:** Incorrect for this question. Assured Workloads applies the personnel and location controls the regime requires to the folder. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **C:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **D:** Correct. In this case: A manual mapping drifts when a project is created without the same settings.

### Question 94 — C

Answer: Turn on Access Transparency and read its logs. Access Transparency records each operator access to content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records each operator access to content.
- **B:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records each operator access to content.
- **C:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records each operator access to content.
- **D:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records each operator access to content.

### Question 95 — C

Answer: Require Access Approval before an operator may read the content. Access Approval makes the operator wait for the decision. Access Approval turns the operator access into a request the customer must grant. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **C:** Correct. Access Approval turns the operator access into a request the customer must grant. In this case: Access Approval makes the operator wait for the decision.
- **D:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval makes the operator wait for the decision.

### Question 96 — A

Answer: Constrain the resources to the required region with a location organization policy. A location constraint blocks resources outside the permitted region. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks resources outside the permitted region.
- **B:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **C:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **D:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks resources outside the permitted region.

### Question 97 — C

Answer: Leave the default multi-region setting. An unchosen default spreads copies beyond the named country. A multi-region default places the copy outside the region the regulator named. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: An unchosen default spreads copies beyond the named country.
- **B:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: An unchosen default spreads copies beyond the named country.
- **C:** Correct. A multi-region default places the copy outside the region the regulator named. In this case: An unchosen default spreads copies beyond the named country.
- **D:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: An unchosen default spreads copies beyond the named country.

### Question 98 — D

Answer: Map each requirement to the control that satisfies it and the evidence it produces. A mapping names the control and the evidence for the clause. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **C:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **D:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: A mapping names the control and the evidence for the clause.

### Question 99 — A

Answer: Name an owner for each control. A named owner is what turns a control list into an operated control. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A named owner is what turns a control list into an operated control.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A named owner is what turns a control list into an operated control.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A named owner is what turns a control list into an operated control.
- **D:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A named owner is what turns a control list into an operated control.

### Question 100 — A

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A boundary decides which resources are in scope before testing. A written boundary decides which resources are in scope and which are out, before the audit begins. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A written boundary decides which resources are in scope and which are out, before the audit begins. In this case: A boundary decides which resources are in scope before testing.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A boundary decides which resources are in scope before testing.
