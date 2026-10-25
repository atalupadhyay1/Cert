# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 6

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. A conglomerate with twelve brands wants one directory standing behind every cloud grant. What should hold the identities?

- A. Create a service account key and embed it in the application configuration
- B. Assign the super administrator role to a dedicated break-glass account with hardware keys
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Federate the workforce to Cloud Identity and enforce it as the identity source

### 2. Group membership must come from the bank's on-premises directory rather than being retyped. What should be scheduled?

- A. Assign the super administrator role to a dedicated break-glass account with hardware keys
- B. Create a service account key and embed it in the application configuration
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Restrict the project to the APIs it needs and review them on a schedule

### 3. The identity provider stays third party and Google Cloud must accept its assertion for console access. What should be configured?

- A. Configure single sign-on with a third-party identity provider over SAML
- B. Let each user decide whether to enrol in 2-step verification
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Create a service account key and embed it in the application configuration

### 4. An hour after termination the account must be suspended, and one account must still exist that can repair the tenant. Which two arrangements apply? Select two.

- A. Create a service account key and embed it in the application configuration
- B. Give every platform lead the super administrator role for convenience
- C. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- D. Assign the super administrator role to a dedicated break-glass account with hardware keys
- E. Have a team member update accounts by hand when the HR export arrives

### 5. The console is administered from an account that also owns the billing relationship. What is the problem?

- A. Assign the super administrator role to a dedicated break-glass account with hardware keys
- B. Give every platform lead the super administrator role for convenience
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Grant the predefined role that matches the task

### 6. A joint venture's own provider must be trusted without issuing Google identities to its staff. What should be configured?

- A. Create a Cloud Identity user per contractor and issue long-lived passwords
- B. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- C. Create a service account key and embed it in the application configuration
- D. Federate the partner workforce with Workforce Identity Federation

### 7. The joint venture issued three hundred local passwords instead of trusting its provider. What is the weakness?

- A. Configure Workload Identity Federation for the external workload
- B. Federate the partner workforce with Workforce Identity Federation
- C. Set the domain restricted sharing constraint on the organisation
- D. Create a Cloud Identity user per contractor and issue long-lived passwords

### 8. Six microservices share one account, so the log cannot say which service deleted the rows. What should be created?

- A. Run the workload as the default Compute Engine service account
- B. Grant the basic Editor role to the team
- C. Create a service account key and embed it in the application configuration
- D. Create a dedicated service account per workload with only the roles it needs

### 9. An account that only reads holds a role that also allows deletion. What should replace the grant?

- A. Build a custom role containing exactly the permissions the task uses
- B. Grant the predefined role that matches the task
- C. Grant the basic Editor role to the team
- D. Give every platform lead the super administrator role for convenience

### 10. The workload uses the account that already existed, because provisioning a new one took a ticket. What did it use?

- A. Create a service account key and embed it in the application configuration
- B. Create a dedicated service account per workload with only the roles it needs
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Run the workload as the default Compute Engine service account

### 11. Credentials were emailed to integrators and are still valid two years later. What was sent?

- A. Issue a short-lived access token through impersonation or metadata
- B. Configure Workload Identity Federation for the external workload
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Create a service account key and embed it in the application configuration

### 12. A credential minted for one build stops working at the end of it. What is it?

- A. Issue a short-lived access token through impersonation or metadata
- B. Create a service account key and embed it in the application configuration
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Set the credential as a plain environment variable in the deployment

### 13. Audit must name the person behind an action taken with a service account. What produces that record?

- A. Enforce 2-step verification for the whole organisation
- B. Grant the caller the Service Account Token Creator role on the target account
- C. Create a service account key and embed it in the application configuration
- D. Set the credential as a plain environment variable in the deployment

### 14. A data platform on another cloud needs Google credentials, and a compromised repository must not be able to obtain them. Which two settings apply? Select two.

- A. Configure Workload Identity Federation for the external workload
- B. Federate the partner workforce with Workforce Identity Federation
- C. Restrict the Workload Identity pool with an attribute condition on the subject
- D. Set the credential as a plain environment variable in the deployment
- E. Create a service account key and embed it in the application configuration

### 15. Any workload hosted by the provider can currently mint a token for the account. What should be added?

- A. Create a service account key and embed it in the application configuration
- B. Restrict the Workload Identity pool with an attribute condition on the subject
- C. Set the domain restricted sharing constraint on the organisation
- D. Configure Workload Identity Federation for the external workload

### 16. A database migration needs the account's rights for two hours and no file may change hands. What should be granted?

- A. Set the credential as a plain environment variable in the deployment
- B. Issue a short-lived access token through impersonation or metadata
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Create a service account key and embed it in the application configuration

### 17. The integrator asked for a key rather than a grant on the account. What is wrong with that?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Hand the caller a JSON key for the service account instead
- C. Configure Workload Identity Federation for the external workload
- D. Issue a short-lived access token through impersonation or metadata

### 18. Credential stuffing must be slowed, and a correct password alone must not complete a console login. Which two policies apply? Select two.

- A. Set a session length and reauthentication policy for the admin console
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Let each user decide whether to enrol in 2-step verification
- D. Enforce 2-step verification for the whole organisation
- E. Restrict the project to the APIs it needs and review them on a schedule

### 19. Users are allowed to skip enrolment in the second factor. What follows?

- A. Set a session length and reauthentication policy for the admin console
- B. Let each user decide whether to enrol in 2-step verification
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Enforce 2-step verification for the whole organisation

### 20. Owner is retained continuously because the team dislikes waiting for approval. What practice is that?

- A. Grant the role through Privileged Access Manager with an approval and a time limit
- B. Grant the predefined role that matches the task
- C. Grant the privileged role permanently and review it once a year
- D. Grant the role to a group and manage membership

### 21. A break-glass procedure must be approved by a second person and expire by itself. What should be used?

- A. Grant the role through Privileged Access Manager with an approval and a time limit
- B. Grant the role to a group and manage membership
- C. Grant the basic Editor role to the team
- D. Grant the privileged role permanently and review it once a year

### 22. Temporary access for an auditor must lapse automatically, and it must be refused from outside the office network. Which two controls apply? Select two.

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Grant the predefined role that matches the task
- C. Attach an IAM deny policy to the organisation
- D. Write an Access Context Manager access level and bind it to the perimeter
- E. Create a service perimeter with VPC Service Controls

### 23. A prohibition must beat every allow that anyone writes later. What should be attached?

- A. Enforce the constraint with an organization policy
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Add an IAM condition that limits the grant to a time window and a resource prefix
- D. Attach an IAM deny policy to the organisation

### 24. A holdco creates a folder for each acquisition and wants one policy per folder. What should be built?

- A. Have a team member update accounts by hand when the HR export arrives
- B. Ask each project owner to disable the setting
- C. Create a folder per environment and attach the policy at the folder
- D. Create a sink in each project and hope nobody adds a project

### 25. Public buckets must be impossible anywhere in the organisation. What should enforce that?

- A. Ask each project owner to disable the setting
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Enforce the constraint with an organization policy
- D. Create a folder per environment and attach the policy at the folder

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. The platform team owns the deny list, and application teams own their own allow list. Which two layers apply? Select two.

- A. Rely on the default VPC firewall rules in each project
- B. Deploy a hierarchical firewall policy at the organisation or folder level
- C. Create a service perimeter with VPC Service Controls
- D. Attach a Cloud Armor security policy to the backend service
- E. Allow all egress and rely on the application to be careful

### 27. Nothing was removed from the permissive rule, so egress is unrestricted. What is that rule?

- A. Deploy the instances with internal IP addresses only
- B. Create a service perimeter with VPC Service Controls
- C. Allow all egress and rely on the application to be careful
- D. Deploy a hierarchical firewall policy at the organisation or folder level

### 28. Only approved SaaS host names may be reached from the shared build network. What should be enabled?

- A. Filter on address and port only and allow the rest
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Deploy Cloud IDS on the network
- D. Route the egress through Secure Web Proxy

### 29. Address filtering was expected to distinguish two services that share a port. What explains the failure?

- A. Deploy Cloud IDS on the network
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Filter on address and port only and allow the rest
- D. Put Identity-Aware Proxy in front of the application

### 30. The edge must filter request patterns, and a scripted client must be challenged without blocking real buyers. Which two controls apply? Select two.

- A. Add a web application firewall rule in the application framework
- B. Attach a Cloud Armor security policy to the backend service
- C. Enable Cloud Armor bot management on the policy
- D. Put Identity-Aware Proxy in front of the application
- E. Terminate TLS at the load balancer with a managed certificate

### 31. Filtering happens in the application framework after the request has consumed backend capacity. What is the weakness?

- A. Put Identity-Aware Proxy in front of the application
- B. Add a web application firewall rule in the application framework
- C. Terminate TLS at the load balancer with a managed certificate
- D. Attach a Cloud Armor security policy to the backend service

### 32. Group membership must be checked for each request to the internal tool. What should sit in front?

- A. Put Identity-Aware Proxy in front of the application
- B. Deploy the instances with internal IP addresses only
- C. Attach a Cloud Armor security policy to the backend service
- D. Publish the application only through a VPN concentrator

### 33. A bypass path exists because the backend also answers on a public address. What closes it?

- A. Deploy the instances with internal IP addresses only
- B. Attach a Cloud Armor security policy to the backend service
- C. Enable layer 7 inspection on the firewall policy for the egress rule
- D. Put Identity-Aware Proxy in front of the application

### 34. Private certificates must come from one authority that can revoke them. What should be used?

- A. Terminate TLS at the load balancer with a managed certificate
- B. Generate a self-signed certificate on each instance
- C. Issue internal certificates from Certificate Authority Service
- D. Enable Private Google Access on the subnet

### 35. One managed certificate must cover every backend behind the proxy. What should terminate the connection?

- A. Pass encrypted traffic straight through to the instance
- B. Filter on address and port only and allow the rest
- C. Terminate TLS at the load balancer with a managed certificate
- D. Generate a self-signed certificate on each instance

### 36. Build agents must be limited to an approved list of web destinations, and the traffic must be read before it leaves. What should carry it?

- A. Route the egress through Secure Web Proxy
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Allow all egress and rely on the application to be careful
- D. Place Cloud NAT in front of the private instances

### 37. A named domain must resolve to nothing inside the network. What should be written?

- A. Enable Private Google Access on the subnet
- B. Use a Cloud DNS response policy to block the known-bad domain
- C. Route the egress through Secure Web Proxy
- D. Turn on DNSSEC for the public zone

### 38. A service must accept no connection from the internet, and its calls to Google APIs must avoid public addresses. Which two settings apply? Select two.

- A. Allow all egress and rely on the application to be careful
- B. Deploy the instances with internal IP addresses only
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Place Cloud NAT in front of the private instances
- E. Enable Private Google Access on the subnet

### 39. Two deprecated APIs remain enabled years after the migration. What should be reviewed?

- A. Enforce the constraint with an organization policy
- B. Create a service perimeter with VPC Service Controls
- C. Write an Access Context Manager access level and bind it to the perimeter
- D. Restrict the project to the APIs it needs and review them on a schedule

### 40. The network must be owned centrally while every team keeps its own project. What should be built?

- A. Peer the two VPC networks and scope the firewall rules to the peer
- B. Place Cloud NAT in front of the private instances
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Host the workload in a Shared VPC service project

### 41. One subnet holds all three tiers, so any tier can reach the database. What should be redesigned?

- A. Allow all egress and rely on the application to be careful
- B. Peer the two VPC networks and scope the firewall rules to the peer
- C. Give each tier its own subnet and allow only the flows between adjacent tiers
- D. Rely on the default VPC firewall rules in each project

### 42. Data must not cross the boundary even for an identity that holds a valid grant. What should be created?

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Make the bucket public but unlisted
- C. Rely on IAM to prevent data leaving the project
- D. Create a service perimeter with VPC Service Controls

### 43. The team assumed IAM was enough to stop data leaving the project. What was missed?

- A. Rely on IAM to prevent data leaving the project
- B. Attach an IAM deny policy to the organisation
- C. Create a service perimeter with VPC Service Controls
- D. Grant authorised views or dataset-level IAM rather than table reads

### 44. A dedicated circuit is required for bandwidth, and a tunnel pair must back it up. Which two services apply? Select two.

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Build a single classic VPN tunnel
- C. Build an HA VPN tunnel pair with two interfaces
- D. Place Cloud NAT in front of the private instances
- E. Provision a Dedicated Interconnect with two attachments

### 45. A branch has a single tunnel and no second path, so planned maintenance always disconnects it. What is described?

- A. Place Cloud NAT in front of the private instances
- B. Build a single classic VPN tunnel
- C. Provision a Dedicated Interconnect with two attachments
- D. Build an HA VPN tunnel pair with two interfaces

### 46. A partner's service must answer on a private address inside the consumer VPC. What should be created?

- A. Publish the service through a Private Service Connect endpoint
- B. Place Cloud NAT in front of the private instances
- C. Build a single classic VPN tunnel
- D. Enable Private Google Access on the subnet

### 47. Egress must be managed and logged with no host to patch. What should be deployed?

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Allow all egress and rely on the application to be careful
- C. Place Cloud NAT in front of the private instances
- D. Terminate TLS at the load balancer with a managed certificate

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. A merger brought forty datasets whose contents nobody has catalogued. What should be run?

- A. Ask the team to report which tables they believe hold personal data
- B. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- C. Make the bucket public but unlisted
- D. Replace the value with an unsalted hash

### 49. Two regions scan the same column and report different match counts. What should be shared?

- A. Save a Sensitive Data Protection inspect template and reuse it
- B. Reuse a stored de-identification template across pipelines
- C. Set the credential as a plain environment variable in the deployment
- D. Ask the team to report which tables they believe hold personal data

### 50. A questionnaire sent to each team is the only inventory of sensitive data. What is the weakness?

- A. Ask the team to report which tables they believe hold personal data
- B. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- C. Save a Sensitive Data Protection inspect template and reuse it
- D. Replace the value with an unsalted hash

### 51. A legacy card reader needs sixteen digits, and a cohort study needs a stable join key. Which two methods apply? Select two.

- A. Replace the value with a pseudonym from a crypto key
- B. Replace the value with an unsalted hash
- C. Apply format-preserving encryption to the card number field
- D. Generate the key in the application and store it beside the data
- E. Redact the matched values with a de-identification template

### 52. The column type and length must survive de-identification unchanged. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Replace the value with a pseudonym from a crypto key
- C. Replace the value with an unsalted hash
- D. Apply format-preserving encryption to the card number field

### 53. Downstream jobs must still match rows across two de-identified tables. What should be applied?

- A. Redact the matched values with a de-identification template
- B. Apply format-preserving encryption to the card number field
- C. Replace the value with an unsalted hash
- D. Replace the value with a pseudonym from a crypto key

### 54. The reporting tool needs aggregates and must never see a row identifier. What should be granted?

- A. Make the bucket public but unlisted
- B. Put the database password in the application config file
- C. Grant the analyst the ability to export the whole table to a bucket
- D. Grant authorised views or dataset-level IAM rather than table reads

### 55. Bucket contents are governed by hundreds of individual object grants that nobody reviews. What should be enabled?

- A. Make the bucket public but unlisted
- B. Allow all egress and rely on the application to be careful
- C. Grant the bucket role to a group with uniform bucket-level access
- D. Set an allUsers object ACL on the specific file

### 56. The application tier must reach the database with no stored password anywhere. What should be enabled?

- A. Put the database password in the application config file
- B. Generate the key in the application and store it beside the data
- C. Use Cloud SQL IAM database authentication for the application
- D. Set the credential as a plain environment variable in the deployment

### 57. A credential must keep its old versions so a rollback restores the previous value. What should hold it?

- A. Set the credential as a plain environment variable in the deployment
- B. Put the database password in the application config file
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Generate the key in the application and store it beside the data

### 58. A credential was found inside a published image layer. How did it get there?

- A. Set the credential as a plain environment variable in the deployment
- B. Generate the key in the application and store it beside the data
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Put the database password in the application config file

### 59. Cloud-init scripts must not be able to steal a token, and departing staff must lose shell access at once. Which two controls apply? Select two.

- A. Create a service account key and embed it in the application configuration
- B. Enable OS Login and turn off project-wide SSH keys
- C. Enforce a password policy with a minimum length and a reuse ban
- D. Deploy the instances with internal IP addresses only
- E. Require the metadata server header on every request

### 60. A shared project key keeps working for people who have left the company. What should be enabled?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Create a service account key and embed it in the application configuration
- C. Enable OS Login and turn off project-wide SSH keys
- D. Require the metadata server header on every request

### 61. The customer must be able to disable their own key and stop every read. What should be configured?

- A. Rely on Google default encryption at rest
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 62. Key material must never sit inside Google infrastructure. What should be used?

- A. Import the wrapping key into Cloud KMS
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Generate the key in the application and store it beside the data
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 63. No key policy exists and the data still must be protected at rest. What applies?

- A. Generate the key in the application and store it beside the data
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Rely on Google default encryption at rest
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 64. Material must come from the retiring platform, and it must then follow the new rotation schedule. Which two steps apply? Select two.

- A. Import the wrapping key into Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Rely on Google default encryption at rest
- D. Generate the key in the application and store it beside the data
- E. Set a rotation period on the key

### 65. Reads fail whenever the external key manager is unavailable. What design causes that?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Import the wrapping key into Cloud KMS
- D. Set a rotation period on the key

### 66. A new version must be created each quarter without anyone acting. What should be configured?

- A. Import the wrapping key into Cloud KMS
- B. Set a rotation period on the key
- C. Generate the key in the application and store it beside the data
- D. Disable the key version and re-wrap the data

### 67. One key version must stop decrypting within minutes of an incident. What should be done?

- A. Disable the key version and re-wrap the data
- B. Set a rotation period on the key
- C. Import the wrapping key into Cloud KMS
- D. Rely on Google default encryption at rest

### 68. A regulator asks for in-use protection on a lift-and-shift server and on a container platform. Which two choices apply? Select two.

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Rely on Google default encryption at rest
- C. Run the pod in a Confidential GKE node pool
- D. Run the workload on a Confidential VM
- E. Enable OS Login and turn off project-wide SSH keys

### 69. Guest RAM must be encrypted so the host cannot inspect it during processing. What should be used?

- A. Enable OS Login and turn off project-wide SSH keys
- B. Rely on Google default encryption at rest
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Run the workload on a Confidential VM

### 70. A retention floor must be impossible to reduce, even by an owner. What should be applied?

- A. Make the bucket public but unlisted
- B. Attach an object lifecycle rule that keeps the required retention
- C. Set an allUsers object ACL on the specific file
- D. Apply a retention policy with bucket lock

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A critical finding must fail the build rather than reach the registry. What should be added?

- A. Let each team patch its own instances when convenient
- B. Add an Artifact Analysis scan to the CI pipeline
- C. Enforce a Binary Authorization policy that requires an attested image
- D. Scan the running image in production once a quarter

### 72. Images that are already serving traffic must be re-checked as new findings appear. What provides that?

- A. Let each team patch its own instances when convenient
- B. Scan the running image in production once a quarter
- C. Add an Artifact Analysis scan to the CI pipeline
- D. Deploy with Binary Authorization in dry-run mode only

### 73. An image without a valid attestation must be refused at admission. What should be enforced?

- A. Deploy with Binary Authorization in dry-run mode only
- B. Attach a Cloud Armor security policy to the backend service
- C. Enforce a Binary Authorization policy that requires an attested image
- D. Deploy the instances with internal IP addresses only

### 74. Admission control must record violations for a week before it blocks anything. What should be used?

- A. Deploy with Binary Authorization in dry-run mode only
- B. Deploy Cloud IDS on the network
- C. Add an Artifact Analysis scan to the CI pipeline
- D. Enforce a Binary Authorization policy that requires an attested image

### 75. A supplier base image must carry nothing extra, and every instance must report its patch level. Which two practices apply? Select two.

- A. Compare the deployed configuration with the intended state on a schedule
- B. Schedule patch jobs across the fleet with VM Manager
- C. Build the base image from a hardened source with a documented baseline
- D. Scan the running image in production once a quarter
- E. Let each team patch its own instances when convenient

### 76. Patching happens per team with no consolidated record of host versions. What is described?

- A. Let each team patch its own instances when convenient
- B. Schedule patch jobs across the fleet with VM Manager
- C. Build the base image from a hardened source with a documented baseline
- D. Compare the deployed configuration with the intended state on a schedule

### 77. A posture check must report the drift, and the policy must prevent the change happening again. Which two mechanisms apply? Select two.

- A. Deploy a Security Health Analytics custom module for the check
- B. Write a custom organization policy constraint for the rule
- C. Compare the deployed configuration with the intended state on a schedule
- D. Have a team member update accounts by hand when the HR export arrives
- E. Lower the log volume by disabling data access logs

### 78. A setting was edited in the console and the next scheduled comparison was the first anyone knew. What should be added?

- A. Lower the log volume by disabling data access logs
- B. Deploy a Security Health Analytics custom module for the check
- C. Write a custom organization policy constraint for the rule
- D. Compare the deployed configuration with the intended state on a schedule

### 79. The network team must produce a list of blocked connections per subnet for last month. What should be enabled?

- A. Enable VPC Flow Logs on the subnets
- B. Lower the log volume by disabling data access logs
- C. Deploy Cloud IDS on the network
- D. Mirror the production traffic to a collector with Packet Mirroring

### 80. An inline appliance must flag traffic that matches a known attack signature. What should be deployed?

- A. Enable VPC Flow Logs on the subnets
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Attach a Cloud Armor security policy to the backend service
- D. Deploy Cloud IDS on the network

### 81. Investigators want a copy of the raw traffic rather than log lines. What should be used?

- A. Enable VPC Flow Logs on the subnets
- B. Query the logs through Log Analytics
- C. Mirror the production traffic to a collector with Packet Mirroring
- D. Deploy Cloud IDS on the network

### 82. The audit trail must be beyond the reach of the team that generates it. What should change?

- A. Lower the log volume by disabling data access logs
- B. Give the SIEM a service account key so it can pull the logs
- C. Create a sink in each project and hope nobody adds a project
- D. Route security logs to a dedicated project with its own retention

### 83. Turning off data access logs saved money and removed the record of who read the objects. What was disabled?

- A. Route security logs to a dedicated project with its own retention
- B. Apply a retention policy with bucket lock
- C. Enable Data Access audit logs for the service
- D. Lower the log volume by disabling data access logs

### 84. A forensic timeline needs both configuration changes and object reads. Which two log types apply? Select two.

- A. Give the SIEM a service account key so it can pull the logs
- B. Enable VPC Flow Logs on the subnets
- C. Create a log sink that routes the entries to the destination
- D. Enable Data Access audit logs for the service
- E. Read the Admin Activity audit log for the change

### 85. An investigator asks who deleted a service account. Which log answers?

- A. Enable VPC Flow Logs on the subnets
- B. Enable Data Access audit logs for the service
- C. Read the Admin Activity audit log for the change
- D. Create a log sink that routes the entries to the destination

### 86. Every project, including the ones created later, must deliver to one destination. What should be created?

- A. Give the SIEM a service account key so it can pull the logs
- B. Create a log sink that routes the entries to the destination
- C. Create an aggregated sink at the organisation level
- D. Create a sink in each project and hope nobody adds a project

### 87. The SIEM team wants a permanent key so it can pull logs by itself. What is the flaw?

- A. Lower the log volume by disabling data access logs
- B. Give the SIEM a service account key so it can pull the logs
- C. Set the credential as a plain environment variable in the deployment
- D. Export the entries to the external SIEM through Pub/Sub

### 88. Every detector and every project must surface in one console. What should be reviewed?

- A. Review the Security Command Center findings for the project
- B. Deploy a Security Health Analytics custom module for the check
- C. Query the logs through Log Analytics
- D. Compare the deployed configuration with the intended state on a schedule

### 89. A finding must open a ticket with no one watching the console. What should be configured?

- A. Give the SIEM a service account key so it can pull the logs
- B. Publish new findings to Pub/Sub for the response pipeline
- C. Close the finding as a false positive without a comment
- D. Lower the log volume by disabling data access logs

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. The question is who installs security updates on the guest operating system of an IaaS virtual machine. What answers it?

- A. Assume Google secures every layer once the data is in the cloud
- B. Document which controls Google operates and which the customer must implement
- C. Declare the whole organisation in scope for every regime
- D. State in the policy document that the environment is compliant

### 91. A reseller argues that using a hosted platform means the customer owns no security work at all. What is wrong?

- A. Assume Google secures every layer once the data is in the cloud
- B. Declare the whole organisation in scope for every regime
- C. Document which controls Google operates and which the customer must implement
- D. State in the policy document that the environment is compliant

### 92. Support staff for the environment must be located in the required jurisdiction. What should be created?

- A. Create the folder as an Assured Workloads environment
- B. Constrain the resources to the required region with a location organization policy
- C. Ask each project owner to disable the setting
- D. Record the regime in a spreadsheet and configure each control by hand

### 93. Each new project is configured for the regime through a checklist and manual console work. What fails first?

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Ask each project owner to disable the setting
- C. Create the folder as an Assured Workloads environment
- D. Keep the audit evidence for the period the regime requires

### 94. The customer requires disclosure whenever a Google employee touches their stored objects. What should be enabled?

- A. Enable Data Access audit logs for the service
- B. Turn on Access Transparency and read its logs
- C. Read the Admin Activity audit log for the change
- D. Require Access Approval before an operator may read the content

### 95. No operator may open the data before the customer agrees. What should be required?

- A. Write an Access Context Manager access level and bind it to the perimeter
- B. Create a service perimeter with VPC Service Controls
- C. Require Access Approval before an operator may read the content
- D. Turn on Access Transparency and read its logs

### 96. A location restriction must keep every dataset inside the named country. What should be enforced?

- A. Declare the whole organisation in scope for every regime
- B. Constrain the resources to the required region with a location organization policy
- C. Leave the default multi-region setting
- D. Record the regime in a spreadsheet and configure each control by hand

### 97. An object store was created without choosing a location, and copies now span several regions. What caused it?

- A. Leave the default multi-region setting
- B. Declare the whole organisation in scope for every regime
- C. Constrain the resources to the required region with a location organization policy
- D. Record the regime in a spreadsheet and configure each control by hand

### 98. A clause must name its control and its evidence, and every control must have someone answerable. Which two artefacts apply? Select two.

- A. Assume Google secures every layer once the data is in the cloud
- B. Declare the whole organisation in scope for every regime
- C. Map each requirement to the control that satisfies it and the evidence it produces
- D. State in the policy document that the environment is compliant
- E. Name an owner for each control

### 99. The evidence set expires after two years and the regime requires three. What was missing?

- A. Keep the audit evidence for the period the regime requires
- B. State in the policy document that the environment is compliant
- C. Lower the log volume by disabling data access logs
- D. Name an owner for each control

### 100. The engagement letter must define which projects the audit will examine. What should be written?

- A. Draw the compliance boundary around the projects and services that hold the regulated data
- B. Declare the whole organisation in scope for every regime
- C. State in the policy document that the environment is compliant
- D. Record the regime in a spreadsheet and configure each control by hand

---

## Answer key and explanations

### Question 1 — D

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory that every grant resolves against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Cloud Identity is the directory that every grant resolves against.
- **B:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Cloud Identity is the directory that every grant resolves against.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Cloud Identity is the directory that every grant resolves against.
- **D:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory that every grant resolves against.

### Question 2 — C

Answer: Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync. GCDS pulls the users and the groups from the existing directory. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: GCDS pulls the users and the groups from the existing directory.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: GCDS pulls the users and the groups from the existing directory.
- **C:** Correct. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. In this case: GCDS pulls the users and the groups from the existing directory.
- **D:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: GCDS pulls the users and the groups from the existing directory.

### Question 3 — A

Answer: Configure single sign-on with a third-party identity provider over SAML. SAML SSO accepts the third-party assertion. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. In this case: SAML SSO accepts the third-party assertion.
- **B:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: SAML SSO accepts the third-party assertion.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: SAML SSO accepts the third-party assertion.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: SAML SSO accepts the third-party assertion.

### Question 4 — C, D

Answers: Drive joiner, mover, and leaver flows through the Admin SDK Directory API; Assign the super administrator role to a dedicated break-glass account with hardware keys. The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant. Automating the lifecycle through the API removes the manual step where access is left behind. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant.
- **B:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant.
- **C:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant.
- **D:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant.
- **E:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The lifecycle automation suspends the account, and a break-glass super administrator repairs the tenant.

### Question 5 — B

Answer: Give every platform lead the super administrator role for convenience. Daily use of the super administrator role removes the separation that makes recovery accountable. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **B:** Correct. In this case: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **C:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.
- **D:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Daily use of the super administrator role removes the separation that makes recovery accountable.

### Question 6 — D

Answer: Federate the partner workforce with Workforce Identity Federation. Workforce Identity Federation accepts the joint venture provider. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Workforce Identity Federation accepts the joint venture provider.
- **B:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Workforce Identity Federation accepts the joint venture provider.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workforce Identity Federation accepts the joint venture provider.
- **D:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Workforce Identity Federation accepts the joint venture provider.

### Question 7 — D

Answer: Create a Cloud Identity user per contractor and issue long-lived passwords. A local account per person multiplies what must be reviewed and revoked. A local user per contractor multiplies the accounts that must be reviewed and revoked. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A local account per person multiplies what must be reviewed and revoked.
- **B:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: A local account per person multiplies what must be reviewed and revoked.
- **C:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: A local account per person multiplies what must be reviewed and revoked.
- **D:** Correct. A local user per contractor multiplies the accounts that must be reviewed and revoked. In this case: A local account per person multiplies what must be reviewed and revoked.

### Question 8 — D

Answer: Create a dedicated service account per workload with only the roles it needs. A dedicated account per workload separates the callers. A per-workload service account bounds the blast radius and makes audit records attributable. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A dedicated account per workload separates the callers.
- **B:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A dedicated account per workload separates the callers.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A dedicated account per workload separates the callers.
- **D:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A dedicated account per workload separates the callers.

### Question 9 — B

Answer: Grant the predefined role that matches the task. A predefined read role carries only the read permissions. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: A predefined read role carries only the read permissions.
- **B:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: A predefined read role carries only the read permissions.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A predefined read role carries only the read permissions.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A predefined read role carries only the read permissions.

### Question 10 — D

Answer: Run the workload as the default Compute Engine service account. The default service account is shared across every workload on the project. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The default service account is shared across every workload on the project.
- **B:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default service account is shared across every workload on the project.
- **C:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: The default service account is shared across every workload on the project.
- **D:** Correct. In this case: The default service account is shared across every workload on the project.

### Question 11 — D

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key carries no expiry unless one is set. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.
- **B:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.
- **C:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.
- **D:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key carries no expiry unless one is set.

### Question 12 — A

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token expires at the end of its window. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: A short-lived token expires at the end of its window.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token expires at the end of its window.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: A short-lived token expires at the end of its window.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token expires at the end of its window.

### Question 13 — B

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation records the person who acted as the account. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: Impersonation records the person who acted as the account.
- **B:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation records the person who acted as the account.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation records the person who acted as the account.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation records the person who acted as the account.

### Question 14 — A, C

Answers: Configure Workload Identity Federation for the external workload; Restrict the Workload Identity pool with an attribute condition on the subject. Federation removes the stored key, and an attribute condition limits which repository may act. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Federation removes the stored key, and an attribute condition limits which repository may act.
- **B:** Incorrect for this question. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Why the correct answer wins: Federation removes the stored key, and an attribute condition limits which repository may act.
- **C:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: Federation removes the stored key, and an attribute condition limits which repository may act.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Federation removes the stored key, and an attribute condition limits which repository may act.
- **E:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation removes the stored key, and an attribute condition limits which repository may act.

### Question 15 — B

Answer: Restrict the Workload Identity pool with an attribute condition on the subject. An attribute condition restricts which external identities may act. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **B:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: An attribute condition restricts which external identities may act.
- **C:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **D:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: An attribute condition restricts which external identities may act.

### Question 16 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation gives the acting right for the window. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation gives the acting right for the window.
- **B:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation gives the acting right for the window.
- **C:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation gives the acting right for the window.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation gives the acting right for the window.

### Question 17 — B

Answer: Hand the caller a JSON key for the service account instead. A handed-out key cannot be scoped and outlives the migration. A handed-out key cannot be scoped to one action and outlives the task that needed it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A handed-out key cannot be scoped and outlives the migration.
- **B:** Correct. A handed-out key cannot be scoped to one action and outlives the task that needed it. In this case: A handed-out key cannot be scoped and outlives the migration.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A handed-out key cannot be scoped and outlives the migration.
- **D:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A handed-out key cannot be scoped and outlives the migration.

### Question 18 — B, D

Answers: Enforce a password policy with a minimum length and a reuse ban; Enforce 2-step verification for the whole organisation. The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor. A password policy raises the cost of credential guessing without depending on the user to choose well. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor.
- **B:** Correct. A password policy raises the cost of credential guessing without depending on the user to choose well. In this case: The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor.
- **C:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor.
- **D:** Correct. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. In this case: The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor.
- **E:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: The password policy raises the guessing cost, and enforced 2-step verification blocks the single factor.

### Question 19 — B

Answer: Let each user decide whether to enrol in 2-step verification. Optional enrolment leaves the riskiest accounts single-factor. Optional enrolment leaves the accounts that most need the second factor without one. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: Optional enrolment leaves the riskiest accounts single-factor.
- **B:** Correct. Optional enrolment leaves the accounts that most need the second factor without one. In this case: Optional enrolment leaves the riskiest accounts single-factor.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Optional enrolment leaves the riskiest accounts single-factor.
- **D:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: Optional enrolment leaves the riskiest accounts single-factor.

### Question 20 — C

Answer: Grant the privileged role permanently and review it once a year. Standing privilege is live in every hour of the year. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Why the correct answer wins: Standing privilege is live in every hour of the year.
- **B:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Standing privilege is live in every hour of the year.
- **C:** Correct. Permanent privilege is live for every hour of the year, including the hours nobody is watching. In this case: Standing privilege is live in every hour of the year.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Standing privilege is live in every hour of the year.

### Question 21 — A

Answer: Grant the role through Privileged Access Manager with an approval and a time limit. Privileged Access Manager gates the grant and expires it. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Privileged Access Manager gates the grant and expires it.
- **B:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager gates the grant and expires it.
- **C:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Privileged Access Manager gates the grant and expires it.
- **D:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager gates the grant and expires it.

### Question 22 — A, D

Answers: Add an IAM condition that limits the grant to a time window and a resource prefix; Write an Access Context Manager access level and bind it to the perimeter. An IAM condition supplies the expiry, and an access level supplies the network requirement. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Access Context Manager describes the request context, such as network origin, that a policy can require. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An IAM condition supplies the expiry, and an access level supplies the network requirement.
- **B:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: An IAM condition supplies the expiry, and an access level supplies the network requirement.
- **C:** Incorrect for this question. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Why the correct answer wins: An IAM condition supplies the expiry, and an access level supplies the network requirement.
- **D:** Correct. Access Context Manager describes the request context, such as network origin, that a policy can require. In this case: An IAM condition supplies the expiry, and an access level supplies the network requirement.
- **E:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An IAM condition supplies the expiry, and an access level supplies the network requirement.

### Question 23 — D

Answer: Attach an IAM deny policy to the organisation. A deny policy is evaluated above every allow beneath it. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **C:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: A deny policy is evaluated above every allow beneath it.
- **D:** Correct. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. In this case: A deny policy is evaluated above every allow beneath it.

### Question 24 — C

Answer: Create a folder per environment and attach the policy at the folder. A folder carries one attachment for every project inside it. A folder boundary means one attachment covers every current and future project inside it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A folder carries one attachment for every project inside it.
- **B:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A folder carries one attachment for every project inside it.
- **C:** Correct. A folder boundary means one attachment covers every current and future project inside it. In this case: A folder carries one attachment for every project inside it.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A folder carries one attachment for every project inside it.

### Question 25 — C

Answer: Enforce the constraint with an organization policy. An organization policy binds every project beneath it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: An organization policy binds every project beneath it.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: An organization policy binds every project beneath it.
- **C:** Correct. In this case: An organization policy binds every project beneath it.
- **D:** Incorrect for this question. A folder boundary means one attachment covers every current and future project inside it. Why the correct answer wins: An organization policy binds every project beneath it.

### Question 26 — A, B

Answers: Deploy a hierarchical firewall policy at the organisation or folder level; Rely on the default VPC firewall rules in each project. The hierarchical policy carries the denies, and project rules carry the local allows. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Project-level rules are editable by the project owner and are evaluated after the hierarchy. In this case: The hierarchical policy carries the denies, and project rules carry the local allows.
- **B:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: The hierarchical policy carries the denies, and project rules carry the local allows.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The hierarchical policy carries the denies, and project rules carry the local allows.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: The hierarchical policy carries the denies, and project rules carry the local allows.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The hierarchical policy carries the denies, and project rules carry the local allows.

### Question 27 — C

Answer: Allow all egress and rely on the application to be careful. An allow-all rule reaches anything the internet offers. Unrestricted egress lets a compromised workload reach anything the internet offers. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: An allow-all rule reaches anything the internet offers.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An allow-all rule reaches anything the internet offers.
- **C:** Correct. Unrestricted egress lets a compromised workload reach anything the internet offers. In this case: An allow-all rule reaches anything the internet offers.
- **D:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: An allow-all rule reaches anything the internet offers.

### Question 28 — B

Answer: Enable layer 7 inspection on the firewall policy for the egress rule. Layer 7 inspection reads the destination host name. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the destination host name.
- **B:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the destination host name.
- **C:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Layer 7 inspection reads the destination host name.
- **D:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: Layer 7 inspection reads the destination host name.

### Question 29 — C

Answer: Filter on address and port only and allow the rest. A layer 4 rule filters on address and port only. A layer 4 rule cannot see the destination host name inside an allowed connection. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **C:** Correct. A layer 4 rule cannot see the destination host name inside an allowed connection. In this case: A layer 4 rule filters on address and port only.
- **D:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A layer 4 rule filters on address and port only.

### Question 30 — B, C

Answers: Attach a Cloud Armor security policy to the backend service; Enable Cloud Armor bot management on the policy. The security policy blocks the patterns, and bot management scores the script. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the script.
- **B:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: The security policy blocks the patterns, and bot management scores the script.
- **C:** Correct. Bot management scores automated traffic so a rule can separate a crawler from a credential-stuffing run. In this case: The security policy blocks the patterns, and bot management scores the script.
- **D:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the script.
- **E:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: The security policy blocks the patterns, and bot management scores the script.

### Question 31 — B

Answer: Add a web application firewall rule in the application framework. In-application filtering happens after the request has arrived. In-application filtering happens after the request has already consumed backend capacity. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: In-application filtering happens after the request has arrived.
- **B:** Correct. In-application filtering happens after the request has already consumed backend capacity. In this case: In-application filtering happens after the request has arrived.
- **C:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: In-application filtering happens after the request has arrived.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: In-application filtering happens after the request has arrived.

### Question 32 — A

Answer: Put Identity-Aware Proxy in front of the application. IAP authorises each request against IAM. IAP authenticates and authorises each request against IAM before it reaches the backend. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. IAP authenticates and authorises each request against IAM before it reaches the backend. In this case: IAP authorises each request against IAM.
- **B:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: IAP authorises each request against IAM.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP authorises each request against IAM.
- **D:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP authorises each request against IAM.

### Question 33 — A

Answer: Deploy the instances with internal IP addresses only. An internal-only address removes the path around the check. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal-only address removes the path around the check.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: An internal-only address removes the path around the check.
- **C:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: An internal-only address removes the path around the check.
- **D:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: An internal-only address removes the path around the check.

### Question 34 — C

Answer: Issue internal certificates from Certificate Authority Service. Certificate Authority Service issues and revokes them. Certificate Authority Service issues and revokes private certificates with an auditable authority. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Certificate Authority Service issues and revokes them.
- **B:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues and revokes them.
- **C:** Correct. Certificate Authority Service issues and revokes private certificates with an auditable authority. In this case: Certificate Authority Service issues and revokes them.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Certificate Authority Service issues and revokes them.

### Question 35 — C

Answer: Terminate TLS at the load balancer with a managed certificate. The load balancer serves the managed certificate. Terminating at the load balancer gives one managed certificate and a single policy point. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: The load balancer serves the managed certificate.
- **B:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: The load balancer serves the managed certificate.
- **C:** Correct. Terminating at the load balancer gives one managed certificate and a single policy point. In this case: The load balancer serves the managed certificate.
- **D:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: The load balancer serves the managed certificate.

### Question 36 — A

Answer: Route the egress through Secure Web Proxy. Secure Web Proxy applies the allowlist and reads the traffic. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: Secure Web Proxy applies the allowlist and reads the traffic.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Secure Web Proxy applies the allowlist and reads the traffic.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Secure Web Proxy applies the allowlist and reads the traffic.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Secure Web Proxy applies the allowlist and reads the traffic.

### Question 37 — B

Answer: Use a Cloud DNS response policy to block the known-bad domain. A response policy overrides the resolution for that domain. A response policy overrides resolution for named domains inside the network. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: A response policy overrides the resolution for that domain.
- **B:** Correct. A response policy overrides resolution for named domains inside the network. In this case: A response policy overrides the resolution for that domain.
- **C:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: A response policy overrides the resolution for that domain.
- **D:** Incorrect for this question. DNSSEC signs the answers so a resolver can detect a forged response. Why the correct answer wins: A response policy overrides the resolution for that domain.

### Question 38 — B, E

Answers: Deploy the instances with internal IP addresses only; Enable Private Google Access on the subnet. An internal address blocks inbound reach, and Private Google Access keeps the API path private. An internal-only address means the workload cannot be reached from the internet at all. Private Google Access lets an instance with only an internal address reach Google APIs. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps the API path private.
- **B:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal address blocks inbound reach, and Private Google Access keeps the API path private.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps the API path private.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An internal address blocks inbound reach, and Private Google Access keeps the API path private.
- **E:** Correct. Private Google Access lets an instance with only an internal address reach Google APIs. In this case: An internal address blocks inbound reach, and Private Google Access keeps the API path private.

### Question 39 — D

Answer: Restrict the project to the APIs it needs and review them on a schedule. The enabled API list should shrink to what is called. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: The enabled API list should shrink to what is called.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: The enabled API list should shrink to what is called.
- **C:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: The enabled API list should shrink to what is called.
- **D:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: The enabled API list should shrink to what is called.

### Question 40 — D

Answer: Host the workload in a Shared VPC service project. Shared VPC centralises the network in the host project. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **D:** Correct. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. In this case: Shared VPC centralises the network in the host project.

### Question 41 — C

Answer: Give each tier its own subnet and allow only the flows between adjacent tiers. Separate tier subnets express which tier may call which. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Separate tier subnets express which tier may call which.
- **B:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Separate tier subnets express which tier may call which.
- **C:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Separate tier subnets express which tier may call which.
- **D:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Separate tier subnets express which tier may call which.

### Question 42 — D

Answer: Create a service perimeter with VPC Service Controls. A service perimeter blocks the movement whatever the grant says. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.
- **B:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.
- **C:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.
- **D:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: A service perimeter blocks the movement whatever the grant says.

### Question 43 — A

Answer: Rely on IAM to prevent data leaving the project. An IAM grant still permits a copy out; only a perimeter stops it. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An IAM grant still permits a copy out; only a perimeter stops it.
- **B:** Incorrect for this question. A deny policy overrides any allow grant beneath it, which is how a hard prohibition is enforced. Why the correct answer wins: An IAM grant still permits a copy out; only a perimeter stops it.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An IAM grant still permits a copy out; only a perimeter stops it.
- **D:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: An IAM grant still permits a copy out; only a perimeter stops it.

### Question 44 — C, E

Answers: Provision a Dedicated Interconnect with two attachments; Build an HA VPN tunnel pair with two interfaces. Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path.
- **B:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path.
- **C:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path.
- **E:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: Dedicated Interconnect carries the circuit, and the HA VPN pair provides the backup path.

### Question 45 — B

Answer: Build a single classic VPN tunnel. A single tunnel carries no redundancy for a maintenance event. A single tunnel has no redundancy, so one maintenance window drops the path. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: A single tunnel carries no redundancy for a maintenance event.
- **B:** Correct. A single tunnel has no redundancy, so one maintenance window drops the path. In this case: A single tunnel carries no redundancy for a maintenance event.
- **C:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: A single tunnel carries no redundancy for a maintenance event.
- **D:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: A single tunnel carries no redundancy for a maintenance event.

### Question 46 — A

Answer: Publish the service through a Private Service Connect endpoint. A Private Service Connect endpoint gives that private address. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A Private Service Connect endpoint gives that private address.
- **B:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: A Private Service Connect endpoint gives that private address.
- **C:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: A Private Service Connect endpoint gives that private address.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: A Private Service Connect endpoint gives that private address.

### Question 47 — C

Answer: Place Cloud NAT in front of the private instances. Cloud NAT provides the managed outbound path. Cloud NAT gives the instances outbound connectivity while they keep no external address. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT provides the managed outbound path.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT provides the managed outbound path.
- **C:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT provides the managed outbound path.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT provides the managed outbound path.

### Question 48 — B

Answer: Run a Sensitive Data Protection discovery scan over the storage and warehouse. A discovery scan profiles where the sensitive data sits. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.
- **B:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: A discovery scan profiles where the sensitive data sits.
- **C:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A discovery scan profiles where the sensitive data sits.

### Question 49 — A

Answer: Save a Sensitive Data Protection inspect template and reuse it. A saved inspect template keeps the rules identical. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A saved inspect template keeps the rules identical.
- **B:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A saved inspect template keeps the rules identical.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A saved inspect template keeps the rules identical.
- **D:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A saved inspect template keeps the rules identical.

### Question 50 — A

Answer: Ask the team to report which tables they believe hold personal data. A self-reported inventory misses what nobody remembered. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A self-reported inventory misses what nobody remembered.
- **B:** Incorrect for this question. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **C:** Incorrect for this question. A saved template keeps the detection rules identical across scans, so results stay comparable. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A self-reported inventory misses what nobody remembered.

### Question 51 — A, C

Answers: Apply format-preserving encryption to the card number field; Replace the value with a pseudonym from a crypto key. Format-preserving encryption keeps the digits, and a pseudonym keeps the join. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: Format-preserving encryption keeps the digits, and a pseudonym keeps the join.
- **B:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Format-preserving encryption keeps the digits, and a pseudonym keeps the join.
- **C:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: Format-preserving encryption keeps the digits, and a pseudonym keeps the join.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Format-preserving encryption keeps the digits, and a pseudonym keeps the join.
- **E:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Format-preserving encryption keeps the digits, and a pseudonym keeps the join.

### Question 52 — D

Answer: Apply format-preserving encryption to the card number field. Format-preserving encryption keeps the type and the length. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **B:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Format-preserving encryption keeps the type and the length.
- **D:** Correct. Format-preserving encryption keeps the column type and length, so legacy code still reads it. In this case: Format-preserving encryption keeps the type and the length.

### Question 53 — D

Answer: Replace the value with a pseudonym from a crypto key. A pseudonym keeps a stable token across the tables. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: A pseudonym keeps a stable token across the tables.
- **B:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: A pseudonym keeps a stable token across the tables.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A pseudonym keeps a stable token across the tables.
- **D:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: A pseudonym keeps a stable token across the tables.

### Question 54 — D

Answer: Grant authorised views or dataset-level IAM rather than table reads. Authorised views expose the aggregate and hide the identifier. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.
- **C:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.
- **D:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Authorised views expose the aggregate and hide the identifier.

### Question 55 — C

Answer: Grant the bucket role to a group with uniform bucket-level access. Uniform bucket-level access makes IAM the only decision point. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **C:** Correct. In this case: Uniform bucket-level access makes IAM the only decision point.
- **D:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.

### Question 56 — C

Answer: Use Cloud SQL IAM database authentication for the application. IAM database authentication binds each connection to an identity. IAM database authentication removes the stored database password and ties each connection to an identity. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: IAM database authentication binds each connection to an identity.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: IAM database authentication binds each connection to an identity.
- **C:** Correct. IAM database authentication removes the stored database password and ties each connection to an identity. In this case: IAM database authentication binds each connection to an identity.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: IAM database authentication binds each connection to an identity.

### Question 57 — C

Answer: Store the credential in Secret Manager and grant the workload the secret accessor role. Secret Manager keeps each version and can pin one. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager keeps each version and can pin one.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager keeps each version and can pin one.
- **C:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager keeps each version and can pin one.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager keeps each version and can pin one.

### Question 58 — B

Answer: Generate the key in the application and store it beside the data. A value baked into the image travels with every copy. A key stored beside the data gives an attacker both halves of the protection. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A value baked into the image travels with every copy.
- **B:** Correct. A key stored beside the data gives an attacker both halves of the protection. In this case: A value baked into the image travels with every copy.
- **C:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: A value baked into the image travels with every copy.
- **D:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: A value baked into the image travels with every copy.

### Question 59 — B, E

Answers: Require the metadata server header on every request; Enable OS Login and turn off project-wide SSH keys. The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity.
- **B:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity.
- **C:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity.
- **D:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity.
- **E:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: The metadata header requirement blocks the theft, and OS Login ties shell access to a live identity.

### Question 60 — C

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login removes the shared key material. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login removes the shared key material.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login removes the shared key material.
- **C:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: OS Login removes the shared key material.
- **D:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login removes the shared key material.

### Question 61 — D

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key can be disabled by its owner. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **D:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key can be disabled by its owner.

### Question 62 — D

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM keeps the material with the external manager. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM keeps the material with the external manager.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM keeps the material with the external manager.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM keeps the material with the external manager.
- **D:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM keeps the material with the external manager.

### Question 63 — C

Answer: Rely on Google default encryption at rest. Default encryption protects the bytes with no customer key work. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **C:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: Default encryption protects the bytes with no customer key work.
- **D:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Default encryption protects the bytes with no customer key work.

### Question 64 — A, E

Answers: Import the wrapping key into Cloud KMS; Set a rotation period on the key. Key import brings the material over, and rotation issues the versions afterwards. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Key import brings the material over, and rotation issues the versions afterwards.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Key import brings the material over, and rotation issues the versions afterwards.
- **C:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Key import brings the material over, and rotation issues the versions afterwards.
- **D:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Key import brings the material over, and rotation issues the versions afterwards.
- **E:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: Key import brings the material over, and rotation issues the versions afterwards.

### Question 65 — B

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM puts the external manager on the read path. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM puts the external manager on the read path.
- **B:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM puts the external manager on the read path.
- **C:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM puts the external manager on the read path.
- **D:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Cloud EKM puts the external manager on the read path.

### Question 66 — B

Answer: Set a rotation period on the key. A rotation period issues the versions on schedule. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: A rotation period issues the versions on schedule.
- **B:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: A rotation period issues the versions on schedule.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A rotation period issues the versions on schedule.
- **D:** Incorrect for this question. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Why the correct answer wins: A rotation period issues the versions on schedule.

### Question 67 — A

Answer: Disable the key version and re-wrap the data. Disabling the version makes the bytes unreadable at once. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. In this case: Disabling the version makes the bytes unreadable at once.
- **B:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Disabling the version makes the bytes unreadable at once.
- **C:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Disabling the version makes the bytes unreadable at once.
- **D:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Disabling the version makes the bytes unreadable at once.

### Question 68 — C, D

Answers: Run the workload on a Confidential VM; Run the pod in a Confidential GKE node pool. A Confidential VM covers the server, and a Confidential GKE node pool covers the containers. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Confidential GKE extends in-use memory protection to each pod on the node. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM covers the server, and a Confidential GKE node pool covers the containers.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM covers the server, and a Confidential GKE node pool covers the containers.
- **C:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential VM covers the server, and a Confidential GKE node pool covers the containers.
- **D:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM covers the server, and a Confidential GKE node pool covers the containers.
- **E:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM covers the server, and a Confidential GKE node pool covers the containers.

### Question 69 — D

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted in use. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **D:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted in use.

### Question 70 — D

Answer: Apply a retention policy with bucket lock. Bucket lock makes the retention period immutable. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **B:** Incorrect for this question. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **C:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Bucket lock makes the retention period immutable.
- **D:** Correct. In this case: Bucket lock makes the retention period immutable.

### Question 71 — B

Answer: Add an Artifact Analysis scan to the CI pipeline. Pipeline scanning fails the build on the finding. Scanning in the pipeline stops the image before it is deployed, not after. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: Pipeline scanning fails the build on the finding.
- **B:** Correct. Scanning in the pipeline stops the image before it is deployed, not after. In this case: Pipeline scanning fails the build on the finding.
- **C:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Pipeline scanning fails the build on the finding.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Pipeline scanning fails the build on the finding.

### Question 72 — B

Answer: Scan the running image in production once a quarter. A production scan checks the images in use. A quarterly production scan finds the vulnerable image after it has already run. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A production scan checks the images in use.
- **B:** Correct. A quarterly production scan finds the vulnerable image after it has already run. In this case: A production scan checks the images in use.
- **C:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: A production scan checks the images in use.
- **D:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: A production scan checks the images in use.

### Question 73 — C

Answer: Enforce a Binary Authorization policy that requires an attested image. Binary Authorization refuses an image that lacks the attestation. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.
- **C:** Correct. In this case: Binary Authorization refuses an image that lacks the attestation.
- **D:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Binary Authorization refuses an image that lacks the attestation.

### Question 74 — A

Answer: Deploy with Binary Authorization in dry-run mode only. Dry-run records the violation and still admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Dry-run records the violation and still admits the image.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **C:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: Dry-run records the violation and still admits the image.
- **D:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Dry-run records the violation and still admits the image.

### Question 75 — B, C

Answers: Build the base image from a hardened source with a documented baseline; Schedule patch jobs across the fleet with VM Manager. A hardened baseline trims the image, and VM Manager reports the patch level. A hardened baseline removes the packages and accounts that a general-purpose image ships. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A hardened baseline trims the image, and VM Manager reports the patch level.
- **B:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: A hardened baseline trims the image, and VM Manager reports the patch level.
- **C:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline trims the image, and VM Manager reports the patch level.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline trims the image, and VM Manager reports the patch level.
- **E:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline trims the image, and VM Manager reports the patch level.

### Question 76 — A

Answer: Let each team patch its own instances when convenient. An unmanaged schedule leaves hosts at different levels with no fleet view. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **B:** Incorrect for this question. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **C:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: An unmanaged schedule leaves hosts at different levels with no fleet view.

### Question 77 — A, B

Answers: Deploy a Security Health Analytics custom module for the check; Write a custom organization policy constraint for the rule. A custom module produces the finding, and a custom constraint prevents the repeat. A custom module turns a local configuration rule into a recurring finding in Security Command Center. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A custom module turns a local configuration rule into a recurring finding in Security Command Center. In this case: A custom module produces the finding, and a custom constraint prevents the repeat.
- **B:** Correct. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. In this case: A custom module produces the finding, and a custom constraint prevents the repeat.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.
- **D:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.
- **E:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom module produces the finding, and a custom constraint prevents the repeat.

### Question 78 — D

Answer: Compare the deployed configuration with the intended state on a schedule. A scheduled comparison finds the change that bypassed the pipeline. A scheduled comparison detects the change that happened outside the pipeline. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **B:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **C:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **D:** Correct. A scheduled comparison detects the change that happened outside the pipeline. In this case: A scheduled comparison finds the change that bypassed the pipeline.

### Question 79 — A

Answer: Enable VPC Flow Logs on the subnets. Flow logs record the accepted and the rejected five-tuples. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Flow logs record the accepted and the rejected five-tuples.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the accepted and the rejected five-tuples.
- **C:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Flow logs record the accepted and the rejected five-tuples.
- **D:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the accepted and the rejected five-tuples.

### Question 80 — D

Answer: Deploy Cloud IDS on the network. Cloud IDS inspects the traffic and raises the finding. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **D:** Correct. In this case: Cloud IDS inspects the traffic and raises the finding.

### Question 81 — C

Answer: Mirror the production traffic to a collector with Packet Mirroring. Packet Mirroring copies the packets to a collector. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **B:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **C:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Packet Mirroring copies the packets to a collector.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Packet Mirroring copies the packets to a collector.

### Question 82 — D

Answer: Route security logs to a dedicated project with its own retention. A dedicated log project keeps the evidence away from that team. A dedicated log project keeps the evidence away from the principals who generate it. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.
- **B:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.
- **C:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A dedicated log project keeps the evidence away from that team.
- **D:** Correct. A dedicated log project keeps the evidence away from the principals who generate it. In this case: A dedicated log project keeps the evidence away from that team.

### Question 83 — D

Answer: Lower the log volume by disabling data access logs. Disabling the logs removes the record of the reads. Disabling data access logs removes the record that shows who read the data. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated log project keeps the evidence away from the principals who generate it. Why the correct answer wins: Disabling the logs removes the record of the reads.
- **B:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: Disabling the logs removes the record of the reads.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Disabling the logs removes the record of the reads.
- **D:** Correct. Disabling data access logs removes the record that shows who read the data. In this case: Disabling the logs removes the record of the reads.

### Question 84 — D, E

Answers: Read the Admin Activity audit log for the change; Enable Data Access audit logs for the service. Admin Activity records the change, and Data Access records the read. Admin Activity records the configuration change and the identity that made it, and is always on. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **C:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the change, and Data Access records the read.
- **D:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Admin Activity records the change, and Data Access records the read.
- **E:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Admin Activity records the change, and Data Access records the read.

### Question 85 — C

Answer: Read the Admin Activity audit log for the change. Admin Activity records the deletion and the identity. Admin Activity records the configuration change and the identity that made it, and is always on. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the deletion and the identity.
- **B:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the deletion and the identity.
- **C:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: Admin Activity records the deletion and the identity.
- **D:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the deletion and the identity.

### Question 86 — C

Answer: Create an aggregated sink at the organisation level. An aggregated sink covers every project beneath the node. An aggregated sink includes the entries from every project beneath the node in one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **C:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: An aggregated sink covers every project beneath the node.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink covers every project beneath the node.

### Question 87 — B

Answer: Give the SIEM a service account key so it can pull the logs. A pulled key lives in a third party and cannot be narrowed to one destination. A pulled key sits in a third-party system and cannot be narrowed to one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **B:** Correct. A pulled key sits in a third-party system and cannot be narrowed to one destination. In this case: A pulled key lives in a third party and cannot be narrowed to one destination.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.
- **D:** Incorrect for this question. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Why the correct answer wins: A pulled key lives in a third party and cannot be narrowed to one destination.

### Question 88 — A

Answer: Review the Security Command Center findings for the project. Security Command Center collects the findings for the tier. Security Command Center collects the findings from the detectors that are enabled for the tier. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Security Command Center collects the findings from the detectors that are enabled for the tier. In this case: Security Command Center collects the findings for the tier.
- **B:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center collects the findings for the tier.
- **C:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center collects the findings for the tier.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center collects the findings for the tier.

### Question 89 — B

Answer: Publish new findings to Pub/Sub for the response pipeline. A notification channel publishes the finding to the ticket tool. A notification channel lets the response automation react to a finding as it is created. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A notification channel publishes the finding to the ticket tool.
- **B:** Correct. A notification channel lets the response automation react to a finding as it is created. In this case: A notification channel publishes the finding to the ticket tool.
- **C:** Incorrect for this question. An unexplained closure destroys the record that the finding was ever reviewed. Why the correct answer wins: A notification channel publishes the finding to the ticket tool.
- **D:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A notification channel publishes the finding to the ticket tool.

### Question 90 — B

Answer: Document which controls Google operates and which the customer must implement. The shared responsibility split assigns the guest layer to the customer. The shared responsibility split decides what the customer actually has to evidence. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The shared responsibility split assigns the guest layer to the customer.
- **B:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The shared responsibility split assigns the guest layer to the customer.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The shared responsibility split assigns the guest layer to the customer.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The shared responsibility split assigns the guest layer to the customer.

### Question 91 — A

Answer: Assume Google secures every layer once the data is in the cloud. The provider secures the infrastructure, not the configuration written on top. The provider secures the infrastructure, not the configuration the customer writes on top of it. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The provider secures the infrastructure, not the configuration the customer writes on top of it. In this case: The provider secures the infrastructure, not the configuration written on top.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **C:** Incorrect for this question. The shared responsibility split decides what the customer actually has to evidence. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.

### Question 92 — A

Answer: Create the folder as an Assured Workloads environment. Assured Workloads applies the personnel controls to the folder. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Assured Workloads applies the personnel controls to the folder.
- **B:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **C:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the personnel controls to the folder.

### Question 93 — A

Answer: Record the regime in a spreadsheet and configure each control by hand. A manual mapping drifts when a project is created without the same settings. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A manual mapping drifts when a project is created without the same settings.
- **B:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **C:** Incorrect for this question. Assured Workloads applies the personnel and location controls the regime requires to the folder. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **D:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.

### Question 94 — B

Answer: Turn on Access Transparency and read its logs. Access Transparency records each operator access to content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records each operator access to content.
- **B:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records each operator access to content.
- **C:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records each operator access to content.
- **D:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records each operator access to content.

### Question 95 — C

Answer: Require Access Approval before an operator may read the content. Access Approval makes the operator wait for the decision. Access Approval turns the operator access into a request the customer must grant. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **B:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **C:** Correct. Access Approval turns the operator access into a request the customer must grant. In this case: Access Approval makes the operator wait for the decision.
- **D:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval makes the operator wait for the decision.

### Question 96 — B

Answer: Constrain the resources to the required region with a location organization policy. A location constraint blocks resources outside the permitted region. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **B:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks resources outside the permitted region.
- **C:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks resources outside the permitted region.

### Question 97 — A

Answer: Leave the default multi-region setting. A multi-region default places a copy outside the named region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A multi-region default places a copy outside the named region.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **C:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A multi-region default places a copy outside the named region.

### Question 98 — C, E

Answers: Map each requirement to the control that satisfies it and the evidence it produces; Name an owner for each control. The mapping ties the clause to the control and the evidence, and the named owner makes it operated. A mapping shows the auditor which control answers which clause and where the evidence lives. A named owner is what turns a control list into something that is actually operated. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The mapping ties the clause to the control and the evidence, and the named owner makes it operated.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The mapping ties the clause to the control and the evidence, and the named owner makes it operated.
- **C:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: The mapping ties the clause to the control and the evidence, and the named owner makes it operated.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The mapping ties the clause to the control and the evidence, and the named owner makes it operated.
- **E:** Correct. A named owner is what turns a control list into something that is actually operated. In this case: The mapping ties the clause to the control and the evidence, and the named owner makes it operated.

### Question 99 — A

Answer: Keep the audit evidence for the period the regime requires. A retention period for evidence is part of the control. A retention period for evidence is itself a control, because an expired record proves nothing. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A retention period for evidence is itself a control, because an expired record proves nothing. In this case: A retention period for evidence is part of the control.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A retention period for evidence is part of the control.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A retention period for evidence is part of the control.
- **D:** Incorrect for this question. A named owner is what turns a control list into something that is actually operated. Why the correct answer wins: A retention period for evidence is part of the control.

### Question 100 — A

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A boundary decides which resources are in scope before testing. A written boundary decides which resources are in scope and which are out, before the audit begins. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A written boundary decides which resources are in scope and which are out, before the audit begins. In this case: A boundary decides which resources are in scope before testing.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **C:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A boundary decides which resources are in scope before testing.
