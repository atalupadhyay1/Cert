# AWS Certified Cloud Practitioner (CLF-C02) — Full-Length Mock Exam 6

Cloud Practitioner · 65 questions · 90 minutes · scaled passing score 700 of 1000

Blueprint-weighted mock exam. Item mix: 55 multiple-choice and 10 multiple-response items (the selection count is stated in each multi-response stem). The live exam publishes 65 questions in 90 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 10-item multi-response block is an authoring choice. At 65 items in 90 minutes this set matches live pacing at about 83 seconds per item. The live exam has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Cloud Concepts (24%) — Cloud Value, Economics, and the Shared Responsibility Model

### 1. A shooter peaks at forty thousand concurrent players on launch night and settles at three thousand the following week. Which cloud benefit covers that demand shape?

- A. Trade capital expense for variable expense
- B. A flat monthly fee that does not change with usage
- C. Keep ownership of the physical data centre
- D. Elasticity: scale capacity with demand

### 2. A two-person studio wants a playable prototype in testers' hands this week to decide whether the idea is worth funding. Which benefit matters most?

- A. Keep ownership of the physical data centre
- B. Reliability through managed, redundant infrastructure
- C. Buy servers up front and depreciate them
- D. Agility: provision resources in minutes

### 3. A studio compares keeping its colocation racks with moving the same workload to AWS. What must be estimated for the colocation option?

- A. Estimate total cost of ownership including facilities and staff
- B. A flat monthly fee that does not change with usage
- C. Volume discounts that grow with usage
- D. Pay-as-you-go pricing

### 4. A pre-revenue startup wants to owe nothing in a month when it runs no infrastructure at all. Which pricing characteristic delivers that?

- A. A flat monthly fee that does not change with usage
- B. Pay-as-you-go pricing
- C. Dedicated Hosts
- D. Reserved Instances

### 5. Matchmaking freezes whenever the leaderboard service is slow, because each matchmaking request waits for a leaderboard write. Which principle should be applied?

- A. Loose coupling with a queue between tiers
- B. Scale the single monolith vertically only
- C. Deploy across multiple Availability Zones
- D. Direct synchronous calls between every tier

### 6. A studio cannot ship a chat improvement without redeploying the whole game backend and retesting every feature. Which design change would help?

- A. Break the application into small independent services
- B. Automate repeated provisioning instead of rebuilding by hand
- C. Scale the single monolith vertically only
- D. Direct synchronous calls between every tier

### 7. A publisher must report how it is reducing the energy its always-on game backend consumes. Which Well-Architected pillar covers that?

- A. Security pillar
- B. Sustainability pillar
- C. Operational excellence pillar
- D. Cost optimization pillar

### 8. A studio must automate its deployments so they are repeatable, and must show that instance families were chosen from measured demand. Which two pillars apply? Select two.

- A. Performance efficiency pillar
- B. Reliability pillar
- C. Security pillar
- D. Sustainability pillar
- E. Operational excellence pillar

### 9. A growing studio needs a multi-account structure and shared networking before three game teams start building. Which perspective delivers that?

- A. Platform perspective of the AWS Cloud Adoption Framework
- B. People perspective of the AWS Cloud Adoption Framework
- C. Governance perspective of the AWS Cloud Adoption Framework
- D. Business perspective of the AWS Cloud Adoption Framework

### 10. After a lift-and-shift the studio has no on-call rotation, no runbooks and no monitoring ownership. Which perspective has been neglected?

- A. Governance perspective of the AWS Cloud Adoption Framework
- B. Platform perspective of the AWS Cloud Adoption Framework
- C. Business perspective of the AWS Cloud Adoption Framework
- D. Operations perspective of the AWS Cloud Adoption Framework

### 11. A self-managed streaming cluster will move to a managed service with small code changes and no application redesign. Which strategy is this?

- A. Retain: keep the workload where it is
- B. Replatform: change a few managed components on the way
- C. Refactor: redesign the application for cloud architecture
- D. Rehost: move the application as it is

### 12. A studio replaces its in-house payroll application with a SaaS product rather than moving the old one. Which strategy is this?

- A. Retain: keep the workload where it is
- B. Relocate: move the platform to a cloud-native equivalent
- C. Repurchase: move to a different product
- D. Rehost: move the application as it is

### 13. A remote substation must run AWS-managed compute on site because the round trip to the nearest Region is too slow for its control loop. Which service fits?

- A. Edge locations for content delivery
- B. AWS Outposts for on-premises capacity
- C. Local Zones for very low latency
- D. AWS Wavelength for carrier networks

### 14. Concurrency climbs every evening and collapses after midnight, and an engineer currently adds servers by hand each afternoon. What should replace that routine?

- A. Place everything in one Availability Zone
- B. Direct synchronous calls between every tier
- C. Scale the single monolith vertically only
- D. Scale out automatically as demand rises

### 15. The leaderboard must keep serving when a data-centre building is lost, and the studio must state how quickly it can restore service after losing a Region. Which two choices fit? Select two.

- A. Deploy across multiple Availability Zones
- B. Place everything in one Availability Zone
- C. Scale the single monolith vertically only
- D. Serverless compute for intermittent work
- E. Define a recovery objective and test the recovery path

### 16. A studio runs its own database engine on Amazon EC2 and must track which engine patches apply to its configuration, even though AWS patches the host. Which concept does that describe?

- A. Some controls are shared, such as patch awareness
- B. AWS is responsible for encrypting customer data by default
- C. AWS is responsible for the physical facilities and hardware
- D. The customer is responsible for the data-centre building

---

## Domain 2 — Security and Compliance (30%) — Identity, Network Protection, Detection, and Compliance

### 17. Every live-ops engineer needs the same permissions, and that permission set changes when the game updates. What should be created?

- A. Put the users in a group and attach the policy to the group
- B. Create an IAM role and let the workload assume it
- C. Rotate access keys on a schedule
- D. Use the root user for daily administration

### 18. One action, deleting the production player table, must be refused even for administrators. How is that expressed?

- A. Give every engineer administrator access for convenience
- B. Require multi-factor authentication
- C. Attach a JSON policy that allows only the required actions
- D. Share the root credentials with the operations team

### 19. Three founders share one root login so any of them can change billing details. Which practice is this?

- A. Require multi-factor authentication
- B. Enable MFA and delete the root access keys
- C. Share the root credentials with the operations team
- D. Create an IAM user with long-lived credentials

### 20. Privileged engineers must prove possession of a hardware token before any administrative action. What should be enforced?

- A. Enable MFA and delete the root access keys
- B. Require multi-factor authentication
- C. Grant only the permissions the task needs
- D. Rotate access keys on a schedule

### 21. Studio staff already sign in to a corporate identity provider and should use it for AWS as well. What should be configured?

- A. Federate the company directory into AWS
- B. Use Amazon Cognito for customer sign-in
- C. Create an IAM user with long-lived credentials
- D. Put the users in a group and attach the policy to the group

### 22. Players must be able to create accounts and stay signed in across devices, with the studio issuing and refreshing the tokens itself. Which service fits?

- A. Use IAM Identity Center for workforce sign-in
- B. Use the root user for daily administration
- C. Use Amazon Cognito for customer sign-in
- D. Create an IAM user with long-lived credentials

### 23. Game servers must accept traffic only from the load balancer and nothing from the internet directly. What should be applied?

- A. Use AWS Network Firewall for VPC-level inspection
- B. Use a security group as a stateful instance firewall
- C. Open every port to the internet and rely on the application
- D. Use a network ACL as a stateless subnet filter

### 24. Launch night brings a volumetric flood, and bot sign-ups are hammering the account form with scripted requests. Which two services fit? Select two.

- A. Use AWS Shield for DDoS protection
- B. Use AWS WAF to block web attack patterns
- C. Use a network ACL as a stateless subnet filter
- D. Use AWS Network Firewall for VPC-level inspection
- E. Use a security group as a stateful instance firewall

### 25. Payment tokens must be encrypted with keys whose use is logged and that can be disabled centrally. Which service fits?

- A. Use AWS KMS to create and control encryption keys
- B. Encrypt data in transit with TLS
- C. Rely on server-side encryption with Amazon S3 managed keys
- D. Use Amazon Macie to find sensitive data in Amazon S3

### 26. Grid telemetry must be encrypted with keys the utility controls and can revoke without asking AWS. What should be used?

- A. Use AWS Certificate Manager for TLS certificates
- B. Use a customer managed key for the required control
- C. Rely on server-side encryption with Amazon S3 managed keys
- D. Encrypt data in transit with TLS

### 27. Certificates for the game studio's domains must renew without anyone remembering the expiry date. Which service fits?

- A. Use AWS KMS to create and control encryption keys
- B. Use AWS Certificate Manager for TLS certificates
- C. Attach a JSON policy that allows only the required actions
- D. Store the database credential in AWS Secrets Manager and rotate it

### 28. Build servers are suddenly consuming capacity around the clock, and the team suspects they are being used to mine cryptocurrency. Which service raises that finding?

- A. Use Amazon Inspector to scan workloads for vulnerabilities
- B. Use Amazon Macie to find sensitive data in Amazon S3
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use AWS CloudTrail to record API activity

### 29. Machine images must be checked for known vulnerabilities, and telemetry buckets must be searched for personal data that should not be there. Which two services fit? Select two.

- A. Use AWS Security Hub to aggregate findings in one place
- B. Use Amazon Inspector to scan workloads for vulnerabilities
- C. Use AWS CloudTrail to record API activity
- D. Use Amazon GuardDuty to detect suspicious activity
- E. Use Amazon Macie to find sensitive data in Amazon S3

### 30. Player save data must be restorable to a defined point after corruption across several services. Which service fits?

- A. An Amazon S3 bucket policy that grants public read
- B. Set a retention period and delete expired copies
- C. AWS Backup
- D. Set an S3 lifecycle rule to expire old objects

### 31. Replay files must disappear automatically thirty days after they are written, with no manual cleanup. What should be configured?

- A. AWS Backup
- B. Classify the data and tag each store by sensitivity
- C. Set an S3 lifecycle rule to expire old objects
- D. An Amazon S3 bucket policy that grants public read

### 32. After a production bucket vanished, the team needs the request that removed it, the caller behind it and the address it came from. Which service holds that evidence?

- A. Use Amazon Macie to find sensitive data in Amazon S3
- B. Use AWS Config to record resource configuration changes
- C. Use Amazon GuardDuty to detect suspicious activity
- D. Use AWS CloudTrail to record API activity

### 33. An auditor wants a history of how each resource was configured over time and a quick list of insecure account settings. Which two services fit? Select two.

- A. Use Amazon GuardDuty to detect suspicious activity
- B. Use AWS CloudTrail to record API activity
- C. Use AWS Config to record resource configuration changes
- D. Read the security checks in AWS Trusted Advisor
- E. Use Amazon Inspector to scan workloads for vulnerabilities

### 34. A studio asks whether AWS or the studio itself decides which of its engineers may query the production player database. Who decides?

- A. AWS is responsible for the physical facilities and hardware
- B. AWS is responsible for patching a managed service such as Amazon S3
- C. The customer is responsible for the data-centre building
- D. The customer is responsible for configuring IAM permissions

### 35. Game teams should be able to launch only server images that the platform team has approved, without asking for approval each time. Which service fits?

- A. AWS Control Tower
- B. Apply a service control policy in AWS Organizations
- C. AWS Service Catalog
- D. Attach a JSON policy that allows only the required actions

---

## Domain 3 — Cloud Technology and Services (34%) — Compute, Storage, Databases, Networking, and Managed Services

### 36. The game backend is a set of container images and the studio wants managed orchestration without running the hosts. Which compute option fits?

- A. AWS Lambda
- B. Amazon Lightsail
- C. Amazon ECS or Amazon EKS with AWS Fargate
- D. Amazon EC2 instances

### 37. Every in-game purchase must trigger a receipt write and a fraud check within a second, with no server kept running between events. Which service fits?

- A. AWS Lambda
- B. Amazon ECS or Amazon EKS with AWS Fargate
- C. AWS Batch
- D. Amazon EC2 instances

### 38. A render farm needs one shared file system that dozens of Linux nodes mount at the same time. Which storage fits?

- A. Amazon S3 Standard
- B. Amazon EFS file system
- C. Amazon EBS volumes
- D. Amazon FSx file systems

### 39. Build servers need block volumes that persist with the instance, and the replay archive is read unpredictably so nobody wants to tier it by hand. Which two services fit? Select two.

- A. Amazon S3 Glacier storage classes
- B. AWS Snowball devices
- C. Amazon S3 Intelligent-Tiering
- D. Amazon EFS file system
- E. Amazon EBS volumes

### 40. Player inventory and session state must serve millions of reads a second with predictable single-digit millisecond latency. Which database fits?

- A. Amazon Redshift
- B. Amazon DynamoDB
- C. Amazon ElastiCache
- D. Amazon RDS

### 41. The leaderboard is recomputed from a relational database for every read and the database is now the bottleneck. Which service should sit in front of it?

- A. Amazon Redshift
- B. Amazon Neptune
- C. Amazon ElastiCache
- D. Amazon DocumentDB

### 42. Real-time game traffic must reach the closest healthy endpoint over the AWS global network using anycast addresses. Which service fits?

- A. Amazon CloudFront
- B. Amazon Route 53
- C. Elastic Load Balancing
- D. AWS Global Accelerator

### 43. Game assets must be cached close to players around the world, and the studio's public domain must be served by managed DNS. Which two services fit? Select two.

- A. Amazon API Gateway
- B. Amazon VPC
- C. Amazon CloudFront
- D. Amazon Route 53
- E. Elastic Load Balancing

### 44. A fleet of game servers must receive operating system patches on a schedule and report which ones are compliant. Which service fits?

- A. Amazon CloudWatch
- B. AWS CloudFormation
- C. AWS Systems Manager
- D. AWS Service Catalog

### 45. The studio wants to know when an AWS service event is affecting the Region its game runs in. Which service fits?

- A. AWS Trusted Advisor
- B. Amazon CloudWatch
- C. Use AWS CloudTrail to record API activity
- D. AWS Health Dashboard

### 46. Every player action emits a telemetry record that must be ingested as a continuous ordered stream. Which service fits?

- A. Amazon Kinesis
- B. Amazon SNS
- C. Amazon SQS
- D. AWS Step Functions

### 47. Matchmaking jobs must be buffered so a slow allocator does not drop them, and one alert must reach the on-call engineer and the studio chat at once. Which two services fit? Select two.

- A. Amazon SNS
- B. Amazon EventBridge
- C. Amazon SQS
- D. Amazon Kinesis
- E. Amazon MQ

### 48. A studio wants non-player characters to hold conversations using a foundation model, with no model hosts to run. Which service fits?

- A. Amazon EMR
- B. Amazon SageMaker
- C. Amazon QuickSight
- D. Amazon Bedrock

### 49. A team must train, tune and deploy its own model that predicts which players will leave. Which service fits?

- A. Amazon Bedrock
- B. Amazon Athena
- C. AWS Glue
- D. Amazon SageMaker

### 50. Every nightly release must pass defined stages with a human approval before it reaches production. Which service coordinates that flow?

- A. AWS CodeDeploy
- B. AWS X-Ray
- C. AWS CodePipeline
- D. AWS CodeBuild

### 51. Matchmaking is slow and the team cannot tell which of five services is responsible for the delay. Which service traces the request?

- A. AWS X-Ray
- B. Use AWS Config to record resource configuration changes
- C. Use AWS CloudTrail to record API activity
- D. Amazon CloudWatch

### 52. A game environment must be declared in a stored template so a rebuild produces exactly the same resources. Which service fits?

- A. AWS Service Catalog
- B. AWS Elastic Beanstalk
- C. AWS Control Tower
- D. AWS CloudFormation

### 53. An indie studio wants compute, storage and networking in one bundle at a predictable monthly price with minimal configuration. Which service fits?

- A. Amazon Lightsail
- B. AWS App Runner
- C. Amazon EC2 instances
- D. AWS Elastic Beanstalk

### 54. The on-call engineer wants to be paged automatically when matchmaking jobs wait longer than five minutes. Which service holds the measurement and triggers the page?

- A. Use AWS Config to record resource configuration changes
- B. Amazon CloudWatch
- C. AWS X-Ray
- D. Use AWS CloudTrail to record API activity

### 55. A slow match must be attributed to a specific service call, and the configuration of that service at the time must be recoverable afterwards. Which two services fit? Select two.

- A. Use AWS Config to record resource configuration changes
- B. Amazon CloudWatch
- C. Use AWS CloudTrail to record API activity
- D. AWS X-Ray
- E. Use Amazon Inspector to scan workloads for vulnerabilities

### 56. A studio office needs a private dedicated link to move large build artefacts into AWS with consistent latency. Which service fits?

- A. Amazon CloudFront
- B. AWS PrivateLink
- C. AWS Site-to-Site VPN
- D. AWS Direct Connect

### 57. Game VPCs in three Regions and the studio's own network must be connected through one central router. Which service fits?

- A. Amazon VPC
- B. AWS Direct Connect
- C. AWS Transit Gateway
- D. AWS PrivateLink

---

## Domain 4 — Billing, Pricing, and Support (12%) — Pricing Models, Cost Control, and Support Plans

### 58. A playtest fleet can lose a machine at any moment and still finish the test, and cost per hour is the constraint. Which option fits?

- A. On-Demand Instances
- B. Reserved Instances
- C. Spot Instances
- D. Dedicated Hosts

### 59. A studio wants a discount for committing to an hourly spend, covering both its compute fleet and its serverless functions. Which option fits?

- A. Savings Plans
- B. Reserved Instances
- C. Spot Instances
- D. On-Demand Instances

### 60. A studio wants an alert when monthly spend crosses the amount the publisher approved. Which tool fits?

- A. AWS Cost Explorer
- B. AWS Budgets
- C. AWS Pricing Calculator
- D. AWS Cost and Usage Report

### 61. Spend that departs from its normal pattern must raise a warning automatically, and the next game launch must be costed before it is built. Which two tools fit? Select two.

- A. AWS Pricing Calculator
- B. AWS Budgets
- C. Cost Anomaly Detection
- D. AWS Cost Explorer
- E. Wait for the monthly invoice and reconcile it afterwards

### 62. A studio has one account per game and wants a single invoice while each game keeps its own account. What should be enabled?

- A. Tag resources and activate cost allocation tags
- B. Consolidated billing in AWS Organizations
- C. Keep a separate bill and separate discounts per account
- D. AWS Cost and Usage Report

### 63. A studio runs a live game in production and needs 24/7 technical support with faster response than a development-only plan. Which plan is the minimum that fits?

- A. AWS Developer Support
- B. AWS Business Support
- C. AWS Enterprise Support
- D. AWS Basic Support

### 64. A studio wants a vetted reference architecture for a common multiplayer backend instead of starting from nothing. What should it use?

- A. Engage an AWS Partner for the delivery work
- B. Search AWS re:Post for an answered question
- C. Read the AWS documentation and service user guides
- D. Start from an AWS Solutions Library reference deployment

### 65. A studio wants to evaluate a few services within published monthly allowances before the game earns any revenue. What provides that?

- A. The AWS Free Tier allowances
- B. Reserved Instances
- C. Savings Plans
- D. Volume discounts that grow with usage

---

## Answer key and explanations

### Question 1 — D

Answer: Elasticity: scale capacity with demand. Capacity is added for the launch and released afterwards, so the studio pays for the peak only while it lasts. Capacity is added and removed as demand changes, so the company pays only for what it uses. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Up-front data-centre investment is replaced by usage-based spending. Why the correct answer wins: Capacity is added for the launch and released afterwards, so the studio pays for the peak only while it lasts.
- **B:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Capacity is added for the launch and released afterwards, so the studio pays for the peak only while it lasts.
- **C:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Capacity is added for the launch and released afterwards, so the studio pays for the peak only while it lasts.
- **D:** Correct. Capacity is added and removed as demand changes, so the company pays only for what it uses. In this case: Capacity is added for the launch and released afterwards, so the studio pays for the peak only while it lasts.

### Question 2 — D

Answer: Agility: provision resources in minutes. Resources are provisioned in minutes, so an experiment no longer waits on hardware. New environments are created in minutes, which shortens the time to test an idea. Local study-map skill 1.1 (Cloud Value Proposition), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The company remains responsible for the building, power and hardware lifecycle. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on hardware.
- **B:** Incorrect for this question. Managed services remove single points of failure that a company would otherwise have to engineer. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on hardware.
- **C:** Incorrect for this question. The company pays for hardware before it is used and carries the depreciation and refresh risk. Why the correct answer wins: Resources are provisioned in minutes, so an experiment no longer waits on hardware.
- **D:** Correct. New environments are created in minutes, which shortens the time to test an idea. In this case: Resources are provisioned in minutes, so an experiment no longer waits on hardware.

### Question 3 — A

Answer: Estimate total cost of ownership including facilities and staff. A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the racks. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the racks.
- **B:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the racks.
- **C:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the racks.
- **D:** Incorrect for this question. There is no up-front commitment and the meter runs only while the resource exists. Why the correct answer wins: A like-for-like comparison carries power, space, cooling, hardware refresh and the staff who run the racks.

### Question 4 — B

Answer: Pay-as-you-go pricing. Usage-based billing carries no up-front commitment and no minimum monthly charge. There is no up-front commitment and the meter runs only while the resource exists. Local study-map skill 1.2 (Cloud Economics and Total Cost of Ownership), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A flat fee removes the usage signal from the bill but does not track demand. Why the correct answer wins: Usage-based billing carries no up-front commitment and no minimum monthly charge.
- **B:** Correct. There is no up-front commitment and the meter runs only while the resource exists. In this case: Usage-based billing carries no up-front commitment and no minimum monthly charge.
- **C:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: Usage-based billing carries no up-front commitment and no minimum monthly charge.
- **D:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Usage-based billing carries no up-front commitment and no minimum monthly charge.

### Question 5 — A

Answer: Loose coupling with a queue between tiers. A buffer between the two services lets matchmaking continue while the leaderboard catches up. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A queue decouples the producer from the consumer so a slow tier does not fail the whole flow. In this case: A buffer between the two services lets matchmaking continue while the leaderboard catches up.
- **B:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: A buffer between the two services lets matchmaking continue while the leaderboard catches up.
- **C:** Incorrect for this question. Two or more Zones give the workload a survivor when one Zone fails. Why the correct answer wins: A buffer between the two services lets matchmaking continue while the leaderboard catches up.
- **D:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: A buffer between the two services lets matchmaking continue while the leaderboard catches up.

### Question 6 — A

Answer: Break the application into small independent services. Independent services can be deployed and tested on their own schedule. Independent services can be deployed and scaled separately. Local study-map skill 1.3 (Cloud Architecture Design Principles), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Independent services can be deployed and scaled separately. In this case: Independent services can be deployed and tested on their own schedule.
- **B:** Incorrect for this question. Environments are created from a script or template, so they are consistent and disposable. Why the correct answer wins: Independent services can be deployed and tested on their own schedule.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Independent services can be deployed and tested on their own schedule.
- **D:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Independent services can be deployed and tested on their own schedule.

### Question 7 — B

Answer: Sustainability pillar. The sustainability pillar covers minimising the environmental impact of running a workload. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: The sustainability pillar covers minimising the environmental impact of running a workload.
- **B:** Correct. In this case: The sustainability pillar covers minimising the environmental impact of running a workload.
- **C:** Incorrect for this question. The pillar about running and improving workloads, including automation and small reversible changes. Why the correct answer wins: The sustainability pillar covers minimising the environmental impact of running a workload.
- **D:** Incorrect for this question. The pillar about delivering value at the lowest price that meets the requirement. Why the correct answer wins: The sustainability pillar covers minimising the environmental impact of running a workload.

### Question 8 — A, E

Answers: Operational excellence pillar; Performance efficiency pillar. Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice. The pillar about running and improving workloads, including automation and small reversible changes. The pillar about using resources efficiently as demand and technology change. Local study-map skill 1.4 (Well-Architected Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. The pillar about using resources efficiently as demand and technology change. In this case: Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice.
- **B:** Incorrect for this question. The pillar about recovering from failure and meeting demand consistently. Why the correct answer wins: Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice.
- **C:** Incorrect for this question. The pillar about protecting data, systems and assets through identity and detective controls. Why the correct answer wins: Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice.
- **D:** Incorrect for this question. The pillar about minimising the environmental impact of running a workload. Why the correct answer wins: Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice.
- **E:** Correct. The pillar about running and improving workloads, including automation and small reversible changes. In this case: Operational excellence covers repeatable automated change, and performance efficiency covers measured resource choice.

### Question 9 — A

Answer: Platform perspective of the AWS Cloud Adoption Framework. The platform perspective covers the technical architecture and the platform workloads run on. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. In this case: The platform perspective covers the technical architecture and the platform workloads run on.
- **B:** Incorrect for this question. The perspective about skills, roles and organisational change. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.
- **C:** Incorrect for this question. The perspective about prioritising, budgeting and measuring the cloud programme. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.
- **D:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The platform perspective covers the technical architecture and the platform workloads run on.

### Question 10 — D

Answer: Operations perspective of the AWS Cloud Adoption Framework. The operations perspective covers running, monitoring and supporting workloads day to day. Local study-map skill 1.5 (Cloud Adoption Framework), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The perspective about prioritising, budgeting and measuring the cloud programme. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.
- **B:** Incorrect for this question. The perspective about the technical architecture and the platform that workloads run on. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.
- **C:** Incorrect for this question. The perspective that connects cloud work to business outcomes and value. Why the correct answer wins: The operations perspective covers running, monitoring and supporting workloads day to day.
- **D:** Correct. In this case: The operations perspective covers running, monitoring and supporting workloads day to day.

### Question 11 — B

Answer: Replatform: change a few managed components on the way. Replatforming swaps in managed components while leaving the application largely intact. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Replatforming swaps in managed components while leaving the application largely intact.
- **B:** Correct. Small changes, such as moving a database to a managed engine, capture benefit with limited rework. In this case: Replatforming swaps in managed components while leaving the application largely intact.
- **C:** Incorrect for this question. The application is rewritten to take advantage of managed and elastic services. Why the correct answer wins: Replatforming swaps in managed components while leaving the application largely intact.
- **D:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Replatforming swaps in managed components while leaving the application largely intact.

### Question 12 — C

Answer: Repurchase: move to a different product. Repurchase moves to a different product instead of hosting the existing application. The company replaces the application with a commercially available equivalent. Local study-map skill 1.6 (Migration Strategies), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The workload stays in place because moving it is not justified yet. Why the correct answer wins: Repurchase moves to a different product instead of hosting the existing application.
- **B:** Incorrect for this question. The whole platform moves to a hosted equivalent without changing the application itself. Why the correct answer wins: Repurchase moves to a different product instead of hosting the existing application.
- **C:** Correct. The company replaces the application with a commercially available equivalent. In this case: Repurchase moves to a different product instead of hosting the existing application.
- **D:** Incorrect for this question. The application moves without code change, which is the fastest path but captures few cloud benefits. Why the correct answer wins: Repurchase moves to a different product instead of hosting the existing application.

### Question 13 — B

Answer: AWS Outposts for on-premises capacity. Outposts installs AWS infrastructure in the customer facility and operates it through AWS. Local study-map skill 1.7 (Global Infrastructure), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Points of presence that cache content close to users rather than in a Region. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **B:** Correct. In this case: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **C:** Incorrect for this question. An extension of a Region placed close to a large population or industry centre. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.
- **D:** Incorrect for this question. Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices. Why the correct answer wins: Outposts installs AWS infrastructure in the customer facility and operates it through AWS.

### Question 14 — D

Answer: Scale out automatically as demand rises. Scaling capacity automatically with measured demand removes the manual step entirely. Capacity follows the measured demand rather than a forecast. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Scaling capacity automatically with measured demand removes the manual step entirely.
- **B:** Incorrect for this question. A synchronous chain means one slow or failed component fails everything behind it. Why the correct answer wins: Scaling capacity automatically with measured demand removes the manual step entirely.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Scaling capacity automatically with measured demand removes the manual step entirely.
- **D:** Correct. Capacity follows the measured demand rather than a forecast. In this case: Scaling capacity automatically with measured demand removes the manual step entirely.

### Question 15 — A, E

Answers: Deploy across multiple Availability Zones; Define a recovery objective and test the recovery path. Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan. Two or more Zones give the workload a survivor when one Zone fails. A recovery time and recovery point objective turn disaster recovery from an intention into a design. Local study-map skill 1.8 (Resiliency and Availability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Two or more Zones give the workload a survivor when one Zone fails. In this case: Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan.
- **B:** Incorrect for this question. One Zone is a single failure domain, so a Zone event takes the workload with it. Why the correct answer wins: Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan.
- **C:** Incorrect for this question. Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply. Why the correct answer wins: Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan.
- **D:** Incorrect for this question. No server is provisioned, and the service runs only when it is invoked. Why the correct answer wins: Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan.
- **E:** Correct. A recovery time and recovery point objective turn disaster recovery from an intention into a design. In this case: Multiple Availability Zones survive a building loss, and recovery objectives define the regional plan.

### Question 16 — A

Answer: Some controls are shared, such as patch awareness. Patch awareness is shared, because both parties act on the same patch. AWS patches the infrastructure while the customer patches what it runs on top of it. Local study-map skill 1.9 (Shared Responsibility Model), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 1 (cloud concepts, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. AWS patches the infrastructure while the customer patches what it runs on top of it. In this case: Patch awareness is shared, because both parties act on the same patch.
- **B:** Incorrect for this question. Data protection choices such as encryption and key custody belong to the customer. Why the correct answer wins: Patch awareness is shared, because both parties act on the same patch.
- **C:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Patch awareness is shared, because both parties act on the same patch.
- **D:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Patch awareness is shared, because both parties act on the same patch.

### Question 17 — A

Answer: Put the users in a group and attach the policy to the group. A group holds the shared policy once, so one change applies to the whole team. A group is a collection of users that share permissions, which keeps the policy in one place. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A group is a collection of users that share permissions, which keeps the policy in one place. In this case: A group holds the shared policy once, so one change applies to the whole team.
- **B:** Incorrect for this question. A role hands out temporary credentials, so nothing long-lived is stored. Why the correct answer wins: A group holds the shared policy once, so one change applies to the whole team.
- **C:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: A group holds the shared policy once, so one change applies to the whole team.
- **D:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: A group holds the shared policy once, so one change applies to the whole team.

### Question 18 — C

Answer: Attach a JSON policy that allows only the required actions. A policy document can state an explicit deny, which overrides any allow. A policy document states which actions are allowed on which resources. Local study-map skill 2.1 (Identity and Access Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Broad standing access means one mistaken action or stolen credential can change anything. Why the correct answer wins: A policy document can state an explicit deny, which overrides any allow.
- **B:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: A policy document can state an explicit deny, which overrides any allow.
- **C:** Correct. A policy document states which actions are allowed on which resources. In this case: A policy document can state an explicit deny, which overrides any allow.
- **D:** Incorrect for this question. Sharing root credentials removes accountability and cannot be limited by policy. Why the correct answer wins: A policy document can state an explicit deny, which overrides any allow.

### Question 19 — C

Answer: Share the root credentials with the operations team. Sharing the root login removes accountability and cannot be limited by policy. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A second factor makes a stolen password insufficient on its own. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.
- **B:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.
- **C:** Correct. In this case: Sharing the root login removes accountability and cannot be limited by policy.
- **D:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Sharing the root login removes accountability and cannot be limited by policy.

### Question 20 — B

Answer: Require multi-factor authentication. Multi-factor authentication requires the second proof before the session is allowed. A second factor makes a stolen password insufficient on its own. Local study-map skill 2.2 (Root User and Credential Hygiene), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. The root user is the most privileged identity, so it is protected and its keys are removed. Why the correct answer wins: Multi-factor authentication requires the second proof before the session is allowed.
- **B:** Correct. A second factor makes a stolen password insufficient on its own. In this case: Multi-factor authentication requires the second proof before the session is allowed.
- **C:** Incorrect for this question. Starting from the minimum and adding as needed keeps the blast radius small. Why the correct answer wins: Multi-factor authentication requires the second proof before the session is allowed.
- **D:** Incorrect for this question. A rotation schedule limits how long a leaked key stays useful. Why the correct answer wins: Multi-factor authentication requires the second proof before the session is allowed.

### Question 21 — A

Answer: Federate the company directory into AWS. Federating the identity provider uses the existing corporate identity instead of new AWS credentials. Existing corporate identities are used instead of a separate set of AWS credentials. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Existing corporate identities are used instead of a separate set of AWS credentials. In this case: Federating the identity provider uses the existing corporate identity instead of new AWS credentials.
- **B:** Incorrect for this question. Cognito handles sign-up, sign-in and tokens for an application end users. Why the correct answer wins: Federating the identity provider uses the existing corporate identity instead of new AWS credentials.
- **C:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Federating the identity provider uses the existing corporate identity instead of new AWS credentials.
- **D:** Incorrect for this question. A group is a collection of users that share permissions, which keeps the policy in one place. Why the correct answer wins: Federating the identity provider uses the existing corporate identity instead of new AWS credentials.

### Question 22 — C

Answer: Use Amazon Cognito for customer sign-in. Cognito manages customer sign-up, sign-in and tokens for an application. Local study-map skill 2.3 (IAM Roles and Federation), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Workforce users sign in once and receive permission sets for the accounts they use. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.
- **B:** Incorrect for this question. The root user cannot be restricted by policy, so daily use magnifies any mistake. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.
- **C:** Correct. In this case: Cognito manages customer sign-up, sign-in and tokens for an application.
- **D:** Incorrect for this question. A user is an identity for a person or application with its own credentials. Why the correct answer wins: Cognito manages customer sign-up, sign-in and tokens for an application.

### Question 23 — B

Answer: Use a security group as a stateful instance firewall. A security group allows only the balancer and drops the rest at the instance. The group allows inbound or outbound traffic and remembers the connection state. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: A security group allows only the balancer and drops the rest at the instance.
- **B:** Correct. The group allows inbound or outbound traffic and remembers the connection state. In this case: A security group allows only the balancer and drops the rest at the instance.
- **C:** Incorrect for this question. An open perimeter exposes every service on the host, including ones nobody meant to publish. Why the correct answer wins: A security group allows only the balancer and drops the rest at the instance.
- **D:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: A security group allows only the balancer and drops the rest at the instance.

### Question 24 — A, B

Answers: Use AWS Shield for DDoS protection; Use AWS WAF to block web attack patterns. Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests. Shield absorbs distributed denial-of-service traffic before it reaches the application. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. Local study-map skill 2.4 (Network Security Controls), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Shield absorbs distributed denial-of-service traffic before it reaches the application. In this case: Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests.
- **B:** Correct. WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks. In this case: Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests.
- **C:** Incorrect for this question. The ACL filters traffic at the subnet boundary and evaluates each direction independently. Why the correct answer wins: Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests.
- **D:** Incorrect for this question. A managed firewall inspects traffic entering and leaving the VPC. Why the correct answer wins: Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests.
- **E:** Incorrect for this question. The group allows inbound or outbound traffic and remembers the connection state. Why the correct answer wins: Shield absorbs the flood before it reaches the application, and WAF rejects the scripted requests.

### Question 25 — A

Answer: Use AWS KMS to create and control encryption keys. KMS stores the keys, logs their use and can disable a key to revoke access. A managed key service creates, stores and audits the keys used to encrypt data. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A managed key service creates, stores and audits the keys used to encrypt data. In this case: KMS stores the keys, logs their use and can disable a key to revoke access.
- **B:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: KMS stores the keys, logs their use and can disable a key to revoke access.
- **C:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: KMS stores the keys, logs their use and can disable a key to revoke access.
- **D:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: KMS stores the keys, logs their use and can disable a key to revoke access.

### Question 26 — B

Answer: Use a customer managed key for the required control. A customer managed key puts the key policy and the revocation decision with the utility. The customer controls the key policy and can revoke access by disabling the key. Local study-map skill 2.5 (Encryption and Key Management), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Certificates are issued, renewed and deployed to integrated services without manual work. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision with the utility.
- **B:** Correct. The customer controls the key policy and can revoke access by disabling the key. In this case: A customer managed key puts the key policy and the revocation decision with the utility.
- **C:** Incorrect for this question. S3 encrypts the object at rest with keys it manages on the customer behalf. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision with the utility.
- **D:** Incorrect for this question. Traffic is protected while it crosses the network, not only while it sits on disk. Why the correct answer wins: A customer managed key puts the key policy and the revocation decision with the utility.

### Question 27 — B

Answer: Use AWS Certificate Manager for TLS certificates. Certificate Manager issues, renews and deploys the certificates automatically. Certificates are issued, renewed and deployed to integrated services without manual work. Local study-map skill 2.6 (Secrets and Certificate Handling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed key service creates, stores and audits the keys used to encrypt data. Why the correct answer wins: Certificate Manager issues, renews and deploys the certificates automatically.
- **B:** Correct. Certificates are issued, renewed and deployed to integrated services without manual work. In this case: Certificate Manager issues, renews and deploys the certificates automatically.
- **C:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: Certificate Manager issues, renews and deploys the certificates automatically.
- **D:** Incorrect for this question. The secret is held centrally and can be rotated on a schedule. Why the correct answer wins: Certificate Manager issues, renews and deploys the certificates automatically.

### Question 28 — C

Answer: Use Amazon GuardDuty to detect suspicious activity. GuardDuty analyses account, network and DNS activity for signs of compromise. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **B:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **C:** Correct. In this case: GuardDuty analyses account, network and DNS activity for signs of compromise.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: GuardDuty analyses account, network and DNS activity for signs of compromise.

### Question 29 — B, E

Answers: Use Amazon Inspector to scan workloads for vulnerabilities; Use Amazon Macie to find sensitive data in Amazon S3. Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Macie classifies objects and reports where personal or sensitive data is stored. Local study-map skill 2.7 (Threat Detection and Monitoring), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Security Hub collects findings from the security services and scores them against a standard. Why the correct answer wins: Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets.
- **B:** Correct. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. In this case: Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets.
- **D:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets.
- **E:** Correct. Macie classifies objects and reports where personal or sensitive data is stored. In this case: Inspector reports the vulnerabilities, and Macie locates the sensitive data in the buckets.

### Question 30 — C

Answer: AWS Backup. AWS Backup centralises and automates backups across supported services. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: AWS Backup centralises and automates backups across supported services.
- **B:** Incorrect for this question. A retention rule stops data from being kept forever by default. Why the correct answer wins: AWS Backup centralises and automates backups across supported services.
- **C:** Correct. In this case: AWS Backup centralises and automates backups across supported services.
- **D:** Incorrect for this question. A lifecycle rule moves or deletes objects automatically as they age. Why the correct answer wins: AWS Backup centralises and automates backups across supported services.

### Question 31 — C

Answer: Set an S3 lifecycle rule to expire old objects. A lifecycle rule deletes the objects automatically once they reach the stated age. Local study-map skill 2.8 (Data Protection and Classification), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed service that centralises and automates backups across supported services. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **B:** Incorrect for this question. A classification decides which controls and retention rules apply to each dataset. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **C:** Correct. In this case: A lifecycle rule deletes the objects automatically once they reach the stated age.
- **D:** Incorrect for this question. A public bucket policy exposes every object in the bucket to anyone on the internet. Why the correct answer wins: A lifecycle rule deletes the objects automatically once they reach the stated age.

### Question 32 — D

Answer: Use AWS CloudTrail to record API activity. CloudTrail records the API call, the caller and the source of the request. CloudTrail logs who called which API, when and from where. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Macie classifies objects and reports where personal or sensitive data is stored. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **B:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **C:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: CloudTrail records the API call, the caller and the source of the request.
- **D:** Correct. CloudTrail logs who called which API, when and from where. In this case: CloudTrail records the API call, the caller and the source of the request.

### Question 33 — C, D

Answers: Use AWS Config to record resource configuration changes; Read the security checks in AWS Trusted Advisor. Config keeps the configuration history, and Trusted Advisor reports insecure settings. Config keeps a history of configuration and evaluates it against rules. Trusted Advisor inspects the account and reports insecure or wasteful settings. Local study-map skill 2.9 (Compliance and Audit Evidence), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. GuardDuty analyses account, network and DNS activity for signs of compromise. Why the correct answer wins: Config keeps the configuration history, and Trusted Advisor reports insecure settings.
- **B:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: Config keeps the configuration history, and Trusted Advisor reports insecure settings.
- **C:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: Config keeps the configuration history, and Trusted Advisor reports insecure settings.
- **D:** Correct. Trusted Advisor inspects the account and reports insecure or wasteful settings. In this case: Config keeps the configuration history, and Trusted Advisor reports insecure settings.
- **E:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: Config keeps the configuration history, and Trusted Advisor reports insecure settings.

### Question 34 — D

Answer: The customer is responsible for configuring IAM permissions. Identity and access configuration stays with the customer in every service model. Local study-map skill 2.10 (Shared Responsibility Boundaries), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. AWS operates the buildings, power, network fabric and the hardware underneath the service. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.
- **B:** Incorrect for this question. The service itself is operated by AWS, including its underlying platform patches. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.
- **C:** Incorrect for this question. Physical facilities are AWS operated, not customer operated. Why the correct answer wins: Identity and access configuration stays with the customer in every service model.
- **D:** Correct. In this case: Identity and access configuration stays with the customer in every service model.

### Question 35 — C

Answer: AWS Service Catalog. Service Catalog publishes the approved images as products that teams can launch themselves. A curated catalogue of approved products that teams can launch themselves. Local study-map skill 2.11 (Governance Guardrails), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 2 (security and compliance, 30 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: Service Catalog publishes the approved images as products that teams can launch themselves.
- **B:** Incorrect for this question. An SCP sets the maximum permissions available to the accounts under it. Why the correct answer wins: Service Catalog publishes the approved images as products that teams can launch themselves.
- **C:** Correct. A curated catalogue of approved products that teams can launch themselves. In this case: Service Catalog publishes the approved images as products that teams can launch themselves.
- **D:** Incorrect for this question. A policy document states which actions are allowed on which resources. Why the correct answer wins: Service Catalog publishes the approved images as products that teams can launch themselves.

### Question 36 — C

Answer: Amazon ECS or Amazon EKS with AWS Fargate. Managed container orchestration runs the containers while the platform owns the hosts. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Run code on an event without provisioning or managing a server. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **B:** Incorrect for this question. A simplified bundle of compute, storage and networking for small projects at a predictable price. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.
- **C:** Correct. In this case: Managed container orchestration runs the containers while the platform owns the hosts.
- **D:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Managed container orchestration runs the containers while the platform owns the hosts.

### Question 37 — A

Answer: AWS Lambda. Lambda runs the handler per event and keeps nothing running in between. Run code on an event without provisioning or managing a server. Local study-map skill 3.1 (Compute Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Run code on an event without provisioning or managing a server. In this case: Lambda runs the handler per event and keeps nothing running in between.
- **B:** Incorrect for this question. Managed container orchestration where the platform runs the hosts. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.
- **C:** Incorrect for this question. Queue and run batch computing jobs without managing the scheduler infrastructure. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.
- **D:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lambda runs the handler per event and keeps nothing running in between.

### Question 38 — B

Answer: Amazon EFS file system. EFS is a shared file system that many Linux instances can mount at once. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Object storage for frequently accessed data with high durability and availability. Why the correct answer wins: EFS is a shared file system that many Linux instances can mount at once.
- **B:** Correct. In this case: EFS is a shared file system that many Linux instances can mount at once.
- **C:** Incorrect for this question. Block storage attached to a single instance, used for an operating system or database files. Why the correct answer wins: EFS is a shared file system that many Linux instances can mount at once.
- **D:** Incorrect for this question. Managed file systems for Windows or high-performance workloads. Why the correct answer wins: EFS is a shared file system that many Linux instances can mount at once.

### Question 39 — C, E

Answers: Amazon EBS volumes; Amazon S3 Intelligent-Tiering. EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes. Block storage attached to a single instance, used for an operating system or database files. Object storage that moves objects between access tiers as usage changes. Local study-map skill 3.2 (Storage Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Archive storage for data that is rarely read and tolerates retrieval time. Why the correct answer wins: EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes.
- **B:** Incorrect for this question. Physical devices that move large datasets into AWS when the network is the bottleneck. Why the correct answer wins: EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes.
- **C:** Correct. Object storage that moves objects between access tiers as usage changes. In this case: EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes.
- **D:** Incorrect for this question. A shared file system that many Linux instances can mount at the same time. Why the correct answer wins: EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes.
- **E:** Correct. Block storage attached to a single instance, used for an operating system or database files. In this case: EBS provides the persistent block volumes, and Intelligent-Tiering moves objects as access changes.

### Question 40 — B

Answer: Amazon DynamoDB. DynamoDB is a managed key-value store built for high-volume, predictable-latency access. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **B:** Correct. In this case: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **C:** Incorrect for this question. A managed in-memory cache for sub-millisecond reads of hot data. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.
- **D:** Incorrect for this question. A managed relational database where AWS handles patching, backups and failover options. Why the correct answer wins: DynamoDB is a managed key-value store built for high-volume, predictable-latency access.

### Question 41 — C

Answer: Amazon ElastiCache. An in-memory cache absorbs the repeated reads with sub-millisecond latency. A managed in-memory cache for sub-millisecond reads of hot data. Local study-map skill 3.3 (Database Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed data warehouse for analytical queries over large datasets. Why the correct answer wins: An in-memory cache absorbs the repeated reads with sub-millisecond latency.
- **B:** Incorrect for this question. A managed graph database for highly connected data. Why the correct answer wins: An in-memory cache absorbs the repeated reads with sub-millisecond latency.
- **C:** Correct. A managed in-memory cache for sub-millisecond reads of hot data. In this case: An in-memory cache absorbs the repeated reads with sub-millisecond latency.
- **D:** Incorrect for this question. A managed document database compatible with MongoDB workloads. Why the correct answer wins: An in-memory cache absorbs the repeated reads with sub-millisecond latency.

### Question 42 — D

Answer: AWS Global Accelerator. Global Accelerator routes players to the closest healthy endpoint using anycast addresses. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Global Accelerator routes players to the closest healthy endpoint using anycast addresses.
- **B:** Incorrect for this question. A managed DNS service that also supports health checks and routing policies. Why the correct answer wins: Global Accelerator routes players to the closest healthy endpoint using anycast addresses.
- **C:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: Global Accelerator routes players to the closest healthy endpoint using anycast addresses.
- **D:** Correct. Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint. In this case: Global Accelerator routes players to the closest healthy endpoint using anycast addresses.

### Question 43 — C, D

Answers: Amazon CloudFront; Amazon Route 53. CloudFront caches the assets at edge locations, and Route 53 serves the DNS records. A content delivery network that caches content at edge locations near users. A managed DNS service that also supports health checks and routing policies. Local study-map skill 3.4 (Networking and Content Delivery), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A managed front door for APIs with throttling, authorisation and usage plans. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **B:** Incorrect for this question. A logically isolated virtual network in which the customer places its resources. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **C:** Correct. A content delivery network that caches content at edge locations near users. In this case: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **D:** Correct. A managed DNS service that also supports health checks and routing policies. In this case: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.
- **E:** Incorrect for this question. Distributes incoming traffic across multiple targets in one or more Availability Zones. Why the correct answer wins: CloudFront caches the assets at edge locations, and Route 53 serves the DNS records.

### Question 44 — C

Answer: AWS Systems Manager. Systems Manager applies the patches and reports compliance across managed nodes. Operations tooling for patching, running commands and inventory across managed nodes. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.
- **B:** Incorrect for this question. Infrastructure defined as a template and created or updated as a stack. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.
- **C:** Correct. Operations tooling for patching, running commands and inventory across managed nodes. In this case: Systems Manager applies the patches and reports compliance across managed nodes.
- **D:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: Systems Manager applies the patches and reports compliance across managed nodes.

### Question 45 — D

Answer: AWS Health Dashboard. The Health Dashboard reports AWS service events and their effect on the account. Service health and event notifications that affect the account. Local study-map skill 3.5 (Management and Governance Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Checks an account against best practices for cost, security, limits and resilience. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **B:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: The Health Dashboard reports AWS service events and their effect on the account.
- **D:** Correct. Service health and event notifications that affect the account. In this case: The Health Dashboard reports AWS service events and their effect on the account.

### Question 46 — A

Answer: Amazon Kinesis. Kinesis ingests and processes continuous streaming records. Streaming data ingestion and processing for continuous records. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Streaming data ingestion and processing for continuous records. In this case: Kinesis ingests and processes continuous streaming records.
- **B:** Incorrect for this question. A pub/sub topic that fans a message out to many subscribers. Why the correct answer wins: Kinesis ingests and processes continuous streaming records.
- **C:** Incorrect for this question. A managed queue that decouples producers from consumers and buffers bursts. Why the correct answer wins: Kinesis ingests and processes continuous streaming records.
- **D:** Incorrect for this question. A state machine that coordinates multi-step workflows with retries and branching. Why the correct answer wins: Kinesis ingests and processes continuous streaming records.

### Question 47 — A, C

Answers: Amazon SQS; Amazon SNS. A queue buffers the jobs, and SNS fans the alert out to every subscriber. A managed queue that decouples producers from consumers and buffers bursts. A pub/sub topic that fans a message out to many subscribers. Local study-map skill 3.6 (Integration and Messaging), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A pub/sub topic that fans a message out to many subscribers. In this case: A queue buffers the jobs, and SNS fans the alert out to every subscriber.
- **B:** Incorrect for this question. An event bus that routes events from AWS services and applications to targets by rule. Why the correct answer wins: A queue buffers the jobs, and SNS fans the alert out to every subscriber.
- **C:** Correct. A managed queue that decouples producers from consumers and buffers bursts. In this case: A queue buffers the jobs, and SNS fans the alert out to every subscriber.
- **D:** Incorrect for this question. Streaming data ingestion and processing for continuous records. Why the correct answer wins: A queue buffers the jobs, and SNS fans the alert out to every subscriber.
- **E:** Incorrect for this question. A managed message broker for existing protocols such as AMQP or MQTT. Why the correct answer wins: A queue buffers the jobs, and SNS fans the alert out to every subscriber.

### Question 48 — D

Answer: Amazon Bedrock. Bedrock exposes foundation models through an API so the studio never operates the model hosts. Access foundation models through an API without operating the model infrastructure. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Managed clusters for big-data frameworks such as Spark and Hadoop. Why the correct answer wins: Bedrock exposes foundation models through an API so the studio never operates the model hosts.
- **B:** Incorrect for this question. Build, train and deploy machine learning models through a managed platform. Why the correct answer wins: Bedrock exposes foundation models through an API so the studio never operates the model hosts.
- **C:** Incorrect for this question. A managed business intelligence service for dashboards and reports. Why the correct answer wins: Bedrock exposes foundation models through an API so the studio never operates the model hosts.
- **D:** Correct. Access foundation models through an API without operating the model infrastructure. In this case: Bedrock exposes foundation models through an API so the studio never operates the model hosts.

### Question 49 — D

Answer: Amazon SageMaker. SageMaker covers the model lifecycle from training through deployment. Build, train and deploy machine learning models through a managed platform. Local study-map skill 3.7 (Analytics and Machine Learning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Access foundation models through an API without operating the model infrastructure. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **B:** Incorrect for this question. Query data in Amazon S3 with SQL and no infrastructure to manage. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **C:** Incorrect for this question. A managed data catalogue and extract-transform-load service. Why the correct answer wins: SageMaker covers the model lifecycle from training through deployment.
- **D:** Correct. Build, train and deploy machine learning models through a managed platform. In this case: SageMaker covers the model lifecycle from training through deployment.

### Question 50 — C

Answer: AWS CodePipeline. CodePipeline orchestrates the stages and the approval between them. Orchestrates the build, test and deploy stages of a release. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Automates the deployment of application revisions to instances and services. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.
- **B:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.
- **C:** Correct. Orchestrates the build, test and deploy stages of a release. In this case: CodePipeline orchestrates the stages and the approval between them.
- **D:** Incorrect for this question. Compiles code and runs tests in a managed build environment. Why the correct answer wins: CodePipeline orchestrates the stages and the approval between them.

### Question 51 — A

Answer: AWS X-Ray. X-Ray traces a request across the services and shows where the time is spent. Traces requests through a distributed application to find where time is spent. Local study-map skill 3.8 (Developer Tooling), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Traces requests through a distributed application to find where time is spent. In this case: X-Ray traces a request across the services and shows where the time is spent.
- **B:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.
- **D:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: X-Ray traces a request across the services and shows where the time is spent.

### Question 52 — D

Answer: AWS CloudFormation. CloudFormation creates and updates resources from a template, so every rebuild matches. Infrastructure defined as a template and created or updated as a stack. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A curated catalogue of approved products that teams can launch themselves. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every rebuild matches.
- **B:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every rebuild matches.
- **C:** Incorrect for this question. A landing zone that applies baseline controls across an organisation. Why the correct answer wins: CloudFormation creates and updates resources from a template, so every rebuild matches.
- **D:** Correct. Infrastructure defined as a template and created or updated as a stack. In this case: CloudFormation creates and updates resources from a template, so every rebuild matches.

### Question 53 — A

Answer: Amazon Lightsail. Lightsail bundles the basics for a small project at a flat, predictable price. A simplified bundle of compute, storage and networking for small projects at a predictable price. Local study-map skill 3.9 (Deployment and Provisioning), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A simplified bundle of compute, storage and networking for small projects at a predictable price. In this case: Lightsail bundles the basics for a small project at a flat, predictable price.
- **B:** Incorrect for this question. Run a containerised web service without choosing or managing the underlying capacity. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.
- **C:** Incorrect for this question. Virtual servers where the customer controls the operating system and the runtime. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.
- **D:** Incorrect for this question. Upload the application and let the platform provision and manage the environment. Why the correct answer wins: Lightsail bundles the basics for a small project at a flat, predictable price.

### Question 54 — B

Answer: Amazon CloudWatch. CloudWatch holds the metric and evaluates the alarm against it. Metrics, logs and alarms for the resources and applications in the account. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Config keeps a history of configuration and evaluates it against rules. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **B:** Correct. Metrics, logs and alarms for the resources and applications in the account. In this case: CloudWatch holds the metric and evaluates the alarm against it.
- **C:** Incorrect for this question. Traces requests through a distributed application to find where time is spent. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.
- **D:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: CloudWatch holds the metric and evaluates the alarm against it.

### Question 55 — A, D

Answers: AWS X-Ray; Use AWS Config to record resource configuration changes. X-Ray attributes the delay to a service call, and Config keeps the configuration history. Traces requests through a distributed application to find where time is spent. Config keeps a history of configuration and evaluates it against rules. Local study-map skill 3.10 (Monitoring and Observability), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Config keeps a history of configuration and evaluates it against rules. In this case: X-Ray attributes the delay to a service call, and Config keeps the configuration history.
- **B:** Incorrect for this question. Metrics, logs and alarms for the resources and applications in the account. Why the correct answer wins: X-Ray attributes the delay to a service call, and Config keeps the configuration history.
- **C:** Incorrect for this question. CloudTrail logs who called which API, when and from where. Why the correct answer wins: X-Ray attributes the delay to a service call, and Config keeps the configuration history.
- **D:** Correct. Traces requests through a distributed application to find where time is spent. In this case: X-Ray attributes the delay to a service call, and Config keeps the configuration history.
- **E:** Incorrect for this question. Inspector finds software vulnerabilities and unintended network exposure on the resources it scans. Why the correct answer wins: X-Ray attributes the delay to a service call, and Config keeps the configuration history.

### Question 56 — D

Answer: AWS Direct Connect. Direct Connect provides a dedicated private link from the customer facility into AWS. A dedicated private network connection from a customer facility into AWS. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A content delivery network that caches content at edge locations near users. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **B:** Incorrect for this question. Private connectivity to a service through an endpoint inside the VPC. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **C:** Incorrect for this question. An encrypted tunnel over the internet between a customer network and a VPC. Why the correct answer wins: Direct Connect provides a dedicated private link from the customer facility into AWS.
- **D:** Correct. A dedicated private network connection from a customer facility into AWS. In this case: Direct Connect provides a dedicated private link from the customer facility into AWS.

### Question 57 — C

Answer: AWS Transit Gateway. Transit Gateway acts as a central router for VPCs and on-premises networks. A central router that connects many VPCs and on-premises networks. Local study-map skill 3.11 (Hybrid and Edge Services), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 3 (cloud technology and services, 34 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. A logically isolated virtual network in which the customer places its resources. Why the correct answer wins: Transit Gateway acts as a central router for VPCs and on-premises networks.
- **B:** Incorrect for this question. A dedicated private network connection from a customer facility into AWS. Why the correct answer wins: Transit Gateway acts as a central router for VPCs and on-premises networks.
- **C:** Correct. A central router that connects many VPCs and on-premises networks. In this case: Transit Gateway acts as a central router for VPCs and on-premises networks.
- **D:** Incorrect for this question. Private connectivity to a service through an endpoint inside the VPC. Why the correct answer wins: Transit Gateway acts as a central router for VPCs and on-premises networks.

### Question 58 — C

Answer: Spot Instances. Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **B:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **C:** Correct. In this case: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.
- **D:** Incorrect for this question. A physical server dedicated to one customer, used for licensing or compliance requirements. Why the correct answer wins: Spot capacity is spare capacity sold at a steep discount and can be reclaimed with short notice.

### Question 59 — A

Answer: Savings Plans. Savings Plans commit to a spend per hour and apply across eligible compute usage. A commitment to a spend level per hour in exchange for a discount across eligible usage. Local study-map skill 4.1 (Pricing Models), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. A commitment to a spend level per hour in exchange for a discount across eligible usage. In this case: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **B:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **C:** Incorrect for this question. Spare capacity at a steep discount that can be reclaimed with short notice. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.
- **D:** Incorrect for this question. Capacity billed by the second or hour with no commitment. Why the correct answer wins: Savings Plans commit to a spend per hour and apply across eligible compute usage.

### Question 60 — B

Answer: AWS Budgets. Budgets tracks spend against a threshold and alerts when it is crossed. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **B:** Correct. In this case: Budgets tracks spend against a threshold and alerts when it is crossed.
- **C:** Incorrect for this question. Estimate the cost of a planned architecture before it is built. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.
- **D:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Budgets tracks spend against a threshold and alerts when it is crossed.

### Question 61 — A, C

Answers: Cost Anomaly Detection; AWS Pricing Calculator. Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch. Machine learning alerts on spending that deviates from the expected pattern. Estimate the cost of a planned architecture before it is built. Local study-map skill 4.2 (Cost Management Tools), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Estimate the cost of a planned architecture before it is built. In this case: Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch.
- **B:** Incorrect for this question. Set a spending or usage threshold and alert or act when it is crossed. Why the correct answer wins: Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch.
- **C:** Correct. Machine learning alerts on spending that deviates from the expected pattern. In this case: Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch.
- **D:** Incorrect for this question. Visualise and analyse past spend and forecast what is coming. Why the correct answer wins: Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch.
- **E:** Incorrect for this question. A retrospective invoice reveals overspend only after the money is gone. Why the correct answer wins: Cost Anomaly Detection warns about the deviation, and the Pricing Calculator costs the planned launch.

### Question 62 — B

Answer: Consolidated billing in AWS Organizations. Consolidated billing puts the accounts on one invoice and pools their usage for discounts. One bill for all accounts, with usage aggregated so volume discounts are shared. Local study-map skill 4.3 (Billing and Account Structures), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Activated tags split the one bill by department, project or cost centre. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **B:** Correct. One bill for all accounts, with usage aggregated so volume discounts are shared. In this case: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **C:** Incorrect for this question. Separate accounts do not pool usage, so each misses the discounts the total would earn. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.
- **D:** Incorrect for this question. The most granular billing dataset, delivered to a bucket for analysis. Why the correct answer wins: Consolidated billing puts the accounts on one invoice and pools their usage for discounts.

### Question 63 — B

Answer: AWS Business Support. Business Support adds 24/7 production support and faster response than Basic or Developer. Production support with 24/7 access, faster response and Trusted Advisor checks. Local study-map skill 4.4 (Support Plans), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Business-hours email support for development and test workloads. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **B:** Correct. Production support with 24/7 access, faster response and Trusted Advisor checks. In this case: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **C:** Incorrect for this question. Mission-critical support with a designated technical account manager and the fastest response. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.
- **D:** Incorrect for this question. Account and billing support with documentation and health checks, at no charge. Why the correct answer wins: Business Support adds 24/7 production support and faster response than Basic or Developer.

### Question 64 — D

Answer: Start from an AWS Solutions Library reference deployment. The Solutions Library publishes vetted reference architectures and deployments. A vetted reference architecture shortens design work for a common workload. Local study-map skill 4.5 (Guidance and Self-Service Resources), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Incorrect for this question. Partners are third-party firms with AWS-validated skills for implementation work. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.
- **B:** Incorrect for this question. The community knowledge base holds answers to common service and account questions. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.
- **C:** Incorrect for this question. The reference documentation states what a service does and how it is configured. Why the correct answer wins: The Solutions Library publishes vetted reference architectures and deployments.
- **D:** Correct. A vetted reference architecture shortens design work for a common workload. In this case: The Solutions Library publishes vetted reference architectures and deployments.

### Question 65 — A

Answer: The AWS Free Tier allowances. The Free Tier publishes monthly allowances for eligible services on a qualifying account. Limited monthly usage at no charge for eligible services on a new or qualifying account. Local study-map skill 4.6 (Free Tier and Discounts), mapped to the official guide: AWS Certified Cloud Practitioner (CLF-C02) exam guide. Primary reference: CLF-C02 exam guide, content domain 4 (billing, pricing, and support, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html.

- **A:** Correct. Limited monthly usage at no charge for eligible services on a new or qualifying account. In this case: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **B:** Incorrect for this question. A one- or three-year commitment in exchange for a lower hourly rate. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **C:** Incorrect for this question. A commitment to a spend level per hour in exchange for a discount across eligible usage. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
- **D:** Incorrect for this question. Aggregated usage across an organisation lowers the effective rate. Why the correct answer wins: The Free Tier publishes monthly allowances for eligible services on a qualifying account.
