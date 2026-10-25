# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 2

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. Clinicians must sign in with the identity provider the hospital already runs, and no second password is allowed. What should be configured?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Configure single sign-on with a third-party identity provider over SAML
- C. Create a service account key and embed it in the application configuration
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 2. A merged charity wants one directory to serve both its workspace and its Google Cloud projects. What should hold the identities?

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Federate the workforce to Cloud Identity and enforce it as the identity source
- C. Restrict the project to the APIs it needs and review them on a schedule
- D. Assign the super administrator role to a dedicated break-glass account with hardware keys

### 3. A nurse who left three weeks ago still appears in the console. Which control was missing?

- A. Grant the role to a group and manage membership
- B. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- C. Have a team member update accounts by hand when the HR export arrives
- D. Give every platform lead the super administrator role for convenience

### 4. Accounts are created today by a ticket to one administrator who is currently on leave. What should replace the ticket?

- A. Grant the predefined role that matches the task
- B. Have a team member update accounts by hand when the HR export arrives
- C. Grant the role to a group and manage membership
- D. Drive joiner, mover, and leaver flows through the Admin SDK Directory API

### 5. Recovery must work while the directory is broken, and joiners must not wait on a person. Which two arrangements apply? Select two.

- A. Give every platform lead the super administrator role for convenience
- B. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- C. Create a service account key and embed it in the application configuration
- D. Have a team member update accounts by hand when the HR export arrives
- E. Assign the super administrator role to a dedicated break-glass account with hardware keys

### 6. A supplier's own Okta tenant must open two APIs for ninety days without a Google account being issued. What should be configured?

- A. Create a service account key and embed it in the application configuration
- B. Federate the partner workforce with Workforce Identity Federation
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Create a Cloud Identity user per contractor and issue long-lived passwords

### 7. Contractors were each given a local Google account and two hundred of them were never removed. What is the flaw?

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Federate the partner workforce with Workforce Identity Federation
- C. Set the domain restricted sharing constraint on the organisation
- D. Configure Workload Identity Federation for the external workload

### 8. Any virtual machine on the project can read the same bucket because of the account the job inherited. What causes that?

- A. Create a service account key and embed it in the application configuration
- B. Run the workload as the default Compute Engine service account
- C. Grant the basic Editor role to the team
- D. Create a dedicated service account per workload with only the roles it needs

### 9. Each job must be attributable in the audit log, and no job may hold more than its task needs. Which two changes apply? Select two.

- A. Run the workload as the default Compute Engine service account
- B. Grant the basic Editor role to the team
- C. Grant the predefined role that matches the task
- D. Create a service account key and embed it in the application configuration
- E. Create a dedicated service account per workload with only the roles it needs

### 10. A pipeline account holds a role that lets it delete datasets it only needs to read. What should replace the grant?

- A. Grant the predefined role that matches the task
- B. Grant the basic Editor role to the team
- C. Give every platform lead the super administrator role for convenience
- D. Build a custom role containing exactly the permissions the task uses

### 11. A key found in a public repository had been valid for two years. What kind of credential was it?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Issue a short-lived access token through impersonation or metadata
- C. Create a service account key and embed it in the application configuration
- D. Configure Workload Identity Federation for the external workload

### 12. A virtual machine must call an API for the length of one job with nothing written to disk. What should it use?

- A. Issue a short-lived access token through impersonation or metadata
- B. Set the credential as a plain environment variable in the deployment
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Create a service account key and embed it in the application configuration

### 13. Nobody can attribute a call to a person because the caller used a shared key. What would have made it attributable?

- A. Create a service account key and embed it in the application configuration
- B. Issue a short-lived access token through impersonation or metadata
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Set the credential as a plain environment variable in the deployment

### 14. A function in another cloud must write to a bucket with no secret stored in the function itself. What should be configured?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Create a service account key and embed it in the application configuration
- C. Configure Workload Identity Federation for the external workload
- D. Set the credential as a plain environment variable in the deployment

### 15. The identity pool accepts tokens from a multi-tenant provider, so any tenant can currently impersonate the account. What should be added?

- A. Set the domain restricted sharing constraint on the organisation
- B. Create a service account key and embed it in the application configuration
- C. Configure Workload Identity Federation for the external workload
- D. Restrict the Workload Identity pool with an attribute condition on the subject

### 16. An on-call engineer must debug with a production account's permissions for thirty minutes. What should be granted?

- A. Create a service account key and embed it in the application configuration
- B. Issue a short-lived access token through impersonation or metadata
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Grant the role through Privileged Access Manager with an approval and a time limit

### 17. A person must be able to act as the account, and the action must be traceable to that person. Which two controls apply? Select two.

- A. Hand the caller a JSON key for the service account instead
- B. Create a service account key and embed it in the application configuration
- C. Set the credential as a plain environment variable in the deployment
- D. Grant the caller the Service Account Token Creator role on the target account
- E. Read the Admin Activity audit log for the change

### 18. The board wants a second factor that survives a phished password on console sign-in. What should be enforced?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Set a session length and reauthentication policy for the admin console
- C. Let each user decide whether to enrol in 2-step verification
- D. Enforce 2-step verification for the whole organisation

### 19. An attacker who steals a password keeps the console session alive for weeks. What shortens that window?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Set a session length and reauthentication policy for the admin console
- C. Restrict the project to the APIs it needs and review them on a schedule
- D. Let each user decide whether to enrol in 2-step verification

### 20. A contractor's Owner grant was created for a one-week task and is still live two years later. What should have been used?

- A. Grant the basic Editor role to the team
- B. Grant the privileged role permanently and review it once a year
- C. Grant the role to a group and manage membership
- D. Grant the role through Privileged Access Manager with an approval and a time limit

### 21. Standing privilege must disappear, and a reviewer must see who actually used the role. Which two controls apply? Select two.

- A. Grant the basic Editor role to the team
- B. Grant the role through Privileged Access Manager with an approval and a time limit
- C. Grant the privileged role permanently and review it once a year
- D. Read the Policy Analyzer output before removing an unused grant
- E. Grant the role to a group and manage membership

### 22. A grant must apply only while the holder is on the on-call rotation. What should be added?

- A. Write an Access Context Manager access level and bind it to the perimeter
- B. Enforce the constraint with an organization policy
- C. Grant the predefined role that matches the task
- D. Add an IAM condition that limits the grant to a time window and a resource prefix

### 23. A project-level allow must lose to a prohibition written at the organisation. What makes that work?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Attach an IAM deny policy to the organisation
- D. Enforce the constraint with an organization policy

### 24. Two hundred projects must be grouped by business unit with one policy per group. What should be built?

- A. Create a folder per environment and attach the policy at the folder
- B. Create a sink in each project and hope nobody adds a project
- C. Ask each project owner to disable the setting
- D. Have a team member update accounts by hand when the HR export arrives

### 25. A constraint must bind a project that does not exist yet. Where should it be attached?

- A. Ask each project owner to disable the setting
- B. Enforce the constraint with an organization policy
- C. Create a folder per environment and attach the policy at the folder
- D. Add an IAM condition that limits the grant to a time window and a resource prefix

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. A team must open a lab port without waiting for a central ticket. Which control allows that safely?

- A. Allow all egress and rely on the application to be careful
- B. Deploy a hierarchical firewall policy at the organisation or folder level
- C. Create a service perimeter with VPC Service Controls
- D. Rely on the default VPC firewall rules in each project

### 27. A central team must own the deny rules while each project still tunes its own allows. Which two layers apply? Select two.

- A. Rely on the default VPC firewall rules in each project
- B. Allow all egress and rely on the application to be careful
- C. Attach a Cloud Armor security policy to the backend service
- D. Create a service perimeter with VPC Service Controls
- E. Deploy a hierarchical firewall policy at the organisation or folder level

### 28. An upload to a file-sharing domain must be blocked while that domain's API stays reachable. What should be enabled?

- A. Filter on address and port only and allow the rest
- B. Attach a Cloud Armor security policy to the backend service
- C. Enable layer 7 inspection on the firewall policy for the egress rule
- D. Route the egress through Secure Web Proxy

### 29. A rule allows an address range and therefore permits every host inside it. What is being described?

- A. Enable layer 7 inspection on the firewall policy for the egress rule
- B. Put Identity-Aware Proxy in front of the application
- C. Filter on address and port only and allow the rest
- D. Deploy Cloud IDS on the network

### 30. An API is being scraped by a botnet spread over many addresses and per-IP throttling is not enough. What should stop it?

- A. Attach a Cloud Armor security policy to the backend service
- B. Put Identity-Aware Proxy in front of the application
- C. Rely on the default VPC firewall rules in each project
- D. Add a web application firewall rule in the application framework

### 31. Injection attempts must be blocked, and a crawler must be scored separately from a person. Which two controls apply? Select two.

- A. Attach a Cloud Armor security policy to the backend service
- B. Put Identity-Aware Proxy in front of the application
- C. Add a web application firewall rule in the application framework
- D. Terminate TLS at the load balancer with a managed certificate
- E. Enable Cloud Armor bot management on the policy

### 32. A staging application must be reachable only by the QA group and by no VPN client. What should be placed in front?

- A. Attach a Cloud Armor security policy to the backend service
- B. Deploy the instances with internal IP addresses only
- C. Put Identity-Aware Proxy in front of the application
- D. Publish the application only through a VPN concentrator

### 33. A VPN login gives every employee the same reach as the platform engineers. What is the flaw?

- A. Attach a Cloud Armor security policy to the backend service
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Put Identity-Aware Proxy in front of the application
- D. Publish the application only through a VPN concentrator

### 34. Certificates for sixty internal services expire one by one and nobody tracks them. What should be introduced?

- A. Enable Private Google Access on the subnet
- B. Issue internal certificates from Certificate Authority Service
- C. Generate a self-signed certificate on each instance
- D. Terminate TLS at the load balancer with a managed certificate

### 35. A customer requires the TLS handshake to reach the backend untouched. What should be configured?

- A. Generate a self-signed certificate on each instance
- B. Terminate TLS at the load balancer with a managed certificate
- C. Filter on address and port only and allow the rest
- D. Pass encrypted traffic straight through to the instance

### 36. Build agents must browse only an allowlisted set of destinations. What should the egress be routed through?

- A. Place Cloud NAT in front of the private instances
- B. Route the egress through Secure Web Proxy
- C. Allow all egress and rely on the application to be careful
- D. Run a NAT instance on a Compute Engine virtual machine

### 37. A phishing domain must resolve to nothing for hosts inside the corporate VPC. What should be written?

- A. Use a Cloud DNS response policy to block the known-bad domain
- B. Route the egress through Secure Web Proxy
- C. Turn on DNSSEC for the public zone
- D. Enable Private Google Access on the subnet

### 38. A developer enabled a new API last month and nobody noticed. What should be reviewed and reduced?

- A. Create a service perimeter with VPC Service Controls
- B. Restrict the project to the APIs it needs and review them on a schedule
- C. Write an Access Context Manager access level and bind it to the perimeter
- D. Enforce the constraint with an organization policy

### 39. Traffic must never traverse the internet, and the workload must stay unreachable inbound. Which two settings apply? Select two.

- A. Place Cloud NAT in front of the private instances
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Allow all egress and rely on the application to be careful
- D. Deploy the instances with internal IP addresses only
- E. Enable Private Google Access on the subnet

### 40. Two teams need private reachability and neither will surrender ownership of its own VPC. What should be configured?

- A. Host the workload in a Shared VPC service project
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Place Cloud NAT in front of the private instances
- D. Peer the two VPC networks and scope the firewall rules to the peer

### 41. A three-tier application lets the web tier reach the database directly. What should be redesigned?

- A. Give each tier its own subnet and allow only the flows between adjacent tiers
- B. Rely on the default VPC firewall rules in each project
- C. Allow all egress and rely on the application to be careful
- D. Peer the two VPC networks and scope the firewall rules to the peer

### 42. Copying a dataset into a personal project must be blocked even though IAM permits the read. What should be created?

- A. Make the bucket public but unlisted
- B. Create a service perimeter with VPC Service Controls
- C. Grant authorised views or dataset-level IAM rather than table reads
- D. Rely on IAM to prevent data leaving the project

### 43. An engineer believes that IAM alone prevents data leaving the project. What is wrong with that belief?

- A. Attach an IAM deny policy to the organisation
- B. Create a service perimeter with VPC Service Controls
- C. Rely on IAM to prevent data leaving the project
- D. Grant authorised views or dataset-level IAM rather than table reads

### 44. A factory needs four gigabits on a private circuit with a redundant path. What should be provisioned?

- A. Provision a Dedicated Interconnect with two attachments
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Build an HA VPN tunnel pair with two interfaces
- D. Build a single classic VPN tunnel

### 45. The hybrid link must be private, and the primary must survive one path failure. Which two services apply? Select two.

- A. Provision a Dedicated Interconnect with two attachments
- B. Build a single classic VPN tunnel
- C. Place Cloud NAT in front of the private instances
- D. Run a NAT instance on a Compute Engine virtual machine
- E. Build an HA VPN tunnel pair with two interfaces

### 46. An application must reach a Google API with no external address and no internet route. What should be enabled?

- A. Enable Private Google Access on the subnet
- B. Place Cloud NAT in front of the private instances
- C. Build a single classic VPN tunnel
- D. Publish the service through a Private Service Connect endpoint

### 47. One legacy NAT virtual machine serves every outbound flow and is now a bottleneck. What should replace it?

- A. Allow all egress and rely on the application to be careful
- B. Terminate TLS at the load balancer with a managed certificate
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Place Cloud NAT in front of the private instances

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. A quarterly review asks where card data is stored and no inventory exists. What should have been run?

- A. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- B. Replace the value with an unsalted hash
- C. Make the bucket public but unlisted
- D. Ask the team to report which tables they believe hold personal data

### 49. Two regions scan the same columns with different infoTypes and the counts do not agree. What should be shared?

- A. Save a Sensitive Data Protection inspect template and reuse it
- B. Set the credential as a plain environment variable in the deployment
- C. Reuse a stored de-identification template across pipelines
- D. Ask the team to report which tables they believe hold personal data

### 50. A team asks engineers to write down which tables they think hold personal data. What is the weakness?

- A. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- B. Replace the value with an unsalted hash
- C. Ask the team to report which tables they believe hold personal data
- D. Save a Sensitive Data Protection inspect template and reuse it

### 51. Analysts must see that a card was on file while seeing only the last four digits. What should be applied?

- A. Replace the value with a pseudonym from a crypto key
- B. Redact the matched values with a de-identification template
- C. Replace the value with an unsalted hash
- D. Apply format-preserving encryption to the card number field

### 52. A cohort study must still join on a patient identifier, and a billing reader needs a sixteen-digit column it cannot decipher. Which two methods apply? Select two.

- A. Redact the matched values with a de-identification template
- B. Replace the value with a pseudonym from a crypto key
- C. Apply format-preserving encryption to the card number field
- D. Generate the key in the application and store it beside the data
- E. Replace the value with an unsalted hash

### 53. A hash of a phone number column can be reversed with a precomputed table. What is the weakness?

- A. Replace the value with an unsalted hash
- B. Replace the value with a pseudonym from a crypto key
- C. Apply format-preserving encryption to the card number field
- D. Redact the matched values with a de-identification template

### 54. A dashboard tool must query aggregates without any access to the raw table. What should be granted?

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Put the database password in the application config file
- C. Grant the analyst the ability to export the whole table to a bucket
- D. Make the bucket public but unlisted

### 55. An analyst asks for the right to export a table to a bucket they own. What risk does that create?

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Use Cloud SQL IAM database authentication for the application
- C. Grant the analyst the ability to export the whole table to a bucket
- D. Set an allUsers object ACL on the specific file

### 56. A Cloud SQL application must connect without a stored database password. What should be enabled?

- A. Use Cloud SQL IAM database authentication for the application
- B. Set the credential as a plain environment variable in the deployment
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Put the database password in the application config file

### 57. A secret was printed in a build log and must be rotated without a redeploy. Where should it live?

- A. Put the database password in the application config file
- B. Set the credential as a plain environment variable in the deployment
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Generate the key in the application and store it beside the data

### 58. A credential must never appear in a build log, and only one workload may read it. Which two choices apply? Select two.

- A. Set the credential as a plain environment variable in the deployment
- B. Store the credential in Secret Manager and grant the workload the secret accessor role
- C. Create a dedicated service account per workload with only the roles it needs
- D. Generate the key in the application and store it beside the data
- E. Put the database password in the application config file

### 59. A request forgery attack reads the instance token from the metadata address. What should reject the call?

- A. Require the metadata server header on every request
- B. Place Cloud NAT in front of the private instances
- C. Deploy the instances with internal IP addresses only
- D. Enable OS Login and turn off project-wide SSH keys

### 60. Personal SSH keys sit in the project metadata and the leavers' keys were never removed. What should be enabled?

- A. Require the metadata server header on every request
- B. Enable OS Login and turn off project-wide SSH keys
- C. Create a service account key and embed it in the application configuration
- D. Enforce a password policy with a minimum length and a reuse ban

### 61. A regulator requires the customer to hold the key that protects a bucket. What should be configured?

- A. Rely on Google default encryption at rest
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Generate the key in the application and store it beside the data
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 62. A startup wants encryption at rest with the least operational work and no key policy. What applies?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Rely on Google default encryption at rest

### 63. An auditor asks whether key material can sit outside Google infrastructure entirely. What should be used?

- A. Generate the key in the application and store it beside the data
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Import the wrapping key into Cloud KMS

### 64. A hardware module in the customer data centre must wrap the warehouse data. What should be configured?

- A. Import the wrapping key into Cloud KMS
- B. Set a rotation period on the key
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 65. Existing wrapped objects must stay readable, and the wrapping key must become auditable inside KMS. Which two steps apply? Select two.

- A. Generate the key in the application and store it beside the data
- B. Import the wrapping key into Cloud KMS
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Set a rotation period on the key
- E. Rely on Google default encryption at rest

### 66. Policy requires a new key version every ninety days. What should be configured?

- A. Set a rotation period on the key
- B. Disable the key version and re-wrap the data
- C. Import the wrapping key into Cloud KMS
- D. Generate the key in the application and store it beside the data

### 67. An incident requires immediate loss of readability for one dataset. What should be done?

- A. Disable the key version and re-wrap the data
- B. Import the wrapping key into Cloud KMS
- C. Set a rotation period on the key
- D. Rely on Google default encryption at rest

### 68. A bank requires that the hypervisor cannot read guest memory while the workload runs. What should be used?

- A. Run the workload on a Confidential VM
- B. Enable OS Login and turn off project-wide SSH keys
- C. Rely on Google default encryption at rest
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 69. A multi-tenant cluster must protect pod memory from the node operator. What should be used?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Run the workload on a Confidential VM
- C. Enable OS Login and turn off project-wide SSH keys
- D. Run the pod in a Confidential GKE node pool

### 70. Objects must disappear after four hundred days, and an administrator must not be able to delete them sooner. Which two controls apply? Select two.

- A. Attach an object lifecycle rule that keeps the required retention
- B. Allow all egress and rely on the application to be careful
- C. Set an allUsers object ACL on the specific file
- D. Make the bucket public but unlisted
- E. Apply a retention policy with bucket lock

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A base image with a known vulnerability reached production because nothing inspects the build output. What should be added?

- A. Scan the running image in production once a quarter
- B. Let each team patch its own instances when convenient
- C. Enforce a Binary Authorization policy that requires an attested image
- D. Add an Artifact Analysis scan to the CI pipeline

### 72. Images must be blocked at build time, and the fleet must also be checked for what already shipped. Which two checks apply? Select two.

- A. Add an Artifact Analysis scan to the CI pipeline
- B. Let each team patch its own instances when convenient
- C. Scan the running image in production once a quarter
- D. Allow all egress and rely on the application to be careful
- E. Deploy with Binary Authorization in dry-run mode only

### 73. Only images signed by the release pipeline may run in the cluster. What should be enforced?

- A. Deploy the instances with internal IP addresses only
- B. Deploy with Binary Authorization in dry-run mode only
- C. Enforce a Binary Authorization policy that requires an attested image
- D. Attach a Cloud Armor security policy to the backend service

### 74. The team wants to see what a new admission policy would block without breaking the release. What should be used?

- A. Add an Artifact Analysis scan to the CI pipeline
- B. Enforce a Binary Authorization policy that requires an attested image
- C. Deploy with Binary Authorization in dry-run mode only
- D. Deploy Cloud IDS on the network

### 75. A base image must come from a documented minimal source with no extra accounts. What should be built?

- A. Schedule patch jobs across the fleet with VM Manager
- B. Scan the running image in production once a quarter
- C. Build the base image from a hardened source with a documented baseline
- D. Let each team patch its own instances when convenient

### 76. Two hundred virtual machines missed last month's kernel patch. What should be introduced?

- A. Schedule patch jobs across the fleet with VM Manager
- B. Build the base image from a hardened source with a documented baseline
- C. Compare the deployed configuration with the intended state on a schedule
- D. Let each team patch its own instances when convenient

### 77. A setting changed outside the pipeline and nobody noticed for months. What should be added?

- A. Deploy a Security Health Analytics custom module for the check
- B. Write a custom organization policy constraint for the rule
- C. Lower the log volume by disabling data access logs
- D. Compare the deployed configuration with the intended state on a schedule

### 78. A misconfiguration must appear as a finding, and a repeat of it must be blocked. Which two mechanisms apply? Select two.

- A. Deploy a Security Health Analytics custom module for the check
- B. Have a team member update accounts by hand when the HR export arrives
- C. Write a custom organization policy constraint for the rule
- D. Lower the log volume by disabling data access logs
- E. Compare the deployed configuration with the intended state on a schedule

### 79. A compromised host talked to a command-and-control address and no record of the flows exists. What should have been enabled?

- A. Lower the log volume by disabling data access logs
- B. Deploy Cloud IDS on the network
- C. Enable VPC Flow Logs on the subnets
- D. Mirror the production traffic to a collector with Packet Mirroring

### 80. Forensics needs the actual payload of a suspicious session. What should be used?

- A. Deploy Cloud IDS on the network
- B. Enable VPC Flow Logs on the subnets
- C. Mirror the production traffic to a collector with Packet Mirroring
- D. Query the logs through Log Analytics

### 81. An inline sensor must raise a threat finding on east-west traffic. What should be deployed?

- A. Enable VPC Flow Logs on the subnets
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Attach a Cloud Armor security policy to the backend service
- D. Deploy Cloud IDS on the network

### 82. An auditor must read logs that the project owner cannot edit. What should change?

- A. Lower the log volume by disabling data access logs
- B. Route security logs to a dedicated project with its own retention
- C. Give the SIEM a service account key so it can pull the logs
- D. Create a sink in each project and hope nobody adds a project

### 83. Evidence must outlive the project, and the principal who generates it must not be able to edit it. Which two controls apply? Select two.

- A. Route security logs to a dedicated project with its own retention
- B. Lower the log volume by disabling data access logs
- C. Create a sink in each project and hope nobody adds a project
- D. Give the SIEM a service account key so it can pull the logs
- E. Create an aggregated sink at the organisation level

### 84. A change to an IAM binding must be attributable to a person. Which log provides that?

- A. Read the Admin Activity audit log for the change
- B. Enable VPC Flow Logs on the subnets
- C. Enable Data Access audit logs for the service
- D. Create a log sink that routes the entries to the destination

### 85. Nobody can tell whether a specific object was read last month. Which log was never enabled?

- A. Read the Admin Activity audit log for the change
- B. Create a log sink that routes the entries to the destination
- C. Enable VPC Flow Logs on the subnets
- D. Enable Data Access audit logs for the service

### 86. The SIEM must receive entries from every project, including the ones created later. What should be created?

- A. Create a log sink that routes the entries to the destination
- B. Create an aggregated sink at the organisation level
- C. Give the SIEM a service account key so it can pull the logs
- D. Create a sink in each project and hope nobody adds a project

### 87. The SIEM team wants to pull logs with a service account key that never expires. What is the flaw?

- A. Set the credential as a plain environment variable in the deployment
- B. Export the entries to the external SIEM through Pub/Sub
- C. Lower the log volume by disabling data access logs
- D. Give the SIEM a service account key so it can pull the logs

### 88. A finding about a public bucket must appear without anyone writing a query. What provides it?

- A. Query the logs through Log Analytics
- B. Review the Security Command Center findings for the project
- C. Compare the deployed configuration with the intended state on a schedule
- D. Deploy a Security Health Analytics custom module for the check

### 89. An engineer closes a finding with no comment and no owner. What practice is missing?

- A. Name an owner for each control
- B. Keep the audit evidence for the period the regime requires
- C. Close the finding as a false positive without a comment
- D. Publish new findings to Pub/Sub for the response pipeline

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. A customer asks whether Google or the customer configures the firewall rules. What answers the question?

- A. State in the policy document that the environment is compliant
- B. Assume Google secures every layer once the data is in the cloud
- C. Declare the whole organisation in scope for every regime
- D. Document which controls Google operates and which the customer must implement

### 91. Legal claims Google protects everything once the data is uploaded. What is wrong with that claim?

- A. State in the policy document that the environment is compliant
- B. Document which controls Google operates and which the customer must implement
- C. Declare the whole organisation in scope for every regime
- D. Assume Google secures every layer once the data is in the cloud

### 92. A regime requires support personnel to be located in one country for every project in a folder. What should be created?

- A. Ask each project owner to disable the setting
- B. Constrain the resources to the required region with a location organization policy
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Create the folder as an Assured Workloads environment

### 93. The environment must carry the regime controls and someone must answer for each one. Which two practices apply? Select two.

- A. State in the policy document that the environment is compliant
- B. Declare the whole organisation in scope for every regime
- C. Create the folder as an Assured Workloads environment
- D. Record the regime in a spreadsheet and configure each control by hand
- E. Name an owner for each control

### 94. A customer must know that a support engineer opened their bucket. What should be enabled?

- A. Require Access Approval before an operator may read the content
- B. Read the Admin Activity audit log for the change
- C. Enable Data Access audit logs for the service
- D. Turn on Access Transparency and read its logs

### 95. A customer must approve each operator access before it happens. What should be required?

- A. Turn on Access Transparency and read its logs
- B. Create a service perimeter with VPC Service Controls
- C. Require Access Approval before an operator may read the content
- D. Write an Access Context Manager access level and bind it to the perimeter

### 96. Data must never leave the European Union, including in a dataset created next quarter, by accident. What should be enforced?

- A. Constrain the resources to the required region with a location organization policy
- B. Declare the whole organisation in scope for every regime
- C. Leave the default multi-region setting
- D. Record the regime in a spreadsheet and configure each control by hand

### 97. A bucket was created in the default location and the contract names a single country. What is the cause?

- A. Constrain the resources to the required region with a location organization policy
- B. Leave the default multi-region setting
- C. Declare the whole organisation in scope for every regime
- D. Record the regime in a spreadsheet and configure each control by hand

### 98. The auditor wants one page linking each clause to a control and to its evidence. What should be produced?

- A. State in the policy document that the environment is compliant
- B. Map each requirement to the control that satisfies it and the evidence it produces
- C. Declare the whole organisation in scope for every regime
- D. Assume Google secures every layer once the data is in the cloud

### 99. A control exists in the list and nobody can say who operates it. What is missing?

- A. State in the policy document that the environment is compliant
- B. Name an owner for each control
- C. Declare the whole organisation in scope for every regime
- D. Keep the audit evidence for the period the regime requires

### 100. The audit must exclude the sandbox projects from the first day. What should be agreed beforehand?

- A. State in the policy document that the environment is compliant
- B. Record the regime in a spreadsheet and configure each control by hand
- C. Draw the compliance boundary around the projects and services that hold the regulated data
- D. Declare the whole organisation in scope for every regime

---

## Answer key and explanations

### Question 1 — B

Answer: Configure single sign-on with a third-party identity provider over SAML. SAML SSO keeps authentication with the existing provider while Google Cloud authorises the session. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: SAML SSO keeps authentication with the existing provider while Google Cloud authorises the session.
- **B:** Correct. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. In this case: SAML SSO keeps authentication with the existing provider while Google Cloud authorises the session.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: SAML SSO keeps authentication with the existing provider while Google Cloud authorises the session.
- **D:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: SAML SSO keeps authentication with the existing provider while Google Cloud authorises the session.

### Question 2 — B

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory that both the workspace and the cloud grants resolve against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Cloud Identity is the directory that both the workspace and the cloud grants resolve against.
- **B:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory that both the workspace and the cloud grants resolve against.
- **C:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: Cloud Identity is the directory that both the workspace and the cloud grants resolve against.
- **D:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Cloud Identity is the directory that both the workspace and the cloud grants resolve against.

### Question 3 — B

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK lifecycle automation is the step that suspends the account when the source record changes. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The Admin SDK lifecycle automation is the step that suspends the account when the source record changes.
- **B:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK lifecycle automation is the step that suspends the account when the source record changes.
- **C:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK lifecycle automation is the step that suspends the account when the source record changes.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: The Admin SDK lifecycle automation is the step that suspends the account when the source record changes.

### Question 4 — D

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK Directory API applies the change without waiting for one person. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: The Admin SDK Directory API applies the change without waiting for one person.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK Directory API applies the change without waiting for one person.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The Admin SDK Directory API applies the change without waiting for one person.
- **D:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK Directory API applies the change without waiting for one person.

### Question 5 — B, E

Answers: Assign the super administrator role to a dedicated break-glass account with hardware keys; Drive joiner, mover, and leaver flows through the Admin SDK Directory API. A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue.
- **B:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue.
- **D:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue.
- **E:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: A break-glass super administrator keeps recovery alive, and the lifecycle API removes the manual queue.

### Question 6 — B

Answer: Federate the partner workforce with Workforce Identity Federation. Workforce Identity Federation accepts the supplier provider directly. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workforce Identity Federation accepts the supplier provider directly.
- **B:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Workforce Identity Federation accepts the supplier provider directly.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Workforce Identity Federation accepts the supplier provider directly.
- **D:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Workforce Identity Federation accepts the supplier provider directly.

### Question 7 — A

Answer: Create a Cloud Identity user per contractor and issue long-lived passwords. A local account per contractor multiplies the accounts that must be reviewed and revoked. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A local account per contractor multiplies the accounts that must be reviewed and revoked.
- **B:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: A local account per contractor multiplies the accounts that must be reviewed and revoked.
- **C:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: A local account per contractor multiplies the accounts that must be reviewed and revoked.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A local account per contractor multiplies the accounts that must be reviewed and revoked.

### Question 8 — B

Answer: Run the workload as the default Compute Engine service account. The default service account is shared across every workload on the project. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The default service account is shared across every workload on the project.
- **B:** Correct. In this case: The default service account is shared across every workload on the project.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: The default service account is shared across every workload on the project.
- **D:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default service account is shared across every workload on the project.

### Question 9 — C, E

Answers: Create a dedicated service account per workload with only the roles it needs; Grant the predefined role that matches the task. A per-workload account attributes every call, and a predefined role keeps the grant to the task. A per-workload service account bounds the blast radius and makes audit records attributable. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A per-workload account attributes every call, and a predefined role keeps the grant to the task.
- **B:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A per-workload account attributes every call, and a predefined role keeps the grant to the task.
- **C:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: A per-workload account attributes every call, and a predefined role keeps the grant to the task.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A per-workload account attributes every call, and a predefined role keeps the grant to the task.
- **E:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A per-workload account attributes every call, and a predefined role keeps the grant to the task.

### Question 10 — A

Answer: Grant the predefined role that matches the task. A predefined read role carries only the permissions the task uses. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: A predefined read role carries only the permissions the task uses.
- **B:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A predefined read role carries only the permissions the task uses.
- **C:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A predefined read role carries only the permissions the task uses.
- **D:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: A predefined read role carries only the permissions the task uses.

### Question 11 — C

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key has no expiry unless someone sets one. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key has no expiry unless someone sets one.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key has no expiry unless someone sets one.
- **C:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key has no expiry unless someone sets one.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key has no expiry unless someone sets one.

### Question 12 — A

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token is minted for the run and leaves no file behind. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: A short-lived token is minted for the run and leaves no file behind.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token is minted for the run and leaves no file behind.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A short-lived token is minted for the run and leaves no file behind.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token is minted for the run and leaves no file behind.

### Question 13 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation records the caller that acted as the account. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation records the caller that acted as the account.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation records the caller that acted as the account.
- **C:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation records the caller that acted as the account.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation records the caller that acted as the account.

### Question 14 — C

Answer: Configure Workload Identity Federation for the external workload. Workload Identity Federation exchanges the function's own token for Google credentials. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Workload Identity Federation exchanges the function's own token for Google credentials.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workload Identity Federation exchanges the function's own token for Google credentials.
- **C:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Workload Identity Federation exchanges the function's own token for Google credentials.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Workload Identity Federation exchanges the function's own token for Google credentials.

### Question 15 — D

Answer: Restrict the Workload Identity pool with an attribute condition on the subject. An attribute condition limits which external identities may impersonate. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: An attribute condition limits which external identities may impersonate.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An attribute condition limits which external identities may impersonate.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: An attribute condition limits which external identities may impersonate.
- **D:** Correct. In this case: An attribute condition limits which external identities may impersonate.

### Question 16 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation lets the engineer act as the account for the session without its key. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation lets the engineer act as the account for the session without its key.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation lets the engineer act as the account for the session without its key.
- **C:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation lets the engineer act as the account for the session without its key.
- **D:** Incorrect for this question. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Why the correct answer wins: Impersonation lets the engineer act as the account for the session without its key.

### Question 17 — D, E

Answers: Grant the caller the Service Account Token Creator role on the target account; Read the Admin Activity audit log for the change. Impersonation grants the acting right, and Admin Activity records who used it. Impersonation lets a principal act as the service account without holding a key for it. Admin Activity records the configuration change and the identity that made it, and is always on. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A handed-out key cannot be scoped to one action and outlives the task that needed it. Why the correct answer wins: Impersonation grants the acting right, and Admin Activity records who used it.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation grants the acting right, and Admin Activity records who used it.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation grants the acting right, and Admin Activity records who used it.
- **D:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation grants the acting right, and Admin Activity records who used it.
- **E:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Impersonation grants the acting right, and Admin Activity records who used it.

### Question 18 — D

Answer: Enforce 2-step verification for the whole organisation. Enforced 2-step verification leaves the attacker with one factor only. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Enforced 2-step verification leaves the attacker with one factor only.
- **B:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: Enforced 2-step verification leaves the attacker with one factor only.
- **C:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: Enforced 2-step verification leaves the attacker with one factor only.
- **D:** Correct. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. In this case: Enforced 2-step verification leaves the attacker with one factor only.

### Question 19 — B

Answer: Set a session length and reauthentication policy for the admin console. A session length policy forces reauthentication after a fixed period. A session control limits how long a stolen browser session stays useful. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A session length policy forces reauthentication after a fixed period.
- **B:** Correct. A session control limits how long a stolen browser session stays useful. In this case: A session length policy forces reauthentication after a fixed period.
- **C:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: A session length policy forces reauthentication after a fixed period.
- **D:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A session length policy forces reauthentication after a fixed period.

### Question 20 — D

Answer: Grant the role through Privileged Access Manager with an approval and a time limit. Privileged Access Manager issues a grant that expires on its own. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Privileged Access Manager issues a grant that expires on its own.
- **B:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager issues a grant that expires on its own.
- **C:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager issues a grant that expires on its own.
- **D:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Privileged Access Manager issues a grant that expires on its own.

### Question 21 — B, D

Answers: Grant the role through Privileged Access Manager with an approval and a time limit; Read the Policy Analyzer output before removing an unused grant. Approved temporary grants remove the standing right, and Policy Analyzer shows the usage. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Approved temporary grants remove the standing right, and Policy Analyzer shows the usage.
- **B:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Approved temporary grants remove the standing right, and Policy Analyzer shows the usage.
- **C:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Approved temporary grants remove the standing right, and Policy Analyzer shows the usage.
- **D:** Correct. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. In this case: Approved temporary grants remove the standing right, and Policy Analyzer shows the usage.
- **E:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Approved temporary grants remove the standing right, and Policy Analyzer shows the usage.

### Question 22 — D

Answer: Add an IAM condition that limits the grant to a time window and a resource prefix. An IAM condition limits the grant to the stated circumstance. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: An IAM condition limits the grant to the stated circumstance.
- **B:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: An IAM condition limits the grant to the stated circumstance.
- **C:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: An IAM condition limits the grant to the stated circumstance.
- **D:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An IAM condition limits the grant to the stated circumstance.

### Question 23 — C

Answer: Attach an IAM deny policy to the organisation. A deny policy is evaluated above every allow beneath it. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **C:** Correct. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. In this case: A deny policy is evaluated above every allow beneath it.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.

### Question 24 — A

Answer: Create a folder per environment and attach the policy at the folder. A folder per unit carries one attachment for every project inside it. A folder boundary means one attachment covers every current and future project inside it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A folder boundary means one attachment covers every current and future project inside it. In this case: A folder per unit carries one attachment for every project inside it.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A folder per unit carries one attachment for every project inside it.
- **C:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A folder per unit carries one attachment for every project inside it.
- **D:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A folder per unit carries one attachment for every project inside it.

### Question 25 — B

Answer: Enforce the constraint with an organization policy. An organization policy inherits down to every project created later. An organization policy applies to every project beneath it, so a new project cannot opt out. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: An organization policy inherits down to every project created later.
- **B:** Correct. An organization policy applies to every project beneath it, so a new project cannot opt out. In this case: An organization policy inherits down to every project created later.
- **C:** Incorrect for this question. A folder boundary means one attachment covers every current and future project inside it. Why the correct answer wins: An organization policy inherits down to every project created later.
- **D:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: An organization policy inherits down to every project created later.

### Question 26 — D

Answer: Rely on the default VPC firewall rules in each project. Project-level rules let the owner tune their own environment within the hierarchy above. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Project-level rules let the owner tune their own environment within the hierarchy above.
- **B:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: Project-level rules let the owner tune their own environment within the hierarchy above.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Project-level rules let the owner tune their own environment within the hierarchy above.
- **D:** Correct. Project-level rules are editable by the project owner and are evaluated after the hierarchy. In this case: Project-level rules let the owner tune their own environment within the hierarchy above.

### Question 27 — A, E

Answers: Deploy a hierarchical firewall policy at the organisation or folder level; Rely on the default VPC firewall rules in each project. The hierarchical policy carries the denies, and project rules express the local allows. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Project-level rules are editable by the project owner and are evaluated after the hierarchy. In this case: The hierarchical policy carries the denies, and project rules express the local allows.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The hierarchical policy carries the denies, and project rules express the local allows.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: The hierarchical policy carries the denies, and project rules express the local allows.
- **D:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The hierarchical policy carries the denies, and project rules express the local allows.
- **E:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: The hierarchical policy carries the denies, and project rules express the local allows.

### Question 28 — C

Answer: Enable layer 7 inspection on the firewall policy for the egress rule. Layer 7 inspection reads the host and the application protocol. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the host and the application protocol.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Layer 7 inspection reads the host and the application protocol.
- **C:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the host and the application protocol.
- **D:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: Layer 7 inspection reads the host and the application protocol.

### Question 29 — C

Answer: Filter on address and port only and allow the rest. A layer 4 rule cannot see the destination host name in an allowed connection. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A layer 4 rule cannot see the destination host name in an allowed connection.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A layer 4 rule cannot see the destination host name in an allowed connection.
- **C:** Correct. In this case: A layer 4 rule cannot see the destination host name in an allowed connection.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: A layer 4 rule cannot see the destination host name in an allowed connection.

### Question 30 — A

Answer: Attach a Cloud Armor security policy to the backend service. Cloud Armor evaluates the request and rate-limits at the edge. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: Cloud Armor evaluates the request and rate-limits at the edge.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Cloud Armor evaluates the request and rate-limits at the edge.
- **C:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Cloud Armor evaluates the request and rate-limits at the edge.
- **D:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Cloud Armor evaluates the request and rate-limits at the edge.

### Question 31 — A, E

Answers: Attach a Cloud Armor security policy to the backend service; Enable Cloud Armor bot management on the policy. The security policy blocks the patterns, and bot management scores the automation. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: The security policy blocks the patterns, and bot management scores the automation.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the automation.
- **C:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the automation.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the automation.
- **E:** Correct. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. In this case: The security policy blocks the patterns, and bot management scores the automation.

### Question 32 — C

Answer: Put Identity-Aware Proxy in front of the application. IAP checks the identity against IAM for each request. IAP authenticates and authorises each request against IAM before it reaches the backend. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP checks the identity against IAM for each request.
- **B:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: IAP checks the identity against IAM for each request.
- **C:** Correct. IAP authenticates and authorises each request against IAM before it reaches the backend. In this case: IAP checks the identity against IAM for each request.
- **D:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP checks the identity against IAM for each request.

### Question 33 — D

Answer: Publish the application only through a VPN concentrator. A VPN authenticates the tunnel and not the individual request. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **C:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **D:** Correct. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. In this case: A VPN authenticates the tunnel and not the individual request.

### Question 34 — B

Answer: Issue internal certificates from Certificate Authority Service. Certificate Authority Service issues and revokes the private certificates in one place. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Certificate Authority Service issues and revokes the private certificates in one place.
- **B:** Correct. In this case: Certificate Authority Service issues and revokes the private certificates in one place.
- **C:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues and revokes the private certificates in one place.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Certificate Authority Service issues and revokes the private certificates in one place.

### Question 35 — D

Answer: Pass encrypted traffic straight through to the instance. Pass-through keeps the handshake end to end, at the cost of per-backend certificate work. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Pass-through keeps the handshake end to end, at the cost of per-backend certificate work.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Pass-through keeps the handshake end to end, at the cost of per-backend certificate work.
- **C:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Pass-through keeps the handshake end to end, at the cost of per-backend certificate work.
- **D:** Correct. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. In this case: Pass-through keeps the handshake end to end, at the cost of per-backend certificate work.

### Question 36 — B

Answer: Route the egress through Secure Web Proxy. Secure Web Proxy applies the allowlist to outbound web traffic. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Secure Web Proxy applies the allowlist to outbound web traffic.
- **B:** Correct. In this case: Secure Web Proxy applies the allowlist to outbound web traffic.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Secure Web Proxy applies the allowlist to outbound web traffic.
- **D:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Secure Web Proxy applies the allowlist to outbound web traffic.

### Question 37 — A

Answer: Use a Cloud DNS response policy to block the known-bad domain. A response policy overrides resolution for the named domain. A response policy overrides resolution for named domains inside the network. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A response policy overrides resolution for named domains inside the network. In this case: A response policy overrides resolution for the named domain.
- **B:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: A response policy overrides resolution for the named domain.
- **C:** Incorrect for this question. DNSSEC signs the answers so a resolver can detect a forged response. Why the correct answer wins: A response policy overrides resolution for the named domain.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: A response policy overrides resolution for the named domain.

### Question 38 — B

Answer: Restrict the project to the APIs it needs and review them on a schedule. The enabled API list is an attack surface that nothing in the workload requires. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The enabled API list is an attack surface that nothing in the workload requires.
- **B:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: The enabled API list is an attack surface that nothing in the workload requires.
- **C:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: The enabled API list is an attack surface that nothing in the workload requires.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: The enabled API list is an attack surface that nothing in the workload requires.

### Question 39 — D, E

Answers: Deploy the instances with internal IP addresses only; Enable Private Google Access on the subnet. An internal address blocks inbound reach, and Private Google Access keeps API calls private. An internal-only address means the workload cannot be reached from the internet at all. Private Google Access lets an instance with only an internal address reach Google APIs. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps API calls private.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps API calls private.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps API calls private.
- **D:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal address blocks inbound reach, and Private Google Access keeps API calls private.
- **E:** Correct. Private Google Access lets an instance with only an internal address reach Google APIs. In this case: An internal address blocks inbound reach, and Private Google Access keeps API calls private.

### Question 40 — D

Answer: Peer the two VPC networks and scope the firewall rules to the peer. Peering connects the two networks while each team keeps its own project. Peering gives private reachability while firewall rules still decide which flows are allowed. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Why the correct answer wins: Peering connects the two networks while each team keeps its own project.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Peering connects the two networks while each team keeps its own project.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Peering connects the two networks while each team keeps its own project.
- **D:** Correct. Peering gives private reachability while firewall rules still decide which flows are allowed. In this case: Peering connects the two networks while each team keeps its own project.

### Question 41 — A

Answer: Give each tier its own subnet and allow only the flows between adjacent tiers. Separate tier subnets let the rules express which tier may call which. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Separate tier subnets let the rules express which tier may call which.
- **B:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Separate tier subnets let the rules express which tier may call which.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Separate tier subnets let the rules express which tier may call which.
- **D:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Separate tier subnets let the rules express which tier may call which.

### Question 42 — B

Answer: Create a service perimeter with VPC Service Controls. A service perimeter blocks the copy whatever the grant says. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A service perimeter blocks the copy whatever the grant says.
- **B:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: A service perimeter blocks the copy whatever the grant says.
- **C:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: A service perimeter blocks the copy whatever the grant says.
- **D:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: A service perimeter blocks the copy whatever the grant says.

### Question 43 — C

Answer: Rely on IAM to prevent data leaving the project. An IAM grant still allows a copy out; only a perimeter stops the movement. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Why the correct answer wins: An IAM grant still allows a copy out; only a perimeter stops the movement.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An IAM grant still allows a copy out; only a perimeter stops the movement.
- **C:** Correct. In this case: An IAM grant still allows a copy out; only a perimeter stops the movement.
- **D:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: An IAM grant still allows a copy out; only a perimeter stops the movement.

### Question 44 — A

Answer: Provision a Dedicated Interconnect with two attachments. Dedicated Interconnect gives the private circuit with redundant attachments. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: Dedicated Interconnect gives the private circuit with redundant attachments.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.
- **C:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.
- **D:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Dedicated Interconnect gives the private circuit with redundant attachments.

### Question 45 — A, E

Answers: Provision a Dedicated Interconnect with two attachments; Build an HA VPN tunnel pair with two interfaces. The interconnect carries the private circuit, and an HA VPN pair covers the redundant path. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: The interconnect carries the private circuit, and an HA VPN pair covers the redundant path.
- **B:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: The interconnect carries the private circuit, and an HA VPN pair covers the redundant path.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: The interconnect carries the private circuit, and an HA VPN pair covers the redundant path.
- **D:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The interconnect carries the private circuit, and an HA VPN pair covers the redundant path.
- **E:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: The interconnect carries the private circuit, and an HA VPN pair covers the redundant path.

### Question 46 — A

Answer: Enable Private Google Access on the subnet. Private Google Access lets an internal-only instance reach the APIs. Private Google Access lets an instance with only an internal address reach Google APIs. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Private Google Access lets an instance with only an internal address reach Google APIs. In this case: Private Google Access lets an internal-only instance reach the APIs.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Private Google Access lets an internal-only instance reach the APIs.
- **C:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Private Google Access lets an internal-only instance reach the APIs.
- **D:** Incorrect for this question. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. Why the correct answer wins: Private Google Access lets an internal-only instance reach the APIs.

### Question 47 — D

Answer: Place Cloud NAT in front of the private instances. Cloud NAT is managed and removes the single host dependency. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT is managed and removes the single host dependency.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT is managed and removes the single host dependency.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT is managed and removes the single host dependency.
- **D:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT is managed and removes the single host dependency.

### Question 48 — A

Answer: Run a Sensitive Data Protection discovery scan over the storage and warehouse. A discovery scan produces the profile the review asks for. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: A discovery scan produces the profile the review asks for.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A discovery scan produces the profile the review asks for.
- **C:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A discovery scan produces the profile the review asks for.
- **D:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A discovery scan produces the profile the review asks for.

### Question 49 — A

Answer: Save a Sensitive Data Protection inspect template and reuse it. A saved inspect template keeps the detection rules identical in both scans. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A saved inspect template keeps the detection rules identical in both scans.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A saved inspect template keeps the detection rules identical in both scans.
- **C:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A saved inspect template keeps the detection rules identical in both scans.
- **D:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A saved inspect template keeps the detection rules identical in both scans.

### Question 50 — C

Answer: Ask the team to report which tables they believe hold personal data. A self-reported inventory misses the tables nobody remembered. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.
- **C:** Correct. In this case: A self-reported inventory misses the tables nobody remembered.
- **D:** Incorrect for this question. A saved template keeps the detection rules identical across scans, so results stay comparable. Why the correct answer wins: A self-reported inventory misses the tables nobody remembered.

### Question 51 — B

Answer: Redact the matched values with a de-identification template. Redaction replaces the matched value and leaves the shape. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Redaction replaces the matched value and leaves the shape.
- **B:** Correct. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. In this case: Redaction replaces the matched value and leaves the shape.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Redaction replaces the matched value and leaves the shape.
- **D:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: Redaction replaces the matched value and leaves the shape.

### Question 52 — B, C

Answers: Replace the value with a pseudonym from a crypto key; Apply format-preserving encryption to the card number field. A pseudonym keeps the join, and format-preserving encryption keeps the column type. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: A pseudonym keeps the join, and format-preserving encryption keeps the column type.
- **B:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: A pseudonym keeps the join, and format-preserving encryption keeps the column type.
- **C:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: A pseudonym keeps the join, and format-preserving encryption keeps the column type.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A pseudonym keeps the join, and format-preserving encryption keeps the column type.
- **E:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A pseudonym keeps the join, and format-preserving encryption keeps the column type.

### Question 53 — A

Answer: Replace the value with an unsalted hash. An unsalted hash of a low-entropy value is easy to reverse. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An unsalted hash of a low-entropy value can be reversed with a precomputed table. In this case: An unsalted hash of a low-entropy value is easy to reverse.
- **B:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.
- **C:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.
- **D:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.

### Question 54 — A

Answer: Grant authorised views or dataset-level IAM rather than table reads. Authorised views expose the aggregate and keep the table unreadable. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Authorised views expose the aggregate and keep the table unreadable.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Authorised views expose the aggregate and keep the table unreadable.
- **C:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Authorised views expose the aggregate and keep the table unreadable.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Authorised views expose the aggregate and keep the table unreadable.

### Question 55 — C

Answer: Grant the analyst the ability to export the whole table to a bucket. An export right hands over every row, including columns the analyst should not see. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: An export right hands over every row, including columns the analyst should not see.
- **B:** Incorrect for this question. IAM database authentication removes the stored database password and ties each connection to an identity. Why the correct answer wins: An export right hands over every row, including columns the analyst should not see.
- **C:** Correct. In this case: An export right hands over every row, including columns the analyst should not see.
- **D:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: An export right hands over every row, including columns the analyst should not see.

### Question 56 — A

Answer: Use Cloud SQL IAM database authentication for the application. IAM database authentication ties each connection to an identity. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: IAM database authentication ties each connection to an identity.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: IAM database authentication ties each connection to an identity.
- **C:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: IAM database authentication ties each connection to an identity.
- **D:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: IAM database authentication ties each connection to an identity.

### Question 57 — C

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager versions the value and rotates it without touching the deployment. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager versions the value and rotates it without touching the deployment.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager versions the value and rotates it without touching the deployment.
- **C:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager versions the value and rotates it without touching the deployment.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager versions the value and rotates it without touching the deployment.

### Question 58 — B, C

Answers: Store the credential in Secret Manager and grant the workload the secret accessor role; Create a dedicated service account per workload with only the roles it needs. Secret Manager keeps the value out of the log, and a dedicated account limits the reader. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. A per-workload service account bounds the blast radius and makes audit records attributable. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager keeps the value out of the log, and a dedicated account limits the reader.
- **B:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager keeps the value out of the log, and a dedicated account limits the reader.
- **C:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: Secret Manager keeps the value out of the log, and a dedicated account limits the reader.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager keeps the value out of the log, and a dedicated account limits the reader.
- **E:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager keeps the value out of the log, and a dedicated account limits the reader.

### Question 59 — A

Answer: Require the metadata server header on every request. Requiring the metadata header blocks the simplest forgery. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: Requiring the metadata header blocks the simplest forgery.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **D:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.

### Question 60 — B

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login ties each login to an identity and removes the shared key material. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key material.
- **B:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: OS Login ties each login to an identity and removes the shared key material.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key material.
- **D:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login ties each login to an identity and removes the shared key material.

### Question 61 — B

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key is held by the customer, not by Google. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key is held by the customer, not by Google.
- **B:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key is held by the customer, not by Google.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key is held by the customer, not by Google.
- **D:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key is held by the customer, not by Google.

### Question 62 — D

Answer: Rely on Google default encryption at rest. Default encryption protects the bytes with no customer key work. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **D:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: Default encryption protects the bytes with no customer key work.

### Question 63 — B

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM keeps the key material with an external party. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM keeps the key material with an external party.
- **B:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM keeps the key material with an external party.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM keeps the key material with an external party.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM keeps the key material with an external party.

### Question 64 — C

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM delegates the wrapping to the external key manager. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM delegates the wrapping to the external key manager.
- **B:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Cloud EKM delegates the wrapping to the external key manager.
- **C:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM delegates the wrapping to the external key manager.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM delegates the wrapping to the external key manager.

### Question 65 — B, D

Answers: Import the wrapping key into Cloud KMS; Set a rotation period on the key. Import brings the existing material under KMS, and rotation issues new versions on schedule. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Import brings the existing material under KMS, and rotation issues new versions on schedule.
- **B:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Import brings the existing material under KMS, and rotation issues new versions on schedule.
- **C:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Import brings the existing material under KMS, and rotation issues new versions on schedule.
- **D:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: Import brings the existing material under KMS, and rotation issues new versions on schedule.
- **E:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Import brings the existing material under KMS, and rotation issues new versions on schedule.

### Question 66 — A

Answer: Set a rotation period on the key. A rotation period issues new versions automatically. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: A rotation period issues new versions automatically.
- **B:** Incorrect for this question. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Why the correct answer wins: A rotation period issues new versions automatically.
- **C:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: A rotation period issues new versions automatically.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A rotation period issues new versions automatically.

### Question 67 — A

Answer: Disable the key version and re-wrap the data. Disabling the key version makes the bytes unreadable at once. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. In this case: Disabling the key version makes the bytes unreadable at once.
- **B:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Disabling the key version makes the bytes unreadable at once.
- **C:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Disabling the key version makes the bytes unreadable at once.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Disabling the key version makes the bytes unreadable at once.

### Question 68 — A

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted in use. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted in use.
- **B:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **C:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.

### Question 69 — D

Answer: Run the pod in a Confidential GKE node pool. A Confidential GKE node pool extends memory protection to the pods. Confidential GKE extends in-use memory protection to each pod on the node. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential GKE node pool extends memory protection to the pods.
- **B:** Incorrect for this question. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Why the correct answer wins: A Confidential GKE node pool extends memory protection to the pods.
- **C:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential GKE node pool extends memory protection to the pods.
- **D:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential GKE node pool extends memory protection to the pods.

### Question 70 — A, E

Answers: Attach an object lifecycle rule that keeps the required retention; Apply a retention policy with bucket lock. A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Bucket lock makes the retention period immutable, so not even an owner can delete early. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. In this case: A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable.
- **C:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable.
- **E:** Correct. Bucket lock makes the retention period immutable, so not even an owner can delete early. In this case: A lifecycle rule deletes on the schedule, and bucket lock makes the period immutable.

### Question 71 — D

Answer: Add an Artifact Analysis scan to the CI pipeline. Pipeline scanning blocks the image before it is deployed. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Pipeline scanning blocks the image before it is deployed.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: Pipeline scanning blocks the image before it is deployed.
- **C:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Pipeline scanning blocks the image before it is deployed.
- **D:** Correct. In this case: Pipeline scanning blocks the image before it is deployed.

### Question 72 — A, C

Answers: Add an Artifact Analysis scan to the CI pipeline; Scan the running image in production once a quarter. The build scan blocks the new image, and the production scan finds the older ones. Scanning in the pipeline stops the image before it is deployed, not after. A quarterly production scan finds the vulnerable image after it has already run. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Scanning in the pipeline stops the image before it is deployed, not after. In this case: The build scan blocks the new image, and the production scan finds the older ones.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: The build scan blocks the new image, and the production scan finds the older ones.
- **C:** Correct. A quarterly production scan finds the vulnerable image after it has already run. In this case: The build scan blocks the new image, and the production scan finds the older ones.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The build scan blocks the new image, and the production scan finds the older ones.
- **E:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: The build scan blocks the new image, and the production scan finds the older ones.

### Question 73 — C

Answer: Enforce a Binary Authorization policy that requires an attested image. Binary Authorization refuses an image without the required attestation. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.
- **B:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.
- **C:** Correct. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. In this case: Binary Authorization refuses an image without the required attestation.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Binary Authorization refuses an image without the required attestation.

### Question 74 — C

Answer: Deploy with Binary Authorization in dry-run mode only. Dry-run records the violation and still admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **B:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **C:** Correct. In this case: Dry-run records the violation and still admits the image.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Dry-run records the violation and still admits the image.

### Question 75 — C

Answer: Build the base image from a hardened source with a documented baseline. A hardened baseline removes what a general-purpose image carries. A hardened baseline removes the packages and accounts that a general-purpose image ships. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **B:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.
- **C:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline removes what a general-purpose image carries.
- **D:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline removes what a general-purpose image carries.

### Question 76 — A

Answer: Schedule patch jobs across the fleet with VM Manager. VM Manager applies and reports patches across the fleet. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: VM Manager applies and reports patches across the fleet.
- **B:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: VM Manager applies and reports patches across the fleet.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: VM Manager applies and reports patches across the fleet.
- **D:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: VM Manager applies and reports patches across the fleet.

### Question 77 — D

Answer: Compare the deployed configuration with the intended state on a schedule. A scheduled comparison finds the change that bypassed the pipeline. A scheduled comparison detects the change that happened outside the pipeline. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **B:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **D:** Correct. A scheduled comparison detects the change that happened outside the pipeline. In this case: A scheduled comparison finds the change that bypassed the pipeline.

### Question 78 — A, C

Answers: Deploy a Security Health Analytics custom module for the check; Write a custom organization policy constraint for the rule. A custom module produces the finding, and a custom constraint prevents the repeat. A custom module turns a local configuration rule into a recurring finding in Security Command Center. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A custom module turns a local configuration rule into a recurring finding in Security Command Center. In this case: A custom module produces the finding, and a custom constraint prevents the repeat.
- **B:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.
- **C:** Correct. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. In this case: A custom module produces the finding, and a custom constraint prevents the repeat.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.
- **E:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.

### Question 79 — C

Answer: Enable VPC Flow Logs on the subnets. Flow logs record the accepted and rejected five-tuples. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **C:** Correct. In this case: Flow logs record the accepted and rejected five-tuples.
- **D:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.

### Question 80 — C

Answer: Mirror the production traffic to a collector with Packet Mirroring. Packet Mirroring copies the packets for the collector. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Packet Mirroring copies the packets for the collector.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Packet Mirroring copies the packets for the collector.
- **C:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Packet Mirroring copies the packets for the collector.
- **D:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Packet Mirroring copies the packets for the collector.

### Question 81 — D

Answer: Deploy Cloud IDS on the network. Cloud IDS inspects the traffic and raises the finding. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **D:** Correct. In this case: Cloud IDS inspects the traffic and raises the finding.

### Question 82 — B

Answer: Route security logs to a dedicated project with its own retention. A dedicated log project keeps the evidence away from that owner. A dedicated log project keeps the evidence away from the principals who generate it. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A dedicated log project keeps the evidence away from that owner.
- **B:** Correct. A dedicated log project keeps the evidence away from the principals who generate it. In this case: A dedicated log project keeps the evidence away from that owner.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A dedicated log project keeps the evidence away from that owner.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A dedicated log project keeps the evidence away from that owner.

### Question 83 — A, E

Answers: Route security logs to a dedicated project with its own retention; Create an aggregated sink at the organisation level. A separate log project protects the evidence, and an aggregated sink collects every project. A dedicated log project keeps the evidence away from the principals who generate it. An aggregated sink includes the entries from every project beneath the node in one destination. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A dedicated log project keeps the evidence away from the principals who generate it. In this case: A separate log project protects the evidence, and an aggregated sink collects every project.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A separate log project protects the evidence, and an aggregated sink collects every project.
- **C:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A separate log project protects the evidence, and an aggregated sink collects every project.
- **D:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A separate log project protects the evidence, and an aggregated sink collects every project.
- **E:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: A separate log project protects the evidence, and an aggregated sink collects every project.

### Question 84 — A

Answer: Read the Admin Activity audit log for the change. Admin Activity records the configuration change and the identity. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Admin Activity records the configuration change and the identity.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the configuration change and the identity.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the configuration change and the identity.
- **D:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the configuration change and the identity.

### Question 85 — D

Answer: Enable Data Access audit logs for the service. Data Access logs record the read and are off until turned on. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Data Access logs record the read and are off until turned on.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Data Access logs record the read and are off until turned on.
- **C:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Data Access logs record the read and are off until turned on.
- **D:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Data Access logs record the read and are off until turned on.

### Question 86 — B

Answer: Create an aggregated sink at the organisation level. An aggregated sink covers every project beneath the node. An aggregated sink includes the entries from every project beneath the node in one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **B:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: An aggregated sink covers every project beneath the node.
- **C:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink covers every project beneath the node.

### Question 87 — D

Answer: Give the SIEM a service account key so it can pull the logs. A pulled key lives in a third party and cannot be narrowed to one destination. A pulled key sits in a third-party system and cannot be narrowed to one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **B:** Incorrect for this question. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **D:** Correct. A pulled key sits in a third-party system and cannot be narrowed to one destination. In this case: A pulled key lives in a third party and cannot be narrowed to one destination.

### Question 88 — B

Answer: Review the Security Command Center findings for the project. Security Command Center collects findings from the enabled detectors. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center collects findings from the enabled detectors.
- **B:** Correct. In this case: Security Command Center collects findings from the enabled detectors.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center collects findings from the enabled detectors.
- **D:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center collects findings from the enabled detectors.

### Question 89 — C

Answer: Close the finding as a false positive without a comment. A closure without a comment destroys the record that the finding was reviewed. An unexplained closure destroys the record that the finding was ever reviewed. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A named owner is what turns a control list into something that is actually operated. Why the correct answer wins: A closure without a comment destroys the record that the finding was reviewed.
- **B:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A closure without a comment destroys the record that the finding was reviewed.
- **C:** Correct. An unexplained closure destroys the record that the finding was ever reviewed. In this case: A closure without a comment destroys the record that the finding was reviewed.
- **D:** Incorrect for this question. A notification channel lets the response automation react to a finding as it is created. Why the correct answer wins: A closure without a comment destroys the record that the finding was reviewed.

### Question 90 — D

Answer: Document which controls Google operates and which the customer must implement. The shared responsibility split assigns the configuration layer to the customer. The shared responsibility split decides what the customer actually has to evidence. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The shared responsibility split assigns the configuration layer to the customer.
- **B:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The shared responsibility split assigns the configuration layer to the customer.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The shared responsibility split assigns the configuration layer to the customer.
- **D:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The shared responsibility split assigns the configuration layer to the customer.

### Question 91 — D

Answer: Assume Google secures every layer once the data is in the cloud. The provider secures the infrastructure, not the configuration written on top of it. The provider secures the infrastructure, not the configuration the customer writes on top of it. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top of it.
- **B:** Incorrect for this question. The shared responsibility split decides what the customer actually has to evidence. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top of it.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top of it.
- **D:** Correct. The provider secures the infrastructure, not the configuration the customer writes on top of it. In this case: The provider secures the infrastructure, not the configuration written on top of it.

### Question 92 — D

Answer: Create the folder as an Assured Workloads environment. Assured Workloads applies the personnel and location controls to the folder. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the personnel and location controls to the folder.
- **B:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: Assured Workloads applies the personnel and location controls to the folder.
- **C:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the personnel and location controls to the folder.
- **D:** Correct. In this case: Assured Workloads applies the personnel and location controls to the folder.

### Question 93 — C, E

Answers: Create the folder as an Assured Workloads environment; Name an owner for each control. Assured Workloads applies the controls, and a named owner makes them operated. Assured Workloads applies the personnel and location controls the regime requires to the folder. A named owner is what turns a control list into something that is actually operated. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: Assured Workloads applies the controls, and a named owner makes them operated.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: Assured Workloads applies the controls, and a named owner makes them operated.
- **C:** Correct. Assured Workloads applies the personnel and location controls the regime requires to the folder. In this case: Assured Workloads applies the controls, and a named owner makes them operated.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the controls, and a named owner makes them operated.
- **E:** Correct. A named owner is what turns a control list into something that is actually operated. In this case: Assured Workloads applies the controls, and a named owner makes them operated.

### Question 94 — D

Answer: Turn on Access Transparency and read its logs. Access Transparency records operator access to customer content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records operator access to customer content.
- **B:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records operator access to customer content.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records operator access to customer content.
- **D:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records operator access to customer content.

### Question 95 — C

Answer: Require Access Approval before an operator may read the content. Access Approval turns operator access into a request the customer grants. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.
- **C:** Correct. In this case: Access Approval turns operator access into a request the customer grants.
- **D:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval turns operator access into a request the customer grants.

### Question 96 — A

Answer: Constrain the resources to the required region with a location organization policy. A location constraint blocks resources outside the permitted region. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks resources outside the permitted region.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **C:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks resources outside the permitted region.

### Question 97 — B

Answer: Leave the default multi-region setting. A multi-region default places a copy outside the named region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **B:** Correct. In this case: A multi-region default places a copy outside the named region.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A multi-region default places a copy outside the named region.

### Question 98 — B

Answer: Map each requirement to the control that satisfies it and the evidence it produces. A mapping names the control and the evidence for the clause. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **B:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: A mapping names the control and the evidence for the clause.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **D:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: A mapping names the control and the evidence for the clause.

### Question 99 — B

Answer: Name an owner for each control. A named owner is what turns a control list into an operated control. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A named owner is what turns a control list into an operated control.
- **B:** Correct. In this case: A named owner is what turns a control list into an operated control.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A named owner is what turns a control list into an operated control.
- **D:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A named owner is what turns a control list into an operated control.

### Question 100 — C

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A written boundary decides which resources are in scope before testing. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A written boundary decides which resources are in scope before testing.
- **B:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A written boundary decides which resources are in scope before testing.
- **C:** Correct. In this case: A written boundary decides which resources are in scope before testing.
- **D:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A written boundary decides which resources are in scope before testing.
