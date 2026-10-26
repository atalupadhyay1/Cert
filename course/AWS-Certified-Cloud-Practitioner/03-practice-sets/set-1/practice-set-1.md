# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 1

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. A retail chain sees web traffic multiply for 36 hours during a flash sale each quarter and wants capacity to follow that curve. Which cloud benefit does this illustrate?

- A. Reliability through managed, redundant infrastructure
- B. Elasticity: scale capacity with demand
- C. Trade capital expense for variable expense
- D. A flat monthly fee that does not change with usage

### 2. A streaming studio plans to launch its catalogue in four new countries next quarter and does not want to build facilities in any of them. Which cloud benefit applies?

- A. Stop spending on undifferentiated heavy lifting
- B. Buy servers up front and depreciate them
- C. Keep ownership of the physical data centre
- D. Global reach: deploy into multiple Regions quickly

### 3. A finance analyst compares refreshing an on-premises estate with a cloud deployment and wants the comparison to be defensible. What must the model include?

- A. A flat monthly fee that does not change with usage
- B. Pay-as-you-go pricing
- C. Volume discounts that grow with usage
- D. Estimate total cost of ownership including facilities and staff

### 4. A seasonal events business wants no up-front payment and a bill that tracks the months it is busy. Which pricing approach matches its request?

- A. Reserved Instances
- B. Buy servers up front and depreciate them
- C. A flat monthly fee that does not change with usage
- D. Pay-as-you-go pricing

### 5. A slow nightly reporting job drags the customer-facing storefront down because each tier calls the next one synchronously. Which design principle addresses this?

- A. Loose coupling with a queue between tiers
- B. Scale the single monolith vertically only
- C. Deploy across multiple Availability Zones
- D. Direct synchronous calls between every tier

### 6. A file-ingest task runs for a few seconds whenever a document arrives and needs no capacity in between. Which design approach fits?

- A. Scale the single monolith vertically only
- B. Deploy across multiple Availability Zones
- C. Serverless compute for intermittent work
- D. Direct synchronous calls between every tier

### 7. A review must show that a workload keeps serving traffic when a component fails and recovers without an operator. Which Well-Architected pillar covers that question?

- A. Reliability pillar
- B. Sustainability pillar
- C. Cost optimization pillar
- D. Operational excellence pillar

### 8. A design review must cover both how small changes are made and reversed, and how the workload is run at the lowest price that still meets its requirement. Which two pillars apply? Select two.

- A. Security pillar
- B. Reliability pillar
- C. Operational excellence pillar
- D. Sustainability pillar
- E. Cost optimization pillar

### 9. Before a cloud programme starts, the board wants agreed business outcomes, a budget and a way to measure progress. Which Cloud Adoption Framework perspective provides this?

- A. People perspective of the AWS Cloud Adoption Framework
- B. Governance perspective of the AWS Cloud Adoption Framework
- C. Operations perspective of the AWS Cloud Adoption Framework
- D. Platform perspective of the AWS Cloud Adoption Framework

### 10. A retailer cloud plan stalls because the teams lack the skills for the new operating model and nobody owns the new roles. Which capability perspective addresses this?

- A. Business perspective of the AWS Cloud Adoption Framework
- B. Security perspective of the AWS Cloud Adoption Framework
- C. People perspective of the AWS Cloud Adoption Framework
- D. Platform perspective of the AWS Cloud Adoption Framework

### 11. An insurer must leave its mainframe policy system in place for regulatory reasons while moving everything else to AWS. Which migration strategy applies to that one system?

- A. Retain: keep the workload where it is
- B. Repurchase: move to a different product
- C. Rehost: move the application as it is
- D. Retire: switch the workload off

### 12. A media company replaces its ageing ticketing tool with a SaaS product instead of hosting the old application in AWS. Which strategy is this?

- A. Replatform: change a few managed components on the way
- B. Relocate: move the platform to a cloud-native equivalent
- C. Repurchase: move to a different product
- D. Refactor: redesign the application for cloud architecture

### 13. A workload serves one country but must survive the loss of a single data-centre building without an outage. Which part of the global infrastructure provides that?

- A. Place everything in one Availability Zone
- B. AWS Outposts for on-premises capacity
- C. Regions and Availability Zones
- D. Edge locations for content delivery

### 14. A checkout service currently runs in one data-centre building and stops when that building loses power. What should be done?

- A. Deploy across multiple Availability Zones
- B. Direct synchronous calls between every tier
- C. Place everything in one Availability Zone
- D. Scale the single monolith vertically only

### 15. A product catalogue must absorb a tenfold seasonal spike and stay online when one Availability Zone is lost, with no manual intervention. Which two design choices fit? Select two.

- A. Direct synchronous calls between every tier
- B. Place everything in one Availability Zone
- C. Deploy across multiple Availability Zones
- D. Scale out automatically as demand rises
- E. Scale the single monolith vertically only

### 16. An Amazon EC2 instance runs an older Linux kernel that needs a security patch. Under the shared responsibility model, who applies it?

- A. AWS is responsible for patching a managed service such as Amazon S3
- B. AWS is responsible for the physical facilities and hardware
- C. The customer is responsible for the data-centre building
- D. The customer is responsible for patching the guest operating system on Amazon EC2

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. A new analyst needs to read one reporting bucket and nothing else. Which approach follows least privilege?

- A. Give every engineer administrator access for convenience
- B. Require multi-factor authentication
- C. Grant only the permissions the task needs
- D. Share the root credentials with the operations team

### 18. Thirty support agents need an identical permission set that is reviewed and changed each quarter. What should be created?

- A. Rotate access keys on a schedule
- B. Create an IAM role and let the workload assume it
- C. Put the users in a group and attach the policy to the group
- D. Use the root user for daily administration

### 19. What should be done with the root user as soon as a new AWS account is created?

- A. Use the root user for daily administration
- B. Share the root credentials with the operations team
- C. Enable MFA and delete the root access keys
- D. Rotate access keys on a schedule

### 20. An audit finds a programmatic access key that has not changed in three years and is used by a reporting script. What should be done?

- A. Require multi-factor authentication
- B. Enable MFA and delete the root access keys
- C. Attach a JSON policy that allows only the required actions
- D. Rotate access keys on a schedule

### 21. An application on Amazon EC2 must read objects from a bucket without any credential being stored on the instance. What should be used?

- A. Use the root user for daily administration
- B. Put the password in the application source code
- C. Create an IAM user with long-lived credentials
- D. Create an IAM role and let the workload assume it

### 22. Employees should sign in to the AWS accounts with the corporate directory account they already use. What should be configured?

- A. Put the users in a group and attach the policy to the group
- B. Federate the company directory into AWS
- C. Use Amazon Cognito for customer sign-in
- D. Create an IAM user with long-lived credentials

### 23. A public web server must accept HTTPS from anywhere and reject every other inbound port. What should be applied to the instance?

- A. Open every port to the internet and rely on the application
- B. Use a security group as a stateful instance firewall
- C. Use AWS Network Firewall for VPC-level inspection
- D. Use a network ACL as a stateless subnet filter

### 24. A public storefront must block scripted injection attempts and absorb a volumetric flood before it reaches the servers. Which two services apply? Select two.

- A. Use AWS Shield for DDoS protection
- B. Use a network ACL as a stateless subnet filter
- C. Use AWS KMS to create and control encryption keys
- D. Use AWS WAF to block web attack patterns
- E. Use a security group as a stateful instance firewall

### 25. A regulator requires the company to control its own encryption keys and to be able to revoke access by disabling a key. What should be used?

- A. Rely on server-side encryption with Amazon S3 managed keys
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use a customer managed key for the required control
- D. Use AWS Certificate Manager for TLS certificates

### 26. Files are copied nightly from an office server to Amazon S3 over the internet and must be unreadable to anyone watching the traffic. What is required?

- A. Encrypt data in transit with TLS
- B. Use AWS KMS to create and control encryption keys
- C. Rely on server-side encryption with Amazon S3 managed keys
- D. Set a retention period and delete expired copies

### 27. A database password is written into the application source code and copied to every environment. What should change?

- A. Store the database credential in AWS Secrets Manager and rotate it
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. Put the password in the application source code
- D. Attach a JSON policy that allows only the required actions

### 28. The security team wants to be alerted when an instance contacts a known malicious address or shows anomalous account behaviour. Which service fits?

- A. Use Amazon GuardDuty to detect suspicious activity
- B. Use Amazon Inspector to scan workloads for vulnerabilities
- C. Use AWS CloudTrail to record API activity
- D. Use Amazon Macie to find sensitive data in Amazon S3

### 29. A review must find unpatched software on running instances and identify which buckets hold personal data. Which two services apply? Select two.

- A. Use AWS Security Hub to aggregate findings in one place
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use Amazon Inspector to scan workloads for vulnerabilities
- D. Use Amazon GuardDuty to detect suspicious activity
- E. Use AWS CloudTrail to record API activity

### 30. A bucket holds customer records and a review must confirm that nobody on the internet can read them. What should be examined?

- A. Set an S3 lifecycle rule to expire old objects
- B. Rely on server-side encryption with Amazon S3 managed keys
- C. An Amazon S3 bucket policy that grants public read
- D. AWS Backup

### 31. An analyst must find out which of several hundred buckets contain personal data before a retention project starts. Which service answers that?

- A. Use Amazon Macie to find sensitive data in Amazon S3
- B. Use Amazon GuardDuty to detect suspicious activity
- C. Use AWS Config to record resource configuration changes
- D. Use Amazon Inspector to scan workloads for vulnerabilities

### 32. An external auditor asks for the AWS SOC 2 report as part of a vendor review. Where is it obtained?

- A. Use AWS CloudTrail to record API activity
- B. Use AWS Config to record resource configuration changes
- C. Download the compliance reports from AWS Artifact
- D. Use AWS Audit Manager to collect evidence for an audit

### 33. An investigation must show who changed a security group last month and what the rule looked like before the change. Which two services provide that evidence? Select two.

- A. Use Amazon Inspector to scan workloads for vulnerabilities
- B. Use AWS CloudTrail to record API activity
- C. Use Amazon Macie to find sensitive data in Amazon S3
- D. Use Amazon GuardDuty to detect suspicious activity
- E. Use AWS Config to record resource configuration changes

### 34. A team runs Amazon RDS and asks who applies engine security patches to the database. Under the shared responsibility model, who does it?

- A. The customer is responsible for the data-centre building
- B. The customer is responsible for the data it stores in AWS
- C. The customer is responsible for patching the guest operating system on Amazon EC2
- D. AWS is responsible for patching a managed service such as Amazon S3

### 35. A company must stop every account in its organisation from using a service that has not been approved, even if an administrator tries. What should be applied?

- A. Use AWS Config to record resource configuration changes
- B. Use a security group as a stateful instance firewall
- C. Attach a JSON policy that allows only the required actions
- D. Apply a service control policy in AWS Organizations

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. A team wants to resize each uploaded photograph when it lands in a bucket, with no server to patch or scale. Which service fits?

- A. Amazon Lightsail
- B. Amazon EC2 instances
- C. AWS Lambda
- D. Amazon ECS or Amazon EKS with AWS Fargate

### 37. A legacy application needs a specific kernel module and full control of the operating system. Which compute service fits?

- A. Amazon EC2 instances
- B. AWS App Runner
- C. AWS Lambda
- D. AWS Elastic Beanstalk

### 38. Audit logs older than 90 days are almost never read but must be kept for seven years at the lowest cost. Which storage option fits?

- A. Amazon EBS volumes
- B. Amazon S3 Glacier storage classes
- C. Amazon S3 Standard
- D. Amazon EFS file system

### 39. A render farm needs a shared directory that many Linux servers mount at once, and finished frames must move to cheap long-term storage. Which two services fit? Select two.

- A. Amazon S3 Glacier storage classes
- B. Amazon EBS volumes
- C. AWS Snowball devices
- D. Amazon EFS file system
- E. Amazon FSx file systems

### 40. A team wants a managed relational database with automated backups and no engine patching of its own. Which service fits?

- A. Amazon EC2 instances
- B. Amazon RDS
- C. Amazon DynamoDB
- D. Amazon Redshift

### 41. A shopping cart must serve millions of key lookups a day at single-digit millisecond latency and scale without a schema migration. Which service fits?

- A. Amazon DynamoDB
- B. Amazon RDS
- C. Amazon ElastiCache
- D. Amazon Redshift

### 42. Users in twelve countries download large product images from one Region and complain about slow first loads. Which service should be added?

- A. Amazon CloudFront
- B. Amazon Route 53
- C. AWS Direct Connect
- D. Elastic Load Balancing

### 43. A company needs a private dedicated link from its own data centre into AWS and a managed DNS service for its public domain. Which two services fit? Select two.

- A. Amazon Route 53
- B. Amazon CloudFront
- C. Amazon API Gateway
- D. AWS Site-to-Site VPN
- E. AWS Direct Connect

### 44. A rule must flag any bucket that becomes public within minutes of the change. Which service evaluates resource configuration continuously?

- A. AWS Trusted Advisor
- B. Use AWS Config to record resource configuration changes
- C. Use AWS CloudTrail to record API activity
- D. Amazon CloudWatch

### 45. A team wants the same environment rebuilt identically in three accounts from one definition file. Which service fits?

- A. AWS Service Catalog
- B. AWS Systems Manager
- C. AWS Control Tower
- D. AWS CloudFormation

### 46. An order service must hand work to a payment service without waiting, and must survive a burst that the payment service cannot absorb instantly. Which service buffers the work?

- A. Amazon EventBridge
- B. Amazon SQS
- C. Amazon SNS
- D. AWS Step Functions

### 47. One alert must reach both an email list and a chat channel, and a three-step approval process must retry a failed step in order. Which two services fit? Select two.

- A. Amazon MQ
- B. Amazon SNS
- C. Amazon SQS
- D. AWS Step Functions
- E. Amazon Kinesis

### 48. Analysts want to run SQL over files already sitting in Amazon S3 without loading them into a warehouse or managing a cluster. Which service fits?

- A. Amazon Redshift
- B. AWS Glue
- C. Amazon EMR
- D. Amazon Athena

### 49. A product team wants to add a text assistant to its app using a foundation model, without operating GPU infrastructure. Which service fits?

- A. Amazon SageMaker
- B. Amazon Bedrock
- C. Amazon EMR
- D. Amazon QuickSight

### 50. A team wants every commit to compile the code and run its tests in a managed environment before anything is deployed. Which service performs that build?

- A. AWS CodeDeploy
- B. AWS CodePipeline
- C. AWS CloudFormation
- D. AWS CodeBuild

### 51. A request is slow and nobody can tell which of six services on its path is responsible. Which service traces the request across them?

- A. Amazon CloudWatch
- B. AWS Health Dashboard
- C. AWS X-Ray
- D. Use AWS CloudTrail to record API activity

### 52. A small team wants to upload application code and have capacity, load balancing and platform patching handled for it. Which service fits?

- A. AWS Elastic Beanstalk
- B. Amazon ECS or Amazon EKS with AWS Fargate
- C. Amazon EC2 instances
- D. AWS Lambda

### 53. A container image must run as a public web service without the team choosing instance types or scaling rules. Which service fits?

- A. Amazon EC2 instances
- B. AWS App Runner
- C. AWS Batch
- D. Amazon Lightsail

### 54. An alarm must fire when average CPU across a fleet stays above 80 percent for ten minutes. Which service provides the metric and the alarm?

- A. Use AWS Config to record resource configuration changes
- B. Amazon CloudWatch
- C. Use AWS CloudTrail to record API activity
- D. AWS X-Ray

### 55. An operations team wants a dashboard of AWS service events that affect its account and a record of every API call made during an incident. Which two services provide them? Select two.

- A. Use Amazon Inspector to scan workloads for vulnerabilities
- B. AWS X-Ray
- C. AWS Health Dashboard
- D. Use AWS CloudTrail to record API activity
- E. Amazon CloudWatch

### 56. A factory floor system must run AWS-managed compute inside the plant because round-trip latency to the nearest Region breaks the control loop. Which service fits?

- A. Edge locations for content delivery
- B. Local Zones for very low latency
- C. AWS Outposts for on-premises capacity
- D. AWS Wavelength for carrier networks

### 57. Sixty terabytes must reach AWS, and the office uplink would need months to transfer it. Which service fits?

- A. Amazon EFS file system
- B. AWS Snowball devices
- C. AWS Direct Connect
- D. AWS Storage Gateway

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. A rendering job can be interrupted and restarted without harm, and cost per compute hour is the binding constraint. Which purchasing option fits?

- A. Reserved Instances
- B. Spot Instances
- C. Dedicated Hosts
- D. On-Demand Instances

### 59. A steady production database will run unchanged for three years and the company wants the lowest committed rate. Which option fits?

- A. Dedicated Hosts
- B. Spot Instances
- C. Reserved Instances
- D. On-Demand Instances

### 60. Finance wants an alert before monthly spend crosses an agreed limit. Which tool fits?

- A. AWS Budgets
- B. AWS Cost and Usage Report
- C. AWS Cost Explorer
- D. AWS Pricing Calculator

### 61. A team must estimate the monthly cost of a design before building it, then later explain which service drove a spend increase. Which two tools fit? Select two.

- A. Wait for the monthly invoice and reconcile it afterwards
- B. AWS Budgets
- C. AWS Pricing Calculator
- D. AWS Cost Explorer
- E. Cost Anomaly Detection

### 62. A group of related accounts wants one invoice and to share the volume discounts their combined usage earns. What should be enabled?

- A. Consolidated billing in AWS Organizations
- B. AWS Cost and Usage Report
- C. Keep a separate bill and separate discounts per account
- D. Apply a service control policy in AWS Organizations

### 63. A company runs production workloads and needs 24/7 access to technical support with faster response times than a development-only plan provides. Which plan is the minimum that fits?

- A. AWS Basic Support
- B. AWS Developer Support
- C. AWS Enterprise Support
- D. AWS Business Support

### 64. An architect wants a vetted reference deployment for a common workload rather than a blank design. What should be used?

- A. Read the AWS documentation and service user guides
- B. Start from an AWS Solutions Library reference deployment
- C. Search AWS re:Post for an answered question
- D. Engage an AWS Partner for the delivery work

### 65. A new account wants to experiment within published monthly limits before any charge applies. What provides that?

- A. Volume discounts that grow with usage
- B. Pay-as-you-go pricing
- C. Savings Plans
- D. The AWS Free Tier allowances

---

## Answer key and explanations

### Question 1 — B

Answer: Elasticity: scale capacity with demand. Capacity follows measured demand, so the sale peak no longer needs servers that sit idle for the rest of the year. Capacity is added and removed as demand changes, so the company pays only for what it uses. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed services remove single points of failure that a company would otherwise have to engineer. Why the correct answer wins: Capacity follows measured demand, so the sale peak no longer needs servers that sit idle for the rest of the year.
- **B:** Correct. Capacity is added and removed as demand changes, so the company pays only for what it uses. In this case: Capacity follows measured demand, so the sale peak no longer needs servers that sit idle for the rest of the year.
- **C:** Incorrect for this question. Up-front data-centre investment is replaced by usage-based spending. Why the correct answer wins: Capacity follows measured demand, so the sale peak no longer needs servers that sit idle for the rest of the year.
- **D:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Capacity follows measured demand, so the sale peak no longer needs servers that sit idle for the rest of the year.

### Question 2 — D

Answer: Global reach: deploy into multiple Regions quickly. Regions and edge locations let the studio serve those countries without owning infrastructure in each one. A global infrastructure lets a company put workloads near its users without building facilities. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. AWS operates the facilities, hardware and managed platforms so the team can focus on its product. Why the correct answer wins: Regions and edge locations let the studio serve those countries without owning infrastructure in each one.
- **B:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Regions and edge locations let the studio serve those countries without owning infrastructure in each one.
- **C:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Regions and edge locations let the studio serve those countries without owning infrastructure in each one.
- **D:** Correct. A global infrastructure lets a company put workloads near its users without building facilities. In this case: Regions and edge locations let the studio serve those countries without owning infrastructure in each one.

### Question 3 — D

Answer: Estimate total cost of ownership including facilities and staff. A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the data centre. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the data centre.
- **B:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the data centre.
- **C:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the data centre.
- **D:** Correct. In this case: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the data centre.

### Question 4 — D

Answer: Pay-as-you-go pricing. Usage-based billing carries no up-front commitment, so cost rises and falls with consumption. There is no up-front commitment and the meter runs only while the resource exists. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Usage-based billing carries no up-front commitment, so cost rises and falls with consumption.
- **B:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Usage-based billing carries no up-front commitment, so cost rises and falls with consumption.
- **C:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Usage-based billing carries no up-front commitment, so cost rises and falls with consumption.
- **D:** Correct. There is no up-front commitment and the meter runs only while the resource exists. In this case: Usage-based billing carries no up-front commitment, so cost rises and falls with consumption.

### Question 5 — A

Answer: Loose coupling with a queue between tiers. A buffer between tiers stops a slow consumer from failing the producer request path. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. In this case: A buffer between tiers stops a slow consumer from failing the producer request path.
- **B:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A buffer between tiers stops a slow consumer from failing the producer request path.
- **C:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: A buffer between tiers stops a slow consumer from failing the producer request path.
- **D:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A buffer between tiers stops a slow consumer from failing the producer request path.

### Question 6 — C

Answer: Serverless compute for intermittent work. Work triggered by an event, with no server held between runs, is the serverless pattern. No server is provisioned, and the service runs only when it is invoked. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Work triggered by an event, with no server held between runs, is the serverless pattern.
- **B:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: Work triggered by an event, with no server held between runs, is the serverless pattern.
- **C:** Correct. No server is provisioned, and the service runs only when it is invoked. In this case: Work triggered by an event, with no server held between runs, is the serverless pattern.
- **D:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Work triggered by an event, with no server held between runs, is the serverless pattern.

### Question 7 — A

Answer: Reliability pillar. The reliability pillar asks how a workload behaves when a component or an entire Availability Zone is lost. The pillar about recovering from failure and meeting demand consistently. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The pillar about recovering from failure and meeting demand consistently. In this case: The reliability pillar asks how a workload behaves when a component or an entire Availability Zone is lost.
- **B:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: The reliability pillar asks how a workload behaves when a component or an entire Availability Zone is lost.
- **C:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The reliability pillar asks how a workload behaves when a component or an entire Availability Zone is lost.
- **D:** Incorrect for this question. The pillar about running and improving workloads, including automation and small reversible changes. Why the correct answer wins: The reliability pillar asks how a workload behaves when a component or an entire Availability Zone is lost.

### Question 8 — C, E

Answers: Operational excellence pillar; Cost optimization pillar. Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price. The pillar about running and improving workloads, including automation and small reversible changes. The pillar about delivering value at the lowest price that meets the requirement. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price.
- **B:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price.
- **C:** Correct. The pillar about running and improving workloads, including automation and small reversible changes. In this case: Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price.
- **D:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price.
- **E:** Correct. The pillar about delivering value at the lowest price that meets the requirement. In this case: Operational excellence covers how changes are made and reversed, and cost optimization covers value delivered at the lowest viable price.

### Question 9 — B

Answer: Governance perspective of the AWS Cloud Adoption Framework. The governance perspective covers prioritisation, budgeting and measuring the programme against business outcomes. The perspective about prioritising, budgeting and measuring the cloud programme. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about skills, roles and organisational change. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme against business outcomes.
- **B:** Correct. The perspective about prioritising, budgeting and measuring the cloud programme. In this case: The governance perspective covers prioritisation, budgeting and measuring the programme against business outcomes.
- **C:** Incorrect for this question. The perspective about running, monitoring and supporting workloads day to day. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme against business outcomes.
- **D:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The governance perspective covers prioritisation, budgeting and measuring the programme against business outcomes.

### Question 10 — C

Answer: People perspective of the AWS Cloud Adoption Framework. The people perspective covers skills, training, roles and the organisational change that adoption requires. The perspective about skills, roles and organisational change. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The people perspective covers skills, training, roles and the organisational change that adoption requires.
- **B:** Incorrect for this question. The perspective about meeting security and compliance objectives. Why the correct answer wins: The people perspective covers skills, training, roles and the organisational change that adoption requires.
- **C:** Correct. The perspective about skills, roles and organisational change. In this case: The people perspective covers skills, training, roles and the organisational change that adoption requires.
- **D:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The people perspective covers skills, training, roles and the organisational change that adoption requires.

### Question 11 — A

Answer: Retain: keep the workload where it is. Retain keeps a workload where it is when a move is not justified yet, and the rest of the estate can move independently. The workload stays in place because moving it is not justified yet. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The workload stays in place because moving it is not justified yet. In this case: Retain keeps a workload where it is when a move is not justified yet, and the rest of the estate can move independently.
- **B:** Incorrect for this question. The company replaces the application with a commercially available equivalent. Why the correct answer wins: Retain keeps a workload where it is when a move is not justified yet, and the rest of the estate can move independently.
- **C:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Retain keeps a workload where it is when a move is not justified yet, and the rest of the estate can move independently.
- **D:** Incorrect for this question. The workload is no longer needed, so it is decommissioned instead of migrated. Why the correct answer wins: Retain keeps a workload where it is when a move is not justified yet, and the rest of the estate can move independently.

### Question 12 — C

Answer: Repurchase: move to a different product. Repurchase moves to a different product rather than moving the existing application. The company replaces the application with a commercially available equivalent. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. Why the correct answer wins: Repurchase moves to a different product rather than moving the existing application.
- **B:** Incorrect for this question. The whole platform moves to a hosted equivalent without changing the application itself. Why the correct answer wins: Repurchase moves to a different product rather than moving the existing application.
- **C:** Correct. The company replaces the application with a commercially available equivalent. In this case: Repurchase moves to a different product rather than moving the existing application.
- **D:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Repurchase moves to a different product rather than moving the existing application.

### Question 13 — C

Answer: Regions and Availability Zones. A Region contains several isolated Availability Zones, so spreading across them survives the loss of one building. A Region is a geographic area and each Availability Zone within it is an isolated group of data centres. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: A Region contains several isolated Availability Zones, so spreading across them survives the loss of one building.
- **B:** Incorrect for this question. A rack of AWS infrastructure installed in the customer facility and operated through AWS. Why the correct answer wins: A Region contains several isolated Availability Zones, so spreading across them survives the loss of one building.
- **C:** Correct. A Region is a geographic area and each Availability Zone within it is an isolated group of data centres. In this case: A Region contains several isolated Availability Zones, so spreading across them survives the loss of one building.
- **D:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: A Region contains several isolated Availability Zones, so spreading across them survives the loss of one building.

### Question 14 — A

Answer: Deploy across multiple Availability Zones. Deploying across multiple Availability Zones leaves a survivor when one Zone fails. Two or more Zones give the workload a survivor when one Zone fails. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: Deploying across multiple Availability Zones leaves a survivor when one Zone fails.
- **B:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Deploying across multiple Availability Zones leaves a survivor when one Zone fails.
- **C:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Deploying across multiple Availability Zones leaves a survivor when one Zone fails.
- **D:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Deploying across multiple Availability Zones leaves a survivor when one Zone fails.

### Question 15 — C, D

Answers: Scale out automatically as demand rises; Deploy across multiple Availability Zones. Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails. Capacity follows the measured demand rather than a forecast. Two or more Zones give the workload a survivor when one Zone fails. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails.
- **B:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails.
- **C:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails.
- **D:** Correct. Capacity follows the measured demand rather than a forecast. In this case: Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails.
- **E:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Automatic scaling follows demand without an operator, and a multi-Zone deployment keeps serving traffic when one Zone fails.

### Question 16 — D

Answer: The customer is responsible for patching the guest operating system on Amazon EC2. The guest operating system sits above the hypervisor, so patching it belongs to the customer. The instance is the customer layer, so its operating system and applications are the customer job. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: The guest operating system sits above the hypervisor, so patching it belongs to the customer.
- **B:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: The guest operating system sits above the hypervisor, so patching it belongs to the customer.
- **C:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: The guest operating system sits above the hypervisor, so patching it belongs to the customer.
- **D:** Correct. The instance is the customer layer, so its operating system and applications are the customer job. In this case: The guest operating system sits above the hypervisor, so patching it belongs to the customer.

### Question 17 — C

Answer: Grant only the permissions the task needs. Granting only the actions the task requires keeps the blast radius of a mistake or a stolen credential small. Starting from the minimum and adding as needed keeps the blast radius small. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Broad standing access means one mistaken action or stolen credential can change anything. Why the correct answer wins: Granting only the actions the task requires keeps the blast radius of a mistake or a stolen credential small.
- **B:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Granting only the actions the task requires keeps the blast radius of a mistake or a stolen credential small.
- **C:** Correct. Starting from the minimum and adding as needed keeps the blast radius small. In this case: Granting only the actions the task requires keeps the blast radius of a mistake or a stolen credential small.
- **D:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: Granting only the actions the task requires keeps the blast radius of a mistake or a stolen credential small.

### Question 18 — C

Answer: Put the users in a group and attach the policy to the group. A group holds the shared policy once, so a quarterly change is made in a single place. A group is a collection of users that share permissions, which keeps the policy in one place. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: A group holds the shared policy once, so a quarterly change is made in a single place.
- **B:** Incorrect for this question. A role hands out temporary credentials, so nothing long-lived is stored. Why the correct answer wins: A group holds the shared policy once, so a quarterly change is made in a single place.
- **C:** Correct. A group is a collection of users that share permissions, which keeps the policy in one place. In this case: A group holds the shared policy once, so a quarterly change is made in a single place.
- **D:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: A group holds the shared policy once, so a quarterly change is made in a single place.

### Question 19 — C

Answer: Enable MFA and delete the root access keys. The root user cannot be limited by policy, so it is protected with multi-factor authentication and its access keys are removed. The root user is the most privileged identity, so it is protected and its keys are removed. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: The root user cannot be limited by policy, so it is protected with multi-factor authentication and its access keys are removed.
- **B:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: The root user cannot be limited by policy, so it is protected with multi-factor authentication and its access keys are removed.
- **C:** Correct. The root user is the most privileged identity, so it is protected and its keys are removed. In this case: The root user cannot be limited by policy, so it is protected with multi-factor authentication and its access keys are removed.
- **D:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: The root user cannot be limited by policy, so it is protected with multi-factor authentication and its access keys are removed.

### Question 20 — D

Answer: Rotate access keys on a schedule. A rotation schedule limits how long a leaked key stays useful, and old keys stop working. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: A rotation schedule limits how long a leaked key stays useful, and old keys stop working.
- **B:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: A rotation schedule limits how long a leaked key stays useful, and old keys stop working.
- **C:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A rotation schedule limits how long a leaked key stays useful, and old keys stop working.
- **D:** Correct. In this case: A rotation schedule limits how long a leaked key stays useful, and old keys stop working.

### Question 21 — D

Answer: Create an IAM role and let the workload assume it. A role supplies temporary credentials to the workload, so nothing long-lived is written to disk. A role hands out temporary credentials, so nothing long-lived is stored. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: A role supplies temporary credentials to the workload, so nothing long-lived is written to disk.
- **B:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A role supplies temporary credentials to the workload, so nothing long-lived is written to disk.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: A role supplies temporary credentials to the workload, so nothing long-lived is written to disk.
- **D:** Correct. A role hands out temporary credentials, so nothing long-lived is stored. In this case: A role supplies temporary credentials to the workload, so nothing long-lived is written to disk.

### Question 22 — B

Answer: Federate the company directory into AWS. Federating the directory uses existing corporate identities instead of a separate set of AWS credentials. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: Federating the directory uses existing corporate identities instead of a separate set of AWS credentials.
- **B:** Correct. In this case: Federating the directory uses existing corporate identities instead of a separate set of AWS credentials.
- **C:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: Federating the directory uses existing corporate identities instead of a separate set of AWS credentials.
- **D:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Federating the directory uses existing corporate identities instead of a separate set of AWS credentials.

### Question 23 — B

Answer: Use a security group as a stateful instance firewall. A security group allows only the stated inbound traffic and remembers the connection state. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. An open perimeter exposes every service on the host, including ones nobody meant to publish. Why the correct answer wins: A security group allows only the stated inbound traffic and remembers the connection state.
- **B:** Correct. In this case: A security group allows only the stated inbound traffic and remembers the connection state.
- **C:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: A security group allows only the stated inbound traffic and remembers the connection state.
- **D:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: A security group allows only the stated inbound traffic and remembers the connection state.

### Question 24 — A, D

Answers: Use AWS WAF to block web attack patterns; Use AWS Shield for DDoS protection. WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Shield absorbs distributed denial-of-service traffic before it reaches the application. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Shield absorbs distributed denial-of-service traffic before it reaches the application. In this case: WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic.
- **B:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic.
- **C:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic.
- **D:** Correct. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. In this case: WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic.
- **E:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: WAF inspects HTTP requests against attack patterns, and Shield absorbs distributed denial-of-service traffic.

### Question 25 — C

Answer: Use a customer managed key for the required control. A customer managed key puts the key policy and the revocation decision in the company hands. The customer controls the key policy and can revoke access by disabling the key. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision in the company hands.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision in the company hands.
- **C:** Correct. The customer controls the key policy and can revoke access by disabling the key. In this case: A customer managed key puts the key policy and the revocation decision in the company hands.
- **D:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision in the company hands.

### Question 26 — A

Answer: Encrypt data in transit with TLS. Encryption in transit with TLS protects the data while it crosses the network. Traffic is protected while it crosses the network, not only while it sits on disk. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Traffic is protected while it crosses the network, not only while it sits on disk. In this case: Encryption in transit with TLS protects the data while it crosses the network.
- **B:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Encryption in transit with TLS protects the data while it crosses the network.
- **C:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: Encryption in transit with TLS protects the data while it crosses the network.
- **D:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: Encryption in transit with TLS protects the data while it crosses the network.

### Question 27 — A

Answer: Store the database credential in AWS Secrets Manager and rotate it. A managed secret store holds the credential centrally and can rotate it on a schedule. The secret is held centrally and can be rotated on a schedule. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The secret is held centrally and can be rotated on a schedule. In this case: A managed secret store holds the credential centrally and can rotate it on a schedule.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A managed secret store holds the credential centrally and can rotate it on a schedule.
- **C:** Incorrect for this question. A credential in source code is copied to every environment and cannot be rotated quietly. Why the correct answer wins: A managed secret store holds the credential centrally and can rotate it on a schedule.
- **D:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A managed secret store holds the credential centrally and can rotate it on a schedule.

### Question 28 — A

Answer: Use Amazon GuardDuty to detect suspicious activity. GuardDuty analyses account, network and DNS activity for signs of compromise. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **B:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **D:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.

### Question 29 — B, C

Answers: Use Amazon Inspector to scan workloads for vulnerabilities; Use Amazon Macie to find sensitive data in Amazon S3. Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Macie classifies objects and reports where personal or sensitive data is stored. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Security Hub collects findings from the security services and scores them against a standard. Why the correct answer wins: Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits.
- **B:** Correct. Macie classifies objects and reports where personal or sensitive data is stored. In this case: Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits.
- **C:** Correct. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. In this case: Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits.
- **D:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits.
- **E:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Inspector reports software vulnerabilities, and Macie classifies objects to show where sensitive data sits.

### Question 30 — C

Answer: An Amazon S3 bucket policy that grants public read. The bucket policy decides who may read the objects, so a public grant there exposes the whole dataset. A public bucket policy exposes every object in the bucket to anyone on the internet. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: The bucket policy decides who may read the objects, so a public grant there exposes the whole dataset.
- **B:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: The bucket policy decides who may read the objects, so a public grant there exposes the whole dataset.
- **C:** Correct. A public bucket policy exposes every object in the bucket to anyone on the internet. In this case: The bucket policy decides who may read the objects, so a public grant there exposes the whole dataset.
- **D:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: The bucket policy decides who may read the objects, so a public grant there exposes the whole dataset.

### Question 31 — A

Answer: Use Amazon Macie to find sensitive data in Amazon S3. Macie inspects objects and reports where sensitive data is stored. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Macie inspects objects and reports where sensitive data is stored.
- **B:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Macie inspects objects and reports where sensitive data is stored.
- **C:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Macie inspects objects and reports where sensitive data is stored.
- **D:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Macie inspects objects and reports where sensitive data is stored.

### Question 32 — C

Answer: Download the compliance reports from AWS Artifact. Artifact provides AWS audit reports and compliance agreements on demand. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Artifact provides AWS audit reports and compliance agreements on demand.
- **B:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: Artifact provides AWS audit reports and compliance agreements on demand.
- **C:** Correct. In this case: Artifact provides AWS audit reports and compliance agreements on demand.
- **D:** Incorrect for this question. Audit Manager assembles evidence against a chosen framework. Why the correct answer wins: Artifact provides AWS audit reports and compliance agreements on demand.

### Question 33 — B, E

Answers: Use AWS CloudTrail to record API activity; Use AWS Config to record resource configuration changes. CloudTrail records the API call and its caller, and Config keeps the configuration history. CloudTrail logs who called which API, when and from where. Config keeps a history of configuration and evaluates it against rules. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: CloudTrail records the API call and its caller, and Config keeps the configuration history.
- **B:** Correct. CloudTrail logs who called which API, when and from where. In this case: CloudTrail records the API call and its caller, and Config keeps the configuration history.
- **C:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: CloudTrail records the API call and its caller, and Config keeps the configuration history.
- **D:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: CloudTrail records the API call and its caller, and Config keeps the configuration history.
- **E:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: CloudTrail records the API call and its caller, and Config keeps the configuration history.

### Question 34 — D

Answer: AWS is responsible for patching a managed service such as Amazon S3. AWS operates the managed database engine, including its patches, while the customer keeps the data and access choices. The service itself is operated by AWS, including its underlying platform patches. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: AWS operates the managed database engine, including its patches, while the customer keeps the data and access choices.
- **B:** Incorrect for this question. Classification, access and protection of the data remain with the customer. Why the correct answer wins: AWS operates the managed database engine, including its patches, while the customer keeps the data and access choices.
- **C:** Incorrect for this question. The instance is the customer layer, so its operating system and applications are the customer job. Why the correct answer wins: AWS operates the managed database engine, including its patches, while the customer keeps the data and access choices.
- **D:** Correct. The service itself is operated by AWS, including its underlying platform patches. In this case: AWS operates the managed database engine, including its patches, while the customer keeps the data and access choices.

### Question 35 — D

Answer: Apply a service control policy in AWS Organizations. A service control policy sets the maximum permissions for the accounts beneath it. An SCP sets the maximum permissions available to the accounts under it. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: A service control policy sets the maximum permissions for the accounts beneath it.
- **B:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: A service control policy sets the maximum permissions for the accounts beneath it.
- **C:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: A service control policy sets the maximum permissions for the accounts beneath it.
- **D:** Correct. An SCP sets the maximum permissions available to the accounts under it. In this case: A service control policy sets the maximum permissions for the accounts beneath it.

### Question 36 — C

Answer: AWS Lambda. Lambda runs the code on the event and keeps no server between invocations. Run code on an event without provisioning or managing a server. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: Lambda runs the code on the event and keeps no server between invocations.
- **B:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lambda runs the code on the event and keeps no server between invocations.
- **C:** Correct. Run code on an event without provisioning or managing a server. In this case: Lambda runs the code on the event and keeps no server between invocations.
- **D:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Lambda runs the code on the event and keeps no server between invocations.

### Question 37 — A

Answer: Amazon EC2 instances. Amazon EC2 gives the customer control of the guest operating system and its kernel. Virtual servers where the customer controls the operating system and the runtime. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Virtual servers where the customer controls the operating system and the runtime. In this case: Amazon EC2 gives the customer control of the guest operating system and its kernel.
- **B:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: Amazon EC2 gives the customer control of the guest operating system and its kernel.
- **C:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Amazon EC2 gives the customer control of the guest operating system and its kernel.
- **D:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: Amazon EC2 gives the customer control of the guest operating system and its kernel.

### Question 38 — B

Answer: Amazon S3 Glacier storage classes. An archive storage class is priced for rarely read data that tolerates retrieval time. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: An archive storage class is priced for rarely read data that tolerates retrieval time.
- **B:** Correct. In this case: An archive storage class is priced for rarely read data that tolerates retrieval time.
- **C:** Incorrect for this question. Object storage for frequently accessed data with high durability and availability. Why the correct answer wins: An archive storage class is priced for rarely read data that tolerates retrieval time.
- **D:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: An archive storage class is priced for rarely read data that tolerates retrieval time.

### Question 39 — A, D

Answers: Amazon EFS file system; Amazon S3 Glacier storage classes. EFS is a shared Linux file system, and an archive class holds the finished frames at low cost. A shared file system that many Linux instances can mount at the same time. Archive storage for data that is rarely read and tolerates retrieval time. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Archive storage for data that is rarely read and tolerates retrieval time. In this case: EFS is a shared Linux file system, and an archive class holds the finished frames at low cost.
- **B:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: EFS is a shared Linux file system, and an archive class holds the finished frames at low cost.
- **C:** Incorrect for this question. Physical devices that move large datasets into AWS when the network is the bottleneck. Why the correct answer wins: EFS is a shared Linux file system, and an archive class holds the finished frames at low cost.
- **D:** Correct. A shared file system that many Linux instances can mount at the same time. In this case: EFS is a shared Linux file system, and an archive class holds the finished frames at low cost.
- **E:** Incorrect for this question. Managed file systems for Windows or high-performance workloads. Why the correct answer wins: EFS is a shared Linux file system, and an archive class holds the finished frames at low cost.

### Question 40 — B

Answer: Amazon RDS. Amazon RDS handles patching, backups and optional failover for the engine it manages. A managed relational database where AWS handles patching, backups and failover options. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Amazon RDS handles patching, backups and optional failover for the engine it manages.
- **B:** Correct. A managed relational database where AWS handles patching, backups and failover options. In this case: Amazon RDS handles patching, backups and optional failover for the engine it manages.
- **C:** Incorrect for this question. A managed key-value and document store for high-volume, predictable-latency access. Why the correct answer wins: Amazon RDS handles patching, backups and optional failover for the engine it manages.
- **D:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Amazon RDS handles patching, backups and optional failover for the engine it manages.

### Question 41 — A

Answer: Amazon DynamoDB. DynamoDB is a managed key-value store built for high-volume, predictable-latency access. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **B:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **C:** Incorrect for this question. A managed in-memory cache for sub-millisecond reads of hot data. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **D:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.

### Question 42 — A

Answer: Amazon CloudFront. CloudFront caches content at edge locations close to those users. A content delivery network that caches content at edge locations near users. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A content delivery network that caches content at edge locations near users. In this case: CloudFront caches content at edge locations close to those users.
- **B:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: CloudFront caches content at edge locations close to those users.
- **C:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: CloudFront caches content at edge locations close to those users.
- **D:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: CloudFront caches content at edge locations close to those users.

### Question 43 — A, E

Answers: AWS Direct Connect; Amazon Route 53. Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records. A dedicated private network connection from a customer facility into AWS. A managed DNS service that also supports health checks and routing policies. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed DNS service that also supports health checks and routing policies. In this case: Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records.
- **B:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records.
- **C:** Incorrect for this question. A managed front door for APIs with throttling, authorisation and usage plans. Why the correct answer wins: Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records.
- **D:** Incorrect for this question. An encrypted tunnel over the internet between a customer network and a VPC. Why the correct answer wins: Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records.
- **E:** Correct. A dedicated private network connection from a customer facility into AWS. In this case: Direct Connect provides the dedicated private link, and Route 53 hosts the public DNS records.

### Question 44 — B

Answer: Use AWS Config to record resource configuration changes. Config records configuration and evaluates it against rules as changes happen. Config keeps a history of configuration and evaluates it against rules. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Checks an account against best practices for cost, security, limits and resilience. Why the correct answer wins: Config records configuration and evaluates it against rules as changes happen.
- **B:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: Config records configuration and evaluates it against rules as changes happen.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Config records configuration and evaluates it against rules as changes happen.
- **D:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: Config records configuration and evaluates it against rules as changes happen.

### Question 45 — D

Answer: AWS CloudFormation. CloudFormation creates and updates resources from a template, so every account gets the same result. Infrastructure defined as a template and created or updated as a stack. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every account gets the same result.
- **B:** Incorrect for this question. Operations tooling for patching, running commands and inventory across managed nodes. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every account gets the same result.
- **C:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every account gets the same result.
- **D:** Correct. Infrastructure defined as a template and created or updated as a stack. In this case: CloudFormation creates and updates resources from a template, so every account gets the same result.

### Question 46 — B

Answer: Amazon SQS. A queue decouples the two services and holds the burst until the consumer catches up. A managed queue that decouples producers from consumers and buffers bursts. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: A queue decouples the two services and holds the burst until the consumer catches up.
- **B:** Correct. A managed queue that decouples producers from consumers and buffers bursts. In this case: A queue decouples the two services and holds the burst until the consumer catches up.
- **C:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: A queue decouples the two services and holds the burst until the consumer catches up.
- **D:** Incorrect for this question. A state machine that coordinates multi-step workflows with retries and branching. Why the correct answer wins: A queue decouples the two services and holds the burst until the consumer catches up.

### Question 47 — B, D

Answers: Amazon SNS; AWS Step Functions. SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries. A pub/sub topic that fans a message out to many subscribers. A state machine that coordinates multi-step workflows with retries and branching. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed message broker for existing protocols such as AMQP or MQTT. Why the correct answer wins: SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries.
- **B:** Correct. A pub/sub topic that fans a message out to many subscribers. In this case: SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries.
- **C:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries.
- **D:** Correct. A state machine that coordinates multi-step workflows with retries and branching. In this case: SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries.
- **E:** Incorrect for this question. Streaming data ingestion and processing for continuous records. Why the correct answer wins: SNS fans a message out to many subscribers, and Step Functions coordinates the ordered steps with retries.

### Question 48 — D

Answer: Amazon Athena. Athena queries the objects in place with SQL and no infrastructure to run. Query data in Amazon S3 with SQL and no infrastructure to manage. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **B:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **C:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Athena queries the objects in place with SQL and no infrastructure to run.
- **D:** Correct. Query data in Amazon S3 with SQL and no infrastructure to manage. In this case: Athena queries the objects in place with SQL and no infrastructure to run.

### Question 49 — B

Answer: Amazon Bedrock. Bedrock exposes foundation models through an API so the team never runs the model hosts. Access foundation models through an API without operating the model infrastructure. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Build, train and deploy machine learning models through a managed platform. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **B:** Correct. Access foundation models through an API without operating the model infrastructure. In this case: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **C:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.
- **D:** Incorrect for this question. A managed business intelligence service for dashboards and reports. Why the correct answer wins: Bedrock exposes foundation models through an API so the team never runs the model hosts.

### Question 50 — D

Answer: AWS CodeBuild. CodeBuild runs the compile and test steps in a managed build environment. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **B:** Incorrect for this question. Orchestrates the build, test and deploy stages of a release. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **C:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: CodeBuild runs the compile and test steps in a managed build environment.
- **D:** Correct. In this case: CodeBuild runs the compile and test steps in a managed build environment.

### Question 51 — C

Answer: AWS X-Ray. X-Ray traces a request through a distributed application and shows where the time goes. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: X-Ray traces a request through a distributed application and shows where the time goes.
- **B:** Incorrect for this question. Service health and event notifications that affect the account. Why the correct answer wins: X-Ray traces a request through a distributed application and shows where the time goes.
- **C:** Correct. In this case: X-Ray traces a request through a distributed application and shows where the time goes.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: X-Ray traces a request through a distributed application and shows where the time goes.

### Question 52 — A

Answer: AWS Elastic Beanstalk. Elastic Beanstalk provisions and manages the environment around the uploaded application. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **B:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.
- **D:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Elastic Beanstalk provisions and manages the environment around the uploaded application.

### Question 53 — B

Answer: AWS App Runner. App Runner runs the container and manages the capacity and scaling behind it. Run a containerised web service without choosing or managing the underlying capacity. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **B:** Correct. Run a containerised web service without choosing or managing the underlying capacity. In this case: App Runner runs the container and manages the capacity and scaling behind it.
- **C:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.
- **D:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: App Runner runs the container and manages the capacity and scaling behind it.

### Question 54 — B

Answer: Amazon CloudWatch. CloudWatch collects the metrics and evaluates the alarm. Metrics, logs and alarms for the resources and applications in the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch collects the metrics and evaluates the alarm.
- **B:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch collects the metrics and evaluates the alarm.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch collects the metrics and evaluates the alarm.
- **D:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudWatch collects the metrics and evaluates the alarm.

### Question 55 — C, D

Answers: AWS Health Dashboard; Use AWS CloudTrail to record API activity. The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls. Service health and event notifications that affect the account. CloudTrail logs who called which API, when and from where. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls.
- **B:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls.
- **C:** Correct. Service health and event notifications that affect the account. In this case: The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls.
- **D:** Correct. CloudTrail logs who called which API, when and from where. In this case: The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls.
- **E:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: The Health Dashboard shows service events affecting the account, and CloudTrail records the API calls.

### Question 56 — C

Answer: AWS Outposts for on-premises capacity. Outposts installs AWS infrastructure in the customer facility and operates it through AWS. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **B:** Incorrect for this question. An extension of a Region placed close to a large population or industry centre. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **C:** Correct. In this case: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **D:** Incorrect for this question. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.

### Question 57 — B

Answer: AWS Snowball devices. A Snowball device moves the data physically, which beats a slow network for a one-off transfer. Physical devices that move large datasets into AWS when the network is the bottleneck. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: A Snowball device moves the data physically, which beats a slow network for a one-off transfer.
- **B:** Correct. Physical devices that move large datasets into AWS when the network is the bottleneck. In this case: A Snowball device moves the data physically, which beats a slow network for a one-off transfer.
- **C:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: A Snowball device moves the data physically, which beats a slow network for a one-off transfer.
- **D:** Incorrect for this question. A hybrid file, volume or tape interface that keeps frequently used data on premises. Why the correct answer wins: A Snowball device moves the data physically, which beats a slow network for a one-off transfer.

### Question 58 — B

Answer: Spot Instances. Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **B:** Correct. In this case: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **C:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **D:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.

### Question 59 — C

Answer: Reserved Instances. A multi-year commitment lowers the hourly rate in exchange for the commitment. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: A multi-year commitment lowers the hourly rate in exchange for the commitment.
- **B:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: A multi-year commitment lowers the hourly rate in exchange for the commitment.
- **C:** Correct. In this case: A multi-year commitment lowers the hourly rate in exchange for the commitment.
- **D:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: A multi-year commitment lowers the hourly rate in exchange for the commitment.

### Question 60 — A

Answer: AWS Budgets. Budgets tracks spend against a threshold and alerts when it is crossed. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: Budgets tracks spend against a threshold and alerts when it is crossed.
- **B:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **C:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **D:** Incorrect for this question. Estimate the cost of a planned architecture before it is built. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.

### Question 61 — C, D

Answers: AWS Pricing Calculator; AWS Cost Explorer. The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent. Estimate the cost of a planned architecture before it is built. Visualise and analyse past spend and forecast what is coming. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent.
- **B:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent.
- **C:** Correct. Estimate the cost of a planned architecture before it is built. In this case: The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent.
- **D:** Correct. Visualise and analyse past spend and forecast what is coming. In this case: The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent.
- **E:** Incorrect for this question. Machine learning alerts on spending that deviates from the expected pattern. Why the correct answer wins: The Pricing Calculator estimates a planned architecture, and Cost Explorer analyses what was actually spent.

### Question 62 — A

Answer: Consolidated billing in AWS Organizations. Consolidated billing puts the accounts on one bill and pools usage for discounts. One bill for all accounts, with usage aggregated so volume discounts are shared. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. One bill for all accounts, with usage aggregated so volume discounts are shared. In this case: Consolidated billing puts the accounts on one bill and pools usage for discounts.
- **B:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Consolidated billing puts the accounts on one bill and pools usage for discounts.
- **C:** Incorrect for this question. Separate accounts do not pool usage, so each misses the discounts the total would earn. Why the correct answer wins: Consolidated billing puts the accounts on one bill and pools usage for discounts.
- **D:** Incorrect for this question. An SCP sets the maximum permissions available to the accounts under it. Why the correct answer wins: Consolidated billing puts the accounts on one bill and pools usage for discounts.

### Question 63 — D

Answer: AWS Business Support. Business Support adds 24/7 production support and faster response than Basic or Developer. Production support with 24/7 access, faster response and Trusted Advisor checks. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Account and billing support with documentation and health checks, at no charge. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **B:** Incorrect for this question. Business-hours email support for development and test workloads. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **C:** Incorrect for this question. Mission-critical support with a designated technical account manager and the fastest response. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **D:** Correct. Production support with 24/7 access, faster response and Trusted Advisor checks. In this case: Business Support adds 24/7 production support and faster response than Basic or Developer.

### Question 64 — B

Answer: Start from an AWS Solutions Library reference deployment. The Solutions Library publishes vetted reference architectures and deployments. A vetted reference architecture shortens design work for a common workload. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The reference documentation states what a service does and how it is configured. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.
- **B:** Correct. A vetted reference architecture shortens design work for a common workload. In this case: The Solutions Library publishes vetted reference architectures and deployments.
- **C:** Incorrect for this question. The community knowledge base holds answers to common service and account questions. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.
- **D:** Incorrect for this question. Partners are third-party firms with AWS-validated skills for implementation work. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.

### Question 65 — D

Answer: The AWS Free Tier allowances. The Free Tier publishes monthly allowances for eligible services on a qualifying account. Limited monthly usage at no charge for eligible services on a new or qualifying account. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **B:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **C:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **D:** Correct. Limited monthly usage at no charge for eligible services on a new or qualifying account. In this case: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
