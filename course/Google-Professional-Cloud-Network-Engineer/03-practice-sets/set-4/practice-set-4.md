# Google Cloud Professional Cloud Network Engineer — Full-Length Mock Exam 4

Professional Cloud Network Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing and Planning a Google Cloud VPC Network (VPC Design, IP Planning, and Load Balancer Choice)

### 1. Players in six regions share one realtime service and cross-region jitter decides the match. Which tier fits?

- A. Deploy a regional external Application Load Balancer
- B. Enable Cloud CDN on the backend service
- C. Use the Premium network service tier
- D. Use the Standard network service tier

### 2. One region serves one country and every gigabyte is budgeted. Which tier fits?

- A. Deploy a global external Application Load Balancer
- B. Order a Dedicated Interconnect connection
- C. Use the Premium network service tier
- D. Use the Standard network service tier

### 3. A single certified hostname must keep working when a whole region is drained. What should front it?

- A. Use an external proxy Network Load Balancer with TLS termination
- B. Deploy an internal passthrough Network Load Balancer
- C. Deploy a global external Application Load Balancer
- D. Deploy a regional external Application Load Balancer

### 4. A region drain must not reset in-flight requests, and unhealthy backends must leave the pool. Which two settings fit? Select two.

- A. Enable session affinity on the backend service
- B. Register the backends as a zonal network endpoint group
- C. Split traffic between two backend services by weight
- D. Attach a health check to the backend service
- E. Enable connection draining with a timeout

### 5. Cloud workloads must resolve the corporate directory that lives on two datacentre resolvers. What should be configured?

- A. Configure a DNS forwarding policy for the on-premises domain
- B. Create a DNS peering zone to the other project
- C. Create an inbound forwarding policy with a forwarding address
- D. Serve split-horizon answers from separate private and public zones

### 6. A private zone lives in the host project and must answer for three service projects. What should be added?

- A. Create a DNS peering zone to the other project
- B. Enable DNSSEC on the zone
- C. Bind the private zone to the service project networks
- D. Configure a DNS forwarding policy for the on-premises domain

### 7. A legacy client requires TLS 1.2 termination at the front and plain HTTP behind it. Which load balancer fits?

- A. Use a passthrough Network Load Balancer
- B. Deploy an internal passthrough Network Load Balancer
- C. Use the Premium network service tier
- D. Use an external proxy Network Load Balancer with TLS termination

### 8. A RADIUS service must see the original client address and keeps its own session state. Which shape fits?

- A. Route by URL path in the URL map
- B. Use a passthrough Network Load Balancer
- C. Use a proxy Network Load Balancer
- D. Split traffic between two backend services by weight

### 9. A regulator requires that the cluster API is not reachable from the internet at all. What should be configured?

- A. Add the office range to the authorised networks
- B. Use private nodes with no external addresses
- C. Use a private control plane endpoint
- D. Use the DNS-based control plane endpoint

### 10. A platform team wants policy enforcement without iptables chains inside the node. What should be enabled?

- A. Enable GKE Dataplane V2
- B. Create a GKE network policy for the namespace
- C. Add a second pod range to the cluster
- D. Configure an IP masquerade policy on the node pool

### 11. Nodes must have no external addresses, and pods must be addressable apart from the node subnet. Which two settings fit? Select two.

- A. Add a second pod range to the cluster
- B. Configure an IP masquerade policy on the node pool
- C. Plan secondary ranges for pods and services
- D. Add the office range to the authorised networks
- E. Use private nodes with no external addresses

### 12. An auditor requires that an automation can read routes and nothing else. What should be granted?

- A. Create a custom role with only the required network permissions
- B. Grant the basic editor role to the automation
- C. Grant the subnet user role on the specific shared subnets
- D. Grant the network administrator role in the host project

### 13. One team attaches service projects and another deploys into shared subnets. Which two grants fit? Select two.

- A. Grant Shared VPC Admin on the host project
- B. Grant the basic editor role to the automation
- C. Create a custom role with only the required network permissions
- D. Grant the network administrator role in the host project
- E. Grant the subnet user role on the specific shared subnets

### 14. A partner publishes a service attachment and the traffic must never leave Google Cloud. What should be created?

- A. Allocate a private services access range
- B. Enable Private Google Access on the subnet
- C. Attach the service to Serverless VPC Access
- D. Create a Private Service Connect endpoint

### 15. On-premises clients must reach a partner's published service privately through the hub. Which two fit? Select two.

- A. Reach the API through its public interface
- B. Propagate the Private Service Connect connection through hybrid spokes
- C. Attach the service to Serverless VPC Access
- D. Allocate a private services access range
- E. Create a Private Service Connect endpoint

### 16. Eight networks must all reach each other and peering has become unmanageable. What topology fits?

- A. Connect the networks as a hub-and-spoke peering topology
- B. Assume peered networks can reach each other transitively
- C. Peer every VPC network with every other VPC network
- D. Connect the VPC networks through a Network Connectivity Center hub

### 17. A new group of teams must inherit the central address plan and firewall policy. What fits?

- A. Create a VPC Network Peering connection between the two networks
- B. Give each team its own standalone VPC network
- C. Build the network as a Shared VPC with host and service projects
- D. Peer every VPC network with every other VPC network

### 18. Two future acquisitions are known to use private ranges and today's design must survive them. What should be chosen?

- A. Bring your own public IP prefixes
- B. Deploy Private NAT for the overlapping ranges
- C. Use non-RFC 1918 space for the internal network
- D. Use privately used public IP address ranges

### 19. Two teams were allocated the same prefix last quarter. What prevents the repeat?

- A. Enable dual-stack IPv6 on the subnet
- B. Automate address allocation from a central IPAM plan
- C. Accept the overlapping subnet ranges as configured
- D. Deploy Private NAT for the overlapping ranges

### 20. An HA VPN carries database replication and the bulk phase stalls. What should be adjusted?

- A. Raise the VPC MTU to 8896 bytes
- B. Keep the default 1500-byte MTU
- C. Leave the MTU mismatch unfixed
- D. Lower the tunnel MTU to 1460 bytes

### 21. Two appliances inspect traffic and either may be replaced at any time. What should the next hop be?

- A. Create a static route with a tag-scoped next hop
- B. Use the internal load balancer as the next hop
- C. Deploy a multi-NIC appliance VM between the two networks
- D. Add a policy-based route that matches the source and destination

---

## Domain 2 — Implementing a VPC Network (VPC Implementation, Routing, and GKE Networking)

### 22. A subnet must grow without recreating the instances inside it. What is the correct action?

- A. Expand the existing subnet range
- B. Use non-RFC 1918 space for the internal network
- C. Enable dual-stack IPv6 on the subnet
- D. Accept the overlapping subnet ranges as configured

### 23. A subnet needs more IPv4 addresses and the platform must also gain IPv6. Which two changes fit? Select two.

- A. Expand the existing subnet range
- B. Use privately used public IP address ranges
- C. Enable dual-stack IPv6 on the subnet
- D. Bring your own public IP prefixes
- E. Accept the overlapping subnet ranges as configured

### 24. A subsidiary keeps its own network but must reach one service subnet. What is the simplest fit?

- A. Connect the VPC networks through a Network Connectivity Center hub
- B. Create a VPC Network Peering connection between the two networks
- C. Peer every VPC network with every other VPC network
- D. Build the network as a Shared VPC with host and service projects

### 25. A policy-based route must reach the peered network. What option carries it?

- A. Assume peered networks can reach each other transitively
- B. Apply a CIDR range filter to the spoke
- C. Add a policy-based route that matches the source and destination
- D. Import and export custom routes over the peering

### 26. A reorganisation moves six projects onto one host network. Which role does the move?

- A. Grant the subnet user role on the specific shared subnets
- B. Grant Shared VPC Admin on the host project
- C. Create a custom role with only the required network permissions
- D. Grant the network administrator role in the host project

### 27. A team must deploy into two shared subnets and read firewall policy without changing it. Which two grants fit? Select two.

- A. Grant the subnet user role on the specific shared subnets
- B. Grant the network administrator role in the host project
- C. Grant Shared VPC Admin on the host project
- D. Create a custom role with only the required network permissions
- E. Grant the basic editor role to the automation

### 28. A VM under a no-external-address policy must call Google APIs. What enables that?

- A. Reach the API through its public interface
- B. Enable Private Google Access on the subnet
- C. Attach the service to Serverless VPC Access
- D. Create a Private Service Connect endpoint

### 29. A regulated dataset must not be reachable from outside an approved project group. What should be configured?

- A. Create a hierarchical firewall policy at the organisation
- B. Review Firewall Insights for shadowed rules
- C. Enclose the project in a VPC Service Controls perimeter
- D. Enable Private Google Access on the subnet

### 30. Two attachments advertise one prefix and the older circuit must carry the traffic. What should be set?

- A. Give the static route a lower priority number than the learned route
- B. Prefer the path with the lower multi-exit discriminator
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Switch best path selection back to the legacy behaviour

### 31. A hub router in Europe must serve subnets in Asia. What should be enabled?

- A. Advertise only the ranges the peer needs
- B. Keep the Cloud Router in regional dynamic routing mode
- C. Switch the Cloud Router to global dynamic routing mode
- D. Prefer the path with the lower multi-exit discriminator

### 32. A router serves three regions and one circuit must be preferred over the other. Which two settings fit? Select two.

- A. Prefer the path with the lower multi-exit discriminator
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Switch best path selection back to the legacy behaviour
- D. Switch the Cloud Router to global dynamic routing mode
- E. Keep the Cloud Router in regional dynamic routing mode

### 33. Traffic to a SaaS provider must be inspected while everything else goes direct. What fits?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Use the internal load balancer as the next hop
- C. Create a static route with a tag-scoped next hop
- D. Add a policy-based route that matches the source and destination

### 34. Only the instances that process card data must be sent through the security appliance. What should be created?

- A. Use the internal load balancer as the next hop
- B. Add a policy-based route that matches the source and destination
- C. Create a static route with a tag-scoped next hop
- D. Give the static route a lower priority number than the learned route

### 35. Appliance failover must not require a route change. What should the next hop be?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Add a policy-based route that matches the source and destination
- C. Use the internal load balancer as the next hop
- D. Create a static route with a tag-scoped next hop

### 36. A VPN tunnel to a branch must join the hub. Which spoke type fits?

- A. Add the attachment as a hybrid spoke
- B. Expect spoke-to-spoke reachability through the hub
- C. Add the VPC network as a VPC spoke
- D. Add the published service as a producer spoke

### 37. Two branch offices must reach each other through the hub. What provides that?

- A. Add the attachment as a hybrid spoke
- B. Apply a CIDR range filter to the spoke
- C. Add the VPC network as a VPC spoke
- D. Expect spoke-to-spoke reachability through the hub

### 38. Only the ingress namespace may reach the database pods. What should be created?

- A. Configure an IP masquerade policy on the node pool
- B. Enable GKE Dataplane V2
- C. Resize the service range allocation
- D. Create a GKE network policy for the namespace

### 39. A busy cluster runs out of pod addresses mid-quarter and cannot be rebuilt. What should be added?

- A. Add a second pod range to the cluster
- B. Plan secondary ranges for pods and services
- C. Resize the service range allocation
- D. Deploy the cluster into a shared subnet

### 40. On-premises firewalls reject the pod range because it was never routed to them. What should be configured?

- A. Resize the service range allocation
- B. Add a second pod range to the cluster
- C. Enable GKE Dataplane V2
- D. Configure an IP masquerade policy on the node pool

### 41. A capacity review needs byte counts per subnet over a week. What should be enabled?

- A. Enable VPC Flow Logs on the subnet
- B. Enable firewall rules logging
- C. Enable Cloud DNS query logging
- D. Enable Cloud NAT logging

---

## Domain 3 — Configuring Managed Network Services (Load Balancing, Cloud CDN, and Cloud DNS)

### 42. A stateful client must stay on its backend, and maintenance must not cut its requests. Which two settings fit? Select two.

- A. Enable session affinity on the backend service
- B. Switch the balancing mode to connections per instance
- C. Enable connection draining with a timeout
- D. Autoscale a managed instance group behind the backend service
- E. Attach a health check to the backend service

### 43. All traffic lands on one instance because CPU readings are unrelated to the work it does. What should be changed?

- A. Attach a health check to the backend service
- B. Switch the balancing mode to connections per instance
- C. Register the backends as a zonal network endpoint group
- D. Enable session affinity on the backend service

### 44. The instance group must grow with request volume. What should be configured?

- A. Autoscale a managed instance group behind the backend service
- B. Register the backends as a zonal network endpoint group
- C. Enable connection draining with a timeout
- D. Register the serverless service as a serverless network endpoint group

### 45. Two applications share a hostname and differ only by path prefix. What routes them?

- A. Mirror a copy of the traffic to a second backend
- B. Rewrite the request path before it reaches the backend
- C. Split traffic between two backend services by weight
- D. Route by URL path in the URL map

### 46. The backend expects a prefix that clients no longer include. What fixes it?

- A. Mirror a copy of the traffic to a second backend
- B. Route by URL path in the URL map
- C. Rewrite the request path before it reaches the backend
- D. Split traffic between two backend services by weight

### 47. A Cloud Run service must be a backend for the global front end. How should it be registered?

- A. Register the third-party origins as an internet network endpoint group
- B. Autoscale a managed instance group behind the backend service
- C. Register the serverless service as a serverless network endpoint group
- D. Register the backends as a zonal network endpoint group

### 48. An on-premises host must be a backend for the load balancer. What should be created?

- A. Register the serverless service as a serverless network endpoint group
- B. Register the backends as a zonal network endpoint group
- C. Add the backends to a backend service behind the front end
- D. Register the third-party origins as an internet network endpoint group

### 49. A small team wants the least Kubernetes configuration for a public service. What fits?

- A. Route by URL path in the URL map
- B. Expose the workload through the GKE Ingress controller
- C. Expose the workload through the GKE Gateway controller
- D. Register the backends as a zonal network endpoint group

### 50. Several namespaces must share one gateway with per-route controls. What fits?

- A. Expose the workload through the GKE Ingress controller
- B. Expose the workload through the GKE Gateway controller
- C. Split traffic between two backend services by weight
- D. Route by URL path in the URL map

### 51. Static assets must be served from the edge and a correction must appear at once. Which two actions fit? Select two.

- A. Invalidate the cached object after the change
- B. Enable Cloud CDN on the backend service
- C. Point Cloud CDN at the origins through an internet endpoint group
- D. Raise the cache time to live
- E. Serve the object through a signed URL

### 52. The origin is a third-party object store outside Google Cloud. What lets the CDN reach it?

- A. Raise the cache time to live
- B. Point Cloud CDN at the origins through an internet endpoint group
- C. Enable Cloud CDN on the backend service
- D. Register the serverless service as a serverless network endpoint group

### 53. Each country must resolve its own regional address. Which policy fits?

- A. Migrate the zone with a staged import and a delegated test
- B. Apply a geolocation routing policy to the record set
- C. Apply a failover routing policy with a health-checked primary
- D. Lower the record TTL before the cutover

### 54. A cutover needs internal resolution and a fast switch between addresses. Which two settings fit? Select two.

- A. Migrate the zone with a staged import and a delegated test
- B. Lower the record TTL before the cutover
- C. Enable DNSSEC on the zone
- D. Create a private Cloud DNS zone
- E. Create a public Cloud DNS zone

### 55. A secondary region should answer only during an outage of the primary, not as a load-sharing peer. Which policy delivers that?

- A. Apply a failover routing policy with a health-checked primary
- B. Apply a geolocation routing policy to the record set
- C. Enable DNSSEC on the zone
- D. Migrate the zone with a staged import and a delegated test

### 56. A regulator requires that European queries never receive a non-European address. Which policy fits?

- A. Apply a failover routing policy with a health-checked primary
- B. Lower the record TTL before the cutover
- C. Apply a geolocation routing policy to the record set
- D. Enable DNSSEC on the zone

### 57. An auditor must be able to detect a tampered public answer. What should be enabled?

- A. Enable Cloud DNS query logging
- B. Enable DNSSEC on the zone
- C. Create a private Cloud DNS zone
- D. Migrate the zone with a staged import and a delegated test

---

## Domain 4 — Configuring and Implementing Hybrid and Multicloud Interconnectivity (Interconnect, VPN, and Cloud Router)

### 58. A new Dedicated Interconnect must carry one subnet, and the existing peer already uses the router's ASN. Which two items fit? Select two.

- A. Enable MACsec on the interconnect
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Order a Partner Interconnect connection
- D. Run HA VPN over Cloud Interconnect instead of MACsec
- E. Create a VLAN attachment on Cloud Router

### 59. Two private circuits are required into a Google colocation facility the company occupies. Which fits?

- A. Order a Dedicated Interconnect connection
- B. Order a Cross-Cloud Interconnect connection
- C. Order a Partner Interconnect connection
- D. Deploy a Classic VPN with a single tunnel

### 60. The circuit is up but the router shows no interface for it. What is missing?

- A. Create a VPC Network Peering connection between the two networks
- B. Add the VPC network as a VPC spoke
- C. Create a VLAN attachment on Cloud Router
- D. Deploy an HA VPN gateway with two interfaces

### 61. A site has no Google facility nearby but a carrier can hand off layer 2. Which fits?

- A. Deploy an HA VPN gateway with two interfaces
- B. Order a Partner Interconnect connection
- C. Order a Dedicated Interconnect connection
- D. Order a Cross-Cloud Interconnect connection

### 62. Data must be copied to another cloud over a private circuit. Which fits?

- A. Order a Partner Interconnect connection
- B. Deploy a Classic VPN with a single tunnel
- C. Order a Dedicated Interconnect connection
- D. Order a Cross-Cloud Interconnect connection

### 63. A site needs redundant tunnels and replication that fits the encapsulated path. Which two settings fit? Select two.

- A. Create a VLAN attachment on Cloud Router
- B. Lower the tunnel MTU to 1460 bytes
- C. Enable MACsec on the interconnect
- D. Deploy a Classic VPN with a single tunnel
- E. Deploy an HA VPN gateway with two interfaces

### 64. A branch needs two tunnels in different zones to meet an SLA. What fits?

- A. Order a Dedicated Interconnect connection
- B. Deploy an HA VPN gateway with two interfaces
- C. Deploy a Classic VPN with a single tunnel
- D. Create a VLAN attachment on Cloud Router

### 65. A site has one tunnel and the SLA forbids a single path. What must replace it?

- A. Order a Dedicated Interconnect connection
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Deploy a Classic VPN with a single tunnel
- D. Deploy an HA VPN gateway with two interfaces

### 66. An appliance at a remote site supports only policy-based tunnels and has no BGP implementation. Which VPN fits?

- A. Create a VLAN attachment on Cloud Router
- B. Deploy a Classic VPN with a single tunnel
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Deploy an HA VPN gateway with two interfaces

### 67. A path dies silently and traffic waits for the hold timer. What should be enabled?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Switch best path selection back to the legacy behaviour
- D. Prefer the path with the lower multi-exit discriminator

### 68. A session stays idle and both ends claim the same ASN. What must change?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Prefer the path with the lower multi-exit discriminator
- C. Switch best path selection back to the legacy behaviour
- D. Enable Bidirectional Forwarding Detection with a short interval

### 69. The peer must see two summaries and the secondary circuit must stay second. Which two settings fit? Select two.

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Switch best path selection back to the legacy behaviour
- C. Prefer the path with the lower multi-exit discriminator
- D. Advertise only the ranges the peer needs
- E. Enable Bidirectional Forwarding Detection with a short interval

### 70. A link degrades without dropping and BGP does not notice. What should be enabled?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Give the static route a lower priority number than the learned route
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Prefer the path with the lower multi-exit discriminator

### 71. Preference changed after an upgrade with no advertisement change. What should be reviewed?

- A. Give the static route a lower priority number than the learned route
- B. Prefer the path with the lower multi-exit discriminator
- C. Switch best path selection back to the legacy behaviour
- D. Enable Bidirectional Forwarding Detection with a short interval

### 72. A static route must take precedence for one prefix. What should be changed?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Prefer the path with the lower multi-exit discriminator
- C. Switch best path selection back to the legacy behaviour
- D. Give the static route a lower priority number than the learned route

### 73. A defence supplier insists that traffic leaving its premises is encrypted at the link layer, and the optics support it. What should be turned on?

- A. Enable MACsec on the interconnect
- B. Create a VLAN attachment on Cloud Router
- C. Deploy an HA VPN gateway with two interfaces
- D. Run HA VPN over Cloud Interconnect instead of MACsec

---

## Domain 5 — Managing, Monitoring, and Troubleshooting Network Operations (Observability, Troubleshooting, and Traffic Movement)

### 74. An auditor wants the rule name behind each denial. What should be enabled?

- A. Enable firewall rules logging
- B. Enable Cloud DNS query logging
- C. Enable VPC Flow Logs on the subnet
- D. Enable Cloud NAT logging

### 75. A resolution failure must be attributed to the client that asked. What should be enabled?

- A. Enable Cloud NAT logging
- B. Enable firewall rules logging
- C. Enable Cloud DNS query logging
- D. Enable VPC Flow Logs on the subnet

### 76. The network team wants a notification the moment an attachment stops passing traffic. What should be configured?

- A. Publish a custom metric from the appliance
- B. Create an alert policy on the network metric
- C. Create a log-based metric from the firewall log entries
- D. Alert on the error budget of the service objective

### 77. A load balancer appliance reports a queue depth that Google's own metrics do not include. What should the team publish?

- A. Create an alert policy on the network metric
- B. Create a log-based metric from the firewall log entries
- C. Alert on the error budget of the service objective
- D. Publish a custom metric from the appliance

### 78. A blocked flow must be traced to a specific rule without guessing. What should be run?

- A. Inspect the flow in Network Topology
- B. Query Flow Analyzer for the top talkers
- C. Run a Connectivity Test between the two endpoints
- D. Check the Performance Dashboard for packet loss

### 79. A path must be proved and loss inside Google versus outside must be separated. Which two tools fit? Select two.

- A. Enable Cloud DNS query logging
- B. Inspect the flow in Network Topology
- C. Check the Performance Dashboard for packet loss
- D. Run a Connectivity Test between the two endpoints
- E. Query Flow Analyzer for the top talkers

### 80. Users report loss and the engineer needs to know whether Google or the ISP is responsible. What should be checked?

- A. Query Flow Analyzer for the top talkers
- B. Inspect the flow in Network Topology
- C. Test the path with a large ping and the do-not-fragment bit
- D. Check the Performance Dashboard for packet loss

### 81. Large packets vanish on a new path while small ones arrive. What should be tested?

- A. Check the Performance Dashboard for packet loss
- B. Test the path with a large ping and the do-not-fragment bit
- C. Leave the MTU mismatch unfixed
- D. Inspect the flow in Network Topology

### 82. A subnet is near its address limit and a route is misconfigured. What surfaces both?

- A. Review Firewall Insights for shadowed rules
- B. Query Flow Analyzer for the top talkers
- C. Run a Connectivity Test between the two endpoints
- D. Read the Network Analyzer findings

### 83. Dead rules and configuration risks must both appear in a review. Which two tools fit? Select two.

- A. Read the Network Analyzer findings
- B. Enable Cloud DNS query logging
- C. Review Firewall Insights for shadowed rules
- D. Query Flow Analyzer for the top talkers
- E. Run a Connectivity Test between the two endpoints

### 84. A new link must be validated against the diagram of intended paths. What shows the real path?

- A. Inspect the flow in Network Topology
- B. Check the Performance Dashboard for packet loss
- C. Run a Connectivity Test between the two endpoints
- D. Query Flow Analyzer for the top talkers

### 85. Egress spend must be attributed to the heaviest flows. What should be queried?

- A. Check the Performance Dashboard for packet loss
- B. Query Flow Analyzer for the top talkers
- C. Inspect the flow in Network Topology
- D. Review Firewall Insights for shadowed rules

### 86. One peer advertises prefixes that the other never receives. What should be compared?

- A. Prefer the path with the lower multi-exit discriminator
- B. Run a Connectivity Test between the two endpoints
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Compare the BGP session state on both peers

### 87. A legacy front end must be retired without cutting sessions. What should be done first?

- A. Drain the backend before removing it
- B. Enable connection draining with a timeout
- C. Query Flow Analyzer for the top talkers
- D. Inspect the flow in Network Topology

---

## Domain 6 — Configuring, Implementing, and Managing a Cloud Network Security Solution (Cloud Armor, Cloud NGFW, NAT, and Egress Security)

### 88. A backend service must allow only two countries. What should be attached?

- A. Attach a Cloud Armor backend security policy
- B. Add a rate-based ban rule
- C. Add a preconfigured WAF rule for the attack class
- D. Attach a Cloud Armor edge security policy

### 89. A hostile range must be refused before the proxy handles anything. What should be attached?

- A. Attach a Cloud Armor edge security policy
- B. Enable bot management on the policy
- C. Enable Adaptive Protection
- D. Attach a Cloud Armor backend security policy

### 90. A comment form is receiving payloads that try to inject SQL into the backing database. What should be enabled?

- A. Add a preconfigured WAF rule for the attack class
- B. Enable bot management on the policy
- C. Apply Google Threat Intelligence lists
- D. Enable Adaptive Protection

### 91. Some automated clients are partners and others are scrapers. What fits?

- A. Enable bot management on the policy
- B. Apply Google Threat Intelligence lists
- C. Enable Adaptive Protection
- D. Add a preconfigured WAF rule for the attack class

### 92. A volumetric flood arrives from thousands of addresses. What should be relied on?

- A. Add a rate-based ban rule
- B. Rely on the default DDoS protection and add a rate limit
- C. Enable Adaptive Protection
- D. Apply Google Threat Intelligence lists

### 93. A baseline must apply to every project, and payload inspection is required. Which two choices fit? Select two.

- A. Create a VPC firewall rule with a target tag
- B. Move the inspection to NGFW Enterprise
- C. Create a hierarchical firewall policy at the organisation
- D. Reorder the rules by priority
- E. Create a regional network firewall policy

### 94. One inspection ruleset has to cover a network wherever its workloads happen to run. Which policy scope fits?

- A. Create a regional network firewall policy
- B. Create a hierarchical firewall policy at the organisation
- C. Create a VPC firewall rule with a target tag
- D. Create a global network firewall policy

### 95. A policy must stay inside one region for data residency. What fits?

- A. Create a regional network firewall policy
- B. Create a global network firewall policy
- C. Create a hierarchical firewall policy at the organisation
- D. Create a VPC firewall rule with a target tag

### 96. An instance owner must not be able to make a workload match a rule. What should target the rule?

- A. Use secure tags as the rule target
- B. Target the rule with network tags
- C. Reorder the rules by priority
- D. Target the rule with a service account

### 97. Instances can currently reach any destination and only three are allowed. What should be created?

- A. Divide the network into micro-segmented tiers
- B. Move the rules to NGFW Standard
- C. Add a deny-all egress rule with a higher priority
- D. Leave the default allow-ingress rule in place

### 98. A development network has unpredictable demand and no partner allowlist. What should Cloud NAT use?

- A. Use dynamic port allocation
- B. Assign a manual static Cloud NAT address
- C. Use static port allocation
- D. Use automatic Cloud NAT IP allocation

### 99. Egress must be filtered by category and inspected for TLS. What fits?

- A. Assign a manual static Cloud NAT address
- B. Configure Packet Mirroring on the instance group
- C. Deploy Secure Web Proxy as the egress path
- D. Deploy a multi-NIC appliance VM between the two networks

### 100. A copy of selected traffic must reach a collector without changing the path. What fits?

- A. Deploy Secure Web Proxy as the egress path
- B. Inspect the traffic out of band with Packet Mirroring
- C. Deploy a multi-NIC appliance VM between the two networks
- D. Configure Packet Mirroring on the instance group

---

## Answer key and explanations

### Question 1 — C

Answer: Use the Premium network service tier. Premium keeps traffic on the Google network from the nearest edge, which reduces jitter. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: Premium keeps traffic on the Google network from the nearest edge, which reduces jitter.
- **B:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: Premium keeps traffic on the Google network from the nearest edge, which reduces jitter.
- **C:** Correct. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. In this case: Premium keeps traffic on the Google network from the nearest edge, which reduces jitter.
- **D:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: Premium keeps traffic on the Google network from the nearest edge, which reduces jitter.

### Question 2 — D

Answer: Use the Standard network service tier. Standard keeps the long haul on the public internet, which is the cheaper path here. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A global anycast address routes each user to the closest healthy region. Why the correct answer wins: Standard keeps the long haul on the public internet, which is the cheaper path here.
- **B:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Standard keeps the long haul on the public internet, which is the cheaper path here.
- **C:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: Standard keeps the long haul on the public internet, which is the cheaper path here.
- **D:** Correct. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. In this case: Standard keeps the long haul on the public internet, which is the cheaper path here.

### Question 3 — C

Answer: Deploy a global external Application Load Balancer. A global anycast address reaches the surviving region without a DNS change. A global anycast address routes each user to the closest healthy region. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates TLS and forwards a separate connection to the backend. Why the correct answer wins: A global anycast address reaches the surviving region without a DNS change.
- **B:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: A global anycast address reaches the surviving region without a DNS change.
- **C:** Correct. A global anycast address routes each user to the closest healthy region. In this case: A global anycast address reaches the surviving region without a DNS change.
- **D:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: A global anycast address reaches the surviving region without a DNS change.

### Question 4 — D, E

Answers: Enable connection draining with a timeout; Attach a health check to the backend service. Draining lets the live requests finish, and the health check removes the failing backends. Removing a backend waits for in-flight requests to finish before the backend is detached. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: Draining lets the live requests finish, and the health check removes the failing backends.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: Draining lets the live requests finish, and the health check removes the failing backends.
- **C:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Draining lets the live requests finish, and the health check removes the failing backends.
- **D:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: Draining lets the live requests finish, and the health check removes the failing backends.
- **E:** Correct. Removing a backend waits for in-flight requests to finish before the backend is detached. In this case: Draining lets the live requests finish, and the health check removes the failing backends.

### Question 5 — A

Answer: Configure a DNS forwarding policy for the on-premises domain. A forwarding policy sends that suffix to those resolvers. Queries for the corporate suffix are forwarded to the on-premises resolvers. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Queries for the corporate suffix are forwarded to the on-premises resolvers. In this case: A forwarding policy sends that suffix to those resolvers.
- **B:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: A forwarding policy sends that suffix to those resolvers.
- **C:** Incorrect for this question. On-premises resolvers send queries to that address to reach Cloud DNS names. Why the correct answer wins: A forwarding policy sends that suffix to those resolvers.
- **D:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: A forwarding policy sends that suffix to those resolvers.

### Question 6 — C

Answer: Bind the private zone to the service project networks. The cross-project binding extends the zone to those networks. The binding makes the host project's zone answer for the service project's networks. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: The cross-project binding extends the zone to those networks.
- **B:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The cross-project binding extends the zone to those networks.
- **C:** Correct. The binding makes the host project's zone answer for the service project's networks. In this case: The cross-project binding extends the zone to those networks.
- **D:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: The cross-project binding extends the zone to those networks.

### Question 7 — D

Answer: Use an external proxy Network Load Balancer with TLS termination. The proxy terminates TLS and forwards a separate connection. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: The proxy terminates TLS and forwards a separate connection.
- **B:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: The proxy terminates TLS and forwards a separate connection.
- **C:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: The proxy terminates TLS and forwards a separate connection.
- **D:** Correct. In this case: The proxy terminates TLS and forwards a separate connection.

### Question 8 — B

Answer: Use a passthrough Network Load Balancer. Passthrough forwards the original packet, preserving the client address. Packets keep their client source address and the backend sees the original flow. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Passthrough forwards the original packet, preserving the client address.
- **B:** Correct. Packets keep their client source address and the backend sees the original flow. In this case: Passthrough forwards the original packet, preserving the client address.
- **C:** Incorrect for this question. The proxy terminates the client connection and opens a separate one to the backend. Why the correct answer wins: Passthrough forwards the original packet, preserving the client address.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Passthrough forwards the original packet, preserving the client address.

### Question 9 — C

Answer: Use a private control plane endpoint. The private endpoint accepts only internal or authorised access. The API server is reachable only through the internal address or an authorised network. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: The private endpoint accepts only internal or authorised access.
- **B:** Incorrect for this question. Nodes reach the control plane and Google APIs through internal paths only. Why the correct answer wins: The private endpoint accepts only internal or authorised access.
- **C:** Correct. The API server is reachable only through the internal address or an authorised network. In this case: The private endpoint accepts only internal or authorised access.
- **D:** Incorrect for this question. The endpoint resolves through a private DNS name instead of a fixed address. Why the correct answer wins: The private endpoint accepts only internal or authorised access.

### Question 10 — A

Answer: Enable GKE Dataplane V2. The eBPF dataplane enforces policy without the iptables path. The eBPF dataplane handles policy and service routing inside the cluster. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The eBPF dataplane handles policy and service routing inside the cluster. In this case: The eBPF dataplane enforces policy without the iptables path.
- **B:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The eBPF dataplane enforces policy without the iptables path.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The eBPF dataplane enforces policy without the iptables path.
- **D:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: The eBPF dataplane enforces policy without the iptables path.

### Question 11 — C, E

Answers: Use private nodes with no external addresses; Plan secondary ranges for pods and services. Private nodes remove external addresses, and secondary ranges separate pod space. Nodes reach the control plane and Google APIs through internal paths only. Alias ranges give pods and services addresses that are separate from the node subnet. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Private nodes remove external addresses, and secondary ranges separate pod space.
- **B:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: Private nodes remove external addresses, and secondary ranges separate pod space.
- **C:** Correct. Alias ranges give pods and services addresses that are separate from the node subnet. In this case: Private nodes remove external addresses, and secondary ranges separate pod space.
- **D:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: Private nodes remove external addresses, and secondary ranges separate pod space.
- **E:** Correct. Nodes reach the control plane and Google APIs through internal paths only. In this case: Private nodes remove external addresses, and secondary ranges separate pod space.

### Question 12 — A

Answer: Create a custom role with only the required network permissions. A custom role names exactly the read permission required. The custom role names the exact permissions the automation needs. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The custom role names the exact permissions the automation needs. In this case: A custom role names exactly the read permission required.
- **B:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: A custom role names exactly the read permission required.
- **C:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: A custom role names exactly the read permission required.
- **D:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: A custom role names exactly the read permission required.

### Question 13 — A, E

Answers: Grant Shared VPC Admin on the host project; Grant the subnet user role on the specific shared subnets. The admin role attaches projects, and subnet user lets the second team deploy. That role attaches service projects and delegates subnet use. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. That role attaches service projects and delegates subnet use. In this case: The admin role attaches projects, and subnet user lets the second team deploy.
- **B:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: The admin role attaches projects, and subnet user lets the second team deploy.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: The admin role attaches projects, and subnet user lets the second team deploy.
- **D:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: The admin role attaches projects, and subnet user lets the second team deploy.
- **E:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: The admin role attaches projects, and subnet user lets the second team deploy.

### Question 14 — D

Answer: Create a Private Service Connect endpoint. A private endpoint targets the partner's attachment inside the VPC. A private endpoint inside the consumer VPC targets a published service attachment. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A reserved internal range lets a managed service provider peer into the VPC. Why the correct answer wins: A private endpoint targets the partner's attachment inside the VPC.
- **B:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A private endpoint targets the partner's attachment inside the VPC.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: A private endpoint targets the partner's attachment inside the VPC.
- **D:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: A private endpoint targets the partner's attachment inside the VPC.

### Question 15 — B, E

Answers: Create a Private Service Connect endpoint; Propagate the Private Service Connect connection through hybrid spokes. The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes. A private endpoint inside the consumer VPC targets a published service attachment. Hybrid traffic reaches the private endpoint without a separate endpoint on each side. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes.
- **B:** Correct. Hybrid traffic reaches the private endpoint without a separate endpoint on each side. In this case: The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes.
- **D:** Incorrect for this question. A reserved internal range lets a managed service provider peer into the VPC. Why the correct answer wins: The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes.
- **E:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: The private endpoint consumes the attachment, and propagation carries it to the hybrid spokes.

### Question 16 — D

Answer: Connect the VPC networks through a Network Connectivity Center hub. A hub connects every spoke and forwards between them. A hub groups spokes so the connected networks reach each other through one managed topology. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network peers with each leaf network, and the leaves do not peer with each other. Why the correct answer wins: A hub connects every spoke and forwards between them.
- **B:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: A hub connects every spoke and forwards between them.
- **C:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: A hub connects every spoke and forwards between them.
- **D:** Correct. A hub groups spokes so the connected networks reach each other through one managed topology. In this case: A hub connects every spoke and forwards between them.

### Question 17 — C

Answer: Build the network as a Shared VPC with host and service projects. Shared VPC gives the teams subnets from the central network. One host project owns the network and subnets while service projects deploy into shared subnets. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Shared VPC gives the teams subnets from the central network.
- **B:** Incorrect for this question. Separate projects own separate networks, and nothing is shared implicitly. Why the correct answer wins: Shared VPC gives the teams subnets from the central network.
- **C:** Correct. One host project owns the network and subnets while service projects deploy into shared subnets. In this case: Shared VPC gives the teams subnets from the central network.
- **D:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Shared VPC gives the teams subnets from the central network.

### Question 18 — C

Answer: Use non-RFC 1918 space for the internal network. Space outside the private ranges cannot collide with those acquisitions. The internal network uses address space outside the private ranges to avoid collisions later. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Space outside the private ranges cannot collide with those acquisitions.
- **B:** Incorrect for this question. Source addresses are translated so two networks with the same private ranges can still talk. Why the correct answer wins: Space outside the private ranges cannot collide with those acquisitions.
- **C:** Correct. The internal network uses address space outside the private ranges to avoid collisions later. In this case: Space outside the private ranges cannot collide with those acquisitions.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Space outside the private ranges cannot collide with those acquisitions.

### Question 19 — B

Answer: Automate address allocation from a central IPAM plan. Allocation from one authoritative plan prevents duplicate assignment. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The subnet carries both an IPv4 range and an internal or external IPv6 range. Why the correct answer wins: Allocation from one authoritative plan prevents duplicate assignment.
- **B:** Correct. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. In this case: Allocation from one authoritative plan prevents duplicate assignment.
- **C:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Allocation from one authoritative plan prevents duplicate assignment.
- **D:** Incorrect for this question. Source addresses are translated so two networks with the same private ranges can still talk. Why the correct answer wins: Allocation from one authoritative plan prevents duplicate assignment.

### Question 20 — D

Answer: Lower the tunnel MTU to 1460 bytes. Tunnel headers reduce usable payload, so the MTU must fit inside the tunnel. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Local study-map skill 1.10 (MTU Sizing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A larger maximum transmission unit carries more payload per packet inside the VPC. Why the correct answer wins: Tunnel headers reduce usable payload, so the MTU must fit inside the tunnel.
- **B:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: Tunnel headers reduce usable payload, so the MTU must fit inside the tunnel.
- **C:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: Tunnel headers reduce usable payload, so the MTU must fit inside the tunnel.
- **D:** Correct. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. In this case: Tunnel headers reduce usable payload, so the MTU must fit inside the tunnel.

### Question 21 — B

Answer: Use the internal load balancer as the next hop. The internal load balancer hides replacement from the route table. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 1.11 (Third-Party Appliance Insertion), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer hides replacement from the route table.
- **B:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer hides replacement from the route table.
- **C:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer hides replacement from the route table.
- **D:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer hides replacement from the route table.

### Question 22 — A

Answer: Expand the existing subnet range. The prefix can grow in place while the instances keep their addresses. A subnet prefix can grow within its address range, and the growth cannot shrink later. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: The prefix can grow in place while the instances keep their addresses.
- **B:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: The prefix can grow in place while the instances keep their addresses.
- **C:** Incorrect for this question. The subnet carries both an IPv4 range and an internal or external IPv6 range. Why the correct answer wins: The prefix can grow in place while the instances keep their addresses.
- **D:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: The prefix can grow in place while the instances keep their addresses.

### Question 23 — A, C

Answers: Enable dual-stack IPv6 on the subnet; Expand the existing subnet range. Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range. The subnet carries both an IPv4 range and an internal or external IPv6 range. A subnet prefix can grow within its address range, and the growth cannot shrink later. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **B:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **C:** Correct. The subnet carries both an IPv4 range and an internal or external IPv6 range. In this case: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **D:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **E:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.

### Question 24 — B

Answer: Create a VPC Network Peering connection between the two networks. Peering joins the two networks and policy limits what is reachable. Two networks exchange routes directly without a gateway or a shared project. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering joins the two networks and policy limits what is reachable.
- **B:** Correct. Two networks exchange routes directly without a gateway or a shared project. In this case: Peering joins the two networks and policy limits what is reachable.
- **C:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering joins the two networks and policy limits what is reachable.
- **D:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: Peering joins the two networks and policy limits what is reachable.

### Question 25 — D

Answer: Import and export custom routes over the peering. Exporting custom routes sends policy-based routes across the peering. The peering option carries static and policy-based routes between the two networks. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: Exporting custom routes sends policy-based routes across the peering.
- **B:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: Exporting custom routes sends policy-based routes across the peering.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: Exporting custom routes sends policy-based routes across the peering.
- **D:** Correct. The peering option carries static and policy-based routes between the two networks. In this case: Exporting custom routes sends policy-based routes across the peering.

### Question 26 — B

Answer: Grant Shared VPC Admin on the host project. Shared VPC Admin attaches the service projects. That role attaches service projects and delegates subnet use. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: Shared VPC Admin attaches the service projects.
- **B:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC Admin attaches the service projects.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: Shared VPC Admin attaches the service projects.
- **D:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC Admin attaches the service projects.

### Question 27 — A, D

Answers: Grant the subnet user role on the specific shared subnets; Create a custom role with only the required network permissions. Subnet user covers the deployable subnets, and a custom role holds the read permission. The role lets a service project deploy into the named subnets and nothing else. The custom role names the exact permissions the automation needs. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Subnet user covers the deployable subnets, and a custom role holds the read permission.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Subnet user covers the deployable subnets, and a custom role holds the read permission.
- **C:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: Subnet user covers the deployable subnets, and a custom role holds the read permission.
- **D:** Correct. The custom role names the exact permissions the automation needs. In this case: Subnet user covers the deployable subnets, and a custom role holds the read permission.
- **E:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Subnet user covers the deployable subnets, and a custom role holds the read permission.

### Question 28 — B

Answer: Enable Private Google Access on the subnet. Private Google Access routes those calls internally. Instances without external addresses reach Google APIs through internal routing. Local study-map skill 2.4 (Private Google Access and APIs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Private Google Access routes those calls internally.
- **B:** Correct. Instances without external addresses reach Google APIs through internal routing. In this case: Private Google Access routes those calls internally.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Private Google Access routes those calls internally.
- **D:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Private Google Access routes those calls internally.

### Question 29 — C

Answer: Enclose the project in a VPC Service Controls perimeter. A service perimeter blocks access across its boundary. The perimeter restricts which services the project may call and blocks data movement outside it. Local study-map skill 2.5 (VPC Service Controls Perimeters), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A service perimeter blocks access across its boundary.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: A service perimeter blocks access across its boundary.
- **C:** Correct. The perimeter restricts which services the project may call and blocks data movement outside it. In this case: A service perimeter blocks access across its boundary.
- **D:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A service perimeter blocks access across its boundary.

### Question 30 — B

Answer: Prefer the path with the lower multi-exit discriminator. The lower discriminator makes the preferred circuit the chosen path. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The lower discriminator makes the preferred circuit the chosen path.
- **B:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The lower discriminator makes the preferred circuit the chosen path.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower discriminator makes the preferred circuit the chosen path.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower discriminator makes the preferred circuit the chosen path.

### Question 31 — C

Answer: Switch the Cloud Router to global dynamic routing mode. Global dynamic routing makes learned routes usable in every region. Routes learned in one region are available to subnets in every region. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: Global dynamic routing makes learned routes usable in every region.
- **B:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global dynamic routing makes learned routes usable in every region.
- **C:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global dynamic routing makes learned routes usable in every region.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global dynamic routing makes learned routes usable in every region.

### Question 32 — A, D

Answers: Switch the Cloud Router to global dynamic routing mode; Prefer the path with the lower multi-exit discriminator. Global mode spreads the learned routes, and the discriminator ranks the circuits. Routes learned in one region are available to subnets in every region. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: Global mode spreads the learned routes, and the discriminator ranks the circuits.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Global mode spreads the learned routes, and the discriminator ranks the circuits.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Global mode spreads the learned routes, and the discriminator ranks the circuits.
- **D:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global mode spreads the learned routes, and the discriminator ranks the circuits.
- **E:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global mode spreads the learned routes, and the discriminator ranks the circuits.

### Question 33 — D

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches that destination and forwards to the appliance. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A policy-based route matches that destination and forwards to the appliance.
- **B:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches that destination and forwards to the appliance.
- **C:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches that destination and forwards to the appliance.
- **D:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches that destination and forwards to the appliance.

### Question 34 — C

Answer: Create a static route with a tag-scoped next hop. A tag-scoped static route affects only the instances that carry that tag. Only instances carrying the tag send their traffic through the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A tag-scoped static route affects only the instances that carry that tag.
- **B:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: A tag-scoped static route affects only the instances that carry that tag.
- **C:** Correct. Only instances carrying the tag send their traffic through the appliance. In this case: A tag-scoped static route affects only the instances that carry that tag.
- **D:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A tag-scoped static route affects only the instances that carry that tag.

### Question 35 — C

Answer: Use the internal load balancer as the next hop. The internal load balancer selects a live appliance. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 2.8 (Internal Load Balancer as Next Hop), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer selects a live appliance.
- **B:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer selects a live appliance.
- **C:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer selects a live appliance.
- **D:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer selects a live appliance.

### Question 36 — A

Answer: Add the attachment as a hybrid spoke. A hybrid spoke carries the tunnel into the hub. The spoke carries the VLAN attachment or VPN into the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The spoke carries the VLAN attachment or VPN into the hub. In this case: A hybrid spoke carries the tunnel into the hub.
- **B:** Incorrect for this question. The hub forwards between spokes, which peering alone cannot do. Why the correct answer wins: A hybrid spoke carries the tunnel into the hub.
- **C:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A hybrid spoke carries the tunnel into the hub.
- **D:** Incorrect for this question. The spoke publishes a service attachment so consumers reach it through the hub. Why the correct answer wins: A hybrid spoke carries the tunnel into the hub.

### Question 37 — D

Answer: Expect spoke-to-spoke reachability through the hub. The hub forwards between spokes, which is what the branches need. The hub forwards between spokes, which peering alone cannot do. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: The hub forwards between spokes, which is what the branches need.
- **B:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: The hub forwards between spokes, which is what the branches need.
- **C:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: The hub forwards between spokes, which is what the branches need.
- **D:** Correct. The hub forwards between spokes, which peering alone cannot do. In this case: The hub forwards between spokes, which is what the branches need.

### Question 38 — D

Answer: Create a GKE network policy for the namespace. A network policy restricts which pods may reach the selected pods. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **C:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **D:** Correct. In this case: A network policy restricts which pods may reach the selected pods.

### Question 39 — A

Answer: Add a second pod range to the cluster. An additional pod range adds alias addresses in place. An additional alias range gives pods more addresses without rebuilding the cluster. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. An additional alias range gives pods more addresses without rebuilding the cluster. In this case: An additional pod range adds alias addresses in place.
- **B:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: An additional pod range adds alias addresses in place.
- **C:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: An additional pod range adds alias addresses in place.
- **D:** Incorrect for this question. The cluster consumes subnets that the host project owns. Why the correct answer wins: An additional pod range adds alias addresses in place.

### Question 40 — D

Answer: Configure an IP masquerade policy on the node pool. Masquerading presents the node address instead of the pod address. Outbound pod traffic is translated to the node address under the chosen conditions. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **C:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **D:** Correct. Outbound pod traffic is translated to the node address under the chosen conditions. In this case: Masquerading presents the node address instead of the pod address.

### Question 41 — A

Answer: Enable VPC Flow Logs on the subnet. Flow logs record byte counts for sampled connections. The logs record sampled connections with source, destination, port and byte counts. Local study-map skill 2.11 (VPC Flow Logs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs record sampled connections with source, destination, port and byte counts. In this case: Flow logs record byte counts for sampled connections.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: Flow logs record byte counts for sampled connections.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Flow logs record byte counts for sampled connections.
- **D:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Flow logs record byte counts for sampled connections.

### Question 42 — A, C

Answers: Enable session affinity on the backend service; Enable connection draining with a timeout. Affinity keeps the client where its state is, and draining lets finished work complete. Affinity keeps a client on the backend that already holds its session state. Removing a backend waits for in-flight requests to finish before the backend is detached. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Affinity keeps a client on the backend that already holds its session state. In this case: Affinity keeps the client where its state is, and draining lets finished work complete.
- **B:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: Affinity keeps the client where its state is, and draining lets finished work complete.
- **C:** Correct. Removing a backend waits for in-flight requests to finish before the backend is detached. In this case: Affinity keeps the client where its state is, and draining lets finished work complete.
- **D:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: Affinity keeps the client where its state is, and draining lets finished work complete.
- **E:** Incorrect for this question. The check removes a backend that cannot answer, so traffic moves to a healthy one. Why the correct answer wins: Affinity keeps the client where its state is, and draining lets finished work complete.

### Question 43 — B

Answer: Switch the balancing mode to connections per instance. Balancing by connection count ignores the misleading CPU signal. The mode spreads load by connection count rather than by CPU utilisation. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The check removes a backend that cannot answer, so traffic moves to a healthy one. Why the correct answer wins: Balancing by connection count ignores the misleading CPU signal.
- **B:** Correct. The mode spreads load by connection count rather than by CPU utilisation. In this case: Balancing by connection count ignores the misleading CPU signal.
- **C:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: Balancing by connection count ignores the misleading CPU signal.
- **D:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: Balancing by connection count ignores the misleading CPU signal.

### Question 44 — A

Answer: Autoscale a managed instance group behind the backend service. The autoscaler adds members as the signal rises. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: The autoscaler adds members as the signal rises.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The autoscaler adds members as the signal rises.
- **C:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: The autoscaler adds members as the signal rises.
- **D:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: The autoscaler adds members as the signal rises.

### Question 45 — D

Answer: Route by URL path in the URL map. The URL map selects the backend from host and path. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: The URL map selects the backend from host and path.
- **B:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: The URL map selects the backend from host and path.
- **C:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The URL map selects the backend from host and path.
- **D:** Correct. In this case: The URL map selects the backend from host and path.

### Question 46 — C

Answer: Rewrite the request path before it reaches the backend. The rewrite presents the expected path to the backend. The rewrite presents the backend with the path it expects without changing the client. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: The rewrite presents the expected path to the backend.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The rewrite presents the expected path to the backend.
- **C:** Correct. The rewrite presents the backend with the path it expects without changing the client. In this case: The rewrite presents the expected path to the backend.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The rewrite presents the expected path to the backend.

### Question 47 — C

Answer: Register the serverless service as a serverless network endpoint group. A serverless endpoint group fronts the service without instance groups. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: A serverless endpoint group fronts the service without instance groups.
- **B:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: A serverless endpoint group fronts the service without instance groups.
- **C:** Correct. In this case: A serverless endpoint group fronts the service without instance groups.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: A serverless endpoint group fronts the service without instance groups.

### Question 48 — D

Answer: Register the third-party origins as an internet network endpoint group. An internet endpoint group targets the external host and port. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: An internet endpoint group targets the external host and port.
- **B:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An internet endpoint group targets the external host and port.
- **C:** Incorrect for this question. The backend service holds the health check, balancing mode and capacity settings. Why the correct answer wins: An internet endpoint group targets the external host and port.
- **D:** Correct. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. In this case: An internet endpoint group targets the external host and port.

### Question 49 — B

Answer: Expose the workload through the GKE Ingress controller. The Ingress controller builds the load balancer from one object. An Ingress object creates a Google Cloud load balancer from the manifest. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Ingress controller builds the load balancer from one object.
- **B:** Correct. An Ingress object creates a Google Cloud load balancer from the manifest. In this case: The Ingress controller builds the load balancer from one object.
- **C:** Incorrect for this question. A Gateway object configures the load balancer through the newer Kubernetes API. Why the correct answer wins: The Ingress controller builds the load balancer from one object.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The Ingress controller builds the load balancer from one object.

### Question 50 — B

Answer: Expose the workload through the GKE Gateway controller. The Gateway controller supports shared gateways and route policy. A Gateway object configures the load balancer through the newer Kubernetes API. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An Ingress object creates a Google Cloud load balancer from the manifest. Why the correct answer wins: The Gateway controller supports shared gateways and route policy.
- **B:** Correct. A Gateway object configures the load balancer through the newer Kubernetes API. In this case: The Gateway controller supports shared gateways and route policy.
- **C:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The Gateway controller supports shared gateways and route policy.
- **D:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Gateway controller supports shared gateways and route policy.

### Question 51 — A, B

Answers: Enable Cloud CDN on the backend service; Invalidate the cached object after the change. Caching shortens the fetch, and invalidation removes the stale copy. The edge holds a copy of the response so later requests are served closer to the user. Invalidation removes the stale copy so the next request fetches the current version. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Invalidation removes the stale copy so the next request fetches the current version. In this case: Caching shortens the fetch, and invalidation removes the stale copy.
- **B:** Correct. The edge holds a copy of the response so later requests are served closer to the user. In this case: Caching shortens the fetch, and invalidation removes the stale copy.
- **C:** Incorrect for this question. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. Why the correct answer wins: Caching shortens the fetch, and invalidation removes the stale copy.
- **D:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: Caching shortens the fetch, and invalidation removes the stale copy.
- **E:** Incorrect for this question. A signed URL authorises one object for a limited time without making the bucket public. Why the correct answer wins: Caching shortens the fetch, and invalidation removes the stale copy.

### Question 52 — B

Answer: Point Cloud CDN at the origins through an internet endpoint group. An internet endpoint group points the CDN at that origin. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: An internet endpoint group points the CDN at that origin.
- **B:** Correct. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. In this case: An internet endpoint group points the CDN at that origin.
- **C:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: An internet endpoint group points the CDN at that origin.
- **D:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: An internet endpoint group points the CDN at that origin.

### Question 53 — B

Answer: Apply a geolocation routing policy to the record set. Geolocation answers from the source region of the query. The answer depends on the source region of the query. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: Geolocation answers from the source region of the query.
- **B:** Correct. The answer depends on the source region of the query. In this case: Geolocation answers from the source region of the query.
- **C:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: Geolocation answers from the source region of the query.
- **D:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: Geolocation answers from the source region of the query.

### Question 54 — B, D

Answers: Create a private Cloud DNS zone; Lower the record TTL before the cutover. The private zone keeps the name internal, and the short TTL speeds the switch. The zone answers only for clients inside the authorised networks. A short TTL lets resolvers pick up the new address quickly after the change. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The private zone keeps the name internal, and the short TTL speeds the switch.
- **B:** Correct. A short TTL lets resolvers pick up the new address quickly after the change. In this case: The private zone keeps the name internal, and the short TTL speeds the switch.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The private zone keeps the name internal, and the short TTL speeds the switch.
- **D:** Correct. The zone answers only for clients inside the authorised networks. In this case: The private zone keeps the name internal, and the short TTL speeds the switch.
- **E:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: The private zone keeps the name internal, and the short TTL speeds the switch.

### Question 55 — A

Answer: Apply a failover routing policy with a health-checked primary. The failover policy keeps the standby silent until the primary fails its health check. The standby answer is served when the primary fails its health check. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy keeps the standby silent until the primary fails its health check.
- **B:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy keeps the standby silent until the primary fails its health check.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The failover policy keeps the standby silent until the primary fails its health check.
- **D:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The failover policy keeps the standby silent until the primary fails its health check.

### Question 56 — C

Answer: Apply a geolocation routing policy to the record set. Geolocation picks the answer from the query's source region. The answer depends on the source region of the query. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: Geolocation picks the answer from the query's source region.
- **B:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: Geolocation picks the answer from the query's source region.
- **C:** Correct. The answer depends on the source region of the query. In this case: Geolocation picks the answer from the query's source region.
- **D:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: Geolocation picks the answer from the query's source region.

### Question 57 — B

Answer: Enable DNSSEC on the zone. DNSSEC signatures let the resolver detect the tampering. Signatures let a resolver verify that the answer was not altered in transit. Local study-map skill 3.8 (DNSSEC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: DNSSEC signatures let the resolver detect the tampering.
- **B:** Correct. Signatures let a resolver verify that the answer was not altered in transit. In this case: DNSSEC signatures let the resolver detect the tampering.
- **C:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: DNSSEC signatures let the resolver detect the tampering.
- **D:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: DNSSEC signatures let the resolver detect the tampering.

### Question 58 — B, E

Answers: Create a VLAN attachment on Cloud Router; Set the Cloud Router ASN to a private value that differs from the peer. The VLAN attachment carries the subnet, and a distinct ASN allows the session. The attachment carries one VLAN over the interconnect and peers with the router. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The VLAN attachment carries the subnet, and a distinct ASN allows the session.
- **B:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The VLAN attachment carries the subnet, and a distinct ASN allows the session.
- **C:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: The VLAN attachment carries the subnet, and a distinct ASN allows the session.
- **D:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: The VLAN attachment carries the subnet, and a distinct ASN allows the session.
- **E:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The VLAN attachment carries the subnet, and a distinct ASN allows the session.

### Question 59 — A

Answer: Order a Dedicated Interconnect connection. Dedicated Interconnect gives the physical circuits into that facility. A private physical circuit connects the premises to a Google colocation facility. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: Dedicated Interconnect gives the physical circuits into that facility.
- **B:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: Dedicated Interconnect gives the physical circuits into that facility.
- **C:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Dedicated Interconnect gives the physical circuits into that facility.
- **D:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Dedicated Interconnect gives the physical circuits into that facility.

### Question 60 — C

Answer: Create a VLAN attachment on Cloud Router. The VLAN attachment is the router interface over the circuit. The attachment carries one VLAN over the interconnect and peers with the router. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: The VLAN attachment is the router interface over the circuit.
- **B:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: The VLAN attachment is the router interface over the circuit.
- **C:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The VLAN attachment is the router interface over the circuit.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: The VLAN attachment is the router interface over the circuit.

### Question 61 — B

Answer: Order a Partner Interconnect connection. Partner Interconnect delivers the circuit through the carrier. A service provider carries the circuit to Google on the customer behalf. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.
- **B:** Correct. A service provider carries the circuit to Google on the customer behalf. In this case: Partner Interconnect delivers the circuit through the carrier.
- **C:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.
- **D:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: Partner Interconnect delivers the circuit through the carrier.

### Question 62 — D

Answer: Order a Cross-Cloud Interconnect connection. Cross-Cloud Interconnect is a dedicated circuit to another provider. A dedicated circuit connects Google Cloud directly to another cloud provider. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **B:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **C:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **D:** Correct. A dedicated circuit connects Google Cloud directly to another cloud provider. In this case: Cross-Cloud Interconnect is a dedicated circuit to another provider.

### Question 63 — B, E

Answers: Deploy an HA VPN gateway with two interfaces; Lower the tunnel MTU to 1460 bytes. The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel. Two interfaces in different zones give the tunnel pair a 99.99% topology. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel.
- **B:** Correct. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. In this case: The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel.
- **C:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel.
- **D:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel.
- **E:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: The two-interface gateway gives redundancy, and the smaller MTU fits the tunnel.

### Question 64 — B

Answer: Deploy an HA VPN gateway with two interfaces. An HA VPN gateway places the interface pair in different zones. Two interfaces in different zones give the tunnel pair a 99.99% topology. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: An HA VPN gateway places the interface pair in different zones.
- **B:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: An HA VPN gateway places the interface pair in different zones.
- **C:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: An HA VPN gateway places the interface pair in different zones.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: An HA VPN gateway places the interface pair in different zones.

### Question 65 — C

Answer: Deploy a Classic VPN with a single tunnel. An HA VPN supplies the redundant pair the SLA requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: An HA VPN supplies the redundant pair the SLA requires.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: An HA VPN supplies the redundant pair the SLA requires.
- **C:** Correct. One tunnel gives a single path and no automatic failover. In this case: An HA VPN supplies the redundant pair the SLA requires.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: An HA VPN supplies the redundant pair the SLA requires.

### Question 66 — B

Answer: Deploy a Classic VPN with a single tunnel. Classic VPN supports the policy-based tunnel mode such a device requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.4 (Classic VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.
- **B:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports the policy-based tunnel mode such a device requires.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.

### Question 67 — B

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the dead path before the hold timer. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the dead path before the hold timer.
- **B:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the dead path before the hold timer.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: BFD detects the dead path before the hold timer.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the dead path before the hold timer.

### Question 68 — A

Answer: Set the Cloud Router ASN to a private value that differs from the peer. Two peers cannot share one autonomous system number. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: Two peers cannot share one autonomous system number.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Two peers cannot share one autonomous system number.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: Two peers cannot share one autonomous system number.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Two peers cannot share one autonomous system number.

### Question 69 — C, D

Answers: Advertise only the ranges the peer needs; Prefer the path with the lower multi-exit discriminator. The advertisement list limits the prefixes, and the discriminator keeps the secondary path second. The router advertises a chosen prefix list instead of every subnet in the VPC. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The advertisement list limits the prefixes, and the discriminator keeps the secondary path second.
- **B:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The advertisement list limits the prefixes, and the discriminator keeps the secondary path second.
- **C:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The advertisement list limits the prefixes, and the discriminator keeps the secondary path second.
- **D:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: The advertisement list limits the prefixes, and the discriminator keeps the secondary path second.
- **E:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The advertisement list limits the prefixes, and the discriminator keeps the secondary path second.

### Question 70 — C

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the degraded path sooner than the session timer. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.6 (BFD and Failover Timers), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the degraded path sooner than the session timer.
- **B:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: BFD detects the degraded path sooner than the session timer.
- **C:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the degraded path sooner than the session timer.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the degraded path sooner than the session timer.

### Question 71 — C

Answer: Switch best path selection back to the legacy behaviour. The best path selection setting decides how ties break. The older selection order picks a different preferred path when the inputs tie. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The best path selection setting decides how ties break.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The best path selection setting decides how ties break.
- **C:** Correct. The older selection order picks a different preferred path when the inputs tie. In this case: The best path selection setting decides how ties break.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The best path selection setting decides how ties break.

### Question 72 — D

Answer: Give the static route a lower priority number than the learned route. A lower priority number gives the static route precedence. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A lower priority number gives the static route precedence.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: A lower priority number gives the static route precedence.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: A lower priority number gives the static route precedence.
- **D:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: A lower priority number gives the static route precedence.

### Question 73 — A

Answer: Enable MACsec on the interconnect. MACsec encrypts the circuit itself between the premises and the Google edge. Link-layer encryption protects each hop of the circuit between the premises and Google. Local study-map skill 4.8 (Interconnect Encryption and SLA), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Link-layer encryption protects each hop of the circuit between the premises and Google. In this case: MACsec encrypts the circuit itself between the premises and the Google edge.
- **B:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: MACsec encrypts the circuit itself between the premises and the Google edge.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: MACsec encrypts the circuit itself between the premises and the Google edge.
- **D:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: MACsec encrypts the circuit itself between the premises and the Google edge.

### Question 74 — A

Answer: Enable firewall rules logging. Firewall logging records the deciding rule. The logs show which rule allowed or denied each connection. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs show which rule allowed or denied each connection. In this case: Firewall logging records the deciding rule.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Firewall logging records the deciding rule.
- **C:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: Firewall logging records the deciding rule.
- **D:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Firewall logging records the deciding rule.

### Question 75 — C

Answer: Enable Cloud DNS query logging. DNS query logging records the names and answers per query. The logs record the names that clients asked for and the answers they received. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: DNS query logging records the names and answers per query.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: DNS query logging records the names and answers per query.
- **C:** Correct. The logs record the names that clients asked for and the answers they received. In this case: DNS query logging records the names and answers per query.
- **D:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: DNS query logging records the names and answers per query.

### Question 76 — B

Answer: Create an alert policy on the network metric. An alert policy on the attachment metric raises the notification at the threshold. The policy notifies on the threshold instead of waiting for a user report. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: An alert policy on the attachment metric raises the notification at the threshold.
- **B:** Correct. The policy notifies on the threshold instead of waiting for a user report. In this case: An alert policy on the attachment metric raises the notification at the threshold.
- **C:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: An alert policy on the attachment metric raises the notification at the threshold.
- **D:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: An alert policy on the attachment metric raises the notification at the threshold.

### Question 77 — D

Answer: Publish a custom metric from the appliance. A custom metric writes the appliance's own number into Monitoring. The appliance reports a signal that no managed metric covers. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: A custom metric writes the appliance's own number into Monitoring.
- **B:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: A custom metric writes the appliance's own number into Monitoring.
- **C:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: A custom metric writes the appliance's own number into Monitoring.
- **D:** Correct. The appliance reports a signal that no managed metric covers. In this case: A custom metric writes the appliance's own number into Monitoring.

### Question 78 — C

Answer: Run a Connectivity Test between the two endpoints. A connectivity test names the blocking rule along the path. The test evaluates the configuration along the path and names the blocking rule or missing route. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A connectivity test names the blocking rule along the path.
- **B:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: A connectivity test names the blocking rule along the path.
- **C:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: A connectivity test names the blocking rule along the path.
- **D:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A connectivity test names the blocking rule along the path.

### Question 79 — C, D

Answers: Run a Connectivity Test between the two endpoints; Check the Performance Dashboard for packet loss. The test proves reachability, and the dashboard separates the loss segments. The test evaluates the configuration along the path and names the blocking rule or missing route. The dashboard separates loss on the Google network from loss outside it. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The test proves reachability, and the dashboard separates the loss segments.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The test proves reachability, and the dashboard separates the loss segments.
- **C:** Correct. The dashboard separates loss on the Google network from loss outside it. In this case: The test proves reachability, and the dashboard separates the loss segments.
- **D:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: The test proves reachability, and the dashboard separates the loss segments.
- **E:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The test proves reachability, and the dashboard separates the loss segments.

### Question 80 — D

Answer: Check the Performance Dashboard for packet loss. The performance dashboard separates Google-network loss from the rest. The dashboard separates loss on the Google network from loss outside it. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The performance dashboard separates Google-network loss from the rest.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The performance dashboard separates Google-network loss from the rest.
- **C:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: The performance dashboard separates Google-network loss from the rest.
- **D:** Correct. The dashboard separates loss on the Google network from loss outside it. In this case: The performance dashboard separates Google-network loss from the rest.

### Question 81 — B

Answer: Test the path with a large ping and the do-not-fragment bit. A large probe with do-not-fragment shows where the payload stops fitting. The probe shows where the payload stops fitting along the path. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A large probe with do-not-fragment shows where the payload stops fitting.
- **B:** Correct. The probe shows where the payload stops fitting along the path. In this case: A large probe with do-not-fragment shows where the payload stops fitting.
- **C:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A large probe with do-not-fragment shows where the payload stops fitting.
- **D:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A large probe with do-not-fragment shows where the payload stops fitting.

### Question 82 — D

Answer: Read the Network Analyzer findings. Network Analyzer reports configuration and quota risks. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Network Analyzer reports configuration and quota risks.
- **B:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Analyzer reports configuration and quota risks.
- **C:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Analyzer reports configuration and quota risks.
- **D:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Network Analyzer reports configuration and quota risks.

### Question 83 — A, C

Answers: Review Firewall Insights for shadowed rules; Read the Network Analyzer findings. Firewall Insights finds the dead rules, and the analyser reports the risks. The insight names rules that never match because a broader rule already covered them. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Firewall Insights finds the dead rules, and the analyser reports the risks.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser reports the risks.
- **C:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights finds the dead rules, and the analyser reports the risks.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser reports the risks.
- **E:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser reports the risks.

### Question 84 — A

Answer: Inspect the flow in Network Topology. Network Topology draws the running paths and their throughput. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: Network Topology draws the running paths and their throughput.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Network Topology draws the running paths and their throughput.
- **C:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Topology draws the running paths and their throughput.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Topology draws the running paths and their throughput.

### Question 85 — B

Answer: Query Flow Analyzer for the top talkers. Flow Analyzer ranks the flows by volume. The analysis ranks the flows that consume the most bandwidth. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Flow Analyzer ranks the flows by volume.
- **B:** Correct. The analysis ranks the flows that consume the most bandwidth. In this case: Flow Analyzer ranks the flows by volume.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Flow Analyzer ranks the flows by volume.
- **D:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Flow Analyzer ranks the flows by volume.

### Question 86 — D

Answer: Compare the BGP session state on both peers. Comparing both peers isolates the fault to one side. A session that is established on one side only points at the shared configuration. Local study-map skill 5.7 (BGP and VPN Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Comparing both peers isolates the fault to one side.
- **B:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Comparing both peers isolates the fault to one side.
- **C:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Comparing both peers isolates the fault to one side.
- **D:** Correct. A session that is established on one side only points at the shared configuration. In this case: Comparing both peers isolates the fault to one side.

### Question 87 — A

Answer: Drain the backend before removing it. Draining moves new flows away and lets the existing ones finish. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 5.8 (Traffic Draining and Migration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: Draining moves new flows away and lets the existing ones finish.
- **B:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Draining moves new flows away and lets the existing ones finish.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Draining moves new flows away and lets the existing ones finish.
- **D:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Draining moves new flows away and lets the existing ones finish.

### Question 88 — A

Answer: Attach a Cloud Armor backend security policy. A backend security policy can match the request origin. The policy filters traffic that has already reached the load balancer. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The policy filters traffic that has already reached the load balancer. In this case: A backend security policy can match the request origin.
- **B:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: A backend security policy can match the request origin.
- **C:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: A backend security policy can match the request origin.
- **D:** Incorrect for this question. The policy filters traffic at the edge before it is proxied to a backend. Why the correct answer wins: A backend security policy can match the request origin.

### Question 89 — A

Answer: Attach a Cloud Armor edge security policy. An edge policy drops the request before it is proxied. The policy filters traffic at the edge before it is proxied to a backend. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The policy filters traffic at the edge before it is proxied to a backend. In this case: An edge policy drops the request before it is proxied.
- **B:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: An edge policy drops the request before it is proxied.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: An edge policy drops the request before it is proxied.
- **D:** Incorrect for this question. The policy filters traffic that has already reached the load balancer. Why the correct answer wins: An edge policy drops the request before it is proxied.

### Question 90 — A

Answer: Add a preconfigured WAF rule for the attack class. A preconfigured WAF rule recognises that injection class and blocks it. The rule matches the signatures of that class of request. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The rule matches the signatures of that class of request. In this case: A preconfigured WAF rule recognises that injection class and blocks it.
- **B:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: A preconfigured WAF rule recognises that injection class and blocks it.
- **C:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: A preconfigured WAF rule recognises that injection class and blocks it.
- **D:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A preconfigured WAF rule recognises that injection class and blocks it.

### Question 91 — A

Answer: Enable bot management on the policy. Bot management classifies clients so rules can act on intent. Known bot categories are classified so the rule can allow or block them by intent. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Known bot categories are classified so the rule can allow or block them by intent. In this case: Bot management classifies clients so rules can act on intent.
- **B:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Bot management classifies clients so rules can act on intent.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Bot management classifies clients so rules can act on intent.
- **D:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Bot management classifies clients so rules can act on intent.

### Question 92 — B

Answer: Rely on the default DDoS protection and add a rate limit. Always-on DDoS protection absorbs the volume. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. Local study-map skill 6.3 (DDoS and Rate Limiting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: Always-on DDoS protection absorbs the volume.
- **B:** Correct. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. In this case: Always-on DDoS protection absorbs the volume.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Always-on DDoS protection absorbs the volume.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Always-on DDoS protection absorbs the volume.

### Question 93 — B, C

Answers: Create a hierarchical firewall policy at the organisation; Move the inspection to NGFW Enterprise. The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection. The policy applies to every project under the organisation node. The enterprise tier adds layer 7 inspection through the managed engine. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection.
- **B:** Correct. The enterprise tier adds layer 7 inspection through the managed engine. In this case: The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection.
- **C:** Correct. The policy applies to every project under the organisation node. In this case: The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection.
- **D:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection.
- **E:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The organisation policy cannot be removed locally, and the enterprise tier adds payload inspection.

### Question 94 — D

Answer: Create a global network firewall policy. The global policy covers every region of the network it is associated with. The policy is evaluated for the networks it is associated with, in every region. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The global policy covers every region of the network it is associated with.
- **B:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: The global policy covers every region of the network it is associated with.
- **C:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The global policy covers every region of the network it is associated with.
- **D:** Correct. The policy is evaluated for the networks it is associated with, in every region. In this case: The global policy covers every region of the network it is associated with.

### Question 95 — A

Answer: Create a regional network firewall policy. The regional policy is scoped to its region. The policy applies only in the region it belongs to. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The policy applies only in the region it belongs to. In this case: The regional policy is scoped to its region.
- **B:** Incorrect for this question. The policy is evaluated for the networks it is associated with, in every region. Why the correct answer wins: The regional policy is scoped to its region.
- **C:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: The regional policy is scoped to its region.
- **D:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The regional policy is scoped to its region.

### Question 96 — A

Answer: Use secure tags as the rule target. Secure tags require a privileged role to apply. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. In this case: Secure tags require a privileged role to apply.
- **B:** Incorrect for this question. Tags identify the instances the rule applies to, and any holder can set one. Why the correct answer wins: Secure tags require a privileged role to apply.
- **C:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: Secure tags require a privileged role to apply.
- **D:** Incorrect for this question. The rule applies to the instances that run as that identity, which only a privileged caller can change. Why the correct answer wins: Secure tags require a privileged role to apply.

### Question 97 — C

Answer: Add a deny-all egress rule with a higher priority. A deny-all egress rule replaces the default allow. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each tier carries a different tag and only the required flows are allowed between tiers. Why the correct answer wins: A deny-all egress rule replaces the default allow.
- **B:** Incorrect for this question. The standard tier adds the policy model and threat intelligence over the base rules. Why the correct answer wins: A deny-all egress rule replaces the default allow.
- **C:** Correct. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. In this case: A deny-all egress rule replaces the default allow.
- **D:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: A deny-all egress rule replaces the default allow.

### Question 98 — D

Answer: Use automatic Cloud NAT IP allocation. Automatic allocation adds and releases addresses as demand changes. Google assigns and releases external addresses as the demand changes. Local study-map skill 6.6 (Cloud NAT and Port Allocation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: Automatic allocation adds and releases addresses as demand changes.
- **B:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Automatic allocation adds and releases addresses as demand changes.
- **C:** Incorrect for this question. Each VM reserves a block of ports, which gives predictable capacity and predictable consumption. Why the correct answer wins: Automatic allocation adds and releases addresses as demand changes.
- **D:** Correct. Google assigns and releases external addresses as the demand changes. In this case: Automatic allocation adds and releases addresses as demand changes.

### Question 99 — C

Answer: Deploy Secure Web Proxy as the egress path. Secure Web Proxy applies URL and TLS policy to outbound traffic. Local study-map skill 6.7 (Secure Web Proxy), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **B:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **C:** Correct. In this case: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **D:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.

### Question 100 — D

Answer: Configure Packet Mirroring on the instance group. Packet Mirroring copies the traffic and leaves the path untouched. Mirrored packets are delivered to the collector for analysis. Local study-map skill 6.8 (Multi-NIC Appliances and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy applies URL and TLS inspection policy to outbound traffic. Why the correct answer wins: Packet Mirroring copies the traffic and leaves the path untouched.
- **B:** Incorrect for this question. A copy of the traffic goes to a collector while the original flow continues untouched. Why the correct answer wins: Packet Mirroring copies the traffic and leaves the path untouched.
- **C:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Packet Mirroring copies the traffic and leaves the path untouched.
- **D:** Correct. Mirrored packets are delivered to the collector for analysis. In this case: Packet Mirroring copies the traffic and leaves the path untouched.
