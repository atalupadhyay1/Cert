# Google Cloud Professional Cloud Network Engineer — Full-Length Mock Exam 1

Professional Cloud Network Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing and Planning a Google Cloud VPC Network (VPC Design, IP Planning, and Load Balancer Choice)

### 1. Customers in eight countries use one service hosted in Belgium, and tail latency is the headline requirement. Which network tier fits?

- A. Use the Standard network service tier
- B. Use the Premium network service tier
- C. Deploy a regional external Application Load Balancer
- D. Enable Cloud CDN on the backend service

### 2. A batch API serves a single country and cost per gigabyte is the binding constraint. Which network tier fits?

- A. Use the Standard network service tier
- B. Deploy a global external Application Load Balancer
- C. Use the Premium network service tier
- D. Order a Dedicated Interconnect connection

### 3. Two regions are active, but an outage takes nine minutes to recover because only a DNS record changes. What should be added?

- A. Deploy a regional external Application Load Balancer
- B. Deploy an internal passthrough Network Load Balancer
- C. Use the Standard network service tier
- D. Deploy a global external Application Load Balancer

### 4. A zone failure must stop attracting traffic, and in-flight requests must not be reset as the shift happens. Which two settings fit? Select two.

- A. Enable session affinity on the backend service
- B. Route by URL path in the URL map
- C. Attach a health check to the backend service
- D. Register the backends as a zonal network endpoint group
- E. Enable connection draining with a timeout

### 5. On-premises servers must resolve internal names that exist only in Cloud DNS. What should be configured?

- A. Create an inbound forwarding policy with a forwarding address
- B. Create a DNS peering zone to the other project
- C. Configure a DNS forwarding policy for the on-premises domain
- D. Create a public Cloud DNS zone

### 6. Workloads in the VPC must resolve a corporate suffix that only the datacentre resolvers hold. What should be configured?

- A. Create an inbound forwarding policy with a forwarding address
- B. Enable DNSSEC on the zone
- C. Serve split-horizon answers from separate private and public zones
- D. Configure a DNS forwarding policy for the on-premises domain

### 7. A UDP telemetry service must see the client source address and must stay inside one region. Which load balancer fits?

- A. Use a proxy Network Load Balancer
- B. Route by URL path in the URL map
- C. Use a passthrough Network Load Balancer
- D. Split traffic between two backend services by weight

### 8. TLS must terminate at the front end and the backend must receive an ordinary HTTP request. Which load balancer fits?

- A. Use an external proxy Network Load Balancer with TLS termination
- B. Use the Premium network service tier
- C. Use a passthrough Network Load Balancer
- D. Deploy an internal passthrough Network Load Balancer

### 9. A planner must size the cluster before any node exists, and the node subnet is already a /24. What is required?

- A. Expand the existing subnet range
- B. Plan secondary ranges for pods and services
- C. Add a second pod range to the cluster
- D. Deploy the cluster into a shared subnet

### 10. A policy forbids any node that owns an external address. Which cluster setting fits?

- A. Add the office range to the authorised networks
- B. Use a private control plane endpoint
- C. Enable GKE Dataplane V2
- D. Use private nodes with no external addresses

### 11. A cluster's API server must not be public, and one office range must still reach it. Which two settings fit? Select two.

- A. Use a private control plane endpoint
- B. Add the office range to the authorised networks
- C. Use private nodes with no external addresses
- D. Create a GKE network policy for the namespace
- E. Use the DNS-based control plane endpoint

### 12. A new service project must be attached to the host project, and only the platform team may do it. Which role should the platform team hold?

- A. Grant Shared VPC Admin on the host project
- B. Grant the basic editor role to the automation
- C. Grant the network administrator role in the host project
- D. Grant the subnet user role on the specific shared subnets

### 13. A service team must deploy into named shared subnets, and a host-project automation must create subnets with no other rights. Which two grants fit? Select two.

- A. Grant the network administrator role in the host project
- B. Grant Shared VPC Admin on the host project
- C. Create a custom role with only the required network permissions
- D. Grant the basic editor role to the automation
- E. Grant the subnet user role on the specific shared subnets

### 14. A serverless function must reach an internal database without a dedicated connector virtual machine. What fits?

- A. Reach the API through its public interface
- B. Attach the service to Serverless VPC Access
- C. Enable Private Google Access on the subnet
- D. Create a Private Service Connect endpoint

### 15. A managed database must sit on an internal address, and a partner service must be consumed without any internet path. Which two choices fit? Select two.

- A. Attach the service to Serverless VPC Access
- B. Enable Private Google Access on the subnet
- C. Reach the API through its public interface
- D. Allocate a private services access range
- E. Create a Private Service Connect endpoint

### 16. Twelve teams need subnets from one central address plan with central firewall control. Which topology fits?

- A. Connect the VPC networks through a Network Connectivity Center hub
- B. Give each team its own standalone VPC network
- C. Build the network as a Shared VPC with host and service projects
- D. Peer every VPC network with every other VPC network

### 17. Four networks must reach each other, and peering has already proved non-transitive. Which topology fits?

- A. Peer every VPC network with every other VPC network
- B. Connect the VPC networks through a Network Connectivity Center hub
- C. Assume peered networks can reach each other transitively
- D. Create a VPC Network Peering connection between the two networks

### 18. An acquisition brought the same 10.0.0.0/8 range and the two networks must still communicate. What fits?

- A. Accept the overlapping subnet ranges as configured
- B. Use privately used public IP address ranges
- C. Use non-RFC 1918 space for the internal network
- D. Deploy Private NAT for the overlapping ranges

### 19. A greenfield network must never collide with any future acquisition's private ranges. What address strategy fits?

- A. Bring your own public IP prefixes
- B. Use non-RFC 1918 space for the internal network
- C. Automate address allocation from a central IPAM plan
- D. Use privately used public IP address ranges

### 20. Bulk copies that worked on-premises stall once they cross a VPN tunnel. What should be changed?

- A. Leave the MTU mismatch unfixed
- B. Raise the VPC MTU to 8896 bytes
- C. Lower the tunnel MTU to 1460 bytes
- D. Keep the default 1500-byte MTU

### 21. Traffic to a public partner endpoint must pass through a third-party firewall appliance. What routes it there?

- A. Add a policy-based route that matches the source and destination
- B. Create a static route with a tag-scoped next hop
- C. Deploy a multi-NIC appliance VM between the two networks
- D. Use the internal load balancer as the next hop

---

## Domain 2 — Implementing a VPC Network (VPC Implementation, Routing, and GKE Networking)

### 22. A subnet has no free addresses and its range must not be replaced. What should be done?

- A. Plan secondary ranges for pods and services
- B. Expand the existing subnet range
- C. Accept the overlapping subnet ranges as configured
- D. Add a second pod range to the cluster

### 23. Address space is exhausted and the subnet cannot be recreated, and the platform must also gain IPv6. Which two changes fit? Select two.

- A. Expand the existing subnet range
- B. Use non-RFC 1918 space for the internal network
- C. Bring your own public IP prefixes
- D. Use privately used public IP address ranges
- E. Enable dual-stack IPv6 on the subnet

### 24. A network reaches its peer but cannot reach the peer's peer. What explains that?

- A. Peer every VPC network with every other VPC network
- B. Connect the VPC networks through a Network Connectivity Center hub
- C. Create a VPC Network Peering connection between the two networks
- D. Assume peered networks can reach each other transitively

### 25. A static route created in one network must appear in the peered network. What should be enabled?

- A. Apply a CIDR range filter to the spoke
- B. Create a VPC Network Peering connection between the two networks
- C. Import and export custom routes over the peering
- D. Assume peered networks can reach each other transitively

### 26. A service project's deployment fails because it cannot use the shared subnet. What should be granted?

- A. Grant the subnet user role on the specific shared subnets
- B. Grant the network administrator role in the host project
- C. Grant Shared VPC Admin on the host project
- D. Create a custom role with only the required network permissions

### 27. One team must attach new service projects, and another must deploy into the shared subnets. Which two grants cover those jobs? Select two.

- A. Grant Shared VPC Admin on the host project
- B. Grant the network administrator role in the host project
- C. Create a custom role with only the required network permissions
- D. Grant the basic editor role to the automation
- E. Grant the subnet user role on the specific shared subnets

### 28. Instances without external addresses must still call Google APIs. What should be enabled?

- A. Create a Private Service Connect endpoint
- B. Enable Private Google Access on the subnet
- C. Reach the API through its public interface
- D. Attach the service to Serverless VPC Access

### 29. Data must not be copied to any API outside an approved set. What should be configured?

- A. Enable Private Google Access on the subnet
- B. Create a hierarchical firewall policy at the organisation
- C. Review Firewall Insights for shadowed rules
- D. Enclose the project in a VPC Service Controls perimeter

### 30. A static route to a partner and a learned route carry the same prefix, and the static one must win. What should be done?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Give the static route a lower priority number than the learned route
- C. Prefer the path with the lower multi-exit discriminator
- D. Switch best path selection back to the legacy behaviour

### 31. A route learned by the router in one region is not usable by subnets in another. What should change?

- A. Switch the Cloud Router to global dynamic routing mode
- B. Keep the Cloud Router in regional dynamic routing mode
- C. Advertise only the ranges the peer needs
- D. Prefer the path with the lower multi-exit discriminator

### 32. The peer must see two summaries instead of every subnet, and the backup link must stay the fallback. Which two settings fit? Select two.

- A. Prefer the path with the lower multi-exit discriminator
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Advertise only the ranges the peer needs
- D. Switch best path selection back to the legacy behaviour
- E. Switch the Cloud Router to global dynamic routing mode

### 33. Flows whose destination matches the internet default route must still be inspected first. What should be added?

- A. Create a static route with a tag-scoped next hop
- B. Add a policy-based route that matches the source and destination
- C. Use the internal load balancer as the next hop
- D. Give the static route a lower priority number than the learned route

### 34. Only the instances that run the legacy client must use the appliance. What should be created?

- A. Use the internal load balancer as the next hop
- B. Create a static route with a tag-scoped next hop
- C. Add a policy-based route that matches the source and destination
- D. Deploy a multi-NIC appliance VM between the two networks

### 35. Two appliances inspect the same traffic and either may fail. What should be the next hop?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Create a static route with a tag-scoped next hop
- C. Add a policy-based route that matches the source and destination
- D. Use the internal load balancer as the next hop

### 36. A VLAN attachment must join the hub. Which spoke type fits?

- A. Add the attachment as a hybrid spoke
- B. Add the VPC network as a VPC spoke
- C. Add the published service as a producer spoke
- D. Apply a CIDR range filter to the spoke

### 37. Only two of a spoke's prefixes may be shared with the hub. What should be applied?

- A. Expect spoke-to-spoke reachability through the hub
- B. Apply a CIDR range filter to the spoke
- C. Add the VPC network as a VPC spoke
- D. Add the attachment as a hybrid spoke

### 38. An existing cluster runs out of pod addresses and must not be recreated. What should be added?

- A. Plan secondary ranges for pods and services
- B. Deploy the cluster into a shared subnet
- C. Add a second pod range to the cluster
- D. Resize the service range allocation

### 39. An external partner accepts traffic only from the node addresses. What should be configured?

- A. Create a GKE network policy for the namespace
- B. Add a second pod range to the cluster
- C. Configure an IP masquerade policy on the node pool
- D. Enable GKE Dataplane V2

### 40. Pods in one namespace must not accept traffic from another namespace. What should be created?

- A. Configure an IP masquerade policy on the node pool
- B. Enable GKE Dataplane V2
- C. Create a GKE network policy for the namespace
- D. Resize the service range allocation

### 41. An audit needs byte counts and ports for connections leaving a subnet. What should be enabled?

- A. Enable Cloud NAT logging
- B. Enable Cloud DNS query logging
- C. Enable firewall rules logging
- D. Enable VPC Flow Logs on the subnet

---

## Domain 3 — Configuring Managed Network Services (Load Balancing, Cloud CDN, and Cloud DNS)

### 42. Backends must leave the pool when unhealthy, and a removed backend must not cut live requests. Which two settings fit? Select two.

- A. Enable session affinity on the backend service
- B. Register the backends as a zonal network endpoint group
- C. Enable connection draining with a timeout
- D. Switch the balancing mode to connections per instance
- E. Attach a health check to the backend service

### 43. One instance receives nearly all the traffic although the others are healthy. What should be changed?

- A. Enable session affinity on the backend service
- B. Enable connection draining with a timeout
- C. Switch the balancing mode to connections per instance
- D. Autoscale a managed instance group behind the backend service

### 44. A legacy cart keeps its state on the instance that built it. What should be enabled?

- A. Enable connection draining with a timeout
- B. Split traffic between two backend services by weight
- C. Switch the balancing mode to connections per instance
- D. Enable session affinity on the backend service

### 45. Requests under one path prefix must reach a different service from everything else. What should be configured?

- A. Route by URL path in the URL map
- B. Rewrite the request path before it reaches the backend
- C. Split traffic between two backend services by weight
- D. Mirror a copy of the traffic to a second backend

### 46. Five percent of live traffic must reach the new version on the same hostname. What should be configured?

- A. Split traffic between two backend services by weight
- B. Rewrite the request path before it reaches the backend
- C. Mirror a copy of the traffic to a second backend
- D. Route by URL path in the URL map

### 47. A Cloud Run service must sit behind the external load balancer. How should it be registered?

- A. Register the backends as a zonal network endpoint group
- B. Autoscale a managed instance group behind the backend service
- C. Register the serverless service as a serverless network endpoint group
- D. Register the third-party origins as an internet network endpoint group

### 48. Instance count must follow demand behind the load balancer. What should be configured?

- A. Switch the balancing mode to connections per instance
- B. Register the backends as a zonal network endpoint group
- C. Add the backends to a backend service behind the front end
- D. Autoscale a managed instance group behind the backend service

### 49. A team wants the load balancer created from a Kubernetes Ingress manifest. What fits?

- A. Route by URL path in the URL map
- B. Expose the workload through the GKE Ingress controller
- C. Register the backends as a zonal network endpoint group
- D. Expose the workload through the GKE Gateway controller

### 50. A platform team wants Kubernetes-native traffic splitting and header matches. What fits?

- A. Expose the workload through the GKE Ingress controller
- B. Split traffic between two backend services by weight
- C. Route by URL path in the URL map
- D. Expose the workload through the GKE Gateway controller

### 51. Static assets must be served from the edge, and a corrected file must appear as soon as it is published. Which two actions fit? Select two.

- A. Enable Cloud CDN on the backend service
- B. Invalidate the cached object after the change
- C. Serve the object through a signed URL
- D. Register the third-party origins as an internet network endpoint group
- E. Raise the cache time to live

### 52. An object must be readable only through a link that expires in fifteen minutes. What should be used?

- A. Invalidate the cached object after the change
- B. Serve the object through a signed URL
- C. Enable Cloud CDN on the backend service
- D. Raise the cache time to live

### 53. A private name must resolve from two projects and must never answer on the internet. Which two settings fit? Select two.

- A. Create a private Cloud DNS zone
- B. Migrate the zone with a staged import and a delegated test
- C. Create a DNS peering zone to the other project
- D. Enable DNSSEC on the zone
- E. Create a public Cloud DNS zone

### 54. A record change must reach resolvers quickly when the cutover happens. What should be done beforehand?

- A. Create a private Cloud DNS zone
- B. Enable DNSSEC on the zone
- C. Migrate the zone with a staged import and a delegated test
- D. Lower the record TTL before the cutover

### 55. Each continent must be answered with its own regional address. Which policy fits?

- A. Apply a geolocation routing policy to the record set
- B. Migrate the zone with a staged import and a delegated test
- C. Lower the record TTL before the cutover
- D. Apply a failover routing policy with a health-checked primary

### 56. A standby address must answer only while the primary is unhealthy. Which policy fits?

- A. Apply a geolocation routing policy to the record set
- B. Apply a failover routing policy with a health-checked primary
- C. Migrate the zone with a staged import and a delegated test
- D. Enable DNSSEC on the zone

### 57. An auditor must be able to prove that answers were not altered in transit. What should be enabled?

- A. Create a private Cloud DNS zone
- B. Enable DNSSEC on the zone
- C. Serve split-horizon answers from separate private and public zones
- D. Enable Cloud DNS query logging

---

## Domain 4 — Configuring and Implementing Hybrid and Multicloud Interconnectivity (Interconnect, VPN, and Cloud Router)

### 58. A Dedicated Interconnect circuit is delivered and the on-premises router must peer over it. Which two items are required? Select two.

- A. Create a VLAN attachment on Cloud Router
- B. Order a Partner Interconnect connection
- C. Order a Cross-Cloud Interconnect connection
- D. Set the Cloud Router ASN to a private value that differs from the peer
- E. Enable MACsec on the interconnect

### 59. A private circuit must terminate in a Google colocation facility the company already uses. Which connection fits?

- A. Order a Partner Interconnect connection
- B. Order a Cross-Cloud Interconnect connection
- C. Deploy an HA VPN gateway with two interfaces
- D. Order a Dedicated Interconnect connection

### 60. The circuit exists but no traffic crosses it, and no BGP session is up. What is missing on the router?

- A. Deploy an HA VPN gateway with two interfaces
- B. Create a VLAN attachment on Cloud Router
- C. Add the VPC network as a VPC spoke
- D. Create a VPC Network Peering connection between the two networks

### 61. The nearest Google colocation is nine hundred kilometres away and one provider location must serve the site. Which connection fits?

- A. Order a Partner Interconnect connection
- B. Order a Cross-Cloud Interconnect connection
- C. Order a Dedicated Interconnect connection
- D. Deploy an HA VPN gateway with two interfaces

### 62. Workloads must reach a second cloud over a dedicated circuit rather than the internet. Which connection fits?

- A. Order a Dedicated Interconnect connection
- B. Deploy an HA VPN gateway with two interfaces
- C. Order a Cross-Cloud Interconnect connection
- D. Order a Partner Interconnect connection

### 63. A site needs tunnel redundancy across zones and bulk transfers that fit the tunnel. Which two settings fit? Select two.

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Deploy a Classic VPN with a single tunnel
- C. Lower the tunnel MTU to 1460 bytes
- D. Order a Dedicated Interconnect connection
- E. Deploy an HA VPN gateway with two interfaces

### 64. Two VPCs in different projects must exchange traffic privately without leaving the Google network. What fits?

- A. Create a VLAN attachment on Cloud Router
- B. Order a Dedicated Interconnect connection
- C. Deploy a Classic VPN with a single tunnel
- D. Deploy an HA VPN gateway with two interfaces

### 65. A single tunnel carries the site and disappears whenever the device reboots. What explains the outage?

- A. Order a Dedicated Interconnect connection
- B. Deploy an HA VPN gateway with two interfaces
- C. Deploy a Classic VPN with a single tunnel
- D. Create a VLAN attachment on Cloud Router

### 66. An old appliance supports only policy-based selection and no dynamic routing. Which VPN fits?

- A. Deploy a Classic VPN with a single tunnel
- B. Deploy an HA VPN gateway with two interfaces
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Create a VLAN attachment on Cloud Router

### 67. The BGP session never reaches established and both ends report ASN 65001. What should change?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Switch best path selection back to the legacy behaviour
- C. Prefer the path with the lower multi-exit discriminator
- D. Enable Bidirectional Forwarding Detection with a short interval

### 68. The same prefix arrives over two attachments and the backup is the path in use. What should be set?

- A. Give the static route a lower priority number than the learned route
- B. Prefer the path with the lower multi-exit discriminator
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Switch best path selection back to the legacy behaviour

### 69. The peer must receive two summaries rather than every subnet, and those summaries must be usable in all regions. Which two settings fit? Select two.

- A. Advertise only the ranges the peer needs
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Prefer the path with the lower multi-exit discriminator
- D. Set the Cloud Router ASN to a private value that differs from the peer
- E. Switch the Cloud Router to global dynamic routing mode

### 70. A dead path keeps attracting traffic for three minutes until the hold timer expires. What should be enabled?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Prefer the path with the lower multi-exit discriminator
- D. Switch best path selection back to the legacy behaviour

### 71. The same prefix exists as an imported route and as a local route, and the wrong one wins. What should be changed?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Prefer the path with the lower multi-exit discriminator
- C. Give the static route a lower priority number than the learned route
- D. Switch best path selection back to the legacy behaviour

### 72. After an upgrade the preferred path changed although the advertisements did not. What explains it?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Give the static route a lower priority number than the learned route
- C. Switch best path selection back to the legacy behaviour
- D. Prefer the path with the lower multi-exit discriminator

### 73. A regulator requires link encryption on the circuit and the equipment supports it. What should be enabled?

- A. Run HA VPN over Cloud Interconnect instead of MACsec
- B. Deploy an HA VPN gateway with two interfaces
- C. Enable MACsec on the interconnect
- D. Create a VLAN attachment on Cloud Router

---

## Domain 5 — Managing, Monitoring, and Troubleshooting Network Operations (Observability, Troubleshooting, and Traffic Movement)

### 74. A connection is refused and nobody knows which rule decided. What should be enabled?

- A. Enable firewall rules logging
- B. Enable Cloud DNS query logging
- C. Enable Cloud NAT logging
- D. Enable VPC Flow Logs on the subnet

### 75. A partner needs the translated address and port for a given flow. What should be enabled?

- A. Enable firewall rules logging
- B. Enable Cloud DNS query logging
- C. Enable VPC Flow Logs on the subnet
- D. Enable Cloud NAT logging

### 76. A tunnel must page the on-call when it leaves established. What should be created?

- A. Create a log-based metric from the firewall log entries
- B. Alert on the error budget of the service objective
- C. Create an alert policy on the network metric
- D. Publish a custom metric from the appliance

### 77. Denied connections must be counted even though no metric exists for them. What should be created?

- A. Create an alert policy on the network metric
- B. Create a log-based metric from the firewall log entries
- C. Alert on the error budget of the service objective
- D. Publish a custom metric from the appliance

### 78. A single connection fails and the route and firewall must be evaluated together. What should be run?

- A. Run a Connectivity Test between the two endpoints
- B. Check the Performance Dashboard for packet loss
- C. Inspect the flow in Network Topology
- D. Query Flow Analyzer for the top talkers

### 79. Two engineers disagree about whether a rule blocks the flow. Which two tools settle it? Select two.

- A. Enable firewall rules logging
- B. Inspect the flow in Network Topology
- C. Query Flow Analyzer for the top talkers
- D. Enable Cloud DNS query logging
- E. Run a Connectivity Test between the two endpoints

### 80. Users report loss and it is unclear whether it happens inside or outside the Google network. What should be checked?

- A. Test the path with a large ping and the do-not-fragment bit
- B. Check the Performance Dashboard for packet loss
- C. Inspect the flow in Network Topology
- D. Query Flow Analyzer for the top talkers

### 81. Large transfers stall while small requests succeed along a new path. What should be done first?

- A. Check the Performance Dashboard for packet loss
- B. Inspect the flow in Network Topology
- C. Leave the MTU mismatch unfixed
- D. Test the path with a large ping and the do-not-fragment bit

### 82. A rule was added but the traffic it should allow is still denied. What should be reviewed?

- A. Review Firewall Insights for shadowed rules
- B. Read the Network Analyzer findings
- C. Query Flow Analyzer for the top talkers
- D. Run a Connectivity Test between the two endpoints

### 83. A review must find rules that never match and configurations that risk an outage. Which two tools fit? Select two.

- A. Read the Network Analyzer findings
- B. Check the Performance Dashboard for packet loss
- C. Query Flow Analyzer for the top talkers
- D. Review Firewall Insights for shadowed rules
- E. Run a Connectivity Test between the two endpoints

### 84. Nobody can describe the path between two regions today. What should be inspected?

- A. Inspect the flow in Network Topology
- B. Query Flow Analyzer for the top talkers
- C. Run a Connectivity Test between the two endpoints
- D. Check the Performance Dashboard for packet loss

### 85. A link is saturated and the consumers must be identified. What should be queried?

- A. Check the Performance Dashboard for packet loss
- B. Inspect the flow in Network Topology
- C. Query Flow Analyzer for the top talkers
- D. Review Firewall Insights for shadowed rules

### 86. A session is established on one peer and idle on the other. What should be done?

- A. Run a Connectivity Test between the two endpoints
- B. Compare the BGP session state on both peers
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Prefer the path with the lower multi-exit discriminator

### 87. A region is being retired and live connections must not be reset. What should be done?

- A. Inspect the flow in Network Topology
- B. Enable connection draining with a timeout
- C. Drain the backend before removing it
- D. Query Flow Analyzer for the top talkers

---

## Domain 6 — Configuring, Implementing, and Managing a Cloud Network Security Solution (Cloud Armor, Cloud NGFW, NAT, and Egress Security)

### 88. Requests that reach a backend service must be filtered by geography before the application sees them. What fits?

- A. Attach a Cloud Armor edge security policy
- B. Add a rate-based ban rule
- C. Add a preconfigured WAF rule for the attack class
- D. Attach a Cloud Armor backend security policy

### 89. Blocked source ranges must be refused before the proxy forwards anything. What fits?

- A. Enable bot management on the policy
- B. Attach a Cloud Armor backend security policy
- C. Attach a Cloud Armor edge security policy
- D. Add a preconfigured WAF rule for the attack class

### 90. The application is being probed with encoded injection payloads. What should be added?

- A. Enable bot management on the policy
- B. Enable Adaptive Protection
- C. Add a preconfigured WAF rule for the attack class
- D. Apply Google Threat Intelligence lists

### 91. Scrapers are inflating costs but some automated clients are legitimate. What fits?

- A. Enable Adaptive Protection
- B. Add a preconfigured WAF rule for the attack class
- C. Enable bot management on the policy
- D. Apply Google Threat Intelligence lists

### 92. A volumetric flood and an application-level flood arrive together. What combination fits?

- A. Apply Google Threat Intelligence lists
- B. Add a rate-based ban rule
- C. Enable Adaptive Protection
- D. Rely on the default DDoS protection and add a rate limit

### 93. A rule must apply to every project, and only a privileged principal may change which workloads it targets. Which two fit? Select two.

- A. Create a VPC firewall rule with a target tag
- B. Reorder the rules by priority
- C. Create a hierarchical firewall policy at the organisation
- D. Create a regional network firewall policy
- E. Use secure tags as the rule target

### 94. Traffic must be inspected at layer 7 through a managed engine. Which tier fits?

- A. Stay on NGFW Essentials for the VPC rules
- B. Move the rules to NGFW Standard
- C. Move the inspection to NGFW Enterprise
- D. Create a global network firewall policy

### 95. A policy must apply only in one region of one network. What fits?

- A. Create a VPC firewall rule with a target tag
- B. Create a hierarchical firewall policy at the organisation
- C. Create a global network firewall policy
- D. Create a regional network firewall policy

### 96. Instances may currently reach any internet destination and that must stop except for named hosts. What should be created?

- A. Add a deny-all egress rule with a higher priority
- B. Leave the default allow-ingress rule in place
- C. Move the rules to NGFW Standard
- D. Reorder the rules by priority

### 97. Which workloads a rule applies to must resist an ordinary instance owner changing it. What should target the rule?

- A. Target the rule with network tags
- B. Target the rule with a service account
- C. Reorder the rules by priority
- D. Create a hierarchical firewall policy at the organisation

### 98. A partner allowlists one source address. What should Cloud NAT use?

- A. Assign a manual static Cloud NAT address
- B. Use dynamic port allocation
- C. Use automatic Cloud NAT IP allocation
- D. Deploy Secure Web Proxy as the egress path

### 99. Outbound traffic must be filtered by URL and inspected for TLS. What fits?

- A. Use dynamic port allocation
- B. Configure Packet Mirroring on the instance group
- C. Assign a manual static Cloud NAT address
- D. Deploy Secure Web Proxy as the egress path

### 100. A security team wants a copy of selected traffic without changing the forwarding path. What fits?

- A. Inspect the traffic out of band with Packet Mirroring
- B. Deploy Secure Web Proxy as the egress path
- C. Deploy a multi-NIC appliance VM between the two networks
- D. Configure Packet Mirroring on the instance group

---

## Answer key and explanations

### Question 1 — B

Answer: Use the Premium network service tier. The premium tier carries traffic on the Google network from the nearest edge, which is what the latency target needs. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: The premium tier carries traffic on the Google network from the nearest edge, which is what the latency target needs.
- **B:** Correct. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. In this case: The premium tier carries traffic on the Google network from the nearest edge, which is what the latency target needs.
- **C:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: The premium tier carries traffic on the Google network from the nearest edge, which is what the latency target needs.
- **D:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: The premium tier carries traffic on the Google network from the nearest edge, which is what the latency target needs.

### Question 2 — A

Answer: Use the Standard network service tier. Standard tiering keeps long-haul traffic on the public internet, which is the cheaper path for that traffic. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. In this case: Standard tiering keeps long-haul traffic on the public internet, which is the cheaper path for that traffic.
- **B:** Incorrect for this question. A global anycast address routes each user to the closest healthy region. Why the correct answer wins: Standard tiering keeps long-haul traffic on the public internet, which is the cheaper path for that traffic.
- **C:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: Standard tiering keeps long-haul traffic on the public internet, which is the cheaper path for that traffic.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Standard tiering keeps long-haul traffic on the public internet, which is the cheaper path for that traffic.

### Question 3 — D

Answer: Deploy a global external Application Load Balancer. A global anycast front end moves users to the surviving region without waiting for DNS to expire. A global anycast address routes each user to the closest healthy region. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: A global anycast front end moves users to the surviving region without waiting for DNS to expire.
- **B:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: A global anycast front end moves users to the surviving region without waiting for DNS to expire.
- **C:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: A global anycast front end moves users to the surviving region without waiting for DNS to expire.
- **D:** Correct. A global anycast address routes each user to the closest healthy region. In this case: A global anycast front end moves users to the surviving region without waiting for DNS to expire.

### Question 4 — C, E

Answers: Attach a health check to the backend service; Enable connection draining with a timeout. The health check removes the failed backends, and draining lets their live requests finish first. The check removes a backend that cannot answer, so traffic moves to a healthy one. Removing a backend waits for in-flight requests to finish before the backend is detached. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: The health check removes the failed backends, and draining lets their live requests finish first.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The health check removes the failed backends, and draining lets their live requests finish first.
- **C:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The health check removes the failed backends, and draining lets their live requests finish first.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The health check removes the failed backends, and draining lets their live requests finish first.
- **E:** Correct. Removing a backend waits for in-flight requests to finish before the backend is detached. In this case: The health check removes the failed backends, and draining lets their live requests finish first.

### Question 5 — A

Answer: Create an inbound forwarding policy with a forwarding address. An inbound forwarding policy gives the on-premises resolvers an address they can query. On-premises resolvers send queries to that address to reach Cloud DNS names. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. On-premises resolvers send queries to that address to reach Cloud DNS names. In this case: An inbound forwarding policy gives the on-premises resolvers an address they can query.
- **B:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: An inbound forwarding policy gives the on-premises resolvers an address they can query.
- **C:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: An inbound forwarding policy gives the on-premises resolvers an address they can query.
- **D:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: An inbound forwarding policy gives the on-premises resolvers an address they can query.

### Question 6 — D

Answer: Configure a DNS forwarding policy for the on-premises domain. A forwarding policy sends queries for that suffix to the datacentre resolvers. Queries for the corporate suffix are forwarded to the on-premises resolvers. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. On-premises resolvers send queries to that address to reach Cloud DNS names. Why the correct answer wins: A forwarding policy sends queries for that suffix to the datacentre resolvers.
- **B:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A forwarding policy sends queries for that suffix to the datacentre resolvers.
- **C:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: A forwarding policy sends queries for that suffix to the datacentre resolvers.
- **D:** Correct. Queries for the corporate suffix are forwarded to the on-premises resolvers. In this case: A forwarding policy sends queries for that suffix to the datacentre resolvers.

### Question 7 — C

Answer: Use a passthrough Network Load Balancer. A passthrough load balancer forwards the original packet, so the backend keeps the client address. Packets keep their client source address and the backend sees the original flow. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates the client connection and opens a separate one to the backend. Why the correct answer wins: A passthrough load balancer forwards the original packet, so the backend keeps the client address.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: A passthrough load balancer forwards the original packet, so the backend keeps the client address.
- **C:** Correct. Packets keep their client source address and the backend sees the original flow. In this case: A passthrough load balancer forwards the original packet, so the backend keeps the client address.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: A passthrough load balancer forwards the original packet, so the backend keeps the client address.

### Question 8 — A

Answer: Use an external proxy Network Load Balancer with TLS termination. The proxy terminates TLS and opens a separate connection to the backend. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: The proxy terminates TLS and opens a separate connection to the backend.
- **B:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: The proxy terminates TLS and opens a separate connection to the backend.
- **C:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: The proxy terminates TLS and opens a separate connection to the backend.
- **D:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: The proxy terminates TLS and opens a separate connection to the backend.

### Question 9 — B

Answer: Plan secondary ranges for pods and services. Secondary ranges give pods and services their own address space beside the node subnet. Alias ranges give pods and services addresses that are separate from the node subnet. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A subnet prefix can grow within its address range, and the growth cannot shrink later. Why the correct answer wins: Secondary ranges give pods and services their own address space beside the node subnet.
- **B:** Correct. Alias ranges give pods and services addresses that are separate from the node subnet. In this case: Secondary ranges give pods and services their own address space beside the node subnet.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Secondary ranges give pods and services their own address space beside the node subnet.
- **D:** Incorrect for this question. The cluster consumes subnets that the host project owns. Why the correct answer wins: Secondary ranges give pods and services their own address space beside the node subnet.

### Question 10 — D

Answer: Use private nodes with no external addresses. Private nodes reach the control plane and Google APIs through internal paths only. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: Private nodes reach the control plane and Google APIs through internal paths only.
- **B:** Incorrect for this question. The API server is reachable only through the internal address or an authorised network. Why the correct answer wins: Private nodes reach the control plane and Google APIs through internal paths only.
- **C:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Private nodes reach the control plane and Google APIs through internal paths only.
- **D:** Correct. In this case: Private nodes reach the control plane and Google APIs through internal paths only.

### Question 11 — A, B

Answers: Use a private control plane endpoint; Add the office range to the authorised networks. The private endpoint removes the public address, and the authorised network admits that one range. The API server is reachable only through the internal address or an authorised network. The named range may reach the control plane endpoint even when it is public. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The API server is reachable only through the internal address or an authorised network. In this case: The private endpoint removes the public address, and the authorised network admits that one range.
- **B:** Correct. The named range may reach the control plane endpoint even when it is public. In this case: The private endpoint removes the public address, and the authorised network admits that one range.
- **C:** Incorrect for this question. Nodes reach the control plane and Google APIs through internal paths only. Why the correct answer wins: The private endpoint removes the public address, and the authorised network admits that one range.
- **D:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The private endpoint removes the public address, and the authorised network admits that one range.
- **E:** Incorrect for this question. The endpoint resolves through a private DNS name instead of a fixed address. Why the correct answer wins: The private endpoint removes the public address, and the authorised network admits that one range.

### Question 12 — A

Answer: Grant Shared VPC Admin on the host project. Shared VPC Admin attaches service projects and delegates subnet use. That role attaches service projects and delegates subnet use. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC Admin attaches service projects and delegates subnet use.
- **B:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Shared VPC Admin attaches service projects and delegates subnet use.
- **C:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC Admin attaches service projects and delegates subnet use.
- **D:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: Shared VPC Admin attaches service projects and delegates subnet use.

### Question 13 — C, E

Answers: Grant the subnet user role on the specific shared subnets; Create a custom role with only the required network permissions. Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission. The role lets a service project deploy into the named subnets and nothing else. The custom role names the exact permissions the automation needs. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission.
- **B:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission.
- **C:** Correct. The custom role names the exact permissions the automation needs. In this case: Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission.
- **D:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission.
- **E:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Subnet user allows use of the named subnets, and the custom role names only the subnet creation permission.

### Question 14 — B

Answer: Attach the service to Serverless VPC Access. Serverless VPC Access gives the function a path into the VPC. A serverless runtime gets a path into the VPC through a connector or direct egress. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Serverless VPC Access gives the function a path into the VPC.
- **B:** Correct. A serverless runtime gets a path into the VPC through a connector or direct egress. In this case: Serverless VPC Access gives the function a path into the VPC.
- **C:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: Serverless VPC Access gives the function a path into the VPC.
- **D:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Serverless VPC Access gives the function a path into the VPC.

### Question 15 — D, E

Answers: Allocate a private services access range; Create a Private Service Connect endpoint. A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment. A reserved internal range lets a managed service provider peer into the VPC. A private endpoint inside the consumer VPC targets a published service attachment. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment.
- **B:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment.
- **C:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment.
- **D:** Correct. A reserved internal range lets a managed service provider peer into the VPC. In this case: A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment.
- **E:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: A reserved private services range places the database internally, and a private endpoint reaches the partner service attachment.

### Question 16 — C

Answer: Build the network as a Shared VPC with host and service projects. A Shared VPC keeps the network in the host project while service projects deploy into its subnets. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: A Shared VPC keeps the network in the host project while service projects deploy into its subnets.
- **B:** Incorrect for this question. Separate projects own separate networks, and nothing is shared implicitly. Why the correct answer wins: A Shared VPC keeps the network in the host project while service projects deploy into its subnets.
- **C:** Correct. In this case: A Shared VPC keeps the network in the host project while service projects deploy into its subnets.
- **D:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: A Shared VPC keeps the network in the host project while service projects deploy into its subnets.

### Question 17 — B

Answer: Connect the VPC networks through a Network Connectivity Center hub. A hub forwards between its spokes, which peering cannot do. A hub groups spokes so the connected networks reach each other through one managed topology. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: A hub forwards between its spokes, which peering cannot do.
- **B:** Correct. A hub groups spokes so the connected networks reach each other through one managed topology. In this case: A hub forwards between its spokes, which peering cannot do.
- **C:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: A hub forwards between its spokes, which peering cannot do.
- **D:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: A hub forwards between its spokes, which peering cannot do.

### Question 18 — D

Answer: Deploy Private NAT for the overlapping ranges. Private NAT translates the source addresses so the overlapping ranges can talk. Source addresses are translated so two networks with the same private ranges can still talk. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Private NAT translates the source addresses so the overlapping ranges can talk.
- **B:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Private NAT translates the source addresses so the overlapping ranges can talk.
- **C:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Private NAT translates the source addresses so the overlapping ranges can talk.
- **D:** Correct. Source addresses are translated so two networks with the same private ranges can still talk. In this case: Private NAT translates the source addresses so the overlapping ranges can talk.

### Question 19 — B

Answer: Use non-RFC 1918 space for the internal network. Space outside the private ranges avoids colliding with any future private network. The internal network uses address space outside the private ranges to avoid collisions later. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Space outside the private ranges avoids colliding with any future private network.
- **B:** Correct. The internal network uses address space outside the private ranges to avoid collisions later. In this case: Space outside the private ranges avoids colliding with any future private network.
- **C:** Incorrect for this question. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Why the correct answer wins: Space outside the private ranges avoids colliding with any future private network.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Space outside the private ranges avoids colliding with any future private network.

### Question 20 — C

Answer: Lower the tunnel MTU to 1460 bytes. Tunnel headers consume payload, so the path MTU must drop to fit inside the tunnel. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Local study-map skill 1.10 (MTU Sizing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: Tunnel headers consume payload, so the path MTU must drop to fit inside the tunnel.
- **B:** Incorrect for this question. A larger maximum transmission unit carries more payload per packet inside the VPC. Why the correct answer wins: Tunnel headers consume payload, so the path MTU must drop to fit inside the tunnel.
- **C:** Correct. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. In this case: Tunnel headers consume payload, so the path MTU must drop to fit inside the tunnel.
- **D:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: Tunnel headers consume payload, so the path MTU must drop to fit inside the tunnel.

### Question 21 — A

Answer: Add a policy-based route that matches the source and destination. A policy-based route forwards the matching flow to the appliance by address and port. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 1.11 (Third-Party Appliance Insertion), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route forwards the matching flow to the appliance by address and port.
- **B:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route forwards the matching flow to the appliance by address and port.
- **C:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A policy-based route forwards the matching flow to the appliance by address and port.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route forwards the matching flow to the appliance by address and port.

### Question 22 — B

Answer: Expand the existing subnet range. A subnet prefix can grow within its range, which adds addresses without a rebuild. A subnet prefix can grow within its address range, and the growth cannot shrink later. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: A subnet prefix can grow within its range, which adds addresses without a rebuild.
- **B:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: A subnet prefix can grow within its range, which adds addresses without a rebuild.
- **C:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: A subnet prefix can grow within its range, which adds addresses without a rebuild.
- **D:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: A subnet prefix can grow within its range, which adds addresses without a rebuild.

### Question 23 — A, E

Answers: Expand the existing subnet range; Enable dual-stack IPv6 on the subnet. Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them. A subnet prefix can grow within its address range, and the growth cannot shrink later. The subnet carries both an IPv4 range and an internal or external IPv6 range. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them.
- **B:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them.
- **C:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them.
- **E:** Correct. The subnet carries both an IPv4 range and an internal or external IPv6 range. In this case: Growing the prefix adds IPv4 addresses in place, and dual-stack adds an IPv6 range beside them.

### Question 24 — D

Answer: Assume peered networks can reach each other transitively. Peering does not pass routes on, so a third network is not reached through the second. Peering is not transitive, so a route learned through one peer is not passed on to another. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering does not pass routes on, so a third network is not reached through the second.
- **B:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering does not pass routes on, so a third network is not reached through the second.
- **C:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Peering does not pass routes on, so a third network is not reached through the second.
- **D:** Correct. Peering is not transitive, so a route learned through one peer is not passed on to another. In this case: Peering does not pass routes on, so a third network is not reached through the second.

### Question 25 — C

Answer: Import and export custom routes over the peering. Import and export of custom routes carries those static routes across the peering. The peering option carries static and policy-based routes between the two networks. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: Import and export of custom routes carries those static routes across the peering.
- **B:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Import and export of custom routes carries those static routes across the peering.
- **C:** Correct. The peering option carries static and policy-based routes between the two networks. In this case: Import and export of custom routes carries those static routes across the peering.
- **D:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: Import and export of custom routes carries those static routes across the peering.

### Question 26 — A

Answer: Grant the subnet user role on the specific shared subnets. Subnet user on that subnet lets the service project deploy into it. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Subnet user on that subnet lets the service project deploy into it.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Subnet user on that subnet lets the service project deploy into it.
- **C:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: Subnet user on that subnet lets the service project deploy into it.
- **D:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: Subnet user on that subnet lets the service project deploy into it.

### Question 27 — A, E

Answers: Grant Shared VPC Admin on the host project; Grant the subnet user role on the specific shared subnets. Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them. That role attaches service projects and delegates subnet use. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them.
- **D:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them.
- **E:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Shared VPC Admin attaches the projects, and subnet user lets the second team deploy into them.

### Question 28 — B

Answer: Enable Private Google Access on the subnet. Private Google Access routes those calls internally without an external address. Instances without external addresses reach Google APIs through internal routing. Local study-map skill 2.4 (Private Google Access and APIs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Private Google Access routes those calls internally without an external address.
- **B:** Correct. Instances without external addresses reach Google APIs through internal routing. In this case: Private Google Access routes those calls internally without an external address.
- **C:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Private Google Access routes those calls internally without an external address.
- **D:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Private Google Access routes those calls internally without an external address.

### Question 29 — D

Answer: Enclose the project in a VPC Service Controls perimeter. A service perimeter restricts which services the project may call and where data may flow. The perimeter restricts which services the project may call and blocks data movement outside it. Local study-map skill 2.5 (VPC Service Controls Perimeters), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A service perimeter restricts which services the project may call and where data may flow.
- **B:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A service perimeter restricts which services the project may call and where data may flow.
- **C:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: A service perimeter restricts which services the project may call and where data may flow.
- **D:** Correct. The perimeter restricts which services the project may call and blocks data movement outside it. In this case: A service perimeter restricts which services the project may call and where data may flow.

### Question 30 — B

Answer: Give the static route a lower priority number than the learned route. A lower priority number makes the static route preferable to the learned one. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A lower priority number makes the static route preferable to the learned one.
- **B:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: A lower priority number makes the static route preferable to the learned one.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: A lower priority number makes the static route preferable to the learned one.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: A lower priority number makes the static route preferable to the learned one.

### Question 31 — A

Answer: Switch the Cloud Router to global dynamic routing mode. Global dynamic routing mode makes learned routes available in every region. Routes learned in one region are available to subnets in every region. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global dynamic routing mode makes learned routes available in every region.
- **B:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global dynamic routing mode makes learned routes available in every region.
- **C:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: Global dynamic routing mode makes learned routes available in every region.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global dynamic routing mode makes learned routes available in every region.

### Question 32 — A, C

Answers: Advertise only the ranges the peer needs; Prefer the path with the lower multi-exit discriminator. Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback. The router advertises a chosen prefix list instead of every subnet in the VPC. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback.
- **C:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback.
- **E:** Incorrect for this question. Routes learned in one region are available to subnets in every region. Why the correct answer wins: Advertising a chosen prefix list hides the rest, and the higher discriminator keeps that link as the fallback.

### Question 33 — B

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches those flows and forwards them to the appliance. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches those flows and forwards them to the appliance.
- **B:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches those flows and forwards them to the appliance.
- **C:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches those flows and forwards them to the appliance.
- **D:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A policy-based route matches those flows and forwards them to the appliance.

### Question 34 — B

Answer: Create a static route with a tag-scoped next hop. A tag-scoped static route sends only the tagged instances through the appliance. Only instances carrying the tag send their traffic through the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A tag-scoped static route sends only the tagged instances through the appliance.
- **B:** Correct. Only instances carrying the tag send their traffic through the appliance. In this case: A tag-scoped static route sends only the tagged instances through the appliance.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: A tag-scoped static route sends only the tagged instances through the appliance.
- **D:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A tag-scoped static route sends only the tagged instances through the appliance.

### Question 35 — D

Answer: Use the internal load balancer as the next hop. The internal load balancer selects a live appliance, so a failure needs no route change. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 2.8 (Internal Load Balancer as Next Hop), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer selects a live appliance, so a failure needs no route change.
- **B:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer selects a live appliance, so a failure needs no route change.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer selects a live appliance, so a failure needs no route change.
- **D:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer selects a live appliance, so a failure needs no route change.

### Question 36 — A

Answer: Add the attachment as a hybrid spoke. A hybrid spoke carries the attachment into the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A hybrid spoke carries the attachment into the hub.
- **B:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A hybrid spoke carries the attachment into the hub.
- **C:** Incorrect for this question. The spoke publishes a service attachment so consumers reach it through the hub. Why the correct answer wins: A hybrid spoke carries the attachment into the hub.
- **D:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: A hybrid spoke carries the attachment into the hub.

### Question 37 — B

Answer: Apply a CIDR range filter to the spoke. A CIDR filter limits which prefixes the spoke exchanges. Only the matching prefixes are exchanged with the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The hub forwards between spokes, which peering alone cannot do. Why the correct answer wins: A CIDR filter limits which prefixes the spoke exchanges.
- **B:** Correct. Only the matching prefixes are exchanged with the hub. In this case: A CIDR filter limits which prefixes the spoke exchanges.
- **C:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A CIDR filter limits which prefixes the spoke exchanges.
- **D:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: A CIDR filter limits which prefixes the spoke exchanges.

### Question 38 — C

Answer: Add a second pod range to the cluster. An additional pod range gives the cluster more alias addresses in place. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: An additional pod range gives the cluster more alias addresses in place.
- **B:** Incorrect for this question. The cluster consumes subnets that the host project owns. Why the correct answer wins: An additional pod range gives the cluster more alias addresses in place.
- **C:** Correct. In this case: An additional pod range gives the cluster more alias addresses in place.
- **D:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: An additional pod range gives the cluster more alias addresses in place.

### Question 39 — C

Answer: Configure an IP masquerade policy on the node pool. The masquerade policy translates pod traffic to the node address for those destinations. Outbound pod traffic is translated to the node address under the chosen conditions. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The masquerade policy translates pod traffic to the node address for those destinations.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The masquerade policy translates pod traffic to the node address for those destinations.
- **C:** Correct. Outbound pod traffic is translated to the node address under the chosen conditions. In this case: The masquerade policy translates pod traffic to the node address for those destinations.
- **D:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: The masquerade policy translates pod traffic to the node address for those destinations.

### Question 40 — C

Answer: Create a GKE network policy for the namespace. A network policy restricts which pods may reach the selected pods. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **C:** Correct. In this case: A network policy restricts which pods may reach the selected pods.
- **D:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.

### Question 41 — D

Answer: Enable VPC Flow Logs on the subnet. Flow logs record the sampled connection details for the subnet. The logs record sampled connections with source, destination, port and byte counts. Local study-map skill 2.11 (VPC Flow Logs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Flow logs record the sampled connection details for the subnet.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Flow logs record the sampled connection details for the subnet.
- **C:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: Flow logs record the sampled connection details for the subnet.
- **D:** Correct. The logs record sampled connections with source, destination, port and byte counts. In this case: Flow logs record the sampled connection details for the subnet.

### Question 42 — C, E

Answers: Attach a health check to the backend service; Enable connection draining with a timeout. The health check removes the failing backend, and draining lets its live requests finish. The check removes a backend that cannot answer, so traffic moves to a healthy one. Removing a backend waits for in-flight requests to finish before the backend is detached. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: The health check removes the failing backend, and draining lets its live requests finish.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The health check removes the failing backend, and draining lets its live requests finish.
- **C:** Correct. Removing a backend waits for in-flight requests to finish before the backend is detached. In this case: The health check removes the failing backend, and draining lets its live requests finish.
- **D:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: The health check removes the failing backend, and draining lets its live requests finish.
- **E:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The health check removes the failing backend, and draining lets its live requests finish.

### Question 43 — C

Answer: Switch the balancing mode to connections per instance. Balancing by connection count spreads load instead of following CPU utilisation. The mode spreads load by connection count rather than by CPU utilisation. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: Balancing by connection count spreads load instead of following CPU utilisation.
- **B:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Balancing by connection count spreads load instead of following CPU utilisation.
- **C:** Correct. The mode spreads load by connection count rather than by CPU utilisation. In this case: Balancing by connection count spreads load instead of following CPU utilisation.
- **D:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: Balancing by connection count spreads load instead of following CPU utilisation.

### Question 44 — D

Answer: Enable session affinity on the backend service. Affinity keeps the client on the instance that holds its cart. Affinity keeps a client on the backend that already holds its session state. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Affinity keeps the client on the instance that holds its cart.
- **B:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Affinity keeps the client on the instance that holds its cart.
- **C:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: Affinity keeps the client on the instance that holds its cart.
- **D:** Correct. Affinity keeps a client on the backend that already holds its session state. In this case: Affinity keeps the client on the instance that holds its cart.

### Question 45 — A

Answer: Route by URL path in the URL map. The URL map selects the backend service from the request host and path. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: The URL map selects the backend service from the request host and path.
- **B:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: The URL map selects the backend service from the request host and path.
- **C:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The URL map selects the backend service from the request host and path.
- **D:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: The URL map selects the backend service from the request host and path.

### Question 46 — A

Answer: Split traffic between two backend services by weight. Weighted backends move that share of traffic onto the new version. Weighted backends move a chosen share of traffic onto the new service. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Weighted backends move a chosen share of traffic onto the new service. In this case: Weighted backends move that share of traffic onto the new version.
- **B:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: Weighted backends move that share of traffic onto the new version.
- **C:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: Weighted backends move that share of traffic onto the new version.
- **D:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Weighted backends move that share of traffic onto the new version.

### Question 47 — C

Answer: Register the serverless service as a serverless network endpoint group. A serverless endpoint group fronts the service without a managed instance group. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: A serverless endpoint group fronts the service without a managed instance group.
- **B:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: A serverless endpoint group fronts the service without a managed instance group.
- **C:** Correct. In this case: A serverless endpoint group fronts the service without a managed instance group.
- **D:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: A serverless endpoint group fronts the service without a managed instance group.

### Question 48 — D

Answer: Autoscale a managed instance group behind the backend service. An autoscaled managed instance group adds and removes instances with the signal. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: An autoscaled managed instance group adds and removes instances with the signal.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An autoscaled managed instance group adds and removes instances with the signal.
- **C:** Incorrect for this question. The backend service holds the health check, balancing mode and capacity settings. Why the correct answer wins: An autoscaled managed instance group adds and removes instances with the signal.
- **D:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: An autoscaled managed instance group adds and removes instances with the signal.

### Question 49 — B

Answer: Expose the workload through the GKE Ingress controller. The Ingress controller builds the load balancer from the manifest. An Ingress object creates a Google Cloud load balancer from the manifest. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Ingress controller builds the load balancer from the manifest.
- **B:** Correct. An Ingress object creates a Google Cloud load balancer from the manifest. In this case: The Ingress controller builds the load balancer from the manifest.
- **C:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The Ingress controller builds the load balancer from the manifest.
- **D:** Incorrect for this question. A Gateway object configures the load balancer through the newer Kubernetes API. Why the correct answer wins: The Ingress controller builds the load balancer from the manifest.

### Question 50 — D

Answer: Expose the workload through the GKE Gateway controller. The Gateway controller exposes those routing features through the newer API. A Gateway object configures the load balancer through the newer Kubernetes API. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An Ingress object creates a Google Cloud load balancer from the manifest. Why the correct answer wins: The Gateway controller exposes those routing features through the newer API.
- **B:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The Gateway controller exposes those routing features through the newer API.
- **C:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Gateway controller exposes those routing features through the newer API.
- **D:** Correct. A Gateway object configures the load balancer through the newer Kubernetes API. In this case: The Gateway controller exposes those routing features through the newer API.

### Question 51 — A, B

Answers: Enable Cloud CDN on the backend service; Invalidate the cached object after the change. Caching serves repeat reads nearby, and invalidation drops the corrected stale copy. The edge holds a copy of the response so later requests are served closer to the user. Invalidation removes the stale copy so the next request fetches the current version. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The edge holds a copy of the response so later requests are served closer to the user. In this case: Caching serves repeat reads nearby, and invalidation drops the corrected stale copy.
- **B:** Correct. Invalidation removes the stale copy so the next request fetches the current version. In this case: Caching serves repeat reads nearby, and invalidation drops the corrected stale copy.
- **C:** Incorrect for this question. A signed URL authorises one object for a limited time without making the bucket public. Why the correct answer wins: Caching serves repeat reads nearby, and invalidation drops the corrected stale copy.
- **D:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: Caching serves repeat reads nearby, and invalidation drops the corrected stale copy.
- **E:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: Caching serves repeat reads nearby, and invalidation drops the corrected stale copy.

### Question 52 — B

Answer: Serve the object through a signed URL. A signed URL authorises that one object for a limited window. A signed URL authorises one object for a limited time without making the bucket public. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Invalidation removes the stale copy so the next request fetches the current version. Why the correct answer wins: A signed URL authorises that one object for a limited window.
- **B:** Correct. A signed URL authorises one object for a limited time without making the bucket public. In this case: A signed URL authorises that one object for a limited window.
- **C:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: A signed URL authorises that one object for a limited window.
- **D:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: A signed URL authorises that one object for a limited window.

### Question 53 — A, C

Answers: Create a private Cloud DNS zone; Create a DNS peering zone to the other project. A private zone answers only inside the authorised networks, and the peering zone covers the second project. The zone answers only for clients inside the authorised networks. The consumer project resolves names from the producer project through a peering zone. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The zone answers only for clients inside the authorised networks. In this case: A private zone answers only inside the authorised networks, and the peering zone covers the second project.
- **B:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: A private zone answers only inside the authorised networks, and the peering zone covers the second project.
- **C:** Correct. The consumer project resolves names from the producer project through a peering zone. In this case: A private zone answers only inside the authorised networks, and the peering zone covers the second project.
- **D:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A private zone answers only inside the authorised networks, and the peering zone covers the second project.
- **E:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: A private zone answers only inside the authorised networks, and the peering zone covers the second project.

### Question 54 — D

Answer: Lower the record TTL before the cutover. A short TTL lets resolvers pick up the new address soon after the change. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: A short TTL lets resolvers pick up the new address soon after the change.
- **B:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A short TTL lets resolvers pick up the new address soon after the change.
- **C:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: A short TTL lets resolvers pick up the new address soon after the change.
- **D:** Correct. In this case: A short TTL lets resolvers pick up the new address soon after the change.

### Question 55 — A

Answer: Apply a geolocation routing policy to the record set. The geolocation policy picks the answer from the source region of the query. The answer depends on the source region of the query. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The answer depends on the source region of the query. In this case: The geolocation policy picks the answer from the source region of the query.
- **B:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The geolocation policy picks the answer from the source region of the query.
- **C:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: The geolocation policy picks the answer from the source region of the query.
- **D:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: The geolocation policy picks the answer from the source region of the query.

### Question 56 — B

Answer: Apply a failover routing policy with a health-checked primary. The failover policy serves the standby when the primary fails its health check. The standby answer is served when the primary fails its health check. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy serves the standby when the primary fails its health check.
- **B:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy serves the standby when the primary fails its health check.
- **C:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The failover policy serves the standby when the primary fails its health check.
- **D:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The failover policy serves the standby when the primary fails its health check.

### Question 57 — B

Answer: Enable DNSSEC on the zone. DNSSEC signatures let a resolver verify that the answer was not changed. Signatures let a resolver verify that the answer was not altered in transit. Local study-map skill 3.8 (DNSSEC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: DNSSEC signatures let a resolver verify that the answer was not changed.
- **B:** Correct. Signatures let a resolver verify that the answer was not altered in transit. In this case: DNSSEC signatures let a resolver verify that the answer was not changed.
- **C:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: DNSSEC signatures let a resolver verify that the answer was not changed.
- **D:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: DNSSEC signatures let a resolver verify that the answer was not changed.

### Question 58 — A, D

Answers: Create a VLAN attachment on Cloud Router; Set the Cloud Router ASN to a private value that differs from the peer. The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's. The attachment carries one VLAN over the interconnect and peers with the router. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's.
- **B:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's.
- **C:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's.
- **D:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's.
- **E:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The VLAN attachment binds the circuit to the router, and the ASN must differ from the peer's.

### Question 59 — D

Answer: Order a Dedicated Interconnect connection. Dedicated Interconnect is a physical circuit into a Google colocation facility. A private physical circuit connects the premises to a Google colocation facility. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Dedicated Interconnect is a physical circuit into a Google colocation facility.
- **B:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: Dedicated Interconnect is a physical circuit into a Google colocation facility.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Dedicated Interconnect is a physical circuit into a Google colocation facility.
- **D:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: Dedicated Interconnect is a physical circuit into a Google colocation facility.

### Question 60 — B

Answer: Create a VLAN attachment on Cloud Router. The VLAN attachment binds the circuit to Cloud Router so BGP can run. The attachment carries one VLAN over the interconnect and peers with the router. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: The VLAN attachment binds the circuit to Cloud Router so BGP can run.
- **B:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The VLAN attachment binds the circuit to Cloud Router so BGP can run.
- **C:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: The VLAN attachment binds the circuit to Cloud Router so BGP can run.
- **D:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: The VLAN attachment binds the circuit to Cloud Router so BGP can run.

### Question 61 — A

Answer: Order a Partner Interconnect connection. A partner carries the circuit to Google from a nearby provider location. A service provider carries the circuit to Google on the customer behalf. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A service provider carries the circuit to Google on the customer behalf. In this case: A partner carries the circuit to Google from a nearby provider location.
- **B:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: A partner carries the circuit to Google from a nearby provider location.
- **C:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: A partner carries the circuit to Google from a nearby provider location.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: A partner carries the circuit to Google from a nearby provider location.

### Question 62 — C

Answer: Order a Cross-Cloud Interconnect connection. Cross-Cloud Interconnect connects Google Cloud directly to another provider. A dedicated circuit connects Google Cloud directly to another cloud provider. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Cross-Cloud Interconnect connects Google Cloud directly to another provider.
- **B:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Cross-Cloud Interconnect connects Google Cloud directly to another provider.
- **C:** Correct. A dedicated circuit connects Google Cloud directly to another cloud provider. In this case: Cross-Cloud Interconnect connects Google Cloud directly to another provider.
- **D:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Cross-Cloud Interconnect connects Google Cloud directly to another provider.

### Question 63 — C, E

Answers: Deploy an HA VPN gateway with two interfaces; Lower the tunnel MTU to 1460 bytes. Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path. Two interfaces in different zones give the tunnel pair a 99.99% topology. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path.
- **B:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path.
- **C:** Correct. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. In this case: Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path.
- **E:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: Two interfaces in different zones give the redundant pair, and the smaller MTU fits the encapsulated path.

### Question 64 — D

Answer: Deploy an HA VPN gateway with two interfaces. An HA VPN gateway between the two networks keeps the traffic internal. Two interfaces in different zones give the tunnel pair a 99.99% topology. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: An HA VPN gateway between the two networks keeps the traffic internal.
- **B:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: An HA VPN gateway between the two networks keeps the traffic internal.
- **C:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: An HA VPN gateway between the two networks keeps the traffic internal.
- **D:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: An HA VPN gateway between the two networks keeps the traffic internal.

### Question 65 — C

Answer: Deploy a Classic VPN with a single tunnel. A Classic VPN has one tunnel and no second path to fail over to. One tunnel gives a single path and no automatic failover. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: A Classic VPN has one tunnel and no second path to fail over to.
- **B:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: A Classic VPN has one tunnel and no second path to fail over to.
- **C:** Correct. One tunnel gives a single path and no automatic failover. In this case: A Classic VPN has one tunnel and no second path to fail over to.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: A Classic VPN has one tunnel and no second path to fail over to.

### Question 66 — A

Answer: Deploy a Classic VPN with a single tunnel. Classic VPN supports the policy-based mode that device requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.4 (Classic VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports the policy-based mode that device requires.
- **B:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Classic VPN supports the policy-based mode that device requires.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Classic VPN supports the policy-based mode that device requires.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: Classic VPN supports the policy-based mode that device requires.

### Question 67 — A

Answer: Set the Cloud Router ASN to a private value that differs from the peer. Two peers cannot share one autonomous system number. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: Two peers cannot share one autonomous system number.
- **B:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Two peers cannot share one autonomous system number.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Two peers cannot share one autonomous system number.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Two peers cannot share one autonomous system number.

### Question 68 — B

Answer: Prefer the path with the lower multi-exit discriminator. The lower discriminator on the preferred attachment makes it the chosen path. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The lower discriminator on the preferred attachment makes it the chosen path.
- **B:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The lower discriminator on the preferred attachment makes it the chosen path.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower discriminator on the preferred attachment makes it the chosen path.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower discriminator on the preferred attachment makes it the chosen path.

### Question 69 — A, E

Answers: Advertise only the ranges the peer needs; Switch the Cloud Router to global dynamic routing mode. A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere. The router advertises a chosen prefix list instead of every subnet in the VPC. Routes learned in one region are available to subnets in every region. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere.
- **E:** Correct. Routes learned in one region are available to subnets in every region. In this case: A chosen advertisement list hides the rest, and global dynamic routing makes the routes usable everywhere.

### Question 70 — A

Answer: Enable Bidirectional Forwarding Detection with a short interval. Bidirectional Forwarding Detection signals the dead path far sooner than the hold timer. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.6 (BFD and Failover Timers), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: Bidirectional Forwarding Detection signals the dead path far sooner than the hold timer.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Bidirectional Forwarding Detection signals the dead path far sooner than the hold timer.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Bidirectional Forwarding Detection signals the dead path far sooner than the hold timer.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Bidirectional Forwarding Detection signals the dead path far sooner than the hold timer.

### Question 71 — C

Answer: Give the static route a lower priority number than the learned route. The lower priority number decides between routes for the same prefix. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower priority number decides between routes for the same prefix.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The lower priority number decides between routes for the same prefix.
- **C:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: The lower priority number decides between routes for the same prefix.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower priority number decides between routes for the same prefix.

### Question 72 — C

Answer: Switch best path selection back to the legacy behaviour. Best path selection order changed, so the tie was broken differently. The older selection order picks a different preferred path when the inputs tie. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Best path selection order changed, so the tie was broken differently.
- **B:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: Best path selection order changed, so the tie was broken differently.
- **C:** Correct. The older selection order picks a different preferred path when the inputs tie. In this case: Best path selection order changed, so the tie was broken differently.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Best path selection order changed, so the tie was broken differently.

### Question 73 — C

Answer: Enable MACsec on the interconnect. MACsec encrypts each hop of the circuit itself. Link-layer encryption protects each hop of the circuit between the premises and Google. Local study-map skill 4.8 (Interconnect Encryption and SLA), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: MACsec encrypts each hop of the circuit itself.
- **B:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: MACsec encrypts each hop of the circuit itself.
- **C:** Correct. Link-layer encryption protects each hop of the circuit between the premises and Google. In this case: MACsec encrypts each hop of the circuit itself.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: MACsec encrypts each hop of the circuit itself.

### Question 74 — A

Answer: Enable firewall rules logging. Firewall logging records the rule that allowed or denied the connection. The logs show which rule allowed or denied each connection. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs show which rule allowed or denied each connection. In this case: Firewall logging records the rule that allowed or denied the connection.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Firewall logging records the rule that allowed or denied the connection.
- **C:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Firewall logging records the rule that allowed or denied the connection.
- **D:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: Firewall logging records the rule that allowed or denied the connection.

### Question 75 — D

Answer: Enable Cloud NAT logging. NAT logging records the translated address and port for each flow. The logs record the translated address and port chosen for each flow. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: NAT logging records the translated address and port for each flow.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: NAT logging records the translated address and port for each flow.
- **C:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: NAT logging records the translated address and port for each flow.
- **D:** Correct. The logs record the translated address and port chosen for each flow. In this case: NAT logging records the translated address and port for each flow.

### Question 76 — C

Answer: Create an alert policy on the network metric. An alert policy on the tunnel state notifies the rotation when it changes. The policy notifies on the threshold instead of waiting for a user report. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: An alert policy on the tunnel state notifies the rotation when it changes.
- **B:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: An alert policy on the tunnel state notifies the rotation when it changes.
- **C:** Correct. The policy notifies on the threshold instead of waiting for a user report. In this case: An alert policy on the tunnel state notifies the rotation when it changes.
- **D:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: An alert policy on the tunnel state notifies the rotation when it changes.

### Question 77 — B

Answer: Create a log-based metric from the firewall log entries. A log-based metric turns matching entries into a counter the alert can use. Matching log entries become a counter the alerting policy can use. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: A log-based metric turns matching entries into a counter the alert can use.
- **B:** Correct. Matching log entries become a counter the alerting policy can use. In this case: A log-based metric turns matching entries into a counter the alert can use.
- **C:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: A log-based metric turns matching entries into a counter the alert can use.
- **D:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: A log-based metric turns matching entries into a counter the alert can use.

### Question 78 — A

Answer: Run a Connectivity Test between the two endpoints. A connectivity test evaluates the configuration along the path and names the blocker. The test evaluates the configuration along the path and names the blocking rule or missing route. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: A connectivity test evaluates the configuration along the path and names the blocker.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A connectivity test evaluates the configuration along the path and names the blocker.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A connectivity test evaluates the configuration along the path and names the blocker.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: A connectivity test evaluates the configuration along the path and names the blocker.

### Question 79 — A, E

Answers: Run a Connectivity Test between the two endpoints; Enable firewall rules logging. The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow. The test evaluates the configuration along the path and names the blocking rule or missing route. The logs show which rule allowed or denied each connection. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs show which rule allowed or denied each connection. In this case: The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow.
- **D:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow.
- **E:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: The connectivity test names the blocking rule, and the firewall log shows the decision recorded for the flow.

### Question 80 — B

Answer: Check the Performance Dashboard for packet loss. The performance dashboard separates loss on the Google network from loss beyond it. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: The performance dashboard separates loss on the Google network from loss beyond it.
- **B:** Correct. In this case: The performance dashboard separates loss on the Google network from loss beyond it.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The performance dashboard separates loss on the Google network from loss beyond it.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The performance dashboard separates loss on the Google network from loss beyond it.

### Question 81 — D

Answer: Test the path with a large ping and the do-not-fragment bit. A large probe with the do-not-fragment bit shows where the payload stops fitting. The probe shows where the payload stops fitting along the path. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A large probe with the do-not-fragment bit shows where the payload stops fitting.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A large probe with the do-not-fragment bit shows where the payload stops fitting.
- **C:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A large probe with the do-not-fragment bit shows where the payload stops fitting.
- **D:** Correct. The probe shows where the payload stops fitting along the path. In this case: A large probe with the do-not-fragment bit shows where the payload stops fitting.

### Question 82 — A

Answer: Review Firewall Insights for shadowed rules. Firewall Insights names a rule that is shadowed by a broader one. The insight names rules that never match because a broader rule already covered them. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights names a rule that is shadowed by a broader one.
- **B:** Incorrect for this question. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Why the correct answer wins: Firewall Insights names a rule that is shadowed by a broader one.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights names a rule that is shadowed by a broader one.
- **D:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights names a rule that is shadowed by a broader one.

### Question 83 — A, D

Answers: Review Firewall Insights for shadowed rules; Read the Network Analyzer findings. Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks. The insight names rules that never match because a broader rule already covered them. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks.
- **D:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks.
- **E:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights finds shadowed and unused rules, and Network Analyzer reports configuration risks.

### Question 84 — A

Answer: Inspect the flow in Network Topology. Network Topology shows the paths and throughput between the resources. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: Network Topology shows the paths and throughput between the resources.
- **B:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Topology shows the paths and throughput between the resources.
- **C:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Topology shows the paths and throughput between the resources.
- **D:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Network Topology shows the paths and throughput between the resources.

### Question 85 — C

Answer: Query Flow Analyzer for the top talkers. Flow Analyzer ranks the flows that consume the most bandwidth. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Flow Analyzer ranks the flows that consume the most bandwidth.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Flow Analyzer ranks the flows that consume the most bandwidth.
- **C:** Correct. In this case: Flow Analyzer ranks the flows that consume the most bandwidth.
- **D:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Flow Analyzer ranks the flows that consume the most bandwidth.

### Question 86 — B

Answer: Compare the BGP session state on both peers. Comparing the state on both peers points at the shared configuration rather than the path. A session that is established on one side only points at the shared configuration. Local study-map skill 5.7 (BGP and VPN Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Comparing the state on both peers points at the shared configuration rather than the path.
- **B:** Correct. A session that is established on one side only points at the shared configuration. In this case: Comparing the state on both peers points at the shared configuration rather than the path.
- **C:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Comparing the state on both peers points at the shared configuration rather than the path.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Comparing the state on both peers points at the shared configuration rather than the path.

### Question 87 — C

Answer: Drain the backend before removing it. Draining moves new traffic away and lets in-flight requests finish. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 5.8 (Traffic Draining and Migration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Draining moves new traffic away and lets in-flight requests finish.
- **B:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Draining moves new traffic away and lets in-flight requests finish.
- **C:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: Draining moves new traffic away and lets in-flight requests finish.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Draining moves new traffic away and lets in-flight requests finish.

### Question 88 — D

Answer: Attach a Cloud Armor backend security policy. A backend security policy filters traffic that has reached the load balancer. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy filters traffic at the edge before it is proxied to a backend. Why the correct answer wins: A backend security policy filters traffic that has reached the load balancer.
- **B:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: A backend security policy filters traffic that has reached the load balancer.
- **C:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: A backend security policy filters traffic that has reached the load balancer.
- **D:** Correct. In this case: A backend security policy filters traffic that has reached the load balancer.

### Question 89 — C

Answer: Attach a Cloud Armor edge security policy. An edge security policy filters traffic before it is proxied to a backend. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: An edge security policy filters traffic before it is proxied to a backend.
- **B:** Incorrect for this question. The policy filters traffic that has already reached the load balancer. Why the correct answer wins: An edge security policy filters traffic before it is proxied to a backend.
- **C:** Correct. In this case: An edge security policy filters traffic before it is proxied to a backend.
- **D:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: An edge security policy filters traffic before it is proxied to a backend.

### Question 90 — C

Answer: Add a preconfigured WAF rule for the attack class. A preconfigured WAF rule matches that attack class. The rule matches the signatures of that class of request. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: A preconfigured WAF rule matches that attack class.
- **B:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A preconfigured WAF rule matches that attack class.
- **C:** Correct. The rule matches the signatures of that class of request. In this case: A preconfigured WAF rule matches that attack class.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: A preconfigured WAF rule matches that attack class.

### Question 91 — C

Answer: Enable bot management on the policy. Bot management classifies automated clients so the rule can act on intent. Known bot categories are classified so the rule can allow or block them by intent. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Bot management classifies automated clients so the rule can act on intent.
- **B:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Bot management classifies automated clients so the rule can act on intent.
- **C:** Correct. Known bot categories are classified so the rule can allow or block them by intent. In this case: Bot management classifies automated clients so the rule can act on intent.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Bot management classifies automated clients so the rule can act on intent.

### Question 92 — D

Answer: Rely on the default DDoS protection and add a rate limit. Always-on protection absorbs the volume while a rate limit covers the application flood. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. Local study-map skill 6.3 (DDoS and Rate Limiting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Always-on protection absorbs the volume while a rate limit covers the application flood.
- **B:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: Always-on protection absorbs the volume while a rate limit covers the application flood.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Always-on protection absorbs the volume while a rate limit covers the application flood.
- **D:** Correct. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. In this case: Always-on protection absorbs the volume while a rate limit covers the application flood.

### Question 93 — C, E

Answers: Create a hierarchical firewall policy at the organisation; Use secure tags as the rule target. The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner. The policy applies to every project under the organisation node. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner.
- **B:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner.
- **C:** Correct. The policy applies to every project under the organisation node. In this case: The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner.
- **D:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner.
- **E:** Correct. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. In this case: The organisation policy covers every project, and secure tags cannot be set by an ordinary instance owner.

### Question 94 — C

Answer: Move the inspection to NGFW Enterprise. The enterprise tier adds layer 7 inspection. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The base tier covers stateful filtering without advanced inspection. Why the correct answer wins: The enterprise tier adds layer 7 inspection.
- **B:** Incorrect for this question. The standard tier adds the policy model and threat intelligence over the base rules. Why the correct answer wins: The enterprise tier adds layer 7 inspection.
- **C:** Correct. In this case: The enterprise tier adds layer 7 inspection.
- **D:** Incorrect for this question. The policy is evaluated for the networks it is associated with, in every region. Why the correct answer wins: The enterprise tier adds layer 7 inspection.

### Question 95 — D

Answer: Create a regional network firewall policy. A regional policy is scoped to the region it belongs to. The policy applies only in the region it belongs to. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: A regional policy is scoped to the region it belongs to.
- **B:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A regional policy is scoped to the region it belongs to.
- **C:** Incorrect for this question. The policy is evaluated for the networks it is associated with, in every region. Why the correct answer wins: A regional policy is scoped to the region it belongs to.
- **D:** Correct. The policy applies only in the region it belongs to. In this case: A regional policy is scoped to the region it belongs to.

### Question 96 — A

Answer: Add a deny-all egress rule with a higher priority. A deny-all egress rule replaces default allow, and named destinations are then permitted. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. In this case: A deny-all egress rule replaces default allow, and named destinations are then permitted.
- **B:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: A deny-all egress rule replaces default allow, and named destinations are then permitted.
- **C:** Incorrect for this question. The standard tier adds the policy model and threat intelligence over the base rules. Why the correct answer wins: A deny-all egress rule replaces default allow, and named destinations are then permitted.
- **D:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: A deny-all egress rule replaces default allow, and named destinations are then permitted.

### Question 97 — B

Answer: Target the rule with a service account. A service account target can only be changed by someone with rights over that identity. The rule applies to the instances that run as that identity, which only a privileged caller can change. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Tags identify the instances the rule applies to, and any holder can set one. Why the correct answer wins: A service account target can only be changed by someone with rights over that identity.
- **B:** Correct. The rule applies to the instances that run as that identity, which only a privileged caller can change. In this case: A service account target can only be changed by someone with rights over that identity.
- **C:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: A service account target can only be changed by someone with rights over that identity.
- **D:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A service account target can only be changed by someone with rights over that identity.

### Question 98 — A

Answer: Assign a manual static Cloud NAT address. A manual static address keeps the same source address for every flow. A fixed address lets the partner allowlist the source. Local study-map skill 6.6 (Cloud NAT and Port Allocation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A fixed address lets the partner allowlist the source. In this case: A manual static address keeps the same source address for every flow.
- **B:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: A manual static address keeps the same source address for every flow.
- **C:** Incorrect for this question. Google assigns and releases external addresses as the demand changes. Why the correct answer wins: A manual static address keeps the same source address for every flow.
- **D:** Incorrect for this question. The proxy applies URL and TLS inspection policy to outbound traffic. Why the correct answer wins: A manual static address keeps the same source address for every flow.

### Question 99 — D

Answer: Deploy Secure Web Proxy as the egress path. Secure Web Proxy applies URL and TLS inspection to outbound traffic. Local study-map skill 6.7 (Secure Web Proxy), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: Secure Web Proxy applies URL and TLS inspection to outbound traffic.
- **B:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Secure Web Proxy applies URL and TLS inspection to outbound traffic.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Secure Web Proxy applies URL and TLS inspection to outbound traffic.
- **D:** Correct. In this case: Secure Web Proxy applies URL and TLS inspection to outbound traffic.

### Question 100 — D

Answer: Configure Packet Mirroring on the instance group. Packet Mirroring sends a copy to the collector while the original flow continues. Mirrored packets are delivered to the collector for analysis. Local study-map skill 6.8 (Multi-NIC Appliances and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A copy of the traffic goes to a collector while the original flow continues untouched. Why the correct answer wins: Packet Mirroring sends a copy to the collector while the original flow continues.
- **B:** Incorrect for this question. The proxy applies URL and TLS inspection policy to outbound traffic. Why the correct answer wins: Packet Mirroring sends a copy to the collector while the original flow continues.
- **C:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Packet Mirroring sends a copy to the collector while the original flow continues.
- **D:** Correct. Mirrored packets are delivered to the collector for analysis. In this case: Packet Mirroring sends a copy to the collector while the original flow continues.
