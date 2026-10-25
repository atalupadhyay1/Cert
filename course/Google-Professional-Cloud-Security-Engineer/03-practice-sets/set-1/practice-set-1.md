# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 1

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. Retail and wholesale divisions must lose access the moment a person leaves, from one directory of record. What should hold identity?

- A. Create a service account key and embed it in the application configuration
- B. Have a team member update accounts by hand when the HR export arrives
- C. Federate the workforce to Cloud Identity and enforce it as the identity source
- D. Give every platform lead the super administrator role for convenience

### 2. The company keeps an on-premises Active Directory and wants Google Cloud to follow it hourly. What should be scheduled?

- A. Enable Private Google Access on the subnet
- B. Set the credential as a plain environment variable in the deployment
- C. Use a Cloud DNS response policy to block the known-bad domain
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 3. One identity provider must prove the password while Google Cloud still authorises, and directory recovery must survive a broken federation. Which two arrangements apply? Select two.

- A. Run the workload as the default Compute Engine service account
- B. Create a service account key and embed it in the application configuration
- C. Have a team member update accounts by hand when the HR export arrives
- D. Assign the super administrator role to a dedicated break-glass account with hardware keys
- E. Configure single sign-on with a third-party identity provider over SAML

### 4. Four hundred joiners a month arrive from the HR system and access must not survive a transfer. What should be automated?

- A. Have a team member update accounts by hand when the HR export arrives
- B. Create a service account key and embed it in the application configuration
- C. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- D. Give every platform lead the super administrator role for convenience

### 5. A directory lockout needs one account that can always sign in and is used for nothing else. What should exist?

- A. Grant the predefined role that matches the task
- B. Assign the super administrator role to a dedicated break-glass account with hardware keys
- C. Give every platform lead the super administrator role for convenience
- D. Grant the role to a group and manage membership

### 6. An acquired agency must use its own identity provider for a six-month project with no new Google accounts. What should be configured?

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Federate the partner workforce with Workforce Identity Federation
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Create a service account key and embed it in the application configuration

### 7. Contractors keep their own directory, and their grants must never name an address outside the acquired domain. Which two controls apply? Select two.

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Set the domain restricted sharing constraint on the organisation
- C. Federate the partner workforce with Workforce Identity Federation
- D. Create a service account key and embed it in the application configuration
- E. Run the workload as the default Compute Engine service account

### 8. Six batch jobs share one project and an audit must name which job read a table. What should be changed?

- A. Grant the basic Editor role to the team
- B. Run the workload as the default Compute Engine service account
- C. Create a service account key and embed it in the application configuration
- D. Create a dedicated service account per workload with only the roles it needs

### 9. A new project inherits an account that every other workload on the project already uses. What risk does that create?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Grant the role to a group and manage membership
- C. Create a dedicated service account per workload with only the roles it needs
- D. Run the workload as the default Compute Engine service account

### 10. A service account must read one bucket and nothing else in the project. What should be granted?

- A. Build a custom role containing exactly the permissions the task uses
- B. Grant the basic Editor role to the team
- C. Grant the predefined role that matches the task
- D. Give every platform lead the super administrator role for convenience

### 11. A build runner needs credentials for twenty minutes and nothing may be stored on disk. What should it obtain?

- A. Issue a short-lived access token through impersonation or metadata
- B. Set the credential as a plain environment variable in the deployment
- C. Create a service account key and embed it in the application configuration
- D. Enforce a password policy with a minimum length and a reuse ban

### 12. Two hundred downloaded keys are in circulation and the callers must still work. Which two changes remove the need for keys? Select two.

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Set the credential as a plain environment variable in the deployment
- C. Create a service account key and embed it in the application configuration
- D. Issue a short-lived access token through impersonation or metadata
- E. Enforce a password policy with a minimum length and a reuse ban

### 13. An auditor finds a credential that never expires and has been copied into three build systems. What is described?

- A. Create a service account key and embed it in the application configuration
- B. Grant the caller the Service Account Token Creator role on the target account
- C. Issue a short-lived access token through impersonation or metadata
- D. Configure Workload Identity Federation for the external workload

### 14. A workload runs in another cloud and must call Google APIs with no key file anywhere. What should be configured?

- A. Set the credential as a plain environment variable in the deployment
- B. Create a service account key and embed it in the application configuration
- C. Issue a short-lived access token through impersonation or metadata
- D. Configure Workload Identity Federation for the external workload

### 15. Any identity from a shared provider could otherwise impersonate the account. Which two settings close that? Select two.

- A. Configure Workload Identity Federation for the external workload
- B. Restrict the Workload Identity pool with an attribute condition on the subject
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Set the credential as a plain environment variable in the deployment
- E. Create a service account key and embed it in the application configuration

### 16. A support engineer must act as a pipeline account for one afternoon each month. What should be granted?

- A. Set the credential as a plain environment variable in the deployment
- B. Create a service account key and embed it in the application configuration
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Issue a short-lived access token through impersonation or metadata

### 17. A team asks for the account key file so that they can impersonate it. What is wrong with the request?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Issue a short-lived access token through impersonation or metadata
- C. Configure Workload Identity Federation for the external workload
- D. Hand the caller a JSON key for the service account instead

### 18. One phished password must not be enough to sign in to the admin console. What should be enforced?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Let each user decide whether to enrol in 2-step verification
- C. Enforce 2-step verification for the whole organisation
- D. Set a session length and reauthentication policy for the admin console

### 19. An administrator leaves a console session open on a shared laptop. What limits the damage?

- A. Let each user decide whether to enrol in 2-step verification
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Restrict the project to the APIs it needs and review them on a schedule
- D. Set a session length and reauthentication policy for the admin console

### 20. A database administrator needs the owner role for a two-hour migration twice a year. What should be used?

- A. Grant the privileged role permanently and review it once a year
- B. Grant the predefined role that matches the task
- C. Grant the role through Privileged Access Manager with an approval and a time limit
- D. Grant the role to a group and manage membership

### 21. A team holds an admin role far wider than the calls it makes. What should be reviewed first?

- A. Read the Policy Analyzer output before removing an unused grant
- B. Apply the Role Recommender suggestion for the oversized role
- C. Build a custom role containing exactly the permissions the task uses
- D. Grant the basic Editor role to the team

### 22. A regulator forbids one action anywhere in the organisation even where a grant allows it. What should be attached?

- A. Grant the predefined role that matches the task
- B. Enforce the constraint with an organization policy
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Attach an IAM deny policy to the organisation

### 23. The console must be reachable only from the corporate address range, whatever the identity. What should be written?

- A. Write an Access Context Manager access level and bind it to the perimeter
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Deploy the instances with internal IP addresses only
- D. Create a service perimeter with VPC Service Controls

### 24. Forty projects will be created next year and each must inherit the same network constraint. What should be used?

- A. Create a folder per environment and attach the policy at the folder
- B. Create a sink in each project and hope nobody adds a project
- C. Have a team member update accounts by hand when the HR export arrives
- D. Ask each project owner to disable the setting

### 25. A developer shares a dataset with a personal account outside the company. Which constraint blocks that?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Set an allUsers object ACL on the specific file
- C. Set the domain restricted sharing constraint on the organisation
- D. Grant the basic Editor role to the team

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. A project owner keeps opening port 22 and the security team must forbid it centrally. What should be deployed?

- A. Rely on the default VPC firewall rules in each project
- B. Deploy a hierarchical firewall policy at the organisation or folder level
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Allow all egress and rely on the application to be careful

### 27. A team wants firewall control it can edit inside its own environment. What exists?

- A. Create a service perimeter with VPC Service Controls
- B. Attach a Cloud Armor security policy to the backend service
- C. Rely on the default VPC firewall rules in each project
- D. Deploy a hierarchical firewall policy at the organisation or folder level

### 28. An egress rule must allow one SaaS host and refuse the rest inside a permitted address range. What should be enabled?

- A. Enable layer 7 inspection on the firewall policy for the egress rule
- B. Filter on address and port only and allow the rest
- C. Put Identity-Aware Proxy in front of the application
- D. Attach a Cloud Armor security policy to the backend service

### 29. Outbound web traffic must be allowlisted by host and inspected before it leaves. Which two services apply? Select two.

- A. Route the egress through Secure Web Proxy
- B. Filter on address and port only and allow the rest
- C. Allow all egress and rely on the application to be careful
- D. Run a NAT instance on a Compute Engine virtual machine
- E. Enable layer 7 inspection on the firewall policy for the egress rule

### 30. A login form is being hammered from many addresses and the backend is queueing. What should stop it?

- A. Put Identity-Aware Proxy in front of the application
- B. Route the egress through Secure Web Proxy
- C. Attach a Cloud Armor security policy to the backend service
- D. Rely on the default VPC firewall rules in each project

### 31. Half of the traffic on a pricing page is automated and a per-request score is needed. What should be enabled?

- A. Enable Cloud Armor bot management on the policy
- B. Terminate TLS at the load balancer with a managed certificate
- C. Attach a Cloud Armor security policy to the backend service
- D. Add a web application firewall rule in the application framework

### 32. A workforce application must verify the identity of each request without a VPN client. What should sit in front?

- A. Publish the application only through a VPN concentrator
- B. Deploy the instances with internal IP addresses only
- C. Put Identity-Aware Proxy in front of the application
- D. Attach a Cloud Armor security policy to the backend service

### 33. An application is reachable by anyone who completes a VPN login, including contractors who should not see it. What is the gap?

- A. Attach a Cloud Armor security policy to the backend service
- B. Put Identity-Aware Proxy in front of the application
- C. Publish the application only through a VPN concentrator
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 34. Internal services must present certificates that every client can validate and that can be revoked. What should be used?

- A. Issue internal certificates from Certificate Authority Service
- B. Generate a self-signed certificate on each instance
- C. Place Cloud NAT in front of the private instances
- D. Enable Private Google Access on the subnet

### 35. One managed certificate and one cipher policy must cover forty backends. What should be configured?

- A. Filter on address and port only and allow the rest
- B. Terminate TLS at the load balancer with a managed certificate
- C. Pass encrypted traffic straight through to the instance
- D. Generate a self-signed certificate on each instance

### 36. A public zone must let a resolver detect a forged answer. What should be turned on?

- A. Use a Cloud DNS response policy to block the known-bad domain
- B. Turn on DNSSEC for the public zone
- C. Route the egress through Secure Web Proxy
- D. Enable Private Google Access on the subnet

### 37. A known-bad domain must not resolve inside the network, and web egress must be allowlisted. Which two controls apply? Select two.

- A. Route the egress through Secure Web Proxy
- B. Use a Cloud DNS response policy to block the known-bad domain
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Turn on DNSSEC for the public zone
- E. Allow all egress and rely on the application to be careful

### 38. A database tier must not be reachable from the internet at all. What should the instances have?

- A. Terminate TLS at the load balancer with a managed certificate
- B. Deploy the instances with internal IP addresses only
- C. Enable Private Google Access on the subnet
- D. Place Cloud NAT in front of the private instances

### 39. An auditor finds twelve APIs enabled that no workload ever calls. What should be done?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Restrict the project to the APIs it needs and review them on a schedule
- C. Create a service perimeter with VPC Service Controls
- D. Enforce the constraint with an organization policy

### 40. Network and firewall policy must stay with the platform team while six teams own their own projects. What should be built?

- A. Place Cloud NAT in front of the private instances
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Peer the two VPC networks and scope the firewall rules to the peer
- D. Host the workload in a Shared VPC service project

### 41. Three tiers must reach only their neighbour, and two VPCs must be privately reachable. Which two designs apply? Select two.

- A. Peer the two VPC networks and scope the firewall rules to the peer
- B. Rely on the default VPC firewall rules in each project
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Allow all egress and rely on the application to be careful
- E. Give each tier its own subnet and allow only the flows between adjacent tiers

### 42. An analyst with a valid dataset grant must still be unable to copy data to a project outside the boundary. What should be created?

- A. Create a service perimeter with VPC Service Controls
- B. Grant authorised views or dataset-level IAM rather than table reads
- C. Rely on IAM to prevent data leaving the project
- D. Make the bucket public but unlisted

### 43. A perimeter must be introduced without breaking the private pipelines that reach Google APIs. Which two choices apply? Select two.

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Create a service perimeter with VPC Service Controls
- C. Rely on IAM to prevent data leaving the project
- D. Use restricted.googleapis.com for the API traffic
- E. Allow all egress and rely on the application to be careful

### 44. A branch link must survive the loss of one peer address under a published SLA. What should be built?

- A. Build a single classic VPN tunnel
- B. Place Cloud NAT in front of the private instances
- C. Build an HA VPN tunnel pair with two interfaces
- D. Provision a Dedicated Interconnect with two attachments

### 45. Twenty gigabits of steady replication must avoid the public internet entirely. What should be provisioned?

- A. Build an HA VPN tunnel pair with two interfaces
- B. Provision a Dedicated Interconnect with two attachments
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Build a single classic VPN tunnel

### 46. A consumer VPC needs a private address for a service that lives in a partner VPC. What should be created?

- A. Enable Private Google Access on the subnet
- B. Build a single classic VPN tunnel
- C. Place Cloud NAT in front of the private instances
- D. Publish the service through a Private Service Connect endpoint

### 47. Private instances must reach package mirrors and must keep no external address. What should be deployed?

- A. Terminate TLS at the load balancer with a managed certificate
- B. Allow all egress and rely on the application to be careful
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Place Cloud NAT in front of the private instances

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. Nobody can say which of nine hundred buckets holds personal data. What should be run?

- A. Ask the team to report which tables they believe hold personal data
- B. Replace the value with an unsalted hash
- C. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- D. Generate the key in the application and store it beside the data

### 49. Three teams scan the same columns and report different hit counts. What should be shared?

- A. Ask the team to report which tables they believe hold personal data
- B. Reuse a stored de-identification template across pipelines
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Set the credential as a plain environment variable in the deployment

### 50. A first scan must cover the whole estate and stay comparable quarter over quarter. Which two steps apply? Select two.

- A. Generate the key in the application and store it beside the data
- B. Replace the value with an unsalted hash
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Ask the team to report which tables they believe hold personal data
- E. Run a Sensitive Data Protection discovery scan over the storage and warehouse

### 51. A support console must show that a card number was present without ever revealing it. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Apply format-preserving encryption to the card number field
- C. Replace the value with a pseudonym from a crypto key
- D. Replace the value with an unsalted hash

### 52. Two reports must still join on a customer identifier after de-identification. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Replace the value with a pseudonym from a crypto key
- C. Replace the value with an unsalted hash
- D. Apply format-preserving encryption to the card number field

### 53. A legacy reader requires a sixteen-digit card column and the data must not be readable. What should be applied?

- A. Replace the value with an unsalted hash
- B. Apply format-preserving encryption to the card number field
- C. Redact the matched values with a de-identification template
- D. Replace the value with a pseudonym from a crypto key

### 54. Analysts need four columns of a table that also holds a national identifier. What should be granted?

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Grant the analyst the ability to export the whole table to a bucket
- C. Put the database password in the application config file
- D. Set an allUsers object ACL on the specific file

### 55. A connection must not carry a stored database password, and the secret that remains must be auditable. Which two controls apply? Select two.

- A. Set the credential as a plain environment variable in the deployment
- B. Generate the key in the application and store it beside the data
- C. Put the database password in the application config file
- D. Use Cloud SQL IAM database authentication for the application
- E. Store the credential in Secret Manager and grant the workload the secret accessor role

### 56. A bucket policy reads correctly but one object is still readable by the world. What removes that possibility?

- A. Make the bucket public but unlisted
- B. Allow all egress and rely on the application to be careful
- C. Set an allUsers object ACL on the specific file
- D. Grant the bucket role to a group with uniform bucket-level access

### 57. A credential must be rotatable without a redeploy and every read must appear in an audit. What should hold it?

- A. Put the database password in the application config file
- B. Set the credential as a plain environment variable in the deployment
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Generate the key in the application and store it beside the data

### 58. A credential is visible in a process listing on a shared host. What is the weakness?

- A. Set the credential as a plain environment variable in the deployment
- B. Store the credential in Secret Manager and grant the workload the secret accessor role
- C. Generate the key in the application and store it beside the data
- D. Put the database password in the application config file

### 59. A request forgery defect lets an attacker reach the instance metadata endpoint. What should reject the request?

- A. Require the metadata server header on every request
- B. Place Cloud NAT in front of the private instances
- C. Deploy the instances with internal IP addresses only
- D. Enable OS Login and turn off project-wide SSH keys

### 60. A project-wide SSH key is shared by everyone who ever joined the team. What should be enabled?

- A. Require the metadata server header on every request
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Create a service account key and embed it in the application configuration
- D. Enable OS Login and turn off project-wide SSH keys

### 61. A small team has no key management obligation and wants the default protection. What applies?

- A. Generate the key in the application and store it beside the data
- B. Rely on Google default encryption at rest
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 62. The customer must be able to stop every read of a dataset by disabling a key they control. What should be used?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Rely on Google default encryption at rest

### 63. One dataset must be revocable by the customer while a public dataset needs no key work at all. Which two choices apply? Select two.

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Set the credential as a plain environment variable in the deployment
- E. Rely on Google default encryption at rest

### 64. Key material must stay with a third party outside Google Cloud while the data stays in BigQuery. What should be used?

- A. Hold the key in Cloud External Key Manager outside Google Cloud
- B. Import the wrapping key into Cloud KMS
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Generate the key in the application and store it beside the data

### 65. Old objects are still wrapped by an on-premises key that must come under KMS control. What should be done?

- A. Hold the key in Cloud External Key Manager outside Google Cloud
- B. Set a rotation period on the key
- C. Import the wrapping key into Cloud KMS
- D. Generate the key in the application and store it beside the data

### 66. An auditor asks how long one key version protects newly written data. What should be configured?

- A. Disable the key version and re-wrap the data
- B. Set a rotation period on the key
- C. Generate the key in the application and store it beside the data
- D. Import the wrapping key into Cloud KMS

### 67. A tenant demands that an incident stops every read of their rows within minutes. What should be done?

- A. Disable the key version and re-wrap the data
- B. Import the wrapping key into Cloud KMS
- C. Set a rotation period on the key
- D. Rely on Google default encryption at rest

### 68. A regulated workload must keep its memory unreadable to the host while it runs. What should be used?

- A. Deploy the instances with internal IP addresses only
- B. Rely on Google default encryption at rest
- C. Run the workload on a Confidential VM
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 69. Two workloads need in-use memory protection, one on a virtual machine and one in a cluster. Which two choices apply? Select two.

- A. Run the pod in a Confidential GKE node pool
- B. Run the workload on a Confidential VM
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Rely on Google default encryption at rest
- E. Enable OS Login and turn off project-wide SSH keys

### 70. A retention period must be immutable even against the bucket owner. What should be applied?

- A. Set an allUsers object ACL on the specific file
- B. Attach an object lifecycle rule that keeps the required retention
- C. Make the bucket public but unlisted
- D. Apply a retention policy with bucket lock

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A vulnerable base image must be stopped before it is ever deployed. What should be added?

- A. Add an Artifact Analysis scan to the CI pipeline
- B. Allow all egress and rely on the application to be careful
- C. Let each team patch its own instances when convenient
- D. Scan the running image in production once a quarter

### 72. A team scans its images only after they have been running for a quarter. What is the flaw?

- A. Add an Artifact Analysis scan to the CI pipeline
- B. Let each team patch its own instances when convenient
- C. Deploy with Binary Authorization in dry-run mode only
- D. Scan the running image in production once a quarter

### 73. Only images with a recorded attestation may be admitted to the cluster. What should be enforced?

- A. Deploy with Binary Authorization in dry-run mode only
- B. Enforce a Binary Authorization policy that requires an attested image
- C. Attach a Cloud Armor security policy to the backend service
- D. Deploy the instances with internal IP addresses only

### 74. A new admission policy must be observed for a week before it is allowed to block a release. Which two steps apply? Select two.

- A. Enforce a Binary Authorization policy that requires an attested image
- B. Attach a Cloud Armor security policy to the backend service
- C. Deploy the instances with internal IP addresses only
- D. Deploy with Binary Authorization in dry-run mode only
- E. Scan the running image in production once a quarter

### 75. An image ships a compiler and three accounts that no service uses. What should replace it?

- A. Allow all egress and rely on the application to be careful
- B. Build the base image from a hardened source with a documented baseline
- C. Let each team patch its own instances when convenient
- D. Scan the running image in production once a quarter

### 76. Nine hundred hosts are at unknown patch levels and a fleet report is required. What should be used?

- A. Let each team patch its own instances when convenient
- B. Schedule patch jobs across the fleet with VM Manager
- C. Build the base image from a hardened source with a documented baseline
- D. Compare the deployed configuration with the intended state on a schedule

### 77. A local misconfiguration must surface as a recurring finding in the security console. What should be built?

- A. Deploy a Security Health Analytics custom module for the check
- B. Have a team member update accounts by hand when the HR export arrives
- C. Compare the deployed configuration with the intended state on a schedule
- D. Ask each project owner to disable the setting

### 78. The same unsafe setting keeps reappearing and must be blocked rather than reported. What should be written?

- A. Compare the deployed configuration with the intended state on a schedule
- B. Lower the log volume by disabling data access logs
- C. Write a custom organization policy constraint for the rule
- D. Deploy a Security Health Analytics custom module for the check

### 79. Analysts need a record of which flows were accepted and rejected last month. What should be enabled?

- A. Lower the log volume by disabling data access logs
- B. Mirror the production traffic to a collector with Packet Mirroring
- C. Deploy Cloud IDS on the network
- D. Enable VPC Flow Logs on the subnets

### 80. An intrusion must be detected inline, and the payload must also be readable by a forensic appliance. Which two services apply? Select two.

- A. Lower the log volume by disabling data access logs
- B. Deploy Cloud IDS on the network
- C. Mirror the production traffic to a collector with Packet Mirroring
- D. Enable VPC Flow Logs on the subnets
- E. Scan the running image in production once a quarter

### 81. Two years of firewall entries must stay queryable for a correlation study. What should be used?

- A. Give the SIEM a service account key so it can pull the logs
- B. Create a sink in each project and hope nobody adds a project
- C. Query the logs through Log Analytics
- D. Lower the log volume by disabling data access logs

### 82. Security logs sit in the same projects as the principals who generate them. What should change?

- A. Give the SIEM a service account key so it can pull the logs
- B. Lower the log volume by disabling data access logs
- C. Create a sink in each project and hope nobody adds a project
- D. Route security logs to a dedicated project with its own retention

### 83. A cost review proposes disabling data access logs to save money. What is the consequence?

- A. Enable Data Access audit logs for the service
- B. Route security logs to a dedicated project with its own retention
- C. Lower the log volume by disabling data access logs
- D. Apply a retention policy with bucket lock

### 84. Someone must be named as having changed a firewall rule at 02:00. Which log answers?

- A. Read the Admin Activity audit log for the change
- B. Enable Data Access audit logs for the service
- C. Create a log sink that routes the entries to the destination
- D. Give the SIEM a service account key so it can pull the logs

### 85. An investigator needs to know who read a specific object rather than who configured it. What must have been enabled?

- A. Read the Admin Activity audit log for the change
- B. Create a log sink that routes the entries to the destination
- C. Enable VPC Flow Logs on the subnets
- D. Enable Data Access audit logs for the service

### 86. Forty projects and three more each quarter must all deliver to one destination. What should be created?

- A. Create a log sink that routes the entries to the destination
- B. Create a sink in each project and hope nobody adds a project
- C. Give the SIEM a service account key so it can pull the logs
- D. Create an aggregated sink at the organisation level

### 87. An external SIEM must receive the entries without an inbound path into the organisation. What should be used?

- A. Give the SIEM a service account key so it can pull the logs
- B. Export the entries to the external SIEM through Pub/Sub
- C. Set the credential as a plain environment variable in the deployment
- D. Lower the log volume by disabling data access logs

### 88. A single console must list findings across detectors and projects. What should be reviewed?

- A. Review the Security Command Center findings for the project
- B. Deploy a Security Health Analytics custom module for the check
- C. Query the logs through Log Analytics
- D. Compare the deployed configuration with the intended state on a schedule

### 89. A finding must reach the response pipeline and must never be closed with nobody answerable. Which two practices apply? Select two.

- A. Name an owner for each control
- B. Publish new findings to Pub/Sub for the response pipeline
- C. Lower the log volume by disabling data access logs
- D. Close the finding as a false positive without a comment
- E. Give the SIEM a service account key so it can pull the logs

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. A customer asks who patches the guest operating system on their own instances. What document answers?

- A. Document which controls Google operates and which the customer must implement
- B. Declare the whole organisation in scope for every regime
- C. State in the policy document that the environment is compliant
- D. Assume Google secures every layer once the data is in the cloud

### 91. An audit must show which layer each party operates and who answers for it. Which two practices apply? Select two.

- A. Document which controls Google operates and which the customer must implement
- B. Declare the whole organisation in scope for every regime
- C. Name an owner for each control
- D. Assume Google secures every layer once the data is in the cloud
- E. State in the policy document that the environment is compliant

### 92. A regulated folder needs personnel and location controls applied by default to every new project. What should be created?

- A. Constrain the resources to the required region with a location organization policy
- B. Record the regime in a spreadsheet and configure each control by hand
- C. Create the folder as an Assured Workloads environment
- D. Ask each project owner to disable the setting

### 93. A team tracks its regime controls in a spreadsheet and configures each project by hand. What fails first?

- A. Ask each project owner to disable the setting
- B. Keep the audit evidence for the period the regime requires
- C. Create the folder as an Assured Workloads environment
- D. Record the regime in a spreadsheet and configure each control by hand

### 94. A customer must see the occasions when a Google operator touched their content. What should be enabled?

- A. Read the Admin Activity audit log for the change
- B. Turn on Access Transparency and read its logs
- C. Require Access Approval before an operator may read the content
- D. Enable Data Access audit logs for the service

### 95. A customer must grant permission before an operator may read the content. What should be required?

- A. Create a service perimeter with VPC Service Controls
- B. Require Access Approval before an operator may read the content
- C. Write an Access Context Manager access level and bind it to the perimeter
- D. Turn on Access Transparency and read its logs

### 96. Every dataset must be created in one named country, including in a project made next year. What should be enforced?

- A. Declare the whole organisation in scope for every regime
- B. Constrain the resources to the required region with a location organization policy
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Leave the default multi-region setting

### 97. A dataset defaults to a multi-region setting and a regulator named a single country. What is the problem?

- A. Declare the whole organisation in scope for every regime
- B. Leave the default multi-region setting
- C. Constrain the resources to the required region with a location organization policy
- D. Record the regime in a spreadsheet and configure each control by hand

### 98. An auditor asks which control answers clause 4.2 and where its evidence lives. What should be produced?

- A. Assume Google secures every layer once the data is in the cloud
- B. Declare the whole organisation in scope for every regime
- C. State in the policy document that the environment is compliant
- D. Map each requirement to the control that satisfies it and the evidence it produces

### 99. Evidence must survive a three-year audit cycle. What must be configured?

- A. Declare the whole organisation in scope for every regime
- B. Lower the log volume by disabling data access logs
- C. State in the policy document that the environment is compliant
- D. Keep the audit evidence for the period the regime requires

### 100. The auditor needs to know which projects the regime covers before testing begins. What should be written?

- A. Draw the compliance boundary around the projects and services that hold the regulated data
- B. Record the regime in a spreadsheet and configure each control by hand
- C. Declare the whole organisation in scope for every regime
- D. State in the policy document that the environment is compliant

---

## Answer key and explanations

### Question 1 — C

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory every Google Cloud grant resolves against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Cloud Identity is the directory every Google Cloud grant resolves against.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: Cloud Identity is the directory every Google Cloud grant resolves against.
- **C:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory every Google Cloud grant resolves against.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: Cloud Identity is the directory every Google Cloud grant resolves against.

### Question 2 — D

Answer: Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync. GCDS pushes users and groups from the existing directory on a schedule. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: GCDS pushes users and groups from the existing directory on a schedule.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: GCDS pushes users and groups from the existing directory on a schedule.
- **C:** Incorrect for this question. A response policy overrides resolution for named domains inside the network. Why the correct answer wins: GCDS pushes users and groups from the existing directory on a schedule.
- **D:** Correct. In this case: GCDS pushes users and groups from the existing directory on a schedule.

### Question 3 — D, E

Answers: Configure single sign-on with a third-party identity provider over SAML; Assign the super administrator role to a dedicated break-glass account with hardware keys. SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible.
- **C:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible.
- **D:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible.
- **E:** Correct. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. In this case: SAML SSO keeps authentication with the provider, and a break-glass super administrator keeps recovery possible.

### Question 4 — C

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK Directory API applies the lifecycle change without a human step. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK Directory API applies the lifecycle change without a human step.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The Admin SDK Directory API applies the lifecycle change without a human step.
- **C:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK Directory API applies the lifecycle change without a human step.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: The Admin SDK Directory API applies the lifecycle change without a human step.

### Question 5 — B

Answer: Assign the super administrator role to a dedicated break-glass account with hardware keys. A dedicated break-glass super administrator is reserved for directory-level recovery. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: A dedicated break-glass super administrator is reserved for directory-level recovery.
- **B:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: A dedicated break-glass super administrator is reserved for directory-level recovery.
- **C:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A dedicated break-glass super administrator is reserved for directory-level recovery.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: A dedicated break-glass super administrator is reserved for directory-level recovery.

### Question 6 — B

Answer: Federate the partner workforce with Workforce Identity Federation. Workforce Identity Federation accepts the external provider without creating Cloud Identity users. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Workforce Identity Federation accepts the external provider without creating Cloud Identity users.
- **B:** Correct. In this case: Workforce Identity Federation accepts the external provider without creating Cloud Identity users.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Workforce Identity Federation accepts the external provider without creating Cloud Identity users.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workforce Identity Federation accepts the external provider without creating Cloud Identity users.

### Question 7 — B, C

Answers: Federate the partner workforce with Workforce Identity Federation; Set the domain restricted sharing constraint on the organisation. Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain.
- **B:** Correct. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. In this case: Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain.
- **C:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain.
- **E:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: Federation avoids new local accounts, and domain restricted sharing keeps grants inside the allowed domain.

### Question 8 — D

Answer: Create a dedicated service account per workload with only the roles it needs. A dedicated service account per workload makes every audit entry attributable. A per-workload service account bounds the blast radius and makes audit records attributable. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A dedicated service account per workload makes every audit entry attributable.
- **B:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A dedicated service account per workload makes every audit entry attributable.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A dedicated service account per workload makes every audit entry attributable.
- **D:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A dedicated service account per workload makes every audit entry attributable.

### Question 9 — D

Answer: Run the workload as the default Compute Engine service account. The default service account is shared, so its grants reach every workload on the project. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: The default service account is shared, so its grants reach every workload on the project.
- **B:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The default service account is shared, so its grants reach every workload on the project.
- **C:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default service account is shared, so its grants reach every workload on the project.
- **D:** Correct. In this case: The default service account is shared, so its grants reach every workload on the project.

### Question 10 — C

Answer: Grant the predefined role that matches the task. The predefined storage role carries only the permissions that read needs. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: The predefined storage role carries only the permissions that read needs.
- **B:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: The predefined storage role carries only the permissions that read needs.
- **C:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: The predefined storage role carries only the permissions that read needs.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: The predefined storage role carries only the permissions that read needs.

### Question 11 — A

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token expires on its own and leaves nothing to copy. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: A short-lived token expires on its own and leaves nothing to copy.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token expires on its own and leaves nothing to copy.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token expires on its own and leaves nothing to copy.
- **D:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A short-lived token expires on its own and leaves nothing to copy.

### Question 12 — A, D

Answers: Grant the caller the Service Account Token Creator role on the target account; Issue a short-lived access token through impersonation or metadata. Impersonation grants the role instead of a key, and a short-lived token expires quickly. Impersonation lets a principal act as the service account without holding a key for it. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation grants the role instead of a key, and a short-lived token expires quickly.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation grants the role instead of a key, and a short-lived token expires quickly.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation grants the role instead of a key, and a short-lived token expires quickly.
- **D:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: Impersonation grants the role instead of a key, and a short-lived token expires quickly.
- **E:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Impersonation grants the role instead of a key, and a short-lived token expires quickly.

### Question 13 — A

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key is long-lived and travels wherever it is pasted. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key is long-lived and travels wherever it is pasted.
- **B:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key is long-lived and travels wherever it is pasted.
- **C:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key is long-lived and travels wherever it is pasted.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key is long-lived and travels wherever it is pasted.

### Question 14 — D

Answer: Configure Workload Identity Federation for the external workload. Workload Identity Federation exchanges the external token for short-lived Google credentials. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Workload Identity Federation exchanges the external token for short-lived Google credentials.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workload Identity Federation exchanges the external token for short-lived Google credentials.
- **C:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Workload Identity Federation exchanges the external token for short-lived Google credentials.
- **D:** Correct. In this case: Workload Identity Federation exchanges the external token for short-lived Google credentials.

### Question 15 — A, B

Answers: Configure Workload Identity Federation for the external workload; Restrict the Workload Identity pool with an attribute condition on the subject. Federation removes the key, and an attribute condition limits which external identities may impersonate. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Federation removes the key, and an attribute condition limits which external identities may impersonate.
- **B:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: Federation removes the key, and an attribute condition limits which external identities may impersonate.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Federation removes the key, and an attribute condition limits which external identities may impersonate.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Federation removes the key, and an attribute condition limits which external identities may impersonate.
- **E:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation removes the key, and an attribute condition limits which external identities may impersonate.

### Question 16 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation lets the engineer act as the account without holding its key. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation lets the engineer act as the account without holding its key.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation lets the engineer act as the account without holding its key.
- **C:** Correct. In this case: Impersonation lets the engineer act as the account without holding its key.
- **D:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation lets the engineer act as the account without holding its key.

### Question 17 — D

Answer: Hand the caller a JSON key for the service account instead. A handed-out key cannot be scoped to one action and outlives the task. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A handed-out key cannot be scoped to one action and outlives the task.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A handed-out key cannot be scoped to one action and outlives the task.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A handed-out key cannot be scoped to one action and outlives the task.
- **D:** Correct. In this case: A handed-out key cannot be scoped to one action and outlives the task.

### Question 18 — C

Answer: Enforce 2-step verification for the whole organisation. Enforced 2-step verification makes the password a partial factor. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Enforced 2-step verification makes the password a partial factor.
- **B:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: Enforced 2-step verification makes the password a partial factor.
- **C:** Correct. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. In this case: Enforced 2-step verification makes the password a partial factor.
- **D:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: Enforced 2-step verification makes the password a partial factor.

### Question 19 — D

Answer: Set a session length and reauthentication policy for the admin console. A session length policy bounds how long a stolen session stays useful. A session control limits how long a stolen browser session stays useful. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A session length policy bounds how long a stolen session stays useful.
- **B:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A session length policy bounds how long a stolen session stays useful.
- **C:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: A session length policy bounds how long a stolen session stays useful.
- **D:** Correct. A session control limits how long a stolen browser session stays useful. In this case: A session length policy bounds how long a stolen session stays useful.

### Question 20 — C

Answer: Grant the role through Privileged Access Manager with an approval and a time limit. Privileged Access Manager issues a temporary grant after approval. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager issues a temporary grant after approval.
- **B:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Privileged Access Manager issues a temporary grant after approval.
- **C:** Correct. In this case: Privileged Access Manager issues a temporary grant after approval.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager issues a temporary grant after approval.

### Question 21 — B

Answer: Apply the Role Recommender suggestion for the oversized role. Role Recommender proposes a narrower role from the permissions actually used. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. Why the correct answer wins: Role Recommender proposes a narrower role from the permissions actually used.
- **B:** Correct. In this case: Role Recommender proposes a narrower role from the permissions actually used.
- **C:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: Role Recommender proposes a narrower role from the permissions actually used.
- **D:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Role Recommender proposes a narrower role from the permissions actually used.

### Question 22 — D

Answer: Attach an IAM deny policy to the organisation. A deny policy overrides every allow beneath it. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: A deny policy overrides every allow beneath it.
- **B:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: A deny policy overrides every allow beneath it.
- **C:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A deny policy overrides every allow beneath it.
- **D:** Correct. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. In this case: A deny policy overrides every allow beneath it.

### Question 23 — A

Answer: Write an Access Context Manager access level and bind it to the perimeter. Access Context Manager describes the request context the policy requires. Access Context Manager describes the request context, such as network origin, that a policy can require. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Access Context Manager describes the request context, such as network origin, that a policy can require. In this case: Access Context Manager describes the request context the policy requires.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Access Context Manager describes the request context the policy requires.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Access Context Manager describes the request context the policy requires.
- **D:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Context Manager describes the request context the policy requires.

### Question 24 — A

Answer: Create a folder per environment and attach the policy at the folder. A folder attachment covers every current and future project inside it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A folder attachment covers every current and future project inside it.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A folder attachment covers every current and future project inside it.
- **C:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A folder attachment covers every current and future project inside it.
- **D:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A folder attachment covers every current and future project inside it.

### Question 25 — C

Answer: Set the domain restricted sharing constraint on the organisation. Domain restricted sharing keeps a grant from naming an outside identity. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Domain restricted sharing keeps a grant from naming an outside identity.
- **B:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Domain restricted sharing keeps a grant from naming an outside identity.
- **C:** Correct. In this case: Domain restricted sharing keeps a grant from naming an outside identity.
- **D:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Domain restricted sharing keeps a grant from naming an outside identity.

### Question 26 — B

Answer: Deploy a hierarchical firewall policy at the organisation or folder level. A hierarchical policy is evaluated before project rules and cannot be overridden below. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: A hierarchical policy is evaluated before project rules and cannot be overridden below.
- **B:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: A hierarchical policy is evaluated before project rules and cannot be overridden below.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: A hierarchical policy is evaluated before project rules and cannot be overridden below.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A hierarchical policy is evaluated before project rules and cannot be overridden below.

### Question 27 — C

Answer: Rely on the default VPC firewall rules in each project. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Project-level rules are editable by the project owner and are evaluated after the hierarchy.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Project-level rules are editable by the project owner and are evaluated after the hierarchy.
- **C:** Correct. In this case: Project-level rules are editable by the project owner and are evaluated after the hierarchy.
- **D:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: Project-level rules are editable by the project owner and are evaluated after the hierarchy.

### Question 28 — A

Answer: Enable layer 7 inspection on the firewall policy for the egress rule. Layer 7 inspection reads the destination host name. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the destination host name.
- **B:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the destination host name.
- **C:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Layer 7 inspection reads the destination host name.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Layer 7 inspection reads the destination host name.

### Question 29 — A, E

Answers: Enable layer 7 inspection on the firewall policy for the egress rule; Route the egress through Secure Web Proxy. Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress.
- **B:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress.
- **D:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress.
- **E:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the host, and Secure Web Proxy applies the allowlist to web egress.

### Question 30 — C

Answer: Attach a Cloud Armor security policy to the backend service. Cloud Armor rate-limits and blocks at the load balancer before the backend. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Cloud Armor rate-limits and blocks at the load balancer before the backend.
- **B:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: Cloud Armor rate-limits and blocks at the load balancer before the backend.
- **C:** Correct. In this case: Cloud Armor rate-limits and blocks at the load balancer before the backend.
- **D:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Cloud Armor rate-limits and blocks at the load balancer before the backend.

### Question 31 — A

Answer: Enable Cloud Armor bot management on the policy. Bot management scores automated traffic so a rule can separate it. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Bot management scores automated traffic so a rule can separate it.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it.
- **D:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it.

### Question 32 — C

Answer: Put Identity-Aware Proxy in front of the application. IAP authorises each request against IAM before it reaches the backend. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP authorises each request against IAM before it reaches the backend.
- **B:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: IAP authorises each request against IAM before it reaches the backend.
- **C:** Correct. In this case: IAP authorises each request against IAM before it reaches the backend.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP authorises each request against IAM before it reaches the backend.

### Question 33 — C

Answer: Publish the application only through a VPN concentrator. A VPN gates the network path but not the individual user. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: A VPN gates the network path but not the individual user.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A VPN gates the network path but not the individual user.
- **C:** Correct. In this case: A VPN gates the network path but not the individual user.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A VPN gates the network path but not the individual user.

### Question 34 — A

Answer: Issue internal certificates from Certificate Authority Service. Certificate Authority Service issues and revokes private certificates. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Certificate Authority Service issues and revokes private certificates.
- **B:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues and revokes private certificates.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Certificate Authority Service issues and revokes private certificates.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Certificate Authority Service issues and revokes private certificates.

### Question 35 — B

Answer: Terminate TLS at the load balancer with a managed certificate. Terminating at the load balancer centralises the certificate and the policy. Terminating at the load balancer gives one managed certificate and a single policy point. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Terminating at the load balancer centralises the certificate and the policy.
- **B:** Correct. Terminating at the load balancer gives one managed certificate and a single policy point. In this case: Terminating at the load balancer centralises the certificate and the policy.
- **C:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: Terminating at the load balancer centralises the certificate and the policy.
- **D:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Terminating at the load balancer centralises the certificate and the policy.

### Question 36 — B

Answer: Turn on DNSSEC for the public zone. DNSSEC signs the answers so a resolver can detect forgery. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A response policy overrides resolution for named domains inside the network. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.
- **B:** Correct. In this case: DNSSEC signs the answers so a resolver can detect forgery.
- **C:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: DNSSEC signs the answers so a resolver can detect forgery.

### Question 37 — A, B

Answers: Route the egress through Secure Web Proxy; Use a Cloud DNS response policy to block the known-bad domain. A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. A response policy overrides resolution for named domains inside the network. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist.
- **B:** Correct. A response policy overrides resolution for named domains inside the network. In this case: A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist.
- **D:** Incorrect for this question. DNSSEC signs the answers so a resolver can detect a forged response. Why the correct answer wins: A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A response policy overrides resolution for named domains, and Secure Web Proxy applies the egress allowlist.

### Question 38 — B

Answer: Deploy the instances with internal IP addresses only. An internal-only address means the workload cannot be reached from the internet. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: An internal-only address means the workload cannot be reached from the internet.
- **B:** Correct. In this case: An internal-only address means the workload cannot be reached from the internet.
- **C:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: An internal-only address means the workload cannot be reached from the internet.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An internal-only address means the workload cannot be reached from the internet.

### Question 39 — B

Answer: Restrict the project to the APIs it needs and review them on a schedule. Disabling unused APIs removes an attack surface nothing needs. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **B:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: Disabling unused APIs removes an attack surface nothing needs.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.

### Question 40 — D

Answer: Host the workload in a Shared VPC service project. Shared VPC centralises the network in the host project. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **C:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **D:** Correct. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. In this case: Shared VPC centralises the network in the host project.

### Question 41 — A, E

Answers: Give each tier its own subnet and allow only the flows between adjacent tiers; Peer the two VPC networks and scope the firewall rules to the peer. Tier subnets express the allowed flows, and peering gives private reachability between the VPCs. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Peering gives private reachability while firewall rules still decide which flows are allowed. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Peering gives private reachability while firewall rules still decide which flows are allowed. In this case: Tier subnets express the allowed flows, and peering gives private reachability between the VPCs.
- **B:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Tier subnets express the allowed flows, and peering gives private reachability between the VPCs.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Tier subnets express the allowed flows, and peering gives private reachability between the VPCs.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Tier subnets express the allowed flows, and peering gives private reachability between the VPCs.
- **E:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Tier subnets express the allowed flows, and peering gives private reachability between the VPCs.

### Question 42 — A

Answer: Create a service perimeter with VPC Service Controls. A service perimeter blocks the movement whatever the IAM grant says. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: A service perimeter blocks the movement whatever the IAM grant says.
- **B:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: A service perimeter blocks the movement whatever the IAM grant says.
- **C:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: A service perimeter blocks the movement whatever the IAM grant says.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A service perimeter blocks the movement whatever the IAM grant says.

### Question 43 — B, D

Answers: Create a service perimeter with VPC Service Controls; Use restricted.googleapis.com for the API traffic. The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it.
- **B:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it.
- **C:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it.
- **D:** Correct. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. In this case: The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The perimeter enforces the boundary, and restricted virtual IPs keep the API path inside it.

### Question 44 — C

Answer: Build an HA VPN tunnel pair with two interfaces. An HA VPN pair gives 99.99 percent availability across two interfaces. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: An HA VPN pair gives 99.99 percent availability across two interfaces.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An HA VPN pair gives 99.99 percent availability across two interfaces.
- **C:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: An HA VPN pair gives 99.99 percent availability across two interfaces.
- **D:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: An HA VPN pair gives 99.99 percent availability across two interfaces.

### Question 45 — B

Answer: Provision a Dedicated Interconnect with two attachments. Dedicated Interconnect gives a private circuit with redundant attachments. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: Dedicated Interconnect gives a private circuit with redundant attachments.
- **B:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: Dedicated Interconnect gives a private circuit with redundant attachments.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Dedicated Interconnect gives a private circuit with redundant attachments.
- **D:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Dedicated Interconnect gives a private circuit with redundant attachments.

### Question 46 — D

Answer: Publish the service through a Private Service Connect endpoint. A Private Service Connect endpoint gives a private address to a service in another VPC. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: A Private Service Connect endpoint gives a private address to a service in another VPC.
- **B:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: A Private Service Connect endpoint gives a private address to a service in another VPC.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: A Private Service Connect endpoint gives a private address to a service in another VPC.
- **D:** Correct. In this case: A Private Service Connect endpoint gives a private address to a service in another VPC.

### Question 47 — D

Answer: Place Cloud NAT in front of the private instances. Cloud NAT gives outbound connectivity without an external address. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT gives outbound connectivity without an external address.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT gives outbound connectivity without an external address.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT gives outbound connectivity without an external address.
- **D:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT gives outbound connectivity without an external address.

### Question 48 — C

Answer: Run a Sensitive Data Protection discovery scan over the storage and warehouse. A discovery scan profiles where the sensitive data actually sits. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A discovery scan profiles where the sensitive data actually sits.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A discovery scan profiles where the sensitive data actually sits.
- **C:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: A discovery scan profiles where the sensitive data actually sits.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A discovery scan profiles where the sensitive data actually sits.

### Question 49 — C

Answer: Save a Sensitive Data Protection inspect template and reuse it. A saved inspect template keeps the detection rules identical. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A saved inspect template keeps the detection rules identical.
- **B:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A saved inspect template keeps the detection rules identical.
- **C:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A saved inspect template keeps the detection rules identical.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A saved inspect template keeps the detection rules identical.

### Question 50 — C, E

Answers: Run a Sensitive Data Protection discovery scan over the storage and warehouse; Save a Sensitive Data Protection inspect template and reuse it. Discovery finds the data, and a saved template keeps the rules stable. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Discovery finds the data, and a saved template keeps the rules stable.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Discovery finds the data, and a saved template keeps the rules stable.
- **C:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: Discovery finds the data, and a saved template keeps the rules stable.
- **D:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: Discovery finds the data, and a saved template keeps the rules stable.
- **E:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: Discovery finds the data, and a saved template keeps the rules stable.

### Question 51 — A

Answer: Redact the matched values with a de-identification template. Redaction replaces the matched value entirely. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Redaction replaces the matched value entirely.
- **B:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: Redaction replaces the matched value entirely.
- **C:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Redaction replaces the matched value entirely.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Redaction replaces the matched value entirely.

### Question 52 — B

Answer: Replace the value with a pseudonym from a crypto key. Pseudonymisation keeps a stable token so the records still join. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Pseudonymisation keeps a stable token so the records still join.
- **B:** Correct. In this case: Pseudonymisation keeps a stable token so the records still join.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Pseudonymisation keeps a stable token so the records still join.
- **D:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: Pseudonymisation keeps a stable token so the records still join.

### Question 53 — B

Answer: Apply format-preserving encryption to the card number field. Format-preserving encryption keeps the type and the length. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **B:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: Format-preserving encryption keeps the type and the length.
- **C:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **D:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Format-preserving encryption keeps the type and the length.

### Question 54 — A

Answer: Grant authorised views or dataset-level IAM rather than table reads. Dataset authority and authorised views expose only the allowed columns. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Dataset authority and authorised views expose only the allowed columns.
- **B:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Dataset authority and authorised views expose only the allowed columns.
- **C:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Dataset authority and authorised views expose only the allowed columns.
- **D:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Dataset authority and authorised views expose only the allowed columns.

### Question 55 — D, E

Answers: Use Cloud SQL IAM database authentication for the application; Store the credential in Secret Manager and grant the workload the secret accessor role. IAM database authentication removes the password, and Secret Manager audits each read. IAM database authentication removes the stored database password and ties each connection to an identity. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: IAM database authentication removes the password, and Secret Manager audits each read.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: IAM database authentication removes the password, and Secret Manager audits each read.
- **C:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: IAM database authentication removes the password, and Secret Manager audits each read.
- **D:** Correct. IAM database authentication removes the stored database password and ties each connection to an identity. In this case: IAM database authentication removes the password, and Secret Manager audits each read.
- **E:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: IAM database authentication removes the password, and Secret Manager audits each read.

### Question 56 — D

Answer: Grant the bucket role to a group with uniform bucket-level access. Uniform bucket-level access makes IAM the only decision point. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **C:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **D:** Correct. In this case: Uniform bucket-level access makes IAM the only decision point.

### Question 57 — C

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager versions the value and audits each read. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager versions the value and audits each read.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager versions the value and audits each read.
- **C:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager versions the value and audits each read.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager versions the value and audits each read.

### Question 58 — A

Answer: Set the credential as a plain environment variable in the deployment. An environment variable is exposed in the process listing and the deployment history. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An environment variable is exposed in the process listing and the deployment history.
- **B:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: An environment variable is exposed in the process listing and the deployment history.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: An environment variable is exposed in the process listing and the deployment history.
- **D:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: An environment variable is exposed in the process listing and the deployment history.

### Question 59 — A

Answer: Require the metadata server header on every request. Requiring the metadata header blocks the simplest forgery. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: Requiring the metadata header blocks the simplest forgery.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **D:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.

### Question 60 — D

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login ties each login to an identity and removes the shared key. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key.
- **B:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key.
- **D:** Correct. In this case: OS Login ties each login to an identity and removes the shared key.

### Question 61 — B

Answer: Rely on Google default encryption at rest. Google default encryption protects the bytes at rest with no customer key work. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Google default encryption protects the bytes at rest with no customer key work.
- **B:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: Google default encryption protects the bytes at rest with no customer key work.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Google default encryption protects the bytes at rest with no customer key work.
- **D:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Google default encryption protects the bytes at rest with no customer key work.

### Question 62 — A

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key can be disabled by the customer. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key can be disabled by the customer.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key can be disabled by the customer.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key can be disabled by the customer.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key can be disabled by the customer.

### Question 63 — A, E

Answers: Encrypt the dataset with a customer-managed key in Cloud KMS; Rely on Google default encryption at rest. A customer-managed key gives revocation, and default encryption is enough for the public set. A customer-managed key lets the customer disable the key and stop every read of the data. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key gives revocation, and default encryption is enough for the public set.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key gives revocation, and default encryption is enough for the public set.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key gives revocation, and default encryption is enough for the public set.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A customer-managed key gives revocation, and default encryption is enough for the public set.
- **E:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: A customer-managed key gives revocation, and default encryption is enough for the public set.

### Question 64 — A

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM keeps the key material with the external party. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM keeps the key material with the external party.
- **B:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM keeps the key material with the external party.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM keeps the key material with the external party.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM keeps the key material with the external party.

### Question 65 — C

Answer: Import the wrapping key into Cloud KMS. Key import brings existing material under KMS control. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Key import brings existing material under KMS control.
- **B:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Key import brings existing material under KMS control.
- **C:** Correct. In this case: Key import brings existing material under KMS control.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Key import brings existing material under KMS control.

### Question 66 — B

Answer: Set a rotation period on the key. Rotation issues new versions on a schedule. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Why the correct answer wins: Rotation issues new versions on a schedule.
- **B:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: Rotation issues new versions on a schedule.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Rotation issues new versions on a schedule.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Rotation issues new versions on a schedule.

### Question 67 — A

Answer: Disable the key version and re-wrap the data. Disabling the key version makes the protected bytes unreadable. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Disabling the key version makes the protected bytes unreadable.
- **B:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Disabling the key version makes the protected bytes unreadable.
- **C:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Disabling the key version makes the protected bytes unreadable.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Disabling the key version makes the protected bytes unreadable.

### Question 68 — C

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted in use. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **C:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted in use.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.

### Question 69 — A, B

Answers: Run the pod in a Confidential GKE node pool; Run the workload on a Confidential VM. A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods. Confidential GKE extends in-use memory protection to each pod on the node. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods.
- **B:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods.
- **E:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM covers the instance, and a Confidential GKE node pool covers the pods.

### Question 70 — D

Answer: Apply a retention policy with bucket lock. Bucket lock makes the retention period immutable. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **B:** Incorrect for this question. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **C:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **D:** Correct. In this case: Bucket lock makes the retention period immutable.

### Question 71 — A

Answer: Add an Artifact Analysis scan to the CI pipeline. Scanning in the pipeline stops the image before deployment. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Scanning in the pipeline stops the image before deployment.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Scanning in the pipeline stops the image before deployment.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: Scanning in the pipeline stops the image before deployment.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Scanning in the pipeline stops the image before deployment.

### Question 72 — D

Answer: Scan the running image in production once a quarter. A quarterly production scan finds the vulnerable image far too late. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **C:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: A quarterly production scan finds the vulnerable image far too late.
- **D:** Correct. In this case: A quarterly production scan finds the vulnerable image far too late.

### Question 73 — B

Answer: Enforce a Binary Authorization policy that requires an attested image. Binary Authorization refuses an image that lacks the attestation. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.
- **B:** Correct. In this case: Binary Authorization refuses an image that lacks the attestation.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.
- **D:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.

### Question 74 — A, D

Answers: Deploy with Binary Authorization in dry-run mode only; Enforce a Binary Authorization policy that requires an attested image. Dry-run records violations without blocking, and enforcement refuses unattested images. Dry-run records the violation and still admits the image. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. In this case: Dry-run records violations without blocking, and enforcement refuses unattested images.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Dry-run records violations without blocking, and enforcement refuses unattested images.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Dry-run records violations without blocking, and enforcement refuses unattested images.
- **D:** Correct. Dry-run records the violation and still admits the image. In this case: Dry-run records violations without blocking, and enforcement refuses unattested images.
- **E:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Dry-run records violations without blocking, and enforcement refuses unattested images.

### Question 75 — B

Answer: Build the base image from a hardened source with a documented baseline. A hardened baseline removes what a general-purpose image carries. A hardened baseline removes the packages and accounts that a general-purpose image ships. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **B:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline removes what a general-purpose image carries.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.

### Question 76 — B

Answer: Schedule patch jobs across the fleet with VM Manager. VM Manager applies and reports patches across the fleet. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: VM Manager applies and reports patches across the fleet.
- **B:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: VM Manager applies and reports patches across the fleet.
- **C:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: VM Manager applies and reports patches across the fleet.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: VM Manager applies and reports patches across the fleet.

### Question 77 — A

Answer: Deploy a Security Health Analytics custom module for the check. A custom module turns the local rule into a recurring finding. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A custom module turns the local rule into a recurring finding.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A custom module turns the local rule into a recurring finding.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom module turns the local rule into a recurring finding.
- **D:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A custom module turns the local rule into a recurring finding.

### Question 78 — C

Answer: Write a custom organization policy constraint for the rule. A custom constraint blocks the configuration change outright. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom constraint blocks the configuration change outright.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom constraint blocks the configuration change outright.
- **C:** Correct. In this case: A custom constraint blocks the configuration change outright.
- **D:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A custom constraint blocks the configuration change outright.

### Question 79 — D

Answer: Enable VPC Flow Logs on the subnets. Flow logs record the five-tuples for later analysis. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the five-tuples for later analysis.
- **B:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the five-tuples for later analysis.
- **C:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Flow logs record the five-tuples for later analysis.
- **D:** Correct. In this case: Flow logs record the five-tuples for later analysis.

### Question 80 — B, C

Answers: Deploy Cloud IDS on the network; Mirror the production traffic to a collector with Packet Mirroring. Cloud IDS raises the threat finding, and Packet Mirroring copies the payload. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Cloud IDS raises the threat finding, and Packet Mirroring copies the payload.
- **B:** Correct. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. In this case: Cloud IDS raises the threat finding, and Packet Mirroring copies the payload.
- **C:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Cloud IDS raises the threat finding, and Packet Mirroring copies the payload.
- **D:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Cloud IDS raises the threat finding, and Packet Mirroring copies the payload.
- **E:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Cloud IDS raises the threat finding, and Packet Mirroring copies the payload.

### Question 81 — C

Answer: Query the logs through Log Analytics. Log Analytics turns the destination into a queryable store. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Log Analytics turns the destination into a queryable store.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: Log Analytics turns the destination into a queryable store.
- **C:** Correct. In this case: Log Analytics turns the destination into a queryable store.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Log Analytics turns the destination into a queryable store.

### Question 82 — D

Answer: Route security logs to a dedicated project with its own retention. A dedicated log project keeps evidence away from those principals. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A dedicated log project keeps evidence away from those principals.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A dedicated log project keeps evidence away from those principals.
- **C:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A dedicated log project keeps evidence away from those principals.
- **D:** Correct. In this case: A dedicated log project keeps evidence away from those principals.

### Question 83 — C

Answer: Lower the log volume by disabling data access logs. Disabling the logs removes the record of who read the data. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **B:** Incorrect for this question. A dedicated log project keeps the evidence away from the principals who generate it. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **C:** Correct. In this case: Disabling the logs removes the record of who read the data.
- **D:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: Disabling the logs removes the record of who read the data.

### Question 84 — A

Answer: Read the Admin Activity audit log for the change. Admin Activity records the change and the identity, and is always on. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Admin Activity records the change and the identity, and is always on.
- **B:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the change and the identity, and is always on.
- **C:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the change and the identity, and is always on.
- **D:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Admin Activity records the change and the identity, and is always on.

### Question 85 — D

Answer: Enable Data Access audit logs for the service. Data Access logs record the read and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Data Access logs record the read and must be turned on per service.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Data Access logs record the read and must be turned on per service.
- **C:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Data Access logs record the read and must be turned on per service.
- **D:** Correct. In this case: Data Access logs record the read and must be turned on per service.

### Question 86 — D

Answer: Create an aggregated sink at the organisation level. An aggregated sink includes every project beneath the node. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: An aggregated sink includes every project beneath the node.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink includes every project beneath the node.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink includes every project beneath the node.
- **D:** Correct. In this case: An aggregated sink includes every project beneath the node.

### Question 87 — B

Answer: Export the entries to the external SIEM through Pub/Sub. Pub/Sub carries the entries out without opening an inbound path. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Pub/Sub carries the entries out without opening an inbound path.
- **B:** Correct. In this case: Pub/Sub carries the entries out without opening an inbound path.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Pub/Sub carries the entries out without opening an inbound path.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Pub/Sub carries the entries out without opening an inbound path.

### Question 88 — A

Answer: Review the Security Command Center findings for the project. Security Command Center collects the findings for the enabled tier. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Security Command Center collects the findings for the enabled tier.
- **B:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **C:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center collects the findings for the enabled tier.

### Question 89 — A, B

Answers: Publish new findings to Pub/Sub for the response pipeline; Name an owner for each control. A notification channel feeds the automation, and a named owner prevents a silent closure. A notification channel lets the response automation react to a finding as it is created. A named owner is what turns a control list into something that is actually operated. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A named owner is what turns a control list into something that is actually operated. In this case: A notification channel feeds the automation, and a named owner prevents a silent closure.
- **B:** Correct. A notification channel lets the response automation react to a finding as it is created. In this case: A notification channel feeds the automation, and a named owner prevents a silent closure.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A notification channel feeds the automation, and a named owner prevents a silent closure.
- **D:** Incorrect for this question. An unexplained closure destroys the record that the finding was ever reviewed. Why the correct answer wins: A notification channel feeds the automation, and a named owner prevents a silent closure.
- **E:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A notification channel feeds the automation, and a named owner prevents a silent closure.

### Question 90 — A

Answer: Document which controls Google operates and which the customer must implement. The shared responsibility split names which controls the customer operates. The shared responsibility split decides what the customer actually has to evidence. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The shared responsibility split names which controls the customer operates.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The shared responsibility split names which controls the customer operates.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The shared responsibility split names which controls the customer operates.
- **D:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The shared responsibility split names which controls the customer operates.

### Question 91 — A, C

Answers: Document which controls Google operates and which the customer must implement; Name an owner for each control. The split names the layers, and a named owner makes the control operated rather than listed. The shared responsibility split decides what the customer actually has to evidence. A named owner is what turns a control list into something that is actually operated. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The split names the layers, and a named owner makes the control operated rather than listed.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The split names the layers, and a named owner makes the control operated rather than listed.
- **C:** Correct. A named owner is what turns a control list into something that is actually operated. In this case: The split names the layers, and a named owner makes the control operated rather than listed.
- **D:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The split names the layers, and a named owner makes the control operated rather than listed.
- **E:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The split names the layers, and a named owner makes the control operated rather than listed.

### Question 92 — C

Answer: Create the folder as an Assured Workloads environment. Assured Workloads applies the regime controls to the folder. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: Assured Workloads applies the regime controls to the folder.
- **B:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the regime controls to the folder.
- **C:** Correct. In this case: Assured Workloads applies the regime controls to the folder.
- **D:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the regime controls to the folder.

### Question 93 — D

Answer: Record the regime in a spreadsheet and configure each control by hand. A manual mapping drifts when a project is created without the same settings. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **B:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **C:** Incorrect for this question. Assured Workloads applies the personnel and location controls the regime requires to the folder. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **D:** Correct. In this case: A manual mapping drifts when a project is created without the same settings.

### Question 94 — B

Answer: Turn on Access Transparency and read its logs. Access Transparency records operator access to content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records operator access to content.
- **B:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records operator access to content.
- **C:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records operator access to content.
- **D:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records operator access to content.

### Question 95 — B

Answer: Require Access Approval before an operator may read the content. Access Approval turns operator access into a request the customer grants. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.
- **B:** Correct. In this case: Access Approval turns operator access into a request the customer grants.
- **C:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.
- **D:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.

### Question 96 — B

Answer: Constrain the resources to the required region with a location organization policy. A location constraint blocks resources outside the permitted region. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **B:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks resources outside the permitted region.
- **C:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **D:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks resources outside the permitted region.

### Question 97 — B

Answer: Leave the default multi-region setting. A multi-region default places a copy outside the named region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **B:** Correct. In this case: A multi-region default places a copy outside the named region.
- **C:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A multi-region default places a copy outside the named region.

### Question 98 — D

Answer: Map each requirement to the control that satisfies it and the evidence it produces. A mapping names the control and the evidence for the clause. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **D:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: A mapping names the control and the evidence for the clause.

### Question 99 — D

Answer: Keep the audit evidence for the period the regime requires. A retention period for evidence is itself part of the control. A retention period for evidence is itself a control, because an expired record proves nothing. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A retention period for evidence is itself part of the control.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A retention period for evidence is itself part of the control.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A retention period for evidence is itself part of the control.
- **D:** Correct. A retention period for evidence is itself a control, because an expired record proves nothing. In this case: A retention period for evidence is itself part of the control.

### Question 100 — A

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A boundary decides which resources are in scope before the audit. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A boundary decides which resources are in scope before the audit.
- **B:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A boundary decides which resources are in scope before the audit.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A boundary decides which resources are in scope before the audit.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A boundary decides which resources are in scope before the audit.
