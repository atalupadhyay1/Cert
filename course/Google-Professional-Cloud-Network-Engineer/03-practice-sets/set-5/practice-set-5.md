# Google Cloud Professional Cloud Network Engineer — Full-Length Mock Exam 5

Professional Cloud Network Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing and Planning a Google Cloud VPC Network (VPC Design, IP Planning, and Load Balancer Choice)

### 1. A hospital group in three countries runs appointment booking from one region and clinicians notice the delay. What should the front end use?

- A. Deploy a regional external Application Load Balancer
- B. Use the Standard network service tier
- C. Enable Cloud CDN on the backend service
- D. Use the Premium network service tier

### 2. A university's archive is read only by its own city and the grant covers a fixed egress budget. What should the front end use?

- A. Use an external proxy Network Load Balancer with TLS termination
- B. Use the Premium network service tier
- C. Assign a manual static Cloud NAT address
- D. Use the Standard network service tier

### 3. During a drill, traffic kept arriving at a pool whose instances had all crashed. What would have removed it automatically?

- A. Switch the balancing mode to connections per instance
- B. Attach a health check to the backend service
- C. Enable connection draining with a timeout
- D. Enable session affinity on the backend service

### 4. A logistics platform needs one address for both continents and a clean way to empty one continent. Which two components fit? Select two.

- A. Deploy an internal passthrough Network Load Balancer
- B. Drain the backend before removing it
- C. Enable session affinity on the backend service
- D. Deploy a global external Application Load Balancer
- E. Deploy a regional external Application Load Balancer

### 5. A retailer's datacentre resolvers must look up names that only exist in Cloud DNS. What gives them somewhere to send queries?

- A. Serve split-horizon answers from separate private and public zones
- B. Configure a DNS forwarding policy for the on-premises domain
- C. Create an inbound forwarding policy with a forwarding address
- D. Create a DNS peering zone to the other project

### 6. A media company's build agents must resolve a supplier domain held by the supplier's own resolvers. What should be configured?

- A. Create an inbound forwarding policy with a forwarding address
- B. Configure a DNS forwarding policy for the on-premises domain
- C. Enable DNSSEC on the zone
- D. Create a DNS peering zone to the other project

### 7. A payroll system must be callable by other workloads and by nothing on the internet. Which front end fits?

- A. Use a passthrough Network Load Balancer
- B. Use a proxy Network Load Balancer
- C. Deploy a global external Application Load Balancer
- D. Deploy an internal passthrough Network Load Balancer

### 8. A gRPC service needs each request balanced separately and TLS ended at the front end. Which shape fits?

- A. Route by URL path in the URL map
- B. Deploy an internal passthrough Network Load Balancer
- C. Use a passthrough Network Load Balancer
- D. Use a proxy Network Load Balancer

### 9. A planner must prove that pod addresses come from somewhere other than the node subnet. What provides that separation?

- A. Expand the existing subnet range
- B. Plan secondary ranges for pods and services
- C. Add a second pod range to the cluster
- D. Create a GKE network policy for the namespace

### 10. A bank's cluster API is public but only the build network may touch it. What should be configured?

- A. Use the DNS-based control plane endpoint
- B. Use a private control plane endpoint
- C. Add the office range to the authorised networks
- D. Use private nodes with no external addresses

### 11. A manufacturer's nodes must hold no public address, and policy must be enforced inside the cluster dataplane. Which two settings fit? Select two.

- A. Use private nodes with no external addresses
- B. Create a GKE network policy for the namespace
- C. Add the office range to the authorised networks
- D. Configure an IP masquerade policy on the node pool
- E. Enable GKE Dataplane V2

### 12. A telco's central team must own every network and subnet object in the host project. Which role fits?

- A. Grant the basic editor role to the automation
- B. Grant the network administrator role in the host project
- C. Create a custom role with only the required network permissions
- D. Grant the subnet user role on the specific shared subnets

### 13. A security team wants an automation that can only read firewall policy, and a platform team that attaches new projects. Which two grants fit? Select two.

- A. Grant the subnet user role on the specific shared subnets
- B. Grant the network administrator role in the host project
- C. Grant the basic editor role to the automation
- D. Create a custom role with only the required network permissions
- E. Grant Shared VPC Admin on the host project

### 14. A managed search service must be provisioned with an address inside the company's own network. What must exist first?

- A. Allocate a private services access range
- B. Enable Private Google Access on the subnet
- C. Attach the service to Serverless VPC Access
- D. Create a Private Service Connect endpoint

### 15. An insurer must consume a partner's published service privately and let a serverless job reach an internal API. Which two mechanisms fit? Select two.

- A. Reach the API through its public interface
- B. Enable Private Google Access on the subnet
- C. Allocate a private services access range
- D. Create a Private Service Connect endpoint
- E. Attach the service to Serverless VPC Access

### 16. A supermarket chain's branch networks must reach the central network but not one another. What topology fits?

- A. Peer every VPC network with every other VPC network
- B. Connect the VPC networks through a Network Connectivity Center hub
- C. Connect the networks as a hub-and-spoke peering topology
- D. Build the network as a Shared VPC with host and service projects

### 17. Three research networks of equal standing must all reach each other and no central network exists. What topology fits?

- A. Create a VPC Network Peering connection between the two networks
- B. Peer every VPC network with every other VPC network
- C. Connect the networks as a hub-and-spoke peering topology
- D. Connect the VPC networks through a Network Connectivity Center hub

### 18. A merger left two factories using the same 10.0.0.0/8 and neither will renumber. What fits?

- A. Deploy Private NAT for the overlapping ranges
- B. Use privately used public IP address ranges
- C. Accept the overlapping subnet ranges as configured
- D. Use non-RFC 1918 space for the internal network

### 19. A broadcaster's existing public prefixes must now be served from Google Cloud. What fits?

- A. Use non-RFC 1918 space for the internal network
- B. Bring your own public IP prefixes
- C. Automate address allocation from a central IPAM plan
- D. Use privately used public IP address ranges

### 20. A database migration succeeds within a zone and stalls at a fixed point across a new tunnel, with no error. What is wrong?

- A. Leave the MTU mismatch unfixed
- B. Keep the default 1500-byte MTU
- C. Lower the tunnel MTU to 1460 bytes
- D. Raise the VPC MTU to 8896 bytes

### 21. A government agency must inspect traffic between two estates that cannot be peered. What should be deployed?

- A. Create a static route with a tag-scoped next hop
- B. Add a policy-based route that matches the source and destination
- C. Use the internal load balancer as the next hop
- D. Deploy a multi-NIC appliance VM between the two networks

---

## Domain 2 — Implementing a VPC Network (VPC Implementation, Routing, and GKE Networking)

### 22. An airline's subnet must gain addresses while its running instances keep theirs. What should be done?

- A. Use privately used public IP address ranges
- B. Expand the existing subnet range
- C. Accept the overlapping subnet ranges as configured
- D. Enable dual-stack IPv6 on the subnet

### 23. A gaming operator's subnet needs more IPv4 addresses and its platform must also answer over IPv6. Which two changes fit? Select two.

- A. Expand the existing subnet range
- B. Use privately used public IP address ranges
- C. Enable dual-stack IPv6 on the subnet
- D. Bring your own public IP prefixes
- E. Accept the overlapping subnet ranges as configured

### 24. A partner reaches its direct peer but never that peer's other partner. What explains the gap?

- A. Assume peered networks can reach each other transitively
- B. Peer every VPC network with every other VPC network
- C. Connect the VPC networks through a Network Connectivity Center hub
- D. Create a VPC Network Peering connection between the two networks

### 25. A startup needs a direct path to one corporate network and nothing else. What provides it?

- A. Connect the VPC networks through a Network Connectivity Center hub
- B. Build the network as a Shared VPC with host and service projects
- C. Create a VPC Network Peering connection between the two networks
- D. Peer every VPC network with every other VPC network

### 26. A charity's service project is refused when it tries to deploy into the shared subnet it was given. What should be granted?

- A. Grant the subnet user role on the specific shared subnets
- B. Grant Shared VPC Admin on the host project
- C. Grant the basic editor role to the automation
- D. Grant the network administrator role in the host project

### 27. A council wants one address plan across departments, with each department confined to its own subnet. Which two choices fit? Select two.

- A. Grant the subnet user role on the specific shared subnets
- B. Build the network as a Shared VPC with host and service projects
- C. Grant the basic editor role to the automation
- D. Give each team its own standalone VPC network
- E. Grant the network administrator role in the host project

### 28. A defence contractor's fleet holds no external addresses and must still call Google APIs. What should be enabled?

- A. Create a Private Service Connect endpoint
- B. Attach the service to Serverless VPC Access
- C. Reach the API through its public interface
- D. Enable Private Google Access on the subnet

### 29. A bank's customer records must not be readable from a project outside its approved group. What should be configured?

- A. Enable Private Google Access on the subnet
- B. Review Firewall Insights for shadowed rules
- C. Create a hierarchical firewall policy at the organisation
- D. Enclose the project in a VPC Service Controls perimeter

### 30. A local static route must win over an imported route for one prefix. What decides that?

- A. Give the static route a lower priority number than the learned route
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Prefer the path with the lower multi-exit discriminator
- D. Set the Cloud Router ASN to a private value that differs from the peer

### 31. A privacy ruling forbids reusing a route learned in one jurisdiction from another. What should be confirmed?

- A. Advertise only the ranges the peer needs
- B. Prefer the path with the lower multi-exit discriminator
- C. Keep the Cloud Router in regional dynamic routing mode
- D. Switch the Cloud Router to global dynamic routing mode

### 32. A single router serves three countries, and a dead path must be abandoned quickly. Which two settings fit? Select two.

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Keep the Cloud Router in regional dynamic routing mode
- C. Prefer the path with the lower multi-exit discriminator
- D. Switch the Cloud Router to global dynamic routing mode
- E. Enable Bidirectional Forwarding Detection with a short interval

### 33. Only one supplier's address range must be inspected while everything else goes straight out. What fits?

- A. Add a policy-based route that matches the source and destination
- B. Use the internal load balancer as the next hop
- C. Deploy a multi-NIC appliance VM between the two networks
- D. Create a static route with a tag-scoped next hop

### 34. Only the cardholder-data instances must use the inspection path. What should be created?

- A. Create a static route with a tag-scoped next hop
- B. Give the static route a lower priority number than the learned route
- C. Add a policy-based route that matches the source and destination
- D. Use the internal load balancer as the next hop

### 35. An appliance instance is rebuilt every week and the route table must not change. What should the next hop be?

- A. Add a policy-based route that matches the source and destination
- B. Create a static route with a tag-scoped next hop
- C. Use the internal load balancer as the next hop
- D. Deploy a multi-NIC appliance VM between the two networks

### 36. A spoke in the hub must publish three warehouse blocks while hiding the rest of its network. What should be applied to it?

- A. Add the attachment as a hybrid spoke
- B. Add the VPC network as a VPC spoke
- C. Expect spoke-to-spoke reachability through the hub
- D. Apply a CIDR range filter to the spoke

### 37. Traffic between two attached offices has to cross the hub rather than hairpin through the internet. What makes that possible?

- A. Expect spoke-to-spoke reachability through the hub
- B. Add the published service as a producer spoke
- C. Apply a CIDR range filter to the spoke
- D. Add the VPC network as a VPC spoke

### 38. Kubernetes reports that no more service addresses can be allocated, even though pods keep starting. Which range needs attention?

- A. Plan secondary ranges for pods and services
- B. Add a second pod range to the cluster
- C. Create a GKE network policy for the namespace
- D. Resize the service range allocation

### 39. A partner firewall rejects pod addresses that it was never told about. What should be configured?

- A. Configure an IP masquerade policy on the node pool
- B. Enable GKE Dataplane V2
- C. Create a GKE network policy for the namespace
- D. Add a second pod range to the cluster

### 40. Only the checkout namespace may reach the payment pods. What should be created?

- A. Add a second pod range to the cluster
- B. Enable GKE Dataplane V2
- C. Create a GKE network policy for the namespace
- D. Configure an IP masquerade policy on the node pool

### 41. A quarterly report must show how many bytes each subnet sent. What should be enabled?

- A. Enable firewall rules logging
- B. Enable Cloud DNS query logging
- C. Enable VPC Flow Logs on the subnet
- D. Enable Cloud NAT logging

---

## Domain 3 — Configuring Managed Network Services (Load Balancing, Cloud CDN, and Cloud DNS)

### 42. A pool must shed members that stop answering, and the group must grow as demand rises. Which two components fit? Select two.

- A. Enable connection draining with a timeout
- B. Autoscale a managed instance group behind the backend service
- C. Enable session affinity on the backend service
- D. Register the backends as a zonal network endpoint group
- E. Attach a health check to the backend service

### 43. Shoppers lose their cart when the front end picks a different backend mid-session. What should be enabled?

- A. Register the backends as a zonal network endpoint group
- B. Enable connection draining with a timeout
- C. Switch the balancing mode to connections per instance
- D. Enable session affinity on the backend service

### 44. Pods must appear as backends without any instance group existing. What should be used?

- A. Register the backends as a zonal network endpoint group
- B. Register the serverless service as a serverless network endpoint group
- C. Autoscale a managed instance group behind the backend service
- D. Register the third-party origins as an internet network endpoint group

### 45. A twentieth of production traffic must reach the replacement backend before it launches. What should be configured?

- A. Rewrite the request path before it reaches the backend
- B. Route by URL path in the URL map
- C. Split traffic between two backend services by weight
- D. Mirror a copy of the traffic to a second backend

### 46. A replacement backend must see live requests without answering any of them. What should be configured?

- A. Rewrite the request path before it reaches the backend
- B. Route by URL path in the URL map
- C. Mirror a copy of the traffic to a second backend
- D. Split traffic between two backend services by weight

### 47. A mainframe application in the datacentre must be a backend behind the front end. What should be created?

- A. Register the backends as a zonal network endpoint group
- B. Register the serverless service as a serverless network endpoint group
- C. Add the backends to a backend service behind the front end
- D. Register the third-party origins as an internet network endpoint group

### 48. The instance count must follow request volume instead of a fixed number. What should be attached?

- A. Switch the balancing mode to connections per instance
- B. Autoscale a managed instance group behind the backend service
- C. Register the serverless service as a serverless network endpoint group
- D. Register the backends as a zonal network endpoint group

### 49. Six product teams must share one entry point with separate route policy. What fits?

- A. Split traffic between two backend services by weight
- B. Expose the workload through the GKE Ingress controller
- C. Expose the workload through the GKE Gateway controller
- D. Route by URL path in the URL map

### 50. A two-person team wants a public entry point created from one Kubernetes object with no extra controller. What fits?

- A. Route by URL path in the URL map
- B. Expose the workload through the GKE Ingress controller
- C. Register the backends as a zonal network endpoint group
- D. Expose the workload through the GKE Gateway controller

### 51. Origin bandwidth must fall, and the catalogue behind it changes once a day. Which two settings fit? Select two.

- A. Invalidate the cached object after the change
- B. Point Cloud CDN at the origins through an internet endpoint group
- C. Raise the cache time to live
- D. Enable Cloud CDN on the backend service
- E. Serve the object through a signed URL

### 52. An auditor must be able to download a filing only through a link that dies in ten minutes. What should be used?

- A. Serve the object through a signed URL
- B. Raise the cache time to live
- C. Invalidate the cached object after the change
- D. Enable Cloud CDN on the backend service

### 53. An internal hostname must resolve only inside one project and never on the internet. Which zone fits?

- A. Create a public Cloud DNS zone
- B. Serve split-horizon answers from separate private and public zones
- C. Create a private Cloud DNS zone
- D. Enable DNSSEC on the zone

### 54. A cutover must switch within minutes, and a second project must resolve the name privately. Which two settings fit? Select two.

- A. Create a DNS peering zone to the other project
- B. Create a public Cloud DNS zone
- C. Migrate the zone with a staged import and a delegated test
- D. Enable DNSSEC on the zone
- E. Lower the record TTL before the cutover

### 55. Each country must be answered with the address of its own cluster. Which policy fits?

- A. Apply a geolocation routing policy to the record set
- B. Apply a failover routing policy with a health-checked primary
- C. Enable DNSSEC on the zone
- D. Lower the record TTL before the cutover

### 56. A warm standby must answer only while the primary fails its health check. Which policy fits?

- A. Enable DNSSEC on the zone
- B. Migrate the zone with a staged import and a delegated test
- C. Apply a failover routing policy with a health-checked primary
- D. Apply a geolocation routing policy to the record set

### 57. A resolver must be able to tell a forged public answer from a real one. What should be enabled?

- A. Enable DNSSEC on the zone
- B. Enable Cloud DNS query logging
- C. Create a private Cloud DNS zone
- D. Migrate the zone with a staged import and a delegated test

---

## Domain 4 — Configuring and Implementing Hybrid and Multicloud Interconnectivity (Interconnect, VPN, and Cloud Router)

### 58. A shipping company occupies its own cage in a Google facility and needs one subnet carried to its router. Which two items fit? Select two.

- A. Order a Dedicated Interconnect connection
- B. Create a VLAN attachment on Cloud Router
- C. Order a Cross-Cloud Interconnect connection
- D. Enable MACsec on the interconnect
- E. Order a Partner Interconnect connection

### 59. A factory needs a circuit within a month and a carrier already serves the industrial park. Which fits?

- A. Deploy an HA VPN gateway with two interfaces
- B. Order a Cross-Cloud Interconnect connection
- C. Order a Partner Interconnect connection
- D. Order a Dedicated Interconnect connection

### 60. A new attachment stays idle and both ends are configured as 65001. What must change?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Prefer the path with the lower multi-exit discriminator
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Create a VLAN attachment on Cloud Router

### 61. An analytics team must copy datasets to a second cloud without touching the internet. Which fits?

- A. Order a Cross-Cloud Interconnect connection
- B. Deploy a Classic VPN with a single tunnel
- C. Order a Partner Interconnect connection
- D. Order a Dedicated Interconnect connection

### 62. A payments company requires encryption at the link layer on its circuit, and its hardware supports it. What should be enabled?

- A. Deploy an HA VPN gateway with two interfaces
- B. Enable MACsec on the interconnect
- C. Create a VLAN attachment on Cloud Router
- D. Run HA VPN over Cloud Interconnect instead of MACsec

### 63. A remote plant needs two tunnels that survive a zone failure, and a dead tunnel must be noticed in seconds. Which two settings fit? Select two.

- A. Deploy an HA VPN gateway with two interfaces
- B. Lower the tunnel MTU to 1460 bytes
- C. Create a VLAN attachment on Cloud Router
- D. Enable Bidirectional Forwarding Detection with a short interval
- E. Deploy a Classic VPN with a single tunnel

### 64. A branch must keep working when one VPN gateway zone is lost. What should be deployed?

- A. Order a Dedicated Interconnect connection
- B. Deploy an HA VPN gateway with two interfaces
- C. Deploy a Classic VPN with a single tunnel
- D. Create a VLAN attachment on Cloud Router

### 65. Replication over a freshly built tunnel stalls on large writes but small ones succeed. What should be adjusted?

- A. Keep the default 1500-byte MTU
- B. Leave the MTU mismatch unfixed
- C. Raise the VPC MTU to 8896 bytes
- D. Lower the tunnel MTU to 1460 bytes

### 66. A legacy router can only select traffic by policy and cannot speak BGP. Which VPN fits?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Deploy a Classic VPN with a single tunnel
- C. Order a Dedicated Interconnect connection
- D. Deploy an HA VPN gateway with two interfaces

### 67. Two circuits advertise one prefix and the standby must stay standby. What should be set?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Switch best path selection back to the legacy behaviour
- D. Prefer the path with the lower multi-exit discriminator

### 68. The carrier must see two summaries instead of forty subnets. What should be configured?

- A. Advertise only the ranges the peer needs
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Give the static route a lower priority number than the learned route
- D. Enable Bidirectional Forwarding Detection with a short interval

### 69. A session will not come up, and the carrier must be told about two summaries only. Which two settings fit? Select two.

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Advertise only the ranges the peer needs
- D. Prefer the path with the lower multi-exit discriminator
- E. Switch best path selection back to the legacy behaviour

### 70. A satellite hop degrades and BGP still believes the session is healthy. What should be enabled?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Give the static route a lower priority number than the learned route
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Prefer the path with the lower multi-exit discriminator

### 71. A route learned in one region must serve subnets in another region. What should change?

- A. Give the static route a lower priority number than the learned route
- B. Keep the Cloud Router in regional dynamic routing mode
- C. Switch the Cloud Router to global dynamic routing mode
- D. Prefer the path with the lower multi-exit discriminator

### 72. An upgrade changed the preferred path even though no advertisement changed. What should be reviewed?

- A. Give the static route a lower priority number than the learned route
- B. Switch best path selection back to the legacy behaviour
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Prefer the path with the lower multi-exit discriminator

### 73. The circuit cannot encrypt at the link layer and encryption is mandatory. What should run over it?

- A. Create a VLAN attachment on Cloud Router
- B. Enable MACsec on the interconnect
- C. Run HA VPN over Cloud Interconnect instead of MACsec
- D. Deploy an HA VPN gateway with two interfaces

---

## Domain 5 — Managing, Monitoring, and Troubleshooting Network Operations (Observability, Troubleshooting, and Traffic Movement)

### 74. An abuse report needs the public address and port that a private host used. What should be enabled?

- A. Enable Cloud DNS query logging
- B. Enable firewall rules logging
- C. Enable Cloud NAT logging
- D. Enable VPC Flow Logs on the subnet

### 75. A tunnel renegotiates every hour and the cause must be found. What should be enabled?

- A. Enable VPC Flow Logs on the subnet
- B. Enable firewall rules logging
- C. Enable Cloud DNS query logging
- D. Enable Cloud VPN logging

### 76. A firewall appliance publishes its own session table depth, and the team wants it charted and alerted. What should be created?

- A. Create a log-based metric from the firewall log entries
- B. Alert on the error budget of the service objective
- C. Create an alert policy on the network metric
- D. Publish a custom metric from the appliance

### 77. A front end must page somebody when its error rate crosses a threshold. What should be created?

- A. Alert on the error budget of the service objective
- B. Create a log-based metric from the firewall log entries
- C. Publish a custom metric from the appliance
- D. Create an alert policy on the network metric

### 78. A change window needs proof that a path works before and after the change. What should be run?

- A. Inspect the flow in Network Topology
- B. Run a Connectivity Test between the two endpoints
- C. Check the Performance Dashboard for packet loss
- D. Query Flow Analyzer for the top talkers

### 79. A path must be proved, and the flow that uses it must be documented afterwards. Which two tools fit? Select two.

- A. Query Flow Analyzer for the top talkers
- B. Enable Cloud DNS query logging
- C. Inspect the flow in Network Topology
- D. Check the Performance Dashboard for packet loss
- E. Run a Connectivity Test between the two endpoints

### 80. Loss must be attributed either to the Google network or to the carrier. What separates the two?

- A. Check the Performance Dashboard for packet loss
- B. Test the path with a large ping and the do-not-fragment bit
- C. Inspect the flow in Network Topology
- D. Query Flow Analyzer for the top talkers

### 81. A tunnel passes small packets and drops large ones with no error. What should be tested?

- A. Inspect the flow in Network Topology
- B. Leave the MTU mismatch unfixed
- C. Check the Performance Dashboard for packet loss
- D. Test the path with a large ping and the do-not-fragment bit

### 82. A rule that never matched anything must be found. What should be reviewed?

- A. Run a Connectivity Test between the two endpoints
- B. Read the Network Analyzer findings
- C. Query Flow Analyzer for the top talkers
- D. Review Firewall Insights for shadowed rules

### 83. Before a quarterly change freeze, dead firewall rules must be removed and configurations that risk an outage found. Which two tools fit? Select two.

- A. Enable Cloud DNS query logging
- B. Run a Connectivity Test between the two endpoints
- C. Read the Network Analyzer findings
- D. Review Firewall Insights for shadowed rules
- E. Query Flow Analyzer for the top talkers

### 84. The heaviest destinations must be ranked before a cost review. What should be queried?

- A. Inspect the flow in Network Topology
- B. Review Firewall Insights for shadowed rules
- C. Check the Performance Dashboard for packet loss
- D. Query Flow Analyzer for the top talkers

### 85. The running path must be compared with the intended diagram. What shows the running path?

- A. Query Flow Analyzer for the top talkers
- B. Run a Connectivity Test between the two endpoints
- C. Check the Performance Dashboard for packet loss
- D. Inspect the flow in Network Topology

### 86. Prefixes arrive on one peer and never appear on the other. What should be compared?

- A. Run a Connectivity Test between the two endpoints
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Compare the BGP session state on both peers
- D. Prefer the path with the lower multi-exit discriminator

### 87. A load balancer is being replaced with its successor and the long-running uploads on it must finish. What should happen first?

- A. Query Flow Analyzer for the top talkers
- B. Inspect the flow in Network Topology
- C. Drain the backend before removing it
- D. Enable connection draining with a timeout

---

## Domain 6 — Configuring, Implementing, and Managing a Cloud Network Security Solution (Cloud Armor, Cloud NGFW, NAT, and Egress Security)

### 88. A backend must accept traffic from two countries and refuse the rest. What should be attached?

- A. Add a preconfigured WAF rule for the attack class
- B. Attach a Cloud Armor backend security policy
- C. Enable Adaptive Protection
- D. Attach a Cloud Armor edge security policy

### 89. A blocklist of countries has to be enforced as early as possible, before any proxy work is done. What should be attached?

- A. Add a rate-based ban rule
- B. Attach a Cloud Armor edge security policy
- C. Attach a Cloud Armor backend security policy
- D. Enable bot management on the policy

### 90. Attack patterns change every week and nobody can write rules in time. What should be enabled?

- A. Add a preconfigured WAF rule for the attack class
- B. Enable Adaptive Protection
- C. Apply Google Threat Intelligence lists
- D. Enable bot management on the policy

### 91. Requests arrive from addresses already listed as malicious infrastructure. What should be applied?

- A. Enable Adaptive Protection
- B. Apply Google Threat Intelligence lists
- C. Add a preconfigured WAF rule for the attack class
- D. Enable bot management on the policy

### 92. One client hammers the login endpoint and must be blocked for ten minutes. What fits?

- A. Enable Adaptive Protection
- B. Rely on the default DDoS protection and add a rate limit
- C. Add a rate-based ban rule
- D. Apply Google Threat Intelligence lists

### 93. Rules must apply in every region of a network and payloads must be inspected. Which two choices fit? Select two.

- A. Create a regional network firewall policy
- B. Reorder the rules by priority
- C. Move the inspection to NGFW Enterprise
- D. Create a VPC firewall rule with a target tag
- E. Create a global network firewall policy

### 94. A baseline rule must cover every project and must resist removal by a project owner. What fits?

- A. Reorder the rules by priority
- B. Create a VPC firewall rule with a target tag
- C. Create a regional network firewall policy
- D. Create a hierarchical firewall policy at the organisation

### 95. A residency rule means inspection policy for one region must not be inherited by another. Which policy scope satisfies that?

- A. Create a regional network firewall policy
- B. Create a VPC firewall rule with a target tag
- C. Create a global network firewall policy
- D. Create a hierarchical firewall policy at the organisation

### 96. Every workload can reach every other workload today. What should be designed?

- A. Reorder the rules by priority
- B. Move the inspection to NGFW Enterprise
- C. Divide the network into micro-segmented tiers
- D. Leave the default allow-ingress rule in place

### 97. Instances can reach anywhere today and only three hosts are allowed. What should be created?

- A. Add a deny-all egress rule with a higher priority
- B. Move the rules to NGFW Standard
- C. Leave the default allow-ingress rule in place
- D. Divide the network into micro-segmented tiers

### 98. A shared NAT pool must survive short bursts from many instances at once. What fits?

- A. Assign a manual static Cloud NAT address
- B. Use dynamic port allocation
- C. Use automatic Cloud NAT IP allocation
- D. Use static port allocation

### 99. Outbound traffic must be blocked by URL category. What fits?

- A. Use dynamic port allocation
- B. Deploy Secure Web Proxy as the egress path
- C. Assign a manual static Cloud NAT address
- D. Configure Packet Mirroring on the instance group

### 100. A collector must receive copies from several estates with no inline device. What fits?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Inspect the traffic out of band with Packet Mirroring
- C. Use the internal load balancer as the next hop
- D. Configure Packet Mirroring on the instance group

---

## Answer key and explanations

### Question 1 — D

Answer: Use the Premium network service tier. Premium hands each clinician to the nearest edge and keeps the path on the Google network. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: Premium hands each clinician to the nearest edge and keeps the path on the Google network.
- **B:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: Premium hands each clinician to the nearest edge and keeps the path on the Google network.
- **C:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: Premium hands each clinician to the nearest edge and keeps the path on the Google network.
- **D:** Correct. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. In this case: Premium hands each clinician to the nearest edge and keeps the path on the Google network.

### Question 2 — D

Answer: Use the Standard network service tier. Standard sends the long haul over the public internet, which is cheaper for that readership. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates TLS and forwards a separate connection to the backend. Why the correct answer wins: Standard sends the long haul over the public internet, which is cheaper for that readership.
- **B:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: Standard sends the long haul over the public internet, which is cheaper for that readership.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Standard sends the long haul over the public internet, which is cheaper for that readership.
- **D:** Correct. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. In this case: Standard sends the long haul over the public internet, which is cheaper for that readership.

### Question 3 — B

Answer: Attach a health check to the backend service. A health check takes a pool that cannot answer out of service. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: A health check takes a pool that cannot answer out of service.
- **B:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: A health check takes a pool that cannot answer out of service.
- **C:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: A health check takes a pool that cannot answer out of service.
- **D:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: A health check takes a pool that cannot answer out of service.

### Question 4 — B, D

Answers: Deploy a global external Application Load Balancer; Drain the backend before removing it. The global address reaches either continent, and draining empties the one being withdrawn. A global anycast address routes each user to the closest healthy region. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: The global address reaches either continent, and draining empties the one being withdrawn.
- **B:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: The global address reaches either continent, and draining empties the one being withdrawn.
- **C:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: The global address reaches either continent, and draining empties the one being withdrawn.
- **D:** Correct. A global anycast address routes each user to the closest healthy region. In this case: The global address reaches either continent, and draining empties the one being withdrawn.
- **E:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: The global address reaches either continent, and draining empties the one being withdrawn.

### Question 5 — C

Answer: Create an inbound forwarding policy with a forwarding address. An inbound forwarding policy publishes an address those resolvers can reach. On-premises resolvers send queries to that address to reach Cloud DNS names. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: An inbound forwarding policy publishes an address those resolvers can reach.
- **B:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: An inbound forwarding policy publishes an address those resolvers can reach.
- **C:** Correct. On-premises resolvers send queries to that address to reach Cloud DNS names. In this case: An inbound forwarding policy publishes an address those resolvers can reach.
- **D:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: An inbound forwarding policy publishes an address those resolvers can reach.

### Question 6 — B

Answer: Configure a DNS forwarding policy for the on-premises domain. A forwarding policy sends that domain to the resolvers that hold it. Queries for the corporate suffix are forwarded to the on-premises resolvers. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. On-premises resolvers send queries to that address to reach Cloud DNS names. Why the correct answer wins: A forwarding policy sends that domain to the resolvers that hold it.
- **B:** Correct. Queries for the corporate suffix are forwarded to the on-premises resolvers. In this case: A forwarding policy sends that domain to the resolvers that hold it.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A forwarding policy sends that domain to the resolvers that hold it.
- **D:** Incorrect for this question. The consumer project resolves names from the producer project through a peering zone. Why the correct answer wins: A forwarding policy sends that domain to the resolvers that hold it.

### Question 7 — D

Answer: Deploy an internal passthrough Network Load Balancer. An internal front end publishes no public address at all. The front end is an internal address reachable only from inside the VPC or its connected networks. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: An internal front end publishes no public address at all.
- **B:** Incorrect for this question. The proxy terminates the client connection and opens a separate one to the backend. Why the correct answer wins: An internal front end publishes no public address at all.
- **C:** Incorrect for this question. A global anycast address routes each user to the closest healthy region. Why the correct answer wins: An internal front end publishes no public address at all.
- **D:** Correct. The front end is an internal address reachable only from inside the VPC or its connected networks. In this case: An internal front end publishes no public address at all.

### Question 8 — D

Answer: Use a proxy Network Load Balancer. A proxy terminates TLS and balances the requests behind it. The proxy terminates the client connection and opens a separate one to the backend. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: A proxy terminates TLS and balances the requests behind it.
- **B:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: A proxy terminates TLS and balances the requests behind it.
- **C:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: A proxy terminates TLS and balances the requests behind it.
- **D:** Correct. The proxy terminates the client connection and opens a separate one to the backend. In this case: A proxy terminates TLS and balances the requests behind it.

### Question 9 — B

Answer: Plan secondary ranges for pods and services. Secondary ranges give pods their own address space beside the node subnet. Alias ranges give pods and services addresses that are separate from the node subnet. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A subnet prefix can grow within its address range, and the growth cannot shrink later. Why the correct answer wins: Secondary ranges give pods their own address space beside the node subnet.
- **B:** Correct. Alias ranges give pods and services addresses that are separate from the node subnet. In this case: Secondary ranges give pods their own address space beside the node subnet.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Secondary ranges give pods their own address space beside the node subnet.
- **D:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: Secondary ranges give pods their own address space beside the node subnet.

### Question 10 — C

Answer: Add the office range to the authorised networks. Authorised networks admit the named ranges and refuse everything else. The named range may reach the control plane endpoint even when it is public. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The endpoint resolves through a private DNS name instead of a fixed address. Why the correct answer wins: Authorised networks admit the named ranges and refuse everything else.
- **B:** Incorrect for this question. The API server is reachable only through the internal address or an authorised network. Why the correct answer wins: Authorised networks admit the named ranges and refuse everything else.
- **C:** Correct. The named range may reach the control plane endpoint even when it is public. In this case: Authorised networks admit the named ranges and refuse everything else.
- **D:** Incorrect for this question. Nodes reach the control plane and Google APIs through internal paths only. Why the correct answer wins: Authorised networks admit the named ranges and refuse everything else.

### Question 11 — A, E

Answers: Use private nodes with no external addresses; Enable GKE Dataplane V2. Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane. Nodes reach the control plane and Google APIs through internal paths only. The eBPF dataplane handles policy and service routing inside the cluster. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Nodes reach the control plane and Google APIs through internal paths only. In this case: Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane.
- **B:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane.
- **C:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane.
- **D:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane.
- **E:** Correct. The eBPF dataplane handles policy and service routing inside the cluster. In this case: Private nodes remove the public node addresses, and Dataplane V2 enforces policy in the dataplane.

### Question 12 — B

Answer: Grant the network administrator role in the host project. The network administrator role owns network and subnet objects. That role creates and changes networks and subnets, which a service team should not hold. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: The network administrator role owns network and subnet objects.
- **B:** Correct. That role creates and changes networks and subnets, which a service team should not hold. In this case: The network administrator role owns network and subnet objects.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: The network administrator role owns network and subnet objects.
- **D:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: The network administrator role owns network and subnet objects.

### Question 13 — D, E

Answers: Create a custom role with only the required network permissions; Grant Shared VPC Admin on the host project. A custom role holds just the read permission, and the admin role attaches service projects. The custom role names the exact permissions the automation needs. That role attaches service projects and delegates subnet use. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: A custom role holds just the read permission, and the admin role attaches service projects.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: A custom role holds just the read permission, and the admin role attaches service projects.
- **C:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: A custom role holds just the read permission, and the admin role attaches service projects.
- **D:** Correct. The custom role names the exact permissions the automation needs. In this case: A custom role holds just the read permission, and the admin role attaches service projects.
- **E:** Correct. That role attaches service projects and delegates subnet use. In this case: A custom role holds just the read permission, and the admin role attaches service projects.

### Question 14 — A

Answer: Allocate a private services access range. A reserved private services range gives the provider somewhere to place the instance. A reserved internal range lets a managed service provider peer into the VPC. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A reserved internal range lets a managed service provider peer into the VPC. In this case: A reserved private services range gives the provider somewhere to place the instance.
- **B:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.
- **D:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.

### Question 15 — D, E

Answers: Create a Private Service Connect endpoint; Attach the service to Serverless VPC Access. The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path. A private endpoint inside the consumer VPC targets a published service attachment. A serverless runtime gets a path into the VPC through a connector or direct egress. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path.
- **B:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path.
- **C:** Incorrect for this question. A reserved internal range lets a managed service provider peer into the VPC. Why the correct answer wins: The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path.
- **D:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path.
- **E:** Correct. A serverless runtime gets a path into the VPC through a connector or direct egress. In this case: The private endpoint consumes the partner attachment, and Serverless VPC Access gives the job a path.

### Question 16 — C

Answer: Connect the networks as a hub-and-spoke peering topology. A hub-and-spoke peering reaches the centre without joining the branches together. A central network peers with each leaf network, and the leaves do not peer with each other. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches together.
- **B:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches together.
- **C:** Correct. A central network peers with each leaf network, and the leaves do not peer with each other. In this case: A hub-and-spoke peering reaches the centre without joining the branches together.
- **D:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches together.

### Question 17 — B

Answer: Peer every VPC network with every other VPC network. A full mesh peers each network with every other one. A full mesh of peering sessions gives each network a direct path to all the others. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: A full mesh peers each network with every other one.
- **B:** Correct. A full mesh of peering sessions gives each network a direct path to all the others. In this case: A full mesh peers each network with every other one.
- **C:** Incorrect for this question. A central network peers with each leaf network, and the leaves do not peer with each other. Why the correct answer wins: A full mesh peers each network with every other one.
- **D:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: A full mesh peers each network with every other one.

### Question 18 — A

Answer: Deploy Private NAT for the overlapping ranges. Private NAT translates the source so identical ranges can exchange traffic. Source addresses are translated so two networks with the same private ranges can still talk. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Source addresses are translated so two networks with the same private ranges can still talk. In this case: Private NAT translates the source so identical ranges can exchange traffic.
- **B:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Private NAT translates the source so identical ranges can exchange traffic.
- **C:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Private NAT translates the source so identical ranges can exchange traffic.
- **D:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Private NAT translates the source so identical ranges can exchange traffic.

### Question 19 — B

Answer: Bring your own public IP prefixes. Bring your own IP advertises prefixes the broadcaster already holds. Public prefixes the organisation already owns are advertised from Google Cloud. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Bring your own IP advertises prefixes the broadcaster already holds.
- **B:** Correct. Public prefixes the organisation already owns are advertised from Google Cloud. In this case: Bring your own IP advertises prefixes the broadcaster already holds.
- **C:** Incorrect for this question. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Why the correct answer wins: Bring your own IP advertises prefixes the broadcaster already holds.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Bring your own IP advertises prefixes the broadcaster already holds.

### Question 20 — A

Answer: Leave the MTU mismatch unfixed. The path disagrees about frame size, so the oversized packets are dropped silently. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Local study-map skill 1.10 (MTU Sizing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. In this case: The path disagrees about frame size, so the oversized packets are dropped silently.
- **B:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: The path disagrees about frame size, so the oversized packets are dropped silently.
- **C:** Incorrect for this question. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Why the correct answer wins: The path disagrees about frame size, so the oversized packets are dropped silently.
- **D:** Incorrect for this question. A larger maximum transmission unit carries more payload per packet inside the VPC. Why the correct answer wins: The path disagrees about frame size, so the oversized packets are dropped silently.

### Question 21 — D

Answer: Deploy a multi-NIC appliance VM between the two networks. An appliance with an interface in each estate inspects and forwards between them. Each interface sits in a different network, so the appliance can inspect and forward between them. Local study-map skill 1.11 (Third-Party Appliance Insertion), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: An appliance with an interface in each estate inspects and forwards between them.
- **B:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: An appliance with an interface in each estate inspects and forwards between them.
- **C:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: An appliance with an interface in each estate inspects and forwards between them.
- **D:** Correct. Each interface sits in a different network, so the appliance can inspect and forward between them. In this case: An appliance with an interface in each estate inspects and forwards between them.

### Question 22 — B

Answer: Expand the existing subnet range. The prefix can grow in place without recreating the instances. A subnet prefix can grow within its address range, and the growth cannot shrink later. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: The prefix can grow in place without recreating the instances.
- **B:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: The prefix can grow in place without recreating the instances.
- **C:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: The prefix can grow in place without recreating the instances.
- **D:** Incorrect for this question. The subnet carries both an IPv4 range and an internal or external IPv6 range. Why the correct answer wins: The prefix can grow in place without recreating the instances.

### Question 23 — A, C

Answers: Expand the existing subnet range; Enable dual-stack IPv6 on the subnet. Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range. A subnet prefix can grow within its address range, and the growth cannot shrink later. The subnet carries both an IPv4 range and an internal or external IPv6 range. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **B:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **C:** Correct. The subnet carries both an IPv4 range and an internal or external IPv6 range. In this case: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **D:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.
- **E:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Growing the prefix adds IPv4 space, and dual-stack adds the IPv6 range.

### Question 24 — A

Answer: Assume peered networks can reach each other transitively. Peering does not hand routes on to a third network. Peering is not transitive, so a route learned through one peer is not passed on to another. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Peering is not transitive, so a route learned through one peer is not passed on to another. In this case: Peering does not hand routes on to a third network.
- **B:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering does not hand routes on to a third network.
- **C:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering does not hand routes on to a third network.
- **D:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: Peering does not hand routes on to a third network.

### Question 25 — C

Answer: Create a VPC Network Peering connection between the two networks. Peering joins exactly the two networks involved. Two networks exchange routes directly without a gateway or a shared project. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering joins exactly the two networks involved.
- **B:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: Peering joins exactly the two networks involved.
- **C:** Correct. Two networks exchange routes directly without a gateway or a shared project. In this case: Peering joins exactly the two networks involved.
- **D:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering joins exactly the two networks involved.

### Question 26 — A

Answer: Grant the subnet user role on the specific shared subnets. Subnet user on that subnet is what the deployment needs. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Subnet user on that subnet is what the deployment needs.
- **B:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: Subnet user on that subnet is what the deployment needs.
- **C:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Subnet user on that subnet is what the deployment needs.
- **D:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Subnet user on that subnet is what the deployment needs.

### Question 27 — A, B

Answers: Build the network as a Shared VPC with host and service projects; Grant the subnet user role on the specific shared subnets. Shared VPC centralises the plan, and subnet user confines each department to its subnet. One host project owns the network and subnets while service projects deploy into shared subnets. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Shared VPC centralises the plan, and subnet user confines each department to its subnet.
- **B:** Correct. One host project owns the network and subnets while service projects deploy into shared subnets. In this case: Shared VPC centralises the plan, and subnet user confines each department to its subnet.
- **C:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Shared VPC centralises the plan, and subnet user confines each department to its subnet.
- **D:** Incorrect for this question. Separate projects own separate networks, and nothing is shared implicitly. Why the correct answer wins: Shared VPC centralises the plan, and subnet user confines each department to its subnet.
- **E:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC centralises the plan, and subnet user confines each department to its subnet.

### Question 28 — D

Answer: Enable Private Google Access on the subnet. Private Google Access routes those calls over internal paths. Instances without external addresses reach Google APIs through internal routing. Local study-map skill 2.4 (Private Google Access and APIs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Private Google Access routes those calls over internal paths.
- **B:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Private Google Access routes those calls over internal paths.
- **C:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Private Google Access routes those calls over internal paths.
- **D:** Correct. Instances without external addresses reach Google APIs through internal routing. In this case: Private Google Access routes those calls over internal paths.

### Question 29 — D

Answer: Enclose the project in a VPC Service Controls perimeter. The perimeter blocks access across its boundary. The perimeter restricts which services the project may call and blocks data movement outside it. Local study-map skill 2.5 (VPC Service Controls Perimeters), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: The perimeter blocks access across its boundary.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: The perimeter blocks access across its boundary.
- **C:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: The perimeter blocks access across its boundary.
- **D:** Correct. The perimeter restricts which services the project may call and blocks data movement outside it. In this case: The perimeter blocks access across its boundary.

### Question 30 — A

Answer: Give the static route a lower priority number than the learned route. The lower priority number wins between routes for one prefix. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: The lower priority number wins between routes for one prefix.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The lower priority number wins between routes for one prefix.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The lower priority number wins between routes for one prefix.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower priority number wins between routes for one prefix.

### Question 31 — C

Answer: Keep the Cloud Router in regional dynamic routing mode. Regional dynamic routing keeps each learned route inside its own region. Routes stay inside the region that learned them. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: Regional dynamic routing keeps each learned route inside its own region.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Regional dynamic routing keeps each learned route inside its own region.
- **C:** Correct. Routes stay inside the region that learned them. In this case: Regional dynamic routing keeps each learned route inside its own region.
- **D:** Incorrect for this question. Routes learned in one region are available to subnets in every region. Why the correct answer wins: Regional dynamic routing keeps each learned route inside its own region.

### Question 32 — D, E

Answers: Switch the Cloud Router to global dynamic routing mode; Enable Bidirectional Forwarding Detection with a short interval. Global mode spreads learned routes, and BFD shortens failure detection. Routes learned in one region are available to subnets in every region. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Global mode spreads learned routes, and BFD shortens failure detection.
- **B:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global mode spreads learned routes, and BFD shortens failure detection.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global mode spreads learned routes, and BFD shortens failure detection.
- **D:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global mode spreads learned routes, and BFD shortens failure detection.
- **E:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: Global mode spreads learned routes, and BFD shortens failure detection.

### Question 33 — A

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches that range and forwards it to the appliance. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches that range and forwards it to the appliance.
- **B:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches that range and forwards it to the appliance.
- **C:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A policy-based route matches that range and forwards it to the appliance.
- **D:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches that range and forwards it to the appliance.

### Question 34 — A

Answer: Create a static route with a tag-scoped next hop. A tag-scoped static route applies to the instances that carry the tag. Only instances carrying the tag send their traffic through the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Only instances carrying the tag send their traffic through the appliance. In this case: A tag-scoped static route applies to the instances that carry the tag.
- **B:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A tag-scoped static route applies to the instances that carry the tag.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: A tag-scoped static route applies to the instances that carry the tag.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A tag-scoped static route applies to the instances that carry the tag.

### Question 35 — C

Answer: Use the internal load balancer as the next hop. The internal load balancer hides the rebuild from routing. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 2.8 (Internal Load Balancer as Next Hop), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer hides the rebuild from routing.
- **B:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer hides the rebuild from routing.
- **C:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer hides the rebuild from routing.
- **D:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer hides the rebuild from routing.

### Question 36 — D

Answer: Apply a CIDR range filter to the spoke. A CIDR filter on the spoke limits what it exchanges with the hub. Only the matching prefixes are exchanged with the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: A CIDR filter on the spoke limits what it exchanges with the hub.
- **B:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A CIDR filter on the spoke limits what it exchanges with the hub.
- **C:** Incorrect for this question. The hub forwards between spokes, which peering alone cannot do. Why the correct answer wins: A CIDR filter on the spoke limits what it exchanges with the hub.
- **D:** Correct. Only the matching prefixes are exchanged with the hub. In this case: A CIDR filter on the spoke limits what it exchanges with the hub.

### Question 37 — A

Answer: Expect spoke-to-spoke reachability through the hub. The hub forwards between its spokes, which is exactly the transitivity on-premises routing expects. The hub forwards between spokes, which peering alone cannot do. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The hub forwards between spokes, which peering alone cannot do. In this case: The hub forwards between its spokes, which is exactly the transitivity on-premises routing expects.
- **B:** Incorrect for this question. The spoke publishes a service attachment so consumers reach it through the hub. Why the correct answer wins: The hub forwards between its spokes, which is exactly the transitivity on-premises routing expects.
- **C:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: The hub forwards between its spokes, which is exactly the transitivity on-premises routing expects.
- **D:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: The hub forwards between its spokes, which is exactly the transitivity on-premises routing expects.

### Question 38 — D

Answer: Resize the service range allocation. The service range, not the pod range, is the pool the cluster uses for service addresses. The service address range must have room for the services the cluster will run. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: The service range, not the pod range, is the pool the cluster uses for service addresses.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: The service range, not the pod range, is the pool the cluster uses for service addresses.
- **C:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: The service range, not the pod range, is the pool the cluster uses for service addresses.
- **D:** Correct. The service address range must have room for the services the cluster will run. In this case: The service range, not the pod range, is the pool the cluster uses for service addresses.

### Question 39 — A

Answer: Configure an IP masquerade policy on the node pool. Masquerading presents the node address instead of the pod address. Outbound pod traffic is translated to the node address under the chosen conditions. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Outbound pod traffic is translated to the node address under the chosen conditions. In this case: Masquerading presents the node address instead of the pod address.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **C:** Incorrect for this question. The policy restricts which pods may talk to the selected pods. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **D:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.

### Question 40 — C

Answer: Create a GKE network policy for the namespace. A network policy restricts which pods may reach the selected pods. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **C:** Correct. In this case: A network policy restricts which pods may reach the selected pods.
- **D:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.

### Question 41 — C

Answer: Enable VPC Flow Logs on the subnet. Flow logs record byte counts for sampled connections. The logs record sampled connections with source, destination, port and byte counts. Local study-map skill 2.11 (VPC Flow Logs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: Flow logs record byte counts for sampled connections.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Flow logs record byte counts for sampled connections.
- **C:** Correct. The logs record sampled connections with source, destination, port and byte counts. In this case: Flow logs record byte counts for sampled connections.
- **D:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Flow logs record byte counts for sampled connections.

### Question 42 — B, E

Answers: Attach a health check to the backend service; Autoscale a managed instance group behind the backend service. The health check decides membership, and the autoscaler sizes the group. The check removes a backend that cannot answer, so traffic moves to a healthy one. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: The health check decides membership, and the autoscaler sizes the group.
- **B:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: The health check decides membership, and the autoscaler sizes the group.
- **C:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: The health check decides membership, and the autoscaler sizes the group.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The health check decides membership, and the autoscaler sizes the group.
- **E:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The health check decides membership, and the autoscaler sizes the group.

### Question 43 — D

Answer: Enable session affinity on the backend service. Affinity keeps each shopper on the backend that holds the cart. Affinity keeps a client on the backend that already holds its session state. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: Affinity keeps each shopper on the backend that holds the cart.
- **B:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Affinity keeps each shopper on the backend that holds the cart.
- **C:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: Affinity keeps each shopper on the backend that holds the cart.
- **D:** Correct. Affinity keeps a client on the backend that already holds its session state. In this case: Affinity keeps each shopper on the backend that holds the cart.

### Question 44 — A

Answer: Register the backends as a zonal network endpoint group. A zonal endpoint group addresses the pod endpoints directly. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. In this case: A zonal endpoint group addresses the pod endpoints directly.
- **B:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: A zonal endpoint group addresses the pod endpoints directly.
- **C:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: A zonal endpoint group addresses the pod endpoints directly.
- **D:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: A zonal endpoint group addresses the pod endpoints directly.

### Question 45 — C

Answer: Split traffic between two backend services by weight. Weighted backends move that share onto the replacement. Weighted backends move a chosen share of traffic onto the new service. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: Weighted backends move that share onto the replacement.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Weighted backends move that share onto the replacement.
- **C:** Correct. Weighted backends move a chosen share of traffic onto the new service. In this case: Weighted backends move that share onto the replacement.
- **D:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: Weighted backends move that share onto the replacement.

### Question 46 — C

Answer: Mirror a copy of the traffic to a second backend. Mirroring sends the copy while the current backend answers. The mirrored request is sent for inspection while the response comes only from the primary. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: Mirroring sends the copy while the current backend answers.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Mirroring sends the copy while the current backend answers.
- **C:** Correct. The mirrored request is sent for inspection while the response comes only from the primary. In this case: Mirroring sends the copy while the current backend answers.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: Mirroring sends the copy while the current backend answers.

### Question 47 — D

Answer: Register the third-party origins as an internet network endpoint group. An internet endpoint group targets that external endpoint. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An internet endpoint group targets that external endpoint.
- **B:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: An internet endpoint group targets that external endpoint.
- **C:** Incorrect for this question. The backend service holds the health check, balancing mode and capacity settings. Why the correct answer wins: An internet endpoint group targets that external endpoint.
- **D:** Correct. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. In this case: An internet endpoint group targets that external endpoint.

### Question 48 — B

Answer: Autoscale a managed instance group behind the backend service. The autoscaler adds and removes members with the signal. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: The autoscaler adds and removes members with the signal.
- **B:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: The autoscaler adds and removes members with the signal.
- **C:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: The autoscaler adds and removes members with the signal.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The autoscaler adds and removes members with the signal.

### Question 49 — C

Answer: Expose the workload through the GKE Gateway controller. The Gateway controller supports shared gateways with route-level policy. A Gateway object configures the load balancer through the newer Kubernetes API. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.
- **B:** Incorrect for this question. An Ingress object creates a Google Cloud load balancer from the manifest. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.
- **C:** Correct. A Gateway object configures the load balancer through the newer Kubernetes API. In this case: The Gateway controller supports shared gateways with route-level policy.
- **D:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.

### Question 50 — B

Answer: Expose the workload through the GKE Ingress controller. The Ingress controller turns a single object into a Google Cloud load balancer. An Ingress object creates a Google Cloud load balancer from the manifest. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Ingress controller turns a single object into a Google Cloud load balancer.
- **B:** Correct. An Ingress object creates a Google Cloud load balancer from the manifest. In this case: The Ingress controller turns a single object into a Google Cloud load balancer.
- **C:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The Ingress controller turns a single object into a Google Cloud load balancer.
- **D:** Incorrect for this question. A Gateway object configures the load balancer through the newer Kubernetes API. Why the correct answer wins: The Ingress controller turns a single object into a Google Cloud load balancer.

### Question 51 — C, D

Answers: Enable Cloud CDN on the backend service; Raise the cache time to live. Edge caching removes repeat fetches, and a longer lifetime suits a daily change. The edge holds a copy of the response so later requests are served closer to the user. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Invalidation removes the stale copy so the next request fetches the current version. Why the correct answer wins: Edge caching removes repeat fetches, and a longer lifetime suits a daily change.
- **B:** Incorrect for this question. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. Why the correct answer wins: Edge caching removes repeat fetches, and a longer lifetime suits a daily change.
- **C:** Correct. A longer lifetime reduces origin load and lengthens the window in which content can be stale. In this case: Edge caching removes repeat fetches, and a longer lifetime suits a daily change.
- **D:** Correct. The edge holds a copy of the response so later requests are served closer to the user. In this case: Edge caching removes repeat fetches, and a longer lifetime suits a daily change.
- **E:** Incorrect for this question. A signed URL authorises one object for a limited time without making the bucket public. Why the correct answer wins: Edge caching removes repeat fetches, and a longer lifetime suits a daily change.

### Question 52 — A

Answer: Serve the object through a signed URL. A signed URL authorises that one object for a limited window. A signed URL authorises one object for a limited time without making the bucket public. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A signed URL authorises one object for a limited time without making the bucket public. In this case: A signed URL authorises that one object for a limited window.
- **B:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: A signed URL authorises that one object for a limited window.
- **C:** Incorrect for this question. Invalidation removes the stale copy so the next request fetches the current version. Why the correct answer wins: A signed URL authorises that one object for a limited window.
- **D:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: A signed URL authorises that one object for a limited window.

### Question 53 — C

Answer: Create a private Cloud DNS zone. A private zone answers only inside its authorised networks. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: A private zone answers only inside its authorised networks.
- **B:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: A private zone answers only inside its authorised networks.
- **C:** Correct. In this case: A private zone answers only inside its authorised networks.
- **D:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A private zone answers only inside its authorised networks.

### Question 54 — A, E

Answers: Lower the record TTL before the cutover; Create a DNS peering zone to the other project. The short TTL speeds the switch, and the peering zone extends resolution. A short TTL lets resolvers pick up the new address quickly after the change. The consumer project resolves names from the producer project through a peering zone. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The consumer project resolves names from the producer project through a peering zone. In this case: The short TTL speeds the switch, and the peering zone extends resolution.
- **B:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: The short TTL speeds the switch, and the peering zone extends resolution.
- **C:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The short TTL speeds the switch, and the peering zone extends resolution.
- **D:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The short TTL speeds the switch, and the peering zone extends resolution.
- **E:** Correct. A short TTL lets resolvers pick up the new address quickly after the change. In this case: The short TTL speeds the switch, and the peering zone extends resolution.

### Question 55 — A

Answer: Apply a geolocation routing policy to the record set. Geolocation answers from the source region of the query. The answer depends on the source region of the query. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The answer depends on the source region of the query. In this case: Geolocation answers from the source region of the query.
- **B:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: Geolocation answers from the source region of the query.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: Geolocation answers from the source region of the query.
- **D:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: Geolocation answers from the source region of the query.

### Question 56 — C

Answer: Apply a failover routing policy with a health-checked primary. The failover policy serves the standby only while the primary is unhealthy. The standby answer is served when the primary fails its health check. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The failover policy serves the standby only while the primary is unhealthy.
- **B:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The failover policy serves the standby only while the primary is unhealthy.
- **C:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy serves the standby only while the primary is unhealthy.
- **D:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy serves the standby only while the primary is unhealthy.

### Question 57 — A

Answer: Enable DNSSEC on the zone. Signed answers let the resolver detect forgery. Signatures let a resolver verify that the answer was not altered in transit. Local study-map skill 3.8 (DNSSEC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Signatures let a resolver verify that the answer was not altered in transit. In this case: Signed answers let the resolver detect forgery.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Signed answers let the resolver detect forgery.
- **C:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: Signed answers let the resolver detect forgery.
- **D:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: Signed answers let the resolver detect forgery.

### Question 58 — A, B

Answers: Order a Dedicated Interconnect connection; Create a VLAN attachment on Cloud Router. The dedicated circuit uses that cage, and the VLAN attachment carries the subnet. A private physical circuit connects the premises to a Google colocation facility. The attachment carries one VLAN over the interconnect and peers with the router. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: The dedicated circuit uses that cage, and the VLAN attachment carries the subnet.
- **B:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The dedicated circuit uses that cage, and the VLAN attachment carries the subnet.
- **C:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the subnet.
- **D:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the subnet.
- **E:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: The dedicated circuit uses that cage, and the VLAN attachment carries the subnet.

### Question 59 — C

Answer: Order a Partner Interconnect connection. A partner hands the circuit off to Google from a nearby provider location. A service provider carries the circuit to Google on the customer behalf. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: A partner hands the circuit off to Google from a nearby provider location.
- **B:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: A partner hands the circuit off to Google from a nearby provider location.
- **C:** Correct. A service provider carries the circuit to Google on the customer behalf. In this case: A partner hands the circuit off to Google from a nearby provider location.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: A partner hands the circuit off to Google from a nearby provider location.

### Question 60 — A

Answer: Set the Cloud Router ASN to a private value that differs from the peer. The two peers must not share an autonomous system number. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The two peers must not share an autonomous system number.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The two peers must not share an autonomous system number.
- **C:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The two peers must not share an autonomous system number.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: The two peers must not share an autonomous system number.

### Question 61 — A

Answer: Order a Cross-Cloud Interconnect connection. Cross-Cloud Interconnect is a dedicated circuit to the other provider. A dedicated circuit connects Google Cloud directly to another cloud provider. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A dedicated circuit connects Google Cloud directly to another cloud provider. In this case: Cross-Cloud Interconnect is a dedicated circuit to the other provider.
- **B:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to the other provider.
- **C:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to the other provider.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to the other provider.

### Question 62 — B

Answer: Enable MACsec on the interconnect. MACsec encrypts each hop between the premises and Google. Link-layer encryption protects each hop of the circuit between the premises and Google. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: MACsec encrypts each hop between the premises and Google.
- **B:** Correct. Link-layer encryption protects each hop of the circuit between the premises and Google. In this case: MACsec encrypts each hop between the premises and Google.
- **C:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: MACsec encrypts each hop between the premises and Google.
- **D:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: MACsec encrypts each hop between the premises and Google.

### Question 63 — A, D

Answers: Deploy an HA VPN gateway with two interfaces; Enable Bidirectional Forwarding Detection with a short interval. The two-interface gateway gives redundancy, and BFD detects the failure quickly. Two interfaces in different zones give the tunnel pair a 99.99% topology. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: The two-interface gateway gives redundancy, and BFD detects the failure quickly.
- **B:** Incorrect for this question. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Why the correct answer wins: The two-interface gateway gives redundancy, and BFD detects the failure quickly.
- **C:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: The two-interface gateway gives redundancy, and BFD detects the failure quickly.
- **D:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: The two-interface gateway gives redundancy, and BFD detects the failure quickly.
- **E:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: The two-interface gateway gives redundancy, and BFD detects the failure quickly.

### Question 64 — B

Answer: Deploy an HA VPN gateway with two interfaces. Two interfaces in different zones give the pair redundancy. Two interfaces in different zones give the tunnel pair a 99.99% topology. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Two interfaces in different zones give the pair redundancy.
- **B:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: Two interfaces in different zones give the pair redundancy.
- **C:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Two interfaces in different zones give the pair redundancy.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: Two interfaces in different zones give the pair redundancy.

### Question 65 — D

Answer: Lower the tunnel MTU to 1460 bytes. The tunnel reduces usable payload, so the MTU must fit inside it. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: The tunnel reduces usable payload, so the MTU must fit inside it.
- **B:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: The tunnel reduces usable payload, so the MTU must fit inside it.
- **C:** Incorrect for this question. A larger maximum transmission unit carries more payload per packet inside the VPC. Why the correct answer wins: The tunnel reduces usable payload, so the MTU must fit inside it.
- **D:** Correct. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. In this case: The tunnel reduces usable payload, so the MTU must fit inside it.

### Question 66 — B

Answer: Deploy a Classic VPN with a single tunnel. Classic VPN supports the policy-based mode such a device requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.4 (Classic VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Classic VPN supports the policy-based mode such a device requires.
- **B:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports the policy-based mode such a device requires.
- **C:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Classic VPN supports the policy-based mode such a device requires.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Classic VPN supports the policy-based mode such a device requires.

### Question 67 — D

Answer: Prefer the path with the lower multi-exit discriminator. A higher discriminator makes that path less preferred. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: A higher discriminator makes that path less preferred.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A higher discriminator makes that path less preferred.
- **C:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: A higher discriminator makes that path less preferred.
- **D:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: A higher discriminator makes that path less preferred.

### Question 68 — A

Answer: Advertise only the ranges the peer needs. The advertisement list publishes only the chosen prefixes. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: The advertisement list publishes only the chosen prefixes.
- **B:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.
- **C:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.
- **D:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.

### Question 69 — A, C

Answers: Set the Cloud Router ASN to a private value that differs from the peer; Advertise only the ranges the peer needs. The ASN must differ from the peer, and the advertisement list limits the prefixes. Two peers cannot form a session when both claim the same autonomous system number. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The ASN must differ from the peer, and the advertisement list limits the prefixes.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The ASN must differ from the peer, and the advertisement list limits the prefixes.
- **C:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: The ASN must differ from the peer, and the advertisement list limits the prefixes.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The ASN must differ from the peer, and the advertisement list limits the prefixes.
- **E:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The ASN must differ from the peer, and the advertisement list limits the prefixes.

### Question 70 — A

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the degraded path while the session still looks established. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.6 (BFD and Failover Timers), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the degraded path while the session still looks established.
- **B:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: BFD detects the degraded path while the session still looks established.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the degraded path while the session still looks established.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the degraded path while the session still looks established.

### Question 71 — C

Answer: Switch the Cloud Router to global dynamic routing mode. Global dynamic routing makes learned routes usable everywhere. Routes learned in one region are available to subnets in every region. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: Global dynamic routing makes learned routes usable everywhere.
- **B:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global dynamic routing makes learned routes usable everywhere.
- **C:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global dynamic routing makes learned routes usable everywhere.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global dynamic routing makes learned routes usable everywhere.

### Question 72 — B

Answer: Switch best path selection back to the legacy behaviour. The best path selection setting decides how ties break. The older selection order picks a different preferred path when the inputs tie. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The best path selection setting decides how ties break.
- **B:** Correct. The older selection order picks a different preferred path when the inputs tie. In this case: The best path selection setting decides how ties break.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The best path selection setting decides how ties break.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The best path selection setting decides how ties break.

### Question 73 — C

Answer: Run HA VPN over Cloud Interconnect instead of MACsec. IPsec tunnels encrypt the traffic where MACsec is unavailable. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Local study-map skill 4.8 (Interconnect Encryption and SLA), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: IPsec tunnels encrypt the traffic where MACsec is unavailable.
- **B:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: IPsec tunnels encrypt the traffic where MACsec is unavailable.
- **C:** Correct. IPsec tunnels inside the interconnect give encryption where MACsec is not available. In this case: IPsec tunnels encrypt the traffic where MACsec is unavailable.
- **D:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: IPsec tunnels encrypt the traffic where MACsec is unavailable.

### Question 74 — C

Answer: Enable Cloud NAT logging. NAT logging records the translated address and port for each flow. The logs record the translated address and port chosen for each flow. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: NAT logging records the translated address and port for each flow.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: NAT logging records the translated address and port for each flow.
- **C:** Correct. The logs record the translated address and port chosen for each flow. In this case: NAT logging records the translated address and port for each flow.
- **D:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: NAT logging records the translated address and port for each flow.

### Question 75 — D

Answer: Enable Cloud VPN logging. VPN logging records state changes and negotiation outcomes. The logs record tunnel state changes and IKE negotiation outcomes. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: VPN logging records state changes and negotiation outcomes.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: VPN logging records state changes and negotiation outcomes.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: VPN logging records state changes and negotiation outcomes.
- **D:** Correct. The logs record tunnel state changes and IKE negotiation outcomes. In this case: VPN logging records state changes and negotiation outcomes.

### Question 76 — D

Answer: Publish a custom metric from the appliance. A custom metric carries the appliance's own gauge into Monitoring so alerts can use it. The appliance reports a signal that no managed metric covers. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: A custom metric carries the appliance's own gauge into Monitoring so alerts can use it.
- **B:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: A custom metric carries the appliance's own gauge into Monitoring so alerts can use it.
- **C:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: A custom metric carries the appliance's own gauge into Monitoring so alerts can use it.
- **D:** Correct. The appliance reports a signal that no managed metric covers. In this case: A custom metric carries the appliance's own gauge into Monitoring so alerts can use it.

### Question 77 — D

Answer: Create an alert policy on the network metric. An alert policy notifies when the metric crosses the threshold. The policy notifies on the threshold instead of waiting for a user report. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: An alert policy notifies when the metric crosses the threshold.
- **B:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: An alert policy notifies when the metric crosses the threshold.
- **C:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: An alert policy notifies when the metric crosses the threshold.
- **D:** Correct. The policy notifies on the threshold instead of waiting for a user report. In this case: An alert policy notifies when the metric crosses the threshold.

### Question 78 — B

Answer: Run a Connectivity Test between the two endpoints. A connectivity test evaluates the path and reports the result. The test evaluates the configuration along the path and names the blocking rule or missing route. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A connectivity test evaluates the path and reports the result.
- **B:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: A connectivity test evaluates the path and reports the result.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A connectivity test evaluates the path and reports the result.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: A connectivity test evaluates the path and reports the result.

### Question 79 — C, E

Answers: Run a Connectivity Test between the two endpoints; Inspect the flow in Network Topology. The test proves the path, and the topology view documents the flow. The test evaluates the configuration along the path and names the blocking rule or missing route. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The test proves the path, and the topology view documents the flow.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The test proves the path, and the topology view documents the flow.
- **C:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: The test proves the path, and the topology view documents the flow.
- **D:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: The test proves the path, and the topology view documents the flow.
- **E:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: The test proves the path, and the topology view documents the flow.

### Question 80 — A

Answer: Check the Performance Dashboard for packet loss. The performance dashboard reports each segment separately. The dashboard separates loss on the Google network from loss outside it. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The dashboard separates loss on the Google network from loss outside it. In this case: The performance dashboard reports each segment separately.
- **B:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: The performance dashboard reports each segment separately.
- **C:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The performance dashboard reports each segment separately.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The performance dashboard reports each segment separately.

### Question 81 — D

Answer: Test the path with a large ping and the do-not-fragment bit. A large probe shows the size at which the payload stops crossing. The probe shows where the payload stops fitting along the path. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A large probe shows the size at which the payload stops crossing.
- **B:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A large probe shows the size at which the payload stops crossing.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A large probe shows the size at which the payload stops crossing.
- **D:** Correct. The probe shows where the payload stops fitting along the path. In this case: A large probe shows the size at which the payload stops crossing.

### Question 82 — D

Answer: Review Firewall Insights for shadowed rules. Firewall Insights reports rules that never match. The insight names rules that never match because a broader rule already covered them. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights reports rules that never match.
- **B:** Incorrect for this question. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Why the correct answer wins: Firewall Insights reports rules that never match.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights reports rules that never match.
- **D:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights reports rules that never match.

### Question 83 — C, D

Answers: Read the Network Analyzer findings; Review Firewall Insights for shadowed rules. Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. The insight names rules that never match because a broader rule already covered them. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic.
- **B:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic.
- **C:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic.
- **D:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic.
- **E:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights lists the rules that never match, and the analyser flags configurations that could break traffic.

### Question 84 — D

Answer: Query Flow Analyzer for the top talkers. Flow Analyzer ranks the flows by volume. The analysis ranks the flows that consume the most bandwidth. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Flow Analyzer ranks the flows by volume.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Flow Analyzer ranks the flows by volume.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Flow Analyzer ranks the flows by volume.
- **D:** Correct. The analysis ranks the flows that consume the most bandwidth. In this case: Flow Analyzer ranks the flows by volume.

### Question 85 — D

Answer: Inspect the flow in Network Topology. Network Topology draws the paths that actually carry traffic. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Topology draws the paths that actually carry traffic.
- **B:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Topology draws the paths that actually carry traffic.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Network Topology draws the paths that actually carry traffic.
- **D:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: Network Topology draws the paths that actually carry traffic.

### Question 86 — C

Answer: Compare the BGP session state on both peers. Comparing both peers isolates the fault to one side. A session that is established on one side only points at the shared configuration. Local study-map skill 5.7 (BGP and VPN Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Comparing both peers isolates the fault to one side.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Comparing both peers isolates the fault to one side.
- **C:** Correct. A session that is established on one side only points at the shared configuration. In this case: Comparing both peers isolates the fault to one side.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Comparing both peers isolates the fault to one side.

### Question 87 — C

Answer: Drain the backend before removing it. New flows are steered elsewhere while the existing uploads are allowed to complete. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 5.8 (Traffic Draining and Migration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: New flows are steered elsewhere while the existing uploads are allowed to complete.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: New flows are steered elsewhere while the existing uploads are allowed to complete.
- **C:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: New flows are steered elsewhere while the existing uploads are allowed to complete.
- **D:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: New flows are steered elsewhere while the existing uploads are allowed to complete.

### Question 88 — B

Answer: Attach a Cloud Armor backend security policy. A backend security policy can match the request origin. The policy filters traffic that has already reached the load balancer. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: A backend security policy can match the request origin.
- **B:** Correct. The policy filters traffic that has already reached the load balancer. In this case: A backend security policy can match the request origin.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A backend security policy can match the request origin.
- **D:** Incorrect for this question. The policy filters traffic at the edge before it is proxied to a backend. Why the correct answer wins: A backend security policy can match the request origin.

### Question 89 — B

Answer: Attach a Cloud Armor edge security policy. An edge policy decides at the edge, so the proxy never handles the request. The policy filters traffic at the edge before it is proxied to a backend. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: An edge policy decides at the edge, so the proxy never handles the request.
- **B:** Correct. The policy filters traffic at the edge before it is proxied to a backend. In this case: An edge policy decides at the edge, so the proxy never handles the request.
- **C:** Incorrect for this question. The policy filters traffic that has already reached the load balancer. Why the correct answer wins: An edge policy decides at the edge, so the proxy never handles the request.
- **D:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: An edge policy decides at the edge, so the proxy never handles the request.

### Question 90 — B

Answer: Enable Adaptive Protection. Adaptive Protection proposes rules for the anomaly it learns. The model learns the normal request pattern and suggests rules for the anomaly it detects. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Adaptive Protection proposes rules for the anomaly it learns.
- **B:** Correct. The model learns the normal request pattern and suggests rules for the anomaly it detects. In this case: Adaptive Protection proposes rules for the anomaly it learns.
- **C:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Adaptive Protection proposes rules for the anomaly it learns.
- **D:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: Adaptive Protection proposes rules for the anomaly it learns.

### Question 91 — B

Answer: Apply Google Threat Intelligence lists. Threat intelligence lists match those addresses without hand-written rules. Requests from addresses on the threat lists are matched without writing rules by hand. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.
- **B:** Correct. Requests from addresses on the threat lists are matched without writing rules by hand. In this case: Threat intelligence lists match those addresses without hand-written rules.
- **C:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.
- **D:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: Threat intelligence lists match those addresses without hand-written rules.

### Question 92 — C

Answer: Add a rate-based ban rule. A rate-based ban blocks a client that crosses the threshold. A client that exceeds the threshold is blocked for the ban duration. Local study-map skill 6.3 (DDoS and Rate Limiting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.
- **B:** Incorrect for this question. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.
- **C:** Correct. A client that exceeds the threshold is blocked for the ban duration. In this case: A rate-based ban blocks a client that crosses the threshold.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: A rate-based ban blocks a client that crosses the threshold.

### Question 93 — C, E

Answers: Create a global network firewall policy; Move the inspection to NGFW Enterprise. The global policy covers every region, and the enterprise tier adds inspection. The policy is evaluated for the networks it is associated with, in every region. The enterprise tier adds layer 7 inspection through the managed engine. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds inspection.
- **B:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds inspection.
- **C:** Correct. The enterprise tier adds layer 7 inspection through the managed engine. In this case: The global policy covers every region, and the enterprise tier adds inspection.
- **D:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The global policy covers every region, and the enterprise tier adds inspection.
- **E:** Correct. The policy is evaluated for the networks it is associated with, in every region. In this case: The global policy covers every region, and the enterprise tier adds inspection.

### Question 94 — D

Answer: Create a hierarchical firewall policy at the organisation. The organisation policy is inherited and cannot be deleted locally. The policy applies to every project under the organisation node. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The organisation policy is inherited and cannot be deleted locally.
- **B:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The organisation policy is inherited and cannot be deleted locally.
- **C:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The organisation policy is inherited and cannot be deleted locally.
- **D:** Correct. The policy applies to every project under the organisation node. In this case: The organisation policy is inherited and cannot be deleted locally.

### Question 95 — A

Answer: Create a regional network firewall policy. A regional policy applies only inside its own region. The policy applies only in the region it belongs to. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The policy applies only in the region it belongs to. In this case: A regional policy applies only inside its own region.
- **B:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: A regional policy applies only inside its own region.
- **C:** Incorrect for this question. The policy is evaluated for the networks it is associated with, in every region. Why the correct answer wins: A regional policy applies only inside its own region.
- **D:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: A regional policy applies only inside its own region.

### Question 96 — C

Answer: Divide the network into micro-segmented tiers. Micro-segmentation gives each tier its own tag and permits only the flows it needs. Each tier carries a different tag and only the required flows are allowed between tiers. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the flows it needs.
- **B:** Incorrect for this question. The enterprise tier adds layer 7 inspection through the managed engine. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the flows it needs.
- **C:** Correct. Each tier carries a different tag and only the required flows are allowed between tiers. In this case: Micro-segmentation gives each tier its own tag and permits only the flows it needs.
- **D:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: Micro-segmentation gives each tier its own tag and permits only the flows it needs.

### Question 97 — A

Answer: Add a deny-all egress rule with a higher priority. A deny-all egress rule replaces the default allow. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. In this case: A deny-all egress rule replaces the default allow.
- **B:** Incorrect for this question. The standard tier adds the policy model and threat intelligence over the base rules. Why the correct answer wins: A deny-all egress rule replaces the default allow.
- **C:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: A deny-all egress rule replaces the default allow.
- **D:** Incorrect for this question. Each tier carries a different tag and only the required flows are allowed between tiers. Why the correct answer wins: A deny-all egress rule replaces the default allow.

### Question 98 — B

Answer: Use dynamic port allocation. Dynamic allocation hands out ports as demand arrives. Ports are assigned from a shared pool as the demand arrives. Local study-map skill 6.6 (Cloud NAT and Port Allocation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.
- **B:** Correct. Ports are assigned from a shared pool as the demand arrives. In this case: Dynamic allocation hands out ports as demand arrives.
- **C:** Incorrect for this question. Google assigns and releases external addresses as the demand changes. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.
- **D:** Incorrect for this question. Each VM reserves a block of ports, which gives predictable capacity and predictable consumption. Why the correct answer wins: Dynamic allocation hands out ports as demand arrives.

### Question 99 — B

Answer: Deploy Secure Web Proxy as the egress path. Secure Web Proxy applies URL policy to egress traffic. The proxy applies URL and TLS inspection policy to outbound traffic. Local study-map skill 6.7 (Secure Web Proxy), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.
- **B:** Correct. The proxy applies URL and TLS inspection policy to outbound traffic. In this case: Secure Web Proxy applies URL policy to egress traffic.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.
- **D:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Secure Web Proxy applies URL policy to egress traffic.

### Question 100 — B

Answer: Inspect the traffic out of band with Packet Mirroring. Out-of-band inspection copies the traffic and leaves the path untouched. A copy of the traffic goes to a collector while the original flow continues untouched. Local study-map skill 6.8 (Multi-NIC Appliances and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Out-of-band inspection copies the traffic and leaves the path untouched.
- **B:** Correct. A copy of the traffic goes to a collector while the original flow continues untouched. In this case: Out-of-band inspection copies the traffic and leaves the path untouched.
- **C:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: Out-of-band inspection copies the traffic and leaves the path untouched.
- **D:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Out-of-band inspection copies the traffic and leaves the path untouched.
