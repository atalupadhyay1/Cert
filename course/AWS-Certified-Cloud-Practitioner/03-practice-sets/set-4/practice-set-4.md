# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 4

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. A bank wants to test a new savings product with real customers in two weeks, without a hardware procurement cycle. Which cloud benefit makes that possible?

- A. Agility: provision resources in minutes
- B. Keep ownership of the physical data centre
- C. Buy servers up front and depreciate them
- D. Reliability through managed, redundant infrastructure

### 2. A tax agency wants to stop buying servers at the start of each five-year cycle and pay for what it runs each month. Which benefit does that describe?

- A. Trade capital expense for variable expense
- B. Global reach: deploy into multiple Regions quickly
- C. Keep ownership of the physical data centre
- D. A flat monthly fee that does not change with usage

### 3. A ministry decides to keep building and running its own machine room rather than using AWS for a sensitive system. Which model has it chosen for that system?

- A. Pay only for what is consumed each month
- B. Pay-as-you-go pricing
- C. Keep ownership of the physical data centre
- D. Volume discounts that grow with usage

### 4. An audit finds that servers were sized for the busiest day of the year and run at five percent utilisation for the other eleven months. Which cost problem is this?

- A. Volume discounts that grow with usage
- B. Pay-as-you-go pricing
- C. Buy for the busiest day and leave the rest idle
- D. Reserved Instances

### 5. A payment chain fails end to end whenever the fraud check takes longer than two seconds, because each step waits on the next. Which characteristic is the cause?

- A. Scale out automatically as demand rises
- B. Break the application into small independent services
- C. Loose coupling with a queue between tiers
- D. Direct synchronous calls between every tier

### 6. Two teams cannot release independently because their components ship in one build and share one database schema. Which design change would let them release separately?

- A. Direct synchronous calls between every tier
- B. Deploy across multiple Availability Zones
- C. Scale the single monolith vertically only
- D. Break the application into small independent services

### 7. A review asks whether each workload delivers its requirement at the lowest price that still meets it. Which Well-Architected pillar covers that?

- A. Security pillar
- B. Cost optimization pillar
- C. Performance efficiency pillar
- D. Reliability pillar

### 8. A design review must show how data and access are protected, and how resources are chosen as demand and technology change. Which two pillars apply? Select two.

- A. Security pillar
- B. Performance efficiency pillar
- C. Reliability pillar
- D. Operational excellence pillar
- E. Cost optimization pillar

### 9. A tax agency buys cloud services but its staff still work in a ticket-driven, hardware-centric model with no cloud roles defined. Which perspective must be addressed?

- A. Platform perspective of the AWS Cloud Adoption Framework
- B. People perspective of the AWS Cloud Adoption Framework
- C. Security perspective of the AWS Cloud Adoption Framework
- D. Business perspective of the AWS Cloud Adoption Framework

### 10. Several departments each fund their own cloud projects and nobody can say which ones matter most. Which perspective would fix that?

- A. Governance perspective of the AWS Cloud Adoption Framework
- B. Platform perspective of the AWS Cloud Adoption Framework
- C. Security perspective of the AWS Cloud Adoption Framework
- D. Operations perspective of the AWS Cloud Adoption Framework

### 11. A reporting database will be moved to a managed engine with small query changes but no redesign of the application. Which strategy is this?

- A. Retain: keep the workload where it is
- B. Rehost: move the application as it is
- C. Refactor: redesign the application for cloud architecture
- D. Replatform: change a few managed components on the way

### 12. A core banking module will be rewritten so it can use managed services and scale per customer. Which strategy is this?

- A. Refactor: redesign the application for cloud architecture
- B. Repurchase: move to a different product
- C. Relocate: move the platform to a cloud-native equivalent
- D. Rehost: move the application as it is

### 13. Field inspectors use mobile devices on a carrier network and need responses in single-digit milliseconds inside the carrier footprint. Which infrastructure option fits?

- A. Edge locations for content delivery
- B. Local Zones for very low latency
- C. AWS Wavelength for carrier networks
- D. AWS Outposts for on-premises capacity

### 14. An architecture review finds the settlement service and its database in one Availability Zone with no replica. Which design problem is this?

- A. Scale out automatically as demand rises
- B. Deploy across multiple Availability Zones
- C. Place everything in one Availability Zone
- D. Loose coupling with a queue between tiers

### 15. A settlement platform must keep processing when one Availability Zone is lost, and must state how quickly it can recover from losing the whole Region. Which two choices fit? Select two.

- A. Define a recovery objective and test the recovery path
- B. Place everything in one Availability Zone
- C. Deploy across multiple Availability Zones
- D. Scale the single monolith vertically only
- E. Direct synchronous calls between every tier

### 16. A department asks who patches the runtime and the underlying host for the Lambda functions it deploys. Under the shared responsibility model, who?

- A. The customer is responsible for the data-centre building
- B. The customer is responsible for the data it stores in AWS
- C. The customer is responsible for patching the guest operating system on Amazon EC2
- D. AWS is responsible for patching a managed service such as Amazon S3

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. An intern's mistaken command deleted a production database because every engineer held administrator access. Which practice made that outcome possible?

- A. Grant only the permissions the task needs
- B. Give every engineer administrator access for convenience
- C. Require multi-factor authentication
- D. Rotate access keys on a schedule

### 18. An auditor asks how the permissions attached to an identity are documented and reviewed as text. Where are they expressed?

- A. Share the root credentials with the operations team
- B. Attach a JSON policy that allows only the required actions
- C. Put the users in a group and attach the policy to the group
- D. Require multi-factor authentication

### 19. The operations team shares one set of root credentials so anyone can fix billing problems. Which practice is this?

- A. Share the root credentials with the operations team
- B. Require multi-factor authentication
- C. Create an IAM user with long-lived credentials
- D. Enable MFA and delete the root access keys

### 20. Keys belonging to a decommissioned integration are still valid months after the project closed. Which control would have limited that exposure?

- A. Enable MFA and delete the root access keys
- B. Share the root credentials with the operations team
- C. Grant only the permissions the task needs
- D. Rotate access keys on a schedule

### 21. Staff must sign in to the AWS accounts with the smartcard-backed corporate identity they use for every other system. What should be configured?

- A. Use the root user for daily administration
- B. Federate the company directory into AWS
- C. Create an IAM user with long-lived credentials
- D. Use Amazon Cognito for customer sign-in

### 22. A citizen-facing portal needs its own account creation, sign-in and token handling for millions of users. Which service fits?

- A. Use Amazon Cognito for customer sign-in
- B. Put the users in a group and attach the policy to the group
- C. Create an IAM user with long-lived credentials
- D. Use IAM Identity Center for workforce sign-in

### 23. A database became reachable from the internet because its rule allowed all ports from any address. Which practice caused the exposure?

- A. Use a security group as a stateful instance firewall
- B. Open every port to the internet and rely on the application
- C. Use AWS Network Firewall for VPC-level inspection
- D. Use a network ACL as a stateless subnet filter

### 24. Instances must accept traffic only from the load balancer on one port, and a public form must reject cross-site scripting attempts. Which two controls fit? Select two.

- A. Use AWS WAF to block web attack patterns
- B. Use AWS Network Firewall for VPC-level inspection
- C. Use a network ACL as a stateless subnet filter
- D. Use a security group as a stateful instance firewall
- E. Use AWS Shield for DDoS protection

### 25. Backup copies are replicated between two Regions over a provider network and must be unreadable on that path. What is required?

- A. Use a customer managed key for the required control
- B. Encrypt data in transit with TLS
- C. Rely on server-side encryption with Amazon S3 managed keys
- D. Set a retention period and delete expired copies

### 26. A regulator requires an audit trail of every use of an encryption key and the ability to disable it centrally. Which service provides that?

- A. Encrypt data in transit with TLS
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Use Amazon Macie to find sensitive data in Amazon S3
- D. Use AWS KMS to create and control encryption keys

### 27. The payment gateway credential must rotate every 30 days without a redeployment. Where should it live?

- A. Put the password in the application source code
- B. Use AWS Certificate Manager for TLS certificates
- C. Store the database credential in AWS Secrets Manager and rotate it
- D. Use AWS KMS to create and control encryption keys

### 28. Compute capacity is being consumed by an unauthorised cryptocurrency miner, and the team needs to be told that the account is compromised. Which service raises that finding?

- A. Use Amazon Inspector to scan workloads for vulnerabilities
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use AWS CloudTrail to record API activity

### 29. A group of accounts needs compromise findings for each one and a single aggregated view with a security score across all of them. Which two services fit? Select two.

- A. Use Amazon Detective to investigate a finding
- B. Use Amazon Inspector to scan workloads for vulnerabilities
- C. Use Amazon Macie to find sensitive data in Amazon S3
- D. Use Amazon GuardDuty to detect suspicious activity
- E. Use AWS Security Hub to aggregate findings in one place

### 30. A database snapshot was shared so a partner could copy it, and it is now downloadable by anyone who finds the identifier. Which mistake was made?

- A. Set a retention period and delete expired copies
- B. Share the snapshot publicly so partners can download it
- C. AWS Backup
- D. An Amazon S3 bucket policy that grants public read

### 31. New buckets must be unable to accept a public read grant, whatever a project team attempts later. What should be applied?

- A. Set a retention period and delete expired copies
- B. An Amazon S3 bucket policy that grants public read
- C. Share the snapshot publicly so partners can download it
- D. Set an S3 lifecycle rule to expire old objects

### 32. An agency must prove that no bucket has been publicly readable at any point in the last ninety days. Which service provides that history?

- A. Use Amazon GuardDuty to detect suspicious activity
- B. Use AWS Audit Manager to collect evidence for an audit
- C. Use AWS Config to record resource configuration changes
- D. Use AWS CloudTrail to record API activity

### 33. An audit must show which identity read a dataset and provide AWS's own certification reports for the underlying infrastructure. Which two services supply that? Select two.

- A. Download the compliance reports from AWS Artifact
- B. Use Amazon GuardDuty to detect suspicious activity
- C. Use AWS CloudTrail to record API activity
- D. Use AWS Audit Manager to collect evidence for an audit
- E. Use AWS Config to record resource configuration changes

### 34. A records officer asks who decides how long citizen records are kept and when they are deleted. Under the shared responsibility model, who?

- A. The customer is responsible for the data it stores in AWS
- B. The customer is responsible for the data-centre building
- C. AWS is responsible for patching a managed service such as Amazon S3
- D. AWS is responsible for the physical facilities and hardware

### 35. A manager wants an organisation-wide guardrail that forbids an unapproved service in every account, while each account's own administrators keep granting approved services. What should be applied?

- A. Attach a JSON policy that allows only the required actions
- B. Apply a service control policy in AWS Organizations
- C. AWS Control Tower
- D. Use a service control policy to grant permissions to a team

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. Each submitted benefit form must be validated and written to a database within a second, with no server to keep running. Which compute service fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. AWS Batch
- C. Amazon EC2 instances
- D. AWS Lambda

### 37. End-of-day interest calculations queue millions of records and need large machines for a few hours each night. Which service fits?

- A. Amazon Lightsail
- B. AWS Batch
- C. AWS App Runner
- D. AWS Lambda

### 38. Years of scanned records are accessed unpredictably, sometimes daily and sometimes not for a year, and the team does not want to move objects by hand. Which storage class fits?

- A. Amazon S3 Standard
- B. Amazon S3 Standard-IA
- C. Amazon S3 Glacier storage classes
- D. Amazon S3 Intelligent-Tiering

### 39. Records read a few times a year must still be available instantly, and a Windows line-of-business application needs a managed shared file system. Which two services fit? Select two.

- A. Amazon S3 Standard-IA
- B. Amazon S3 Glacier storage classes
- C. Amazon EBS volumes
- D. Amazon FSx file systems
- E. Amazon EFS file system

### 40. Investigators must follow relationships between accounts, transfers and addresses across many hops. Which database fits?

- A. Amazon DynamoDB
- B. Amazon Redshift
- C. Amazon RDS
- D. Amazon Neptune

### 41. A case management application needs a managed PostgreSQL database with automated backups and point-in-time restore. Which service fits?

- A. Amazon Redshift
- B. Amazon RDS
- C. Amazon ElastiCache
- D. Amazon DynamoDB

### 42. A three-tier application needs its own isolated network with separate subnets for web, application and database tiers. Which service provides it?

- A. Amazon VPC
- B. Amazon Route 53
- C. Elastic Load Balancing
- D. AWS Direct Connect

### 43. Static assets must be cached close to users in many countries, and the public domain must resolve through a managed DNS service. Which two services fit? Select two.

- A. Elastic Load Balancing
- B. AWS Global Accelerator
- C. Amazon Route 53
- D. Amazon CloudFront
- E. Amazon API Gateway

### 44. A department opens a new account every month and each must inherit the same baseline guardrails automatically. Which service fits?

- A. AWS Control Tower
- B. AWS CloudFormation
- C. AWS Service Catalog
- D. Apply a service control policy in AWS Organizations

### 45. A new account owner wants a quick review of idle resources, open ports and service limits before going live. Which service fits?

- A. Use AWS CloudTrail to record API activity
- B. AWS Trusted Advisor
- C. Use AWS Config to record resource configuration changes
- D. AWS Health Dashboard

### 46. A grant application moves through five decision steps with retries and branching, and the flow must be visible as one execution. Which service fits?

- A. Amazon SNS
- B. Amazon EventBridge
- C. Amazon SQS
- D. AWS Step Functions

### 47. A fraud alert must reach several teams at once, and every card transaction must be ingested as a continuous ordered stream. Which two services fit? Select two.

- A. Amazon Kinesis
- B. Amazon MQ
- C. Amazon EventBridge
- D. Amazon SQS
- E. Amazon SNS

### 48. Programme managers want scheduled dashboards over data already held in AWS, with no servers to run. Which service fits?

- A. Amazon Redshift
- B. Amazon Athena
- C. Amazon QuickSight
- D. Amazon SageMaker

### 49. An auditor needs SQL answers over archived CSV files in Amazon S3 without loading them anywhere. Which service fits?

- A. AWS Glue
- B. Amazon Redshift
- C. Amazon Athena
- D. Amazon EMR

### 50. A release must shift traffic to the new version gradually and roll back automatically when alarms fire. Which service fits?

- A. AWS CodeBuild
- B. AWS CodeDeploy
- C. AWS CodePipeline
- D. AWS X-Ray

### 51. Requests cross six services and the team needs to see which hop contributes most of the latency. Which service fits?

- A. Use AWS Config to record resource configuration changes
- B. Use AWS CloudTrail to record API activity
- C. Amazon CloudWatch
- D. AWS X-Ray

### 52. The whole environment must be declared in a stored template so an auditor can review it and a rebuild produces the same result. Which service fits?

- A. AWS Service Catalog
- B. AWS Control Tower
- C. AWS CloudFormation
- D. AWS Elastic Beanstalk

### 53. An agency API is packaged as a container and must run without a cluster or scaling rules written by the team. Which service fits?

- A. AWS App Runner
- B. Amazon Lightsail
- C. AWS Batch
- D. Amazon EC2 instances

### 54. An investigator must identify who changed the retention setting on a bucket and from which address. Which service holds that record?

- A. Amazon CloudWatch
- B. AWS X-Ray
- C. Use AWS CloudTrail to record API activity
- D. Use AWS Config to record resource configuration changes

### 55. The team needs an alarm on error rate and a reliable record of what each resource's configuration was at the time of the incident. Which two services fit? Select two.

- A. AWS X-Ray
- B. Use AWS Config to record resource configuration changes
- C. Amazon CloudWatch
- D. Use Amazon Inspector to scan workloads for vulnerabilities
- E. Use AWS CloudTrail to record API activity

### 56. An application must reach a payment provider service privately, without any traffic crossing the public internet. Which service fits?

- A. AWS PrivateLink
- B. AWS Transit Gateway
- C. AWS Direct Connect
- D. Amazon VPC

### 57. A regional office needs an encrypted connection to its VPC over the internet within a week. Which service fits?

- A. AWS Global Accelerator
- B. AWS Direct Connect
- C. AWS Site-to-Site VPN
- D. AWS PrivateLink

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. A department wants a discount in exchange for an hourly spend commitment, and wants it to cover both compute and serverless usage. Which option fits?

- A. Spot Instances
- B. On-Demand Instances
- C. Savings Plans
- D. Reserved Instances

### 59. A regulation requires the workload to run on hardware that no other organisation shares, and the team must see the physical sockets. Which option fits?

- A. Savings Plans
- B. On-Demand Instances
- C. Spot Instances
- D. Dedicated Hosts

### 60. Finance asks which service caused last month's increase and by how much, and wants a forecast for the next quarter. Which tool fits?

- A. AWS Cost Explorer
- B. AWS Cost and Usage Report
- C. AWS Pricing Calculator
- D. AWS Budgets

### 61. A migration must be costed before approval, and later the same team must be warned when spend departs from its normal pattern. Which two tools fit? Select two.

- A. AWS Budgets
- B. Cost Anomaly Detection
- C. AWS Pricing Calculator
- D. AWS Cost Explorer
- E. Wait for the monthly invoice and reconcile it afterwards

### 62. Several agencies share a central AWS organisation and want a single invoice while each keeps its own accounts. What should be enabled?

- A. Consolidated billing in AWS Organizations
- B. AWS Cost and Usage Report
- C. Keep a separate bill and separate discounts per account
- D. Tag resources and activate cost allocation tags

### 63. A small team has no budget for support and only needs help with account and billing questions. Which plan fits?

- A. AWS Basic Support
- B. AWS Enterprise Support
- C. AWS Business Support
- D. AWS Developer Support

### 64. An agency lacks the skills to deliver a migration and wants a firm with AWS-validated capability to do the work. What should it use?

- A. Read the AWS documentation and service user guides
- B. Start from an AWS Solutions Library reference deployment
- C. Search AWS re:Post for an answered question
- D. Engage an AWS Partner for the delivery work

### 65. Which discount grows as an organisation's combined usage of a service grows, with no upfront commitment required?

- A. Reserved Instances
- B. Savings Plans
- C. Volume discounts that grow with usage
- D. The AWS Free Tier allowances

---

## Answer key and explanations

### Question 1 — A

Answer: Agility: provision resources in minutes. Resources are provisioned in minutes, so an experiment no longer waits on a purchase order. New environments are created in minutes, which shortens the time to test an idea. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. New environments are created in minutes, which shortens the time to test an idea. In this case: Resources are provisioned in minutes, so an experiment no longer waits on a purchase order.
- **B:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on a purchase order.
- **C:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on a purchase order.
- **D:** Incorrect for this question. Managed services remove single points of failure that a company would otherwise have to engineer. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on a purchase order.

### Question 2 — A

Answer: Trade capital expense for variable expense. Up-front capital investment is replaced by spending that follows usage. Up-front data-centre investment is replaced by usage-based spending. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Up-front data-centre investment is replaced by usage-based spending. In this case: Up-front capital investment is replaced by spending that follows usage.
- **B:** Incorrect for this question. A global infrastructure lets a company put workloads near its users without building facilities. Why the correct answer wins: Up-front capital investment is replaced by spending that follows usage.
- **C:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Up-front capital investment is replaced by spending that follows usage.
- **D:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Up-front capital investment is replaced by spending that follows usage.

### Question 3 — C

Answer: Keep ownership of the physical data centre. The organisation keeps the building, power and hardware lifecycle for itself. The company remains responsible for the building, power and hardware lifecycle. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Costs follow usage, so the bill rises and falls with demand rather than with a purchase decision. Why the correct answer wins: The organisation keeps the building, power and hardware lifecycle for itself.
- **B:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: The organisation keeps the building, power and hardware lifecycle for itself.
- **C:** Correct. The company remains responsible for the building, power and hardware lifecycle. In this case: The organisation keeps the building, power and hardware lifecycle for itself.
- **D:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: The organisation keeps the building, power and hardware lifecycle for itself.

### Question 4 — C

Answer: Buy for the busiest day and leave the rest idle. Sizing for the annual peak means the organisation pays all year for capacity it does not use. Sizing for the annual peak means paying all year for capacity that mostly sits unused. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: Sizing for the annual peak means the organisation pays all year for capacity it does not use.
- **B:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: Sizing for the annual peak means the organisation pays all year for capacity it does not use.
- **C:** Correct. Sizing for the annual peak means paying all year for capacity that mostly sits unused. In this case: Sizing for the annual peak means the organisation pays all year for capacity it does not use.
- **D:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Sizing for the annual peak means the organisation pays all year for capacity it does not use.

### Question 5 — D

Answer: Direct synchronous calls between every tier. A synchronous chain makes every caller hostage to the slowest component in it. A synchronous chain means one slow or failed component fails everything behind it. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Capacity follows the measured demand rather than a forecast. Why the correct answer wins: A synchronous chain makes every caller hostage to the slowest component in it.
- **B:** Incorrect for this question. Independent services can be deployed and scaled separately. Why the correct answer wins: A synchronous chain makes every caller hostage to the slowest component in it.
- **C:** Incorrect for this question. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Why the correct answer wins: A synchronous chain makes every caller hostage to the slowest component in it.
- **D:** Correct. A synchronous chain means one slow or failed component fails everything behind it. In this case: A synchronous chain makes every caller hostage to the slowest component in it.

### Question 6 — D

Answer: Break the application into small independent services. Independent services with their own interfaces can be deployed on their own schedule. Independent services can be deployed and scaled separately. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Independent services with their own interfaces can be deployed on their own schedule.
- **B:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: Independent services with their own interfaces can be deployed on their own schedule.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Independent services with their own interfaces can be deployed on their own schedule.
- **D:** Correct. Independent services can be deployed and scaled separately. In this case: Independent services with their own interfaces can be deployed on their own schedule.

### Question 7 — B

Answer: Cost optimization pillar. The cost optimization pillar asks whether the money spent is delivering the required outcome. The pillar about delivering value at the lowest price that meets the requirement. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: The cost optimization pillar asks whether the money spent is delivering the required outcome.
- **B:** Correct. The pillar about delivering value at the lowest price that meets the requirement. In this case: The cost optimization pillar asks whether the money spent is delivering the required outcome.
- **C:** Incorrect for this question. The pillar about using resources efficiently as demand and technology change. Why the correct answer wins: The cost optimization pillar asks whether the money spent is delivering the required outcome.
- **D:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: The cost optimization pillar asks whether the money spent is delivering the required outcome.

### Question 8 — A, B

Answers: Security pillar; Performance efficiency pillar. Security covers protection of data and access, and performance efficiency covers resource choice as demand changes. The pillar about protecting data, systems and assets through identity and detective controls. The pillar about using resources efficiently as demand and technology change. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The pillar about protecting data, systems and assets through identity and detective controls. In this case: Security covers protection of data and access, and performance efficiency covers resource choice as demand changes.
- **B:** Correct. The pillar about using resources efficiently as demand and technology change. In this case: Security covers protection of data and access, and performance efficiency covers resource choice as demand changes.
- **C:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: Security covers protection of data and access, and performance efficiency covers resource choice as demand changes.
- **D:** Incorrect for this question. The pillar about running and improving workloads, including automation and small reversible changes. Why the correct answer wins: Security covers protection of data and access, and performance efficiency covers resource choice as demand changes.
- **E:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: Security covers protection of data and access, and performance efficiency covers resource choice as demand changes.

### Question 9 — B

Answer: People perspective of the AWS Cloud Adoption Framework. The people perspective covers skills, roles and the organisational change adoption requires. The perspective about skills, roles and organisational change. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The people perspective covers skills, roles and the organisational change adoption requires.
- **B:** Correct. The perspective about skills, roles and organisational change. In this case: The people perspective covers skills, roles and the organisational change adoption requires.
- **C:** Incorrect for this question. The perspective about meeting security and compliance objectives. Why the correct answer wins: The people perspective covers skills, roles and the organisational change adoption requires.
- **D:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The people perspective covers skills, roles and the organisational change adoption requires.

### Question 10 — A

Answer: Governance perspective of the AWS Cloud Adoption Framework. The governance perspective covers prioritisation, budgeting and measuring the programme. The perspective about prioritising, budgeting and measuring the cloud programme. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The perspective about prioritising, budgeting and measuring the cloud programme. In this case: The governance perspective covers prioritisation, budgeting and measuring the programme.
- **B:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme.
- **C:** Incorrect for this question. The perspective about meeting security and compliance objectives. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme.
- **D:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme.

### Question 11 — D

Answer: Replatform: change a few managed components on the way. Replatforming changes a few managed components while leaving the application largely intact. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Replatforming changes a few managed components while leaving the application largely intact.
- **B:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Replatforming changes a few managed components while leaving the application largely intact.
- **C:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Replatforming changes a few managed components while leaving the application largely intact.
- **D:** Correct. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. In this case: Replatforming changes a few managed components while leaving the application largely intact.

### Question 12 — A

Answer: Refactor: redesign the application for cloud architecture. Refactoring redesigns the application to take advantage of cloud services. The application is rewritten to take advantage of managed and elastic services. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The application is rewritten to take advantage of managed and elastic services. In this case: Refactoring redesigns the application to take advantage of cloud services.
- **B:** Incorrect for this question. The company replaces the application with a commercially available equivalent. Why the correct answer wins: Refactoring redesigns the application to take advantage of cloud services.
- **C:** Incorrect for this question. The whole platform moves to a hosted equivalent without changing the application itself. Why the correct answer wins: Refactoring redesigns the application to take advantage of cloud services.
- **D:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Refactoring redesigns the application to take advantage of cloud services.

### Question 13 — C

Answer: AWS Wavelength for carrier networks. Wavelength places compute inside the carrier network close to the mobile devices. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: Wavelength places compute inside the carrier network close to the mobile devices.
- **B:** Incorrect for this question. An extension of a Region placed close to a large population or industry centre. Why the correct answer wins: Wavelength places compute inside the carrier network close to the mobile devices.
- **C:** Correct. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. In this case: Wavelength places compute inside the carrier network close to the mobile devices.
- **D:** Incorrect for this question. A rack of AWS infrastructure installed in the customer facility and operated through AWS. Why the correct answer wins: Wavelength places compute inside the carrier network close to the mobile devices.

### Question 14 — C

Answer: Place everything in one Availability Zone. One Zone is a single failure domain, so a Zone event takes the whole service with it. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Capacity follows the measured demand rather than a forecast. Why the correct answer wins: One Zone is a single failure domain, so a Zone event takes the whole service with it.
- **B:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: One Zone is a single failure domain, so a Zone event takes the whole service with it.
- **C:** Correct. In this case: One Zone is a single failure domain, so a Zone event takes the whole service with it.
- **D:** Incorrect for this question. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Why the correct answer wins: One Zone is a single failure domain, so a Zone event takes the whole service with it.

### Question 15 — A, C

Answers: Deploy across multiple Availability Zones; Define a recovery objective and test the recovery path. A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan. Two or more Zones give the workload a survivor when one Zone fails. A recovery time and recovery point objective turn disaster recovery from an intention into a design. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A recovery time and recovery point objective turn disaster recovery from an intention into a design. In this case: A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan.
- **B:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan.
- **C:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan.
- **D:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan.
- **E:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and recovery objectives define the regional plan.

### Question 16 — D

Answer: AWS is responsible for patching a managed service such as Amazon S3. AWS operates the managed compute environment, so its patching belongs to AWS. The service itself is operated by AWS, including its underlying platform patches. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: AWS operates the managed compute environment, so its patching belongs to AWS.
- **B:** Incorrect for this question. Classification, access and protection of the data remain with the customer. Why the correct answer wins: AWS operates the managed compute environment, so its patching belongs to AWS.
- **C:** Incorrect for this question. The instance is the customer layer, so its operating system and applications are the customer job. Why the correct answer wins: AWS operates the managed compute environment, so its patching belongs to AWS.
- **D:** Correct. The service itself is operated by AWS, including its underlying platform patches. In this case: AWS operates the managed compute environment, so its patching belongs to AWS.

### Question 17 — B

Answer: Give every engineer administrator access for convenience. Broad standing access means one mistake can reach anything in the account. Broad standing access means one mistaken action or stolen credential can change anything. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: Broad standing access means one mistake can reach anything in the account.
- **B:** Correct. Broad standing access means one mistaken action or stolen credential can change anything. In this case: Broad standing access means one mistake can reach anything in the account.
- **C:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Broad standing access means one mistake can reach anything in the account.
- **D:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: Broad standing access means one mistake can reach anything in the account.

### Question 18 — B

Answer: Attach a JSON policy that allows only the required actions. A policy document states the allowed actions and resources in reviewable form. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: A policy document states the allowed actions and resources in reviewable form.
- **B:** Correct. In this case: A policy document states the allowed actions and resources in reviewable form.
- **C:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: A policy document states the allowed actions and resources in reviewable form.
- **D:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: A policy document states the allowed actions and resources in reviewable form.

### Question 19 — A

Answer: Share the root credentials with the operations team. Sharing the root login removes accountability and cannot be limited by policy. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Sharing the root login removes accountability and cannot be limited by policy.
- **B:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.
- **D:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.

### Question 20 — D

Answer: Rotate access keys on a schedule. A rotation schedule retires keys, so an old key stops working after it is replaced. A rotation schedule limits how long a leaked key stays useful. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: A rotation schedule retires keys, so an old key stops working after it is replaced.
- **B:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: A rotation schedule retires keys, so an old key stops working after it is replaced.
- **C:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: A rotation schedule retires keys, so an old key stops working after it is replaced.
- **D:** Correct. A rotation schedule limits how long a leaked key stays useful. In this case: A rotation schedule retires keys, so an old key stops working after it is replaced.

### Question 21 — B

Answer: Federate the company directory into AWS. Federating the corporate directory lets staff use existing identities instead of new AWS credentials. Existing corporate identities are used instead of a separate set of AWS credentials. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: Federating the corporate directory lets staff use existing identities instead of new AWS credentials.
- **B:** Correct. Existing corporate identities are used instead of a separate set of AWS credentials. In this case: Federating the corporate directory lets staff use existing identities instead of new AWS credentials.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Federating the corporate directory lets staff use existing identities instead of new AWS credentials.
- **D:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: Federating the corporate directory lets staff use existing identities instead of new AWS credentials.

### Question 22 — A

Answer: Use Amazon Cognito for customer sign-in. Cognito manages customer sign-up, sign-in and tokens for an application. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Cognito manages customer sign-up, sign-in and tokens for an application.
- **B:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.
- **D:** Incorrect for this question. Workforce users sign in once and receive permission sets for the accounts they use. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.

### Question 23 — B

Answer: Open every port to the internet and rely on the application. Opening every port to the internet publishes every service on the host, including ones nobody meant to expose. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: Opening every port to the internet publishes every service on the host, including ones nobody meant to expose.
- **B:** Correct. In this case: Opening every port to the internet publishes every service on the host, including ones nobody meant to expose.
- **C:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: Opening every port to the internet publishes every service on the host, including ones nobody meant to expose.
- **D:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: Opening every port to the internet publishes every service on the host, including ones nobody meant to expose.

### Question 24 — A, D

Answers: Use a security group as a stateful instance firewall; Use AWS WAF to block web attack patterns. A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns. The group allows inbound or outbound traffic and remembers the connection state. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. In this case: A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns.
- **B:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns.
- **C:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns.
- **D:** Correct. The group allows inbound or outbound traffic and remembers the connection state. In this case: A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns.
- **E:** Incorrect for this question. Shield absorbs distributed denial-of-service traffic before it reaches the application. Why the correct answer wins: A security group allows only the balancer, and WAF inspects the HTTP request for attack patterns.

### Question 25 — B

Answer: Encrypt data in transit with TLS. Encryption in transit protects the data while it crosses the network between Regions. Traffic is protected while it crosses the network, not only while it sits on disk. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The customer controls the key policy and can revoke access by disabling the key. Why the correct answer wins: Encryption in transit protects the data while it crosses the network between Regions.
- **B:** Correct. Traffic is protected while it crosses the network, not only while it sits on disk. In this case: Encryption in transit protects the data while it crosses the network between Regions.
- **C:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: Encryption in transit protects the data while it crosses the network between Regions.
- **D:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: Encryption in transit protects the data while it crosses the network between Regions.

### Question 26 — D

Answer: Use AWS KMS to create and control encryption keys. KMS stores the keys and logs their use, and a key can be disabled to revoke access. A managed key service creates, stores and audits the keys used to encrypt data. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: KMS stores the keys and logs their use, and a key can be disabled to revoke access.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: KMS stores the keys and logs their use, and a key can be disabled to revoke access.
- **C:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: KMS stores the keys and logs their use, and a key can be disabled to revoke access.
- **D:** Correct. A managed key service creates, stores and audits the keys used to encrypt data. In this case: KMS stores the keys and logs their use, and a key can be disabled to revoke access.

### Question 27 — C

Answer: Store the database credential in AWS Secrets Manager and rotate it. A managed secret store holds the credential and can rotate it on a schedule. The secret is held centrally and can be rotated on a schedule. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A managed secret store holds the credential and can rotate it on a schedule.
- **B:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: A managed secret store holds the credential and can rotate it on a schedule.
- **C:** Correct. The secret is held centrally and can be rotated on a schedule. In this case: A managed secret store holds the credential and can rotate it on a schedule.
- **D:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: A managed secret store holds the credential and can rotate it on a schedule.

### Question 28 — C

Answer: Use Amazon GuardDuty to detect suspicious activity. GuardDuty analyses account, network and DNS activity for signs of compromise. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **C:** Correct. In this case: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.

### Question 29 — D, E

Answers: Use Amazon GuardDuty to detect suspicious activity; Use AWS Security Hub to aggregate findings in one place. GuardDuty produces the findings, and Security Hub aggregates them across accounts. GuardDuty analyses account, network and DNS activity for signs of compromise. Security Hub collects findings from the security services and scores them against a standard. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Detective builds a behaviour graph that helps explain how a finding happened. Why the correct answer wins: GuardDuty produces the findings, and Security Hub aggregates them across accounts.
- **B:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: GuardDuty produces the findings, and Security Hub aggregates them across accounts.
- **C:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: GuardDuty produces the findings, and Security Hub aggregates them across accounts.
- **D:** Correct. GuardDuty analyses account, network and DNS activity for signs of compromise. In this case: GuardDuty produces the findings, and Security Hub aggregates them across accounts.
- **E:** Correct. Security Hub collects findings from the security services and scores them against a standard. In this case: GuardDuty produces the findings, and Security Hub aggregates them across accounts.

### Question 30 — B

Answer: Share the snapshot publicly so partners can download it. A public snapshot exposes the whole dataset to anyone who learns the identifier. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: A public snapshot exposes the whole dataset to anyone who learns the identifier.
- **B:** Correct. In this case: A public snapshot exposes the whole dataset to anyone who learns the identifier.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A public snapshot exposes the whole dataset to anyone who learns the identifier.
- **D:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A public snapshot exposes the whole dataset to anyone who learns the identifier.

### Question 31 — B

Answer: An Amazon S3 bucket policy that grants public read. A bucket policy that denies public grants keeps the data private even if someone tries to open it. A public bucket policy exposes every object in the bucket to anyone on the internet. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: A bucket policy that denies public grants keeps the data private even if someone tries to open it.
- **B:** Correct. A public bucket policy exposes every object in the bucket to anyone on the internet. In this case: A bucket policy that denies public grants keeps the data private even if someone tries to open it.
- **C:** Incorrect for this question. A public snapshot exposes the whole dataset to anyone who finds it. Why the correct answer wins: A bucket policy that denies public grants keeps the data private even if someone tries to open it.
- **D:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: A bucket policy that denies public grants keeps the data private even if someone tries to open it.

### Question 32 — C

Answer: Use AWS Config to record resource configuration changes. Config records resource configuration over time and evaluates it against rules. Config keeps a history of configuration and evaluates it against rules. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Config records resource configuration over time and evaluates it against rules.
- **B:** Incorrect for this question. Audit Manager assembles evidence against a chosen framework. Why the correct answer wins: Config records resource configuration over time and evaluates it against rules.
- **C:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: Config records resource configuration over time and evaluates it against rules.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Config records resource configuration over time and evaluates it against rules.

### Question 33 — A, C

Answers: Use AWS CloudTrail to record API activity; Download the compliance reports from AWS Artifact. CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports. CloudTrail logs who called which API, when and from where. Artifact provides AWS audit reports and agreements on demand. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Artifact provides AWS audit reports and agreements on demand. In this case: CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports.
- **B:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports.
- **C:** Correct. CloudTrail logs who called which API, when and from where. In this case: CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports.
- **D:** Incorrect for this question. Audit Manager assembles evidence against a chosen framework. Why the correct answer wins: CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports.
- **E:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudTrail records data and API access by identity, and Artifact provides the AWS certification reports.

### Question 34 — A

Answer: The customer is responsible for the data it stores in AWS. Retention and deletion of the data are customer decisions in every service model. Classification, access and protection of the data remain with the customer. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Classification, access and protection of the data remain with the customer. In this case: Retention and deletion of the data are customer decisions in every service model.
- **B:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Retention and deletion of the data are customer decisions in every service model.
- **C:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: Retention and deletion of the data are customer decisions in every service model.
- **D:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Retention and deletion of the data are customer decisions in every service model.

### Question 35 — B

Answer: Apply a service control policy in AWS Organizations. A service control policy caps what accounts may do, so it can forbid the service without granting anything itself. An SCP sets the maximum permissions available to the accounts under it. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A service control policy caps what accounts may do, so it can forbid the service without granting anything itself.
- **B:** Correct. An SCP sets the maximum permissions available to the accounts under it. In this case: A service control policy caps what accounts may do, so it can forbid the service without granting anything itself.
- **C:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: A service control policy caps what accounts may do, so it can forbid the service without granting anything itself.
- **D:** Incorrect for this question. An SCP only limits permissions; it never grants them. Why the correct answer wins: A service control policy caps what accounts may do, so it can forbid the service without granting anything itself.

### Question 36 — D

Answer: AWS Lambda. Lambda runs the validation per submission and keeps nothing running between them. Run code on an event without provisioning or managing a server. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Lambda runs the validation per submission and keeps nothing running between them.
- **B:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: Lambda runs the validation per submission and keeps nothing running between them.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lambda runs the validation per submission and keeps nothing running between them.
- **D:** Correct. Run code on an event without provisioning or managing a server. In this case: Lambda runs the validation per submission and keeps nothing running between them.

### Question 37 — B

Answer: AWS Batch. A managed batch scheduler queues the jobs and provisions capacity for each run. Queue and run batch computing jobs without managing the scheduler infrastructure. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each run.
- **B:** Correct. Queue and run batch computing jobs without managing the scheduler infrastructure. In this case: A managed batch scheduler queues the jobs and provisions capacity for each run.
- **C:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each run.
- **D:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each run.

### Question 38 — D

Answer: Amazon S3 Intelligent-Tiering. Intelligent-Tiering moves objects between access tiers as usage changes. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Object storage for frequently accessed data with high durability and availability. Why the correct answer wins: Intelligent-Tiering moves objects between access tiers as usage changes.
- **B:** Incorrect for this question. Object storage for data that is accessed less often but must be available immediately. Why the correct answer wins: Intelligent-Tiering moves objects between access tiers as usage changes.
- **C:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: Intelligent-Tiering moves objects between access tiers as usage changes.
- **D:** Correct. In this case: Intelligent-Tiering moves objects between access tiers as usage changes.

### Question 39 — A, D

Answers: Amazon S3 Standard-IA; Amazon FSx file systems. Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system. Object storage for data that is accessed less often but must be available immediately. Managed file systems for Windows or high-performance workloads. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Object storage for data that is accessed less often but must be available immediately. In this case: Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system.
- **B:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system.
- **C:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system.
- **D:** Correct. Managed file systems for Windows or high-performance workloads. In this case: Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system.
- **E:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: Standard-IA keeps rarely read objects instantly available, and FSx provides the managed Windows file system.

### Question 40 — D

Answer: Amazon Neptune. A graph database is built for highly connected data and multi-hop queries. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: A graph database is built for highly connected data and multi-hop queries.
- **B:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: A graph database is built for highly connected data and multi-hop queries.
- **C:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: A graph database is built for highly connected data and multi-hop queries.
- **D:** Correct. In this case: A graph database is built for highly connected data and multi-hop queries.

### Question 41 — B

Answer: Amazon RDS. Amazon RDS manages the engine, backups and point-in-time restore. A managed relational database where AWS handles patching, backups and failover options. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Amazon RDS manages the engine, backups and point-in-time restore.
- **B:** Correct. A managed relational database where AWS handles patching, backups and failover options. In this case: Amazon RDS manages the engine, backups and point-in-time restore.
- **C:** Incorrect for this question. A managed in-memory cache for sub-millisecond reads of hot data. Why the correct answer wins: Amazon RDS manages the engine, backups and point-in-time restore.
- **D:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: Amazon RDS manages the engine, backups and point-in-time restore.

### Question 42 — A

Answer: Amazon VPC. A VPC is a logically isolated network in which the customer defines the subnets. A logically isolated virtual network in which the customer places its resources. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A logically isolated virtual network in which the customer places its resources. In this case: A VPC is a logically isolated network in which the customer defines the subnets.
- **B:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: A VPC is a logically isolated network in which the customer defines the subnets.
- **C:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: A VPC is a logically isolated network in which the customer defines the subnets.
- **D:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: A VPC is a logically isolated network in which the customer defines the subnets.

### Question 43 — C, D

Answers: Amazon CloudFront; Amazon Route 53. CloudFront caches the assets at edge locations, and Route 53 serves the DNS records. A content delivery network that caches content at edge locations near users. A managed DNS service that also supports health checks and routing policies. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **B:** Incorrect for this question. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **C:** Correct. A managed DNS service that also supports health checks and routing policies. In this case: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **D:** Correct. A content delivery network that caches content at edge locations near users. In this case: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **E:** Incorrect for this question. A managed front door for APIs with throttling, authorisation and usage plans. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.

### Question 44 — A

Answer: AWS Control Tower. Control Tower establishes the landing zone and applies baseline controls to new accounts. A landing zone that applies baseline controls across an organisation. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A landing zone that applies baseline controls across an organisation. In this case: Control Tower establishes the landing zone and applies baseline controls to new accounts.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Control Tower establishes the landing zone and applies baseline controls to new accounts.
- **C:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: Control Tower establishes the landing zone and applies baseline controls to new accounts.
- **D:** Incorrect for this question. An SCP sets the maximum permissions available to the accounts under it. Why the correct answer wins: Control Tower establishes the landing zone and applies baseline controls to new accounts.

### Question 45 — B

Answer: AWS Trusted Advisor. Trusted Advisor checks the account against cost, security, limit and resilience best practices. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **B:** Correct. In this case: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **C:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **D:** Incorrect for this question. Service health and event notifications that affect the account. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.

### Question 46 — D

Answer: AWS Step Functions. Step Functions coordinates the ordered steps, retries and branching in one state machine. A state machine that coordinates multi-step workflows with retries and branching. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: Step Functions coordinates the ordered steps, retries and branching in one state machine.
- **B:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: Step Functions coordinates the ordered steps, retries and branching in one state machine.
- **C:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: Step Functions coordinates the ordered steps, retries and branching in one state machine.
- **D:** Correct. A state machine that coordinates multi-step workflows with retries and branching. In this case: Step Functions coordinates the ordered steps, retries and branching in one state machine.

### Question 47 — A, E

Answers: Amazon SNS; Amazon Kinesis. SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream. A pub/sub topic that fans a message out to many subscribers. Streaming data ingestion and processing for continuous records. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Streaming data ingestion and processing for continuous records. In this case: SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream.
- **B:** Incorrect for this question. A managed message broker for existing protocols such as AMQP or MQTT. Why the correct answer wins: SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream.
- **C:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream.
- **D:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream.
- **E:** Correct. A pub/sub topic that fans a message out to many subscribers. In this case: SNS fans the alert out to subscribers, and Kinesis ingests the continuous transaction stream.

### Question 48 — C

Answer: Amazon QuickSight. QuickSight provides managed dashboards and reports over that data. A managed business intelligence service for dashboards and reports. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: QuickSight provides managed dashboards and reports over that data.
- **B:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: QuickSight provides managed dashboards and reports over that data.
- **C:** Correct. A managed business intelligence service for dashboards and reports. In this case: QuickSight provides managed dashboards and reports over that data.
- **D:** Incorrect for this question. Build, train and deploy machine learning models through a managed platform. Why the correct answer wins: QuickSight provides managed dashboards and reports over that data.

### Question 49 — C

Answer: Amazon Athena. Athena queries the objects in place with SQL and no infrastructure to manage. Query data in Amazon S3 with SQL and no infrastructure to manage. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to manage.
- **B:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to manage.
- **C:** Correct. Query data in Amazon S3 with SQL and no infrastructure to manage. In this case: Athena queries the objects in place with SQL and no infrastructure to manage.
- **D:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to manage.

### Question 50 — B

Answer: AWS CodeDeploy. CodeDeploy manages the traffic shift and can roll back when the deployment health check fails. Automates the deployment of application revisions to instances and services. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: CodeDeploy manages the traffic shift and can roll back when the deployment health check fails.
- **B:** Correct. Automates the deployment of application revisions to instances and services. In this case: CodeDeploy manages the traffic shift and can roll back when the deployment health check fails.
- **C:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: CodeDeploy manages the traffic shift and can roll back when the deployment health check fails.
- **D:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CodeDeploy manages the traffic shift and can roll back when the deployment health check fails.

### Question 51 — D

Answer: AWS X-Ray. X-Ray traces a request across the services and shows where the time is spent. Traces requests through a distributed application to find where time is spent. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.
- **B:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.
- **C:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.
- **D:** Correct. Traces requests through a distributed application to find where time is spent. In this case: X-Ray traces a request across the services and shows where the time is spent.

### Question 52 — C

Answer: AWS CloudFormation. CloudFormation creates and updates resources from a template, so the rebuild matches. Infrastructure defined as a template and created or updated as a stack. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: CloudFormation creates and updates resources from a template, so the rebuild matches.
- **B:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: CloudFormation creates and updates resources from a template, so the rebuild matches.
- **C:** Correct. Infrastructure defined as a template and created or updated as a stack. In this case: CloudFormation creates and updates resources from a template, so the rebuild matches.
- **D:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: CloudFormation creates and updates resources from a template, so the rebuild matches.

### Question 53 — A

Answer: AWS App Runner. App Runner runs the container and manages the capacity and scaling behind it. Run a containerised web service without choosing or managing the underlying capacity. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Run a containerised web service without choosing or managing the underlying capacity. In this case: App Runner runs the container and manages the capacity and scaling behind it.
- **B:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **C:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **D:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.

### Question 54 — C

Answer: Use AWS CloudTrail to record API activity. CloudTrail records the API call, the caller and the source of the request. CloudTrail logs who called which API, when and from where. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **B:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **C:** Correct. CloudTrail logs who called which API, when and from where. In this case: CloudTrail records the API call, the caller and the source of the request.
- **D:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.

### Question 55 — B, C

Answers: Amazon CloudWatch; Use AWS Config to record resource configuration changes. CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history. Metrics, logs and alarms for the resources and applications in the account. Config keeps a history of configuration and evaluates it against rules. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history.
- **B:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history.
- **C:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history.
- **D:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history.
- **E:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch holds the metric and the alarm, and Config keeps the resource configuration history.

### Question 56 — A

Answer: AWS PrivateLink. PrivateLink provides a private endpoint inside the VPC for the provider service. Private connectivity to a service through an endpoint inside the VPC. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Private connectivity to a service through an endpoint inside the VPC. In this case: PrivateLink provides a private endpoint inside the VPC for the provider service.
- **B:** Incorrect for this question. A central router that connects many VPCs and on-premises networks. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the provider service.
- **C:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the provider service.
- **D:** Incorrect for this question. A logically isolated virtual network in which the customer places its resources. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the provider service.

### Question 57 — C

Answer: AWS Site-to-Site VPN. A Site-to-Site VPN builds an encrypted tunnel over the internet and can be created quickly. An encrypted tunnel over the internet between a customer network and a VPC. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be created quickly.
- **B:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be created quickly.
- **C:** Correct. An encrypted tunnel over the internet between a customer network and a VPC. In this case: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be created quickly.
- **D:** Incorrect for this question. Private connectivity to a service through an endpoint inside the VPC. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be created quickly.

### Question 58 — C

Answer: Savings Plans. Savings Plans commit to a spend per hour and apply across eligible compute usage. A commitment to a spend level per hour in exchange for a discount across eligible usage. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **B:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **C:** Correct. A commitment to a spend level per hour in exchange for a discount across eligible usage. In this case: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **D:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.

### Question 59 — D

Answer: Dedicated Hosts. Dedicated Hosts give the customer a physical server no other account uses. A physical server dedicated to one customer, used for licensing or compliance requirements. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: Dedicated Hosts give the customer a physical server no other account uses.
- **B:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Dedicated Hosts give the customer a physical server no other account uses.
- **C:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: Dedicated Hosts give the customer a physical server no other account uses.
- **D:** Correct. A physical server dedicated to one customer, used for licensing or compliance requirements. In this case: Dedicated Hosts give the customer a physical server no other account uses.

### Question 60 — A

Answer: AWS Cost Explorer. Cost Explorer visualises past spend by service and forecasts what is coming. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Cost Explorer visualises past spend by service and forecasts what is coming.
- **B:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Cost Explorer visualises past spend by service and forecasts what is coming.
- **C:** Incorrect for this question. Estimate the cost of a planned architecture before it is built. Why the correct answer wins: Cost Explorer visualises past spend by service and forecasts what is coming.
- **D:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: Cost Explorer visualises past spend by service and forecasts what is coming.

### Question 61 — B, C

Answers: AWS Pricing Calculator; Cost Anomaly Detection. The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation. Estimate the cost of a planned architecture before it is built. Machine learning alerts on spending that deviates from the expected pattern. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation.
- **B:** Correct. Machine learning alerts on spending that deviates from the expected pattern. In this case: The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation.
- **C:** Correct. Estimate the cost of a planned architecture before it is built. In this case: The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation.
- **D:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation.
- **E:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: The Pricing Calculator estimates the planned migration, and Cost Anomaly Detection warns about the deviation.

### Question 62 — A

Answer: Consolidated billing in AWS Organizations. Consolidated billing puts the accounts on one invoice and pools their usage for discounts. One bill for all accounts, with usage aggregated so volume discounts are shared. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. One bill for all accounts, with usage aggregated so volume discounts are shared. In this case: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **B:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **C:** Incorrect for this question. Separate accounts do not pool usage, so each misses the discounts the total would earn. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **D:** Incorrect for this question. Activated tags split the one bill by department, project or cost centre. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.

### Question 63 — A

Answer: AWS Basic Support. Basic Support covers account and billing questions at no charge. Account and billing support with documentation and health checks, at no charge. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Account and billing support with documentation and health checks, at no charge. In this case: Basic Support covers account and billing questions at no charge.
- **B:** Incorrect for this question. Mission-critical support with a designated technical account manager and the fastest response. Why the correct answer wins: Basic Support covers account and billing questions at no charge.
- **C:** Incorrect for this question. Production support with 24/7 access, faster response and Trusted Advisor checks. Why the correct answer wins: Basic Support covers account and billing questions at no charge.
- **D:** Incorrect for this question. Business-hours email support for development and test workloads. Why the correct answer wins: Basic Support covers account and billing questions at no charge.

### Question 64 — D

Answer: Engage an AWS Partner for the delivery work. The AWS Partner Network lists third-party firms with AWS-validated delivery skills. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The reference documentation states what a service does and how it is configured. Why the correct answer wins: The AWS Partner Network lists third-party firms with AWS-validated delivery skills.
- **B:** Incorrect for this question. A vetted reference architecture shortens design work for a common workload. Why the correct answer wins: The AWS Partner Network lists third-party firms with AWS-validated delivery skills.
- **C:** Incorrect for this question. The community knowledge base holds answers to common service and account questions. Why the correct answer wins: The AWS Partner Network lists third-party firms with AWS-validated delivery skills.
- **D:** Correct. In this case: The AWS Partner Network lists third-party firms with AWS-validated delivery skills.

### Question 65 — C

Answer: Volume discounts that grow with usage. Volume discounts lower the effective rate as aggregated usage rises. Aggregated usage across an organisation lowers the effective rate. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Volume discounts lower the effective rate as aggregated usage rises.
- **B:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: Volume discounts lower the effective rate as aggregated usage rises.
- **C:** Correct. Aggregated usage across an organisation lowers the effective rate. In this case: Volume discounts lower the effective rate as aggregated usage rises.
- **D:** Incorrect for this question. Limited monthly usage at no charge for eligible services on a new or qualifying account. Why the correct answer wins: Volume discounts lower the effective rate as aggregated usage rises.
