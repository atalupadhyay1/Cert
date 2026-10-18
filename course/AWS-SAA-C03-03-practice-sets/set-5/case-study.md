# Set 5 Case Study — **GlobalBank's Hybrid Cloud Migration**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set reference this scenario directly. You can
> come back to this README as often as needed during the set.

## Background

**GlobalBank** is a large multinational bank that is migrating its
core banking workloads from an on-premises IBM mainframe to AWS over 3
years. The migration is being done in waves:

- **Wave 1 (now):** customer-facing web portal and mobile app.
- **Wave 2 (year 2):** account opening and loan origination.
- **Wave 3 (year 3):** core ledger and settlement systems.

The bank has strict regulatory requirements (FFIEC, PCI DSS, SOX, GDPR)
and a board-mandated RTO of 4 hours and RPO of 15 minutes for
customer-facing workloads.

## Key facts

- **Current on-premises:** IBM z14 mainframe in 2 data centers
  (Virginia and Texas), 200+ TB of data, 10,000+ MIPS capacity.
- **Connectivity:** redundant 10 Gbps Direct Connect circuits to each
  on-premises data center, with a VPN backup.
- **Workloads in scope for Wave 1:** web portal, mobile app API,
  authentication service, marketing email.
- **Workloads NOT in scope for Wave 1:** core banking, ATM network,
  fraud detection, regulatory reporting.
- **Compliance:** FFIEC (US banking), PCI DSS, SOX, GDPR (EU customers).
- **Identity:** on-premises Active Directory with 50,000 users; must be
  the source of truth for at least 2 more years.
- **Data classification:** customer PII (regulated), cardholder data
  (PCI), public data.

## Your task

Design the Wave 1 architecture and the hybrid connectivity that will
serve as the foundation for Waves 2 and 3. Pay particular attention to:

1. The hybrid network (Direct Connect + VPN backup + routing).
2. Identity federation (on-prem AD to AWS IAM/Identity Center).
3. Network segmentation (PCI workload isolation).
4. DR strategy that meets RTO 4 hr / RPO 15 min.

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the GlobalBank scenario..."** — these are the case-study questions.
The remaining questions in the set are standalone questions unrelated to
this scenario.
