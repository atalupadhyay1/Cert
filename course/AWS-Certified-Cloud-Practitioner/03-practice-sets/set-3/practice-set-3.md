# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 3

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. A freight forwarder wins contracts in five countries in one quarter and needs its tracking portal served there without building anything locally. Which cloud benefit does this depend on?

- A. Global reach: deploy into multiple Regions quickly
- B. Keep ownership of the physical data centre
- C. Elasticity: scale capacity with demand
- D. Buy servers up front and depreciate them

### 2. A cold-chain monitoring platform cannot afford gaps in temperature data when a disk or a host fails. Which cloud benefit addresses that requirement?

- A. A flat monthly fee that does not change with usage
- B. Reliability through managed, redundant infrastructure
- C. Stop spending on undifferentiated heavy lifting
- D. Buy servers up front and depreciate them

### 3. A distributor's finance director describes buying servers every four years and writing them down over that period. Which spending model is being described?

- A. Volume discounts that grow with usage
- B. Pay only for what is consumed each month
- C. Pay-as-you-go pricing
- D. Buy servers up front and depreciate them

### 4. A warehouse platform vendor quotes the same monthly amount whether the system processes ten orders or ten thousand. Which pricing model is the quote using?

- A. Pay-as-you-go pricing
- B. On-Demand Instances
- C. Volume discounts that grow with usage
- D. A flat monthly fee that does not change with usage

### 5. Parcel scans are lost whenever the label-printing service stalls, because the scanner posts to it directly and waits. Which design principle would stop the loss?

- A. Direct synchronous calls between every tier
- B. Deploy across multiple Availability Zones
- C. Loose coupling with a queue between tiers
- D. Scale the single monolith vertically only

### 6. A depot application has been moved to a larger server every year and has now reached the largest size the provider offers. Which approach has been taken to its limit?

- A. Scale out automatically as demand rises
- B. Scale the single monolith vertically only
- C. Break the application into small independent services
- D. Deploy across multiple Availability Zones

### 7. A review must show that routine changes are automated, reversible and tested before release. Which Well-Architected pillar covers that?

- A. Performance efficiency pillar
- B. Cost optimization pillar
- C. Security pillar
- D. Operational excellence pillar

### 8. A team must record its answers against every pillar in a repeatable way and must also demonstrate that the workload recovers from failure. Which two apply? Select two.

- A. Reliability pillar
- B. Cost optimization pillar
- C. Review the workload against the Well-Architected Tool
- D. Sustainability pillar
- E. Security pillar

### 9. A logistics group needs an agreed technical architecture and a landing zone before teams start building. Which Cloud Adoption Framework perspective delivers it?

- A. People perspective of the AWS Cloud Adoption Framework
- B. Platform perspective of the AWS Cloud Adoption Framework
- C. Business perspective of the AWS Cloud Adoption Framework
- D. Governance perspective of the AWS Cloud Adoption Framework

### 10. Six months after migration a manufacturer has no runbooks, no monitoring ownership and no support model. Which perspective has been neglected?

- A. Operations perspective of the AWS Cloud Adoption Framework
- B. Business perspective of the AWS Cloud Adoption Framework
- C. Platform perspective of the AWS Cloud Adoption Framework
- D. Governance perspective of the AWS Cloud Adoption Framework

### 11. A manufacturer wants to move its whole VMware estate to a cloud-hosted equivalent without changing any application. Which strategy is this?

- A. Relocate: move the platform to a cloud-native equivalent
- B. Rehost: move the application as it is
- C. Retain: keep the workload where it is
- D. Refactor: redesign the application for cloud architecture

### 12. A supplier portal has had no logins for two years and is being switched off entirely. Which migration strategy applies?

- A. Repurchase: move to a different product
- B. Rehost: move the application as it is
- C. Retire: switch the workload off
- D. Retain: keep the workload where it is

### 13. An assembly-line analytics service needs single-digit millisecond responses in a city that has no AWS Region. Which infrastructure option fits?

- A. Local Zones for very low latency
- B. Edge locations for content delivery
- C. AWS Wavelength for carrier networks
- D. AWS Outposts for on-premises capacity

### 14. Parcel volume triples in the weeks before the holidays and returns to normal in January, and capacity should follow without a purchase order. What should be configured?

- A. Place everything in one Availability Zone
- B. Scale out automatically as demand rises
- C. Scale the single monolith vertically only
- D. Direct synchronous calls between every tier

### 15. A depot system must keep accepting scans while a downstream service is slow, and must grow automatically during the pre-holiday peak. Which two choices fit? Select two.

- A. Place everything in one Availability Zone
- B. Scale the single monolith vertically only
- C. Loose coupling with a queue between tiers
- D. Scale out automatically as demand rises
- E. Direct synchronous calls between every tier

### 16. A warehouse platform uses several AWS services and the auditor asks who decides which staff may read which data. Under the shared responsibility model, who?

- A. The customer is responsible for configuring IAM permissions
- B. The customer is responsible for the data-centre building
- C. AWS is responsible for the physical facilities and hardware
- D. AWS is responsible for patching a managed service such as Amazon S3

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. A dashboard vendor asks for administrator rights to avoid future permission problems. What should be granted instead?

- A. Share the root credentials with the operations team
- B. Give every engineer administrator access for convenience
- C. Create an IAM user with long-lived credentials
- D. Grant only the permissions the task needs

### 18. Thirty contractors must each have their own AWS identity so that every action is attributed to a person. What should be created for each of them?

- A. Share the root credentials with the operations team
- B. Create an IAM role and let the workload assume it
- C. Put the users in a group and attach the policy to the group
- D. Create an IAM user with long-lived credentials

### 19. A founder keeps the only AWS account and signs in as root occasionally when something needs attention. What is the minimum protection for that identity?

- A. Use the root user for daily administration
- B. Enable MFA and delete the root access keys
- C. Share the root credentials with the operations team
- D. Attach a JSON policy that allows only the required actions

### 20. An auditor asks for proof that programmatic credentials are replaced on a defined schedule. What provides that evidence?

- A. Grant only the permissions the task needs
- B. Rotate access keys on a schedule
- C. Require multi-factor authentication
- D. Enable MFA and delete the root access keys

### 21. A group with forty accounts wants one sign-in for employees and a defined permission set per account. Which service fits?

- A. Put the users in a group and attach the policy to the group
- B. Create an IAM user with long-lived credentials
- C. Use IAM Identity Center for workforce sign-in
- D. Use Amazon Cognito for customer sign-in

### 22. A function must write messages to a queue without any credential being stored in its configuration. What should it use?

- A. Put the password in the application source code
- B. Create an IAM role and let the workload assume it
- C. Create an IAM user with long-lived credentials
- D. Federate the company directory into AWS

### 23. Web servers behind a load balancer must accept traffic only from that balancer on port 443. What should be applied to the servers?

- A. Open every port to the internet and rely on the application
- B. Use AWS WAF to block web attack patterns
- C. Use a security group as a stateful instance firewall
- D. Use a network ACL as a stateless subnet filter

### 24. A hostile address range must be dropped at the subnet boundary, and traffic leaving the VPC must be inspected for command-and-control callbacks. Which two controls fit? Select two.

- A. Use a security group as a stateful instance firewall
- B. Use AWS WAF to block web attack patterns
- C. Use AWS Shield for DDoS protection
- D. Use AWS Network Firewall for VPC-level inspection
- E. Use a network ACL as a stateless subnet filter

### 25. Service calls between two VPCs cross a shared network path and must be unreadable to anything watching that path. What is required?

- A. Encrypt data in transit with TLS
- B. Set a retention period and delete expired copies
- C. Use AWS Certificate Manager for TLS certificates
- D. Rely on server-side encryption with Amazon S3 managed keys

### 26. A data-lake bucket must encrypt every new object automatically without any change to the writing application. What fits?

- A. Encrypt data in transit with TLS
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Use a customer managed key for the required control
- D. Use AWS KMS to create and control encryption keys

### 27. A review finds a supplier API password committed to a shared code repository and copied into three environments. Which practice caused this exposure?

- A. Use AWS KMS to create and control encryption keys
- B. Use AWS Certificate Manager for TLS certificates
- C. Put the password in the application source code
- D. Store the database credential in AWS Secrets Manager and rotate it

### 28. Container images and instances must be checked for known software vulnerabilities before each release. Which service fits?

- A. Use Amazon Macie to find sensitive data in Amazon S3
- B. Use AWS Security Hub to aggregate findings in one place
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use Amazon Inspector to scan workloads for vulnerabilities

### 29. Findings from several detection services and many accounts must be aggregated, and instances must be scanned for missing patches. Which two services fit? Select two.

- A. Use Amazon GuardDuty to detect suspicious activity
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use AWS CloudTrail to record API activity
- D. Use Amazon Inspector to scan workloads for vulnerabilities
- E. Use AWS Security Hub to aggregate findings in one place

### 30. A depot's operational data must be recoverable to a defined point after accidental deletion across several services. Which service fits?

- A. An Amazon S3 bucket policy that grants public read
- B. Set an S3 lifecycle rule to expire old objects
- C. AWS Backup
- D. Set a retention period and delete expired copies

### 31. A regulator requires that each record class be kept for a stated period and then deleted. What must be defined?

- A. An Amazon S3 bucket policy that grants public read
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Set a retention period and delete expired copies
- D. AWS Backup

### 32. An investigation must show which identity deleted a bucket and from which address at three in the morning. Which service holds that evidence?

- A. Use AWS Config to record resource configuration changes
- B. Use AWS CloudTrail to record API activity
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use Amazon Macie to find sensitive data in Amazon S3

### 33. Evidence must include each resource's configuration history and be assembled against a framework for an external auditor. Which two services fit? Select two.

- A. Read the security checks in AWS Trusted Advisor
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use AWS Audit Manager to collect evidence for an audit
- D. Use AWS CloudTrail to record API activity
- E. Use AWS Config to record resource configuration changes

### 34. A review asks who maintains the physical network fabric that connects Availability Zones inside a Region. Under the shared responsibility model, who?

- A. AWS is responsible for the physical facilities and hardware
- B. The customer is responsible for the data it stores in AWS
- C. The customer is responsible for the data-centre building
- D. The customer is responsible for configuring IAM permissions

### 35. An administrator wants a guarantee that no account in the organisation can turn off its audit logging. What should be applied?

- A. Apply a service control policy in AWS Organizations
- B. Attach a JSON policy that allows only the required actions
- C. Use AWS Config to record resource configuration changes
- D. Use a service control policy to grant permissions to a team

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. Every barcode scan must trigger a short lookup and a write, and there is no capacity to keep running between scans. Which compute service fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. AWS Lambda
- C. Amazon EC2 instances
- D. AWS Batch

### 37. A route-simulation package needs a specific GPU driver and full control of the operating system. Which compute service fits?

- A. Amazon ECS or Amazon EKS with AWS Fargate
- B. AWS Lambda
- C. AWS App Runner
- D. Amazon EC2 instances

### 38. Shipping documents are opened many times a day and must be durable and available without any server to manage. Which storage fits?

- A. Amazon S3 Glacier storage classes
- B. Amazon EBS volumes
- C. Amazon S3 Standard
- D. Amazon S3 Standard-IA

### 39. Database volumes need block storage that persists with the instance, and every supported resource needs centralised scheduled backups. Which two services fit? Select two.

- A. AWS Backup
- B. AWS Snowball devices
- C. Amazon S3 Glacier storage classes
- D. Amazon EBS volumes
- E. Amazon EFS file system

### 40. Analysts must query billions of historical shipment rows with complex joins and aggregations. Which service fits?

- A. Amazon Redshift
- B. Amazon ElastiCache
- C. Amazon RDS
- D. Amazon DynamoDB

### 41. An existing application uses MongoDB drivers and the team wants a managed compatible service. Which service fits?

- A. Amazon DynamoDB
- B. Amazon RDS
- C. Amazon DocumentDB
- D. Amazon Neptune

### 42. A public domain needs hosted DNS records and failover to a secondary endpoint when a health check fails. Which service fits?

- A. Elastic Load Balancing
- B. Amazon Route 53
- C. Amazon CloudFront
- D. AWS Global Accelerator

### 43. An API needs throttling and per-customer usage plans, and users on three continents must reach the closest healthy endpoint. Which two services fit? Select two.

- A. AWS Global Accelerator
- B. Amazon API Gateway
- C. Amazon CloudFront
- D. Elastic Load Balancing
- E. Amazon Route 53

### 44. A new depot must be built with exactly the same resources as the first one, from a stored definition. Which service fits?

- A. AWS Systems Manager
- B. AWS Service Catalog
- C. AWS Control Tower
- D. AWS CloudFormation

### 45. An operator wants metrics, logs and alarms for queues, functions and databases in one place. Which service fits?

- A. Use AWS Config to record resource configuration changes
- B. Amazon CloudWatch
- C. Use AWS CloudTrail to record API activity
- D. AWS Health Dashboard

### 46. One shipment exception must reach an email list, a chat channel and a mobile push at the same time. Which service fits?

- A. Amazon SNS
- B. Amazon SQS
- C. Amazon EventBridge
- D. AWS Step Functions

### 47. Work must be buffered so a slow consumer does not lose jobs, and AWS service state changes must be routed to targets by rule. Which two services fit? Select two.

- A. Amazon MQ
- B. Amazon EventBridge
- C. Amazon Kinesis
- D. Amazon SQS
- E. Amazon SNS

### 48. Data from six source systems must be catalogued and transformed before analysts can query it. Which service fits?

- A. Amazon QuickSight
- B. AWS Glue
- C. Amazon EMR
- D. Amazon Athena

### 49. A team wants managed Spark clusters to process very large files with custom libraries. Which service fits?

- A. Amazon EMR
- B. AWS Glue
- C. Amazon Redshift
- D. Amazon Athena

### 50. Every pull request must compile and run the unit tests in a clean managed environment. Which service performs that work?

- A. AWS CodePipeline
- B. AWS CloudFormation
- C. AWS CodeDeploy
- D. AWS CodeBuild

### 51. An auditor wants a record of which release passed each stage and who approved the production step. Which service holds that record?

- A. AWS CodePipeline
- B. AWS CodeDeploy
- C. AWS CodeBuild
- D. AWS X-Ray

### 52. A PHP application needs a managed environment with capacity, load balancing and platform updates handled for it. Which service fits?

- A. AWS Elastic Beanstalk
- B. AWS Lambda
- C. Amazon EC2 instances
- D. Amazon ECS or Amazon EKS with AWS Fargate

### 53. A container image must run as an internal web service with no cluster and no scaling rules written by the team. Which service fits?

- A. AWS Elastic Beanstalk
- B. AWS Batch
- C. AWS App Runner
- D. Amazon EC2 instances

### 54. An alarm must fire when the queue depth stays above a threshold for fifteen minutes. Which service provides the metric and the alarm?

- A. Use AWS Config to record resource configuration changes
- B. AWS Trusted Advisor
- C. Amazon CloudWatch
- D. Use AWS CloudTrail to record API activity

### 55. A depot team needs alarms on its own business metrics and separate notice when an AWS service event affects the account. Which two services fit? Select two.

- A. Amazon CloudWatch
- B. AWS Health Dashboard
- C. AWS X-Ray
- D. Use AWS CloudTrail to record API activity
- E. AWS Trusted Advisor

### 56. Twenty VPCs and two on-premises networks must be connected through one central router. Which service fits?

- A. AWS Direct Connect
- B. Amazon VPC
- C. AWS PrivateLink
- D. AWS Transit Gateway

### 57. A manufacturer must keep a local tape and file interface on the factory site while a copy lives in AWS. Which service fits?

- A. AWS Snowball devices
- B. AWS Storage Gateway
- C. AWS Backup
- D. Amazon EFS file system

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. A warehouse application runs at steady load all year and the CFO will commit for one year to get a lower rate. Which option fits?

- A. On-Demand Instances
- B. Spot Instances
- C. Savings Plans
- D. Reserved Instances

### 59. A new depot opens next month and the load is unknown, and no commitment is acceptable yet. Which option fits?

- A. Reserved Instances
- B. Dedicated Hosts
- C. On-Demand Instances
- D. Spot Instances

### 60. A solution must be costed before it is built so the board can approve a budget. Which tool fits?

- A. AWS Cost and Usage Report
- B. AWS Budgets
- C. AWS Cost Explorer
- D. AWS Pricing Calculator

### 61. Finance needs the most granular billing dataset for its own model and automatic warning when spend departs from its normal pattern. Which two tools fit? Select two.

- A. AWS Budgets
- B. Wait for the monthly invoice and reconcile it afterwards
- C. AWS Cost Explorer
- D. AWS Cost and Usage Report
- E. Cost Anomaly Detection

### 62. Twenty accounts share one bill and each department must see its own share of that bill. What should be applied?

- A. Tag resources and activate cost allocation tags
- B. Consolidated billing in AWS Organizations
- C. AWS Cost and Usage Report
- D. Keep a separate bill and separate discounts per account

### 63. A test environment needs business-hours email access to technical support at the lowest paid tier. Which plan fits?

- A. AWS Enterprise Support
- B. AWS Business Support
- C. AWS Developer Support
- D. AWS Basic Support

### 64. An engineer needs the authoritative statement of what a service limit is and which parameters an API accepts. Where should it be read?

- A. Start from an AWS Solutions Library reference deployment
- B. Search AWS re:Post for an answered question
- C. Read the AWS documentation and service user guides
- D. Engage an AWS Partner for the delivery work

### 65. Fault-tolerant route optimisation can restart at any time and should cost as little as possible per hour. Which option fits?

- A. Volume discounts that grow with usage
- B. The AWS Free Tier allowances
- C. Savings Plans
- D. Spot Instances

---

## Answer key and explanations

### Question 1 — A

Answer: Global reach: deploy into multiple Regions quickly. Regions and edge locations let the forwarder serve each country without owning facilities in it. A global infrastructure lets a company put workloads near its users without building facilities. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A global infrastructure lets a company put workloads near its users without building facilities. In this case: Regions and edge locations let the forwarder serve each country without owning facilities in it.
- **B:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Regions and edge locations let the forwarder serve each country without owning facilities in it.
- **C:** Incorrect for this question. Capacity is added and removed as demand changes, so the company pays only for what it uses. Why the correct answer wins: Regions and edge locations let the forwarder serve each country without owning facilities in it.
- **D:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Regions and edge locations let the forwarder serve each country without owning facilities in it.

### Question 2 — B

Answer: Reliability through managed, redundant infrastructure. Managed, redundant infrastructure removes single points of failure that the company would otherwise engineer itself. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Managed, redundant infrastructure removes single points of failure that the company would otherwise engineer itself.
- **B:** Correct. In this case: Managed, redundant infrastructure removes single points of failure that the company would otherwise engineer itself.
- **C:** Incorrect for this question. AWS operates the facilities, hardware and managed platforms so the team can focus on its product. Why the correct answer wins: Managed, redundant infrastructure removes single points of failure that the company would otherwise engineer itself.
- **D:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Managed, redundant infrastructure removes single points of failure that the company would otherwise engineer itself.

### Question 3 — D

Answer: Buy servers up front and depreciate them. Capital expense pays for hardware before it is used and carries depreciation and refresh risk. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: Capital expense pays for hardware before it is used and carries depreciation and refresh risk.
- **B:** Incorrect for this question. Costs follow usage, so the bill rises and falls with demand rather than with a purchase decision. Why the correct answer wins: Capital expense pays for hardware before it is used and carries depreciation and refresh risk.
- **C:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: Capital expense pays for hardware before it is used and carries depreciation and refresh risk.
- **D:** Correct. In this case: Capital expense pays for hardware before it is used and carries depreciation and refresh risk.

### Question 4 — D

Answer: A flat monthly fee that does not change with usage. A flat fee does not follow usage, so the bill tells the business nothing about demand. A flat fee removes the usage signal from the bill but does not track demand. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: A flat fee does not follow usage, so the bill tells the business nothing about demand.
- **B:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: A flat fee does not follow usage, so the bill tells the business nothing about demand.
- **C:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: A flat fee does not follow usage, so the bill tells the business nothing about demand.
- **D:** Correct. A flat fee removes the usage signal from the bill but does not track demand. In this case: A flat fee does not follow usage, so the bill tells the business nothing about demand.

### Question 5 — C

Answer: Loose coupling with a queue between tiers. A buffer between the scanner and the printer lets each side work at its own pace. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A buffer between the scanner and the printer lets each side work at its own pace.
- **B:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: A buffer between the scanner and the printer lets each side work at its own pace.
- **C:** Correct. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. In this case: A buffer between the scanner and the printer lets each side work at its own pace.
- **D:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A buffer between the scanner and the printer lets each side work at its own pace.

### Question 6 — B

Answer: Scale the single monolith vertically only. Scaling a single application vertically ends at the largest machine available, whatever the demand. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Capacity follows the measured demand rather than a forecast. Why the correct answer wins: Scaling a single application vertically ends at the largest machine available, whatever the demand.
- **B:** Correct. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. In this case: Scaling a single application vertically ends at the largest machine available, whatever the demand.
- **C:** Incorrect for this question. Independent services can be deployed and scaled separately. Why the correct answer wins: Scaling a single application vertically ends at the largest machine available, whatever the demand.
- **D:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: Scaling a single application vertically ends at the largest machine available, whatever the demand.

### Question 7 — D

Answer: Operational excellence pillar. The operational excellence pillar covers how workloads are run and how changes are made and reversed. The pillar about running and improving workloads, including automation and small reversible changes. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about using resources efficiently as demand and technology change. Why the correct answer wins: The operational excellence pillar covers how workloads are run and how changes are made and reversed.
- **B:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The operational excellence pillar covers how workloads are run and how changes are made and reversed.
- **C:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: The operational excellence pillar covers how workloads are run and how changes are made and reversed.
- **D:** Correct. The pillar about running and improving workloads, including automation and small reversible changes. In this case: The operational excellence pillar covers how workloads are run and how changes are made and reversed.

### Question 8 — A, C

Answers: Review the workload against the Well-Architected Tool; Reliability pillar. The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure. The tool records answers against each pillar and produces improvement items. The pillar about recovering from failure and meeting demand consistently. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The pillar about recovering from failure and meeting demand consistently. In this case: The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure.
- **B:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure.
- **C:** Correct. The tool records answers against each pillar and produces improvement items. In this case: The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure.
- **D:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure.
- **E:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: The Well-Architected Tool captures the review, and the reliability pillar covers recovery from failure.

### Question 9 — B

Answer: Platform perspective of the AWS Cloud Adoption Framework. The platform perspective covers the technical architecture and the platform workloads run on. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about skills, roles and organisational change. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.
- **B:** Correct. In this case: The platform perspective covers the technical architecture and the platform workloads run on.
- **C:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.
- **D:** Incorrect for this question. The perspective about prioritising, budgeting and measuring the cloud programme. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.

### Question 10 — A

Answer: Operations perspective of the AWS Cloud Adoption Framework. The operations perspective covers running, monitoring and supporting workloads day to day. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: The operations perspective covers running, monitoring and supporting workloads day to day.
- **B:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.
- **C:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.
- **D:** Incorrect for this question. The perspective about prioritising, budgeting and measuring the cloud programme. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.

### Question 11 — A

Answer: Relocate: move the platform to a cloud-native equivalent. Relocate moves the platform to a hosted equivalent without touching the applications themselves. The whole platform moves to a hosted equivalent without changing the application itself. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The whole platform moves to a hosted equivalent without changing the application itself. In this case: Relocate moves the platform to a hosted equivalent without touching the applications themselves.
- **B:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Relocate moves the platform to a hosted equivalent without touching the applications themselves.
- **C:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Relocate moves the platform to a hosted equivalent without touching the applications themselves.
- **D:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Relocate moves the platform to a hosted equivalent without touching the applications themselves.

### Question 12 — C

Answer: Retire: switch the workload off. Retirement decommissions a workload that is no longer needed rather than moving it. The workload is no longer needed, so it is decommissioned instead of migrated. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company replaces the application with a commercially available equivalent. Why the correct answer wins: Retirement decommissions a workload that is no longer needed rather than moving it.
- **B:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Retirement decommissions a workload that is no longer needed rather than moving it.
- **C:** Correct. The workload is no longer needed, so it is decommissioned instead of migrated. In this case: Retirement decommissions a workload that is no longer needed rather than moving it.
- **D:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Retirement decommissions a workload that is no longer needed rather than moving it.

### Question 13 — A

Answer: Local Zones for very low latency. A Local Zone extends a Region close to a population or industry centre for very low latency. An extension of a Region placed close to a large population or industry centre. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. An extension of a Region placed close to a large population or industry centre. In this case: A Local Zone extends a Region close to a population or industry centre for very low latency.
- **B:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: A Local Zone extends a Region close to a population or industry centre for very low latency.
- **C:** Incorrect for this question. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. Why the correct answer wins: A Local Zone extends a Region close to a population or industry centre for very low latency.
- **D:** Incorrect for this question. A rack of AWS infrastructure installed in the customer facility and operated through AWS. Why the correct answer wins: A Local Zone extends a Region close to a population or industry centre for very low latency.

### Question 14 — B

Answer: Scale out automatically as demand rises. Scaling capacity automatically with measured demand removes the need to size for the peak all year. Capacity follows the measured demand rather than a forecast. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Scaling capacity automatically with measured demand removes the need to size for the peak all year.
- **B:** Correct. Capacity follows the measured demand rather than a forecast. In this case: Scaling capacity automatically with measured demand removes the need to size for the peak all year.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Scaling capacity automatically with measured demand removes the need to size for the peak all year.
- **D:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Scaling capacity automatically with measured demand removes the need to size for the peak all year.

### Question 15 — C, D

Answers: Loose coupling with a queue between tiers; Scale out automatically as demand rises. A queue decouples the scanner from the slow service, and automatic scaling covers the peak. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Capacity follows the measured demand rather than a forecast. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: A queue decouples the scanner from the slow service, and automatic scaling covers the peak.
- **B:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A queue decouples the scanner from the slow service, and automatic scaling covers the peak.
- **C:** Correct. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. In this case: A queue decouples the scanner from the slow service, and automatic scaling covers the peak.
- **D:** Correct. Capacity follows the measured demand rather than a forecast. In this case: A queue decouples the scanner from the slow service, and automatic scaling covers the peak.
- **E:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A queue decouples the scanner from the slow service, and automatic scaling covers the peak.

### Question 16 — A

Answer: The customer is responsible for configuring IAM permissions. Identity and access configuration stays with the customer in every service model. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Identity and access configuration stays with the customer in every service model.
- **B:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.
- **C:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.
- **D:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.

### Question 17 — D

Answer: Grant only the permissions the task needs. Granting only the actions the integration needs keeps a vendor mistake from reaching the whole account. Starting from the minimum and adding as needed keeps the blast radius small. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: Granting only the actions the integration needs keeps a vendor mistake from reaching the whole account.
- **B:** Incorrect for this question. Broad standing access means one mistaken action or stolen credential can change anything. Why the correct answer wins: Granting only the actions the integration needs keeps a vendor mistake from reaching the whole account.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Granting only the actions the integration needs keeps a vendor mistake from reaching the whole account.
- **D:** Correct. Starting from the minimum and adding as needed keeps the blast radius small. In this case: Granting only the actions the integration needs keeps a vendor mistake from reaching the whole account.

### Question 18 — D

Answer: Create an IAM user with long-lived credentials. A user is an identity for a person or application, so the activity trail names the individual. A user is an identity for a person or application with its own credentials. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: A user is an identity for a person or application, so the activity trail names the individual.
- **B:** Incorrect for this question. A role hands out temporary credentials, so nothing long-lived is stored. Why the correct answer wins: A user is an identity for a person or application, so the activity trail names the individual.
- **C:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: A user is an identity for a person or application, so the activity trail names the individual.
- **D:** Correct. A user is an identity for a person or application with its own credentials. In this case: A user is an identity for a person or application, so the activity trail names the individual.

### Question 19 — B

Answer: Enable MFA and delete the root access keys. The root user cannot be limited by policy, so it needs multi-factor authentication and no standing access keys. The root user is the most privileged identity, so it is protected and its keys are removed. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: The root user cannot be limited by policy, so it needs multi-factor authentication and no standing access keys.
- **B:** Correct. The root user is the most privileged identity, so it is protected and its keys are removed. In this case: The root user cannot be limited by policy, so it needs multi-factor authentication and no standing access keys.
- **C:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: The root user cannot be limited by policy, so it needs multi-factor authentication and no standing access keys.
- **D:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: The root user cannot be limited by policy, so it needs multi-factor authentication and no standing access keys.

### Question 20 — B

Answer: Rotate access keys on a schedule. Rotation replaces the key on a schedule, so a leaked key stops working once it is replaced. A rotation schedule limits how long a leaked key stays useful. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: Rotation replaces the key on a schedule, so a leaked key stops working once it is replaced.
- **B:** Correct. A rotation schedule limits how long a leaked key stays useful. In this case: Rotation replaces the key on a schedule, so a leaked key stops working once it is replaced.
- **C:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Rotation replaces the key on a schedule, so a leaked key stops working once it is replaced.
- **D:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Rotation replaces the key on a schedule, so a leaked key stops working once it is replaced.

### Question 21 — C

Answer: Use IAM Identity Center for workforce sign-in. IAM Identity Center gives workforce users one sign-in and permission sets for the accounts they use. Workforce users sign in once and receive permission sets for the accounts they use. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: IAM Identity Center gives workforce users one sign-in and permission sets for the accounts they use.
- **B:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: IAM Identity Center gives workforce users one sign-in and permission sets for the accounts they use.
- **C:** Correct. Workforce users sign in once and receive permission sets for the accounts they use. In this case: IAM Identity Center gives workforce users one sign-in and permission sets for the accounts they use.
- **D:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: IAM Identity Center gives workforce users one sign-in and permission sets for the accounts they use.

### Question 22 — B

Answer: Create an IAM role and let the workload assume it. A role gives the function temporary credentials that AWS manages and rotates. A role hands out temporary credentials, so nothing long-lived is stored. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A role gives the function temporary credentials that AWS manages and rotates.
- **B:** Correct. A role hands out temporary credentials, so nothing long-lived is stored. In this case: A role gives the function temporary credentials that AWS manages and rotates.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: A role gives the function temporary credentials that AWS manages and rotates.
- **D:** Incorrect for this question. Existing corporate identities are used instead of a separate set of AWS credentials. Why the correct answer wins: A role gives the function temporary credentials that AWS manages and rotates.

### Question 23 — C

Answer: Use a security group as a stateful instance firewall. A security group can allow the balancer and nothing else, which is the instance-level control. The group allows inbound or outbound traffic and remembers the connection state. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. An open perimeter exposes every service on the host, including ones nobody meant to publish. Why the correct answer wins: A security group can allow the balancer and nothing else, which is the instance-level control.
- **B:** Incorrect for this question. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Why the correct answer wins: A security group can allow the balancer and nothing else, which is the instance-level control.
- **C:** Correct. The group allows inbound or outbound traffic and remembers the connection state. In this case: A security group can allow the balancer and nothing else, which is the instance-level control.
- **D:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: A security group can allow the balancer and nothing else, which is the instance-level control.

### Question 24 — D, E

Answers: Use a network ACL as a stateless subnet filter; Use AWS Network Firewall for VPC-level inspection. A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary. The ACL filters traffic at the subnet boundary and evaluates each direction independently. A managed firewall inspects traffic entering and leaving the VPC. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary.
- **B:** Incorrect for this question. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Why the correct answer wins: A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary.
- **C:** Incorrect for this question. Shield absorbs distributed denial-of-service traffic before it reaches the application. Why the correct answer wins: A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary.
- **D:** Correct. A managed firewall inspects traffic entering and leaving the VPC. In this case: A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary.
- **E:** Correct. The ACL filters traffic at the subnet boundary and evaluates each direction independently. In this case: A network ACL drops the range before it reaches any host, and Network Firewall inspects traffic at the VPC boundary.

### Question 25 — A

Answer: Encrypt data in transit with TLS. Encryption in transit with TLS protects the data while it moves between the services. Traffic is protected while it crosses the network, not only while it sits on disk. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Traffic is protected while it crosses the network, not only while it sits on disk. In this case: Encryption in transit with TLS protects the data while it moves between the services.
- **B:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: Encryption in transit with TLS protects the data while it moves between the services.
- **C:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: Encryption in transit with TLS protects the data while it moves between the services.
- **D:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: Encryption in transit with TLS protects the data while it moves between the services.

### Question 26 — B

Answer: Rely on server-side encryption with Amazon S3 managed keys. Bucket default encryption encrypts each object as it is written, with no application change. S3 encrypts the object at rest with keys it manages on the customer behalf. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: Bucket default encryption encrypts each object as it is written, with no application change.
- **B:** Correct. S3 encrypts the object at rest with keys it manages on the customer behalf. In this case: Bucket default encryption encrypts each object as it is written, with no application change.
- **C:** Incorrect for this question. The customer controls the key policy and can revoke access by disabling the key. Why the correct answer wins: Bucket default encryption encrypts each object as it is written, with no application change.
- **D:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Bucket default encryption encrypts each object as it is written, with no application change.

### Question 27 — C

Answer: Put the password in the application source code. A credential in source code is copied everywhere and cannot be rotated quietly. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: A credential in source code is copied everywhere and cannot be rotated quietly.
- **B:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: A credential in source code is copied everywhere and cannot be rotated quietly.
- **C:** Correct. In this case: A credential in source code is copied everywhere and cannot be rotated quietly.
- **D:** Incorrect for this question. The secret is held centrally and can be rotated on a schedule. Why the correct answer wins: A credential in source code is copied everywhere and cannot be rotated quietly.

### Question 28 — D

Answer: Use Amazon Inspector to scan workloads for vulnerabilities. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Inspector finds software vulnerabilities and unintended network exposure on the resources it scans.
- **B:** Incorrect for this question. Security Hub collects findings from the security services and scores them against a standard. Why the correct answer wins: Inspector finds software vulnerabilities and unintended network exposure on the resources it scans.
- **C:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Inspector finds software vulnerabilities and unintended network exposure on the resources it scans.
- **D:** Correct. In this case: Inspector finds software vulnerabilities and unintended network exposure on the resources it scans.

### Question 29 — D, E

Answers: Use AWS Security Hub to aggregate findings in one place; Use Amazon Inspector to scan workloads for vulnerabilities. Security Hub aggregates and scores findings, and Inspector reports the missing patches. Security Hub collects findings from the security services and scores them against a standard. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Security Hub aggregates and scores findings, and Inspector reports the missing patches.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Security Hub aggregates and scores findings, and Inspector reports the missing patches.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Security Hub aggregates and scores findings, and Inspector reports the missing patches.
- **D:** Correct. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. In this case: Security Hub aggregates and scores findings, and Inspector reports the missing patches.
- **E:** Correct. Security Hub collects findings from the security services and scores them against a standard. In this case: Security Hub aggregates and scores findings, and Inspector reports the missing patches.

### Question 30 — C

Answer: AWS Backup. AWS Backup centralises and automates backups across supported services to a restore point. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: AWS Backup centralises and automates backups across supported services to a restore point.
- **B:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: AWS Backup centralises and automates backups across supported services to a restore point.
- **C:** Correct. In this case: AWS Backup centralises and automates backups across supported services to a restore point.
- **D:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: AWS Backup centralises and automates backups across supported services to a restore point.

### Question 31 — C

Answer: Set a retention period and delete expired copies. A retention period per data class decides when a copy must be deleted. A retention rule stops data from being kept forever by default. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A retention period per data class decides when a copy must be deleted.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A retention period per data class decides when a copy must be deleted.
- **C:** Correct. A retention rule stops data from being kept forever by default. In this case: A retention period per data class decides when a copy must be deleted.
- **D:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A retention period per data class decides when a copy must be deleted.

### Question 32 — B

Answer: Use AWS CloudTrail to record API activity. CloudTrail records the API call, the caller and the source of the request. CloudTrail logs who called which API, when and from where. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **B:** Correct. CloudTrail logs who called which API, when and from where. In this case: CloudTrail records the API call, the caller and the source of the request.
- **C:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **D:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.

### Question 33 — C, E

Answers: Use AWS Config to record resource configuration changes; Use AWS Audit Manager to collect evidence for an audit. Config keeps the configuration history, and Audit Manager assembles the framework evidence. Config keeps a history of configuration and evaluates it against rules. Audit Manager assembles evidence against a chosen framework. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Trusted Advisor inspects the account and reports insecure or wasteful settings. Why the correct answer wins: Config keeps the configuration history, and Audit Manager assembles the framework evidence.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: Config keeps the configuration history, and Audit Manager assembles the framework evidence.
- **C:** Correct. Audit Manager assembles evidence against a chosen framework. In this case: Config keeps the configuration history, and Audit Manager assembles the framework evidence.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Config keeps the configuration history, and Audit Manager assembles the framework evidence.
- **E:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: Config keeps the configuration history, and Audit Manager assembles the framework evidence.

### Question 34 — A

Answer: AWS is responsible for the physical facilities and hardware. AWS operates the buildings, power and network fabric beneath every service. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: AWS operates the buildings, power and network fabric beneath every service.
- **B:** Incorrect for this question. Classification, access and protection of the data remain with the customer. Why the correct answer wins: AWS operates the buildings, power and network fabric beneath every service.
- **C:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: AWS operates the buildings, power and network fabric beneath every service.
- **D:** Incorrect for this question. Identity and access configuration is a customer responsibility in every model. Why the correct answer wins: AWS operates the buildings, power and network fabric beneath every service.

### Question 35 — A

Answer: Apply a service control policy in AWS Organizations. A service control policy caps what every account beneath it can do, whoever administers that account. An SCP sets the maximum permissions available to the accounts under it. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. An SCP sets the maximum permissions available to the accounts under it. In this case: A service control policy caps what every account beneath it can do, whoever administers that account.
- **B:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A service control policy caps what every account beneath it can do, whoever administers that account.
- **C:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: A service control policy caps what every account beneath it can do, whoever administers that account.
- **D:** Incorrect for this question. An SCP only limits permissions; it never grants them. Why the correct answer wins: A service control policy caps what every account beneath it can do, whoever administers that account.

### Question 36 — B

Answer: AWS Lambda. Lambda runs the handler per event and keeps nothing running in between. Run code on an event without provisioning or managing a server. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.
- **B:** Correct. Run code on an event without provisioning or managing a server. In this case: Lambda runs the handler per event and keeps nothing running in between.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.
- **D:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.

### Question 37 — D

Answer: Amazon EC2 instances. Amazon EC2 gives the customer the operating system and the hardware selection, including accelerated instance types. Virtual servers where the customer controls the operating system and the runtime. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Amazon EC2 gives the customer the operating system and the hardware selection, including accelerated instance types.
- **B:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Amazon EC2 gives the customer the operating system and the hardware selection, including accelerated instance types.
- **C:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: Amazon EC2 gives the customer the operating system and the hardware selection, including accelerated instance types.
- **D:** Correct. Virtual servers where the customer controls the operating system and the runtime. In this case: Amazon EC2 gives the customer the operating system and the hardware selection, including accelerated instance types.

### Question 38 — C

Answer: Amazon S3 Standard. S3 Standard is built for frequently accessed objects with high durability and no server to run. Object storage for frequently accessed data with high durability and availability. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: S3 Standard is built for frequently accessed objects with high durability and no server to run.
- **B:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: S3 Standard is built for frequently accessed objects with high durability and no server to run.
- **C:** Correct. Object storage for frequently accessed data with high durability and availability. In this case: S3 Standard is built for frequently accessed objects with high durability and no server to run.
- **D:** Incorrect for this question. Object storage for data that is accessed less often but must be available immediately. Why the correct answer wins: S3 Standard is built for frequently accessed objects with high durability and no server to run.

### Question 39 — A, D

Answers: Amazon EBS volumes; AWS Backup. EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies. Block storage attached to a single instance, used for an operating system or database files. A managed service that centralises and automates backups across supported services. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed service that centralises and automates backups across supported services. In this case: EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies.
- **B:** Incorrect for this question. Physical devices that move large datasets into AWS when the network is the bottleneck. Why the correct answer wins: EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies.
- **C:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies.
- **D:** Correct. Block storage attached to a single instance, used for an operating system or database files. In this case: EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies.
- **E:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: EBS provides the persistent block volumes, and AWS Backup schedules and centralises the copies.

### Question 40 — A

Answer: Amazon Redshift. A managed data warehouse is built for analytical queries over large datasets. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: A managed data warehouse is built for analytical queries over large datasets.
- **B:** Incorrect for this question. A managed in-memory cache for sub-millisecond reads of hot data. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.
- **C:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.
- **D:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: A managed data warehouse is built for analytical queries over large datasets.

### Question 41 — C

Answer: Amazon DocumentDB. DocumentDB is a managed document database compatible with MongoDB workloads. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: DocumentDB is a managed document database compatible with MongoDB workloads.
- **B:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: DocumentDB is a managed document database compatible with MongoDB workloads.
- **C:** Correct. In this case: DocumentDB is a managed document database compatible with MongoDB workloads.
- **D:** Incorrect for this question. A managed graph database for highly connected data. Why the correct answer wins: DocumentDB is a managed document database compatible with MongoDB workloads.

### Question 42 — B

Answer: Amazon Route 53. Route 53 hosts DNS records and supports health checks and failover routing. A managed DNS service that also supports health checks and routing policies. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: Route 53 hosts DNS records and supports health checks and failover routing.
- **B:** Correct. A managed DNS service that also supports health checks and routing policies. In this case: Route 53 hosts DNS records and supports health checks and failover routing.
- **C:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Route 53 hosts DNS records and supports health checks and failover routing.
- **D:** Incorrect for this question. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Why the correct answer wins: Route 53 hosts DNS records and supports health checks and failover routing.

### Question 43 — A, B

Answers: Amazon API Gateway; AWS Global Accelerator. API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint. A managed front door for APIs with throttling, authorisation and usage plans. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. In this case: API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint.
- **B:** Correct. A managed front door for APIs with throttling, authorisation and usage plans. In this case: API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint.
- **C:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint.
- **D:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint.
- **E:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: API Gateway provides throttling and usage plans, and Global Accelerator routes users to the nearest healthy endpoint.

### Question 44 — D

Answer: AWS CloudFormation. CloudFormation creates and updates resources from a template, so each build is identical. Infrastructure defined as a template and created or updated as a stack. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Operations tooling for patching, running commands and inventory across managed nodes. Why the correct answer wins: CloudFormation creates and updates resources from a template, so each build is identical.
- **B:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: CloudFormation creates and updates resources from a template, so each build is identical.
- **C:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: CloudFormation creates and updates resources from a template, so each build is identical.
- **D:** Correct. Infrastructure defined as a template and created or updated as a stack. In this case: CloudFormation creates and updates resources from a template, so each build is identical.

### Question 45 — B

Answer: Amazon CloudWatch. CloudWatch collects the metrics and logs and evaluates the alarms. Metrics, logs and alarms for the resources and applications in the account. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch collects the metrics and logs and evaluates the alarms.
- **B:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch collects the metrics and logs and evaluates the alarms.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch collects the metrics and logs and evaluates the alarms.
- **D:** Incorrect for this question. Service health and event notifications that affect the account. Why the correct answer wins: CloudWatch collects the metrics and logs and evaluates the alarms.

### Question 46 — A

Answer: Amazon SNS. SNS fans one message out to many subscribers. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: SNS fans one message out to many subscribers.
- **B:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: SNS fans one message out to many subscribers.
- **C:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: SNS fans one message out to many subscribers.
- **D:** Incorrect for this question. A state machine that coordinates multi-step workflows with retries and branching. Why the correct answer wins: SNS fans one message out to many subscribers.

### Question 47 — B, D

Answers: Amazon SQS; Amazon EventBridge. A queue buffers the jobs, and EventBridge routes the state-change events by rule. A managed queue that decouples producers from consumers and buffers bursts. An event bus that routes events from AWS services and applications to targets by rule. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed message broker for existing protocols such as AMQP or MQTT. Why the correct answer wins: A queue buffers the jobs, and EventBridge routes the state-change events by rule.
- **B:** Correct. An event bus that routes events from AWS services and applications to targets by rule. In this case: A queue buffers the jobs, and EventBridge routes the state-change events by rule.
- **C:** Incorrect for this question. Streaming data ingestion and processing for continuous records. Why the correct answer wins: A queue buffers the jobs, and EventBridge routes the state-change events by rule.
- **D:** Correct. A managed queue that decouples producers from consumers and buffers bursts. In this case: A queue buffers the jobs, and EventBridge routes the state-change events by rule.
- **E:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: A queue buffers the jobs, and EventBridge routes the state-change events by rule.

### Question 48 — B

Answer: AWS Glue. Glue provides the data catalogue and the extract-transform-load jobs. A managed data catalogue and extract-transform-load service. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed business intelligence service for dashboards and reports. Why the correct answer wins: Glue provides the data catalogue and the extract-transform-load jobs.
- **B:** Correct. A managed data catalogue and extract-transform-load service. In this case: Glue provides the data catalogue and the extract-transform-load jobs.
- **C:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Glue provides the data catalogue and the extract-transform-load jobs.
- **D:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: Glue provides the data catalogue and the extract-transform-load jobs.

### Question 49 — A

Answer: Amazon EMR. EMR runs managed big-data frameworks such as Spark on clusters AWS operates. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: EMR runs managed big-data frameworks such as Spark on clusters AWS operates.
- **B:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: EMR runs managed big-data frameworks such as Spark on clusters AWS operates.
- **C:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: EMR runs managed big-data frameworks such as Spark on clusters AWS operates.
- **D:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: EMR runs managed big-data frameworks such as Spark on clusters AWS operates.

### Question 50 — D

Answer: AWS CodeBuild. CodeBuild runs the compile and test steps in a managed build environment. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **C:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **D:** Correct. In this case: CodeBuild runs the compile and test steps in a managed build environment.

### Question 51 — A

Answer: AWS CodePipeline. CodePipeline records the stages, approvals and outcomes of each release. Orchestrates the build, test and deploy stages of a release. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Orchestrates the build, test and deploy stages of a release. In this case: CodePipeline records the stages, approvals and outcomes of each release.
- **B:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodePipeline records the stages, approvals and outcomes of each release.
- **C:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: CodePipeline records the stages, approvals and outcomes of each release.
- **D:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CodePipeline records the stages, approvals and outcomes of each release.

### Question 52 — A

Answer: AWS Elastic Beanstalk. Elastic Beanstalk provisions and manages the environment around the uploaded application. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **B:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **D:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.

### Question 53 — C

Answer: AWS App Runner. App Runner runs the container and manages the capacity and scaling behind it. Run a containerised web service without choosing or managing the underlying capacity. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **B:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **C:** Correct. Run a containerised web service without choosing or managing the underlying capacity. In this case: App Runner runs the container and manages the capacity and scaling behind it.
- **D:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.

### Question 54 — C

Answer: Amazon CloudWatch. CloudWatch holds the metric and evaluates the alarm against it. Metrics, logs and alarms for the resources and applications in the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **B:** Incorrect for this question. Checks an account against best practices for cost, security, limits and resilience. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **C:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch holds the metric and evaluates the alarm against it.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.

### Question 55 — A, B

Answers: Amazon CloudWatch; AWS Health Dashboard. CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events. Metrics, logs and alarms for the resources and applications in the account. Service health and event notifications that affect the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events.
- **B:** Correct. Service health and event notifications that affect the account. In this case: CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events.
- **C:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events.
- **E:** Incorrect for this question. Checks an account against best practices for cost, security, limits and resilience. Why the correct answer wins: CloudWatch covers the account's own metrics and alarms, and the Health Dashboard reports AWS service events.

### Question 56 — D

Answer: AWS Transit Gateway. Transit Gateway acts as a central router that connects many VPCs and on-premises networks. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: Transit Gateway acts as a central router that connects many VPCs and on-premises networks.
- **B:** Incorrect for this question. A logically isolated virtual network in which the customer places its resources. Why the correct answer wins: Transit Gateway acts as a central router that connects many VPCs and on-premises networks.
- **C:** Incorrect for this question. Private connectivity to a service through an endpoint inside the VPC. Why the correct answer wins: Transit Gateway acts as a central router that connects many VPCs and on-premises networks.
- **D:** Correct. In this case: Transit Gateway acts as a central router that connects many VPCs and on-premises networks.

### Question 57 — B

Answer: AWS Storage Gateway. Storage Gateway provides the hybrid file, volume or tape interface backed by AWS. A hybrid file, volume or tape interface that keeps frequently used data on premises. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Physical devices that move large datasets into AWS when the network is the bottleneck. Why the correct answer wins: Storage Gateway provides the hybrid file, volume or tape interface backed by AWS.
- **B:** Correct. A hybrid file, volume or tape interface that keeps frequently used data on premises. In this case: Storage Gateway provides the hybrid file, volume or tape interface backed by AWS.
- **C:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: Storage Gateway provides the hybrid file, volume or tape interface backed by AWS.
- **D:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: Storage Gateway provides the hybrid file, volume or tape interface backed by AWS.

### Question 58 — D

Answer: Reserved Instances. A one- or three-year commitment lowers the hourly rate in exchange for the commitment. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: A one- or three-year commitment lowers the hourly rate in exchange for the commitment.
- **B:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: A one- or three-year commitment lowers the hourly rate in exchange for the commitment.
- **C:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: A one- or three-year commitment lowers the hourly rate in exchange for the commitment.
- **D:** Correct. In this case: A one- or three-year commitment lowers the hourly rate in exchange for the commitment.

### Question 59 — C

Answer: On-Demand Instances. On-Demand capacity is billed as used, with no commitment to forecast around. Capacity billed by the second or hour with no commitment. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: On-Demand capacity is billed as used, with no commitment to forecast around.
- **B:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: On-Demand capacity is billed as used, with no commitment to forecast around.
- **C:** Correct. Capacity billed by the second or hour with no commitment. In this case: On-Demand capacity is billed as used, with no commitment to forecast around.
- **D:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: On-Demand capacity is billed as used, with no commitment to forecast around.

### Question 60 — D

Answer: AWS Pricing Calculator. The Pricing Calculator estimates a planned architecture before anything is deployed. Estimate the cost of a planned architecture before it is built. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: The Pricing Calculator estimates a planned architecture before anything is deployed.
- **B:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: The Pricing Calculator estimates a planned architecture before anything is deployed.
- **C:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: The Pricing Calculator estimates a planned architecture before anything is deployed.
- **D:** Correct. Estimate the cost of a planned architecture before it is built. In this case: The Pricing Calculator estimates a planned architecture before anything is deployed.

### Question 61 — D, E

Answers: AWS Cost and Usage Report; Cost Anomaly Detection. The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation. The most granular billing dataset, delivered to a bucket for analysis. Machine learning alerts on spending that deviates from the expected pattern. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation.
- **B:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation.
- **C:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation.
- **D:** Correct. The most granular billing dataset, delivered to a bucket for analysis. In this case: The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation.
- **E:** Correct. Machine learning alerts on spending that deviates from the expected pattern. In this case: The Cost and Usage Report delivers line-item detail, and Cost Anomaly Detection alerts on the deviation.

### Question 62 — A

Answer: Tag resources and activate cost allocation tags. Activated cost allocation tags split the single bill by department or project. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Activated cost allocation tags split the single bill by department or project.
- **B:** Incorrect for this question. One bill for all accounts, with usage aggregated so volume discounts are shared. Why the correct answer wins: Activated cost allocation tags split the single bill by department or project.
- **C:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Activated cost allocation tags split the single bill by department or project.
- **D:** Incorrect for this question. Separate accounts do not pool usage, so each misses the discounts the total would earn. Why the correct answer wins: Activated cost allocation tags split the single bill by department or project.

### Question 63 — C

Answer: AWS Developer Support. Developer Support provides business-hours email support for development and test workloads. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Mission-critical support with a designated technical account manager and the fastest response. Why the correct answer wins: Developer Support provides business-hours email support for development and test workloads.
- **B:** Incorrect for this question. Production support with 24/7 access, faster response and Trusted Advisor checks. Why the correct answer wins: Developer Support provides business-hours email support for development and test workloads.
- **C:** Correct. In this case: Developer Support provides business-hours email support for development and test workloads.
- **D:** Incorrect for this question. Account and billing support with documentation and health checks, at no charge. Why the correct answer wins: Developer Support provides business-hours email support for development and test workloads.

### Question 64 — C

Answer: Read the AWS documentation and service user guides. The AWS documentation is the reference for service behaviour, limits and API parameters. The reference documentation states what a service does and how it is configured. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A vetted reference architecture shortens design work for a common workload. Why the correct answer wins: The AWS documentation is the reference for service behaviour, limits and API parameters.
- **B:** Incorrect for this question. The community knowledge base holds answers to common service and account questions. Why the correct answer wins: The AWS documentation is the reference for service behaviour, limits and API parameters.
- **C:** Correct. The reference documentation states what a service does and how it is configured. In this case: The AWS documentation is the reference for service behaviour, limits and API parameters.
- **D:** Incorrect for this question. Partners are third-party firms with AWS-validated skills for implementation work. Why the correct answer wins: The AWS documentation is the reference for service behaviour, limits and API parameters.

### Question 65 — D

Answer: Spot Instances. Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **B:** Incorrect for this question. Limited monthly usage at no charge for eligible services on a new or qualifying account. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **C:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **D:** Correct. In this case: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
