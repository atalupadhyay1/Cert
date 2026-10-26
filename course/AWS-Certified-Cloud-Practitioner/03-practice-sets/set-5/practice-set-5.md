# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 5

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. Online examinations run twice a year and cannot drop a connection mid-paper when a server component fails. Which cloud benefit matters most here?

- A. Stop spending on undifferentiated heavy lifting
- B. Buy servers up front and depreciate them
- C. Reliability through managed, redundant infrastructure
- D. Global reach: deploy into multiple Regions quickly

### 2. A course team wants a separate practice environment for each student, created at the start of term and deleted at the end. Which cloud benefit makes that affordable?

- A. Agility: provision resources in minutes
- B. A flat monthly fee that does not change with usage
- C. Keep ownership of the physical data centre
- D. Trade capital expense for variable expense

### 3. A training lab runs for twenty minutes per class, several times a day, and should not be billed for the idle hours between classes. Which pricing characteristic matters?

- A. Buy servers up front and depreciate them
- B. A flat monthly fee that does not change with usage
- C. Billing per second for compute that exists briefly
- D. Keep ownership of the physical data centre

### 4. A travel site plans to stream large destination videos from AWS and has never paid for outbound traffic before. Which cost item must enter the business case?

- A. Data transfer out to the internet carries a charge
- B. Volume discounts that grow with usage
- C. A flat monthly fee that does not change with usage
- D. Reserved Instances

### 5. The student portal fails whenever the email service is slow, because the portal waits on it to confirm each registration. Which principle should be applied?

- A. Direct synchronous calls between every tier
- B. Scale the single monolith vertically only
- C. Loose coupling with a queue between tiers
- D. Deploy across multiple Availability Zones

### 6. Technicians rebuild the teaching lab environment by hand at the start of every term, with small differences each time. Which principle would fix this?

- A. Scale the single monolith vertically only
- B. Direct synchronous calls between every tier
- C. Serverless compute for intermittent work
- D. Automate repeated provisioning instead of rebuilding by hand

### 7. A review asks whether the chosen instance families and storage tiers still suit the workload as its usage changes. Which Well-Architected pillar covers that?

- A. Performance efficiency pillar
- B. Cost optimization pillar
- C. Security pillar
- D. Sustainability pillar

### 8. A university must reduce the energy its workloads consume and also justify every dollar of cloud spend. Which two pillars apply? Select two.

- A. Security pillar
- B. Cost optimization pillar
- C. Operational excellence pillar
- D. Sustainability pillar
- E. Reliability pillar

### 9. A university wants its cloud programme measured by enrolment, completion and student satisfaction rather than by servers migrated. Which perspective does that?

- A. People perspective of the AWS Cloud Adoption Framework
- B. Business perspective of the AWS Cloud Adoption Framework
- C. Operations perspective of the AWS Cloud Adoption Framework
- D. Platform perspective of the AWS Cloud Adoption Framework

### 10. A university must show that its cloud programme meets student-data protection obligations. Which Cloud Adoption Framework perspective covers this?

- A. Security perspective of the AWS Cloud Adoption Framework
- B. Business perspective of the AWS Cloud Adoption Framework
- C. Platform perspective of the AWS Cloud Adoption Framework
- D. Operations perspective of the AWS Cloud Adoption Framework

### 11. The student records system must move to AWS over one weekend with no code change at all. Which strategy is this?

- A. Repurchase: move to a different product
- B. Relocate: move the platform to a cloud-native equivalent
- C. Refactor: redesign the application for cloud architecture
- D. Rehost: move the application as it is

### 12. An alumni directory is due to be decommissioned when the new system goes live in nine months. What should happen to it in the migration plan?

- A. Retire: switch the workload off
- B. Retain: keep the workload where it is
- C. Rehost: move the application as it is
- D. Replatform: change a few managed components on the way

### 13. Lecture recordings are watched from many countries and must be served from caches close to viewers. Which infrastructure element provides that?

- A. Local Zones for very low latency
- B. Regions and Availability Zones
- C. AWS Outposts for on-premises capacity
- D. Edge locations for content delivery

### 14. The exam board needs to know how much submitted coursework could be lost in a regional failure and how quickly results could be republished. What must be defined?

- A. Scale the single monolith vertically only
- B. Define a recovery objective and test the recovery path
- C. Direct synchronous calls between every tier
- D. Place everything in one Availability Zone

### 15. Results publication day brings a short traffic peak, and the service must survive the loss of one Availability Zone without manual action. Which two choices fit? Select two.

- A. Deploy across multiple Availability Zones
- B. Place everything in one Availability Zone
- C. Scale the single monolith vertically only
- D. Scale out automatically as demand rises
- E. Direct synchronous calls between every tier

### 16. A review asks who maintains the physical hosts and their disks underneath the virtual machines the university runs. Under the shared responsibility model, who?

- A. The customer is responsible for the data-centre building
- B. The customer is responsible for configuring IAM permissions
- C. AWS is responsible for the physical facilities and hardware
- D. The customer is responsible for the data it stores in AWS

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. Every registrar needs the same read access to enrolment data, and that access changes when policy changes. What should be created?

- A. Use the root user for daily administration
- B. Put the users in a group and attach the policy to the group
- C. Create an IAM role and let the workload assume it
- D. Create an IAM user with long-lived credentials

### 18. A contractor needs to read one table for one week and nothing more. What should be granted?

- A. Rotate access keys on a schedule
- B. Require multi-factor authentication
- C. Give every engineer administrator access for convenience
- D. Grant only the permissions the task needs

### 19. A lecturer's AWS password was reused from a site that was breached, and the account signs in with a password only. Which control limits the damage?

- A. Rotate access keys on a schedule
- B. Grant only the permissions the task needs
- C. Put the users in a group and attach the policy to the group
- D. Require multi-factor authentication

### 20. Access keys were baked into a teaching lab image two years ago and are still valid. Which control should have been applied?

- A. Rotate access keys on a schedule
- B. Require multi-factor authentication
- C. Enable MFA and delete the root access keys
- D. Grant only the permissions the task needs

### 21. The grading job on Amazon EC2 must read submitted coursework from a bucket without storing any credential. What should it use?

- A. Put the password in the application source code
- B. Use the root user for daily administration
- C. Create an IAM role and let the workload assume it
- D. Create an IAM user with long-lived credentials

### 22. Academic staff should sign in to AWS with the university directory account they already use. What should be configured?

- A. Federate the company directory into AWS
- B. Put the users in a group and attach the policy to the group
- C. Create an IAM user with long-lived credentials
- D. Use Amazon Cognito for customer sign-in

### 23. The administration interface must accept connections only from the campus address range. What should be applied?

- A. Use AWS Network Firewall for VPC-level inspection
- B. Use a network ACL as a stateless subnet filter
- C. Open every port to the internet and rely on the application
- D. Use a security group as a stateful instance firewall

### 24. The exam portal must reject scripted form attacks and stay reachable during a flood of junk traffic on results day. Which two services fit? Select two.

- A. Use a security group as a stateful instance firewall
- B. Use AWS WAF to block web attack patterns
- C. Use AWS Network Firewall for VPC-level inspection
- D. Use AWS Shield for DDoS protection
- E. Use a network ACL as a stateless subnet filter

### 25. Coursework is uploaded from student laptops over the internet and must be unreadable to anyone intercepting it. What is required?

- A. Set a retention period and delete expired copies
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Encrypt data in transit with TLS
- D. Use a customer managed key for the required control

### 26. Research data must be encrypted with keys the university can revoke on its own authority when a project ends. What should be used?

- A. Use Amazon Macie to find sensitive data in Amazon S3
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Encrypt data in transit with TLS
- D. Use a customer managed key for the required control

### 27. The shared lab database password must be rotated every month and must never appear in application configuration files. Where should it live?

- A. Put the password in the application source code
- B. Use AWS Certificate Manager for TLS certificates
- C. Store the database credential in AWS Secrets Manager and rotate it
- D. Use AWS KMS to create and control encryption keys

### 28. Research buckets may contain student identifiers that should never have been copied there. Which service finds them?

- A. Use AWS CloudTrail to record API activity
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use Amazon Inspector to scan workloads for vulnerabilities
- D. Use Amazon GuardDuty to detect suspicious activity

### 29. Exam servers must be checked for missing software patches, and the team must be told if one of them starts behaving like a compromised host. Which two services fit? Select two.

- A. Use AWS Security Hub to aggregate findings in one place
- B. Use Amazon Inspector to scan workloads for vulnerabilities
- C. Use AWS CloudTrail to record API activity
- D. Use Amazon Macie to find sensitive data in Amazon S3
- E. Use Amazon GuardDuty to detect suspicious activity

### 30. Before retention and encryption rules can be set for a research data lake, the team must agree which datasets are sensitive. What comes first?

- A. AWS Backup
- B. Classify the data and tag each store by sensitivity
- C. An Amazon S3 bucket policy that grants public read
- D. Set an S3 lifecycle rule to expire old objects

### 31. Recorded lectures must be deleted automatically after two years with no manual cleanup. What should be configured?

- A. Set an S3 lifecycle rule to expire old objects
- B. An Amazon S3 bucket policy that grants public read
- C. AWS Backup
- D. Set a retention period and delete expired copies

### 32. An accreditation review needs evidence collected and mapped to a control framework across several accounts. Which service fits?

- A. Use AWS Config to record resource configuration changes
- B. Use AWS Audit Manager to collect evidence for an audit
- C. Download the compliance reports from AWS Artifact
- D. Use AWS CloudTrail to record API activity

### 33. A compliance lead wants a quick check for insecure account settings and a record of every API call made during a term. Which two services provide them? Select two.

- A. Use Amazon GuardDuty to detect suspicious activity
- B. Read the security checks in AWS Trusted Advisor
- C. Use Amazon Macie to find sensitive data in Amazon S3
- D. Use Amazon Inspector to scan workloads for vulnerabilities
- E. Use AWS CloudTrail to record API activity

### 34. A review asks who decides which staff may read the enrolment database and with what permissions. Under the shared responsibility model, who?

- A. AWS is responsible for patching a managed service such as Amazon S3
- B. AWS is responsible for the physical facilities and hardware
- C. The customer is responsible for configuring IAM permissions
- D. The customer is responsible for the data-centre building

### 35. A university must prevent any account in its organisation from deploying resources outside two approved Regions. What should be applied?

- A. AWS Control Tower
- B. Attach a JSON policy that allows only the required actions
- C. Apply a service control policy in AWS Organizations
- D. Use a service control policy to grant permissions to a team

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. Each uploaded lecture must be transcoded into three formats as soon as it arrives, with no server kept running. Which compute service fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. AWS Batch
- C. AWS Lambda
- D. Amazon EC2 instances

### 37. A booking engine is already split into container images and needs managed orchestration without the team operating hosts. Which compute option fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. Amazon Lightsail
- C. Amazon EC2 instances
- D. AWS Lambda

### 38. Recorded lectures are watched a few times a year but must start playing immediately when requested. Which storage class fits?

- A. Amazon EBS volumes
- B. Amazon S3 Standard
- C. Amazon S3 Glacier storage classes
- D. Amazon S3 Standard-IA

### 39. A media department must physically ship 300 TB of archive footage to AWS, and the footage must then sit in cheap long-term storage. Which two services fit? Select two.

- A. Amazon S3 Glacier storage classes
- B. Amazon EBS volumes
- C. AWS Backup
- D. Amazon EFS file system
- E. AWS Snowball devices

### 40. Exam answer keys must be read millions of times during a paper at consistent single-digit millisecond latency. Which database fits?

- A. Amazon RDS
- B. Amazon ElastiCache
- C. Amazon DynamoDB
- D. Amazon Redshift

### 41. Analysts need multi-year enrolment and results reporting with complex joins across large tables. Which service fits?

- A. Amazon Athena
- B. Amazon RDS
- C. Amazon Redshift
- D. Amazon DynamoDB

### 42. Booking traffic from many countries must reach the closest healthy endpoint over the AWS global network with static anycast addresses. Which service fits?

- A. Amazon Route 53
- B. Amazon CloudFront
- C. AWS Global Accelerator
- D. Elastic Load Balancing

### 43. The public domain needs health-checked failover between two endpoints, and traffic must be spread across instances in both Availability Zones. Which two services fit? Select two.

- A. Elastic Load Balancing
- B. Amazon CloudFront
- C. AWS Global Accelerator
- D. Amazon Route 53
- E. Amazon API Gateway

### 44. A lab fleet of Windows and Linux servers must receive patches on a schedule and report compliance. Which service fits?

- A. Amazon CloudWatch
- B. AWS CloudFormation
- C. AWS Systems Manager
- D. AWS Service Catalog

### 45. Teaching teams should launch only pre-approved course environments themselves, without a platform ticket. Which service fits?

- A. AWS Service Catalog
- B. AWS CloudFormation
- C. AWS Systems Manager
- D. AWS Control Tower

### 46. Assignment submissions arrive in bursts that the marking service cannot absorb immediately, and none may be lost. Which service fits?

- A. Amazon SQS
- B. AWS Step Functions
- C. Amazon SNS
- D. Amazon EventBridge

### 47. An admission decision moves through several ordered steps with retries, and the process must start when an application record changes state. Which two services fit? Select two.

- A. Amazon SQS
- B. Amazon Kinesis
- C. AWS Step Functions
- D. Amazon SNS
- E. Amazon EventBridge

### 48. A language department wants a conversational tutor built on a foundation model without operating any model infrastructure. Which service fits?

- A. Amazon EMR
- B. Amazon SageMaker
- C. Amazon QuickSight
- D. Amazon Bedrock

### 49. Course teams want SQL answers over clickstream files already stored in Amazon S3 with no cluster to manage. Which service fits?

- A. Amazon EMR
- B. AWS Glue
- C. Amazon Redshift
- D. Amazon Athena

### 50. Students need a development environment in a browser with no software installed on their own laptops. Which service fits?

- A. AWS CodePipeline
- B. AWS Cloud9
- C. AWS CodeBuild
- D. AWS CodeDeploy

### 51. Every commit must compile and run the test suite in a clean managed environment. Which service performs the work?

- A. AWS CodeDeploy
- B. AWS CloudFormation
- C. AWS CodePipeline
- D. AWS CodeBuild

### 52. A teaching team uploads its Java web application and wants the platform to size, balance and patch the servers around it. Which service fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. AWS Elastic Beanstalk
- C. Amazon EC2 instances
- D. AWS Lambda

### 53. Each department must be able to launch a standard lab environment from an approved template without asking the platform team. Which service fits?

- A. AWS CloudFormation
- B. AWS Service Catalog
- C. AWS Systems Manager
- D. AWS Control Tower

### 54. Operations wants automatic notification when unsent coursework messages pile up beyond a set depth. Which service holds the measurement and triggers the notification?

- A. Amazon CloudWatch
- B. AWS X-Ray
- C. Use AWS CloudTrail to record API activity
- D. Use AWS Config to record resource configuration changes

### 55. A sluggish booking flow must be attributed to the component that consumed the time, and incidents published on the AWS side need their own feed. Which two services fit? Select two.

- A. AWS Health Dashboard
- B. Use AWS CloudTrail to record API activity
- C. Use Amazon Inspector to scan workloads for vulnerabilities
- D. AWS X-Ray
- E. Amazon CloudWatch

### 56. A campus file share must keep working locally while a copy is stored in AWS for disaster recovery. Which service fits?

- A. Amazon EFS file system
- B. AWS Snowball devices
- C. AWS Backup
- D. AWS Storage Gateway

### 57. A research application must reach a partner service privately without any traffic crossing the internet. Which service fits?

- A. AWS Transit Gateway
- B. AWS PrivateLink
- C. Amazon VPC
- D. AWS Direct Connect

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. Term-time lab demand is unknown in advance and nothing can be committed this year. Which purchasing option fits?

- A. Dedicated Hosts
- B. On-Demand Instances
- C. Reserved Instances
- D. Spot Instances

### 59. Overnight encoding of lecture videos can be interrupted and restarted, and cost per hour is the binding constraint. Which option fits?

- A. Spot Instances
- B. Reserved Instances
- C. On-Demand Instances
- D. Dedicated Hosts

### 60. A department wants an alert when its term spend reaches eighty percent of the agreed budget. Which tool fits?

- A. AWS Cost Explorer
- B. AWS Budgets
- C. AWS Pricing Calculator
- D. AWS Cost and Usage Report

### 61. The finance office must see spend broken down by service and export line-item detail for its own model. Which two tools fit? Select two.

- A. Wait for the monthly invoice and reconcile it afterwards
- B. AWS Cost and Usage Report
- C. Cost Anomaly Detection
- D. AWS Cost Explorer
- E. AWS Budgets

### 62. One invoice covers the whole university and each faculty must see its own share of it. What should be applied?

- A. AWS Cost and Usage Report
- B. Tag resources and activate cost allocation tags
- C. Consolidated billing in AWS Organizations
- D. Keep a separate bill and separate discounts per account

### 63. A university wants a named technical advisor who understands its account and helps with planning. Which benefit provides that?

- A. A designated Technical Account Manager
- B. AWS Basic Support
- C. AWS Developer Support
- D. AWS Business Support

### 64. A department wants to buy a third-party learning plugin that is billed on the same AWS invoice. Where should it buy it?

- A. Buy the software through AWS Marketplace
- B. Read the AWS documentation and service user guides
- C. Search AWS re:Post for an answered question
- D. Start from an AWS Solutions Library reference deployment

### 65. A student wants to explore a few services within published monthly limits before incurring any charge. What provides that?

- A. Savings Plans
- B. Volume discounts that grow with usage
- C. Reserved Instances
- D. The AWS Free Tier allowances

---

## Answer key and explanations

### Question 1 — C

Answer: Reliability through managed, redundant infrastructure. Managed, redundant infrastructure removes the single points of failure the university would otherwise engineer. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. AWS operates the facilities, hardware and managed platforms so the team can focus on its product. Why the correct answer wins: Managed, redundant infrastructure removes the single points of failure the university would otherwise engineer.
- **B:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Managed, redundant infrastructure removes the single points of failure the university would otherwise engineer.
- **C:** Correct. In this case: Managed, redundant infrastructure removes the single points of failure the university would otherwise engineer.
- **D:** Incorrect for this question. A global infrastructure lets a company put workloads near its users without building facilities. Why the correct answer wins: Managed, redundant infrastructure removes the single points of failure the university would otherwise engineer.

### Question 2 — A

Answer: Agility: provision resources in minutes. Environments are provisioned in minutes and removed afterwards, so a short-lived copy is a routine step. New environments are created in minutes, which shortens the time to test an idea. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. New environments are created in minutes, which shortens the time to test an idea. In this case: Environments are provisioned in minutes and removed afterwards, so a short-lived copy is a routine step.
- **B:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Environments are provisioned in minutes and removed afterwards, so a short-lived copy is a routine step.
- **C:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Environments are provisioned in minutes and removed afterwards, so a short-lived copy is a routine step.
- **D:** Incorrect for this question. Up-front data-centre investment is replaced by usage-based spending. Why the correct answer wins: Environments are provisioned in minutes and removed afterwards, so a short-lived copy is a routine step.

### Question 3 — C

Answer: Billing per second for compute that exists briefly. Compute billed per second means short sessions cost only the minutes they run. Short-lived compute is charged for the seconds it runs rather than a minimum period. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Compute billed per second means short sessions cost only the minutes they run.
- **B:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Compute billed per second means short sessions cost only the minutes they run.
- **C:** Correct. Short-lived compute is charged for the seconds it runs rather than a minimum period. In this case: Compute billed per second means short sessions cost only the minutes they run.
- **D:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Compute billed per second means short sessions cost only the minutes they run.

### Question 4 — A

Answer: Data transfer out to the internet carries a charge. Traffic leaving AWS for the internet is billed, and a media-heavy site generates a lot of it. Traffic leaving AWS for the internet is billed, which an on-premises design never had to count. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Traffic leaving AWS for the internet is billed, which an on-premises design never had to count. In this case: Traffic leaving AWS for the internet is billed, and a media-heavy site generates a lot of it.
- **B:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: Traffic leaving AWS for the internet is billed, and a media-heavy site generates a lot of it.
- **C:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Traffic leaving AWS for the internet is billed, and a media-heavy site generates a lot of it.
- **D:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Traffic leaving AWS for the internet is billed, and a media-heavy site generates a lot of it.

### Question 5 — C

Answer: Loose coupling with a queue between tiers. A buffer between the portal and the email service lets each side work at its own pace. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A buffer between the portal and the email service lets each side work at its own pace.
- **B:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A buffer between the portal and the email service lets each side work at its own pace.
- **C:** Correct. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. In this case: A buffer between the portal and the email service lets each side work at its own pace.
- **D:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: A buffer between the portal and the email service lets each side work at its own pace.

### Question 6 — D

Answer: Automate repeated provisioning instead of rebuilding by hand. Creating the environment from a template makes each rebuild identical and disposable. Environments are created from a script or template, so they are consistent and disposable. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Creating the environment from a template makes each rebuild identical and disposable.
- **B:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Creating the environment from a template makes each rebuild identical and disposable.
- **C:** Incorrect for this question. No server is provisioned, and the service runs only when it is invoked. Why the correct answer wins: Creating the environment from a template makes each rebuild identical and disposable.
- **D:** Correct. Environments are created from a script or template, so they are consistent and disposable. In this case: Creating the environment from a template makes each rebuild identical and disposable.

### Question 7 — A

Answer: Performance efficiency pillar. The performance efficiency pillar asks whether resources are chosen well as demand and technology change. The pillar about using resources efficiently as demand and technology change. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The pillar about using resources efficiently as demand and technology change. In this case: The performance efficiency pillar asks whether resources are chosen well as demand and technology change.
- **B:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The performance efficiency pillar asks whether resources are chosen well as demand and technology change.
- **C:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: The performance efficiency pillar asks whether resources are chosen well as demand and technology change.
- **D:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: The performance efficiency pillar asks whether resources are chosen well as demand and technology change.

### Question 8 — B, D

Answers: Sustainability pillar; Cost optimization pillar. Sustainability covers environmental impact, and cost optimization covers value for the money spent. The pillar about minimising the environmental impact of running a workload. The pillar about delivering value at the lowest price that meets the requirement. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: Sustainability covers environmental impact, and cost optimization covers value for the money spent.
- **B:** Correct. The pillar about delivering value at the lowest price that meets the requirement. In this case: Sustainability covers environmental impact, and cost optimization covers value for the money spent.
- **C:** Incorrect for this question. The pillar about running and improving workloads, including automation and small reversible changes. Why the correct answer wins: Sustainability covers environmental impact, and cost optimization covers value for the money spent.
- **D:** Correct. The pillar about minimising the environmental impact of running a workload. In this case: Sustainability covers environmental impact, and cost optimization covers value for the money spent.
- **E:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: Sustainability covers environmental impact, and cost optimization covers value for the money spent.

### Question 9 — B

Answer: Business perspective of the AWS Cloud Adoption Framework. The business perspective connects cloud work to business outcomes and value. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about skills, roles and organisational change. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.
- **B:** Correct. In this case: The business perspective connects cloud work to business outcomes and value.
- **C:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.
- **D:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The business perspective connects cloud work to business outcomes and value.

### Question 10 — A

Answer: Security perspective of the AWS Cloud Adoption Framework. The security perspective covers meeting security and compliance objectives. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: The security perspective covers meeting security and compliance objectives.
- **B:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.
- **C:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.
- **D:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The security perspective covers meeting security and compliance objectives.

### Question 11 — D

Answer: Rehost: move the application as it is. Rehost moves the application as it is, which is the fastest and least invasive path. The application moves without code change, which is the fastest path but captures few cloud benefits. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company replaces the application with a commercially available equivalent. Why the correct answer wins: Rehost moves the application as it is, which is the fastest and least invasive path.
- **B:** Incorrect for this question. The whole platform moves to a hosted equivalent without changing the application itself. Why the correct answer wins: Rehost moves the application as it is, which is the fastest and least invasive path.
- **C:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Rehost moves the application as it is, which is the fastest and least invasive path.
- **D:** Correct. The application moves without code change, which is the fastest path but captures few cloud benefits. In this case: Rehost moves the application as it is, which is the fastest and least invasive path.

### Question 12 — B

Answer: Retain: keep the workload where it is. Retain keeps a workload in place when moving it would cost more than waiting for retirement. The workload stays in place because moving it is not justified yet. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The workload is no longer needed, so it is decommissioned instead of migrated. Why the correct answer wins: Retain keeps a workload in place when moving it would cost more than waiting for retirement.
- **B:** Correct. The workload stays in place because moving it is not justified yet. In this case: Retain keeps a workload in place when moving it would cost more than waiting for retirement.
- **C:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Retain keeps a workload in place when moving it would cost more than waiting for retirement.
- **D:** Incorrect for this question. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. Why the correct answer wins: Retain keeps a workload in place when moving it would cost more than waiting for retirement.

### Question 13 — D

Answer: Edge locations for content delivery. Edge locations cache content near users rather than serving everything from a Region. Points of presence that cache content close to users rather than in a Region. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. An extension of a Region placed close to a large population or industry centre. Why the correct answer wins: Edge locations cache content near users rather than serving everything from a Region.
- **B:** Incorrect for this question. A Region is a geographic area and each Availability Zone within it is an isolated group of data centres. Why the correct answer wins: Edge locations cache content near users rather than serving everything from a Region.
- **C:** Incorrect for this question. A rack of AWS infrastructure installed in the customer facility and operated through AWS. Why the correct answer wins: Edge locations cache content near users rather than serving everything from a Region.
- **D:** Correct. Points of presence that cache content close to users rather than in a Region. In this case: Edge locations cache content near users rather than serving everything from a Region.

### Question 14 — B

Answer: Define a recovery objective and test the recovery path. Recovery point and recovery time objectives state the loss and downtime the service can tolerate. A recovery time and recovery point objective turn disaster recovery from an intention into a design. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Recovery point and recovery time objectives state the loss and downtime the service can tolerate.
- **B:** Correct. A recovery time and recovery point objective turn disaster recovery from an intention into a design. In this case: Recovery point and recovery time objectives state the loss and downtime the service can tolerate.
- **C:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Recovery point and recovery time objectives state the loss and downtime the service can tolerate.
- **D:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Recovery point and recovery time objectives state the loss and downtime the service can tolerate.

### Question 15 — A, D

Answers: Deploy across multiple Availability Zones; Scale out automatically as demand rises. Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure. Two or more Zones give the workload a survivor when one Zone fails. Capacity follows the measured demand rather than a forecast. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure.
- **B:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure.
- **D:** Correct. Capacity follows the measured demand rather than a forecast. In this case: Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure.
- **E:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Automatic scaling covers the publication peak, and a multi-Zone deployment survives a Zone failure.

### Question 16 — C

Answer: AWS is responsible for the physical facilities and hardware. AWS owns the physical servers, storage hardware and the facilities around them. AWS operates the buildings, power, network fabric and the hardware underneath the service. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: AWS owns the physical servers, storage hardware and the facilities around them.
- **B:** Incorrect for this question. Identity and access configuration is a customer responsibility in every model. Why the correct answer wins: AWS owns the physical servers, storage hardware and the facilities around them.
- **C:** Correct. AWS operates the buildings, power, network fabric and the hardware underneath the service. In this case: AWS owns the physical servers, storage hardware and the facilities around them.
- **D:** Incorrect for this question. Classification, access and protection of the data remain with the customer. Why the correct answer wins: AWS owns the physical servers, storage hardware and the facilities around them.

### Question 17 — B

Answer: Put the users in a group and attach the policy to the group. A group holds the shared policy once, so one change updates every registrar. A group is a collection of users that share permissions, which keeps the policy in one place. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: A group holds the shared policy once, so one change updates every registrar.
- **B:** Correct. A group is a collection of users that share permissions, which keeps the policy in one place. In this case: A group holds the shared policy once, so one change updates every registrar.
- **C:** Incorrect for this question. A role hands out temporary credentials, so nothing long-lived is stored. Why the correct answer wins: A group holds the shared policy once, so one change updates every registrar.
- **D:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: A group holds the shared policy once, so one change updates every registrar.

### Question 18 — D

Answer: Grant only the permissions the task needs. Granting only the actions the task requires limits the damage a mistake or a leaked credential can do. Starting from the minimum and adding as needed keeps the blast radius small. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: Granting only the actions the task requires limits the damage a mistake or a leaked credential can do.
- **B:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Granting only the actions the task requires limits the damage a mistake or a leaked credential can do.
- **C:** Incorrect for this question. Broad standing access means one mistaken action or stolen credential can change anything. Why the correct answer wins: Granting only the actions the task requires limits the damage a mistake or a leaked credential can do.
- **D:** Correct. Starting from the minimum and adding as needed keeps the blast radius small. In this case: Granting only the actions the task requires limits the damage a mistake or a leaked credential can do.

### Question 19 — D

Answer: Require multi-factor authentication. A second factor means the breached password alone cannot sign in. A second factor makes a stolen password insufficient on its own. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: A second factor means the breached password alone cannot sign in.
- **B:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: A second factor means the breached password alone cannot sign in.
- **C:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: A second factor means the breached password alone cannot sign in.
- **D:** Correct. A second factor makes a stolen password insufficient on its own. In this case: A second factor means the breached password alone cannot sign in.

### Question 20 — A

Answer: Rotate access keys on a schedule. Rotation retires keys on a schedule, so a key copied into an image stops working. A rotation schedule limits how long a leaked key stays useful. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A rotation schedule limits how long a leaked key stays useful. In this case: Rotation retires keys on a schedule, so a key copied into an image stops working.
- **B:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Rotation retires keys on a schedule, so a key copied into an image stops working.
- **C:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Rotation retires keys on a schedule, so a key copied into an image stops working.
- **D:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: Rotation retires keys on a schedule, so a key copied into an image stops working.

### Question 21 — C

Answer: Create an IAM role and let the workload assume it. A role issues temporary credentials to the workload, so nothing long-lived is written down. A role hands out temporary credentials, so nothing long-lived is stored. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A role issues temporary credentials to the workload, so nothing long-lived is written down.
- **B:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: A role issues temporary credentials to the workload, so nothing long-lived is written down.
- **C:** Correct. A role hands out temporary credentials, so nothing long-lived is stored. In this case: A role issues temporary credentials to the workload, so nothing long-lived is written down.
- **D:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: A role issues temporary credentials to the workload, so nothing long-lived is written down.

### Question 22 — A

Answer: Federate the company directory into AWS. Federating the directory uses the existing identity instead of a new set of AWS credentials. Existing corporate identities are used instead of a separate set of AWS credentials. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Existing corporate identities are used instead of a separate set of AWS credentials. In this case: Federating the directory uses the existing identity instead of a new set of AWS credentials.
- **B:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: Federating the directory uses the existing identity instead of a new set of AWS credentials.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Federating the directory uses the existing identity instead of a new set of AWS credentials.
- **D:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: Federating the directory uses the existing identity instead of a new set of AWS credentials.

### Question 23 — D

Answer: Use a security group as a stateful instance firewall. A security group allows only that range and drops everything else at the instance. The group allows inbound or outbound traffic and remembers the connection state. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: A security group allows only that range and drops everything else at the instance.
- **B:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: A security group allows only that range and drops everything else at the instance.
- **C:** Incorrect for this question. An open perimeter exposes every service on the host, including ones nobody meant to publish. Why the correct answer wins: A security group allows only that range and drops everything else at the instance.
- **D:** Correct. The group allows inbound or outbound traffic and remembers the connection state. In this case: A security group allows only that range and drops everything else at the instance.

### Question 24 — B, D

Answers: Use AWS WAF to block web attack patterns; Use AWS Shield for DDoS protection. WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Shield absorbs distributed denial-of-service traffic before it reaches the application. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application.
- **B:** Correct. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. In this case: WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application.
- **C:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application.
- **D:** Correct. Shield absorbs distributed denial-of-service traffic before it reaches the application. In this case: WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application.
- **E:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: WAF inspects the HTTP request for attack patterns, and Shield absorbs the flood before it reaches the application.

### Question 25 — C

Answer: Encrypt data in transit with TLS. Encryption in transit with TLS protects the upload while it crosses the network. Traffic is protected while it crosses the network, not only while it sits on disk. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: Encryption in transit with TLS protects the upload while it crosses the network.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: Encryption in transit with TLS protects the upload while it crosses the network.
- **C:** Correct. Traffic is protected while it crosses the network, not only while it sits on disk. In this case: Encryption in transit with TLS protects the upload while it crosses the network.
- **D:** Incorrect for this question. The customer controls the key policy and can revoke access by disabling the key. Why the correct answer wins: Encryption in transit with TLS protects the upload while it crosses the network.

### Question 26 — D

Answer: Use a customer managed key for the required control. A customer managed key lets the university control the key policy and disable it to revoke access. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: A customer managed key lets the university control the key policy and disable it to revoke access.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A customer managed key lets the university control the key policy and disable it to revoke access.
- **C:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: A customer managed key lets the university control the key policy and disable it to revoke access.
- **D:** Correct. In this case: A customer managed key lets the university control the key policy and disable it to revoke access.

### Question 27 — C

Answer: Store the database credential in AWS Secrets Manager and rotate it. A managed secret store holds the credential and rotates it on a schedule. The secret is held centrally and can be rotated on a schedule. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A managed secret store holds the credential and rotates it on a schedule.
- **B:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: A managed secret store holds the credential and rotates it on a schedule.
- **C:** Correct. The secret is held centrally and can be rotated on a schedule. In this case: A managed secret store holds the credential and rotates it on a schedule.
- **D:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: A managed secret store holds the credential and rotates it on a schedule.

### Question 28 — B

Answer: Use Amazon Macie to find sensitive data in Amazon S3. Macie classifies objects and reports where sensitive data is stored. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Macie classifies objects and reports where sensitive data is stored.
- **B:** Correct. In this case: Macie classifies objects and reports where sensitive data is stored.
- **C:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Macie classifies objects and reports where sensitive data is stored.
- **D:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Macie classifies objects and reports where sensitive data is stored.

### Question 29 — B, E

Answers: Use Amazon Inspector to scan workloads for vulnerabilities; Use Amazon GuardDuty to detect suspicious activity. Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. GuardDuty analyses account, network and DNS activity for signs of compromise. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Security Hub collects findings from the security services and scores them against a standard. Why the correct answer wins: Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding.
- **B:** Correct. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. In this case: Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding.
- **D:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding.
- **E:** Correct. GuardDuty analyses account, network and DNS activity for signs of compromise. In this case: Inspector reports the vulnerabilities, and GuardDuty raises the compromise finding.

### Question 30 — B

Answer: Classify the data and tag each store by sensitivity. A classification decides which controls and retention rules apply to each dataset. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.
- **B:** Correct. In this case: A classification decides which controls and retention rules apply to each dataset.
- **C:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.
- **D:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: A classification decides which controls and retention rules apply to each dataset.

### Question 31 — A

Answer: Set an S3 lifecycle rule to expire old objects. A lifecycle rule deletes the objects automatically once they reach the stated age. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **B:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **D:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.

### Question 32 — B

Answer: Use AWS Audit Manager to collect evidence for an audit. Audit Manager assembles evidence against the chosen framework. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Audit Manager assembles evidence against the chosen framework.
- **B:** Correct. In this case: Audit Manager assembles evidence against the chosen framework.
- **C:** Incorrect for this question. Artifact provides AWS audit reports and agreements on demand. Why the correct answer wins: Audit Manager assembles evidence against the chosen framework.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Audit Manager assembles evidence against the chosen framework.

### Question 33 — B, E

Answers: Read the security checks in AWS Trusted Advisor; Use AWS CloudTrail to record API activity. Trusted Advisor reports insecure settings, and CloudTrail records the API activity. Trusted Advisor inspects the account and reports insecure or wasteful settings. CloudTrail logs who called which API, when and from where. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Trusted Advisor reports insecure settings, and CloudTrail records the API activity.
- **B:** Correct. Trusted Advisor inspects the account and reports insecure or wasteful settings. In this case: Trusted Advisor reports insecure settings, and CloudTrail records the API activity.
- **C:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Trusted Advisor reports insecure settings, and CloudTrail records the API activity.
- **D:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Trusted Advisor reports insecure settings, and CloudTrail records the API activity.
- **E:** Correct. CloudTrail logs who called which API, when and from where. In this case: Trusted Advisor reports insecure settings, and CloudTrail records the API activity.

### Question 34 — C

Answer: The customer is responsible for configuring IAM permissions. Identity and access configuration is a customer responsibility in every service model. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: Identity and access configuration is a customer responsibility in every service model.
- **B:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Identity and access configuration is a customer responsibility in every service model.
- **C:** Correct. In this case: Identity and access configuration is a customer responsibility in every service model.
- **D:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Identity and access configuration is a customer responsibility in every service model.

### Question 35 — C

Answer: Apply a service control policy in AWS Organizations. A service control policy caps the permissions of every account beneath it, including the Regions it may use. An SCP sets the maximum permissions available to the accounts under it. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: A service control policy caps the permissions of every account beneath it, including the Regions it may use.
- **B:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A service control policy caps the permissions of every account beneath it, including the Regions it may use.
- **C:** Correct. An SCP sets the maximum permissions available to the accounts under it. In this case: A service control policy caps the permissions of every account beneath it, including the Regions it may use.
- **D:** Incorrect for this question. An SCP only limits permissions; it never grants them. Why the correct answer wins: A service control policy caps the permissions of every account beneath it, including the Regions it may use.

### Question 36 — C

Answer: AWS Lambda. Lambda runs the work per upload and keeps nothing running in between. Run code on an event without provisioning or managing a server. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Lambda runs the work per upload and keeps nothing running in between.
- **B:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: Lambda runs the work per upload and keeps nothing running in between.
- **C:** Correct. Run code on an event without provisioning or managing a server. In this case: Lambda runs the work per upload and keeps nothing running in between.
- **D:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lambda runs the work per upload and keeps nothing running in between.

### Question 37 — A

Answer: Amazon ECS or Amazon EKS with AWS Fargate. Managed container orchestration runs the containers while the platform owns the hosts. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Managed container orchestration runs the containers while the platform owns the hosts.
- **B:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **D:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.

### Question 38 — D

Answer: Amazon S3 Standard-IA. Standard-IA is priced for rarely read data that must still be available at once. Object storage for data that is accessed less often but must be available immediately. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: Standard-IA is priced for rarely read data that must still be available at once.
- **B:** Incorrect for this question. Object storage for frequently accessed data with high durability and availability. Why the correct answer wins: Standard-IA is priced for rarely read data that must still be available at once.
- **C:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: Standard-IA is priced for rarely read data that must still be available at once.
- **D:** Correct. Object storage for data that is accessed less often but must be available immediately. In this case: Standard-IA is priced for rarely read data that must still be available at once.

### Question 39 — A, E

Answers: AWS Snowball devices; Amazon S3 Glacier storage classes. Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards. Physical devices that move large datasets into AWS when the network is the bottleneck. Archive storage for data that is rarely read and tolerates retrieval time. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Archive storage for data that is rarely read and tolerates retrieval time. In this case: Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards.
- **B:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards.
- **D:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards.
- **E:** Correct. Physical devices that move large datasets into AWS when the network is the bottleneck. In this case: Snowball moves the bulk data physically, and an archive class holds it at low cost afterwards.

### Question 40 — C

Answer: Amazon DynamoDB. DynamoDB is a managed key-value store built for high-volume, predictable-latency reads. A managed key-value and document store for high-volume, predictable-latency access. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency reads.
- **B:** Incorrect for this question. A managed in-memory cache for sub-millisecond reads of hot data. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency reads.
- **C:** Correct. A managed key-value and document store for high-volume, predictable-latency access. In this case: DynamoDB is a managed key-value store built for high-volume, predictable-latency reads.
- **D:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency reads.

### Question 41 — C

Answer: Amazon Redshift. A managed data warehouse is built for analytical queries over large datasets. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.
- **B:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.
- **C:** Correct. In this case: A managed data warehouse is built for analytical queries over large datasets.
- **D:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.

### Question 42 — C

Answer: AWS Global Accelerator. Global Accelerator routes users to the closest healthy endpoint using anycast addresses. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: Global Accelerator routes users to the closest healthy endpoint using anycast addresses.
- **B:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Global Accelerator routes users to the closest healthy endpoint using anycast addresses.
- **C:** Correct. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. In this case: Global Accelerator routes users to the closest healthy endpoint using anycast addresses.
- **D:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: Global Accelerator routes users to the closest healthy endpoint using anycast addresses.

### Question 43 — A, D

Answers: Amazon Route 53; Elastic Load Balancing. Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets. A managed DNS service that also supports health checks and routing policies. Distributes incoming traffic across multiple targets in one or more Availability Zones. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Distributes incoming traffic across multiple targets in one or more Availability Zones. In this case: Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets.
- **B:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets.
- **C:** Incorrect for this question. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Why the correct answer wins: Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets.
- **D:** Correct. A managed DNS service that also supports health checks and routing policies. In this case: Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets.
- **E:** Incorrect for this question. A managed front door for APIs with throttling, authorisation and usage plans. Why the correct answer wins: Route 53 handles the DNS failover, and Elastic Load Balancing spreads traffic across the targets.

### Question 44 — C

Answer: AWS Systems Manager. Systems Manager applies the patches and reports compliance across managed nodes. Operations tooling for patching, running commands and inventory across managed nodes. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.
- **C:** Correct. Operations tooling for patching, running commands and inventory across managed nodes. In this case: Systems Manager applies the patches and reports compliance across managed nodes.
- **D:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.

### Question 45 — A

Answer: AWS Service Catalog. Service Catalog publishes the approved products that teams can launch on their own. A curated catalogue of approved products that teams can launch themselves. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A curated catalogue of approved products that teams can launch themselves. In this case: Service Catalog publishes the approved products that teams can launch on their own.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Service Catalog publishes the approved products that teams can launch on their own.
- **C:** Incorrect for this question. Operations tooling for patching, running commands and inventory across managed nodes. Why the correct answer wins: Service Catalog publishes the approved products that teams can launch on their own.
- **D:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: Service Catalog publishes the approved products that teams can launch on their own.

### Question 46 — A

Answer: Amazon SQS. A queue holds the submissions until the marking service catches up. A managed queue that decouples producers from consumers and buffers bursts. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed queue that decouples producers from consumers and buffers bursts. In this case: A queue holds the submissions until the marking service catches up.
- **B:** Incorrect for this question. A state machine that coordinates multi-step workflows with retries and branching. Why the correct answer wins: A queue holds the submissions until the marking service catches up.
- **C:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: A queue holds the submissions until the marking service catches up.
- **D:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: A queue holds the submissions until the marking service catches up.

### Question 47 — C, E

Answers: AWS Step Functions; Amazon EventBridge. Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change. A state machine that coordinates multi-step workflows with retries and branching. An event bus that routes events from AWS services and applications to targets by rule. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change.
- **B:** Incorrect for this question. Streaming data ingestion and processing for continuous records. Why the correct answer wins: Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change.
- **C:** Correct. A state machine that coordinates multi-step workflows with retries and branching. In this case: Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change.
- **D:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change.
- **E:** Correct. An event bus that routes events from AWS services and applications to targets by rule. In this case: Step Functions coordinates the ordered steps, and EventBridge starts the workflow on the state change.

### Question 48 — D

Answer: Amazon Bedrock. Bedrock exposes foundation models through an API so the team never runs the model hosts. Access foundation models through an API without operating the model infrastructure. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **B:** Incorrect for this question. Build, train and deploy machine learning models through a managed platform. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **C:** Incorrect for this question. A managed business intelligence service for dashboards and reports. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **D:** Correct. Access foundation models through an API without operating the model infrastructure. In this case: Bedrock exposes foundation models through an API so the team never runs the model hosts.

### Question 49 — D

Answer: Amazon Athena. Athena queries the objects in place with SQL and no infrastructure to run. Query data in Amazon S3 with SQL and no infrastructure to manage. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **B:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **C:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **D:** Correct. Query data in Amazon S3 with SQL and no infrastructure to manage. In this case: Athena queries the objects in place with SQL and no infrastructure to run.

### Question 50 — B

Answer: AWS Cloud9. Cloud9 provides a browser-based integrated development environment. A cloud-based integrated development environment that runs in the browser. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: Cloud9 provides a browser-based integrated development environment.
- **B:** Correct. A cloud-based integrated development environment that runs in the browser. In this case: Cloud9 provides a browser-based integrated development environment.
- **C:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: Cloud9 provides a browser-based integrated development environment.
- **D:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: Cloud9 provides a browser-based integrated development environment.

### Question 51 — D

Answer: AWS CodeBuild. CodeBuild runs the compile and test steps in a managed build environment. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **C:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **D:** Correct. In this case: CodeBuild runs the compile and test steps in a managed build environment.

### Question 52 — B

Answer: AWS Elastic Beanstalk. Elastic Beanstalk provisions and manages the environment around the uploaded application. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **B:** Correct. In this case: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **D:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.

### Question 53 — B

Answer: AWS Service Catalog. Service Catalog offers the approved template as a launchable product. A curated catalogue of approved products that teams can launch themselves. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Service Catalog offers the approved template as a launchable product.
- **B:** Correct. A curated catalogue of approved products that teams can launch themselves. In this case: Service Catalog offers the approved template as a launchable product.
- **C:** Incorrect for this question. Operations tooling for patching, running commands and inventory across managed nodes. Why the correct answer wins: Service Catalog offers the approved template as a launchable product.
- **D:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: Service Catalog offers the approved template as a launchable product.

### Question 54 — A

Answer: Amazon CloudWatch. CloudWatch holds the metric and evaluates the alarm against it. Metrics, logs and alarms for the resources and applications in the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch holds the metric and evaluates the alarm against it.
- **B:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **D:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.

### Question 55 — A, D

Answers: AWS X-Ray; AWS Health Dashboard. X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents. Traces requests through a distributed application to find where time is spent. Service health and event notifications that affect the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Service health and event notifications that affect the account. In this case: X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents.
- **B:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents.
- **C:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents.
- **D:** Correct. Traces requests through a distributed application to find where time is spent. In this case: X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents.
- **E:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: X-Ray attributes the time to each component, and the Health Dashboard publishes the AWS-side incidents.

### Question 56 — D

Answer: AWS Storage Gateway. Storage Gateway provides the local file interface with an AWS-backed copy. A hybrid file, volume or tape interface that keeps frequently used data on premises. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: Storage Gateway provides the local file interface with an AWS-backed copy.
- **B:** Incorrect for this question. Physical devices that move large datasets into AWS when the network is the bottleneck. Why the correct answer wins: Storage Gateway provides the local file interface with an AWS-backed copy.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: Storage Gateway provides the local file interface with an AWS-backed copy.
- **D:** Correct. A hybrid file, volume or tape interface that keeps frequently used data on premises. In this case: Storage Gateway provides the local file interface with an AWS-backed copy.

### Question 57 — B

Answer: AWS PrivateLink. PrivateLink provides a private endpoint inside the VPC for the partner service. Private connectivity to a service through an endpoint inside the VPC. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A central router that connects many VPCs and on-premises networks. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the partner service.
- **B:** Correct. Private connectivity to a service through an endpoint inside the VPC. In this case: PrivateLink provides a private endpoint inside the VPC for the partner service.
- **C:** Incorrect for this question. A logically isolated virtual network in which the customer places its resources. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the partner service.
- **D:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: PrivateLink provides a private endpoint inside the VPC for the partner service.

### Question 58 — B

Answer: On-Demand Instances. On-Demand capacity is billed as it is used with no commitment to forecast around. Capacity billed by the second or hour with no commitment. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment to forecast around.
- **B:** Correct. Capacity billed by the second or hour with no commitment. In this case: On-Demand capacity is billed as it is used with no commitment to forecast around.
- **C:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment to forecast around.
- **D:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: On-Demand capacity is billed as it is used with no commitment to forecast around.

### Question 59 — A

Answer: Spot Instances. Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **B:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **C:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **D:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.

### Question 60 — B

Answer: AWS Budgets. Budgets tracks spend against a threshold and alerts when it is crossed. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **B:** Correct. In this case: Budgets tracks spend against a threshold and alerts when it is crossed.
- **C:** Incorrect for this question. Estimate the cost of a planned architecture before it is built. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **D:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.

### Question 61 — B, D

Answers: AWS Cost Explorer; AWS Cost and Usage Report. Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items. Visualise and analyse past spend and forecast what is coming. The most granular billing dataset, delivered to a bucket for analysis. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items.
- **B:** Correct. The most granular billing dataset, delivered to a bucket for analysis. In this case: Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items.
- **C:** Incorrect for this question. Machine learning alerts on spending that deviates from the expected pattern. Why the correct answer wins: Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items.
- **D:** Correct. Visualise and analyse past spend and forecast what is coming. In this case: Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items.
- **E:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: Cost Explorer breaks spend down by service, and the Cost and Usage Report provides the line items.

### Question 62 — B

Answer: Tag resources and activate cost allocation tags. Activated cost allocation tags split the single bill by faculty or cost centre. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Activated cost allocation tags split the single bill by faculty or cost centre.
- **B:** Correct. In this case: Activated cost allocation tags split the single bill by faculty or cost centre.
- **C:** Incorrect for this question. One bill for all accounts, with usage aggregated so volume discounts are shared. Why the correct answer wins: Activated cost allocation tags split the single bill by faculty or cost centre.
- **D:** Incorrect for this question. Separate accounts do not pool usage, so each misses the discounts the total would earn. Why the correct answer wins: Activated cost allocation tags split the single bill by faculty or cost centre.

### Question 63 — A

Answer: A designated Technical Account Manager. A designated technical account manager comes with Enterprise Support. A named advisor who understands the account and helps with planning and escalation. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A named advisor who understands the account and helps with planning and escalation. In this case: A designated technical account manager comes with Enterprise Support.
- **B:** Incorrect for this question. Account and billing support with documentation and health checks, at no charge. Why the correct answer wins: A designated technical account manager comes with Enterprise Support.
- **C:** Incorrect for this question. Business-hours email support for development and test workloads. Why the correct answer wins: A designated technical account manager comes with Enterprise Support.
- **D:** Incorrect for this question. Production support with 24/7 access, faster response and Trusted Advisor checks. Why the correct answer wins: A designated technical account manager comes with Enterprise Support.

### Question 64 — A

Answer: Buy the software through AWS Marketplace. AWS Marketplace purchases are billed through AWS and can draw on committed spend. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: AWS Marketplace purchases are billed through AWS and can draw on committed spend.
- **B:** Incorrect for this question. The reference documentation states what a service does and how it is configured. Why the correct answer wins: AWS Marketplace purchases are billed through AWS and can draw on committed spend.
- **C:** Incorrect for this question. The community knowledge base holds answers to common service and account questions. Why the correct answer wins: AWS Marketplace purchases are billed through AWS and can draw on committed spend.
- **D:** Incorrect for this question. A vetted reference architecture shortens design work for a common workload. Why the correct answer wins: AWS Marketplace purchases are billed through AWS and can draw on committed spend.

### Question 65 — D

Answer: The AWS Free Tier allowances. The Free Tier publishes monthly allowances for eligible services on a qualifying account. Limited monthly usage at no charge for eligible services on a new or qualifying account. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **B:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **C:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **D:** Correct. Limited monthly usage at no charge for eligible services on a new or qualifying account. In this case: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
