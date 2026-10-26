# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 2

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. A hospital patient portal is hammered when appointment slots open at eight each morning and is almost idle by nine. Which benefit of cloud computing does the portal need?

- A. A flat monthly fee that does not change with usage
- B. Global reach: deploy into multiple Regions quickly
- C. Buy servers up front and depreciate them
- D. Elasticity: scale capacity with demand

### 2. A clinic group of four IT staff currently spends most of its week racking servers and replacing disks. Which cloud benefit frees that time?

- A. Buy servers up front and depreciate them
- B. Stop spending on undifferentiated heavy lifting
- C. Keep ownership of the physical data centre
- D. Global reach: deploy into multiple Regions quickly

### 3. A dental group is replacing a five-year server purchase with a monthly AWS bill and asks how the new spending pattern is described. Which term applies?

- A. Buy servers up front and depreciate them
- B. Pay only for what is consumed each month
- C. A flat monthly fee that does not change with usage
- D. Keep ownership of the physical data centre

### 4. A hospital network lets each department buy its own AWS capacity, yet the combined monthly usage earns a lower effective rate than any department alone would get. Which economic effect is this?

- A. Volume discounts that grow with usage
- B. A flat monthly fee that does not change with usage
- C. Pay-as-you-go pricing
- D. Buy servers up front and depreciate them

### 5. Every release of a patient records system forces a full rebuild and regression test of the whole application. Which design principle would reduce that cost?

- A. Scale the single monolith vertically only
- B. Deploy across multiple Availability Zones
- C. Direct synchronous calls between every tier
- D. Break the application into small independent services

### 6. A clinical team wants a throwaway copy of the test environment for each candidate release, created and deleted the same day. Which cloud characteristic makes this practical?

- A. Agility: provision resources in minutes
- B. Buy servers up front and depreciate them
- C. A flat monthly fee that does not change with usage
- D. Scale the single monolith vertically only

### 7. A design review must show that patient data is protected and that only approved staff can reach it. Which Well-Architected pillar answers that question?

- A. Cost optimization pillar
- B. Sustainability pillar
- C. Performance efficiency pillar
- D. Security pillar

### 8. A review must cover how efficiently resources are used as demand grows and how the workload's environmental impact is reduced. Which two pillars apply? Select two.

- A. Cost optimization pillar
- B. Sustainability pillar
- C. Reliability pillar
- D. Security pillar
- E. Performance efficiency pillar

### 9. An insurer wants its cloud roadmap tied to measurable claims-handling outcomes that the board already tracks. Which Cloud Adoption Framework perspective does that?

- A. Operations perspective of the AWS Cloud Adoption Framework
- B. Platform perspective of the AWS Cloud Adoption Framework
- C. People perspective of the AWS Cloud Adoption Framework
- D. Business perspective of the AWS Cloud Adoption Framework

### 10. A health provider must show that its cloud programme meets its regulatory and patient-privacy objectives. Which Cloud Adoption Framework perspective covers this?

- A. Operations perspective of the AWS Cloud Adoption Framework
- B. Security perspective of the AWS Cloud Adoption Framework
- C. Business perspective of the AWS Cloud Adoption Framework
- D. Platform perspective of the AWS Cloud Adoption Framework

### 11. A hospital wants its claims application in AWS within a month with no code change, even though it will gain few cloud benefits. Which strategy is this?

- A. Retire: switch the workload off
- B. Repurchase: move to a different product
- C. Rehost: move the application as it is
- D. Refactor: redesign the application for cloud architecture

### 12. A scheduling system will be rewritten to use managed services so it can scale through seasonal demand. Which strategy is this?

- A. Rehost: move the application as it is
- B. Retain: keep the workload where it is
- C. Refactor: redesign the application for cloud architecture
- D. Relocate: move the platform to a cloud-native equivalent

### 13. A hospital group must keep patient records inside one country and still serve two cities in it with low latency. Which infrastructure concept is it choosing between?

- A. Regions and Availability Zones
- B. AWS Outposts for on-premises capacity
- C. Edge locations for content delivery
- D. AWS Wavelength for carrier networks

### 14. A clinic has backups but nobody can say how long a restore takes or how much data would be lost. What is missing?

- A. Direct synchronous calls between every tier
- B. Scale the single monolith vertically only
- C. Define a recovery objective and test the recovery path
- D. Place everything in one Availability Zone

### 15. A laboratory system must keep reporting results when one Availability Zone is lost, and the team must be able to state how fast it can recover from a full regional loss. Which two choices fit? Select two.

- A. Scale the single monolith vertically only
- B. Serverless compute for intermittent work
- C. Deploy across multiple Availability Zones
- D. Place everything in one Availability Zone
- E. Define a recovery objective and test the recovery path

### 16. A hospital stores patient records in Amazon S3 and asks who decides how those records are classified, encrypted and accessed. Under the shared responsibility model, who?

- A. AWS is responsible for patching a managed service such as Amazon S3
- B. AWS is responsible for the physical facilities and hardware
- C. The customer is responsible for the data-centre building
- D. The customer is responsible for the data it stores in AWS

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. A billing analyst must be allowed to read one bucket and start one report job, and nothing else. What should be attached to the identity?

- A. Share the root credentials with the operations team
- B. Give every engineer administrator access for convenience
- C. Attach a JSON policy that allows only the required actions
- D. Put the users in a group and attach the policy to the group

### 18. Clinicians sign in to AWS from shared workstations in wards where passwords are easy to observe. Which control most reduces the risk?

- A. Require multi-factor authentication
- B. Rotate access keys on a schedule
- C. Grant only the permissions the task needs
- D. Put the users in a group and attach the policy to the group

### 19. A new administrator proposes doing all daily work as the root user because it never hits a permission error. Which practice does the proposal represent?

- A. Use the root user for daily administration
- B. Grant only the permissions the task needs
- C. Enable MFA and delete the root access keys
- D. Require multi-factor authentication

### 20. An attacker reached the management console with a stolen password that had no second factor. Which control would have blocked that sign-in?

- A. Rotate access keys on a schedule
- B. Enable MFA and delete the root access keys
- C. Attach a JSON policy that allows only the required actions
- D. Require multi-factor authentication

### 21. A security team in one account must read findings in a second account without any long-term key being shared. What should be created?

- A. Federate the company directory into AWS
- B. Create an IAM user with long-lived credentials
- C. Create an IAM role and let the workload assume it
- D. Use Amazon Cognito for customer sign-in

### 22. A patient-facing mobile app needs sign-up, sign-in and token handling for millions of consumers. Which service fits?

- A. Put the users in a group and attach the policy to the group
- B. Use IAM Identity Center for workforce sign-in
- C. Create an IAM user with long-lived credentials
- D. Use Amazon Cognito for customer sign-in

### 23. A specific external address range is attacking a subnet and must be blocked before it reaches any instance in it. What should be applied?

- A. Open every port to the internet and rely on the application
- B. Use a network ACL as a stateless subnet filter
- C. Use AWS WAF to block web attack patterns
- D. Use a security group as a stateful instance firewall

### 24. Traffic entering a VPC must be inspected for intrusion patterns, and a public form must reject injection attempts in HTTP requests. Which two services apply? Select two.

- A. Use AWS Network Firewall for VPC-level inspection
- B. Use AWS KMS to create and control encryption keys
- C. Use AWS WAF to block web attack patterns
- D. Use AWS Shield for DDoS protection
- E. Use a network ACL as a stateless subnet filter

### 25. Records must be encrypted at rest with every key use logged and with the ability to disable a key centrally. Which service provides that?

- A. Encrypt data in transit with TLS
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Use Amazon Macie to find sensitive data in Amazon S3
- D. Use AWS KMS to create and control encryption keys

### 26. A team wants objects encrypted at rest immediately, with no key policy of its own to design or operate. What fits?

- A. Encrypt data in transit with TLS
- B. Use AWS KMS to create and control encryption keys
- C. Use a customer managed key for the required control
- D. Rely on server-side encryption with Amazon S3 managed keys

### 27. The certificate on a patient portal keeps expiring because someone renews it by hand each year. Which service removes that manual step?

- A. Use AWS Certificate Manager for TLS certificates
- B. Use AWS KMS to create and control encryption keys
- C. Attach a JSON policy that allows only the required actions
- D. Store the database credential in AWS Secrets Manager and rotate it

### 28. A security lead wants findings from several AWS detection services and many accounts scored in one place. Which service fits?

- A. Use AWS Security Hub to aggregate findings in one place
- B. Use AWS CloudTrail to record API activity
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use Amazon Inspector to scan workloads for vulnerabilities

### 29. A team must detect that an account is being used by an intruder and then understand the sequence of activity behind that finding. Which two services apply? Select two.

- A. Use Amazon Detective to investigate a finding
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use Amazon Inspector to scan workloads for vulnerabilities
- D. Use Amazon GuardDuty to detect suspicious activity
- E. Use AWS CloudTrail to record API activity

### 30. Before choosing encryption and retention rules for a new data lake, the team must decide which datasets are most sensitive. What should be done first?

- A. An Amazon S3 bucket policy that grants public read
- B. Set an S3 lifecycle rule to expire old objects
- C. AWS Backup
- D. Classify the data and tag each store by sensitivity

### 31. Objects in a logging bucket must be deleted automatically after 400 days with no manual cleanup. What should be configured?

- A. An Amazon S3 bucket policy that grants public read
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Set an S3 lifecycle rule to expire old objects
- D. AWS Backup

### 32. An internal audit needs evidence assembled against a chosen control framework across several AWS accounts. Which service fits?

- A. Use AWS CloudTrail to record API activity
- B. Use AWS Config to record resource configuration changes
- C. Use AWS Audit Manager to collect evidence for an audit
- D. Download the compliance reports from AWS Artifact

### 33. A compliance team needs a quick check of the account for insecure settings and needs to download AWS audit reports for its own audit. Which two services fit? Select two.

- A. Use Amazon Macie to find sensitive data in Amazon S3
- B. Use Amazon Inspector to scan workloads for vulnerabilities
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Read the security checks in AWS Trusted Advisor
- E. Download the compliance reports from AWS Artifact

### 34. AWS patches the managed service, yet the customer must still track which patches change what it has configured. Which part of the shared responsibility model does that describe?

- A. AWS is responsible for encrypting customer data by default
- B. The customer is responsible for the data-centre building
- C. Some controls are shared, such as patch awareness
- D. AWS is responsible for the physical facilities and hardware

### 35. A group wants a preconfigured landing zone with baseline controls applied to every new account automatically. Which service fits?

- A. AWS Service Catalog
- B. Attach a JSON policy that allows only the required actions
- C. Apply a service control policy in AWS Organizations
- D. AWS Control Tower

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. An imaging service is already packaged as containers, and the team wants managed orchestration without operating the hosts itself. Which compute option fits?

- A. Amazon EC2 instances
- B. Amazon ECS or Amazon EKS with AWS Fargate
- C. AWS Lambda
- D. Amazon Lightsail

### 37. Genome analysis jobs arrive in bursts, queue for hours and each needs a large machine for a short time. Which service fits?

- A. Amazon EC2 instances
- B. AWS Batch
- C. AWS Lambda
- D. AWS App Runner

### 38. A database instance needs a block device that holds its data files and survives an instance stop and start. Which storage fits?

- A. Amazon FSx file systems
- B. Amazon EBS volumes
- C. Amazon S3 Standard
- D. Amazon EFS file system

### 39. A clinic wants its active files cached locally while a copy lives in AWS, and must also seed a 200 TB archive that would take a year to upload. Which two services fit? Select two.

- A. AWS Storage Gateway
- B. Amazon EFS file system
- C. AWS Backup
- D. Amazon EBS volumes
- E. AWS Snowball devices

### 40. A team wants a MySQL-compatible managed database with higher throughput and a managed failover replica. Which service fits?

- A. Amazon RDS
- B. Amazon Aurora
- C. Amazon DynamoDB
- D. Amazon Redshift

### 41. The same reference tables are read thousands of times a second and the database is struggling. Which service should sit in front of it?

- A. Amazon ElastiCache
- B. Amazon Redshift
- C. Amazon RDS
- D. Amazon Neptune

### 42. Requests must be spread across instances in two Availability Zones and stop being sent to a failed one. Which service fits?

- A. Elastic Load Balancing
- B. Amazon Route 53
- C. Amazon CloudFront
- D. Amazon API Gateway

### 43. A records tier needs its own isolated network, and a partner service must be reached privately without crossing the public internet. Which two services fit? Select two.

- A. Amazon VPC
- B. AWS PrivateLink
- C. AWS Direct Connect
- D. Amazon Route 53
- E. Amazon CloudFront

### 44. A fleet of servers must receive operating system patches on a schedule and accept remote commands without inbound access. Which service fits?

- A. AWS Service Catalog
- B. AWS Systems Manager
- C. AWS CloudFormation
- D. Amazon CloudWatch

### 45. A new account owner wants a quick list of idle resources and insecure settings before the first bill arrives. Which service fits?

- A. AWS Trusted Advisor
- B. Use AWS Config to record resource configuration changes
- C. Use AWS CloudTrail to record API activity
- D. AWS Health Dashboard

### 46. A workflow must start whenever an AWS service reports that a resource changed state, with routing decided by rules. Which service fits?

- A. Amazon SQS
- B. Amazon EventBridge
- C. Amazon SNS
- D. AWS Step Functions

### 47. Continuous sensor readings must be ingested in order, and a slow downstream consumer must not lose records during a burst. Which two services fit? Select two.

- A. Amazon MQ
- B. Amazon EventBridge
- C. Amazon SNS
- D. Amazon Kinesis
- E. Amazon SQS

### 48. Executives want scheduled dashboards over data already in AWS, with no servers or clusters to run. Which service fits?

- A. Amazon QuickSight
- B. Amazon Redshift
- C. Amazon Athena
- D. Amazon SageMaker

### 49. A data science team must train, tune and deploy its own models through a managed platform. Which service fits?

- A. AWS Glue
- B. Amazon EMR
- C. Amazon Bedrock
- D. Amazon SageMaker

### 50. A release must move through build, test and deploy stages in a defined order with approvals between them. Which service coordinates that flow?

- A. AWS CodePipeline
- B. AWS CodeBuild
- C. AWS CodeDeploy
- D. AWS CloudFormation

### 51. A new application version must reach a small share of traffic first and roll back automatically if errors rise. Which service fits?

- A. AWS CodeDeploy
- B. AWS CodeBuild
- C. AWS CodePipeline
- D. AWS X-Ray

### 52. Teams should launch only approved, preconfigured products themselves, without asking the platform team each time. Which service fits?

- A. AWS CloudFormation
- B. AWS Systems Manager
- C. AWS Service Catalog
- D. AWS Control Tower

### 53. A two-person clinic wants a simple bundle of compute, storage and networking at a predictable monthly price with little configuration. Which service fits?

- A. AWS App Runner
- B. Amazon EC2 instances
- C. Amazon Lightsail
- D. AWS Elastic Beanstalk

### 54. An operations lead wants to know when an AWS service event affects the account, separate from the account's own metrics. Which service fits?

- A. AWS Trusted Advisor
- B. Use AWS CloudTrail to record API activity
- C. Amazon CloudWatch
- D. AWS Health Dashboard

### 55. An application team needs alarms on latency and a trace that shows which of several services took most of the time in a slow request. Which two services fit? Select two.

- A. Use AWS CloudTrail to record API activity
- B. AWS X-Ray
- C. Use AWS Config to record resource configuration changes
- D. Use Amazon Inspector to scan workloads for vulnerabilities
- E. Amazon CloudWatch

### 56. A hospital data centre needs a private dedicated connection into AWS with consistent latency for nightly imaging transfers. Which service fits?

- A. AWS Direct Connect
- B. Amazon CloudFront
- C. AWS Transit Gateway
- D. AWS Site-to-Site VPN

### 57. A temporary clinic must be connected to its VPC within days over the public internet with encryption. Which service fits?

- A. AWS Direct Connect
- B. AWS Site-to-Site VPN
- C. AWS PrivateLink
- D. AWS Global Accelerator

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. A development team runs short experiments of unpredictable length and does not want any commitment. Which option fits?

- A. Reserved Instances
- B. On-Demand Instances
- C. Dedicated Hosts
- D. Spot Instances

### 59. A software licence is tied to physical sockets and requires the workload to have its own physical server. Which option fits?

- A. Spot Instances
- B. Savings Plans
- C. Dedicated Hosts
- D. On-Demand Instances

### 60. Finance wants to be warned automatically when spend departs from its normal pattern, even if no fixed limit is crossed. Which tool fits?

- A. AWS Cost and Usage Report
- B. Cost Anomaly Detection
- C. AWS Budgets
- D. AWS Cost Explorer

### 61. A finance team needs the most granular billing dataset for its own analysis and an alert when a project exceeds its monthly allowance. Which two tools fit? Select two.

- A. AWS Budgets
- B. AWS Pricing Calculator
- C. Wait for the monthly invoice and reconcile it afterwards
- D. AWS Cost and Usage Report
- E. AWS Cost Explorer

### 62. What happens when related accounts each keep their own bill instead of joining one organisation bill?

- A. AWS Cost and Usage Report
- B. The AWS Free Tier allowances
- C. Keep a separate bill and separate discounts per account
- D. Consolidated billing in AWS Organizations

### 63. A bank needs a named technical advisor and the fastest response for mission-critical workloads. Which plan fits?

- A. AWS Developer Support
- B. AWS Business Support
- C. AWS Enterprise Support
- D. AWS Basic Support

### 64. An engineer has a narrow question about a service limit that others have almost certainly hit before. Where should the answer be sought first?

- A. Engage an AWS Partner for the delivery work
- B. Search AWS re:Post for an answered question
- C. Read the AWS documentation and service user guides
- D. Start from an AWS Solutions Library reference deployment

### 65. A company wants a discount in exchange for committing to an hourly spend, and wants the discount to apply across compute and machine learning usage. Which option fits?

- A. Spot Instances
- B. The AWS Free Tier allowances
- C. Savings Plans
- D. Reserved Instances

---

## Answer key and explanations

### Question 1 — D

Answer: Elasticity: scale capacity with demand. Capacity that follows the morning peak removes the need for servers sized for one hour of demand. Capacity is added and removed as demand changes, so the company pays only for what it uses. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Capacity that follows the morning peak removes the need for servers sized for one hour of demand.
- **B:** Incorrect for this question. A global infrastructure lets a company put workloads near its users without building facilities. Why the correct answer wins: Capacity that follows the morning peak removes the need for servers sized for one hour of demand.
- **C:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Capacity that follows the morning peak removes the need for servers sized for one hour of demand.
- **D:** Correct. Capacity is added and removed as demand changes, so the company pays only for what it uses. In this case: Capacity that follows the morning peak removes the need for servers sized for one hour of demand.

### Question 2 — B

Answer: Stop spending on undifferentiated heavy lifting. AWS operates the facilities and hardware, so a small team can work on services instead of equipment. AWS operates the facilities, hardware and managed platforms so the team can focus on its product. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: AWS operates the facilities and hardware, so a small team can work on services instead of equipment.
- **B:** Correct. AWS operates the facilities, hardware and managed platforms so the team can focus on its product. In this case: AWS operates the facilities and hardware, so a small team can work on services instead of equipment.
- **C:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: AWS operates the facilities and hardware, so a small team can work on services instead of equipment.
- **D:** Incorrect for this question. A global infrastructure lets a company put workloads near its users without building facilities. Why the correct answer wins: AWS operates the facilities and hardware, so a small team can work on services instead of equipment.

### Question 3 — B

Answer: Pay only for what is consumed each month. Consumption-based spending appears as an operating expense instead of a depreciating asset. Costs follow usage, so the bill rises and falls with demand rather than with a purchase decision. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Consumption-based spending appears as an operating expense instead of a depreciating asset.
- **B:** Correct. Costs follow usage, so the bill rises and falls with demand rather than with a purchase decision. In this case: Consumption-based spending appears as an operating expense instead of a depreciating asset.
- **C:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Consumption-based spending appears as an operating expense instead of a depreciating asset.
- **D:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Consumption-based spending appears as an operating expense instead of a depreciating asset.

### Question 4 — A

Answer: Volume discounts that grow with usage. Aggregated usage across an organisation lowers the effective rate charged for the same services. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Aggregated usage across an organisation lowers the effective rate charged for the same services.
- **B:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Aggregated usage across an organisation lowers the effective rate charged for the same services.
- **C:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: Aggregated usage across an organisation lowers the effective rate charged for the same services.
- **D:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Aggregated usage across an organisation lowers the effective rate charged for the same services.

### Question 5 — D

Answer: Break the application into small independent services. Small independent services can be changed and deployed separately, so a release touches less of the system. Independent services can be deployed and scaled separately. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Small independent services can be changed and deployed separately, so a release touches less of the system.
- **B:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: Small independent services can be changed and deployed separately, so a release touches less of the system.
- **C:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Small independent services can be changed and deployed separately, so a release touches less of the system.
- **D:** Correct. Independent services can be deployed and scaled separately. In this case: Small independent services can be changed and deployed separately, so a release touches less of the system.

### Question 6 — A

Answer: Agility: provision resources in minutes. Environment provisioning in minutes turns a copy of the estate into a routine step rather than a purchase. New environments are created in minutes, which shortens the time to test an idea. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. New environments are created in minutes, which shortens the time to test an idea. In this case: Environment provisioning in minutes turns a copy of the estate into a routine step rather than a purchase.
- **B:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Environment provisioning in minutes turns a copy of the estate into a routine step rather than a purchase.
- **C:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Environment provisioning in minutes turns a copy of the estate into a routine step rather than a purchase.
- **D:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Environment provisioning in minutes turns a copy of the estate into a routine step rather than a purchase.

### Question 7 — D

Answer: Security pillar. The security pillar covers protecting data, systems and assets through identity and detective controls. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The security pillar covers protecting data, systems and assets through identity and detective controls.
- **B:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: The security pillar covers protecting data, systems and assets through identity and detective controls.
- **C:** Incorrect for this question. The pillar about using resources efficiently as demand and technology change. Why the correct answer wins: The security pillar covers protecting data, systems and assets through identity and detective controls.
- **D:** Correct. In this case: The security pillar covers protecting data, systems and assets through identity and detective controls.

### Question 8 — B, E

Answers: Performance efficiency pillar; Sustainability pillar. Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use. The pillar about using resources efficiently as demand and technology change. The pillar about minimising the environmental impact of running a workload. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use.
- **B:** Correct. The pillar about minimising the environmental impact of running a workload. In this case: Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use.
- **C:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use.
- **D:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use.
- **E:** Correct. The pillar about using resources efficiently as demand and technology change. In this case: Performance efficiency covers resource use as demand changes, and sustainability covers the environmental impact of that use.

### Question 9 — D

Answer: Business perspective of the AWS Cloud Adoption Framework. The business perspective connects cloud work to business outcomes and value. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.
- **B:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.
- **C:** Incorrect for this question. The perspective about skills, roles and organisational change. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.
- **D:** Correct. In this case: The business perspective connects cloud work to business outcomes and value.

### Question 10 — B

Answer: Security perspective of the AWS Cloud Adoption Framework. The security perspective covers meeting security and compliance objectives. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.
- **B:** Correct. In this case: The security perspective covers meeting security and compliance objectives.
- **C:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.
- **D:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.

### Question 11 — C

Answer: Rehost: move the application as it is. Rehost moves the application as it is, which is the fastest path and the least disruptive to the code. The application moves without code change, which is the fastest path but captures few cloud benefits. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The workload is no longer needed, so it is decommissioned instead of migrated. Why the correct answer wins: Rehost moves the application as it is, which is the fastest path and the least disruptive to the code.
- **B:** Incorrect for this question. The company replaces the application with a commercially available equivalent. Why the correct answer wins: Rehost moves the application as it is, which is the fastest path and the least disruptive to the code.
- **C:** Correct. The application moves without code change, which is the fastest path but captures few cloud benefits. In this case: Rehost moves the application as it is, which is the fastest path and the least disruptive to the code.
- **D:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Rehost moves the application as it is, which is the fastest path and the least disruptive to the code.

### Question 12 — C

Answer: Refactor: redesign the application for cloud architecture. Refactoring redesigns the application to take advantage of managed and elastic services. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Refactoring redesigns the application to take advantage of managed and elastic services.
- **B:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Refactoring redesigns the application to take advantage of managed and elastic services.
- **C:** Correct. In this case: Refactoring redesigns the application to take advantage of managed and elastic services.
- **D:** Incorrect for this question. The whole platform moves to a hosted equivalent without changing the application itself. Why the correct answer wins: Refactoring redesigns the application to take advantage of managed and elastic services.

### Question 13 — A

Answer: Regions and Availability Zones. A Region is the geographic unit that determines where data is stored and roughly how close it sits to users. A Region is a geographic area and each Availability Zone within it is an isolated group of data centres. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A Region is a geographic area and each Availability Zone within it is an isolated group of data centres. In this case: A Region is the geographic unit that determines where data is stored and roughly how close it sits to users.
- **B:** Incorrect for this question. A rack of AWS infrastructure installed in the customer facility and operated through AWS. Why the correct answer wins: A Region is the geographic unit that determines where data is stored and roughly how close it sits to users.
- **C:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: A Region is the geographic unit that determines where data is stored and roughly how close it sits to users.
- **D:** Incorrect for this question. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. Why the correct answer wins: A Region is the geographic unit that determines where data is stored and roughly how close it sits to users.

### Question 14 — C

Answer: Define a recovery objective and test the recovery path. Recovery time and recovery point objectives turn disaster recovery from an intention into a tested design. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Recovery time and recovery point objectives turn disaster recovery from an intention into a tested design.
- **B:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Recovery time and recovery point objectives turn disaster recovery from an intention into a tested design.
- **C:** Correct. In this case: Recovery time and recovery point objectives turn disaster recovery from an intention into a tested design.
- **D:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Recovery time and recovery point objectives turn disaster recovery from an intention into a tested design.

### Question 15 — C, E

Answers: Deploy across multiple Availability Zones; Define a recovery objective and test the recovery path. A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path. Two or more Zones give the workload a survivor when one Zone fails. A recovery time and recovery point objective turn disaster recovery from an intention into a design. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path.
- **B:** Incorrect for this question. No server is provisioned, and the service runs only when it is invoked. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path.
- **C:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path.
- **D:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path.
- **E:** Correct. A recovery time and recovery point objective turn disaster recovery from an intention into a design. In this case: A multi-Zone deployment survives a single Zone failure, and stated recovery objectives define the regional recovery path.

### Question 16 — D

Answer: The customer is responsible for the data it stores in AWS. The data itself and the choices about protecting it remain with the customer. Classification, access and protection of the data remain with the customer. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: The data itself and the choices about protecting it remain with the customer.
- **B:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: The data itself and the choices about protecting it remain with the customer.
- **C:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: The data itself and the choices about protecting it remain with the customer.
- **D:** Correct. Classification, access and protection of the data remain with the customer. In this case: The data itself and the choices about protecting it remain with the customer.

### Question 17 — C

Answer: Attach a JSON policy that allows only the required actions. A policy document names the exact actions and resources, which is how least privilege is expressed. A policy document states which actions are allowed on which resources. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: A policy document names the exact actions and resources, which is how least privilege is expressed.
- **B:** Incorrect for this question. Broad standing access means one mistaken action or stolen credential can change anything. Why the correct answer wins: A policy document names the exact actions and resources, which is how least privilege is expressed.
- **C:** Correct. A policy document states which actions are allowed on which resources. In this case: A policy document names the exact actions and resources, which is how least privilege is expressed.
- **D:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: A policy document names the exact actions and resources, which is how least privilege is expressed.

### Question 18 — A

Answer: Require multi-factor authentication. A second factor means an observed password is not enough to sign in. A second factor makes a stolen password insufficient on its own. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A second factor makes a stolen password insufficient on its own. In this case: A second factor means an observed password is not enough to sign in.
- **B:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: A second factor means an observed password is not enough to sign in.
- **C:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: A second factor means an observed password is not enough to sign in.
- **D:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: A second factor means an observed password is not enough to sign in.

### Question 19 — A

Answer: Use the root user for daily administration. Daily use of the root user is the practice to avoid, because no policy can limit what it can do. The root user cannot be restricted by policy, so daily use magnifies any mistake. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The root user cannot be restricted by policy, so daily use magnifies any mistake. In this case: Daily use of the root user is the practice to avoid, because no policy can limit what it can do.
- **B:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: Daily use of the root user is the practice to avoid, because no policy can limit what it can do.
- **C:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Daily use of the root user is the practice to avoid, because no policy can limit what it can do.
- **D:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Daily use of the root user is the practice to avoid, because no policy can limit what it can do.

### Question 20 — D

Answer: Require multi-factor authentication. Multi-factor authentication requires a second proof, so the stolen password alone fails. A second factor makes a stolen password insufficient on its own. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: Multi-factor authentication requires a second proof, so the stolen password alone fails.
- **B:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Multi-factor authentication requires a second proof, so the stolen password alone fails.
- **C:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: Multi-factor authentication requires a second proof, so the stolen password alone fails.
- **D:** Correct. A second factor makes a stolen password insufficient on its own. In this case: Multi-factor authentication requires a second proof, so the stolen password alone fails.

### Question 21 — C

Answer: Create an IAM role and let the workload assume it. A role in the target account can be assumed for temporary credentials, so nothing long-lived is passed around. A role hands out temporary credentials, so nothing long-lived is stored. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Existing corporate identities are used instead of a separate set of AWS credentials. Why the correct answer wins: A role in the target account can be assumed for temporary credentials, so nothing long-lived is passed around.
- **B:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: A role in the target account can be assumed for temporary credentials, so nothing long-lived is passed around.
- **C:** Correct. A role hands out temporary credentials, so nothing long-lived is stored. In this case: A role in the target account can be assumed for temporary credentials, so nothing long-lived is passed around.
- **D:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: A role in the target account can be assumed for temporary credentials, so nothing long-lived is passed around.

### Question 22 — D

Answer: Use Amazon Cognito for customer sign-in. Cognito manages customer identity, including sign-up, sign-in and tokens. Cognito handles sign-up, sign-in and tokens for an application end users. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: Cognito manages customer identity, including sign-up, sign-in and tokens.
- **B:** Incorrect for this question. Workforce users sign in once and receive permission sets for the accounts they use. Why the correct answer wins: Cognito manages customer identity, including sign-up, sign-in and tokens.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Cognito manages customer identity, including sign-up, sign-in and tokens.
- **D:** Correct. Cognito handles sign-up, sign-in and tokens for an application end users. In this case: Cognito manages customer identity, including sign-up, sign-in and tokens.

### Question 23 — B

Answer: Use a network ACL as a stateless subnet filter. A network ACL filters at the subnet boundary, so it stops the range before any instance sees it. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. An open perimeter exposes every service on the host, including ones nobody meant to publish. Why the correct answer wins: A network ACL filters at the subnet boundary, so it stops the range before any instance sees it.
- **B:** Correct. The ACL filters traffic at the subnet boundary and evaluates each direction independently. In this case: A network ACL filters at the subnet boundary, so it stops the range before any instance sees it.
- **C:** Incorrect for this question. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Why the correct answer wins: A network ACL filters at the subnet boundary, so it stops the range before any instance sees it.
- **D:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: A network ACL filters at the subnet boundary, so it stops the range before any instance sees it.

### Question 24 — A, C

Answers: Use AWS Network Firewall for VPC-level inspection; Use AWS WAF to block web attack patterns. Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves. A managed firewall inspects traffic entering and leaving the VPC. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed firewall inspects traffic entering and leaving the VPC. In this case: Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves.
- **B:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves.
- **C:** Correct. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. In this case: Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves.
- **D:** Incorrect for this question. Shield absorbs distributed denial-of-service traffic before it reaches the application. Why the correct answer wins: Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves.
- **E:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: Network Firewall inspects traffic at the VPC boundary, and WAF inspects the HTTP requests themselves.

### Question 25 — D

Answer: Use AWS KMS to create and control encryption keys. KMS creates, stores and audits the keys used to encrypt the data. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: KMS creates, stores and audits the keys used to encrypt the data.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: KMS creates, stores and audits the keys used to encrypt the data.
- **C:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: KMS creates, stores and audits the keys used to encrypt the data.
- **D:** Correct. In this case: KMS creates, stores and audits the keys used to encrypt the data.

### Question 26 — D

Answer: Rely on server-side encryption with Amazon S3 managed keys. Server-side encryption with S3 managed keys encrypts the objects without the team running any key infrastructure. S3 encrypts the object at rest with keys it manages on the customer behalf. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: Server-side encryption with S3 managed keys encrypts the objects without the team running any key infrastructure.
- **B:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Server-side encryption with S3 managed keys encrypts the objects without the team running any key infrastructure.
- **C:** Incorrect for this question. The customer controls the key policy and can revoke access by disabling the key. Why the correct answer wins: Server-side encryption with S3 managed keys encrypts the objects without the team running any key infrastructure.
- **D:** Correct. S3 encrypts the object at rest with keys it manages on the customer behalf. In this case: Server-side encryption with S3 managed keys encrypts the objects without the team running any key infrastructure.

### Question 27 — A

Answer: Use AWS Certificate Manager for TLS certificates. Certificate Manager issues and renews certificates and deploys them to integrated services. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Certificate Manager issues and renews certificates and deploys them to integrated services.
- **B:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Certificate Manager issues and renews certificates and deploys them to integrated services.
- **C:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: Certificate Manager issues and renews certificates and deploys them to integrated services.
- **D:** Incorrect for this question. The secret is held centrally and can be rotated on a schedule. Why the correct answer wins: Certificate Manager issues and renews certificates and deploys them to integrated services.

### Question 28 — A

Answer: Use AWS Security Hub to aggregate findings in one place. Security Hub aggregates findings and scores them against a standard. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Security Hub aggregates findings and scores them against a standard.
- **B:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Security Hub aggregates findings and scores them against a standard.
- **C:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Security Hub aggregates findings and scores them against a standard.
- **D:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Security Hub aggregates findings and scores them against a standard.

### Question 29 — A, D

Answers: Use Amazon GuardDuty to detect suspicious activity; Use Amazon Detective to investigate a finding. GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it. GuardDuty analyses account, network and DNS activity for signs of compromise. Detective builds a behaviour graph that helps explain how a finding happened. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Detective builds a behaviour graph that helps explain how a finding happened. In this case: GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it.
- **C:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it.
- **D:** Correct. GuardDuty analyses account, network and DNS activity for signs of compromise. In this case: GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it.
- **E:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: GuardDuty raises the finding and Detective builds the behaviour graph needed to investigate it.

### Question 30 — D

Answer: Classify the data and tag each store by sensitivity. A classification decides which controls and retention rules apply to each dataset. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.
- **B:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.
- **D:** Correct. In this case: A classification decides which controls and retention rules apply to each dataset.

### Question 31 — C

Answer: Set an S3 lifecycle rule to expire old objects. A lifecycle rule moves or deletes objects automatically as they age. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A lifecycle rule moves or deletes objects automatically as they age.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A lifecycle rule moves or deletes objects automatically as they age.
- **C:** Correct. In this case: A lifecycle rule moves or deletes objects automatically as they age.
- **D:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A lifecycle rule moves or deletes objects automatically as they age.

### Question 32 — C

Answer: Use AWS Audit Manager to collect evidence for an audit. Audit Manager assembles evidence against a framework and keeps it ready for review. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Audit Manager assembles evidence against a framework and keeps it ready for review.
- **B:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Audit Manager assembles evidence against a framework and keeps it ready for review.
- **C:** Correct. In this case: Audit Manager assembles evidence against a framework and keeps it ready for review.
- **D:** Incorrect for this question. Artifact provides AWS audit reports and agreements on demand. Why the correct answer wins: Audit Manager assembles evidence against a framework and keeps it ready for review.

### Question 33 — D, E

Answers: Read the security checks in AWS Trusted Advisor; Download the compliance reports from AWS Artifact. Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports. Trusted Advisor inspects the account and reports insecure or wasteful settings. Artifact provides AWS audit reports and agreements on demand. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports.
- **B:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports.
- **C:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports.
- **D:** Correct. Trusted Advisor inspects the account and reports insecure or wasteful settings. In this case: Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports.
- **E:** Correct. Artifact provides AWS audit reports and agreements on demand. In this case: Trusted Advisor reports insecure settings, and Artifact provides the AWS audit reports.

### Question 34 — C

Answer: Some controls are shared, such as patch awareness. Patch awareness is a shared control, because both parties act on the same change. AWS patches the infrastructure while the customer patches what it runs on top of it. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Data protection choices such as encryption and key custody belong to the customer. Why the correct answer wins: Patch awareness is a shared control, because both parties act on the same change.
- **B:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Patch awareness is a shared control, because both parties act on the same change.
- **C:** Correct. AWS patches the infrastructure while the customer patches what it runs on top of it. In this case: Patch awareness is a shared control, because both parties act on the same change.
- **D:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Patch awareness is a shared control, because both parties act on the same change.

### Question 35 — D

Answer: AWS Control Tower. Control Tower establishes a landing zone and applies baseline controls across the organisation. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: Control Tower establishes a landing zone and applies baseline controls across the organisation.
- **B:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: Control Tower establishes a landing zone and applies baseline controls across the organisation.
- **C:** Incorrect for this question. An SCP sets the maximum permissions available to the accounts under it. Why the correct answer wins: Control Tower establishes a landing zone and applies baseline controls across the organisation.
- **D:** Correct. In this case: Control Tower establishes a landing zone and applies baseline controls across the organisation.

### Question 36 — B

Answer: Amazon ECS or Amazon EKS with AWS Fargate. Managed container orchestration runs the containers while the platform owns the hosts. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **B:** Correct. In this case: Managed container orchestration runs the containers while the platform owns the hosts.
- **C:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **D:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.

### Question 37 — B

Answer: AWS Batch. A managed batch scheduler queues the jobs and provisions capacity for each one. Queue and run batch computing jobs without managing the scheduler infrastructure. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each one.
- **B:** Correct. Queue and run batch computing jobs without managing the scheduler infrastructure. In this case: A managed batch scheduler queues the jobs and provisions capacity for each one.
- **C:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each one.
- **D:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: A managed batch scheduler queues the jobs and provisions capacity for each one.

### Question 38 — B

Answer: Amazon EBS volumes. An EBS volume is block storage attached to the instance and persists independently of the running state. Block storage attached to a single instance, used for an operating system or database files. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed file systems for Windows or high-performance workloads. Why the correct answer wins: An EBS volume is block storage attached to the instance and persists independently of the running state.
- **B:** Correct. Block storage attached to a single instance, used for an operating system or database files. In this case: An EBS volume is block storage attached to the instance and persists independently of the running state.
- **C:** Incorrect for this question. Object storage for frequently accessed data with high durability and availability. Why the correct answer wins: An EBS volume is block storage attached to the instance and persists independently of the running state.
- **D:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: An EBS volume is block storage attached to the instance and persists independently of the running state.

### Question 39 — A, E

Answers: AWS Storage Gateway; AWS Snowball devices. Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically. A hybrid file, volume or tape interface that keeps frequently used data on premises. Physical devices that move large datasets into AWS when the network is the bottleneck. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A hybrid file, volume or tape interface that keeps frequently used data on premises. In this case: Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically.
- **B:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically.
- **D:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically.
- **E:** Correct. Physical devices that move large datasets into AWS when the network is the bottleneck. In this case: Storage Gateway keeps a local cache backed by AWS, and Snowball moves the large archive physically.

### Question 40 — B

Answer: Amazon Aurora. Aurora is a managed relational engine compatible with MySQL that adds throughput and managed failover. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: Aurora is a managed relational engine compatible with MySQL that adds throughput and managed failover.
- **B:** Correct. In this case: Aurora is a managed relational engine compatible with MySQL that adds throughput and managed failover.
- **C:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: Aurora is a managed relational engine compatible with MySQL that adds throughput and managed failover.
- **D:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Aurora is a managed relational engine compatible with MySQL that adds throughput and managed failover.

### Question 41 — A

Answer: Amazon ElastiCache. An in-memory cache absorbs repeated reads with sub-millisecond latency. A managed in-memory cache for sub-millisecond reads of hot data. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed in-memory cache for sub-millisecond reads of hot data. In this case: An in-memory cache absorbs repeated reads with sub-millisecond latency.
- **B:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: An in-memory cache absorbs repeated reads with sub-millisecond latency.
- **C:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: An in-memory cache absorbs repeated reads with sub-millisecond latency.
- **D:** Incorrect for this question. A managed graph database for highly connected data. Why the correct answer wins: An in-memory cache absorbs repeated reads with sub-millisecond latency.

### Question 42 — A

Answer: Elastic Load Balancing. Elastic Load Balancing spreads traffic across targets and removes the unhealthy ones. Distributes incoming traffic across multiple targets in one or more Availability Zones. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Distributes incoming traffic across multiple targets in one or more Availability Zones. In this case: Elastic Load Balancing spreads traffic across targets and removes the unhealthy ones.
- **B:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: Elastic Load Balancing spreads traffic across targets and removes the unhealthy ones.
- **C:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Elastic Load Balancing spreads traffic across targets and removes the unhealthy ones.
- **D:** Incorrect for this question. A managed front door for APIs with throttling, authorisation and usage plans. Why the correct answer wins: Elastic Load Balancing spreads traffic across targets and removes the unhealthy ones.

### Question 43 — A, B

Answers: Amazon VPC; AWS PrivateLink. A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint. A logically isolated virtual network in which the customer places its resources. Private connectivity to a service through an endpoint inside the VPC. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A logically isolated virtual network in which the customer places its resources. In this case: A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint.
- **B:** Correct. Private connectivity to a service through an endpoint inside the VPC. In this case: A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint.
- **C:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint.
- **D:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint.
- **E:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: A VPC provides the isolated network, and PrivateLink reaches the partner service through a private endpoint.

### Question 44 — B

Answer: AWS Systems Manager. Systems Manager handles patching and remote command execution across managed nodes. Operations tooling for patching, running commands and inventory across managed nodes. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: Systems Manager handles patching and remote command execution across managed nodes.
- **B:** Correct. Operations tooling for patching, running commands and inventory across managed nodes. In this case: Systems Manager handles patching and remote command execution across managed nodes.
- **C:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Systems Manager handles patching and remote command execution across managed nodes.
- **D:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: Systems Manager handles patching and remote command execution across managed nodes.

### Question 45 — A

Answer: AWS Trusted Advisor. Trusted Advisor checks the account against cost, security, limit and resilience best practices. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **B:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.
- **D:** Incorrect for this question. Service health and event notifications that affect the account. Why the correct answer wins: Trusted Advisor checks the account against cost, security, limit and resilience best practices.

### Question 46 — B

Answer: Amazon EventBridge. EventBridge routes events from AWS services to targets according to rules. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: EventBridge routes events from AWS services to targets according to rules.
- **B:** Correct. In this case: EventBridge routes events from AWS services to targets according to rules.
- **C:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: EventBridge routes events from AWS services to targets according to rules.
- **D:** Incorrect for this question. A state machine that coordinates multi-step workflows with retries and branching. Why the correct answer wins: EventBridge routes events from AWS services to targets according to rules.

### Question 47 — D, E

Answers: Amazon Kinesis; Amazon SQS. Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer. Streaming data ingestion and processing for continuous records. A managed queue that decouples producers from consumers and buffers bursts. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed message broker for existing protocols such as AMQP or MQTT. Why the correct answer wins: Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer.
- **B:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer.
- **C:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer.
- **D:** Correct. Streaming data ingestion and processing for continuous records. In this case: Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer.
- **E:** Correct. A managed queue that decouples producers from consumers and buffers bursts. In this case: Kinesis ingests the continuous stream, and a queue buffers records for the slower consumer.

### Question 48 — A

Answer: Amazon QuickSight. QuickSight provides managed business intelligence dashboards and reports. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: QuickSight provides managed business intelligence dashboards and reports.
- **B:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: QuickSight provides managed business intelligence dashboards and reports.
- **C:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: QuickSight provides managed business intelligence dashboards and reports.
- **D:** Incorrect for this question. Build, train and deploy machine learning models through a managed platform. Why the correct answer wins: QuickSight provides managed business intelligence dashboards and reports.

### Question 49 — D

Answer: Amazon SageMaker. SageMaker covers the model lifecycle from training through deployment. Build, train and deploy machine learning models through a managed platform. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **B:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **C:** Incorrect for this question. Access foundation models through an API without operating the model infrastructure. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **D:** Correct. Build, train and deploy machine learning models through a managed platform. In this case: SageMaker covers the model lifecycle from training through deployment.

### Question 50 — A

Answer: AWS CodePipeline. CodePipeline orchestrates the stages and the approval between them. Orchestrates the build, test and deploy stages of a release. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Orchestrates the build, test and deploy stages of a release. In this case: CodePipeline orchestrates the stages and the approval between them.
- **B:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.
- **C:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.
- **D:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.

### Question 51 — A

Answer: AWS CodeDeploy. CodeDeploy shifts traffic gradually and can roll back when the deployment health check fails. Automates the deployment of application revisions to instances and services. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Automates the deployment of application revisions to instances and services. In this case: CodeDeploy shifts traffic gradually and can roll back when the deployment health check fails.
- **B:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: CodeDeploy shifts traffic gradually and can roll back when the deployment health check fails.
- **C:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: CodeDeploy shifts traffic gradually and can roll back when the deployment health check fails.
- **D:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CodeDeploy shifts traffic gradually and can roll back when the deployment health check fails.

### Question 52 — C

Answer: AWS Service Catalog. Service Catalog publishes a curated set of approved products that teams can launch. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Service Catalog publishes a curated set of approved products that teams can launch.
- **B:** Incorrect for this question. Operations tooling for patching, running commands and inventory across managed nodes. Why the correct answer wins: Service Catalog publishes a curated set of approved products that teams can launch.
- **C:** Correct. In this case: Service Catalog publishes a curated set of approved products that teams can launch.
- **D:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: Service Catalog publishes a curated set of approved products that teams can launch.

### Question 53 — C

Answer: Amazon Lightsail. Lightsail bundles the basics for a small project at a flat, predictable price. A simplified bundle of compute, storage and networking for small projects at a predictable price. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.
- **B:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.
- **C:** Correct. A simplified bundle of compute, storage and networking for small projects at a predictable price. In this case: Lightsail bundles the basics for a small project at a flat, predictable price.
- **D:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.

### Question 54 — D

Answer: AWS Health Dashboard. The Health Dashboard reports AWS service events and their effect on the account. Service health and event notifications that affect the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Checks an account against best practices for cost, security, limits and resilience. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **B:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **C:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **D:** Correct. Service health and event notifications that affect the account. In this case: The Health Dashboard reports AWS service events and their effect on the account.

### Question 55 — B, E

Answers: Amazon CloudWatch; AWS X-Ray. CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services. Metrics, logs and alarms for the resources and applications in the account. Traces requests through a distributed application to find where time is spent. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services.
- **B:** Correct. Traces requests through a distributed application to find where time is spent. In this case: CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services.
- **C:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services.
- **D:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services.
- **E:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch holds the metric and the alarm, and X-Ray traces the request across the services.

### Question 56 — A

Answer: AWS Direct Connect. Direct Connect provides a dedicated private link from the customer facility into AWS. A dedicated private network connection from a customer facility into AWS. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A dedicated private network connection from a customer facility into AWS. In this case: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **B:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **C:** Incorrect for this question. A central router that connects many VPCs and on-premises networks. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **D:** Incorrect for this question. An encrypted tunnel over the internet between a customer network and a VPC. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.

### Question 57 — B

Answer: AWS Site-to-Site VPN. A Site-to-Site VPN builds an encrypted tunnel over the internet and can be set up quickly. An encrypted tunnel over the internet between a customer network and a VPC. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be set up quickly.
- **B:** Correct. An encrypted tunnel over the internet between a customer network and a VPC. In this case: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be set up quickly.
- **C:** Incorrect for this question. Private connectivity to a service through an endpoint inside the VPC. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be set up quickly.
- **D:** Incorrect for this question. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Why the correct answer wins: A Site-to-Site VPN builds an encrypted tunnel over the internet and can be set up quickly.

### Question 58 — B

Answer: On-Demand Instances. On-Demand capacity is billed as it is used with no commitment. Capacity billed by the second or hour with no commitment. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment.
- **B:** Correct. Capacity billed by the second or hour with no commitment. In this case: On-Demand capacity is billed as it is used with no commitment.
- **C:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment.
- **D:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment.

### Question 59 — C

Answer: Dedicated Hosts. Dedicated Hosts give the customer a physical server that no other account shares. A physical server dedicated to one customer, used for licensing or compliance requirements. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: Dedicated Hosts give the customer a physical server that no other account shares.
- **B:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: Dedicated Hosts give the customer a physical server that no other account shares.
- **C:** Correct. A physical server dedicated to one customer, used for licensing or compliance requirements. In this case: Dedicated Hosts give the customer a physical server that no other account shares.
- **D:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Dedicated Hosts give the customer a physical server that no other account shares.

### Question 60 — B

Answer: Cost Anomaly Detection. Cost Anomaly Detection alerts on spending that deviates from the expected pattern. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Cost Anomaly Detection alerts on spending that deviates from the expected pattern.
- **B:** Correct. In this case: Cost Anomaly Detection alerts on spending that deviates from the expected pattern.
- **C:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: Cost Anomaly Detection alerts on spending that deviates from the expected pattern.
- **D:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: Cost Anomaly Detection alerts on spending that deviates from the expected pattern.

### Question 61 — A, D

Answers: AWS Cost and Usage Report; AWS Budgets. The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance. The most granular billing dataset, delivered to a bucket for analysis. Set a spending or usage threshold and alert or act when it is crossed. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Set a spending or usage threshold and alert or act when it is crossed. In this case: The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance.
- **B:** Incorrect for this question. Estimate the cost of a planned architecture before it is built. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance.
- **C:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance.
- **D:** Correct. The most granular billing dataset, delivered to a bucket for analysis. In this case: The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance.
- **E:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Budgets alerts against the allowance.

### Question 62 — C

Answer: Keep a separate bill and separate discounts per account. Each account's usage stays separate, so the combined volume discount is never earned. Separate accounts do not pool usage, so each misses the discounts the total would earn. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Each account's usage stays separate, so the combined volume discount is never earned.
- **B:** Incorrect for this question. Limited monthly usage at no charge for eligible services on a new or qualifying account. Why the correct answer wins: Each account's usage stays separate, so the combined volume discount is never earned.
- **C:** Correct. Separate accounts do not pool usage, so each misses the discounts the total would earn. In this case: Each account's usage stays separate, so the combined volume discount is never earned.
- **D:** Incorrect for this question. One bill for all accounts, with usage aggregated so volume discounts are shared. Why the correct answer wins: Each account's usage stays separate, so the combined volume discount is never earned.

### Question 63 — C

Answer: AWS Enterprise Support. Enterprise Support adds a designated technical account manager and the fastest response. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Business-hours email support for development and test workloads. Why the correct answer wins: Enterprise Support adds a designated technical account manager and the fastest response.
- **B:** Incorrect for this question. Production support with 24/7 access, faster response and Trusted Advisor checks. Why the correct answer wins: Enterprise Support adds a designated technical account manager and the fastest response.
- **C:** Correct. In this case: Enterprise Support adds a designated technical account manager and the fastest response.
- **D:** Incorrect for this question. Account and billing support with documentation and health checks, at no charge. Why the correct answer wins: Enterprise Support adds a designated technical account manager and the fastest response.

### Question 64 — B

Answer: Search AWS re:Post for an answered question. re:Post is the community knowledge base where common service and account questions are answered. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Partners are third-party firms with AWS-validated skills for implementation work. Why the correct answer wins: re:Post is the community knowledge base where common service and account questions are answered.
- **B:** Correct. In this case: re:Post is the community knowledge base where common service and account questions are answered.
- **C:** Incorrect for this question. The reference documentation states what a service does and how it is configured. Why the correct answer wins: re:Post is the community knowledge base where common service and account questions are answered.
- **D:** Incorrect for this question. A vetted reference architecture shortens design work for a common workload. Why the correct answer wins: re:Post is the community knowledge base where common service and account questions are answered.

### Question 65 — C

Answer: Savings Plans. Savings Plans commit to a spend level per hour and apply the discount across eligible usage. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: Savings Plans commit to a spend level per hour and apply the discount across eligible usage.
- **B:** Incorrect for this question. Limited monthly usage at no charge for eligible services on a new or qualifying account. Why the correct answer wins: Savings Plans commit to a spend level per hour and apply the discount across eligible usage.
- **C:** Correct. In this case: Savings Plans commit to a spend level per hour and apply the discount across eligible usage.
- **D:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Savings Plans commit to a spend level per hour and apply the discount across eligible usage.
