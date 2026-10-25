# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 3

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. A new studio has no directory and needs one source of identity for both its workspace and its cloud projects. What should hold the accounts?

- A. Federate the workforce to Cloud Identity and enforce it as the identity source
- B. Create a service account key and embed it in the application configuration
- C. Assign the super administrator role to a dedicated break-glass account with hardware keys
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 2. The on-premises directory must stay authoritative, and one account must always be able to recover the tenant. Which two arrangements apply? Select two.

- A. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- B. Have a team member update accounts by hand when the HR export arrives
- C. Create a service account key and embed it in the application configuration
- D. Give every platform lead the super administrator role for convenience
- E. Assign the super administrator role to a dedicated break-glass account with hardware keys

### 3. Federation is broken and no administrator can reach the console. Which account is designed for that moment?

- A. Assign the super administrator role to a dedicated break-glass account with hardware keys
- B. Give every platform lead the super administrator role for convenience
- C. Grant the role to a group and manage membership
- D. Grant the predefined role that matches the task

### 4. Contractors are removed only when their manager remembers to raise a ticket. What should replace that step?

- A. Have a team member update accounts by hand when the HR export arrives
- B. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- C. Create a service account key and embed it in the application configuration
- D. Grant the role to a group and manage membership

### 5. An administrator created a second super admin account and signs in with it every morning. What is wrong with that?

- A. Grant the predefined role that matches the task
- B. Assign the super administrator role to a dedicated break-glass account with hardware keys
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Give every platform lead the super administrator role for convenience

### 6. A logistics partner's Entra ID must open a warehouse API for one shipping season. What should be configured?

- A. Create a service account key and embed it in the application configuration
- B. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- C. Create a Cloud Identity user per contractor and issue long-lived passwords
- D. Federate the partner workforce with Workforce Identity Federation

### 7. Contractors were issued Cloud Identity passwords instead of using the provider their employer already runs. What is the weakness?

- A. Federate the partner workforce with Workforce Identity Federation
- B. Create a Cloud Identity user per contractor and issue long-lived passwords
- C. Configure Workload Identity Federation for the external workload
- D. Set the domain restricted sharing constraint on the organisation

### 8. One shared account runs three pipelines and two cron jobs, so no log line names the caller. What should be created?

- A. Create a dedicated service account per workload with only the roles it needs
- B. Run the workload as the default Compute Engine service account
- C. Grant the basic Editor role to the team
- D. Create a service account key and embed it in the application configuration

### 9. A service account was given Editor because someone was in a hurry. What should replace it?

- A. Give every platform lead the super administrator role for convenience
- B. Build a custom role containing exactly the permissions the task uses
- C. Grant the basic Editor role to the team
- D. Grant the predefined role that matches the task

### 10. A virtual machine runs with the project's default compute account and therefore holds Editor. What is the risk?

- A. Create a dedicated service account per workload with only the roles it needs
- B. Create a service account key and embed it in the application configuration
- C. Run the workload as the default Compute Engine service account
- D. Grant the role to a group and manage membership

### 11. The acting right must be limited to business hours, and no downloadable key may be issued. Which two controls apply? Select two.

- A. Set the credential as a plain environment variable in the deployment
- B. Grant the caller the Service Account Token Creator role on the target account
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Create a service account key and embed it in the application configuration
- E. Enforce a password policy with a minimum length and a reuse ban

### 12. A rotation broke production because callers had been downloading credentials by hand. What were they using?

- A. Create a service account key and embed it in the application configuration
- B. Grant the caller the Service Account Token Creator role on the target account
- C. Issue a short-lived access token through impersonation or metadata
- D. Configure Workload Identity Federation for the external workload

### 13. A token is minted for one job and stops working fifteen minutes later even if it leaks. What is it?

- A. Enforce 2-step verification for the whole organisation
- B. Issue a short-lived access token through impersonation or metadata
- C. Set the credential as a plain environment variable in the deployment
- D. Create a service account key and embed it in the application configuration

### 14. A workflow in GitHub must deploy with no secret stored in the repository. What should be configured?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Create a service account key and embed it in the application configuration
- C. Configure Workload Identity Federation for the external workload
- D. Set the credential as a plain environment variable in the deployment

### 15. A pool trusts a provider that issues tokens for hundreds of repositories. What should limit who may impersonate?

- A. Restrict the Workload Identity pool with an attribute condition on the subject
- B. Configure Workload Identity Federation for the external workload
- C. Create a service account key and embed it in the application configuration
- D. Set the domain restricted sharing constraint on the organisation

### 16. An auditor asks how a person used an account's permissions without ever holding its key. What allowed that?

- A. Set the credential as a plain environment variable in the deployment
- B. Create a service account key and embed it in the application configuration
- C. Issue a short-lived access token through impersonation or metadata
- D. Grant the caller the Service Account Token Creator role on the target account

### 17. A key was emailed to a partner so that they could act as the account. What should have been configured instead?

- A. Configure Workload Identity Federation for the external workload
- B. Issue a short-lived access token through impersonation or metadata
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Hand the caller a JSON key for the service account instead

### 18. Passwords must be strong, and one stolen password must not be enough to sign in. Which two policies apply? Select two.

- A. Let each user decide whether to enrol in 2-step verification
- B. Set a session length and reauthentication policy for the admin console
- C. Enforce 2-step verification for the whole organisation
- D. Restrict the project to the APIs it needs and review them on a schedule
- E. Enforce a password policy with a minimum length and a reuse ban

### 19. Users may decline the second factor at enrolment time. What is the consequence?

- A. Set a session length and reauthentication policy for the admin console
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Enforce 2-step verification for the whole organisation
- D. Let each user decide whether to enrol in 2-step verification

### 20. The team keeps Owner permanently to avoid waiting for approvals. What practice is that?

- A. Grant the predefined role that matches the task
- B. Grant the role through Privileged Access Manager with an approval and a time limit
- C. Grant the role to a group and manage membership
- D. Grant the privileged role permanently and review it once a year

### 21. A database administrator must hold the owner role only for a migration window. What should be used?

- A. Grant the basic Editor role to the team
- B. Grant the role to a group and manage membership
- C. Grant the role through Privileged Access Manager with an approval and a time limit
- D. Grant the privileged role permanently and review it once a year

### 22. A grant must name a resource prefix and expire at the end of the quarter. What should be added?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Grant the predefined role that matches the task
- C. Write an Access Context Manager access level and bind it to the perimeter
- D. Enforce the constraint with an organization policy

### 23. An emergency prohibition must beat an allow written on the project. What makes that work?

- A. Attach an IAM deny policy to the organisation
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Enforce the constraint with an organization policy

### 24. A policy must be written once for a business unit, and a new project must not opt out. Which two mechanisms apply? Select two.

- A. Create a sink in each project and hope nobody adds a project
- B. Have a team member update accounts by hand when the HR export arrives
- C. Create a folder per environment and attach the policy at the folder
- D. Enforce the constraint with an organization policy
- E. Ask each project owner to disable the setting

### 25. A partner address keeps appearing in resource grants. What should be enforced to stop it?

- A. Set an allUsers object ACL on the specific file
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Grant the basic Editor role to the team
- D. Set the domain restricted sharing constraint on the organisation

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. Egress to one range must be denied for every project, including the ones created later. What should be deployed?

- A. Rely on the default VPC firewall rules in each project
- B. Deploy a hierarchical firewall policy at the organisation or folder level
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Allow all egress and rely on the application to be careful

### 27. A lab needs its own port opened without a central ticket. Which rules allow that safely?

- A. Rely on the default VPC firewall rules in each project
- B. Deploy a hierarchical firewall policy at the organisation or folder level
- C. Create a service perimeter with VPC Service Controls
- D. Attach a Cloud Armor security policy to the backend service

### 28. Egress must be limited to named hosts, and the restriction must survive a project owner's edits. Which two controls apply? Select two.

- A. Filter on address and port only and allow the rest
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Allow all egress and rely on the application to be careful
- D. Deploy a hierarchical firewall policy at the organisation or folder level
- E. Enable layer 7 inspection on the firewall policy for the egress rule

### 29. Two services listen on port 443 in the same range and a rule cannot tell them apart. Why?

- A. Filter on address and port only and allow the rest
- B. Deploy Cloud IDS on the network
- C. Put Identity-Aware Proxy in front of the application
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 30. A checkout API needs per-client rate limits and a ban list at the edge. What should be configured?

- A. Add a web application firewall rule in the application framework
- B. Rely on the default VPC firewall rules in each project
- C. Attach a Cloud Armor security policy to the backend service
- D. Put Identity-Aware Proxy in front of the application

### 31. Crawler traffic must be separated from human traffic before a decision is made. What should be enabled?

- A. Terminate TLS at the load balancer with a managed certificate
- B. Add a web application firewall rule in the application framework
- C. Attach a Cloud Armor security policy to the backend service
- D. Enable Cloud Armor bot management on the policy

### 32. An internal tool must check group membership on every request. What should sit in front of it?

- A. Publish the application only through a VPN concentrator
- B. Put Identity-Aware Proxy in front of the application
- C. Deploy the instances with internal IP addresses only
- D. Attach a Cloud Armor security policy to the backend service

### 33. The team put the tool behind a VPN and considers access control done. What is missing?

- A. Attach a Cloud Armor security policy to the backend service
- B. Publish the application only through a VPN concentrator
- C. Put Identity-Aware Proxy in front of the application
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 34. Internal services need certificates from a controlled authority, and one cipher policy must cover every backend. Which two choices apply? Select two.

- A. Pass encrypted traffic straight through to the instance
- B. Terminate TLS at the load balancer with a managed certificate
- C. Filter on address and port only and allow the rest
- D. Generate a self-signed certificate on each instance
- E. Issue internal certificates from Certificate Authority Service

### 35. Each instance makes its own certificate and clients cannot validate it. What is the cause?

- A. Terminate TLS at the load balancer with a managed certificate
- B. Generate a self-signed certificate on each instance
- C. Pass encrypted traffic straight through to the instance
- D. Issue internal certificates from Certificate Authority Service

### 36. Outbound web traffic must be decrypted and inspected against an allowlist. What should carry it?

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Route the egress through Secure Web Proxy
- C. Allow all egress and rely on the application to be careful
- D. Place Cloud NAT in front of the private instances

### 37. Zone data must carry a signature that a recursive resolver can verify. What should be turned on?

- A. Use a Cloud DNS response policy to block the known-bad domain
- B. Enable Private Google Access on the subnet
- C. Route the egress through Secure Web Proxy
- D. Turn on DNSSEC for the public zone

### 38. A workload needs outbound updates and must not be reachable from the internet. Which address plan applies?

- A. Place Cloud NAT in front of the private instances
- B. Deploy the instances with internal IP addresses only
- C. Enable Private Google Access on the subnet
- D. Terminate TLS at the load balancer with a managed certificate

### 39. A project has forty APIs enabled while the application calls three. What should be reduced?

- A. Restrict the project to the APIs it needs and review them on a schedule
- B. Create a service perimeter with VPC Service Controls
- C. Enforce the constraint with an organization policy
- D. Add an IAM condition that limits the grant to a time window and a resource prefix

### 40. One team must own the network, and each tier must reach only its neighbour. Which two designs apply? Select two.

- A. Host the workload in a Shared VPC service project
- B. Give each tier its own subnet and allow only the flows between adjacent tiers
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Peer the two VPC networks and scope the firewall rules to the peer
- E. Allow all egress and rely on the application to be careful

### 41. Two VPCs need private reachability and neither team will merge its project. What should be configured?

- A. Place Cloud NAT in front of the private instances
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Peer the two VPC networks and scope the firewall rules to the peer
- D. Host the workload in a Shared VPC service project

### 42. A perimeter must cover both the warehouse and the object store. What should be created?

- A. Create a service perimeter with VPC Service Controls
- B. Rely on IAM to prevent data leaving the project
- C. Grant authorised views or dataset-level IAM rather than table reads
- D. Make the bucket public but unlisted

### 43. The perimeter broke the build because the API calls used public virtual IPs. What should the calls use instead?

- A. Enable Private Google Access on the subnet
- B. Create a service perimeter with VPC Service Controls
- C. Use restricted.googleapis.com for the API traffic
- D. Place Cloud NAT in front of the private instances

### 44. A data-centre link needs 99.99 percent and must survive one tunnel failing. What should be built?

- A. Build a single classic VPN tunnel
- B. Place Cloud NAT in front of the private instances
- C. Build an HA VPN tunnel pair with two interfaces
- D. Provision a Dedicated Interconnect with two attachments

### 45. One tunnel is the only path and every maintenance window drops the link. What is being described?

- A. Provision a Dedicated Interconnect with two attachments
- B. Place Cloud NAT in front of the private instances
- C. Build a single classic VPN tunnel
- D. Build an HA VPN tunnel pair with two interfaces

### 46. Hosts on-premises must reach Google APIs privately, and a partner service must answer on a private address. Which two services apply? Select two.

- A. Publish the service through a Private Service Connect endpoint
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Allow all egress and rely on the application to be careful
- D. Place Cloud NAT in front of the private instances
- E. Configure Private Google Access for on-premises hosts over the hybrid route

### 47. Private instances need a managed egress path with no host to patch. What should be deployed?

- A. Allow all egress and rely on the application to be careful
- B. Place Cloud NAT in front of the private instances
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Terminate TLS at the load balancer with a managed certificate

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. A scan must cover both file shares and warehouses, and the next run must produce the same hits. Which two arrangements apply? Select two.

- A. Generate the key in the application and store it beside the data
- B. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Ask the team to report which tables they believe hold personal data
- E. Replace the value with an unsalted hash

### 49. The legal team wants the same detection confidence on every scan of the same column. What should be shared?

- A. Save a Sensitive Data Protection inspect template and reuse it
- B. Ask the team to report which tables they believe hold personal data
- C. Reuse a stored de-identification template across pipelines
- D. Set the credential as a plain environment variable in the deployment

### 50. Privacy relies on a spreadsheet of tables that teams update by hand. What is the weakness?

- A. Ask the team to report which tables they believe hold personal data
- B. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Replace the value with an unsalted hash

### 51. A support agent may see that an IBAN exists on file but must not see its digits. What should be applied?

- A. Replace the value with an unsalted hash
- B. Redact the matched values with a de-identification template
- C. Apply format-preserving encryption to the card number field
- D. Replace the value with a pseudonym from a crypto key

### 52. Two analyses must join on the same customer token after de-identification. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Apply format-preserving encryption to the card number field
- C. Replace the value with an unsalted hash
- D. Replace the value with a pseudonym from a crypto key

### 53. A payment file must keep its exact length and still pass a checksum validator. What should be applied?

- A. Replace the value with a pseudonym from a crypto key
- B. Redact the matched values with a de-identification template
- C. Replace the value with an unsalted hash
- D. Apply format-preserving encryption to the card number field

### 54. The analytics team must never read the identifier column, only the aggregates. What should be granted?

- A. Grant the analyst the ability to export the whole table to a bucket
- B. Put the database password in the application config file
- C. Make the bucket public but unlisted
- D. Grant authorised views or dataset-level IAM rather than table reads

### 55. A fleet of application servers must connect to Cloud SQL without a password file. What should be enabled?

- A. Set the credential as a plain environment variable in the deployment
- B. Generate the key in the application and store it beside the data
- C. Use Cloud SQL IAM database authentication for the application
- D. Put the database password in the application config file

### 56. A database password was pasted into a deployment configuration file. Where should it move?

- A. Generate the key in the application and store it beside the data
- B. Put the database password in the application config file
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Set the credential as a plain environment variable in the deployment

### 57. A secret must be readable by one workload only and every read must be recorded. What should hold it?

- A. Put the database password in the application config file
- B. Generate the key in the application and store it beside the data
- C. Set the credential as a plain environment variable in the deployment
- D. Store the credential in Secret Manager and grant the workload the secret accessor role

### 58. The password appears in the process listing of the running container. How was it supplied?

- A. Generate the key in the application and store it beside the data
- B. Put the database password in the application config file
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Set the credential as a plain environment variable in the deployment

### 59. The metadata endpoint must reject forged requests, and interactive logins must be tied to identities. Which two controls apply? Select two.

- A. Create a service account key and embed it in the application configuration
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Deploy the instances with internal IP addresses only
- D. Require the metadata server header on every request
- E. Enable OS Login and turn off project-wide SSH keys

### 60. A project-wide key let a former engineer log in months after leaving. What would have prevented it?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Create a service account key and embed it in the application configuration
- C. Enable OS Login and turn off project-wide SSH keys
- D. Require the metadata server header on every request

### 61. Default encryption is enough for a workload and no key work is wanted. What applies?

- A. Generate the key in the application and store it beside the data
- B. Rely on Google default encryption at rest
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 62. The customer must hold the key so they can revoke their own access. What should be configured?

- A. Rely on Google default encryption at rest
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Generate the key in the application and store it beside the data

### 63. Key material must live in the customer's own hardware module. What should be used?

- A. Generate the key in the application and store it beside the data
- B. Import the wrapping key into Cloud KMS
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 64. A key from another provider must be brought under KMS control without re-encrypting everything. What should be done?

- A. Set a rotation period on the key
- B. Import the wrapping key into Cloud KMS
- C. Generate the key in the application and store it beside the data
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 65. Reads fail whenever the external key manager is unreachable. What design produces that dependency?

- A. Hold the key in Cloud External Key Manager outside Google Cloud
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Import the wrapping key into Cloud KMS
- D. Set a rotation period on the key

### 66. New data must use a fresh key version on schedule, and a suspect version must stop decrypting at once. Which two controls apply? Select two.

- A. Disable the key version and re-wrap the data
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Set a rotation period on the key
- E. Import the wrapping key into Cloud KMS

### 67. An auditor asks how key versions are tracked over the life of a dataset. What answers that?

- A. Generate the key in the application and store it beside the data
- B. Disable the key version and re-wrap the data
- C. Set a rotation period on the key
- D. Import the wrapping key into Cloud KMS

### 68. Memory must stay encrypted for a standalone virtual machine and for a pod in a shared cluster. Which two choices apply? Select two.

- A. Enable OS Login and turn off project-wide SSH keys
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Run the workload on a Confidential VM
- D. Rely on Google default encryption at rest
- E. Run the pod in a Confidential GKE node pool

### 69. An auditor asks which control covers data while it is being processed rather than stored. Which one does?

- A. Rely on Google default encryption at rest
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Run the workload on a Confidential VM
- D. Enable OS Login and turn off project-wide SSH keys

### 70. A retention obligation requires objects to be kept seven years and then removed automatically. What should be attached?

- A. Apply a retention policy with bucket lock
- B. Attach an object lifecycle rule that keeps the required retention
- C. Make the bucket public but unlisted
- D. Set an allUsers object ACL on the specific file

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A vulnerability in a base layer was discovered only after the image had been deployed. What was missing?

- A. Enforce a Binary Authorization policy that requires an attested image
- B. Let each team patch its own instances when convenient
- C. Scan the running image in production once a quarter
- D. Add an Artifact Analysis scan to the CI pipeline

### 72. A team scans images on a quarterly cycle long after they started running. What is wrong with that?

- A. Add an Artifact Analysis scan to the CI pipeline
- B. Let each team patch its own instances when convenient
- C. Deploy with Binary Authorization in dry-run mode only
- D. Scan the running image in production once a quarter

### 73. An image built on a developer laptop tried to start in the cluster. What should have stopped it?

- A. Deploy with Binary Authorization in dry-run mode only
- B. Attach a Cloud Armor security policy to the backend service
- C. Deploy the instances with internal IP addresses only
- D. Enforce a Binary Authorization policy that requires an attested image

### 74. The admission policy has been in dry-run for a year and has never blocked anything. What is the state?

- A. Enforce a Binary Authorization policy that requires an attested image
- B. Deploy Cloud IDS on the network
- C. Deploy with Binary Authorization in dry-run mode only
- D. Add an Artifact Analysis scan to the CI pipeline

### 75. Base images must be minimal, and every host must receive operating-system patches on schedule. Which two practices apply? Select two.

- A. Schedule patch jobs across the fleet with VM Manager
- B. Build the base image from a hardened source with a documented baseline
- C. Let each team patch its own instances when convenient
- D. Scan the running image in production once a quarter
- E. Compare the deployed configuration with the intended state on a schedule

### 76. Each team patches when it remembers and no fleet report exists. What is being described?

- A. Let each team patch its own instances when convenient
- B. Build the base image from a hardened source with a documented baseline
- C. Compare the deployed configuration with the intended state on a schedule
- D. Schedule patch jobs across the fleet with VM Manager

### 77. A bucket became public through a console change and nobody noticed. What should be added?

- A. Write a custom organization policy constraint for the rule
- B. Compare the deployed configuration with the intended state on a schedule
- C. Lower the log volume by disabling data access logs
- D. Deploy a Security Health Analytics custom module for the check

### 78. The same public-bucket setting returns every month after each manual fix. What should be written?

- A. Write a custom organization policy constraint for the rule
- B. Lower the log volume by disabling data access logs
- C. Deploy a Security Health Analytics custom module for the check
- D. Compare the deployed configuration with the intended state on a schedule

### 79. A quarterly report must show denied flows per subnet. What should be enabled?

- A. Lower the log volume by disabling data access logs
- B. Mirror the production traffic to a collector with Packet Mirroring
- C. Enable VPC Flow Logs on the subnets
- D. Deploy Cloud IDS on the network

### 80. A forensic team needs the bytes of a suspicious session. What should be used?

- A. Query the logs through Log Analytics
- B. Enable VPC Flow Logs on the subnets
- C. Mirror the production traffic to a collector with Packet Mirroring
- D. Deploy Cloud IDS on the network

### 81. An inline appliance must alert on a known exploit signature in east-west traffic. What should be deployed?

- A. Deploy Cloud IDS on the network
- B. Enable VPC Flow Logs on the subnets
- C. Attach a Cloud Armor security policy to the backend service
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 82. An auditor must read logs that the operations team cannot edit. What should change?

- A. Give the SIEM a service account key so it can pull the logs
- B. Lower the log volume by disabling data access logs
- C. Route security logs to a dedicated project with its own retention
- D. Create a sink in each project and hope nobody adds a project

### 83. A cost review proposes turning off data access logs for a month. What is lost?

- A. Enable Data Access audit logs for the service
- B. Route security logs to a dedicated project with its own retention
- C. Apply a retention policy with bucket lock
- D. Lower the log volume by disabling data access logs

### 84. Configuration changes must be attributable, and reads of sensitive objects must be recorded. Which two log types apply? Select two.

- A. Read the Admin Activity audit log for the change
- B. Give the SIEM a service account key so it can pull the logs
- C. Enable VPC Flow Logs on the subnets
- D. Create a log sink that routes the entries to the destination
- E. Enable Data Access audit logs for the service

### 85. An investigator asks when a service account was created and by whom. Which log answers?

- A. Read the Admin Activity audit log for the change
- B. Create a log sink that routes the entries to the destination
- C. Enable Data Access audit logs for the service
- D. Enable VPC Flow Logs on the subnets

### 86. Each project has its own sink and every new project is missed. What should be created?

- A. Create a log sink that routes the entries to the destination
- B. Create an aggregated sink at the organisation level
- C. Give the SIEM a service account key so it can pull the logs
- D. Create a sink in each project and hope nobody adds a project

### 87. The SIEM team wants a service account key so that it can pull logs forever. What is the flaw?

- A. Set the credential as a plain environment variable in the deployment
- B. Export the entries to the external SIEM through Pub/Sub
- C. Give the SIEM a service account key so it can pull the logs
- D. Lower the log volume by disabling data access logs

### 88. A new finding must reach the response tool, and every finding must have an owner. Which two practices apply? Select two.

- A. Lower the log volume by disabling data access logs
- B. Close the finding as a false positive without a comment
- C. Publish new findings to Pub/Sub for the response pipeline
- D. Name an owner for each control
- E. Review the Security Command Center findings for the project

### 89. A console must list findings from every project and detector in one view. What should be reviewed?

- A. Query the logs through Log Analytics
- B. Review the Security Command Center findings for the project
- C. Deploy a Security Health Analytics custom module for the check
- D. Compare the deployed configuration with the intended state on a schedule

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. A customer asks who encrypts the stored bytes in Cloud Storage. What answers the question?

- A. Document which controls Google operates and which the customer must implement
- B. State in the policy document that the environment is compliant
- C. Declare the whole organisation in scope for every regime
- D. Assume Google secures every layer once the data is in the cloud

### 91. A vendor claims the provider covers the customer's IAM configuration. What is wrong?

- A. State in the policy document that the environment is compliant
- B. Assume Google secures every layer once the data is in the cloud
- C. Declare the whole organisation in scope for every regime
- D. Document which controls Google operates and which the customer must implement

### 92. A defence customer requires that only cleared personnel support the environment. What should be created?

- A. Constrain the resources to the required region with a location organization policy
- B. Create the folder as an Assured Workloads environment
- C. Ask each project owner to disable the setting
- D. Record the regime in a spreadsheet and configure each control by hand

### 93. The team re-creates the regime settings by hand in every new project. What fails first?

- A. Ask each project owner to disable the setting
- B. Keep the audit evidence for the period the regime requires
- C. Create the folder as an Assured Workloads environment
- D. Record the regime in a spreadsheet and configure each control by hand

### 94. A bank needs a record of each time Google staff accessed their content. What should be enabled?

- A. Turn on Access Transparency and read its logs
- B. Enable Data Access audit logs for the service
- C. Require Access Approval before an operator may read the content
- D. Read the Admin Activity audit log for the change

### 95. Auditors insist that no Google employee may open a customer's storage without that customer saying yes first. What should be required?

- A. Require Access Approval before an operator may read the content
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Turn on Access Transparency and read its logs
- D. Create a service perimeter with VPC Service Controls

### 96. Data must stay in one country, and a new project must inherit the restriction. Which two controls apply? Select two.

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Constrain the resources to the required region with a location organization policy
- C. Enforce the constraint with an organization policy
- D. Leave the default multi-region setting
- E. Declare the whole organisation in scope for every regime

### 97. A dataset sits in a multi-region location while the contract names one country. What caused it?

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Declare the whole organisation in scope for every regime
- C. Constrain the resources to the required region with a location organization policy
- D. Leave the default multi-region setting

### 98. The auditor asks for a mapping from clause to control to evidence. What should be produced?

- A. State in the policy document that the environment is compliant
- B. Map each requirement to the control that satisfies it and the evidence it produces
- C. Declare the whole organisation in scope for every regime
- D. Assume Google secures every layer once the data is in the cloud

### 99. Evidence was deleted after two years and the audit cycle is three years long. What was missing?

- A. Name an owner for each control
- B. Keep the audit evidence for the period the regime requires
- C. State in the policy document that the environment is compliant
- D. Lower the log volume by disabling data access logs

### 100. Which resources the regime covers must be documented before the audit opens. What should be written?

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Declare the whole organisation in scope for every regime
- C. Draw the compliance boundary around the projects and services that hold the regulated data
- D. State in the policy document that the environment is compliant

---

## Answer key and explanations

### Question 1 — A

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory that both surfaces resolve against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory that both surfaces resolve against.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Cloud Identity is the directory that both surfaces resolve against.
- **C:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Cloud Identity is the directory that both surfaces resolve against.
- **D:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Cloud Identity is the directory that both surfaces resolve against.

### Question 2 — A, E

Answers: Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync; Assign the super administrator role to a dedicated break-glass account with hardware keys. GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. In this case: GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery.
- **E:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: GCDS keeps the existing directory authoritative, and a break-glass super administrator preserves recovery.

### Question 3 — A

Answer: Assign the super administrator role to a dedicated break-glass account with hardware keys. A dedicated break-glass super administrator exists for directory-level recovery. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: A dedicated break-glass super administrator exists for directory-level recovery.
- **B:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A dedicated break-glass super administrator exists for directory-level recovery.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: A dedicated break-glass super administrator exists for directory-level recovery.
- **D:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: A dedicated break-glass super administrator exists for directory-level recovery.

### Question 4 — B

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK lifecycle automation suspends the account when the source record changes. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the source record changes.
- **B:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK lifecycle automation suspends the account when the source record changes.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the source record changes.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the source record changes.

### Question 5 — D

Answer: Give every platform lead the super administrator role for convenience. Daily use of the super administrator role removes the separation that makes recovery accountable. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **B:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **C:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **D:** Correct. In this case: Daily use of the super administrator role removes the separation that makes recovery accountable.

### Question 6 — D

Answer: Federate the partner workforce with Workforce Identity Federation. Workforce Identity Federation accepts the partner provider for the season. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workforce Identity Federation accepts the partner provider for the season.
- **B:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Workforce Identity Federation accepts the partner provider for the season.
- **C:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Workforce Identity Federation accepts the partner provider for the season.
- **D:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Workforce Identity Federation accepts the partner provider for the season.

### Question 7 — B

Answer: Create a Cloud Identity user per contractor and issue long-lived passwords. A local account per contractor multiplies what must be reviewed and revoked. A local user per contractor multiplies the accounts that must be reviewed and revoked. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.
- **B:** Correct. A local user per contractor multiplies the accounts that must be reviewed and revoked. In this case: A local account per contractor multiplies what must be reviewed and revoked.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.
- **D:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: A local account per contractor multiplies what must be reviewed and revoked.

### Question 8 — A

Answer: Create a dedicated service account per workload with only the roles it needs. A dedicated account per workload makes each entry attributable. A per-workload service account bounds the blast radius and makes audit records attributable. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A dedicated account per workload makes each entry attributable.
- **B:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A dedicated account per workload makes each entry attributable.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A dedicated account per workload makes each entry attributable.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A dedicated account per workload makes each entry attributable.

### Question 9 — D

Answer: Grant the predefined role that matches the task. A predefined role carries only the permissions the task needs. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A predefined role carries only the permissions the task needs.
- **B:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: A predefined role carries only the permissions the task needs.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A predefined role carries only the permissions the task needs.
- **D:** Correct. In this case: A predefined role carries only the permissions the task needs.

### Question 10 — C

Answer: Run the workload as the default Compute Engine service account. The default account is shared, so its grants reach every workload on the project. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.
- **C:** Correct. In this case: The default account is shared, so its grants reach every workload on the project.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The default account is shared, so its grants reach every workload on the project.

### Question 11 — B, C

Answers: Add an IAM condition that limits the grant to a time window and a resource prefix; Grant the caller the Service Account Token Creator role on the target account. An IAM condition limits when the right applies, and impersonation replaces the key file. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: An IAM condition limits when the right applies, and impersonation replaces the key file.
- **B:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: An IAM condition limits when the right applies, and impersonation replaces the key file.
- **C:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An IAM condition limits when the right applies, and impersonation replaces the key file.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An IAM condition limits when the right applies, and impersonation replaces the key file.
- **E:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: An IAM condition limits when the right applies, and impersonation replaces the key file.

### Question 12 — A

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key must be replaced by hand at every rotation. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key must be replaced by hand at every rotation.
- **B:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key must be replaced by hand at every rotation.
- **C:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key must be replaced by hand at every rotation.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key must be replaced by hand at every rotation.

### Question 13 — B

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token expires on its own, so a leak has a bounded window. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: A short-lived token expires on its own, so a leak has a bounded window.
- **B:** Correct. In this case: A short-lived token expires on its own, so a leak has a bounded window.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token expires on its own, so a leak has a bounded window.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token expires on its own, so a leak has a bounded window.

### Question 14 — C

Answer: Configure Workload Identity Federation for the external workload. Workload Identity Federation exchanges the workflow's own token for Google credentials. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Workload Identity Federation exchanges the workflow's own token for Google credentials.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workload Identity Federation exchanges the workflow's own token for Google credentials.
- **C:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Workload Identity Federation exchanges the workflow's own token for Google credentials.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Workload Identity Federation exchanges the workflow's own token for Google credentials.

### Question 15 — A

Answer: Restrict the Workload Identity pool with an attribute condition on the subject. An attribute condition restricts which external identities may act. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: An attribute condition restricts which external identities may act.
- **B:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **D:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: An attribute condition restricts which external identities may act.

### Question 16 — D

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation records the person acting as the account. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation records the person acting as the account.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation records the person acting as the account.
- **C:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation records the person acting as the account.
- **D:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation records the person acting as the account.

### Question 17 — D

Answer: Hand the caller a JSON key for the service account instead. Impersonation grants the acting right without exporting a credential. A handed-out key cannot be scoped to one action and outlives the task that needed it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: Impersonation grants the acting right without exporting a credential.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation grants the acting right without exporting a credential.
- **C:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: Impersonation grants the acting right without exporting a credential.
- **D:** Correct. A handed-out key cannot be scoped to one action and outlives the task that needed it. In this case: Impersonation grants the acting right without exporting a credential.

### Question 18 — C, E

Answers: Enforce a password policy with a minimum length and a reuse ban; Enforce 2-step verification for the whole organisation. A password policy raises the guessing cost, and enforced 2-step verification removes the single factor. A password policy raises the cost of credential guessing without depending on the user to choose well. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A password policy raises the guessing cost, and enforced 2-step verification removes the single factor.
- **B:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: A password policy raises the guessing cost, and enforced 2-step verification removes the single factor.
- **C:** Correct. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. In this case: A password policy raises the guessing cost, and enforced 2-step verification removes the single factor.
- **D:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: A password policy raises the guessing cost, and enforced 2-step verification removes the single factor.
- **E:** Correct. A password policy raises the cost of credential guessing without depending on the user to choose well. In this case: A password policy raises the guessing cost, and enforced 2-step verification removes the single factor.

### Question 19 — D

Answer: Let each user decide whether to enrol in 2-step verification. Optional enrolment leaves the accounts that need it most without a second factor. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: Optional enrolment leaves the accounts that need it most without a second factor.
- **B:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Optional enrolment leaves the accounts that need it most without a second factor.
- **C:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: Optional enrolment leaves the accounts that need it most without a second factor.
- **D:** Correct. In this case: Optional enrolment leaves the accounts that need it most without a second factor.

### Question 20 — D

Answer: Grant the privileged role permanently and review it once a year. Standing privilege is live every hour of the year, including the unattended ones. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Standing privilege is live every hour of the year, including the unattended ones.
- **B:** Incorrect for this question. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Why the correct answer wins: Standing privilege is live every hour of the year, including the unattended ones.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Standing privilege is live every hour of the year, including the unattended ones.
- **D:** Correct. Permanent privilege is live for every hour of the year, including the hours nobody is watching. In this case: Standing privilege is live every hour of the year, including the unattended ones.

### Question 21 — C

Answer: Grant the role through Privileged Access Manager with an approval and a time limit. Privileged Access Manager issues a temporary approved grant. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Privileged Access Manager issues a temporary approved grant.
- **B:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager issues a temporary approved grant.
- **C:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Privileged Access Manager issues a temporary approved grant.
- **D:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager issues a temporary approved grant.

### Question 22 — A

Answer: Add an IAM condition that limits the grant to a time window and a resource prefix. An IAM condition narrows the grant to the stated circumstance. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An IAM condition narrows the grant to the stated circumstance.
- **B:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: An IAM condition narrows the grant to the stated circumstance.
- **C:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: An IAM condition narrows the grant to the stated circumstance.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: An IAM condition narrows the grant to the stated circumstance.

### Question 23 — A

Answer: Attach an IAM deny policy to the organisation. A deny policy overrides every allow beneath it. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. In this case: A deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: A deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A deny policy overrides every allow beneath it.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: A deny policy overrides every allow beneath it.

### Question 24 — C, D

Answers: Create a folder per environment and attach the policy at the folder; Enforce the constraint with an organization policy. A folder attachment covers the unit, and the organization policy binds every project inside it. A folder boundary means one attachment covers every current and future project inside it. An organization policy applies to every project beneath it, so a new project cannot opt out. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A folder attachment covers the unit, and the organization policy binds every project inside it.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A folder attachment covers the unit, and the organization policy binds every project inside it.
- **C:** Correct. A folder boundary means one attachment covers every current and future project inside it. In this case: A folder attachment covers the unit, and the organization policy binds every project inside it.
- **D:** Correct. An organization policy applies to every project beneath it, so a new project cannot opt out. In this case: A folder attachment covers the unit, and the organization policy binds every project inside it.
- **E:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A folder attachment covers the unit, and the organization policy binds every project inside it.

### Question 25 — D

Answer: Set the domain restricted sharing constraint on the organisation. Domain restricted sharing refuses a grant that names an outside identity. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Domain restricted sharing refuses a grant that names an outside identity.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Domain restricted sharing refuses a grant that names an outside identity.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Domain restricted sharing refuses a grant that names an outside identity.
- **D:** Correct. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. In this case: Domain restricted sharing refuses a grant that names an outside identity.

### Question 26 — B

Answer: Deploy a hierarchical firewall policy at the organisation or folder level. A hierarchical policy applies below the node and is evaluated first. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: A hierarchical policy applies below the node and is evaluated first.
- **B:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: A hierarchical policy applies below the node and is evaluated first.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: A hierarchical policy applies below the node and is evaluated first.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A hierarchical policy applies below the node and is evaluated first.

### Question 27 — A

Answer: Rely on the default VPC firewall rules in each project. Project rules let the owner tune the environment inside the hierarchy above. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Project-level rules are editable by the project owner and are evaluated after the hierarchy. In this case: Project rules let the owner tune the environment inside the hierarchy above.
- **B:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: Project rules let the owner tune the environment inside the hierarchy above.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Project rules let the owner tune the environment inside the hierarchy above.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Project rules let the owner tune the environment inside the hierarchy above.

### Question 28 — D, E

Answers: Enable layer 7 inspection on the firewall policy for the egress rule; Deploy a hierarchical firewall policy at the organisation or folder level. Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project.
- **D:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project.
- **E:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the host name, and the hierarchical policy keeps the deny above the project.

### Question 29 — A

Answer: Filter on address and port only and allow the rest. A layer 4 rule filters on address and port only. A layer 4 rule cannot see the destination host name inside an allowed connection. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A layer 4 rule cannot see the destination host name inside an allowed connection. In this case: A layer 4 rule filters on address and port only.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **C:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A layer 4 rule filters on address and port only.

### Question 30 — C

Answer: Attach a Cloud Armor security policy to the backend service. Cloud Armor enforces the rate limit before the request reaches the backend. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Cloud Armor enforces the rate limit before the request reaches the backend.
- **B:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Cloud Armor enforces the rate limit before the request reaches the backend.
- **C:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: Cloud Armor enforces the rate limit before the request reaches the backend.
- **D:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Cloud Armor enforces the rate limit before the request reaches the backend.

### Question 31 — D

Answer: Enable Cloud Armor bot management on the policy. Bot management scores each request so a rule can separate the automation. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Bot management scores each request so a rule can separate the automation.
- **B:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Bot management scores each request so a rule can separate the automation.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Bot management scores each request so a rule can separate the automation.
- **D:** Correct. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. In this case: Bot management scores each request so a rule can separate the automation.

### Question 32 — B

Answer: Put Identity-Aware Proxy in front of the application. IAP authorises each request against IAM. IAP authenticates and authorises each request against IAM before it reaches the backend. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP authorises each request against IAM.
- **B:** Correct. IAP authenticates and authorises each request against IAM before it reaches the backend. In this case: IAP authorises each request against IAM.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: IAP authorises each request against IAM.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP authorises each request against IAM.

### Question 33 — B

Answer: Publish the application only through a VPN concentrator. A VPN authenticates the tunnel and not the individual request. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **B:** Correct. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. In this case: A VPN authenticates the tunnel and not the individual request.
- **C:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.

### Question 34 — B, E

Answers: Issue internal certificates from Certificate Authority Service; Terminate TLS at the load balancer with a managed certificate. Certificate Authority Service issues the certificates, and the load balancer terminates them centrally. Certificate Authority Service issues and revokes private certificates with an auditable authority. Terminating at the load balancer gives one managed certificate and a single policy point. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: Certificate Authority Service issues the certificates, and the load balancer terminates them centrally.
- **B:** Correct. Terminating at the load balancer gives one managed certificate and a single policy point. In this case: Certificate Authority Service issues the certificates, and the load balancer terminates them centrally.
- **C:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Certificate Authority Service issues the certificates, and the load balancer terminates them centrally.
- **D:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues the certificates, and the load balancer terminates them centrally.
- **E:** Correct. Certificate Authority Service issues and revokes private certificates with an auditable authority. In this case: Certificate Authority Service issues the certificates, and the load balancer terminates them centrally.

### Question 35 — B

Answer: Generate a self-signed certificate on each instance. A self-signed certificate cannot be validated by a client with no prior trust. Self-signed certificates cannot be validated by a client that has no prior trust in them. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: A self-signed certificate cannot be validated by a client with no prior trust.
- **B:** Correct. Self-signed certificates cannot be validated by a client that has no prior trust in them. In this case: A self-signed certificate cannot be validated by a client with no prior trust.
- **C:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: A self-signed certificate cannot be validated by a client with no prior trust.
- **D:** Incorrect for this question. Certificate Authority Service issues and revokes private certificates with an auditable authority. Why the correct answer wins: A self-signed certificate cannot be validated by a client with no prior trust.

### Question 36 — B

Answer: Route the egress through Secure Web Proxy. Secure Web Proxy inspects and allowlists the outbound web traffic. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Secure Web Proxy inspects and allowlists the outbound web traffic.
- **B:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: Secure Web Proxy inspects and allowlists the outbound web traffic.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Secure Web Proxy inspects and allowlists the outbound web traffic.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Secure Web Proxy inspects and allowlists the outbound web traffic.

### Question 37 — D

Answer: Turn on DNSSEC for the public zone. DNSSEC signs the answers so a resolver can detect forgery. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A response policy overrides resolution for named domains inside the network. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.
- **B:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.
- **C:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.
- **D:** Correct. In this case: DNSSEC signs the answers so a resolver can detect forgery.

### Question 38 — B

Answer: Deploy the instances with internal IP addresses only. An internal-only address keeps the workload unreachable inbound. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An internal-only address keeps the workload unreachable inbound.
- **B:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal-only address keeps the workload unreachable inbound.
- **C:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: An internal-only address keeps the workload unreachable inbound.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: An internal-only address keeps the workload unreachable inbound.

### Question 39 — A

Answer: Restrict the project to the APIs it needs and review them on a schedule. Disabling unused APIs removes an attack surface nothing needs. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: Disabling unused APIs removes an attack surface nothing needs.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **C:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **D:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.

### Question 40 — A, B

Answers: Host the workload in a Shared VPC service project; Give each tier its own subnet and allow only the flows between adjacent tiers. Shared VPC centralises the network, and tier subnets express the allowed flows. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. In this case: Shared VPC centralises the network, and tier subnets express the allowed flows.
- **B:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Shared VPC centralises the network, and tier subnets express the allowed flows.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Shared VPC centralises the network, and tier subnets express the allowed flows.
- **D:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Shared VPC centralises the network, and tier subnets express the allowed flows.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Shared VPC centralises the network, and tier subnets express the allowed flows.

### Question 41 — C

Answer: Peer the two VPC networks and scope the firewall rules to the peer. Peering connects the networks while each team keeps its own project. Peering gives private reachability while firewall rules still decide which flows are allowed. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Peering connects the networks while each team keeps its own project.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Peering connects the networks while each team keeps its own project.
- **C:** Correct. Peering gives private reachability while firewall rules still decide which flows are allowed. In this case: Peering connects the networks while each team keeps its own project.
- **D:** Incorrect for this question. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Why the correct answer wins: Peering connects the networks while each team keeps its own project.

### Question 42 — A

Answer: Create a service perimeter with VPC Service Controls. A service perimeter names the services it protects and blocks access from outside. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: A service perimeter names the services it protects and blocks access from outside.
- **B:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: A service perimeter names the services it protects and blocks access from outside.
- **C:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: A service perimeter names the services it protects and blocks access from outside.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A service perimeter names the services it protects and blocks access from outside.

### Question 43 — C

Answer: Use restricted.googleapis.com for the API traffic. Restricted virtual IPs keep the API path inside the boundary. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.
- **C:** Correct. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. In this case: Restricted virtual IPs keep the API path inside the boundary.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.

### Question 44 — C

Answer: Build an HA VPN tunnel pair with two interfaces. An HA VPN pair provides two interfaces and the published availability. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: An HA VPN pair provides two interfaces and the published availability.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An HA VPN pair provides two interfaces and the published availability.
- **C:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: An HA VPN pair provides two interfaces and the published availability.
- **D:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: An HA VPN pair provides two interfaces and the published availability.

### Question 45 — C

Answer: Build a single classic VPN tunnel. A single tunnel has no redundancy for a maintenance event. A single tunnel has no redundancy, so one maintenance window drops the path. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: A single tunnel has no redundancy for a maintenance event.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: A single tunnel has no redundancy for a maintenance event.
- **C:** Correct. A single tunnel has no redundancy, so one maintenance window drops the path. In this case: A single tunnel has no redundancy for a maintenance event.
- **D:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: A single tunnel has no redundancy for a maintenance event.

### Question 46 — A, E

Answers: Configure Private Google Access for on-premises hosts over the hybrid route; Publish the service through a Private Service Connect endpoint. The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. In this case: The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner.
- **E:** Correct. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. In this case: The on-premises variant of Private Google Access covers the APIs, and a Private Service Connect endpoint covers the partner.

### Question 47 — B

Answer: Place Cloud NAT in front of the private instances. Cloud NAT is managed and removes the host from the path. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT is managed and removes the host from the path.
- **B:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT is managed and removes the host from the path.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT is managed and removes the host from the path.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT is managed and removes the host from the path.

### Question 48 — B, C

Answers: Run a Sensitive Data Protection discovery scan over the storage and warehouse; Save a Sensitive Data Protection inspect template and reuse it. Discovery covers the estate, and a saved template makes the hits repeatable. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Discovery covers the estate, and a saved template makes the hits repeatable.
- **B:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: Discovery covers the estate, and a saved template makes the hits repeatable.
- **C:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: Discovery covers the estate, and a saved template makes the hits repeatable.
- **D:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: Discovery covers the estate, and a saved template makes the hits repeatable.
- **E:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Discovery covers the estate, and a saved template makes the hits repeatable.

### Question 49 — A

Answer: Save a Sensitive Data Protection inspect template and reuse it. A saved inspect template keeps the detection rules identical. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A saved inspect template keeps the detection rules identical.
- **B:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A saved inspect template keeps the detection rules identical.
- **C:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A saved inspect template keeps the detection rules identical.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A saved inspect template keeps the detection rules identical.

### Question 50 — A

Answer: Ask the team to report which tables they believe hold personal data. A self-reported inventory misses the tables nobody remembered. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A self-reported inventory misses the tables nobody remembered.
- **B:** Incorrect for this question. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.
- **C:** Incorrect for this question. A saved template keeps the detection rules identical across scans, so results stay comparable. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.

### Question 51 — B

Answer: Redact the matched values with a de-identification template. Redaction replaces the matched value and keeps the field shape. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Redaction replaces the matched value and keeps the field shape.
- **B:** Correct. In this case: Redaction replaces the matched value and keeps the field shape.
- **C:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: Redaction replaces the matched value and keeps the field shape.
- **D:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Redaction replaces the matched value and keeps the field shape.

### Question 52 — D

Answer: Replace the value with a pseudonym from a crypto key. A pseudonym keeps a stable token so the records join. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: A pseudonym keeps a stable token so the records join.
- **B:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: A pseudonym keeps a stable token so the records join.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A pseudonym keeps a stable token so the records join.
- **D:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: A pseudonym keeps a stable token so the records join.

### Question 53 — D

Answer: Apply format-preserving encryption to the card number field. Format-preserving encryption keeps the type and the length. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **B:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **D:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: Format-preserving encryption keeps the type and the length.

### Question 54 — D

Answer: Grant authorised views or dataset-level IAM rather than table reads. Authorised views expose the aggregate and keep the column unreadable. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Authorised views expose the aggregate and keep the column unreadable.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Authorised views expose the aggregate and keep the column unreadable.
- **C:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Authorised views expose the aggregate and keep the column unreadable.
- **D:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Authorised views expose the aggregate and keep the column unreadable.

### Question 55 — C

Answer: Use Cloud SQL IAM database authentication for the application. IAM database authentication ties each connection to an identity. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: IAM database authentication ties each connection to an identity.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: IAM database authentication ties each connection to an identity.
- **C:** Correct. In this case: IAM database authentication ties each connection to an identity.
- **D:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: IAM database authentication ties each connection to an identity.

### Question 56 — C

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager keeps the value out of the deployment and audits each read. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager keeps the value out of the deployment and audits each read.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager keeps the value out of the deployment and audits each read.
- **C:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager keeps the value out of the deployment and audits each read.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager keeps the value out of the deployment and audits each read.

### Question 57 — D

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager versions the value and audits each access. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager versions the value and audits each access.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager versions the value and audits each access.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager versions the value and audits each access.
- **D:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager versions the value and audits each access.

### Question 58 — D

Answer: Set the credential as a plain environment variable in the deployment. An environment variable is visible in the process listing. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: An environment variable is visible in the process listing.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: An environment variable is visible in the process listing.
- **C:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: An environment variable is visible in the process listing.
- **D:** Correct. In this case: An environment variable is visible in the process listing.

### Question 59 — D, E

Answers: Require the metadata server header on every request; Enable OS Login and turn off project-wide SSH keys. The metadata header requirement blocks the forgery, and OS Login ties each login to an identity. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The metadata header requirement blocks the forgery, and OS Login ties each login to an identity.
- **B:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: The metadata header requirement blocks the forgery, and OS Login ties each login to an identity.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: The metadata header requirement blocks the forgery, and OS Login ties each login to an identity.
- **D:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: The metadata header requirement blocks the forgery, and OS Login ties each login to an identity.
- **E:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: The metadata header requirement blocks the forgery, and OS Login ties each login to an identity.

### Question 60 — C

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login removes the shared key and ties the login to a live identity. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.
- **C:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: OS Login removes the shared key and ties the login to a live identity.
- **D:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login removes the shared key and ties the login to a live identity.

### Question 61 — B

Answer: Rely on Google default encryption at rest. Default encryption protects the bytes at rest with no customer key work. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Default encryption protects the bytes at rest with no customer key work.
- **B:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: Default encryption protects the bytes at rest with no customer key work.
- **C:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Default encryption protects the bytes at rest with no customer key work.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Default encryption protects the bytes at rest with no customer key work.

### Question 62 — C

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key is held and disabled by the customer. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key is held and disabled by the customer.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key is held and disabled by the customer.
- **C:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key is held and disabled by the customer.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key is held and disabled by the customer.

### Question 63 — C

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM keeps the material with the external key manager. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM keeps the material with the external key manager.
- **B:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM keeps the material with the external key manager.
- **C:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM keeps the material with the external key manager.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM keeps the material with the external key manager.

### Question 64 — B

Answer: Import the wrapping key into Cloud KMS. Key import brings the existing material into KMS. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Key import brings the existing material into KMS.
- **B:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Key import brings the existing material into KMS.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Key import brings the existing material into KMS.
- **D:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Key import brings the existing material into KMS.

### Question 65 — A

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM makes the external key manager part of the read path. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM makes the external key manager part of the read path.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM makes the external key manager part of the read path.
- **C:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM makes the external key manager part of the read path.
- **D:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Cloud EKM makes the external key manager part of the read path.

### Question 66 — A, D

Answers: Set a rotation period on the key; Disable the key version and re-wrap the data. Rotation issues the new versions, and disabling the version stops the decryption. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. In this case: Rotation issues the new versions, and disabling the version stops the decryption.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Rotation issues the new versions, and disabling the version stops the decryption.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Rotation issues the new versions, and disabling the version stops the decryption.
- **D:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: Rotation issues the new versions, and disabling the version stops the decryption.
- **E:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Rotation issues the new versions, and disabling the version stops the decryption.

### Question 67 — C

Answer: Set a rotation period on the key. A rotation period creates and tracks the versions on schedule. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A rotation period creates and tracks the versions on schedule.
- **B:** Incorrect for this question. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Why the correct answer wins: A rotation period creates and tracks the versions on schedule.
- **C:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: A rotation period creates and tracks the versions on schedule.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: A rotation period creates and tracks the versions on schedule.

### Question 68 — C, E

Answers: Run the workload on a Confidential VM; Run the pod in a Confidential GKE node pool. A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Confidential GKE extends in-use memory protection to each pod on the node. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod.
- **C:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod.
- **E:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pod.

### Question 69 — C

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted while the workload runs. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted while the workload runs.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted while the workload runs.
- **C:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted while the workload runs.
- **D:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM keeps memory encrypted while the workload runs.

### Question 70 — B

Answer: Attach an object lifecycle rule that keeps the required retention. A lifecycle rule keeps and deletes objects on the stated schedule. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: A lifecycle rule keeps and deletes objects on the stated schedule.
- **B:** Correct. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. In this case: A lifecycle rule keeps and deletes objects on the stated schedule.
- **C:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A lifecycle rule keeps and deletes objects on the stated schedule.
- **D:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: A lifecycle rule keeps and deletes objects on the stated schedule.

### Question 71 — D

Answer: Add an Artifact Analysis scan to the CI pipeline. Pipeline scanning blocks the image before deployment. Scanning in the pipeline stops the image before it is deployed, not after. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Pipeline scanning blocks the image before deployment.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: Pipeline scanning blocks the image before deployment.
- **C:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Pipeline scanning blocks the image before deployment.
- **D:** Correct. Scanning in the pipeline stops the image before it is deployed, not after. In this case: Pipeline scanning blocks the image before deployment.

### Question 72 — D

Answer: Scan the running image in production once a quarter. A quarterly production scan finds the vulnerable image far too late. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **C:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **D:** Correct. In this case: A quarterly production scan finds the vulnerable image far too late.

### Question 73 — D

Answer: Enforce a Binary Authorization policy that requires an attested image. Binary Authorization refuses an image without the required attestation. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.
- **D:** Correct. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. In this case: Binary Authorization refuses an image without the required attestation.

### Question 74 — C

Answer: Deploy with Binary Authorization in dry-run mode only. Dry-run records the violation and still admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **C:** Correct. In this case: Dry-run records the violation and still admits the image.
- **D:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: Dry-run records the violation and still admits the image.

### Question 75 — A, B

Answers: Build the base image from a hardened source with a documented baseline; Schedule patch jobs across the fleet with VM Manager. A hardened baseline trims the image, and VM Manager patches the fleet. A hardened baseline removes the packages and accounts that a general-purpose image ships. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: A hardened baseline trims the image, and VM Manager patches the fleet.
- **B:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline trims the image, and VM Manager patches the fleet.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline trims the image, and VM Manager patches the fleet.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline trims the image, and VM Manager patches the fleet.
- **E:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A hardened baseline trims the image, and VM Manager patches the fleet.

### Question 76 — A

Answer: Let each team patch its own instances when convenient. An unmanaged schedule leaves hosts at different levels with no fleet view. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **B:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **D:** Incorrect for this question. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.

### Question 77 — B

Answer: Compare the deployed configuration with the intended state on a schedule. A scheduled comparison finds the change that bypassed the pipeline. A scheduled comparison detects the change that happened outside the pipeline. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **B:** Correct. A scheduled comparison detects the change that happened outside the pipeline. In this case: A scheduled comparison finds the change that bypassed the pipeline.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **D:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.

### Question 78 — A

Answer: Write a custom organization policy constraint for the rule. A custom constraint blocks the change instead of reporting it. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. In this case: A custom constraint blocks the change instead of reporting it.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.
- **C:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom constraint blocks the change instead of reporting it.

### Question 79 — C

Answer: Enable VPC Flow Logs on the subnets. Flow logs record the accepted and rejected five-tuples. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **B:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **C:** Correct. In this case: Flow logs record the accepted and rejected five-tuples.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.

### Question 80 — C

Answer: Mirror the production traffic to a collector with Packet Mirroring. Packet Mirroring copies the packets to a collector. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **C:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Packet Mirroring copies the packets to a collector.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Packet Mirroring copies the packets to a collector.

### Question 81 — A

Answer: Deploy Cloud IDS on the network. Cloud IDS inspects the traffic and raises the finding. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Cloud IDS inspects the traffic and raises the finding.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.

### Question 82 — C

Answer: Route security logs to a dedicated project with its own retention. A dedicated log project keeps the evidence away from that team. A dedicated log project keeps the evidence away from the principals who generate it. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.
- **C:** Correct. A dedicated log project keeps the evidence away from the principals who generate it. In this case: A dedicated log project keeps the evidence away from that team.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.

### Question 83 — D

Answer: Lower the log volume by disabling data access logs. Disabling the logs removes the record of who read the data. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **B:** Incorrect for this question. A dedicated log project keeps the evidence away from the principals who generate it. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **C:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **D:** Correct. In this case: Disabling the logs removes the record of who read the data.

### Question 84 — A, E

Answers: Read the Admin Activity audit log for the change; Enable Data Access audit logs for the service. Admin Activity records the change, and Data Access records the read. Admin Activity records the configuration change and the identity that made it, and is always on. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Admin Activity records the change, and Data Access records the read.
- **B:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **C:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **D:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **E:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Admin Activity records the change, and Data Access records the read.

### Question 85 — A

Answer: Read the Admin Activity audit log for the change. Admin Activity records the creation and the identity. Admin Activity records the configuration change and the identity that made it, and is always on. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Admin Activity records the creation and the identity.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the creation and the identity.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the creation and the identity.
- **D:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the creation and the identity.

### Question 86 — B

Answer: Create an aggregated sink at the organisation level. An aggregated sink covers every project beneath the node. An aggregated sink includes the entries from every project beneath the node in one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **B:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: An aggregated sink covers every project beneath the node.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink covers every project beneath the node.

### Question 87 — C

Answer: Give the SIEM a service account key so it can pull the logs. A pulled key lives in a third party and cannot be narrowed to one destination. A pulled key sits in a third-party system and cannot be narrowed to one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **B:** Incorrect for this question. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **C:** Correct. A pulled key sits in a third-party system and cannot be narrowed to one destination. In this case: A pulled key lives in a third party and cannot be narrowed to one destination.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.

### Question 88 — C, D

Answers: Publish new findings to Pub/Sub for the response pipeline; Name an owner for each control. A notification channel feeds the tool, and a named owner prevents a silent closure. A notification channel lets the response automation react to a finding as it is created. A named owner is what turns a control list into something that is actually operated. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A notification channel feeds the tool, and a named owner prevents a silent closure.
- **B:** Incorrect for this question. An unexplained closure destroys the record that the finding was ever reviewed. Why the correct answer wins: A notification channel feeds the tool, and a named owner prevents a silent closure.
- **C:** Correct. A notification channel lets the response automation react to a finding as it is created. In this case: A notification channel feeds the tool, and a named owner prevents a silent closure.
- **D:** Correct. A named owner is what turns a control list into something that is actually operated. In this case: A notification channel feeds the tool, and a named owner prevents a silent closure.
- **E:** Incorrect for this question. Security Command Center collects the findings from the detectors that are enabled for the tier. Why the correct answer wins: A notification channel feeds the tool, and a named owner prevents a silent closure.

### Question 89 — B

Answer: Review the Security Command Center findings for the project. Security Command Center collects the findings for the enabled tier. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **B:** Correct. In this case: Security Command Center collects the findings for the enabled tier.
- **C:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.

### Question 90 — A

Answer: Document which controls Google operates and which the customer must implement. The shared responsibility split assigns the storage layer controls. The shared responsibility split decides what the customer actually has to evidence. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The shared responsibility split assigns the storage layer controls.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The shared responsibility split assigns the storage layer controls.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The shared responsibility split assigns the storage layer controls.
- **D:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The shared responsibility split assigns the storage layer controls.

### Question 91 — B

Answer: Assume Google secures every layer once the data is in the cloud. The provider secures the infrastructure, not the configuration written on top. The provider secures the infrastructure, not the configuration the customer writes on top of it. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **B:** Correct. The provider secures the infrastructure, not the configuration the customer writes on top of it. In this case: The provider secures the infrastructure, not the configuration written on top.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **D:** Incorrect for this question. The shared responsibility split decides what the customer actually has to evidence. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.

### Question 92 — B

Answer: Create the folder as an Assured Workloads environment. Assured Workloads applies the personnel controls to the folder. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **B:** Correct. In this case: Assured Workloads applies the personnel controls to the folder.
- **C:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.

### Question 93 — D

Answer: Record the regime in a spreadsheet and configure each control by hand. A manual mapping drifts when a project is created without the same settings. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **B:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **C:** Incorrect for this question. Assured Workloads applies the personnel and location controls the regime requires to the folder. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **D:** Correct. In this case: A manual mapping drifts when a project is created without the same settings.

### Question 94 — A

Answer: Turn on Access Transparency and read its logs. Access Transparency records operator access to content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records operator access to content.
- **B:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records operator access to content.
- **C:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records operator access to content.
- **D:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records operator access to content.

### Question 95 — A

Answer: Require Access Approval before an operator may read the content. Access Approval makes the operator wait for a customer decision. Access Approval turns the operator access into a request the customer must grant. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Access Approval turns the operator access into a request the customer must grant. In this case: Access Approval makes the operator wait for a customer decision.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval makes the operator wait for a customer decision.
- **C:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval makes the operator wait for a customer decision.
- **D:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval makes the operator wait for a customer decision.

### Question 96 — B, C

Answers: Constrain the resources to the required region with a location organization policy; Enforce the constraint with an organization policy. A location constraint blocks other regions, and an organization policy binds new projects. A location constraint blocks the resource from being created outside the permitted region. An organization policy applies to every project beneath it, so a new project cannot opt out. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks other regions, and an organization policy binds new projects.
- **B:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks other regions, and an organization policy binds new projects.
- **C:** Correct. An organization policy applies to every project beneath it, so a new project cannot opt out. In this case: A location constraint blocks other regions, and an organization policy binds new projects.
- **D:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks other regions, and an organization policy binds new projects.
- **E:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks other regions, and an organization policy binds new projects.

### Question 97 — D

Answer: Leave the default multi-region setting. A multi-region default places a copy outside the named region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **C:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **D:** Correct. In this case: A multi-region default places a copy outside the named region.

### Question 98 — B

Answer: Map each requirement to the control that satisfies it and the evidence it produces. A mapping names the control and where its evidence lives. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A mapping names the control and where its evidence lives.
- **B:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: A mapping names the control and where its evidence lives.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A mapping names the control and where its evidence lives.
- **D:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: A mapping names the control and where its evidence lives.

### Question 99 — B

Answer: Keep the audit evidence for the period the regime requires. A retention period for evidence is part of the control. A retention period for evidence is itself a control, because an expired record proves nothing. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A named owner is what turns a control list into something that is actually operated. Why the correct answer wins: A retention period for evidence is part of the control.
- **B:** Correct. A retention period for evidence is itself a control, because an expired record proves nothing. In this case: A retention period for evidence is part of the control.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A retention period for evidence is part of the control.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A retention period for evidence is part of the control.

### Question 100 — C

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A boundary decides which resources are in scope before testing. A written boundary decides which resources are in scope and which are out, before the audit begins. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **C:** Correct. A written boundary decides which resources are in scope and which are out, before the audit begins. In this case: A boundary decides which resources are in scope before testing.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A boundary decides which resources are in scope before testing.
