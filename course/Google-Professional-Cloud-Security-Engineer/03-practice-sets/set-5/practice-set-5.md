# Google Cloud Professional Cloud Security Engineer — Full-Length Mock Exam 5

Professional Cloud Security Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Configuring Access (Identity, Service Accounts, and the Resource Hierarchy)

### 1. A university has forty thousand students and wants a single directory behind its cloud access. What should hold them?

- A. Assign the super administrator role to a dedicated break-glass account with hardware keys
- B. Federate the workforce to Cloud Identity and enforce it as the identity source
- C. Create a service account key and embed it in the application configuration
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 2. A steel maker will not move its directory off premises, yet cloud groups must follow it nightly. What should be scheduled?

- A. Create a service account key and embed it in the application configuration
- B. Restrict the project to the APIs it needs and review them on a schedule
- C. Assign the super administrator role to a dedicated break-glass account with hardware keys
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync

### 3. Airline staff must sign in with the identity provider the company already runs for every other system. What should be configured?

- A. Configure single sign-on with a third-party identity provider over SAML
- B. Let each user decide whether to enrol in 2-step verification
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Create a service account key and embed it in the application configuration

### 4. Students who graduated in June still hold project access in September. What should have removed it?

- A. Drive joiner, mover, and leaver flows through the Admin SDK Directory API
- B. Grant the role to a group and manage membership
- C. Have a team member update accounts by hand when the HR export arrives
- D. Assign the super administrator role to a dedicated break-glass account with hardware keys

### 5. An auditor asks how many identities can bypass single sign-on entirely. Which role answers that?

- A. Add an IAM condition that limits the grant to a time window and a resource prefix
- B. Assign the super administrator role to a dedicated break-glass account with hardware keys
- C. Grant the predefined role that matches the task
- D. Give every platform lead the super administrator role for convenience

### 6. A research partner's provider must be trusted for one study with no new Google accounts. What should be configured?

- A. Federate the partner workforce with Workforce Identity Federation
- B. Create a service account key and embed it in the application configuration
- C. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- D. Create a Cloud Identity user per contractor and issue long-lived passwords

### 7. A partner keeps its own directory, and its grants must never name an address outside the agreed company. Which two controls apply? Select two.

- A. Set the domain restricted sharing constraint on the organisation
- B. Create a Cloud Identity user per contractor and issue long-lived passwords
- C. Create a service account key and embed it in the application configuration
- D. Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync
- E. Federate the partner workforce with Workforce Identity Federation

### 8. A nightly export and the web front end run as the same account, so nothing in the log separates them. What should be created?

- A. Create a service account key and embed it in the application configuration
- B. Grant the basic Editor role to the team
- C. Create a dedicated service account per workload with only the roles it needs
- D. Run the workload as the default Compute Engine service account

### 9. A project created this morning already has a compute account holding Editor. Where did that come from?

- A. Grant the caller the Service Account Token Creator role on the target account
- B. Run the workload as the default Compute Engine service account
- C. Create a service account key and embed it in the application configuration
- D. Create a dedicated service account per workload with only the roles it needs

### 10. An account can rotate keys and delete buckets although it only writes objects. What should replace the grant?

- A. Grant the basic Editor role to the team
- B. Build a custom role containing exactly the permissions the task uses
- C. Give every platform lead the super administrator role for convenience
- D. Grant the predefined role that matches the task

### 11. The build must stop storing credentials, and any credential it does use must expire by itself. Which two controls apply? Select two.

- A. Set the credential as a plain environment variable in the deployment
- B. Enforce a password policy with a minimum length and a reuse ban
- C. Create a service account key and embed it in the application configuration
- D. Issue a short-lived access token through impersonation or metadata
- E. Grant the caller the Service Account Token Creator role on the target account

### 12. A credential with no expiry date was found in a pipeline variable. What kind of value is it?

- A. Issue a short-lived access token through impersonation or metadata
- B. Configure Workload Identity Federation for the external workload
- C. Create a service account key and embed it in the application configuration
- D. Grant the caller the Service Account Token Creator role on the target account

### 13. The blast radius of a leaked credential is limited to the next sixty minutes. What makes that true?

- A. Enforce 2-step verification for the whole organisation
- B. Create a service account key and embed it in the application configuration
- C. Issue a short-lived access token through impersonation or metadata
- D. Set the credential as a plain environment variable in the deployment

### 14. A continuous integration service outside Google must deploy with nothing stored in its settings. What should be configured?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Set the credential as a plain environment variable in the deployment
- C. Configure Workload Identity Federation for the external workload
- D. Create a service account key and embed it in the application configuration

### 15. Any repository of the provider may currently assume the deployer account. What should limit that?

- A. Restrict the Workload Identity pool with an attribute condition on the subject
- B. Create a service account key and embed it in the application configuration
- C. Configure Workload Identity Federation for the external workload
- D. Set the domain restricted sharing constraint on the organisation

### 16. A vendor engineer must use the deployer account for a week without receiving a file. What should be granted?

- A. Set the credential as a plain environment variable in the deployment
- B. Create a service account key and embed it in the application configuration
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Issue a short-lived access token through impersonation or metadata

### 17. The vendor asked for the account key so that it could act as the deployer. What is wrong with that?

- A. Issue a short-lived access token through impersonation or metadata
- B. Configure Workload Identity Federation for the external workload
- C. Grant the caller the Service Account Token Creator role on the target account
- D. Hand the caller a JSON key for the service account instead

### 18. One stolen password must not open the console by itself. What should be enforced?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Set a session length and reauthentication policy for the admin console
- C. Let each user decide whether to enrol in 2-step verification
- D. Enforce 2-step verification for the whole organisation

### 19. Users pick seasonal words and reuse them everywhere. What should be enforced?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Restrict the project to the APIs it needs and review them on a schedule
- C. Set a session length and reauthentication policy for the admin console
- D. Let each user decide whether to enrol in 2-step verification

### 20. Privilege must be temporary and approved, and the reviewer must see whether it was used. Which two controls apply? Select two.

- A. Grant the basic Editor role to the team
- B. Grant the role through Privileged Access Manager with an approval and a time limit
- C. Read the Policy Analyzer output before removing an unused grant
- D. Grant the role to a group and manage membership
- E. Grant the privileged role permanently and review it once a year

### 21. The operations team holds Owner continuously so nobody has to wait. What practice is that?

- A. Grant the role to a group and manage membership
- B. Grant the privileged role permanently and review it once a year
- C. Grant the predefined role that matches the task
- D. Grant the role through Privileged Access Manager with an approval and a time limit

### 22. A grant must lapse when the audit window closes. What should be added?

- A. Write an Access Context Manager access level and bind it to the perimeter
- B. Grant the predefined role that matches the task
- C. Enforce the constraint with an organization policy
- D. Add an IAM condition that limits the grant to a time window and a resource prefix

### 23. A valid grant must still be refused when the request comes from outside the corporate range. What should be written?

- A. Write an Access Context Manager access level and bind it to the perimeter
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Create a service perimeter with VPC Service Controls
- D. Enforce the constraint with an organization policy

### 24. One attachment must cover a whole department, and a project created later must inherit it unasked. Which two mechanisms apply? Select two.

- A. Have a team member update accounts by hand when the HR export arrives
- B. Create a folder per environment and attach the policy at the folder
- C. Enforce the constraint with an organization policy
- D. Create a sink in each project and hope nobody adds a project
- E. Ask each project owner to disable the setting

### 25. A constraint must stop public buckets everywhere in the organisation. What should enforce it?

- A. Enforce the constraint with an organization policy
- B. Add an IAM condition that limits the grant to a time window and a resource prefix
- C. Ask each project owner to disable the setting
- D. Create a folder per environment and attach the policy at the folder

---

## Domain 2 — Securing Communications and Establishing Boundary Protection (Firewalls, Perimeters, and Private Connectivity)

### 26. One deny must cover every project, including the ones that do not exist yet. What should be deployed?

- A. Deploy a hierarchical firewall policy at the organisation or folder level
- B. Allow all egress and rely on the application to be careful
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Rely on the default VPC firewall rules in each project

### 27. Traffic leaves the VPC freely because no one removed the permissive default. What is being described?

- A. Deploy the instances with internal IP addresses only
- B. Allow all egress and rely on the application to be careful
- C. Create a service perimeter with VPC Service Controls
- D. Deploy a hierarchical firewall policy at the organisation or folder level

### 28. A firewall must act on the TLS server name, and an inline sensor must alert on the payload. Which two services apply? Select two.

- A. Allow all egress and rely on the application to be careful
- B. Enable VPC Flow Logs on the subnets
- C. Filter on address and port only and allow the rest
- D. Deploy Cloud IDS on the network
- E. Enable layer 7 inspection on the firewall policy for the egress rule

### 29. The team expected host matching and got address matching. Why?

- A. Filter on address and port only and allow the rest
- B. Put Identity-Aware Proxy in front of the application
- C. Deploy Cloud IDS on the network
- D. Enable layer 7 inspection on the firewall policy for the egress rule

### 30. A login endpoint must be throttled per client address before the backend sees it. What should be configured?

- A. Attach a Cloud Armor security policy to the backend service
- B. Rely on the default VPC firewall rules in each project
- C. Add a web application firewall rule in the application framework
- D. Put Identity-Aware Proxy in front of the application

### 31. Scrapers must be scored so a rule can treat them differently from people. What should be enabled?

- A. Add a web application firewall rule in the application framework
- B. Terminate TLS at the load balancer with a managed certificate
- C. Enable Cloud Armor bot management on the policy
- D. Attach a Cloud Armor security policy to the backend service

### 32. An internal dashboard must check group membership on each request. What should sit in front?

- A. Publish the application only through a VPN concentrator
- B. Attach a Cloud Armor security policy to the backend service
- C. Put Identity-Aware Proxy in front of the application
- D. Deploy the instances with internal IP addresses only

### 33. Everyone who completes a VPN login can reach the dashboard today. What is the gap?

- A. Put Identity-Aware Proxy in front of the application
- B. Enable layer 7 inspection on the firewall policy for the egress rule
- C. Publish the application only through a VPN concentrator
- D. Attach a Cloud Armor security policy to the backend service

### 34. Internal certificates must come from one managed authority, and the handshake must end at the proxy tier. Which two choices apply? Select two.

- A. Generate a self-signed certificate on each instance
- B. Issue internal certificates from Certificate Authority Service
- C. Pass encrypted traffic straight through to the instance
- D. Terminate TLS at the load balancer with a managed certificate
- E. Filter on address and port only and allow the rest

### 35. The requirement is that the backend itself sees the client handshake. What should be configured?

- A. Generate a self-signed certificate on each instance
- B. Filter on address and port only and allow the rest
- C. Terminate TLS at the load balancer with a managed certificate
- D. Pass encrypted traffic straight through to the instance

### 36. Outbound browsing must follow an allowlist and be inspected on the way out. What should carry it?

- A. Run a NAT instance on a Compute Engine virtual machine
- B. Route the egress through Secure Web Proxy
- C. Place Cloud NAT in front of the private instances
- D. Allow all egress and rely on the application to be careful

### 37. A resolver must be able to tell that an answer was forged. What should be turned on?

- A. Enable Private Google Access on the subnet
- B. Route the egress through Secure Web Proxy
- C. Turn on DNSSEC for the public zone
- D. Use a Cloud DNS response policy to block the known-bad domain

### 38. A workload must accept no connection that originates on the internet. What should it have?

- A. Place Cloud NAT in front of the private instances
- B. Deploy the instances with internal IP addresses only
- C. Enable Private Google Access on the subnet
- D. Terminate TLS at the load balancer with a managed certificate

### 39. Six APIs are enabled that the service never calls. What should be reduced?

- A. Restrict the project to the APIs it needs and review them on a schedule
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Enforce the constraint with an organization policy
- D. Create a service perimeter with VPC Service Controls

### 40. Two network teams need private reachability, and each application tier must reach only its neighbour. Which two designs apply? Select two.

- A. Peer the two VPC networks and scope the firewall rules to the peer
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Host the workload in a Shared VPC service project
- D. Give each tier its own subnet and allow only the flows between adjacent tiers
- E. Allow all egress and rely on the application to be careful

### 41. Network control must stay central while each team keeps its own project. What should be built?

- A. Place Cloud NAT in front of the private instances
- B. Host the workload in a Shared VPC service project
- C. Peer the two VPC networks and scope the firewall rules to the peer
- D. Run a NAT instance on a Compute Engine virtual machine

### 42. Data must not leave the boundary even for an identity with a valid grant. What should be created?

- A. Rely on IAM to prevent data leaving the project
- B. Grant authorised views or dataset-level IAM rather than table reads
- C. Create a service perimeter with VPC Service Controls
- D. Make the bucket public but unlisted

### 43. The perimeter broke the API calls because they resolved to public virtual IPs. What should they use?

- A. Place Cloud NAT in front of the private instances
- B. Use restricted.googleapis.com for the API traffic
- C. Create a service perimeter with VPC Service Controls
- D. Enable Private Google Access on the subnet

### 44. The branch needs two tunnels so that one failure does not end the link. What should be built?

- A. Build an HA VPN tunnel pair with two interfaces
- B. Provision a Dedicated Interconnect with two attachments
- C. Build a single classic VPN tunnel
- D. Place Cloud NAT in front of the private instances

### 45. A private circuit at ten gigabits per second is required for replication. What should be provisioned?

- A. Build an HA VPN tunnel pair with two interfaces
- B. Run a NAT instance on a Compute Engine virtual machine
- C. Build a single classic VPN tunnel
- D. Provision a Dedicated Interconnect with two attachments

### 46. Hosts inside the data centre must reach Google APIs without internet egress. What should be configured?

- A. Publish the service through a Private Service Connect endpoint
- B. Configure Private Google Access for on-premises hosts over the hybrid route
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Place Cloud NAT in front of the private instances

### 47. Private instances need outbound access, and nothing may reach them from the internet. Which two settings apply? Select two.

- A. Place Cloud NAT in front of the private instances
- B. Terminate TLS at the load balancer with a managed certificate
- C. Run a NAT instance on a Compute Engine virtual machine
- D. Deploy the instances with internal IP addresses only
- E. Allow all egress and rely on the application to be careful

---

## Domain 3 — Ensuring Data Protection (Sensitive Data, Keys, and Confidential Computing)

### 48. A first pass must find where personal data lives, and every pipeline must apply the same fix. Which two choices apply? Select two.

- A. Replace the value with an unsalted hash
- B. Ask the team to report which tables they believe hold personal data
- C. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- D. Reuse a stored de-identification template across pipelines
- E. Generate the key in the application and store it beside the data

### 49. Two teams' scans of one column disagree about the number of matches. Why?

- A. Ask the team to report which tables they believe hold personal data
- B. Reuse a stored de-identification template across pipelines
- C. Set the credential as a plain environment variable in the deployment
- D. Save a Sensitive Data Protection inspect template and reuse it

### 50. A spreadsheet maintained by each team is the only record of sensitive tables. What is the weakness?

- A. Run a Sensitive Data Protection discovery scan over the storage and warehouse
- B. Ask the team to report which tables they believe hold personal data
- C. Replace the value with an unsalted hash
- D. Save a Sensitive Data Protection inspect template and reuse it

### 51. Support staff must not see the stored value at all. What should be applied?

- A. Apply format-preserving encryption to the card number field
- B. Replace the value with a pseudonym from a crypto key
- C. Redact the matched values with a de-identification template
- D. Replace the value with an unsalted hash

### 52. Two downstream jobs must still join on the same customer key. What should be applied?

- A. Apply format-preserving encryption to the card number field
- B. Redact the matched values with a de-identification template
- C. Replace the value with a pseudonym from a crypto key
- D. Replace the value with an unsalted hash

### 53. A hashed postcode column was reversed in minutes with a lookup table. What caused that?

- A. Replace the value with an unsalted hash
- B. Apply format-preserving encryption to the card number field
- C. Replace the value with a pseudonym from a crypto key
- D. Redact the matched values with a de-identification template

### 54. Analysts need aggregates only and must never see the row-level identifier. What should be granted?

- A. Grant authorised views or dataset-level IAM rather than table reads
- B. Grant the analyst the ability to export the whole table to a bucket
- C. Put the database password in the application config file
- D. Make the bucket public but unlisted

### 55. Per-object ACLs make it impossible to say who can read a bucket. What should be enabled?

- A. Make the bucket public but unlisted
- B. Grant the bucket role to a group with uniform bucket-level access
- C. Allow all egress and rely on the application to be careful
- D. Set an allUsers object ACL on the specific file

### 56. The application servers must connect to the database with no password stored anywhere. What should be enabled?

- A. Generate the key in the application and store it beside the data
- B. Put the database password in the application config file
- C. Use Cloud SQL IAM database authentication for the application
- D. Set the credential as a plain environment variable in the deployment

### 57. A secret must keep its previous versions, and every read must be recorded. Which two controls apply? Select two.

- A. Put the database password in the application config file
- B. Store the credential in Secret Manager and grant the workload the secret accessor role
- C. Set the credential as a plain environment variable in the deployment
- D. Enable Data Access audit logs for the service
- E. Generate the key in the application and store it beside the data

### 58. A password is readable in the process listing of the container. How was it supplied?

- A. Put the database password in the application config file
- B. Generate the key in the application and store it beside the data
- C. Store the credential in Secret Manager and grant the workload the secret accessor role
- D. Set the credential as a plain environment variable in the deployment

### 59. A forged request from the application can read the instance token. What should reject it?

- A. Enable OS Login and turn off project-wide SSH keys
- B. Require the metadata server header on every request
- C. Deploy the instances with internal IP addresses only
- D. Place Cloud NAT in front of the private instances

### 60. One project-wide key gives every holder the same login months after leaving. What should be enabled?

- A. Enforce a password policy with a minimum length and a reuse ban
- B. Require the metadata server header on every request
- C. Create a service account key and embed it in the application configuration
- D. Enable OS Login and turn off project-wide SSH keys

### 61. Nothing in the workload requires customer key management. What protects the data at rest?

- A. Generate the key in the application and store it beside the data
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Encrypt the dataset with a customer-managed key in Cloud KMS
- D. Rely on Google default encryption at rest

### 62. The customer must be able to revoke access to their own dataset by disabling a key. What should be configured?

- A. Generate the key in the application and store it beside the data
- B. Rely on Google default encryption at rest
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 63. The key material must stay inside the customer's own hardware security module. What should be used?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Hold the key in Cloud External Key Manager outside Google Cloud
- C. Generate the key in the application and store it beside the data
- D. Import the wrapping key into Cloud KMS

### 64. Every read stalls while a request travels to the customer's own key appliance. What design causes that?

- A. Encrypt the dataset with a customer-managed key in Cloud KMS
- B. Set a rotation period on the key
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Import the wrapping key into Cloud KMS

### 65. Wrapped objects predate the migration and must stay readable once inside KMS. What should be used?

- A. Import the wrapping key into Cloud KMS
- B. Set a rotation period on the key
- C. Generate the key in the application and store it beside the data
- D. Hold the key in Cloud External Key Manager outside Google Cloud

### 66. The crypto policy requires periodic re-wrapping, and an incident requires one version to stop at once. Which two controls apply? Select two.

- A. Import the wrapping key into Cloud KMS
- B. Generate the key in the application and store it beside the data
- C. Hold the key in Cloud External Key Manager outside Google Cloud
- D. Set a rotation period on the key
- E. Disable the key version and re-wrap the data

### 67. An incident demands that one key version stops decrypting today. What should be done?

- A. Rely on Google default encryption at rest
- B. Disable the key version and re-wrap the data
- C. Set a rotation period on the key
- D. Import the wrapping key into Cloud KMS

### 68. The hypervisor itself must not be able to read guest memory. What should be used?

- A. Enable OS Login and turn off project-wide SSH keys
- B. Rely on Google default encryption at rest
- C. Run the workload on a Confidential VM
- D. Encrypt the dataset with a customer-managed key in Cloud KMS

### 69. Pod memory must be protected from the node operator in a shared cluster. What should be used?

- A. Enable OS Login and turn off project-wide SSH keys
- B. Encrypt the dataset with a customer-managed key in Cloud KMS
- C. Run the pod in a Confidential GKE node pool
- D. Run the workload on a Confidential VM

### 70. Retention requires automatic deletion, and the floor must not be overridable by an owner. Which two controls apply? Select two.

- A. Allow all egress and rely on the application to be careful
- B. Apply a retention policy with bucket lock
- C. Set an allUsers object ACL on the specific file
- D. Make the bucket public but unlisted
- E. Attach an object lifecycle rule that keeps the required retention

---

## Domain 4 — Managing Operations (Automation, Detection, and Logging)

### 71. A vulnerable image must fail the build rather than reach the registry. What should be added?

- A. Enforce a Binary Authorization policy that requires an attested image
- B. Let each team patch its own instances when convenient
- C. Scan the running image in production once a quarter
- D. Add an Artifact Analysis scan to the CI pipeline

### 72. Images already running in production must be re-checked for new vulnerabilities. What provides that?

- A. Let each team patch its own instances when convenient
- B. Deploy with Binary Authorization in dry-run mode only
- C. Add an Artifact Analysis scan to the CI pipeline
- D. Scan the running image in production once a quarter

### 73. Admission must refuse unattested images once a trial shows no false blocks. Which two stages apply? Select two.

- A. Deploy with Binary Authorization in dry-run mode only
- B. Enforce a Binary Authorization policy that requires an attested image
- C. Attach a Cloud Armor security policy to the backend service
- D. Scan the running image in production once a quarter
- E. Deploy the instances with internal IP addresses only

### 74. The admission policy has only ever recorded violations and never stopped one. What state is it in?

- A. Deploy Cloud IDS on the network
- B. Add an Artifact Analysis scan to the CI pipeline
- C. Enforce a Binary Authorization policy that requires an attested image
- D. Deploy with Binary Authorization in dry-run mode only

### 75. The base image must carry nothing beyond what the service needs. What should be built?

- A. Build the base image from a hardened source with a documented baseline
- B. Let each team patch its own instances when convenient
- C. Schedule patch jobs across the fleet with VM Manager
- D. Scan the running image in production once a quarter

### 76. The fleet must be patched and reported on one schedule. What should be introduced?

- A. Build the base image from a hardened source with a documented baseline
- B. Schedule patch jobs across the fleet with VM Manager
- C. Let each team patch its own instances when convenient
- D. Compare the deployed configuration with the intended state on a schedule

### 77. A local misconfiguration must appear as a finding without a bespoke pipeline. What should be built?

- A. Deploy a Security Health Analytics custom module for the check
- B. Lower the log volume by disabling data access logs
- C. Compare the deployed configuration with the intended state on a schedule
- D. Write a custom organization policy constraint for the rule

### 78. A console change altered a setting and nobody noticed for a month. What should be added?

- A. Lower the log volume by disabling data access logs
- B. Deploy a Security Health Analytics custom module for the check
- C. Compare the deployed configuration with the intended state on a schedule
- D. Write a custom organization policy constraint for the rule

### 79. Security needs the denied flows per subnet for last quarter. What should be enabled?

- A. Enable VPC Flow Logs on the subnets
- B. Deploy Cloud IDS on the network
- C. Lower the log volume by disabling data access logs
- D. Mirror the production traffic to a collector with Packet Mirroring

### 80. An inline sensor must raise a finding on a known exploit pattern. What should be deployed?

- A. Attach a Cloud Armor security policy to the backend service
- B. Enable VPC Flow Logs on the subnets
- C. Enable layer 7 inspection on the firewall policy for the egress rule
- D. Deploy Cloud IDS on the network

### 81. The forensic team needs the packets themselves. What should be used?

- A. Enable VPC Flow Logs on the subnets
- B. Query the logs through Log Analytics
- C. Mirror the production traffic to a collector with Packet Mirroring
- D. Deploy Cloud IDS on the network

### 82. The audit trail must sit beyond the reach of the project team, and it must last for the audit period. Which two controls apply? Select two.

- A. Give the SIEM a service account key so it can pull the logs
- B. Lower the log volume by disabling data access logs
- C. Create a sink in each project and hope nobody adds a project
- D. Keep the audit evidence for the period the regime requires
- E. Route security logs to a dedicated project with its own retention

### 83. Data access logs were switched off during a cost review. What is gone?

- A. Apply a retention policy with bucket lock
- B. Lower the log volume by disabling data access logs
- C. Enable Data Access audit logs for the service
- D. Route security logs to a dedicated project with its own retention

### 84. An investigator asks who edited an IAM binding on Tuesday. Which log answers?

- A. Read the Admin Activity audit log for the change
- B. Enable VPC Flow Logs on the subnets
- C. Enable Data Access audit logs for the service
- D. Create a log sink that routes the entries to the destination

### 85. An investigator asks whether a named analyst downloaded a particular file. Which log answers?

- A. Read the Admin Activity audit log for the change
- B. Create a log sink that routes the entries to the destination
- C. Enable VPC Flow Logs on the subnets
- D. Enable Data Access audit logs for the service

### 86. Every project, including the ones created next year, must deliver to the SIEM. What should be created?

- A. Give the SIEM a service account key so it can pull the logs
- B. Create a sink in each project and hope nobody adds a project
- C. Create a log sink that routes the entries to the destination
- D. Create an aggregated sink at the organisation level

### 87. Security monitoring runs outside Google Cloud and must consume entries without an inbound route. What should be used?

- A. Set the credential as a plain environment variable in the deployment
- B. Export the entries to the external SIEM through Pub/Sub
- C. Lower the log volume by disabling data access logs
- D. Give the SIEM a service account key so it can pull the logs

### 88. A finding must open a ticket, and the closure must be attributable to a person. Which two controls apply? Select two.

- A. Close the finding as a false positive without a comment
- B. Read the Admin Activity audit log for the change
- C. Lower the log volume by disabling data access logs
- D. Publish new findings to Pub/Sub for the response pipeline
- E. Give the SIEM a service account key so it can pull the logs

### 89. One screen must show every detector finding from every project. What should be reviewed?

- A. Review the Security Command Center findings for the project
- B. Compare the deployed configuration with the intended state on a schedule
- C. Deploy a Security Health Analytics custom module for the check
- D. Query the logs through Log Analytics

---

## Domain 5 — Supporting Compliance Requirements (Compliance Controls and the Shared Responsibility Model)

### 90. A customer asks who configures the firewall rules on their own network. What answers it?

- A. Declare the whole organisation in scope for every regime
- B. Document which controls Google operates and which the customer must implement
- C. Assume Google secures every layer once the data is in the cloud
- D. State in the policy document that the environment is compliant

### 91. A provider claims that hosting removes every security duty from the customer. What is wrong?

- A. Assume Google secures every layer once the data is in the cloud
- B. State in the policy document that the environment is compliant
- C. Document which controls Google operates and which the customer must implement
- D. Declare the whole organisation in scope for every regime

### 92. Personnel controls must apply to the folder, and the resources must stay in one location. Which two controls apply? Select two.

- A. Ask each project owner to disable the setting
- B. Declare the whole organisation in scope for every regime
- C. Constrain the resources to the required region with a location organization policy
- D. Record the regime in a spreadsheet and configure each control by hand
- E. Create the folder as an Assured Workloads environment

### 93. Regime settings are rebuilt by hand in each project as it appears. What fails first?

- A. Create the folder as an Assured Workloads environment
- B. Keep the audit evidence for the period the regime requires
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Ask each project owner to disable the setting

### 94. The customer needs a record of each Google staff access to their content. What should be enabled?

- A. Enable Data Access audit logs for the service
- B. Read the Admin Activity audit log for the change
- C. Turn on Access Transparency and read its logs
- D. Require Access Approval before an operator may read the content

### 95. No operator may open the data until the customer says yes. What should be required?

- A. Create a service perimeter with VPC Service Controls
- B. Write an Access Context Manager access level and bind it to the perimeter
- C. Turn on Access Transparency and read its logs
- D. Require Access Approval before an operator may read the content

### 96. Every resource must be created in one named country. What should be enforced?

- A. Record the regime in a spreadsheet and configure each control by hand
- B. Leave the default multi-region setting
- C. Declare the whole organisation in scope for every regime
- D. Constrain the resources to the required region with a location organization policy

### 97. Storage landed in a multi-region location and the contract names one country. What caused it?

- A. Constrain the resources to the required region with a location organization policy
- B. Leave the default multi-region setting
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Declare the whole organisation in scope for every regime

### 98. Each clause must name the control that answers it and the evidence it produces. What should be produced?

- A. Assume Google secures every layer once the data is in the cloud
- B. Declare the whole organisation in scope for every regime
- C. Map each requirement to the control that satisfies it and the evidence it produces
- D. State in the policy document that the environment is compliant

### 99. Evidence disappears after two years while the audit cycle runs three. What was missing?

- A. State in the policy document that the environment is compliant
- B. Keep the audit evidence for the period the regime requires
- C. Lower the log volume by disabling data access logs
- D. Name an owner for each control

### 100. The auditor needs the project list in scope before the first test. What should be written?

- A. Declare the whole organisation in scope for every regime
- B. State in the policy document that the environment is compliant
- C. Record the regime in a spreadsheet and configure each control by hand
- D. Draw the compliance boundary around the projects and services that hold the regulated data

---

## Answer key and explanations

### Question 1 — B

Answer: Federate the workforce to Cloud Identity and enforce it as the identity source. Cloud Identity is the directory every grant resolves against. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: Cloud Identity is the directory every grant resolves against.
- **B:** Correct. Cloud Identity becomes the single directory that Google Cloud authorises, so leavers lose access everywhere at once. In this case: Cloud Identity is the directory every grant resolves against.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Cloud Identity is the directory every grant resolves against.
- **D:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Cloud Identity is the directory every grant resolves against.

### Question 2 — D

Answer: Sync the on-premises directory to Cloud Identity with Google Cloud Directory Sync. GCDS pushes the users and groups from the existing directory. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: GCDS pushes the users and groups from the existing directory.
- **B:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: GCDS pushes the users and groups from the existing directory.
- **C:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: GCDS pushes the users and groups from the existing directory.
- **D:** Correct. In this case: GCDS pushes the users and groups from the existing directory.

### Question 3 — A

Answer: Configure single sign-on with a third-party identity provider over SAML. SAML SSO keeps authentication with that provider. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. Local study-map skill 1.1 (Cloud Identity, SSO, and Directory Sync), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. SAML SSO lets the existing identity provider authenticate the user while Cloud Identity authorises the session. In this case: SAML SSO keeps authentication with that provider.
- **B:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: SAML SSO keeps authentication with that provider.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: SAML SSO keeps authentication with that provider.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: SAML SSO keeps authentication with that provider.

### Question 4 — A

Answer: Drive joiner, mover, and leaver flows through the Admin SDK Directory API. The Admin SDK lifecycle automation suspends the account when the record changes. Automating the lifecycle through the API removes the manual step where access is left behind. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Automating the lifecycle through the API removes the manual step where access is left behind. In this case: The Admin SDK lifecycle automation suspends the account when the record changes.
- **B:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the record changes.
- **C:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the record changes.
- **D:** Incorrect for this question. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Why the correct answer wins: The Admin SDK lifecycle automation suspends the account when the record changes.

### Question 5 — B

Answer: Assign the super administrator role to a dedicated break-glass account with hardware keys. The super administrator role can sign in without the federated path. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. Local study-map skill 1.2 (Super Administrator and Lifecycle Automation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: The super administrator role can sign in without the federated path.
- **B:** Correct. A dedicated break-glass super administrator is used only for directory-level recovery and is never a daily account. In this case: The super administrator role can sign in without the federated path.
- **C:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: The super administrator role can sign in without the federated path.
- **D:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: The super administrator role can sign in without the federated path.

### Question 6 — A

Answer: Federate the partner workforce with Workforce Identity Federation. Workforce Identity Federation accepts the partner provider directly. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Workforce Identity Federation accepts the partner provider directly.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workforce Identity Federation accepts the partner provider directly.
- **C:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Workforce Identity Federation accepts the partner provider directly.
- **D:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Workforce Identity Federation accepts the partner provider directly.

### Question 7 — A, E

Answers: Federate the partner workforce with Workforce Identity Federation; Set the domain restricted sharing constraint on the organisation. Federation accepts the partner directory, and domain restricted sharing bounds the grants. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Local study-map skill 1.3 (Workforce Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. In this case: Federation accepts the partner directory, and domain restricted sharing bounds the grants.
- **B:** Incorrect for this question. A local user per contractor multiplies the accounts that must be reviewed and revoked. Why the correct answer wins: Federation accepts the partner directory, and domain restricted sharing bounds the grants.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Federation accepts the partner directory, and domain restricted sharing bounds the grants.
- **D:** Incorrect for this question. GCDS pushes users and groups from the existing directory on a schedule, so one directory remains authoritative. Why the correct answer wins: Federation accepts the partner directory, and domain restricted sharing bounds the grants.
- **E:** Correct. Workforce Identity Federation lets an external identity provider grant Google Cloud access without creating Cloud Identity users. In this case: Federation accepts the partner directory, and domain restricted sharing bounds the grants.

### Question 8 — C

Answer: Create a dedicated service account per workload with only the roles it needs. A dedicated account per workload separates the two callers. A per-workload service account bounds the blast radius and makes audit records attributable. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A dedicated account per workload separates the two callers.
- **B:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A dedicated account per workload separates the two callers.
- **C:** Correct. A per-workload service account bounds the blast radius and makes audit records attributable. In this case: A dedicated account per workload separates the two callers.
- **D:** Incorrect for this question. The default service account is shared by every workload on the project, so its grants reach all of them. Why the correct answer wins: A dedicated account per workload separates the two callers.

### Question 9 — B

Answer: Run the workload as the default Compute Engine service account. The default service account is created with broad access on every project. The default service account is shared by every workload on the project, so its grants reach all of them. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: The default service account is created with broad access on every project.
- **B:** Correct. The default service account is shared by every workload on the project, so its grants reach all of them. In this case: The default service account is created with broad access on every project.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: The default service account is created with broad access on every project.
- **D:** Incorrect for this question. A per-workload service account bounds the blast radius and makes audit records attributable. Why the correct answer wins: The default service account is created with broad access on every project.

### Question 10 — D

Answer: Grant the predefined role that matches the task. A predefined role that matches the write task carries nothing else. A predefined role carries the permissions the task needs and nothing broader. Local study-map skill 1.4 (Service Account Hygiene and Default Accounts), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: A predefined role that matches the write task carries nothing else.
- **B:** Incorrect for this question. A custom role is justified when no predefined role is narrow enough, at the cost of maintenance. Why the correct answer wins: A predefined role that matches the write task carries nothing else.
- **C:** Incorrect for this question. Daily use of the super administrator role removes the separation that makes directory recovery accountable. Why the correct answer wins: A predefined role that matches the write task carries nothing else.
- **D:** Correct. A predefined role carries the permissions the task needs and nothing broader. In this case: A predefined role that matches the write task carries nothing else.

### Question 11 — D, E

Answers: Grant the caller the Service Account Token Creator role on the target account; Issue a short-lived access token through impersonation or metadata. Impersonation removes the stored key, and a short-lived token expires without a rotation. Impersonation lets a principal act as the service account without holding a key for it. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation removes the stored key, and a short-lived token expires without a rotation.
- **B:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Impersonation removes the stored key, and a short-lived token expires without a rotation.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation removes the stored key, and a short-lived token expires without a rotation.
- **D:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: Impersonation removes the stored key, and a short-lived token expires without a rotation.
- **E:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation removes the stored key, and a short-lived token expires without a rotation.

### Question 12 — C

Answer: Create a service account key and embed it in the application configuration. A downloaded service account key carries no expiry unless one is set. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.
- **B:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.
- **C:** Correct. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. In this case: A downloaded service account key carries no expiry unless one is set.
- **D:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A downloaded service account key carries no expiry unless one is set.

### Question 13 — C

Answer: Issue a short-lived access token through impersonation or metadata. A short-lived token stops working at the end of its window. A short-lived token expires on its own, so a leaked value has a bounded window of use. Local study-map skill 1.5 (Service Account Keys and Short-Lived Credentials), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Why the correct answer wins: A short-lived token stops working at the end of its window.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: A short-lived token stops working at the end of its window.
- **C:** Correct. A short-lived token expires on its own, so a leaked value has a bounded window of use. In this case: A short-lived token stops working at the end of its window.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A short-lived token stops working at the end of its window.

### Question 14 — C

Answer: Configure Workload Identity Federation for the external workload. Workload Identity Federation exchanges the service's own token. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Workload Identity Federation exchanges the service's own token.
- **B:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Workload Identity Federation exchanges the service's own token.
- **C:** Correct. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. In this case: Workload Identity Federation exchanges the service's own token.
- **D:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Workload Identity Federation exchanges the service's own token.

### Question 15 — A

Answer: Restrict the Workload Identity pool with an attribute condition on the subject. An attribute condition restricts which external identities may act. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. Local study-map skill 1.6 (Workload Identity Federation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An attribute condition limits which external identities may impersonate, so a whole provider cannot mint tokens. In this case: An attribute condition restricts which external identities may act.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **C:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: An attribute condition restricts which external identities may act.
- **D:** Incorrect for this question. Domain restricted sharing keeps a resource grant from naming an identity outside the allowed domain. Why the correct answer wins: An attribute condition restricts which external identities may act.

### Question 16 — C

Answer: Grant the caller the Service Account Token Creator role on the target account. Impersonation gives the acting right for the period. Impersonation lets a principal act as the service account without holding a key for it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Impersonation gives the acting right for the period.
- **B:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: Impersonation gives the acting right for the period.
- **C:** Correct. Impersonation lets a principal act as the service account without holding a key for it. In this case: Impersonation gives the acting right for the period.
- **D:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: Impersonation gives the acting right for the period.

### Question 17 — D

Answer: Hand the caller a JSON key for the service account instead. A handed-out key cannot be scoped and outlives the engagement. A handed-out key cannot be scoped to one action and outlives the task that needed it. Local study-map skill 1.7 (Service Account Impersonation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A short-lived token expires on its own, so a leaked value has a bounded window of use. Why the correct answer wins: A handed-out key cannot be scoped and outlives the engagement.
- **B:** Incorrect for this question. Workload Identity Federation exchanges an external OIDC or SAML token for short-lived Google credentials with no key on disk. Why the correct answer wins: A handed-out key cannot be scoped and outlives the engagement.
- **C:** Incorrect for this question. Impersonation lets a principal act as the service account without holding a key for it. Why the correct answer wins: A handed-out key cannot be scoped and outlives the engagement.
- **D:** Correct. A handed-out key cannot be scoped to one action and outlives the task that needed it. In this case: A handed-out key cannot be scoped and outlives the engagement.

### Question 18 — D

Answer: Enforce 2-step verification for the whole organisation. Enforced 2-step verification leaves the attacker one factor short. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: Enforced 2-step verification leaves the attacker one factor short.
- **B:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: Enforced 2-step verification leaves the attacker one factor short.
- **C:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: Enforced 2-step verification leaves the attacker one factor short.
- **D:** Correct. Enforced 2-step verification turns a stolen password into a partial factor rather than a login. In this case: Enforced 2-step verification leaves the attacker one factor short.

### Question 19 — A

Answer: Enforce a password policy with a minimum length and a reuse ban. A password policy adds length, complexity, and a reuse ban. A password policy raises the cost of credential guessing without depending on the user to choose well. Local study-map skill 1.8 (Password, Session, and 2-Step Verification Policy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A password policy raises the cost of credential guessing without depending on the user to choose well. In this case: A password policy adds length, complexity, and a reuse ban.
- **B:** Incorrect for this question. Disabling unused APIs removes an attack surface that no code enables on purpose. Why the correct answer wins: A password policy adds length, complexity, and a reuse ban.
- **C:** Incorrect for this question. A session control limits how long a stolen browser session stays useful. Why the correct answer wins: A password policy adds length, complexity, and a reuse ban.
- **D:** Incorrect for this question. Optional enrolment leaves the accounts that most need the second factor without one. Why the correct answer wins: A password policy adds length, complexity, and a reuse ban.

### Question 20 — B, C

Answers: Grant the role through Privileged Access Manager with an approval and a time limit; Read the Policy Analyzer output before removing an unused grant. Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The basic roles span every service in the project and cannot express least privilege. Why the correct answer wins: Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage.
- **B:** Correct. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. In this case: Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage.
- **C:** Correct. Policy Intelligence shows who actually used a permission, so a removal is evidence-based. In this case: Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage.
- **D:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage.
- **E:** Incorrect for this question. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Why the correct answer wins: Privileged Access Manager gates and expires the grant, and Policy Analyser shows the usage.

### Question 21 — B

Answer: Grant the privileged role permanently and review it once a year. Standing privilege is live in the hours nobody is watching. Permanent privilege is live for every hour of the year, including the hours nobody is watching. Local study-map skill 1.9 (Privileged Roles, Separation of Duties, and PAM), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A group binding keeps the policy small and makes the reviewer look at membership instead of bindings. Why the correct answer wins: Standing privilege is live in the hours nobody is watching.
- **B:** Correct. Permanent privilege is live for every hour of the year, including the hours nobody is watching. In this case: Standing privilege is live in the hours nobody is watching.
- **C:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: Standing privilege is live in the hours nobody is watching.
- **D:** Incorrect for this question. Privileged Access Manager issues a temporary grant only after approval, so standing privilege disappears. Why the correct answer wins: Standing privilege is live in the hours nobody is watching.

### Question 22 — D

Answer: Add an IAM condition that limits the grant to a time window and a resource prefix. An IAM condition puts a time limit on the grant. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: An IAM condition puts a time limit on the grant.
- **B:** Incorrect for this question. A predefined role carries the permissions the task needs and nothing broader. Why the correct answer wins: An IAM condition puts a time limit on the grant.
- **C:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: An IAM condition puts a time limit on the grant.
- **D:** Correct. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. In this case: An IAM condition puts a time limit on the grant.

### Question 23 — A

Answer: Write an Access Context Manager access level and bind it to the perimeter. An access level in Access Context Manager describes the required request context. Access Context Manager describes the request context, such as network origin, that a policy can require. Local study-map skill 1.10 (IAM Conditions, Deny Policies, and Access Context Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Access Context Manager describes the request context, such as network origin, that a policy can require. In this case: An access level in Access Context Manager describes the required request context.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: An access level in Access Context Manager describes the required request context.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An access level in Access Context Manager describes the required request context.
- **D:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: An access level in Access Context Manager describes the required request context.

### Question 24 — B, C

Answers: Create a folder per environment and attach the policy at the folder; Enforce the constraint with an organization policy. The folder attachment covers the department, and the organization policy inherits to each project. A folder boundary means one attachment covers every current and future project inside it. An organization policy applies to every project beneath it, so a new project cannot opt out. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual update depends on someone remembering, which is exactly where stale access survives. Why the correct answer wins: The folder attachment covers the department, and the organization policy inherits to each project.
- **B:** Correct. A folder boundary means one attachment covers every current and future project inside it. In this case: The folder attachment covers the department, and the organization policy inherits to each project.
- **C:** Correct. An organization policy applies to every project beneath it, so a new project cannot opt out. In this case: The folder attachment covers the department, and the organization policy inherits to each project.
- **D:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: The folder attachment covers the department, and the organization policy inherits to each project.
- **E:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: The folder attachment covers the department, and the organization policy inherits to each project.

### Question 25 — A

Answer: Enforce the constraint with an organization policy. An organization policy binds every project beneath it. Local study-map skill 1.11 (Resource Hierarchy and Organization Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 1 (configuring access): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An organization policy binds every project beneath it.
- **B:** Incorrect for this question. An IAM condition narrows an existing grant to stated circumstances instead of creating a second role. Why the correct answer wins: An organization policy binds every project beneath it.
- **C:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: An organization policy binds every project beneath it.
- **D:** Incorrect for this question. A folder boundary means one attachment covers every current and future project inside it. Why the correct answer wins: An organization policy binds every project beneath it.

### Question 26 — A

Answer: Deploy a hierarchical firewall policy at the organisation or folder level. A hierarchical policy applies to everything beneath the node. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. In this case: A hierarchical policy applies to everything beneath the node.
- **B:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: A hierarchical policy applies to everything beneath the node.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: A hierarchical policy applies to everything beneath the node.
- **D:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: A hierarchical policy applies to everything beneath the node.

### Question 27 — B

Answer: Allow all egress and rely on the application to be careful. An allow-all rule reaches anything the internet offers. Unrestricted egress lets a compromised workload reach anything the internet offers. Local study-map skill 2.1 (Firewall Rules and Hierarchical Policies), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: An allow-all rule reaches anything the internet offers.
- **B:** Correct. Unrestricted egress lets a compromised workload reach anything the internet offers. In this case: An allow-all rule reaches anything the internet offers.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: An allow-all rule reaches anything the internet offers.
- **D:** Incorrect for this question. A hierarchical policy is evaluated before project rules, so a project cannot open a port the policy closed. Why the correct answer wins: An allow-all rule reaches anything the internet offers.

### Question 28 — D, E

Answers: Enable layer 7 inspection on the firewall policy for the egress rule; Deploy Cloud IDS on the network. Layer 7 inspection reads the name, and Cloud IDS raises the finding. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Layer 7 inspection reads the name, and Cloud IDS raises the finding.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Layer 7 inspection reads the name, and Cloud IDS raises the finding.
- **C:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Layer 7 inspection reads the name, and Cloud IDS raises the finding.
- **D:** Correct. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. In this case: Layer 7 inspection reads the name, and Cloud IDS raises the finding.
- **E:** Correct. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. In this case: Layer 7 inspection reads the name, and Cloud IDS raises the finding.

### Question 29 — A

Answer: Filter on address and port only and allow the rest. A layer 4 rule filters on address and port only. A layer 4 rule cannot see the destination host name inside an allowed connection. Local study-map skill 2.2 (Layer 7 Inspection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A layer 4 rule cannot see the destination host name inside an allowed connection. In this case: A layer 4 rule filters on address and port only.
- **B:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **C:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: A layer 4 rule filters on address and port only.
- **D:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A layer 4 rule filters on address and port only.

### Question 30 — A

Answer: Attach a Cloud Armor security policy to the backend service. Cloud Armor applies the limit at the edge. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. In this case: Cloud Armor applies the limit at the edge.
- **B:** Incorrect for this question. Project-level rules are editable by the project owner and are evaluated after the hierarchy. Why the correct answer wins: Cloud Armor applies the limit at the edge.
- **C:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Cloud Armor applies the limit at the edge.
- **D:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: Cloud Armor applies the limit at the edge.

### Question 31 — C

Answer: Enable Cloud Armor bot management on the policy. Bot management scores automated traffic so a rule can separate it from a person. Local study-map skill 2.3 (Cloud Armor Web Application Firewall), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. In-application filtering happens after the request has already consumed backend capacity. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it from a person.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it from a person.
- **C:** Correct. In this case: Bot management scores automated traffic so a rule can separate it from a person.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Bot management scores automated traffic so a rule can separate it from a person.

### Question 32 — C

Answer: Put Identity-Aware Proxy in front of the application. IAP authorises each request against IAM. IAP authenticates and authorises each request against IAM before it reaches the backend. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Why the correct answer wins: IAP authorises each request against IAM.
- **B:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: IAP authorises each request against IAM.
- **C:** Correct. IAP authenticates and authorises each request against IAM before it reaches the backend. In this case: IAP authorises each request against IAM.
- **D:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: IAP authorises each request against IAM.

### Question 33 — C

Answer: Publish the application only through a VPN concentrator. A VPN authenticates the tunnel and not the individual request. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. Local study-map skill 2.4 (Identity-Aware Proxy), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IAP authenticates and authorises each request against IAM before it reaches the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **B:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.
- **C:** Correct. A VPN gates the network path but not the individual user, so anyone on the tunnel reaches the app. In this case: A VPN authenticates the tunnel and not the individual request.
- **D:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: A VPN authenticates the tunnel and not the individual request.

### Question 34 — B, D

Answers: Issue internal certificates from Certificate Authority Service; Terminate TLS at the load balancer with a managed certificate. Certificate Authority Service issues them, and the load balancer terminates the handshake. Certificate Authority Service issues and revokes private certificates with an auditable authority. Terminating at the load balancer gives one managed certificate and a single policy point. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Certificate Authority Service issues them, and the load balancer terminates the handshake.
- **B:** Correct. Certificate Authority Service issues and revokes private certificates with an auditable authority. In this case: Certificate Authority Service issues them, and the load balancer terminates the handshake.
- **C:** Incorrect for this question. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Why the correct answer wins: Certificate Authority Service issues them, and the load balancer terminates the handshake.
- **D:** Correct. Terminating at the load balancer gives one managed certificate and a single policy point. In this case: Certificate Authority Service issues them, and the load balancer terminates the handshake.
- **E:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Certificate Authority Service issues them, and the load balancer terminates the handshake.

### Question 35 — D

Answer: Pass encrypted traffic straight through to the instance. Pass-through keeps the handshake end to end. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. Local study-map skill 2.5 (TLS, Load Balancing, and Certificate Authority Service), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Self-signed certificates cannot be validated by a client that has no prior trust in them. Why the correct answer wins: Pass-through keeps the handshake end to end.
- **B:** Incorrect for this question. A layer 4 rule cannot see the destination host name inside an allowed connection. Why the correct answer wins: Pass-through keeps the handshake end to end.
- **C:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Pass-through keeps the handshake end to end.
- **D:** Correct. Pass-through moves certificate lifecycle and cipher policy onto every backend separately. In this case: Pass-through keeps the handshake end to end.

### Question 36 — B

Answer: Route the egress through Secure Web Proxy. Secure Web Proxy inspects and allowlists the traffic. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Secure Web Proxy inspects and allowlists the traffic.
- **B:** Correct. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. In this case: Secure Web Proxy inspects and allowlists the traffic.
- **C:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Secure Web Proxy inspects and allowlists the traffic.
- **D:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Secure Web Proxy inspects and allowlists the traffic.

### Question 37 — C

Answer: Turn on DNSSEC for the public zone. DNSSEC signs the answers for the resolver to verify. DNSSEC signs the answers so a resolver can detect a forged response. Local study-map skill 2.6 (Secure Web Proxy and Cloud DNS Security), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: DNSSEC signs the answers for the resolver to verify.
- **B:** Incorrect for this question. Secure Web Proxy applies an allowlist and TLS inspection to outbound web traffic from the workload. Why the correct answer wins: DNSSEC signs the answers for the resolver to verify.
- **C:** Correct. DNSSEC signs the answers so a resolver can detect a forged response. In this case: DNSSEC signs the answers for the resolver to verify.
- **D:** Incorrect for this question. A response policy overrides resolution for named domains inside the network. Why the correct answer wins: DNSSEC signs the answers for the resolver to verify.

### Question 38 — B

Answer: Deploy the instances with internal IP addresses only. An internal-only address removes the inbound path. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An internal-only address removes the inbound path.
- **B:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: An internal-only address removes the inbound path.
- **C:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: An internal-only address removes the inbound path.
- **D:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: An internal-only address removes the inbound path.

### Question 39 — A

Answer: Restrict the project to the APIs it needs and review them on a schedule. Disabling unused APIs removes an attack surface nothing needs. Disabling unused APIs removes an attack surface that no code enables on purpose. Local study-map skill 2.7 (Private Addressing and API Restriction), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Disabling unused APIs removes an attack surface that no code enables on purpose. In this case: Disabling unused APIs removes an attack surface nothing needs.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **C:** Incorrect for this question. An organization policy applies to every project beneath it, so a new project cannot opt out. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.
- **D:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Disabling unused APIs removes an attack surface nothing needs.

### Question 40 — A, D

Answers: Peer the two VPC networks and scope the firewall rules to the peer; Give each tier its own subnet and allow only the flows between adjacent tiers. Peering gives the reachability, and tier subnets express the allowed flows. Peering gives private reachability while firewall rules still decide which flows are allowed. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Peering gives private reachability while firewall rules still decide which flows are allowed. In this case: Peering gives the reachability, and tier subnets express the allowed flows.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Peering gives the reachability, and tier subnets express the allowed flows.
- **C:** Incorrect for this question. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Why the correct answer wins: Peering gives the reachability, and tier subnets express the allowed flows.
- **D:** Correct. Tier subnets let firewall rules express which tier may call which, rather than allowing the whole range. In this case: Peering gives the reachability, and tier subnets express the allowed flows.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Peering gives the reachability, and tier subnets express the allowed flows.

### Question 41 — B

Answer: Host the workload in a Shared VPC service project. Shared VPC centralises the network in the host project. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. Local study-map skill 2.8 (VPC Firewalls, Peering, and Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **B:** Correct. Shared VPC centralises the network and the firewall in the host project while the workload stays in its own project. In this case: Shared VPC centralises the network in the host project.
- **C:** Incorrect for this question. Peering gives private reachability while firewall rules still decide which flows are allowed. Why the correct answer wins: Shared VPC centralises the network in the host project.
- **D:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Shared VPC centralises the network in the host project.

### Question 42 — C

Answer: Create a service perimeter with VPC Service Controls. A service perimeter blocks the movement whatever the grant says. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An IAM grant still permits a copy out of the project; only a perimeter stops the movement. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.
- **B:** Incorrect for this question. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.
- **C:** Correct. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. In this case: A service perimeter blocks the movement whatever the grant says.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: A service perimeter blocks the movement whatever the grant says.

### Question 43 — B

Answer: Use restricted.googleapis.com for the API traffic. Restricted virtual IPs keep the API path inside the boundary. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. Local study-map skill 2.9 (VPC Service Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.
- **B:** Correct. Restricted virtual IPs keep API traffic on a path that a perimeter can evaluate. In this case: Restricted virtual IPs keep the API path inside the boundary.
- **C:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.
- **D:** Incorrect for this question. Private Google Access lets an instance with only an internal address reach Google APIs. Why the correct answer wins: Restricted virtual IPs keep the API path inside the boundary.

### Question 44 — A

Answer: Build an HA VPN tunnel pair with two interfaces. An HA VPN pair keeps the link up across one failure. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. In this case: An HA VPN pair keeps the link up across one failure.
- **B:** Incorrect for this question. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Why the correct answer wins: An HA VPN pair keeps the link up across one failure.
- **C:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: An HA VPN pair keeps the link up across one failure.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: An HA VPN pair keeps the link up across one failure.

### Question 45 — D

Answer: Provision a Dedicated Interconnect with two attachments. Dedicated Interconnect provides the private circuit. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. Local study-map skill 2.10 (HA VPN and Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An HA VPN pair gives the published 99.99% SLA and survives the loss of one peer address. Why the correct answer wins: Dedicated Interconnect provides the private circuit.
- **B:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Dedicated Interconnect provides the private circuit.
- **C:** Incorrect for this question. A single tunnel has no redundancy, so one maintenance window drops the path. Why the correct answer wins: Dedicated Interconnect provides the private circuit.
- **D:** Correct. Dedicated Interconnect gives a private circuit with attachments that survive a single link failure. In this case: Dedicated Interconnect provides the private circuit.

### Question 46 — B

Answer: Configure Private Google Access for on-premises hosts over the hybrid route. The on-premises variant of Private Google Access carries the traffic privately. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. Local study-map skill 2.11 (Private Google Access and Private Service Connect), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Private Service Connect endpoint gives the consumer a private address for a service in another VPC. Why the correct answer wins: The on-premises variant of Private Google Access carries the traffic privately.
- **B:** Correct. The on-premises variant lets hosts behind the VPN or Interconnect reach Google APIs without a public path. In this case: The on-premises variant of Private Google Access carries the traffic privately.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: The on-premises variant of Private Google Access carries the traffic privately.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: The on-premises variant of Private Google Access carries the traffic privately.

### Question 47 — A, D

Answers: Place Cloud NAT in front of the private instances; Deploy the instances with internal IP addresses only. Cloud NAT provides the egress, and the internal address blocks the inbound path. Cloud NAT gives the instances outbound connectivity while they keep no external address. An internal-only address means the workload cannot be reached from the internet at all. Local study-map skill 2.12 (Cloud NAT Egress), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 2 (securing communications and boundary protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Cloud NAT gives the instances outbound connectivity while they keep no external address. In this case: Cloud NAT provides the egress, and the internal address blocks the inbound path.
- **B:** Incorrect for this question. Terminating at the load balancer gives one managed certificate and a single policy point. Why the correct answer wins: Cloud NAT provides the egress, and the internal address blocks the inbound path.
- **C:** Incorrect for this question. A single NAT instance is a bottleneck and a single point of failure for every outbound flow. Why the correct answer wins: Cloud NAT provides the egress, and the internal address blocks the inbound path.
- **D:** Correct. An internal-only address means the workload cannot be reached from the internet at all. In this case: Cloud NAT provides the egress, and the internal address blocks the inbound path.
- **E:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Cloud NAT provides the egress, and the internal address blocks the inbound path.

### Question 48 — C, D

Answers: Run a Sensitive Data Protection discovery scan over the storage and warehouse; Reuse a stored de-identification template across pipelines. Discovery finds the data, and a stored template makes the fix identical everywhere. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. A stored template prevents two pipelines from de-identifying the same column differently. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Discovery finds the data, and a stored template makes the fix identical everywhere.
- **B:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: Discovery finds the data, and a stored template makes the fix identical everywhere.
- **C:** Correct. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. In this case: Discovery finds the data, and a stored template makes the fix identical everywhere.
- **D:** Correct. A stored template prevents two pipelines from de-identifying the same column differently. In this case: Discovery finds the data, and a stored template makes the fix identical everywhere.
- **E:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Discovery finds the data, and a stored template makes the fix identical everywhere.

### Question 49 — D

Answer: Save a Sensitive Data Protection inspect template and reuse it. A shared inspect template keeps the detection rules identical. A saved template keeps the detection rules identical across scans, so results stay comparable. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A self-reported inventory misses the tables nobody remembered to mention. Why the correct answer wins: A shared inspect template keeps the detection rules identical.
- **B:** Incorrect for this question. A stored template prevents two pipelines from de-identifying the same column differently. Why the correct answer wins: A shared inspect template keeps the detection rules identical.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: A shared inspect template keeps the detection rules identical.
- **D:** Correct. A saved template keeps the detection rules identical across scans, so results stay comparable. In this case: A shared inspect template keeps the detection rules identical.

### Question 50 — B

Answer: Ask the team to report which tables they believe hold personal data. A self-reported inventory misses what nobody remembered. Local study-map skill 3.1 (Sensitive Data Protection Discovery), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A discovery scan profiles where sensitive data sits so the controls can be aimed at the right buckets and tables. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **B:** Correct. In this case: A self-reported inventory misses what nobody remembered.
- **C:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A self-reported inventory misses what nobody remembered.
- **D:** Incorrect for this question. A saved template keeps the detection rules identical across scans, so results stay comparable. Why the correct answer wins: A self-reported inventory misses what nobody remembered.

### Question 51 — C

Answer: Redact the matched values with a de-identification template. Redaction replaces the matched value entirely, so the field keeps its shape without the data. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: Redaction replaces the matched value entirely, so the field keeps its shape without the data.
- **B:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: Redaction replaces the matched value entirely, so the field keeps its shape without the data.
- **C:** Correct. In this case: Redaction replaces the matched value entirely, so the field keeps its shape without the data.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: Redaction replaces the matched value entirely, so the field keeps its shape without the data.

### Question 52 — C

Answer: Replace the value with a pseudonym from a crypto key. A pseudonym keeps a stable token for the join. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: A pseudonym keeps a stable token for the join.
- **B:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: A pseudonym keeps a stable token for the join.
- **C:** Correct. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. In this case: A pseudonym keeps a stable token for the join.
- **D:** Incorrect for this question. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Why the correct answer wins: A pseudonym keeps a stable token for the join.

### Question 53 — A

Answer: Replace the value with an unsalted hash. An unsalted hash of a low-entropy value is easy to reverse. An unsalted hash of a low-entropy value can be reversed with a precomputed table. Local study-map skill 3.2 (De-identification Templates), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. An unsalted hash of a low-entropy value can be reversed with a precomputed table. In this case: An unsalted hash of a low-entropy value is easy to reverse.
- **B:** Incorrect for this question. Format-preserving encryption keeps the column type and length, so legacy code still reads it. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.
- **C:** Incorrect for this question. Pseudonymisation keeps a stable token so records still join, while the original value is not stored. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.
- **D:** Incorrect for this question. Redaction replaces the matched value entirely, so the field keeps its shape and loses the data. Why the correct answer wins: An unsalted hash of a low-entropy value is easy to reverse.

### Question 54 — A

Answer: Grant authorised views or dataset-level IAM rather than table reads. Authorised views expose the aggregate and hide the identifier. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dataset-level authority and authorised views keep the raw table unreadable while exposing the columns that are allowed. In this case: Authorised views expose the aggregate and hide the identifier.
- **B:** Incorrect for this question. An export right hands over every row, including the columns the analyst should not see. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.
- **C:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Authorised views expose the aggregate and hide the identifier.

### Question 55 — B

Answer: Grant the bucket role to a group with uniform bucket-level access. Uniform bucket-level access makes IAM the only decision point. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **B:** Correct. In this case: Uniform bucket-level access makes IAM the only decision point.
- **C:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.
- **D:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: Uniform bucket-level access makes IAM the only decision point.

### Question 56 — C

Answer: Use Cloud SQL IAM database authentication for the application. IAM database authentication binds the connection to an identity. IAM database authentication removes the stored database password and ties each connection to an identity. Local study-map skill 3.3 (Access Control for BigQuery, Cloud Storage, and Cloud SQL), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: IAM database authentication binds the connection to an identity.
- **B:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: IAM database authentication binds the connection to an identity.
- **C:** Correct. IAM database authentication removes the stored database password and ties each connection to an identity. In this case: IAM database authentication binds the connection to an identity.
- **D:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: IAM database authentication binds the connection to an identity.

### Question 57 — B, D

Answers: Store the credential in Secret Manager and grant the workload the secret accessor role; Enable Data Access audit logs for the service. Secret Manager keeps the versions, and Data Access logs record the reads. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: Secret Manager keeps the versions, and Data Access logs record the reads.
- **B:** Correct. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. In this case: Secret Manager keeps the versions, and Data Access logs record the reads.
- **C:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Secret Manager keeps the versions, and Data Access logs record the reads.
- **D:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Secret Manager keeps the versions, and Data Access logs record the reads.
- **E:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Secret Manager keeps the versions, and Data Access logs record the reads.

### Question 58 — D

Answer: Set the credential as a plain environment variable in the deployment. An environment variable is visible in the process listing. Local study-map skill 3.4 (Secret Manager), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password in a config file is copied into every environment and outlives its owner. Why the correct answer wins: An environment variable is visible in the process listing.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: An environment variable is visible in the process listing.
- **C:** Incorrect for this question. Secret Manager versions the value, audits each read, and lets the access be revoked without a redeploy. Why the correct answer wins: An environment variable is visible in the process listing.
- **D:** Correct. In this case: An environment variable is visible in the process listing.

### Question 59 — B

Answer: Require the metadata server header on every request. Requiring the metadata header blocks the simplest forgery. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **B:** Correct. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. In this case: Requiring the metadata header blocks the simplest forgery.
- **C:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.
- **D:** Incorrect for this question. Cloud NAT gives the instances outbound connectivity while they keep no external address. Why the correct answer wins: Requiring the metadata header blocks the simplest forgery.

### Question 60 — D

Answer: Enable OS Login and turn off project-wide SSH keys. OS Login replaces the shared key with per-identity access. OS Login ties each login to an identity and removes the shared key that never expires. Local study-map skill 3.5 (Instance Metadata Protection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A password policy raises the cost of credential guessing without depending on the user to choose well. Why the correct answer wins: OS Login replaces the shared key with per-identity access.
- **B:** Incorrect for this question. Requiring the Metadata-Flavor header blocks the simplest server-side request forgery against the metadata server. Why the correct answer wins: OS Login replaces the shared key with per-identity access.
- **C:** Incorrect for this question. A downloaded key never expires, is copied into build systems, and cannot be traced to a single caller. Why the correct answer wins: OS Login replaces the shared key with per-identity access.
- **D:** Correct. OS Login ties each login to an identity and removes the shared key that never expires. In this case: OS Login replaces the shared key with per-identity access.

### Question 61 — D

Answer: Rely on Google default encryption at rest. Default encryption protects the bytes with no customer key work. Google default encryption protects the bytes at rest and needs no key management from the customer. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **B:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **C:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Default encryption protects the bytes with no customer key work.
- **D:** Correct. Google default encryption protects the bytes at rest and needs no key management from the customer. In this case: Default encryption protects the bytes with no customer key work.

### Question 62 — D

Answer: Encrypt the dataset with a customer-managed key in Cloud KMS. A customer-managed key can be disabled by its owner. A customer-managed key lets the customer disable the key and stop every read of the data. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **C:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: A customer-managed key can be disabled by its owner.
- **D:** Correct. A customer-managed key lets the customer disable the key and stop every read of the data. In this case: A customer-managed key can be disabled by its owner.

### Question 63 — B

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM keeps the material with the external manager. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.6 (Default Encryption and CMEK), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM keeps the material with the external manager.
- **B:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM keeps the material with the external manager.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Cloud EKM keeps the material with the external manager.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM keeps the material with the external manager.

### Question 64 — C

Answer: Hold the key in Cloud External Key Manager outside Google Cloud. Cloud EKM makes the external manager part of the read path. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: Cloud EKM makes the external manager part of the read path.
- **B:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Cloud EKM makes the external manager part of the read path.
- **C:** Correct. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. In this case: Cloud EKM makes the external manager part of the read path.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Cloud EKM makes the external manager part of the read path.

### Question 65 — A

Answer: Import the wrapping key into Cloud KMS. Key import brings the pre-existing material into KMS. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Local study-map skill 3.7 (Cloud EKM and Key Import), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Key import brings existing key material under KMS control so the old key can still unwrap old objects. In this case: Key import brings the pre-existing material into KMS.
- **B:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Key import brings the pre-existing material into KMS.
- **C:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Key import brings the pre-existing material into KMS.
- **D:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Key import brings the pre-existing material into KMS.

### Question 66 — D, E

Answers: Set a rotation period on the key; Disable the key version and re-wrap the data. Rotation produces the new versions, and revocation disables the suspect one. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Rotation produces the new versions, and revocation disables the suspect one.
- **B:** Incorrect for this question. A key stored beside the data gives an attacker both halves of the protection. Why the correct answer wins: Rotation produces the new versions, and revocation disables the suspect one.
- **C:** Incorrect for this question. Cloud EKM keeps the key material with a third party, so the customer controls availability of the key itself. Why the correct answer wins: Rotation produces the new versions, and revocation disables the suspect one.
- **D:** Correct. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. In this case: Rotation produces the new versions, and revocation disables the suspect one.
- **E:** Correct. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. In this case: Rotation produces the new versions, and revocation disables the suspect one.

### Question 67 — B

Answer: Disable the key version and re-wrap the data. Disabling the version makes the bytes unreadable. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. Local study-map skill 3.8 (Key Rotation and Revocation), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: Disabling the version makes the bytes unreadable.
- **B:** Correct. Disabling the version is the mechanism that makes the protected bytes unreadable immediately. In this case: Disabling the version makes the bytes unreadable.
- **C:** Incorrect for this question. Rotation issues new key versions on a schedule, which bounds how long one version protects new data. Why the correct answer wins: Disabling the version makes the bytes unreadable.
- **D:** Incorrect for this question. Key import brings existing key material under KMS control so the old key can still unwrap old objects. Why the correct answer wins: Disabling the version makes the bytes unreadable.

### Question 68 — C

Answer: Run the workload on a Confidential VM. A Confidential VM keeps memory encrypted in use. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **B:** Incorrect for this question. Google default encryption protects the bytes at rest and needs no key management from the customer. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.
- **C:** Correct. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. In this case: A Confidential VM keeps memory encrypted in use.
- **D:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential VM keeps memory encrypted in use.

### Question 69 — C

Answer: Run the pod in a Confidential GKE node pool. A Confidential GKE node pool protects each pod. Confidential GKE extends in-use memory protection to each pod on the node. Local study-map skill 3.9 (Confidential Computing), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. OS Login ties each login to an identity and removes the shared key that never expires. Why the correct answer wins: A Confidential GKE node pool protects each pod.
- **B:** Incorrect for this question. A customer-managed key lets the customer disable the key and stop every read of the data. Why the correct answer wins: A Confidential GKE node pool protects each pod.
- **C:** Correct. Confidential GKE extends in-use memory protection to each pod on the node. In this case: A Confidential GKE node pool protects each pod.
- **D:** Incorrect for this question. A Confidential VM keeps memory encrypted while in use, so the host cannot read the data. Why the correct answer wins: A Confidential GKE node pool protects each pod.

### Question 70 — B, E

Answers: Attach an object lifecycle rule that keeps the required retention; Apply a retention policy with bucket lock. The lifecycle rule deletes on schedule, and bucket lock fixes the floor. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. Bucket lock makes the retention period immutable, so not even an owner can delete early. Local study-map skill 3.10 (Storage Lifecycle and Retention), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 3 (ensuring data protection): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unrestricted egress lets a compromised workload reach anything the internet offers. Why the correct answer wins: The lifecycle rule deletes on schedule, and bucket lock fixes the floor.
- **B:** Correct. Bucket lock makes the retention period immutable, so not even an owner can delete early. In this case: The lifecycle rule deletes on schedule, and bucket lock fixes the floor.
- **C:** Incorrect for this question. An object ACL that names allUsers is invisible to a reviewer who only reads the bucket policy. Why the correct answer wins: The lifecycle rule deletes on schedule, and bucket lock fixes the floor.
- **D:** Incorrect for this question. An unlisted public bucket is still readable by anyone who learns the object name. Why the correct answer wins: The lifecycle rule deletes on schedule, and bucket lock fixes the floor.
- **E:** Correct. A lifecycle rule keeps or deletes objects on a schedule, which is how a retention obligation is met. In this case: The lifecycle rule deletes on schedule, and bucket lock fixes the floor.

### Question 71 — D

Answer: Add an Artifact Analysis scan to the CI pipeline. Pipeline scanning fails the build on the finding. Scanning in the pipeline stops the image before it is deployed, not after. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Pipeline scanning fails the build on the finding.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: Pipeline scanning fails the build on the finding.
- **C:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Pipeline scanning fails the build on the finding.
- **D:** Correct. Scanning in the pipeline stops the image before it is deployed, not after. In this case: Pipeline scanning fails the build on the finding.

### Question 72 — D

Answer: Scan the running image in production once a quarter. A production scan checks the images in use. A quarterly production scan finds the vulnerable image after it has already run. Local study-map skill 4.1 (CVE Scanning in CI/CD), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A production scan checks the images in use.
- **B:** Incorrect for this question. Dry-run records the violation and still admits the image. Why the correct answer wins: A production scan checks the images in use.
- **C:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: A production scan checks the images in use.
- **D:** Correct. A quarterly production scan finds the vulnerable image after it has already run. In this case: A production scan checks the images in use.

### Question 73 — A, B

Answers: Enforce a Binary Authorization policy that requires an attested image; Deploy with Binary Authorization in dry-run mode only. Dry-run shows the effect, and enforcement refuses the image. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Dry-run records the violation and still admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Dry-run records the violation and still admits the image. In this case: Dry-run shows the effect, and enforcement refuses the image.
- **B:** Correct. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. In this case: Dry-run shows the effect, and enforcement refuses the image.
- **C:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Dry-run shows the effect, and enforcement refuses the image.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: Dry-run shows the effect, and enforcement refuses the image.
- **E:** Incorrect for this question. An internal-only address means the workload cannot be reached from the internet at all. Why the correct answer wins: Dry-run shows the effect, and enforcement refuses the image.

### Question 74 — D

Answer: Deploy with Binary Authorization in dry-run mode only. Dry-run records the violation and admits the image. Local study-map skill 4.2 (Binary Authorization), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Dry-run records the violation and admits the image.
- **B:** Incorrect for this question. Scanning in the pipeline stops the image before it is deployed, not after. Why the correct answer wins: Dry-run records the violation and admits the image.
- **C:** Incorrect for this question. Binary Authorization refuses to admit an image that lacks the attestation the policy demands. Why the correct answer wins: Dry-run records the violation and admits the image.
- **D:** Correct. In this case: Dry-run records the violation and admits the image.

### Question 75 — A

Answer: Build the base image from a hardened source with a documented baseline. A hardened baseline trims the image. A hardened baseline removes the packages and accounts that a general-purpose image ships. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A hardened baseline removes the packages and accounts that a general-purpose image ships. In this case: A hardened baseline trims the image.
- **B:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: A hardened baseline trims the image.
- **C:** Incorrect for this question. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Why the correct answer wins: A hardened baseline trims the image.
- **D:** Incorrect for this question. A quarterly production scan finds the vulnerable image after it has already run. Why the correct answer wins: A hardened baseline trims the image.

### Question 76 — B

Answer: Schedule patch jobs across the fleet with VM Manager. VM Manager applies and reports the patches. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. Local study-map skill 4.3 (Hardened Images and Patch Management), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hardened baseline removes the packages and accounts that a general-purpose image ships. Why the correct answer wins: VM Manager applies and reports the patches.
- **B:** Correct. VM Manager applies and reports operating-system patches on a schedule, with a record of each host. In this case: VM Manager applies and reports the patches.
- **C:** Incorrect for this question. An unmanaged schedule leaves hosts at different patch levels with no fleet view. Why the correct answer wins: VM Manager applies and reports the patches.
- **D:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: VM Manager applies and reports the patches.

### Question 77 — A

Answer: Deploy a Security Health Analytics custom module for the check. A custom module produces the recurring finding. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. A custom module turns a local configuration rule into a recurring finding in Security Command Center. In this case: A custom module produces the recurring finding.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A custom module produces the recurring finding.
- **C:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: A custom module produces the recurring finding.
- **D:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A custom module produces the recurring finding.

### Question 78 — C

Answer: Compare the deployed configuration with the intended state on a schedule. A scheduled comparison finds the change that bypassed the pipeline. A scheduled comparison detects the change that happened outside the pipeline. Local study-map skill 4.4 (Posture Management and Drift Detection), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **B:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.
- **C:** Correct. A scheduled comparison detects the change that happened outside the pipeline. In this case: A scheduled comparison finds the change that bypassed the pipeline.
- **D:** Incorrect for this question. A custom constraint blocks the configuration change outright, which prevents the drift instead of reporting it. Why the correct answer wins: A scheduled comparison finds the change that bypassed the pipeline.

### Question 79 — A

Answer: Enable VPC Flow Logs on the subnets. Flow logs record the accepted and rejected five-tuples. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Flow logs record the accepted and rejected five-tuples.
- **B:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.
- **D:** Incorrect for this question. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Why the correct answer wins: Flow logs record the accepted and rejected five-tuples.

### Question 80 — D

Answer: Deploy Cloud IDS on the network. Cloud IDS inspects the traffic and raises the finding. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Armor evaluates request attributes at the load balancer and blocks or rate-limits before the backend. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **C:** Incorrect for this question. Layer 7 inspection reads the application protocol, so a rule can act on the URL or the TLS server name. Why the correct answer wins: Cloud IDS inspects the traffic and raises the finding.
- **D:** Correct. In this case: Cloud IDS inspects the traffic and raises the finding.

### Question 81 — C

Answer: Mirror the production traffic to a collector with Packet Mirroring. Packet Mirroring copies the packets to a collector. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. Local study-map skill 4.5 (Network Logs, Cloud IDS, and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **B:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Packet Mirroring copies the packets to a collector.
- **C:** Correct. Packet Mirroring copies the packets so a deep inspection appliance can read the payload. In this case: Packet Mirroring copies the packets to a collector.
- **D:** Incorrect for this question. Cloud IDS inspects the traffic and raises a threat finding for the pattern it recognises. Why the correct answer wins: Packet Mirroring copies the packets to a collector.

### Question 82 — D, E

Answers: Route security logs to a dedicated project with its own retention; Keep the audit evidence for the period the regime requires. A separate log project isolates the evidence, and the retention period keeps it. A dedicated log project keeps the evidence away from the principals who generate it. A retention period for evidence is itself a control, because an expired record proves nothing. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A separate log project isolates the evidence, and the retention period keeps it.
- **B:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A separate log project isolates the evidence, and the retention period keeps it.
- **C:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: A separate log project isolates the evidence, and the retention period keeps it.
- **D:** Correct. A retention period for evidence is itself a control, because an expired record proves nothing. In this case: A separate log project isolates the evidence, and the retention period keeps it.
- **E:** Correct. A dedicated log project keeps the evidence away from the principals who generate it. In this case: A separate log project isolates the evidence, and the retention period keeps it.

### Question 83 — B

Answer: Lower the log volume by disabling data access logs. Disabling the logs removes the record of who read the data. Local study-map skill 4.6 (Logging Strategy and Secure Log Access), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bucket lock makes the retention period immutable, so not even an owner can delete early. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **B:** Correct. In this case: Disabling the logs removes the record of who read the data.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Disabling the logs removes the record of who read the data.
- **D:** Incorrect for this question. A dedicated log project keeps the evidence away from the principals who generate it. Why the correct answer wins: Disabling the logs removes the record of who read the data.

### Question 84 — A

Answer: Read the Admin Activity audit log for the change. Admin Activity records the configuration change and the identity. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Admin Activity records the configuration change and the identity.
- **B:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Admin Activity records the configuration change and the identity.
- **C:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Admin Activity records the configuration change and the identity.
- **D:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Admin Activity records the configuration change and the identity.

### Question 85 — D

Answer: Enable Data Access audit logs for the service. Data Access records the read of the object and must be enabled per service. Data Access logs record the read and write of the data itself, and must be turned on per service. Local study-map skill 4.7 (Audit Logs and Data Access Logs), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Data Access records the read of the object and must be enabled per service.
- **B:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: Data Access records the read of the object and must be enabled per service.
- **C:** Incorrect for this question. Flow logs record the accepted and rejected five-tuples for later analysis. Why the correct answer wins: Data Access records the read of the object and must be enabled per service.
- **D:** Correct. Data Access logs record the read and write of the data itself, and must be turned on per service. In this case: Data Access records the read of the object and must be enabled per service.

### Question 86 — D

Answer: Create an aggregated sink at the organisation level. An aggregated sink covers every project beneath the node. An aggregated sink includes the entries from every project beneath the node in one destination. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **B:** Incorrect for this question. A per-project sink misses every project created after the last one was configured. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **C:** Incorrect for this question. A sink is the routing rule that decides where entries are written. Why the correct answer wins: An aggregated sink covers every project beneath the node.
- **D:** Correct. An aggregated sink includes the entries from every project beneath the node in one destination. In this case: An aggregated sink covers every project beneath the node.

### Question 87 — B

Answer: Export the entries to the external SIEM through Pub/Sub. Pub/Sub delivers the entries outward without an inbound path. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. Local study-map skill 4.8 (Log Sinks and SIEM Export), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An environment variable is visible in the process listing and in the deployment history. Why the correct answer wins: Pub/Sub delivers the entries outward without an inbound path.
- **B:** Correct. Pub/Sub carries the entries to the SIEM without opening an inbound path into the organisation. In this case: Pub/Sub delivers the entries outward without an inbound path.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: Pub/Sub delivers the entries outward without an inbound path.
- **D:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: Pub/Sub delivers the entries outward without an inbound path.

### Question 88 — B, D

Answers: Publish new findings to Pub/Sub for the response pipeline; Read the Admin Activity audit log for the change. A notification channel feeds the ticket, and Admin Activity records the closure. A notification channel lets the response automation react to a finding as it is created. Admin Activity records the configuration change and the identity that made it, and is always on. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unexplained closure destroys the record that the finding was ever reviewed. Why the correct answer wins: A notification channel feeds the ticket, and Admin Activity records the closure.
- **B:** Correct. Admin Activity records the configuration change and the identity that made it, and is always on. In this case: A notification channel feeds the ticket, and Admin Activity records the closure.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A notification channel feeds the ticket, and Admin Activity records the closure.
- **D:** Correct. A notification channel lets the response automation react to a finding as it is created. In this case: A notification channel feeds the ticket, and Admin Activity records the closure.
- **E:** Incorrect for this question. A pulled key sits in a third-party system and cannot be narrowed to one destination. Why the correct answer wins: A notification channel feeds the ticket, and Admin Activity records the closure.

### Question 89 — A

Answer: Review the Security Command Center findings for the project. Security Command Center aggregates the findings for the tier. Security Command Center collects the findings from the detectors that are enabled for the tier. Local study-map skill 4.9 (Security Command Center Findings), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 4 (managing operations): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. Security Command Center collects the findings from the detectors that are enabled for the tier. In this case: Security Command Center aggregates the findings for the tier.
- **B:** Incorrect for this question. A scheduled comparison detects the change that happened outside the pipeline. Why the correct answer wins: Security Command Center aggregates the findings for the tier.
- **C:** Incorrect for this question. A custom module turns a local configuration rule into a recurring finding in Security Command Center. Why the correct answer wins: Security Command Center aggregates the findings for the tier.
- **D:** Incorrect for this question. Log Analytics turns the sink destination into a queryable store for the correlation. Why the correct answer wins: Security Command Center aggregates the findings for the tier.

### Question 90 — B

Answer: Document which controls Google operates and which the customer must implement. The shared responsibility split assigns the configuration layer. The shared responsibility split decides what the customer actually has to evidence. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The shared responsibility split assigns the configuration layer.
- **B:** Correct. The shared responsibility split decides what the customer actually has to evidence. In this case: The shared responsibility split assigns the configuration layer.
- **C:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: The shared responsibility split assigns the configuration layer.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The shared responsibility split assigns the configuration layer.

### Question 91 — A

Answer: Assume Google secures every layer once the data is in the cloud. The provider secures the infrastructure, not the configuration written on top. The provider secures the infrastructure, not the configuration the customer writes on top of it. Local study-map skill 5.1 (Shared Responsibility Model), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Correct. The provider secures the infrastructure, not the configuration the customer writes on top of it. In this case: The provider secures the infrastructure, not the configuration written on top.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **C:** Incorrect for this question. The shared responsibility split decides what the customer actually has to evidence. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.
- **D:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: The provider secures the infrastructure, not the configuration written on top.

### Question 92 — C, E

Answers: Create the folder as an Assured Workloads environment; Constrain the resources to the required region with a location organization policy. Assured Workloads applies the personnel controls, and the location constraint fixes the region. Assured Workloads applies the personnel and location controls the regime requires to the folder. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: Assured Workloads applies the personnel controls, and the location constraint fixes the region.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: Assured Workloads applies the personnel controls, and the location constraint fixes the region.
- **C:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: Assured Workloads applies the personnel controls, and the location constraint fixes the region.
- **D:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: Assured Workloads applies the personnel controls, and the location constraint fixes the region.
- **E:** Correct. Assured Workloads applies the personnel and location controls the regime requires to the folder. In this case: Assured Workloads applies the personnel controls, and the location constraint fixes the region.

### Question 93 — C

Answer: Record the regime in a spreadsheet and configure each control by hand. A manual mapping drifts when a project is created without the same settings. Local study-map skill 5.2 (Assured Workloads), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Assured Workloads applies the personnel and location controls the regime requires to the folder. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **B:** Incorrect for this question. A retention period for evidence is itself a control, because an expired record proves nothing. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.
- **C:** Correct. In this case: A manual mapping drifts when a project is created without the same settings.
- **D:** Incorrect for this question. A per-project request has to be repeated for every new project and is forgotten under pressure. Why the correct answer wins: A manual mapping drifts when a project is created without the same settings.

### Question 94 — C

Answer: Turn on Access Transparency and read its logs. Access Transparency records each operator access to customer content. Access Transparency records the occasions when a Google operator accesses customer content. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Data Access logs record the read and write of the data itself, and must be turned on per service. Why the correct answer wins: Access Transparency records each operator access to customer content.
- **B:** Incorrect for this question. Admin Activity records the configuration change and the identity that made it, and is always on. Why the correct answer wins: Access Transparency records each operator access to customer content.
- **C:** Correct. Access Transparency records the occasions when a Google operator accesses customer content. In this case: Access Transparency records each operator access to customer content.
- **D:** Incorrect for this question. Access Approval turns the operator access into a request the customer must grant. Why the correct answer wins: Access Transparency records each operator access to customer content.

### Question 95 — D

Answer: Require Access Approval before an operator may read the content. Access Approval makes the operator wait for the decision. Access Approval turns the operator access into a request the customer must grant. Local study-map skill 5.3 (Access Transparency and Access Approval), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service perimeter blocks access to the protected services from outside the boundary, whatever the IAM grant. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **B:** Incorrect for this question. Access Context Manager describes the request context, such as network origin, that a policy can require. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **C:** Incorrect for this question. Access Transparency records the occasions when a Google operator accesses customer content. Why the correct answer wins: Access Approval makes the operator wait for the decision.
- **D:** Correct. Access Approval turns the operator access into a request the customer must grant. In this case: Access Approval makes the operator wait for the decision.

### Question 96 — D

Answer: Constrain the resources to the required region with a location organization policy. A location constraint blocks resources outside the permitted region. A location constraint blocks the resource from being created outside the permitted region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **B:** Incorrect for this question. A multi-region default places the copy outside the region the regulator named. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **C:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A location constraint blocks resources outside the permitted region.
- **D:** Correct. A location constraint blocks the resource from being created outside the permitted region. In this case: A location constraint blocks resources outside the permitted region.

### Question 97 — B

Answer: Leave the default multi-region setting. A multi-region default places a copy outside the named region. Local study-map skill 5.4 (Regionalization of Data and Services), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A location constraint blocks the resource from being created outside the permitted region. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **B:** Correct. In this case: A multi-region default places a copy outside the named region.
- **C:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A multi-region default places a copy outside the named region.
- **D:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A multi-region default places a copy outside the named region.

### Question 98 — C

Answer: Map each requirement to the control that satisfies it and the evidence it produces. A mapping names the control and the evidence for the clause. A mapping shows the auditor which control answers which clause and where the evidence lives. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The provider secures the infrastructure, not the configuration the customer writes on top of it. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **B:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A mapping names the control and the evidence for the clause.
- **C:** Correct. A mapping shows the auditor which control answers which clause and where the evidence lives. In this case: A mapping names the control and the evidence for the clause.
- **D:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A mapping names the control and the evidence for the clause.

### Question 99 — B

Answer: Keep the audit evidence for the period the regime requires. A retention period for evidence is part of the control. A retention period for evidence is itself a control, because an expired record proves nothing. Local study-map skill 5.5 (Mapping Requirements to Controls), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A retention period for evidence is part of the control.
- **B:** Correct. A retention period for evidence is itself a control, because an expired record proves nothing. In this case: A retention period for evidence is part of the control.
- **C:** Incorrect for this question. Disabling data access logs removes the record that shows who read the data. Why the correct answer wins: A retention period for evidence is part of the control.
- **D:** Incorrect for this question. A named owner is what turns a control list into something that is actually operated. Why the correct answer wins: A retention period for evidence is part of the control.

### Question 100 — D

Answer: Draw the compliance boundary around the projects and services that hold the regulated data. A boundary decides which resources are in scope before testing. A written boundary decides which resources are in scope and which are out, before the audit begins. Local study-map skill 5.6 (Scoping the Compliance Boundary), mapped to the official guide: Google Cloud Professional Cloud Security Engineer exam guide. Primary reference: Professional Cloud Security Engineer exam guide, section 5 (supporting compliance requirements): https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unbounded scope makes the evidence impossible to collect and hides the resources that truly matter. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **B:** Incorrect for this question. An assertion without the control and the evidence is not something an auditor can test. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **C:** Incorrect for this question. A manual mapping drifts the moment a new project is created without the same settings. Why the correct answer wins: A boundary decides which resources are in scope before testing.
- **D:** Correct. A written boundary decides which resources are in scope and which are out, before the audit begins. In this case: A boundary decides which resources are in scope before testing.
