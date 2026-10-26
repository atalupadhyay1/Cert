# Google Cloud Professional Cloud Network Engineer — Full-Length Mock Exam 2

Professional Cloud Network Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing and Planning a Google Cloud VPC Network (VPC Design, IP Planning, and Load Balancer Choice)

### 1. A trading desk in Singapore reads a service hosted in Frankfurt and every millisecond counts. Which tier should the front end use?

- A. Use the Premium network service tier
- B. Use the Standard network service tier
- C. Deploy a regional external Application Load Balancer
- D. Order a Partner Interconnect connection

### 2. A nightly reporting endpoint serves one city and the finance team caps egress spend. Which tier fits?

- A. Use the Standard network service tier
- B. Assign a manual static Cloud NAT address
- C. Use an external proxy Network Load Balancer with TLS termination
- D. Use the Premium network service tier

### 3. A failover exercise kept sending requests to a dead instance group until operators deleted it. What was missing?

- A. Enable connection draining with a timeout
- B. Switch the balancing mode to connections per instance
- C. Attach a health check to the backend service
- D. Enable session affinity on the backend service

### 4. A retailer needs one address that serves both regions and stops using a region that fails. Which two components give that? Select two.

- A. Deploy a regional external Application Load Balancer
- B. Use the Premium network service tier
- C. Deploy an internal passthrough Network Load Balancer
- D. Deploy a global external Application Load Balancer
- E. Attach a health check to the backend service

### 5. Applications in the VPC must resolve a name that only the branch-office resolvers know. What should be configured?

- A. Configure a DNS forwarding policy for the on-premises domain
- B. Create an inbound forwarding policy with a forwarding address
- C. Create a public Cloud DNS zone
- D. Create a DNS peering zone to the other project

### 6. The datacentre resolvers must query Cloud DNS for private zones in two projects. What gives them an address to query?

- A. Create an inbound forwarding policy with a forwarding address
- B. Configure a DNS forwarding policy for the on-premises domain
- C. Serve split-horizon answers from separate private and public zones
- D. Create a DNS peering zone to the other project

### 7. A gRPC service needs the front end to balance individual requests rather than whole connections. Which shape fits?

- A. Deploy an internal passthrough Network Load Balancer
- B. Route by URL path in the URL map
- C. Use a proxy Network Load Balancer
- D. Use a passthrough Network Load Balancer

### 8. A licensing server identifies clients by source address and must keep seeing that address. Which shape fits?

- A. Split traffic between two backend services by weight
- B. Route by URL path in the URL map
- C. Use a proxy Network Load Balancer
- D. Use a passthrough Network Load Balancer

### 9. A platform team must host clusters in subnets the central network team owns. What fits?

- A. Plan secondary ranges for pods and services
- B. Deploy the cluster into a shared subnet
- C. Enable GKE Dataplane V2
- D. Use private nodes with no external addresses

### 10. Clients move between networks and a fixed control-plane address keeps being blocked. What removes the fixed address?

- A. Configure an IP masquerade policy on the node pool
- B. Add the office range to the authorised networks
- C. Use the DNS-based control plane endpoint
- D. Use a private control plane endpoint

### 11. Planners need pod addresses counted separately from node addresses, and room to add more pods later. Which two choices give that? Select two.

- A. Add a second pod range to the cluster
- B. Configure an IP masquerade policy on the node pool
- C. Create a GKE network policy for the namespace
- D. Plan secondary ranges for pods and services
- E. Resize the service range allocation

### 12. The central network team must create and change networks in the host project. Which role fits?

- A. Grant the subnet user role on the specific shared subnets
- B. Grant the network administrator role in the host project
- C. Create a custom role with only the required network permissions
- D. Grant the basic editor role to the automation

### 13. An auditor wants the CI identity limited to reading subnets and using one shared subnet. Which two grants fit? Select two.

- A. Grant Shared VPC Admin on the host project
- B. Create a custom role with only the required network permissions
- C. Grant the network administrator role in the host project
- D. Grant the basic editor role to the automation
- E. Grant the subnet user role on the specific shared subnets

### 14. A Cloud Run service must appear as an address in the subnet and avoid a connector bottleneck. What fits?

- A. Attach the service to Serverless VPC Access
- B. Create a Private Service Connect endpoint
- C. Use Direct VPC egress for the serverless workload
- D. Allocate a private services access range

### 15. Two managed services must be reached privately: one published by a partner and one provisioned in the project. Which two mechanisms fit? Select two.

- A. Create a Private Service Connect endpoint
- B. Enable Private Google Access on the subnet
- C. Reach the API through its public interface
- D. Allocate a private services access range
- E. Attach the service to Serverless VPC Access

### 16. Two business units insist on separate networks but must exchange traffic directly. Which simplest mechanism fits?

- A. Connect the VPC networks through a Network Connectivity Center hub
- B. Create a VPC Network Peering connection between the two networks
- C. Peer every VPC network with every other VPC network
- D. Build the network as a Shared VPC with host and service projects

### 17. A four-network design uses peering everywhere and the fourth hop never works. What was misunderstood?

- A. Create a VPC Network Peering connection between the two networks
- B. Peer every VPC network with every other VPC network
- C. Assume peered networks can reach each other transitively
- D. Expect spoke-to-spoke reachability through the hub

### 18. Twenty teams request ranges by ticket and overlaps keep reaching production. What should be introduced?

- A. Bring your own public IP prefixes
- B. Accept the overlapping subnet ranges as configured
- C. Use privately used public IP address ranges
- D. Automate address allocation from a central IPAM plan

### 19. Public prefixes the company already owns must be advertised from Google Cloud. What fits?

- A. Bring your own public IP prefixes
- B. Deploy Private NAT for the overlapping ranges
- C. Use non-RFC 1918 space for the internal network
- D. Use privately used public IP address ranges

### 20. Backups between two zones inside one VPC run at a fraction of the link speed. What should be raised?

- A. Keep the default 1500-byte MTU
- B. Raise the VPC MTU to 8896 bytes
- C. Leave the MTU mismatch unfixed
- D. Lower the tunnel MTU to 1460 bytes

### 21. A vendor firewall must inspect traffic between two VPC networks and cannot be peered. What should be deployed?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Add a policy-based route that matches the source and destination
- C. Use the internal load balancer as the next hop
- D. Create a static route with a tag-scoped next hop

---

## Domain 2 — Implementing a VPC Network (VPC Implementation, Routing, and GKE Networking)

### 22. A cluster subnet needs a thousand more addresses without touching existing nodes. What should be done?

- A. Add a second pod range to the cluster
- B. Expand the existing subnet range
- C. Enable dual-stack IPv6 on the subnet
- D. Accept the overlapping subnet ranges as configured

### 23. A subnet is too small, and a second team has proposed a range that collides with it. Which two actions resolve that? Select two.

- A. Add a second pod range to the cluster
- B. Accept the overlapping subnet ranges as configured
- C. Expand the existing subnet range
- D. Bring your own public IP prefixes
- E. Use non-RFC 1918 space for the internal network

### 24. A partner's project must reach one subnet and nothing else in the network. What provides the connection?

- A. Assume peered networks can reach each other transitively
- B. Create a VPC Network Peering connection between the two networks
- C. Peer every VPC network with every other VPC network
- D. Connect the VPC networks through a Network Connectivity Center hub

### 25. A policy-based route created locally must be visible on the far side of a peering. What option enables that?

- A. Apply a CIDR range filter to the spoke
- B. Assume peered networks can reach each other transitively
- C. Create a VPC Network Peering connection between the two networks
- D. Import and export custom routes over the peering

### 26. A reorganisation needs six service projects attached to one host project. Which role performs it?

- A. Grant Shared VPC Admin on the host project
- B. Create a custom role with only the required network permissions
- C. Grant the network administrator role in the host project
- D. Grant the subnet user role on the specific shared subnets

### 27. A group of teams must share one address plan, and each must be able to deploy only into its own subnet. Which two choices fit? Select two.

- A. Grant the basic editor role to the automation
- B. Grant the subnet user role on the specific shared subnets
- C. Give each team its own standalone VPC network
- D. Grant the network administrator role in the host project
- E. Build the network as a Shared VPC with host and service projects

### 28. A VM with no external address must reach Cloud Storage. What should be enabled on its subnet?

- A. Create a Private Service Connect endpoint
- B. Enable Private Google Access on the subnet
- C. Attach the service to Serverless VPC Access
- D. Reach the API through its public interface

### 29. A regulated workload must not read from a bucket outside its own perimeter. What should be configured?

- A. Enclose the project in a VPC Service Controls perimeter
- B. Review Firewall Insights for shadowed rules
- C. Enable Private Google Access on the subnet
- D. Create a hierarchical firewall policy at the organisation

### 30. Two interconnects carry the same prefix and the wrong one is preferred. Which attribute decides?

- A. Switch best path selection back to the legacy behaviour
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Prefer the path with the lower multi-exit discriminator
- D. Give the static route a lower priority number than the learned route

### 31. A regulator requires that a route learned in Europe must not be usable in Asia. What should be confirmed?

- A. Advertise only the ranges the peer needs
- B. Prefer the path with the lower multi-exit discriminator
- C. Switch the Cloud Router to global dynamic routing mode
- D. Keep the Cloud Router in regional dynamic routing mode

### 32. One router serves three regions, and the peer must only see a summary of two ranges. Which two settings fit? Select two.

- A. Switch the Cloud Router to global dynamic routing mode
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Keep the Cloud Router in regional dynamic routing mode
- D. Advertise only the ranges the peer needs
- E. Switch best path selection back to the legacy behaviour

### 33. Only the database tier must leave through the inspection appliance. What should be created?

- A. Add a policy-based route that matches the source and destination
- B. Deploy a multi-NIC appliance VM between the two networks
- C. Create a static route with a tag-scoped next hop
- D. Use the internal load balancer as the next hop

### 34. Traffic to one partner range must be steered through an appliance although the route table says otherwise. What fits?

- A. Give the static route a lower priority number than the learned route
- B. Add a policy-based route that matches the source and destination
- C. Create a static route with a tag-scoped next hop
- D. Use the internal load balancer as the next hop

### 35. An appliance pair must survive the loss of one instance without any route change. What should the route point at?

- A. Create a static route with a tag-scoped next hop
- B. Add a policy-based route that matches the source and destination
- C. Use the internal load balancer as the next hop
- D. Deploy a multi-NIC appliance VM between the two networks

### 36. Three networks must reach each other through one managed hub. What does the hub provide?

- A. Apply a CIDR range filter to the spoke
- B. Expect spoke-to-spoke reachability through the hub
- C. Add the VPC network as a VPC spoke
- D. Assume peered networks can reach each other transitively

### 37. An existing VPC network must export its subnets into the hub. Which spoke type fits?

- A. Add the published service as a producer spoke
- B. Add the attachment as a hybrid spoke
- C. Apply a CIDR range filter to the spoke
- D. Add the VPC network as a VPC spoke

### 38. A cluster cannot create more services although pods have plenty of addresses. What should be resized?

- A. Create a GKE network policy for the namespace
- B. Resize the service range allocation
- C. Add a second pod range to the cluster
- D. Plan secondary ranges for pods and services

### 39. A platform team wants policy enforcement and service routing inside the cluster dataplane. What should be enabled?

- A. Configure an IP masquerade policy on the node pool
- B. Add a second pod range to the cluster
- C. Create a GKE network policy for the namespace
- D. Enable GKE Dataplane V2

### 40. Logs on an external system show pod addresses, and the operator wants only node addresses. What should be configured?

- A. Enable GKE Dataplane V2
- B. Configure an IP masquerade policy on the node pool
- C. Add a second pod range to the cluster
- D. Resize the service range allocation

### 41. A compliance report needs a record of which internal hosts talked to which external ranges. What should be enabled?

- A. Enable Cloud NAT logging
- B. Enable firewall rules logging
- C. Enable Cloud DNS query logging
- D. Enable VPC Flow Logs on the subnet

---

## Domain 3 — Configuring Managed Network Services (Load Balancing, Cloud CDN, and Cloud DNS)

### 42. Backends must drop out when unhealthy, and a stateful client must stay on one backend. Which two settings fit? Select two.

- A. Enable connection draining with a timeout
- B. Enable session affinity on the backend service
- C. Switch the balancing mode to connections per instance
- D. Register the backends as a zonal network endpoint group
- E. Attach a health check to the backend service

### 43. A rolling replacement resets requests that were still running on the old instances. What should be configured?

- A. Autoscale a managed instance group behind the backend service
- B. Enable connection draining with a timeout
- C. Switch the balancing mode to connections per instance
- D. Enable session affinity on the backend service

### 44. Traffic tripled overnight and the instance group stayed at four members. What should be configured?

- A. Switch the balancing mode to connections per instance
- B. Register the third-party origins as an internet network endpoint group
- C. Register the backends as a zonal network endpoint group
- D. Autoscale a managed instance group behind the backend service

### 45. A new version must receive a copy of production requests without answering them. What should be configured?

- A. Route by URL path in the URL map
- B. Rewrite the request path before it reaches the backend
- C. Mirror a copy of the traffic to a second backend
- D. Split traffic between two backend services by weight

### 46. The backend expects a prefix that the public path no longer includes. What should be configured?

- A. Rewrite the request path before it reaches the backend
- B. Route by URL path in the URL map
- C. Mirror a copy of the traffic to a second backend
- D. Split traffic between two backend services by weight

### 47. Individual pods must be registered as backends rather than instances. What should be used?

- A. Register the serverless service as a serverless network endpoint group
- B. Autoscale a managed instance group behind the backend service
- C. Register the third-party origins as an internet network endpoint group
- D. Register the backends as a zonal network endpoint group

### 48. An on-premises application must sit behind the Google front end by hostname and port. What should be registered?

- A. Autoscale a managed instance group behind the backend service
- B. Register the backends as a zonal network endpoint group
- C. Register the third-party origins as an internet network endpoint group
- D. Register the serverless service as a serverless network endpoint group

### 49. A small team wants an external load balancer with the least Kubernetes configuration. What fits?

- A. Register the backends as a zonal network endpoint group
- B. Route by URL path in the URL map
- C. Expose the workload through the GKE Ingress controller
- D. Expose the workload through the GKE Gateway controller

### 50. A gateway must be shared by several namespaces with per-route policy. What fits?

- A. Split traffic between two backend services by weight
- B. Expose the workload through the GKE Gateway controller
- C. Route by URL path in the URL map
- D. Expose the workload through the GKE Ingress controller

### 51. Assets must be cached close to users, and the origin is a third-party storage host. Which two choices fit? Select two.

- A. Serve the object through a signed URL
- B. Register the serverless service as a serverless network endpoint group
- C. Raise the cache time to live
- D. Enable Cloud CDN on the backend service
- E. Point Cloud CDN at the origins through an internet endpoint group

### 52. Origin load is too high and the content changes once a day. What should be raised?

- A. Invalidate the cached object after the change
- B. Serve the object through a signed URL
- C. Raise the cache time to live
- D. Enable Cloud CDN on the backend service

### 53. A host project's private zone must answer for a service project's network, and must not be visible outside. Which two settings fit? Select two.

- A. Migrate the zone with a staged import and a delegated test
- B. Enable DNSSEC on the zone
- C. Create a private Cloud DNS zone
- D. Create a public Cloud DNS zone
- E. Bind the private zone to the service project networks

### 54. An on-premises resolver must query a private zone that lives in a service project. What provides the address?

- A. Configure a DNS forwarding policy for the on-premises domain
- B. Create a private Cloud DNS zone
- C. Create a DNS peering zone to the other project
- D. Create an inbound forwarding policy with a forwarding address

### 55. Traffic must move to a standby region only when the primary fails its health check. Which policy fits?

- A. Enable DNSSEC on the zone
- B. Apply a geolocation routing policy to the record set
- C. Migrate the zone with a staged import and a delegated test
- D. Apply a failover routing policy with a health-checked primary

### 56. European users must resolve the European address and nobody else should. Which policy fits?

- A. Apply a geolocation routing policy to the record set
- B. Lower the record TTL before the cutover
- C. Enable DNSSEC on the zone
- D. Apply a failover routing policy with a health-checked primary

### 57. A resolver must be able to reject a forged answer for the public zone. What should be enabled?

- A. Enable DNSSEC on the zone
- B. Create a private Cloud DNS zone
- C. Enable Cloud DNS query logging
- D. Serve split-horizon answers from separate private and public zones

---

## Domain 4 — Configuring and Implementing Hybrid and Multicloud Interconnectivity (Interconnect, VPN, and Cloud Router)

### 58. A bank's own cage is in a Google colocation facility, and a VLAN must carry one subnet to its router. Which two items fit? Select two.

- A. Order a Dedicated Interconnect connection
- B. Create a VLAN attachment on Cloud Router
- C. Enable MACsec on the interconnect
- D. Deploy an HA VPN gateway with two interfaces
- E. Order a Partner Interconnect connection

### 59. BGP is configured on both routers but no session forms with the circuit. What has not been created?

- A. Create a VLAN attachment on Cloud Router
- B. Create a VPC Network Peering connection between the two networks
- C. Deploy an HA VPN gateway with two interfaces
- D. Add the attachment as a hybrid spoke

### 60. Two circuits in different facilities are required for a 99.99% topology. Which connection type fits?

- A. Order a Cross-Cloud Interconnect connection
- B. Deploy a Classic VPN with a single tunnel
- C. Order a Partner Interconnect connection
- D. Order a Dedicated Interconnect connection

### 61. A site in a country with no Google colocation needs a layer 2 handoff from a carrier. Which fits?

- A. Order a Partner Interconnect connection
- B. Order a Dedicated Interconnect connection
- C. Deploy an HA VPN gateway with two interfaces
- D. Order a Cross-Cloud Interconnect connection

### 62. The carrier offers encryption at layer 2 on a Partner Interconnect attachment. What should be enabled?

- A. Deploy an HA VPN gateway with two interfaces
- B. Create a VLAN attachment on Cloud Router
- C. Enable MACsec on the interconnect
- D. Run HA VPN over Cloud Interconnect instead of MACsec

### 63. Two tunnels must survive one gateway zone failing, and a dead tunnel must be detected in seconds. Which two settings fit? Select two.

- A. Deploy an HA VPN gateway with two interfaces
- B. Prefer the path with the lower multi-exit discriminator
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Deploy a Classic VPN with a single tunnel
- E. Create a VLAN attachment on Cloud Router

### 64. A legacy site has one tunnel and no second path, and the SLA now forbids that. What should be deployed instead?

- A. Order a Dedicated Interconnect connection
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Deploy an HA VPN gateway with two interfaces
- D. Deploy a Classic VPN with a single tunnel

### 65. Two projects must exchange traffic privately and neither will accept peering. What fits?

- A. Deploy a Classic VPN with a single tunnel
- B. Order a Cross-Cloud Interconnect connection
- C. Create a VLAN attachment on Cloud Router
- D. Deploy an HA VPN gateway with two interfaces

### 66. The remote device cannot run dynamic routing and needs policy-based selection. Which VPN fits?

- A. Order a Dedicated Interconnect connection
- B. Deploy a Classic VPN with a single tunnel
- C. Deploy an HA VPN gateway with two interfaces
- D. Set the Cloud Router ASN to a private value that differs from the peer

### 67. A new attachment will not form a session and the far side already uses 64512. What should be changed?

- A. Prefer the path with the lower multi-exit discriminator
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Switch best path selection back to the legacy behaviour
- D. Enable Bidirectional Forwarding Detection with a short interval

### 68. A microwave link fails silently and traffic waits for the BGP hold timer. What should be enabled?

- A. Switch best path selection back to the legacy behaviour
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Prefer the path with the lower multi-exit discriminator
- D. Set the Cloud Router ASN to a private value that differs from the peer

### 69. The primary circuit must be preferred over the backup, and the peer must learn only two ranges. Which two settings fit? Select two.

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Advertise only the ranges the peer needs
- C. Prefer the path with the lower multi-exit discriminator
- D. Give the static route a lower priority number than the learned route
- E. Switch best path selection back to the legacy behaviour

### 70. Two paths carry equal prefixes and one must always lose. Which knob sets that?

- A. Give the static route a lower priority number than the learned route
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Prefer the path with the lower multi-exit discriminator
- D. Enable Bidirectional Forwarding Detection with a short interval

### 71. A routing change altered preference for equal-cost paths without any advertisement change. What should be checked?

- A. Give the static route a lower priority number than the learned route
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Prefer the path with the lower multi-exit discriminator
- D. Switch best path selection back to the legacy behaviour

### 72. The on-premises router must learn two summaries instead of forty subnets. What should be configured?

- A. Switch the Cloud Router to global dynamic routing mode
- B. Advertise only the ranges the peer needs
- C. Give the static route a lower priority number than the learned route
- D. Prefer the path with the lower multi-exit discriminator

### 73. The interconnect hardware does not support link encryption but encryption is mandatory. What should be run instead?

- A. Deploy an HA VPN gateway with two interfaces
- B. Create a VLAN attachment on Cloud Router
- C. Run HA VPN over Cloud Interconnect instead of MACsec
- D. Enable MACsec on the interconnect

---

## Domain 5 — Managing, Monitoring, and Troubleshooting Network Operations (Observability, Troubleshooting, and Traffic Movement)

### 74. A resolver answer must be traced back to the client that asked. What should be enabled?

- A. Enable Cloud DNS query logging
- B. Enable Cloud NAT logging
- C. Enable firewall rules logging
- D. Enable VPC Flow Logs on the subnet

### 75. An IKE negotiation fails every few hours and the reason must be found. What should be enabled?

- A. Enable Cloud DNS query logging
- B. Enable Cloud NAT logging
- C. Enable Cloud VPN logging
- D. Enable VPC Flow Logs on the subnet

### 76. An appliance reports a health value that no managed metric covers. What should be published?

- A. Publish a custom metric from the appliance
- B. Alert on the error budget of the service objective
- C. Create an alert policy on the network metric
- D. Create a log-based metric from the firewall log entries

### 77. Paging fires on interface errors that users never notice. What should drive paging instead?

- A. Alert on the error budget of the service objective
- B. Publish a custom metric from the appliance
- C. Create an alert policy on the network metric
- D. Create a log-based metric from the firewall log entries

### 78. A new subnet cannot reach an on-premises host and the cause is unknown. What should be run first?

- A. Check the Performance Dashboard for packet loss
- B. Inspect the flow in Network Topology
- C. Query Flow Analyzer for the top talkers
- D. Run a Connectivity Test between the two endpoints

### 79. A path must be proved before a change window, and the current flow must be documented afterwards. Which two tools fit? Select two.

- A. Enable Cloud DNS query logging
- B. Inspect the flow in Network Topology
- C. Check the Performance Dashboard for packet loss
- D. Query Flow Analyzer for the top talkers
- E. Run a Connectivity Test between the two endpoints

### 80. A complaint spans several projects and the scope of the loss must be established. What shows project-scoped loss?

- A. Check the Performance Dashboard for packet loss
- B. Test the path with a large ping and the do-not-fragment bit
- C. Inspect the flow in Network Topology
- D. Query Flow Analyzer for the top talkers

### 81. A file transfer over a new tunnel hangs at a consistent size. What should be tested first?

- A. Test the path with a large ping and the do-not-fragment bit
- B. Leave the MTU mismatch unfixed
- C. Check the Performance Dashboard for packet loss
- D. Inspect the flow in Network Topology

### 82. A subnet is close to its address limit and a route is misconfigured. What reports both?

- A. Run a Connectivity Test between the two endpoints
- B. Read the Network Analyzer findings
- C. Review Firewall Insights for shadowed rules
- D. Query Flow Analyzer for the top talkers

### 83. A monthly review must surface configuration risks and rules that never match. Which two tools fit? Select two.

- A. Review Firewall Insights for shadowed rules
- B. Read the Network Analyzer findings
- C. Query Flow Analyzer for the top talkers
- D. Enable Cloud DNS query logging
- E. Run a Connectivity Test between the two endpoints

### 84. Egress cost rose sharply and the heaviest destinations must be found. What should be queried?

- A. Review Firewall Insights for shadowed rules
- B. Check the Performance Dashboard for packet loss
- C. Inspect the flow in Network Topology
- D. Query Flow Analyzer for the top talkers

### 85. A new interconnect must be checked against the intended path. What shows the current path?

- A. Query Flow Analyzer for the top talkers
- B. Check the Performance Dashboard for packet loss
- C. Inspect the flow in Network Topology
- D. Run a Connectivity Test between the two endpoints

### 86. Routes keep appearing and disappearing on one peer only. What should be compared?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Run a Connectivity Test between the two endpoints
- C. Compare the BGP session state on both peers
- D. Prefer the path with the lower multi-exit discriminator

### 87. An old load balancer must be retired without dropping sessions. What should be done first?

- A. Inspect the flow in Network Topology
- B. Enable connection draining with a timeout
- C. Query Flow Analyzer for the top talkers
- D. Drain the backend before removing it

---

## Domain 6 — Configuring, Implementing, and Managing a Cloud Network Security Solution (Cloud Armor, Cloud NGFW, NAT, and Egress Security)

### 88. A backend service must refuse requests from sanctioned regions. What should be attached?

- A. Attach a Cloud Armor backend security policy
- B. Attach a Cloud Armor edge security policy
- C. Enable Adaptive Protection
- D. Add a preconfigured WAF rule for the attack class

### 89. A range must be refused before the proxy consumes any capacity. What should be attached?

- A. Add a rate-based ban rule
- B. Enable bot management on the policy
- C. Attach a Cloud Armor backend security policy
- D. Attach a Cloud Armor edge security policy

### 90. Attack traffic changes shape weekly and nobody can write the rules in time. What should be enabled?

- A. Apply Google Threat Intelligence lists
- B. Enable bot management on the policy
- C. Add a preconfigured WAF rule for the attack class
- D. Enable Adaptive Protection

### 91. Requests come from addresses already known to be malicious infrastructure. What should be applied?

- A. Add a preconfigured WAF rule for the attack class
- B. Enable bot management on the policy
- C. Enable Adaptive Protection
- D. Apply Google Threat Intelligence lists

### 92. One client sends a thousand requests a second and must be blocked for ten minutes. What fits?

- A. Rely on the default DDoS protection and add a rate limit
- B. Add a rate-based ban rule
- C. Enable Adaptive Protection
- D. Apply Google Threat Intelligence lists

### 93. Inspection must apply in every region of a network, and payloads must be examined at layer 7. Which two choices fit? Select two.

- A. Create a VPC firewall rule with a target tag
- B. Create a global network firewall policy
- C. Create a regional network firewall policy
- D. Move the inspection to NGFW Enterprise
- E. Reorder the rules by priority

### 94. A baseline rule must apply to every project in the organisation and cannot be deleted locally. What fits?

- A. Reorder the rules by priority
- B. Create a regional network firewall policy
- C. Create a hierarchical firewall policy at the organisation
- D. Create a VPC firewall rule with a target tag

### 95. A team needs stateful allow and deny rules with no payload inspection. Which tier suffices?

- A. Stay on NGFW Essentials for the VPC rules
- B. Move the inspection to NGFW Enterprise
- C. Move the rules to NGFW Standard
- D. Create a global network firewall policy

### 96. A flat network lets any instance reach any other instance. What should be designed?

- A. Divide the network into micro-segmented tiers
- B. Move the inspection to NGFW Enterprise
- C. Leave the default allow-ingress rule in place
- D. Reorder the rules by priority

### 97. Tag values must not be settable by whoever creates an instance. What should replace network tags?

- A. Reorder the rules by priority
- B. Target the rule with network tags
- C. Use secure tags as the rule target
- D. Target the rule with a service account

### 98. A shared NAT pool must serve sudden short bursts from many instances. What fits?

- A. Use automatic Cloud NAT IP allocation
- B. Use dynamic port allocation
- C. Assign a manual static Cloud NAT address
- D. Use static port allocation

### 99. Outbound requests to a category of sites must be blocked by URL. What fits?

- A. Use dynamic port allocation
- B. Deploy Secure Web Proxy as the egress path
- C. Assign a manual static Cloud NAT address
- D. Configure Packet Mirroring on the instance group

### 100. A collector must receive copies from several networks without an inline appliance. What fits?

- A. Use the internal load balancer as the next hop
- B. Configure Packet Mirroring on the instance group
- C. Inspect the traffic out of band with Packet Mirroring
- D. Deploy a multi-NIC appliance VM between the two networks

---

## Answer key and explanations

### Question 1 — A

Answer: Use the Premium network service tier. Premium keeps the path on the Google network from the Singapore edge into Frankfurt. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. In this case: Premium keeps the path on the Google network from the Singapore edge into Frankfurt.
- **B:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: Premium keeps the path on the Google network from the Singapore edge into Frankfurt.
- **C:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: Premium keeps the path on the Google network from the Singapore edge into Frankfurt.
- **D:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Premium keeps the path on the Google network from the Singapore edge into Frankfurt.

### Question 2 — A

Answer: Use the Standard network service tier. Standard sends the return path over the public internet, which is cheaper for that pattern. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. In this case: Standard sends the return path over the public internet, which is cheaper for that pattern.
- **B:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Standard sends the return path over the public internet, which is cheaper for that pattern.
- **C:** Incorrect for this question. The proxy terminates TLS and forwards a separate connection to the backend. Why the correct answer wins: Standard sends the return path over the public internet, which is cheaper for that pattern.
- **D:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: Standard sends the return path over the public internet, which is cheaper for that pattern.

### Question 3 — C

Answer: Attach a health check to the backend service. A health check removes the dead group from the pool without an operator. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: A health check removes the dead group from the pool without an operator.
- **B:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: A health check removes the dead group from the pool without an operator.
- **C:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: A health check removes the dead group from the pool without an operator.
- **D:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: A health check removes the dead group from the pool without an operator.

### Question 4 — D, E

Answers: Deploy a global external Application Load Balancer; Attach a health check to the backend service. The global address routes users to a live region, and the health check takes the failed one out. A global anycast address routes each user to the closest healthy region. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: The global address routes users to a live region, and the health check takes the failed one out.
- **B:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: The global address routes users to a live region, and the health check takes the failed one out.
- **C:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: The global address routes users to a live region, and the health check takes the failed one out.
- **D:** Correct. A global anycast address routes each user to the closest healthy region. In this case: The global address routes users to a live region, and the health check takes the failed one out.
- **E:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The global address routes users to a live region, and the health check takes the failed one out.

### Question 5 — A

Answer: Configure a DNS forwarding policy for the on-premises domain. A forwarding policy sends that suffix to the resolvers that hold it. Queries for the corporate suffix are forwarded to the on-premises resolvers. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Queries for the corporate suffix are forwarded to the on-premises resolvers. In this case: A forwarding policy sends that suffix to the resolvers that hold it.
- **B:** Incorrect for this question. On-premises resolvers send queries to that address to reach Cloud DNS names. Why the correct answer wins: A forwarding policy sends that suffix to the resolvers that hold it.
- **C:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: A forwarding policy sends that suffix to the resolvers that hold it.
- **D:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: A forwarding policy sends that suffix to the resolvers that hold it.

### Question 6 — A

Answer: Create an inbound forwarding policy with a forwarding address. An inbound forwarding policy publishes a forwarding address for those resolvers. On-premises resolvers send queries to that address to reach Cloud DNS names. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. On-premises resolvers send queries to that address to reach Cloud DNS names. In this case: An inbound forwarding policy publishes a forwarding address for those resolvers.
- **B:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: An inbound forwarding policy publishes a forwarding address for those resolvers.
- **C:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: An inbound forwarding policy publishes a forwarding address for those resolvers.
- **D:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: An inbound forwarding policy publishes a forwarding address for those resolvers.

### Question 7 — C

Answer: Use a proxy Network Load Balancer. A proxy load balancer terminates the client connection and balances the requests behind it. The proxy terminates the client connection and opens a separate one to the backend. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: A proxy load balancer terminates the client connection and balances the requests behind it.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: A proxy load balancer terminates the client connection and balances the requests behind it.
- **C:** Correct. The proxy terminates the client connection and opens a separate one to the backend. In this case: A proxy load balancer terminates the client connection and balances the requests behind it.
- **D:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: A proxy load balancer terminates the client connection and balances the requests behind it.

### Question 8 — D

Answer: Use a passthrough Network Load Balancer. Passthrough keeps the original packet, so the backend still sees the client address. Packets keep their client source address and the backend sees the original flow. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Passthrough keeps the original packet, so the backend still sees the client address.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Passthrough keeps the original packet, so the backend still sees the client address.
- **C:** Incorrect for this question. The proxy terminates the client connection and opens a separate one to the backend. Why the correct answer wins: Passthrough keeps the original packet, so the backend still sees the client address.
- **D:** Correct. Packets keep their client source address and the backend sees the original flow. In this case: Passthrough keeps the original packet, so the backend still sees the client address.

### Question 9 — B

Answer: Deploy the cluster into a shared subnet. Deploying into shared subnets lets the central team own the address plan. The cluster consumes subnets that the host project owns. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: Deploying into shared subnets lets the central team own the address plan.
- **B:** Correct. The cluster consumes subnets that the host project owns. In this case: Deploying into shared subnets lets the central team own the address plan.
- **C:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Deploying into shared subnets lets the central team own the address plan.
- **D:** Incorrect for this question. Nodes reach the control plane and Google APIs through internal paths only. Why the correct answer wins: Deploying into shared subnets lets the central team own the address plan.

### Question 10 — C

Answer: Use the DNS-based control plane endpoint. The DNS-based endpoint resolves through a private name instead of a fixed address. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: The DNS-based endpoint resolves through a private name instead of a fixed address.
- **B:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: The DNS-based endpoint resolves through a private name instead of a fixed address.
- **C:** Correct. In this case: The DNS-based endpoint resolves through a private name instead of a fixed address.
- **D:** Incorrect for this question. The API server is reachable only through the internal address or an authorised network. Why the correct answer wins: The DNS-based endpoint resolves through a private name instead of a fixed address.

### Question 11 — A, D

Answers: Plan secondary ranges for pods and services; Add a second pod range to the cluster. Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later. Alias ranges give pods and services addresses that are separate from the node subnet. An additional alias range gives pods more addresses without rebuilding the cluster. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. An additional alias range gives pods more addresses without rebuilding the cluster. In this case: Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later.
- **B:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later.
- **C:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later.
- **D:** Correct. Alias ranges give pods and services addresses that are separate from the node subnet. In this case: Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later.
- **E:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: Secondary ranges separate pod space from the node subnet, and an extra pod range adds room later.

### Question 12 — B

Answer: Grant the network administrator role in the host project. The network administrator role owns network and subnet objects. That role creates and changes networks and subnets, which a service team should not hold. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: The network administrator role owns network and subnet objects.
- **B:** Correct. That role creates and changes networks and subnets, which a service team should not hold. In this case: The network administrator role owns network and subnet objects.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: The network administrator role owns network and subnet objects.
- **D:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: The network administrator role owns network and subnet objects.

### Question 13 — B, E

Answers: Create a custom role with only the required network permissions; Grant the subnet user role on the specific shared subnets. A custom role can hold just the read permission, and subnet user covers the one deployable subnet. The custom role names the exact permissions the automation needs. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: A custom role can hold just the read permission, and subnet user covers the one deployable subnet.
- **B:** Correct. The custom role names the exact permissions the automation needs. In this case: A custom role can hold just the read permission, and subnet user covers the one deployable subnet.
- **C:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: A custom role can hold just the read permission, and subnet user covers the one deployable subnet.
- **D:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: A custom role can hold just the read permission, and subnet user covers the one deployable subnet.
- **E:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: A custom role can hold just the read permission, and subnet user covers the one deployable subnet.

### Question 14 — C

Answer: Use Direct VPC egress for the serverless workload. Direct VPC egress gives the revision its own address in the subnet. The workload receives its own address in the subnet instead of going through a connector. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Direct VPC egress gives the revision its own address in the subnet.
- **B:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Direct VPC egress gives the revision its own address in the subnet.
- **C:** Correct. The workload receives its own address in the subnet instead of going through a connector. In this case: Direct VPC egress gives the revision its own address in the subnet.
- **D:** Incorrect for this question. A reserved internal range lets a managed service provider peer into the VPC. Why the correct answer wins: Direct VPC egress gives the revision its own address in the subnet.

### Question 15 — A, D

Answers: Create a Private Service Connect endpoint; Allocate a private services access range. The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range. A private endpoint inside the consumer VPC targets a published service attachment. A reserved internal range lets a managed service provider peer into the VPC. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range.
- **B:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range.
- **C:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range.
- **D:** Correct. A reserved internal range lets a managed service provider peer into the VPC. In this case: The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range.
- **E:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: The partner's attachment is consumed through a private endpoint, and the provisioned service needs a reserved private services range.

### Question 16 — B

Answer: Create a VPC Network Peering connection between the two networks. Peering exchanges routes between exactly the two networks involved. Two networks exchange routes directly without a gateway or a shared project. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering exchanges routes between exactly the two networks involved.
- **B:** Correct. Two networks exchange routes directly without a gateway or a shared project. In this case: Peering exchanges routes between exactly the two networks involved.
- **C:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering exchanges routes between exactly the two networks involved.
- **D:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: Peering exchanges routes between exactly the two networks involved.

### Question 17 — C

Answer: Assume peered networks can reach each other transitively. Peering never forwards routes to a third network, so chained peers cannot reach each other. Peering is not transitive, so a route learned through one peer is not passed on to another. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Peering never forwards routes to a third network, so chained peers cannot reach each other.
- **B:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering never forwards routes to a third network, so chained peers cannot reach each other.
- **C:** Correct. Peering is not transitive, so a route learned through one peer is not passed on to another. In this case: Peering never forwards routes to a third network, so chained peers cannot reach each other.
- **D:** Incorrect for this question. The hub forwards between spokes, which peering alone cannot do. Why the correct answer wins: Peering never forwards routes to a third network, so chained peers cannot reach each other.

### Question 18 — D

Answer: Automate address allocation from a central IPAM plan. Automated allocation from one authoritative plan removes hand-picked overlaps. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Automated allocation from one authoritative plan removes hand-picked overlaps.
- **B:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Automated allocation from one authoritative plan removes hand-picked overlaps.
- **C:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Automated allocation from one authoritative plan removes hand-picked overlaps.
- **D:** Correct. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. In this case: Automated allocation from one authoritative plan removes hand-picked overlaps.

### Question 19 — A

Answer: Bring your own public IP prefixes. Bring your own IP advertises the prefixes the organisation already holds. Public prefixes the organisation already owns are advertised from Google Cloud. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Public prefixes the organisation already owns are advertised from Google Cloud. In this case: Bring your own IP advertises the prefixes the organisation already holds.
- **B:** Incorrect for this question. Source addresses are translated so two networks with the same private ranges can still talk. Why the correct answer wins: Bring your own IP advertises the prefixes the organisation already holds.
- **C:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Bring your own IP advertises the prefixes the organisation already holds.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Bring your own IP advertises the prefixes the organisation already holds.

### Question 20 — B

Answer: Raise the VPC MTU to 8896 bytes. A larger MTU carries more payload per packet on links that support it. A larger maximum transmission unit carries more payload per packet inside the VPC. Local study-map skill 1.10 (MTU Sizing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: A larger MTU carries more payload per packet on links that support it.
- **B:** Correct. A larger maximum transmission unit carries more payload per packet inside the VPC. In this case: A larger MTU carries more payload per packet on links that support it.
- **C:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A larger MTU carries more payload per packet on links that support it.
- **D:** Incorrect for this question. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Why the correct answer wins: A larger MTU carries more payload per packet on links that support it.

### Question 21 — A

Answer: Deploy a multi-NIC appliance VM between the two networks. An appliance with an interface in each network can inspect and forward between them. Local study-map skill 1.11 (Third-Party Appliance Insertion), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: An appliance with an interface in each network can inspect and forward between them.
- **B:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: An appliance with an interface in each network can inspect and forward between them.
- **C:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: An appliance with an interface in each network can inspect and forward between them.
- **D:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: An appliance with an interface in each network can inspect and forward between them.

### Question 22 — B

Answer: Expand the existing subnet range. Growing the prefix adds addresses while the existing instances keep theirs. A subnet prefix can grow within its address range, and the growth cannot shrink later. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Growing the prefix adds addresses while the existing instances keep theirs.
- **B:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing the prefix adds addresses while the existing instances keep theirs.
- **C:** Incorrect for this question. The subnet carries both an IPv4 range and an internal or external IPv6 range. Why the correct answer wins: Growing the prefix adds addresses while the existing instances keep theirs.
- **D:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Growing the prefix adds addresses while the existing instances keep theirs.

### Question 23 — B, C

Answers: Expand the existing subnet range; Accept the overlapping subnet ranges as configured. Growing the prefix adds space, and rejecting the colliding range keeps the plan routable. A subnet prefix can grow within its address range, and the growth cannot shrink later. Two subnets with the same prefix cannot be routed to each other without translation. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Growing the prefix adds space, and rejecting the colliding range keeps the plan routable.
- **B:** Correct. Two subnets with the same prefix cannot be routed to each other without translation. In this case: Growing the prefix adds space, and rejecting the colliding range keeps the plan routable.
- **C:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing the prefix adds space, and rejecting the colliding range keeps the plan routable.
- **D:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Growing the prefix adds space, and rejecting the colliding range keeps the plan routable.
- **E:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Growing the prefix adds space, and rejecting the colliding range keeps the plan routable.

### Question 24 — B

Answer: Create a VPC Network Peering connection between the two networks. Peering joins the two networks, and firewall policy then limits what is reachable. Two networks exchange routes directly without a gateway or a shared project. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: Peering joins the two networks, and firewall policy then limits what is reachable.
- **B:** Correct. Two networks exchange routes directly without a gateway or a shared project. In this case: Peering joins the two networks, and firewall policy then limits what is reachable.
- **C:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering joins the two networks, and firewall policy then limits what is reachable.
- **D:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering joins the two networks, and firewall policy then limits what is reachable.

### Question 25 — D

Answer: Import and export custom routes over the peering. Exporting custom routes carries them to the peered network. The peering option carries static and policy-based routes between the two networks. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: Exporting custom routes carries them to the peered network.
- **B:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: Exporting custom routes carries them to the peered network.
- **C:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Exporting custom routes carries them to the peered network.
- **D:** Correct. The peering option carries static and policy-based routes between the two networks. In this case: Exporting custom routes carries them to the peered network.

### Question 26 — A

Answer: Grant Shared VPC Admin on the host project. Shared VPC Admin attaches service projects to the host. That role attaches service projects and delegates subnet use. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC Admin attaches service projects to the host.
- **B:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: Shared VPC Admin attaches service projects to the host.
- **C:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC Admin attaches service projects to the host.
- **D:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: Shared VPC Admin attaches service projects to the host.

### Question 27 — B, E

Answers: Build the network as a Shared VPC with host and service projects; Grant the subnet user role on the specific shared subnets. Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use. One host project owns the network and subnets while service projects deploy into shared subnets. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use.
- **B:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use.
- **C:** Incorrect for this question. Separate projects own separate networks, and nothing is shared implicitly. Why the correct answer wins: Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use.
- **D:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use.
- **E:** Correct. One host project owns the network and subnets while service projects deploy into shared subnets. In this case: Shared VPC centralises the plan, and subnet user on one subnet limits what each team can use.

### Question 28 — B

Answer: Enable Private Google Access on the subnet. Private Google Access lets the instance reach Google APIs over internal routing. Instances without external addresses reach Google APIs through internal routing. Local study-map skill 2.4 (Private Google Access and APIs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Private Google Access lets the instance reach Google APIs over internal routing.
- **B:** Correct. Instances without external addresses reach Google APIs through internal routing. In this case: Private Google Access lets the instance reach Google APIs over internal routing.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Private Google Access lets the instance reach Google APIs over internal routing.
- **D:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Private Google Access lets the instance reach Google APIs over internal routing.

### Question 29 — A

Answer: Enclose the project in a VPC Service Controls perimeter. A service perimeter blocks data access across its boundary. The perimeter restricts which services the project may call and blocks data movement outside it. Local study-map skill 2.5 (VPC Service Controls Perimeters), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The perimeter restricts which services the project may call and blocks data movement outside it. In this case: A service perimeter blocks data access across its boundary.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: A service perimeter blocks data access across its boundary.
- **C:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A service perimeter blocks data access across its boundary.
- **D:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A service perimeter blocks data access across its boundary.

### Question 30 — C

Answer: Prefer the path with the lower multi-exit discriminator. The lower multi-exit discriminator is preferred between otherwise equal paths. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower multi-exit discriminator is preferred between otherwise equal paths.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower multi-exit discriminator is preferred between otherwise equal paths.
- **C:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The lower multi-exit discriminator is preferred between otherwise equal paths.
- **D:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The lower multi-exit discriminator is preferred between otherwise equal paths.

### Question 31 — D

Answer: Keep the Cloud Router in regional dynamic routing mode. Regional dynamic routing keeps each learned route inside the region that learned it. Routes stay inside the region that learned them. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: Regional dynamic routing keeps each learned route inside the region that learned it.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Regional dynamic routing keeps each learned route inside the region that learned it.
- **C:** Incorrect for this question. Routes learned in one region are available to subnets in every region. Why the correct answer wins: Regional dynamic routing keeps each learned route inside the region that learned it.
- **D:** Correct. Routes stay inside the region that learned them. In this case: Regional dynamic routing keeps each learned route inside the region that learned it.

### Question 32 — A, D

Answers: Switch the Cloud Router to global dynamic routing mode; Advertise only the ranges the peer needs. Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees. Routes learned in one region are available to subnets in every region. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees.
- **C:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees.
- **D:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees.
- **E:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Global mode makes the learned routes usable in every region, and the advertisement list limits what the peer sees.

### Question 33 — C

Answer: Create a static route with a tag-scoped next hop. A tag-scoped static route applies only to instances carrying that tag. Only instances carrying the tag send their traffic through the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: A tag-scoped static route applies only to instances carrying that tag.
- **B:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A tag-scoped static route applies only to instances carrying that tag.
- **C:** Correct. Only instances carrying the tag send their traffic through the appliance. In this case: A tag-scoped static route applies only to instances carrying that tag.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A tag-scoped static route applies only to instances carrying that tag.

### Question 34 — B

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches the flow before the ordinary route table decides. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A policy-based route matches the flow before the ordinary route table decides.
- **B:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches the flow before the ordinary route table decides.
- **C:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches the flow before the ordinary route table decides.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches the flow before the ordinary route table decides.

### Question 35 — C

Answer: Use the internal load balancer as the next hop. The internal load balancer picks the surviving appliance automatically. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 2.8 (Internal Load Balancer as Next Hop), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer picks the surviving appliance automatically.
- **B:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer picks the surviving appliance automatically.
- **C:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer picks the surviving appliance automatically.
- **D:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer picks the surviving appliance automatically.

### Question 36 — B

Answer: Expect spoke-to-spoke reachability through the hub. The hub forwards between spokes, which is the transitivity that peering lacks. The hub forwards between spokes, which peering alone cannot do. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: The hub forwards between spokes, which is the transitivity that peering lacks.
- **B:** Correct. The hub forwards between spokes, which peering alone cannot do. In this case: The hub forwards between spokes, which is the transitivity that peering lacks.
- **C:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: The hub forwards between spokes, which is the transitivity that peering lacks.
- **D:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: The hub forwards between spokes, which is the transitivity that peering lacks.

### Question 37 — D

Answer: Add the VPC network as a VPC spoke. A VPC spoke exports the network's subnets to the hub. The spoke exports the network subnets to the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The spoke publishes a service attachment so consumers reach it through the hub. Why the correct answer wins: A VPC spoke exports the network's subnets to the hub.
- **B:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: A VPC spoke exports the network's subnets to the hub.
- **C:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: A VPC spoke exports the network's subnets to the hub.
- **D:** Correct. The spoke exports the network subnets to the hub. In this case: A VPC spoke exports the network's subnets to the hub.

### Question 38 — B

Answer: Resize the service range allocation. The service range must have room for the services the cluster will create. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The service range must have room for the services the cluster will create.
- **B:** Correct. In this case: The service range must have room for the services the cluster will create.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The service range must have room for the services the cluster will create.
- **D:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: The service range must have room for the services the cluster will create.

### Question 39 — D

Answer: Enable GKE Dataplane V2. The eBPF dataplane handles policy and service routing in the cluster. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: The eBPF dataplane handles policy and service routing in the cluster.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The eBPF dataplane handles policy and service routing in the cluster.
- **C:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The eBPF dataplane handles policy and service routing in the cluster.
- **D:** Correct. In this case: The eBPF dataplane handles policy and service routing in the cluster.

### Question 40 — B

Answer: Configure an IP masquerade policy on the node pool. The masquerade policy translates pod source addresses to the node address. Outbound pod traffic is translated to the node address under the chosen conditions. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: The masquerade policy translates pod source addresses to the node address.
- **B:** Correct. Outbound pod traffic is translated to the node address under the chosen conditions. In this case: The masquerade policy translates pod source addresses to the node address.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The masquerade policy translates pod source addresses to the node address.
- **D:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: The masquerade policy translates pod source addresses to the node address.

### Question 41 — D

Answer: Enable VPC Flow Logs on the subnet. Flow logs record the source, destination, port and byte counts of sampled connections. Local study-map skill 2.11 (VPC Flow Logs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Flow logs record the source, destination, port and byte counts of sampled connections.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: Flow logs record the source, destination, port and byte counts of sampled connections.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Flow logs record the source, destination, port and byte counts of sampled connections.
- **D:** Correct. In this case: Flow logs record the source, destination, port and byte counts of sampled connections.

### Question 42 — B, E

Answers: Attach a health check to the backend service; Enable session affinity on the backend service. The health check removes the unhealthy backend, and affinity keeps that client where its state is. The check removes a backend that cannot answer, so traffic moves to a healthy one. Affinity keeps a client on the backend that already holds its session state. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: The health check removes the unhealthy backend, and affinity keeps that client where its state is.
- **B:** Correct. Affinity keeps a client on the backend that already holds its session state. In this case: The health check removes the unhealthy backend, and affinity keeps that client where its state is.
- **C:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: The health check removes the unhealthy backend, and affinity keeps that client where its state is.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The health check removes the unhealthy backend, and affinity keeps that client where its state is.
- **E:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The health check removes the unhealthy backend, and affinity keeps that client where its state is.

### Question 43 — B

Answer: Enable connection draining with a timeout. Draining waits for in-flight requests before the backend is detached. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: Draining waits for in-flight requests before the backend is detached.
- **B:** Correct. In this case: Draining waits for in-flight requests before the backend is detached.
- **C:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: Draining waits for in-flight requests before the backend is detached.
- **D:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: Draining waits for in-flight requests before the backend is detached.

### Question 44 — D

Answer: Autoscale a managed instance group behind the backend service. An autoscaler adds members as the chosen signal rises. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: An autoscaler adds members as the chosen signal rises.
- **B:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: An autoscaler adds members as the chosen signal rises.
- **C:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An autoscaler adds members as the chosen signal rises.
- **D:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: An autoscaler adds members as the chosen signal rises.

### Question 45 — C

Answer: Mirror a copy of the traffic to a second backend. Mirroring sends the copy for inspection while the primary answers. The mirrored request is sent for inspection while the response comes only from the primary. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Mirroring sends the copy for inspection while the primary answers.
- **B:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: Mirroring sends the copy for inspection while the primary answers.
- **C:** Correct. The mirrored request is sent for inspection while the response comes only from the primary. In this case: Mirroring sends the copy for inspection while the primary answers.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Mirroring sends the copy for inspection while the primary answers.

### Question 46 — A

Answer: Rewrite the request path before it reaches the backend. The rewrite presents the backend with the path it expects. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: The rewrite presents the backend with the path it expects.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The rewrite presents the backend with the path it expects.
- **C:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: The rewrite presents the backend with the path it expects.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The rewrite presents the backend with the path it expects.

### Question 47 — D

Answer: Register the backends as a zonal network endpoint group. A zonal endpoint group addresses specific endpoints such as pods. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: A zonal endpoint group addresses specific endpoints such as pods.
- **B:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: A zonal endpoint group addresses specific endpoints such as pods.
- **C:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: A zonal endpoint group addresses specific endpoints such as pods.
- **D:** Correct. In this case: A zonal endpoint group addresses specific endpoints such as pods.

### Question 48 — C

Answer: Register the third-party origins as an internet network endpoint group. An internet endpoint group targets endpoints outside Google Cloud. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: An internet endpoint group targets endpoints outside Google Cloud.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An internet endpoint group targets endpoints outside Google Cloud.
- **C:** Correct. In this case: An internet endpoint group targets endpoints outside Google Cloud.
- **D:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: An internet endpoint group targets endpoints outside Google Cloud.

### Question 49 — C

Answer: Expose the workload through the GKE Ingress controller. The Ingress controller creates the load balancer from one object. An Ingress object creates a Google Cloud load balancer from the manifest. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The Ingress controller creates the load balancer from one object.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Ingress controller creates the load balancer from one object.
- **C:** Correct. An Ingress object creates a Google Cloud load balancer from the manifest. In this case: The Ingress controller creates the load balancer from one object.
- **D:** Incorrect for this question. A Gateway object configures the load balancer through the newer Kubernetes API. Why the correct answer wins: The Ingress controller creates the load balancer from one object.

### Question 50 — B

Answer: Expose the workload through the GKE Gateway controller. The Gateway controller supports shared gateways and route-level policy. A Gateway object configures the load balancer through the newer Kubernetes API. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The Gateway controller supports shared gateways and route-level policy.
- **B:** Correct. A Gateway object configures the load balancer through the newer Kubernetes API. In this case: The Gateway controller supports shared gateways and route-level policy.
- **C:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Gateway controller supports shared gateways and route-level policy.
- **D:** Incorrect for this question. An Ingress object creates a Google Cloud load balancer from the manifest. Why the correct answer wins: The Gateway controller supports shared gateways and route-level policy.

### Question 51 — D, E

Answers: Enable Cloud CDN on the backend service; Point Cloud CDN at the origins through an internet endpoint group. Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin. The edge holds a copy of the response so later requests are served closer to the user. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL authorises one object for a limited time without making the bucket public. Why the correct answer wins: Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin.
- **B:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin.
- **C:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin.
- **D:** Correct. The edge holds a copy of the response so later requests are served closer to the user. In this case: Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin.
- **E:** Correct. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. In this case: Caching at the edge shortens the fetch, and the internet endpoint group lets the CDN reach that origin.

### Question 52 — C

Answer: Raise the cache time to live. A longer lifetime cuts origin fetches when the content rarely changes. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Invalidation removes the stale copy so the next request fetches the current version. Why the correct answer wins: A longer lifetime cuts origin fetches when the content rarely changes.
- **B:** Incorrect for this question. A signed URL authorises one object for a limited time without making the bucket public. Why the correct answer wins: A longer lifetime cuts origin fetches when the content rarely changes.
- **C:** Correct. A longer lifetime reduces origin load and lengthens the window in which content can be stale. In this case: A longer lifetime cuts origin fetches when the content rarely changes.
- **D:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: A longer lifetime cuts origin fetches when the content rarely changes.

### Question 53 — C, E

Answers: Create a private Cloud DNS zone; Bind the private zone to the service project networks. The private zone stays internal, and the cross-project binding extends it to that network. The zone answers only for clients inside the authorised networks. The binding makes the host project's zone answer for the service project's networks. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The private zone stays internal, and the cross-project binding extends it to that network.
- **B:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The private zone stays internal, and the cross-project binding extends it to that network.
- **C:** Correct. The zone answers only for clients inside the authorised networks. In this case: The private zone stays internal, and the cross-project binding extends it to that network.
- **D:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: The private zone stays internal, and the cross-project binding extends it to that network.
- **E:** Correct. The binding makes the host project's zone answer for the service project's networks. In this case: The private zone stays internal, and the cross-project binding extends it to that network.

### Question 54 — D

Answer: Create an inbound forwarding policy with a forwarding address. An inbound forwarding policy in that project gives the resolver an address to use. On-premises resolvers send queries to that address to reach Cloud DNS names. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: An inbound forwarding policy in that project gives the resolver an address to use.
- **B:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: An inbound forwarding policy in that project gives the resolver an address to use.
- **C:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: An inbound forwarding policy in that project gives the resolver an address to use.
- **D:** Correct. On-premises resolvers send queries to that address to reach Cloud DNS names. In this case: An inbound forwarding policy in that project gives the resolver an address to use.

### Question 55 — D

Answer: Apply a failover routing policy with a health-checked primary. The failover policy answers with the standby only while the primary is unhealthy. The standby answer is served when the primary fails its health check. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The failover policy answers with the standby only while the primary is unhealthy.
- **B:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy answers with the standby only while the primary is unhealthy.
- **C:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The failover policy answers with the standby only while the primary is unhealthy.
- **D:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy answers with the standby only while the primary is unhealthy.

### Question 56 — A

Answer: Apply a geolocation routing policy to the record set. The geolocation policy answers from the source region of the query. The answer depends on the source region of the query. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The answer depends on the source region of the query. In this case: The geolocation policy answers from the source region of the query.
- **B:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: The geolocation policy answers from the source region of the query.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The geolocation policy answers from the source region of the query.
- **D:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: The geolocation policy answers from the source region of the query.

### Question 57 — A

Answer: Enable DNSSEC on the zone. Signed answers let the resolver verify the response. Signatures let a resolver verify that the answer was not altered in transit. Local study-map skill 3.8 (DNSSEC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Signatures let a resolver verify that the answer was not altered in transit. In this case: Signed answers let the resolver verify the response.
- **B:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: Signed answers let the resolver verify the response.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Signed answers let the resolver verify the response.
- **D:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: Signed answers let the resolver verify the response.

### Question 58 — A, B

Answers: Order a Dedicated Interconnect connection; Create a VLAN attachment on Cloud Router. The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router. A private physical circuit connects the premises to a Google colocation facility. The attachment carries one VLAN over the interconnect and peers with the router. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router.
- **B:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router.
- **C:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router.
- **E:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the traffic to the router.

### Question 59 — A

Answer: Create a VLAN attachment on Cloud Router. The VLAN attachment is the object the router peers over. The attachment carries one VLAN over the interconnect and peers with the router. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The VLAN attachment is the object the router peers over.
- **B:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: The VLAN attachment is the object the router peers over.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: The VLAN attachment is the object the router peers over.
- **D:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: The VLAN attachment is the object the router peers over.

### Question 60 — D

Answer: Order a Dedicated Interconnect connection. Dedicated Interconnect supplies the physical circuits each facility needs. A private physical circuit connects the premises to a Google colocation facility. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: Dedicated Interconnect supplies the physical circuits each facility needs.
- **B:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Dedicated Interconnect supplies the physical circuits each facility needs.
- **C:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Dedicated Interconnect supplies the physical circuits each facility needs.
- **D:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: Dedicated Interconnect supplies the physical circuits each facility needs.

### Question 61 — A

Answer: Order a Partner Interconnect connection. Partner Interconnect delivers the circuit through the carrier. A service provider carries the circuit to Google on the customer behalf. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A service provider carries the circuit to Google on the customer behalf. In this case: Partner Interconnect delivers the circuit through the carrier.
- **B:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.
- **D:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.

### Question 62 — C

Answer: Enable MACsec on the interconnect. MACsec protects the link between the premises and Google. Link-layer encryption protects each hop of the circuit between the premises and Google. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: MACsec protects the link between the premises and Google.
- **B:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: MACsec protects the link between the premises and Google.
- **C:** Correct. Link-layer encryption protects each hop of the circuit between the premises and Google. In this case: MACsec protects the link between the premises and Google.
- **D:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: MACsec protects the link between the premises and Google.

### Question 63 — A, C

Answers: Deploy an HA VPN gateway with two interfaces; Enable Bidirectional Forwarding Detection with a short interval. The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly. Two interfaces in different zones give the tunnel pair a 99.99% topology. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly.
- **C:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly.
- **D:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly.
- **E:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: The two-interface gateway spreads the tunnels across zones, and BFD detects the failure quickly.

### Question 64 — D

Answer: Deploy a Classic VPN with a single tunnel. An HA VPN gives the redundant pair the SLA requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: An HA VPN gives the redundant pair the SLA requires.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: An HA VPN gives the redundant pair the SLA requires.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: An HA VPN gives the redundant pair the SLA requires.
- **D:** Correct. One tunnel gives a single path and no automatic failover. In this case: An HA VPN gives the redundant pair the SLA requires.

### Question 65 — D

Answer: Deploy an HA VPN gateway with two interfaces. An HA VPN between the networks carries the traffic inside the Google network. Two interfaces in different zones give the tunnel pair a 99.99% topology. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: An HA VPN between the networks carries the traffic inside the Google network.
- **B:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: An HA VPN between the networks carries the traffic inside the Google network.
- **C:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: An HA VPN between the networks carries the traffic inside the Google network.
- **D:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: An HA VPN between the networks carries the traffic inside the Google network.

### Question 66 — B

Answer: Deploy a Classic VPN with a single tunnel. Classic VPN supports policy-based tunnels for devices without BGP. One tunnel gives a single path and no automatic failover. Local study-map skill 4.4 (Classic VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Classic VPN supports policy-based tunnels for devices without BGP.
- **B:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports policy-based tunnels for devices without BGP.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Classic VPN supports policy-based tunnels for devices without BGP.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Classic VPN supports policy-based tunnels for devices without BGP.

### Question 67 — B

Answer: Set the Cloud Router ASN to a private value that differs from the peer. The two peers must use different autonomous system numbers. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The two peers must use different autonomous system numbers.
- **B:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The two peers must use different autonomous system numbers.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The two peers must use different autonomous system numbers.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The two peers must use different autonomous system numbers.

### Question 68 — B

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the dead path before the hold timer expires. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: BFD detects the dead path before the hold timer expires.
- **B:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the dead path before the hold timer expires.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the dead path before the hold timer expires.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the dead path before the hold timer expires.

### Question 69 — B, C

Answers: Prefer the path with the lower multi-exit discriminator; Advertise only the ranges the peer needs. The lower discriminator makes the primary preferred, and the advertisement list limits what is announced. The lower discriminator wins when the same prefix arrives over two attachments. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower discriminator makes the primary preferred, and the advertisement list limits what is announced.
- **B:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: The lower discriminator makes the primary preferred, and the advertisement list limits what is announced.
- **C:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The lower discriminator makes the primary preferred, and the advertisement list limits what is announced.
- **D:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The lower discriminator makes the primary preferred, and the advertisement list limits what is announced.
- **E:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower discriminator makes the primary preferred, and the advertisement list limits what is announced.

### Question 70 — C

Answer: Prefer the path with the lower multi-exit discriminator. A higher multi-exit discriminator makes that path less preferred. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 4.6 (BFD and Failover Timers), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A higher multi-exit discriminator makes that path less preferred.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A higher multi-exit discriminator makes that path less preferred.
- **C:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: A higher multi-exit discriminator makes that path less preferred.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: A higher multi-exit discriminator makes that path less preferred.

### Question 71 — D

Answer: Switch best path selection back to the legacy behaviour. The best path selection setting decides how those ties are broken. The older selection order picks a different preferred path when the inputs tie. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The best path selection setting decides how those ties are broken.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The best path selection setting decides how those ties are broken.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The best path selection setting decides how those ties are broken.
- **D:** Correct. The older selection order picks a different preferred path when the inputs tie. In this case: The best path selection setting decides how those ties are broken.

### Question 72 — B

Answer: Advertise only the ranges the peer needs. A custom advertisement list publishes the chosen prefixes only. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Routes learned in one region are available to subnets in every region. Why the correct answer wins: A custom advertisement list publishes the chosen prefixes only.
- **B:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: A custom advertisement list publishes the chosen prefixes only.
- **C:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A custom advertisement list publishes the chosen prefixes only.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: A custom advertisement list publishes the chosen prefixes only.

### Question 73 — C

Answer: Run HA VPN over Cloud Interconnect instead of MACsec. IPsec tunnels over the interconnect encrypt the traffic where MACsec is unavailable. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Local study-map skill 4.8 (Interconnect Encryption and SLA), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: IPsec tunnels over the interconnect encrypt the traffic where MACsec is unavailable.
- **B:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: IPsec tunnels over the interconnect encrypt the traffic where MACsec is unavailable.
- **C:** Correct. IPsec tunnels inside the interconnect give encryption where MACsec is not available. In this case: IPsec tunnels over the interconnect encrypt the traffic where MACsec is unavailable.
- **D:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: IPsec tunnels over the interconnect encrypt the traffic where MACsec is unavailable.

### Question 74 — A

Answer: Enable Cloud DNS query logging. DNS query logging records the names asked for and the answers returned. The logs record the names that clients asked for and the answers they received. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs record the names that clients asked for and the answers they received. In this case: DNS query logging records the names asked for and the answers returned.
- **B:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: DNS query logging records the names asked for and the answers returned.
- **C:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: DNS query logging records the names asked for and the answers returned.
- **D:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: DNS query logging records the names asked for and the answers returned.

### Question 75 — C

Answer: Enable Cloud VPN logging. VPN logging records tunnel state changes and negotiation outcomes. The logs record tunnel state changes and IKE negotiation outcomes. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: VPN logging records tunnel state changes and negotiation outcomes.
- **B:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: VPN logging records tunnel state changes and negotiation outcomes.
- **C:** Correct. The logs record tunnel state changes and IKE negotiation outcomes. In this case: VPN logging records tunnel state changes and negotiation outcomes.
- **D:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: VPN logging records tunnel state changes and negotiation outcomes.

### Question 76 — A

Answer: Publish a custom metric from the appliance. A custom metric carries the appliance's own signal into Monitoring. The appliance reports a signal that no managed metric covers. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The appliance reports a signal that no managed metric covers. In this case: A custom metric carries the appliance's own signal into Monitoring.
- **B:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: A custom metric carries the appliance's own signal into Monitoring.
- **C:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: A custom metric carries the appliance's own signal into Monitoring.
- **D:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: A custom metric carries the appliance's own signal into Monitoring.

### Question 77 — A

Answer: Alert on the error budget of the service objective. Alerting on the error budget follows the reliability users actually experience. The alert fires on the reliability users experience rather than on a single resource. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The alert fires on the reliability users experience rather than on a single resource. In this case: Alerting on the error budget follows the reliability users actually experience.
- **B:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: Alerting on the error budget follows the reliability users actually experience.
- **C:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: Alerting on the error budget follows the reliability users actually experience.
- **D:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: Alerting on the error budget follows the reliability users actually experience.

### Question 78 — D

Answer: Run a Connectivity Test between the two endpoints. A connectivity test evaluates the path configuration and names the blocking rule. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A connectivity test evaluates the path configuration and names the blocking rule.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A connectivity test evaluates the path configuration and names the blocking rule.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: A connectivity test evaluates the path configuration and names the blocking rule.
- **D:** Correct. In this case: A connectivity test evaluates the path configuration and names the blocking rule.

### Question 79 — B, E

Answers: Run a Connectivity Test between the two endpoints; Inspect the flow in Network Topology. The test proves reachability before the change, and the topology view documents what carries the traffic. The test evaluates the configuration along the path and names the blocking rule or missing route. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The test proves reachability before the change, and the topology view documents what carries the traffic.
- **B:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: The test proves reachability before the change, and the topology view documents what carries the traffic.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: The test proves reachability before the change, and the topology view documents what carries the traffic.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The test proves reachability before the change, and the topology view documents what carries the traffic.
- **E:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: The test proves reachability before the change, and the topology view documents what carries the traffic.

### Question 80 — A

Answer: Check the Performance Dashboard for packet loss. The performance dashboard reports loss and latency per scope. The dashboard separates loss on the Google network from loss outside it. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The dashboard separates loss on the Google network from loss outside it. In this case: The performance dashboard reports loss and latency per scope.
- **B:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: The performance dashboard reports loss and latency per scope.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The performance dashboard reports loss and latency per scope.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The performance dashboard reports loss and latency per scope.

### Question 81 — A

Answer: Test the path with a large ping and the do-not-fragment bit. A large probe shows the size at which the payload stops crossing the path. The probe shows where the payload stops fitting along the path. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The probe shows where the payload stops fitting along the path. In this case: A large probe shows the size at which the payload stops crossing the path.
- **B:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A large probe shows the size at which the payload stops crossing the path.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A large probe shows the size at which the payload stops crossing the path.
- **D:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A large probe shows the size at which the payload stops crossing the path.

### Question 82 — B

Answer: Read the Network Analyzer findings. Network Analyzer reports configuration risks including quota pressure. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Analyzer reports configuration risks including quota pressure.
- **B:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Network Analyzer reports configuration risks including quota pressure.
- **C:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Network Analyzer reports configuration risks including quota pressure.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Analyzer reports configuration risks including quota pressure.

### Question 83 — A, B

Answers: Read the Network Analyzer findings; Review Firewall Insights for shadowed rules. The analyser reports the risks, and firewall insights lists the unused rules. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. The insight names rules that never match because a broader rule already covered them. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: The analyser reports the risks, and firewall insights lists the unused rules.
- **B:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: The analyser reports the risks, and firewall insights lists the unused rules.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The analyser reports the risks, and firewall insights lists the unused rules.
- **D:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The analyser reports the risks, and firewall insights lists the unused rules.
- **E:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: The analyser reports the risks, and firewall insights lists the unused rules.

### Question 84 — D

Answer: Query Flow Analyzer for the top talkers. Flow Analyzer ranks flows so the heaviest destinations appear first. The analysis ranks the flows that consume the most bandwidth. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Flow Analyzer ranks flows so the heaviest destinations appear first.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Flow Analyzer ranks flows so the heaviest destinations appear first.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Flow Analyzer ranks flows so the heaviest destinations appear first.
- **D:** Correct. The analysis ranks the flows that consume the most bandwidth. In this case: Flow Analyzer ranks flows so the heaviest destinations appear first.

### Question 85 — C

Answer: Inspect the flow in Network Topology. Network Topology draws the paths and throughput between the resources. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Topology draws the paths and throughput between the resources.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Network Topology draws the paths and throughput between the resources.
- **C:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: Network Topology draws the paths and throughput between the resources.
- **D:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Topology draws the paths and throughput between the resources.

### Question 86 — C

Answer: Compare the BGP session state on both peers. Comparing both peers separates a local configuration fault from a path fault. A session that is established on one side only points at the shared configuration. Local study-map skill 5.7 (BGP and VPN Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Comparing both peers separates a local configuration fault from a path fault.
- **B:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Comparing both peers separates a local configuration fault from a path fault.
- **C:** Correct. A session that is established on one side only points at the shared configuration. In this case: Comparing both peers separates a local configuration fault from a path fault.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Comparing both peers separates a local configuration fault from a path fault.

### Question 87 — D

Answer: Drain the backend before removing it. Draining moves new flows elsewhere and lets the existing ones finish. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 5.8 (Traffic Draining and Migration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Draining moves new flows elsewhere and lets the existing ones finish.
- **B:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Draining moves new flows elsewhere and lets the existing ones finish.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Draining moves new flows elsewhere and lets the existing ones finish.
- **D:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: Draining moves new flows elsewhere and lets the existing ones finish.

### Question 88 — A

Answer: Attach a Cloud Armor backend security policy. A backend security policy filters traffic that reached the load balancer. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A backend security policy filters traffic that reached the load balancer.
- **B:** Incorrect for this question. The policy filters traffic at the edge before it is proxied to a backend. Why the correct answer wins: A backend security policy filters traffic that reached the load balancer.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A backend security policy filters traffic that reached the load balancer.
- **D:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: A backend security policy filters traffic that reached the load balancer.

### Question 89 — D

Answer: Attach a Cloud Armor edge security policy. An edge security policy filters the request before it is proxied. The policy filters traffic at the edge before it is proxied to a backend. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: An edge security policy filters the request before it is proxied.
- **B:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: An edge security policy filters the request before it is proxied.
- **C:** Incorrect for this question. The policy filters traffic that has already reached the load balancer. Why the correct answer wins: An edge security policy filters the request before it is proxied.
- **D:** Correct. The policy filters traffic at the edge before it is proxied to a backend. In this case: An edge security policy filters the request before it is proxied.

### Question 90 — D

Answer: Enable Adaptive Protection. Adaptive Protection learns the normal pattern and proposes rules for the anomaly. The model learns the normal request pattern and suggests rules for the anomaly it detects. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Adaptive Protection learns the normal pattern and proposes rules for the anomaly.
- **B:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: Adaptive Protection learns the normal pattern and proposes rules for the anomaly.
- **C:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Adaptive Protection learns the normal pattern and proposes rules for the anomaly.
- **D:** Correct. The model learns the normal request pattern and suggests rules for the anomaly it detects. In this case: Adaptive Protection learns the normal pattern and proposes rules for the anomaly.

### Question 91 — D

Answer: Apply Google Threat Intelligence lists. Threat intelligence lists match those addresses without hand-written rules. Requests from addresses on the threat lists are matched without writing rules by hand. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.
- **B:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.
- **D:** Correct. Requests from addresses on the threat lists are matched without writing rules by hand. In this case: Threat intelligence lists match those addresses without hand-written rules.

### Question 92 — B

Answer: Add a rate-based ban rule. A rate-based ban blocks a client that crosses the threshold. A client that exceeds the threshold is blocked for the ban duration. Local study-map skill 6.3 (DDoS and Rate Limiting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.
- **B:** Correct. A client that exceeds the threshold is blocked for the ban duration. In this case: A rate-based ban blocks a client that crosses the threshold.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.

### Question 93 — B, D

Answers: Create a global network firewall policy; Move the inspection to NGFW Enterprise. The global policy covers every region, and the enterprise tier adds layer 7 inspection. The policy is evaluated for the networks it is associated with, in every region. The enterprise tier adds layer 7 inspection through the managed engine. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds layer 7 inspection.
- **B:** Correct. The policy is evaluated for the networks it is associated with, in every region. In this case: The global policy covers every region, and the enterprise tier adds layer 7 inspection.
- **C:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds layer 7 inspection.
- **D:** Correct. The enterprise tier adds layer 7 inspection through the managed engine. In this case: The global policy covers every region, and the enterprise tier adds layer 7 inspection.
- **E:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds layer 7 inspection.

### Question 94 — C

Answer: Create a hierarchical firewall policy at the organisation. The organisation policy is inherited and cannot be removed by a project owner. The policy applies to every project under the organisation node. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The organisation policy is inherited and cannot be removed by a project owner.
- **B:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The organisation policy is inherited and cannot be removed by a project owner.
- **C:** Correct. The policy applies to every project under the organisation node. In this case: The organisation policy is inherited and cannot be removed by a project owner.
- **D:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The organisation policy is inherited and cannot be removed by a project owner.

### Question 95 — A

Answer: Stay on NGFW Essentials for the VPC rules. The base tier gives stateful filtering without advanced inspection. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: The base tier gives stateful filtering without advanced inspection.
- **B:** Incorrect for this question. The enterprise tier adds layer 7 inspection through the managed engine. Why the correct answer wins: The base tier gives stateful filtering without advanced inspection.
- **C:** Incorrect for this question. The standard tier adds the policy model and threat intelligence over the base rules. Why the correct answer wins: The base tier gives stateful filtering without advanced inspection.
- **D:** Incorrect for this question. The policy is evaluated for the networks it is associated with, in every region. Why the correct answer wins: The base tier gives stateful filtering without advanced inspection.

### Question 96 — A

Answer: Divide the network into micro-segmented tiers. Micro-segmentation gives each tier its own tag and permits only the required flows. Each tier carries a different tag and only the required flows are allowed between tiers. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Each tier carries a different tag and only the required flows are allowed between tiers. In this case: Micro-segmentation gives each tier its own tag and permits only the required flows.
- **B:** Incorrect for this question. The enterprise tier adds layer 7 inspection through the managed engine. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the required flows.
- **C:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the required flows.
- **D:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the required flows.

### Question 97 — C

Answer: Use secure tags as the rule target. Secure tags can only be applied by principals holding the tag role. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: Secure tags can only be applied by principals holding the tag role.
- **B:** Incorrect for this question. Tags identify the instances the rule applies to, and any holder can set one. Why the correct answer wins: Secure tags can only be applied by principals holding the tag role.
- **C:** Correct. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. In this case: Secure tags can only be applied by principals holding the tag role.
- **D:** Incorrect for this question. The rule applies to the instances that run as that identity, which only a privileged caller can change. Why the correct answer wins: Secure tags can only be applied by principals holding the tag role.

### Question 98 — B

Answer: Use dynamic port allocation. Dynamic allocation hands out ports as demand arrives. Ports are assigned from a shared pool as the demand arrives. Local study-map skill 6.6 (Cloud NAT and Port Allocation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google assigns and releases external addresses as the demand changes. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.
- **B:** Correct. Ports are assigned from a shared pool as the demand arrives. In this case: Dynamic allocation hands out ports as demand arrives.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.
- **D:** Incorrect for this question. Each VM reserves a block of ports, which gives predictable capacity and predictable consumption. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.

### Question 99 — B

Answer: Deploy Secure Web Proxy as the egress path. Secure Web Proxy applies URL policy to egress traffic. The proxy applies URL and TLS inspection policy to outbound traffic. Local study-map skill 6.7 (Secure Web Proxy), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.
- **B:** Correct. The proxy applies URL and TLS inspection policy to outbound traffic. In this case: Secure Web Proxy applies URL policy to egress traffic.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.
- **D:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.

### Question 100 — C

Answer: Inspect the traffic out of band with Packet Mirroring. Out-of-band inspection copies the traffic so the forwarding path is untouched. A copy of the traffic goes to a collector while the original flow continues untouched. Local study-map skill 6.8 (Multi-NIC Appliances and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: Out-of-band inspection copies the traffic so the forwarding path is untouched.
- **B:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Out-of-band inspection copies the traffic so the forwarding path is untouched.
- **C:** Correct. A copy of the traffic goes to a collector while the original flow continues untouched. In this case: Out-of-band inspection copies the traffic so the forwarding path is untouched.
- **D:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Out-of-band inspection copies the traffic so the forwarding path is untouched.
