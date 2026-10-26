# Google Cloud Professional Cloud Network Engineer — Full-Length Mock Exam 3

Professional Cloud Network Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study item is reproduced. The live paper allows two hours for 50-60 items, so this 100-item set is a slower-per-item rehearsal: about 72 seconds per item here against roughly 120-144 seconds live. Use it to build a habit of finishing with time to review. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Designing and Planning a Google Cloud VPC Network (VPC Design, IP Planning, and Load Balancer Choice)

### 1. A streaming platform serves viewers in twenty countries from three regions and buffers must stay small. Which tier fits?

- A. Enable Cloud CDN on the backend service
- B. Deploy a regional external Application Load Balancer
- C. Use the Premium network service tier
- D. Use the Standard network service tier

### 2. An internal build farm transfers artefacts within one country and finance watches egress cost. Which tier fits?

- A. Use an external proxy Network Load Balancer with TLS termination
- B. Use the Premium network service tier
- C. Use the Standard network service tier
- D. Assign a manual static Cloud NAT address

### 3. A gaming backend must serve the same hostname on three continents with automatic failover. What should front it?

- A. Deploy a regional external Application Load Balancer
- B. Deploy a global external Application Load Balancer
- C. Route by URL path in the URL map
- D. Deploy an internal passthrough Network Load Balancer

### 4. A media service must serve users from the closest region and must stop using a region whose backends fail. Which two components fit? Select two.

- A. Enable session affinity on the backend service
- B. Deploy a global external Application Load Balancer
- C. Attach a health check to the backend service
- D. Register the backends as a zonal network endpoint group
- E. Deploy a regional external Application Load Balancer

### 5. A shared services project must resolve names owned by a network project without forwarding to the internet. What fits?

- A. Bind the private zone to the service project networks
- B. Create an inbound forwarding policy with a forwarding address
- C. Configure a DNS forwarding policy for the on-premises domain
- D. Create a DNS peering zone to the other project

### 6. The same hostname must answer with an internal address inside and a public address outside. What should be configured?

- A. Enable DNSSEC on the zone
- B. Create a public Cloud DNS zone
- C. Serve split-horizon answers from separate private and public zones
- D. Create a private Cloud DNS zone

### 7. A service must be reachable only from inside the VPC and its connected networks. Which front end fits?

- A. Use a proxy Network Load Balancer
- B. Deploy an internal passthrough Network Load Balancer
- C. Use a passthrough Network Load Balancer
- D. Deploy a global external Application Load Balancer

### 8. A web application must serve users in Asia and Europe from one certified hostname. What should be deployed?

- A. Use an external proxy Network Load Balancer with TLS termination
- B. Deploy a global external Application Load Balancer
- C. Deploy an internal passthrough Network Load Balancer
- D. Deploy a regional external Application Load Balancer

### 9. A public control plane endpoint must accept only the corporate VPN range. What should be configured?

- A. Add the office range to the authorised networks
- B. Use a private control plane endpoint
- C. Use private nodes with no external addresses
- D. Use the DNS-based control plane endpoint

### 10. A cluster must run IPv6 workloads alongside IPv4 without a second cluster. What should be planned?

- A. Bring your own public IP prefixes
- B. Plan secondary ranges for pods and services
- C. Use privately used public IP address ranges
- D. Enable dual-stack IPv6 on the subnet

### 11. A regulated cluster must have no externally addressed nodes and no public API endpoint. Which two settings fit? Select two.

- A. Add the office range to the authorised networks
- B. Enable GKE Dataplane V2
- C. Configure an IP masquerade policy on the node pool
- D. Use a private control plane endpoint
- E. Use private nodes with no external addresses

### 12. A deployment pipeline must use one shared subnet without the ability to change it. Which role fits?

- A. Grant the basic editor role to the automation
- B. Grant the network administrator role in the host project
- C. Grant the subnet user role on the specific shared subnets
- D. Grant Shared VPC Admin on the host project

### 13. A network automation identity must create subnets and read routes but must not touch firewalls. Which two grants fit? Select two.

- A. Create a custom role with only the required network permissions
- B. Grant the subnet user role on the specific shared subnets
- C. Grant the network administrator role in the host project
- D. Grant Shared VPC Admin on the host project
- E. Grant the basic editor role to the automation

### 14. An analytics warehouse must be provisioned with an internal address in the project. What is required first?

- A. Create a Private Service Connect endpoint
- B. Allocate a private services access range
- C. Attach the service to Serverless VPC Access
- D. Enable Private Google Access on the subnet

### 15. A revision must call a partner's published service privately and must appear as a subnet address itself. Which two mechanisms fit? Select two.

- A. Create a Private Service Connect endpoint
- B. Use Direct VPC egress for the serverless workload
- C. Attach the service to Serverless VPC Access
- D. Allocate a private services access range
- E. Reach the API through its public interface

### 16. Three networks of equal standing must all reach each other and no hub is allowed. What topology fits?

- A. Connect the networks as a hub-and-spoke peering topology
- B. Connect the VPC networks through a Network Connectivity Center hub
- C. Peer every VPC network with every other VPC network
- D. Build the network as a Shared VPC with host and service projects

### 17. Six branch networks must reach a central network and never reach each other. What topology fits?

- A. Create a VPC Network Peering connection between the two networks
- B. Peer every VPC network with every other VPC network
- C. Connect the VPC networks through a Network Connectivity Center hub
- D. Connect the networks as a hub-and-spoke peering topology

### 18. Internal workloads need more addresses and no public route will ever be published. What fits?

- A. Use privately used public IP address ranges
- B. Bring your own public IP prefixes
- C. Use non-RFC 1918 space for the internal network
- D. Deploy Private NAT for the overlapping ranges

### 19. Two merged companies both use 192.168.0.0/16 and must keep their addresses. What fits?

- A. Use privately used public IP address ranges
- B. Accept the overlapping subnet ranges as configured
- C. Deploy Private NAT for the overlapping ranges
- D. Automate address allocation from a central IPAM plan

### 20. A storage cluster inside one network sees poor throughput on jumbo-capable links. What should be raised?

- A. Keep the default 1500-byte MTU
- B. Lower the tunnel MTU to 1460 bytes
- C. Leave the MTU mismatch unfixed
- D. Raise the VPC MTU to 8896 bytes

### 21. A cloud firewall appliance must see traffic to one SaaS provider before it leaves. What routes it?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Create a static route with a tag-scoped next hop
- C. Add a policy-based route that matches the source and destination
- D. Use the internal load balancer as the next hop

---

## Domain 2 — Implementing a VPC Network (VPC Implementation, Routing, and GKE Networking)

### 22. A new regulation expects IPv6 reachability for public workloads. What should be enabled on the subnet?

- A. Enable dual-stack IPv6 on the subnet
- B. Add a second pod range to the cluster
- C. Expand the existing subnet range
- D. Use privately used public IP address ranges

### 23. Two subnets are nearly full and new teams keep requesting overlapping blocks. Which two actions fit? Select two.

- A. Automate address allocation from a central IPAM plan
- B. Bring your own public IP prefixes
- C. Expand the existing subnet range
- D. Accept the overlapping subnet ranges as configured
- E. Use non-RFC 1918 space for the internal network

### 24. A policy-based route must be visible across a peering boundary. What should be enabled?

- A. Assume peered networks can reach each other transitively
- B. Import and export custom routes over the peering
- C. Add a policy-based route that matches the source and destination
- D. Apply a CIDR range filter to the spoke

### 25. Two departments need a direct path between their own networks and no shared project. What fits?

- A. Build the network as a Shared VPC with host and service projects
- B. Create a VPC Network Peering connection between the two networks
- C. Peer every VPC network with every other VPC network
- D. Connect the VPC networks through a Network Connectivity Center hub

### 26. The platform team must delegate subnets from one host network to four consumers. Which role allows it?

- A. Grant Shared VPC Admin on the host project
- B. Grant the network administrator role in the host project
- C. Create a custom role with only the required network permissions
- D. Grant the subnet user role on the specific shared subnets

### 27. A holding company wants one network, central control, and per-team isolation. Which two choices fit? Select two.

- A. Grant the basic editor role to the automation
- B. Grant Shared VPC Admin on the host project
- C. Grant the subnet user role on the specific shared subnets
- D. Build the network as a Shared VPC with host and service projects
- E. Give each team its own standalone VPC network

### 28. A batch fleet with no external addresses must pull container images from Google's registry. What should be enabled?

- A. Create a Private Service Connect endpoint
- B. Enable Private Google Access on the subnet
- C. Reach the API through its public interface
- D. Attach the service to Serverless VPC Access

### 29. A dataset must not be readable from a project that sits outside the approved boundary. What should be configured?

- A. Enclose the project in a VPC Service Controls perimeter
- B. Review Firewall Insights for shadowed rules
- C. Enable Private Google Access on the subnet
- D. Create a hierarchical firewall policy at the organisation

### 30. A static route must beat a dynamic route for the same prefix. What determines that?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Give the static route a lower priority number than the learned route
- C. Prefer the path with the lower multi-exit discriminator
- D. Switch best path selection back to the legacy behaviour

### 31. A VPN hub in one region must serve subnets in three regions. Which routing mode fits?

- A. Advertise only the ranges the peer needs
- B. Keep the Cloud Router in regional dynamic routing mode
- C. Switch the Cloud Router to global dynamic routing mode
- D. Prefer the path with the lower multi-exit discriminator

### 32. Two attachments carry equal prefixes and the older selection order picks the wrong one. Which two settings decide it? Select two.

- A. Give the static route a lower priority number than the learned route
- B. Switch best path selection back to the legacy behaviour
- C. Prefer the path with the lower multi-exit discriminator
- D. Set the Cloud Router ASN to a private value that differs from the peer
- E. Enable Bidirectional Forwarding Detection with a short interval

### 33. Traffic from one source range must reach an appliance although the destination is the internet. What fits?

- A. Deploy a multi-NIC appliance VM between the two networks
- B. Use the internal load balancer as the next hop
- C. Add a policy-based route that matches the source and destination
- D. Create a static route with a tag-scoped next hop

### 34. A test fleet alone must use the inspection path. What should be created?

- A. Give the static route a lower priority number than the learned route
- B. Create a static route with a tag-scoped next hop
- C. Add a policy-based route that matches the source and destination
- D. Use the internal load balancer as the next hop

### 35. Appliance instances are replaced weekly and routes must not change. What should the next hop be?

- A. Create a static route with a tag-scoped next hop
- B. Deploy a multi-NIC appliance VM between the two networks
- C. Use the internal load balancer as the next hop
- D. Add a policy-based route that matches the source and destination

### 36. A published service attachment must be reachable through the hub. Which spoke type fits?

- A. Add the published service as a producer spoke
- B. Add the VPC network as a VPC spoke
- C. Apply a CIDR range filter to the spoke
- D. Add the attachment as a hybrid spoke

### 37. Only the datacentre prefixes may be exchanged with the hub, not the whole range. What should be applied?

- A. Add the VPC network as a VPC spoke
- B. Expect spoke-to-spoke reachability through the hub
- C. Apply a CIDR range filter to the spoke
- D. Add the published service as a producer spoke

### 38. A payment namespace must accept traffic only from the checkout namespace. What should be created?

- A. Configure an IP masquerade policy on the node pool
- B. Enable GKE Dataplane V2
- C. Add a second pod range to the cluster
- D. Create a GKE network policy for the namespace

### 39. A partner firewall drops pod traffic because it never saw those addresses. What should be configured?

- A. Enable GKE Dataplane V2
- B. Add a second pod range to the cluster
- C. Resize the service range allocation
- D. Configure an IP masquerade policy on the node pool

### 40. Batch jobs exhaust pod addresses every night and the cluster cannot be rebuilt. What should be added?

- A. Add a second pod range to the cluster
- B. Deploy the cluster into a shared subnet
- C. Resize the service range allocation
- D. Plan secondary ranges for pods and services

### 41. A team must see which external hosts a subnet talks to and how much it sends. What should be enabled?

- A. Enable VPC Flow Logs on the subnet
- B. Enable firewall rules logging
- C. Enable Cloud NAT logging
- D. Enable Cloud DNS query logging

---

## Domain 3 — Configuring Managed Network Services (Load Balancing, Cloud CDN, and Cloud DNS)

### 42. A new front end needs a pool of backends with a check that removes unhealthy members. Which two objects are required? Select two.

- A. Add the backends to a backend service behind the front end
- B. Route by URL path in the URL map
- C. Split traffic between two backend services by weight
- D. Attach a health check to the backend service
- E. Register the backends as a zonal network endpoint group

### 43. A checkout flow stores a cart on the instance and users lose it mid-flow. What should be enabled?

- A. Enable connection draining with a timeout
- B. Switch the balancing mode to connections per instance
- C. Autoscale a managed instance group behind the backend service
- D. Enable session affinity on the backend service

### 44. A container workload has no instance group and pods must be addressed directly. What should be registered?

- A. Register the backends as a zonal network endpoint group
- B. Register the serverless service as a serverless network endpoint group
- C. Autoscale a managed instance group behind the backend service
- D. Register the third-party origins as an internet network endpoint group

### 45. A migration needs one percent of live requests on the new backend. What should be configured?

- A. Split traffic between two backend services by weight
- B. Mirror a copy of the traffic to a second backend
- C. Route by URL path in the URL map
- D. Rewrite the request path before it reaches the backend

### 46. Two services share a hostname and are separated only by path. What selects between them?

- A. Route by URL path in the URL map
- B. Mirror a copy of the traffic to a second backend
- C. Rewrite the request path before it reaches the backend
- D. Split traffic between two backend services by weight

### 47. A front end must add instances when CPU rises. What should be attached to the group?

- A. Autoscale a managed instance group behind the backend service
- B. Register the serverless service as a serverless network endpoint group
- C. Switch the balancing mode to connections per instance
- D. Register the backends as a zonal network endpoint group

### 48. A legacy origin outside Google Cloud must be a backend for the global front end. What should be created?

- A. Add the backends to a backend service behind the front end
- B. Register the third-party origins as an internet network endpoint group
- C. Register the serverless service as a serverless network endpoint group
- D. Register the backends as a zonal network endpoint group

### 49. Several teams need one shared entry point with per-route policy. What fits?

- A. Register the backends as a zonal network endpoint group
- B. Expose the workload through the GKE Ingress controller
- C. Route by URL path in the URL map
- D. Expose the workload through the GKE Gateway controller

### 50. A workload needs an external load balancer created from one Kubernetes object. What fits?

- A. Split traffic between two backend services by weight
- B. Route by URL path in the URL map
- C. Expose the workload through the GKE Gateway controller
- D. Expose the workload through the GKE Ingress controller

### 51. Paid video must be cached near viewers and served only to entitled users. Which two choices fit? Select two.

- A. Raise the cache time to live
- B. Point Cloud CDN at the origins through an internet endpoint group
- C. Invalidate the cached object after the change
- D. Enable Cloud CDN on the backend service
- E. Serve the object through a signed URL

### 52. A legal notice requires that a removed document stop being served immediately. What should be done?

- A. Raise the cache time to live
- B. Invalidate the cached object after the change
- C. Enable Cloud CDN on the backend service
- D. Register the third-party origins as an internet network endpoint group

### 53. A cutover needs an automatic standby answer and a fast switch between addresses. Which two settings fit? Select two.

- A. Migrate the zone with a staged import and a delegated test
- B. Create a public Cloud DNS zone
- C. Lower the record TTL before the cutover
- D. Apply a failover routing policy with a health-checked primary
- E. Apply a geolocation routing policy to the record set

### 54. A new marketing domain must resolve for anyone on the internet. Which zone type fits?

- A. Create a public Cloud DNS zone
- B. Serve split-horizon answers from separate private and public zones
- C. Enable DNSSEC on the zone
- D. Create a private Cloud DNS zone

### 55. Traffic from each country must land in its own regional cluster. Which policy fits?

- A. Apply a geolocation routing policy to the record set
- B. Apply a failover routing policy with a health-checked primary
- C. Migrate the zone with a staged import and a delegated test
- D. Lower the record TTL before the cutover

### 56. A secondary region must answer only during a primary outage. Which policy fits?

- A. Enable DNSSEC on the zone
- B. Lower the record TTL before the cutover
- C. Apply a failover routing policy with a health-checked primary
- D. Apply a geolocation routing policy to the record set

### 57. A security review demands proof that public answers are authentic. What should be enabled?

- A. Enable DNSSEC on the zone
- B. Enable Cloud DNS query logging
- C. Create a private Cloud DNS zone
- D. Migrate the zone with a staged import and a delegated test

---

## Domain 4 — Configuring and Implementing Hybrid and Multicloud Interconnectivity (Interconnect, VPN, and Cloud Router)

### 58. A manufacturer's own cage sits in a Google facility, and one subnet must reach its router over the circuit. Which two items fit? Select two.

- A. Deploy an HA VPN gateway with two interfaces
- B. Create a VLAN attachment on Cloud Router
- C. Enable MACsec on the interconnect
- D. Order a Dedicated Interconnect connection
- E. Order a Partner Interconnect connection

### 59. A site needs a 10 Gbps circuit but has no presence in any Google facility. Which fits?

- A. Order a Dedicated Interconnect connection
- B. Deploy a Classic VPN with a single tunnel
- C. Order a Partner Interconnect connection
- D. Order a Cross-Cloud Interconnect connection

### 60. A new attachment never leaves idle because the far side already uses 65001. What should be changed?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Set the Cloud Router ASN to a private value that differs from the peer
- C. Prefer the path with the lower multi-exit discriminator
- D. Create a VLAN attachment on Cloud Router

### 61. A migration must move data to another cloud without crossing the internet. What fits?

- A. Deploy an HA VPN gateway with two interfaces
- B. Order a Partner Interconnect connection
- C. Order a Cross-Cloud Interconnect connection
- D. Order a Dedicated Interconnect connection

### 62. A bank requires layer 2 encryption on its Dedicated Interconnect. What should be enabled?

- A. Run HA VPN over Cloud Interconnect instead of MACsec
- B. Enable MACsec on the interconnect
- C. Deploy an HA VPN gateway with two interfaces
- D. Create a VLAN attachment on Cloud Router

### 63. A legacy appliance supports policy-based selection and a single tunnel must be replaced by a redundant design. Which two choices fit? Select two.

- A. Order a Dedicated Interconnect connection
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Deploy an HA VPN gateway with two interfaces
- D. Prefer the path with the lower multi-exit discriminator
- E. Deploy a Classic VPN with a single tunnel

### 64. A remote site must survive the loss of one VPN gateway zone. What should be deployed?

- A. Deploy an HA VPN gateway with two interfaces
- B. Order a Dedicated Interconnect connection
- C. Create a VLAN attachment on Cloud Router
- D. Deploy a Classic VPN with a single tunnel

### 65. A tunnel fails and traffic keeps using it until the hold timer expires. What should be enabled?

- A. Enable Bidirectional Forwarding Detection with a short interval
- B. Switch best path selection back to the legacy behaviour
- C. Prefer the path with the lower multi-exit discriminator
- D. Set the Cloud Router ASN to a private value that differs from the peer

### 66. A device can only select traffic by policy and cannot run BGP. Which VPN fits?

- A. Deploy an HA VPN gateway with two interfaces
- B. Deploy a Classic VPN with a single tunnel
- C. Set the Cloud Router ASN to a private value that differs from the peer
- D. Order a Dedicated Interconnect connection

### 67. The peer must learn two summaries instead of every subnet. What should be configured?

- A. Switch best path selection back to the legacy behaviour
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Advertise only the ranges the peer needs
- D. Prefer the path with the lower multi-exit discriminator

### 68. Both circuits advertise the same prefix and the cheaper one must lose. What should be set?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Switch best path selection back to the legacy behaviour
- C. Give the static route a lower priority number than the learned route
- D. Prefer the path with the lower multi-exit discriminator

### 69. A new session will not establish, and the failure must be detected faster once it is up. Which two settings fit? Select two.

- A. Advertise only the ranges the peer needs
- B. Prefer the path with the lower multi-exit discriminator
- C. Enable Bidirectional Forwarding Detection with a short interval
- D. Switch best path selection back to the legacy behaviour
- E. Set the Cloud Router ASN to a private value that differs from the peer

### 70. A microwave link degrades without dropping and BGP never notices. What should be enabled?

- A. Set the Cloud Router ASN to a private value that differs from the peer
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Give the static route a lower priority number than the learned route
- D. Prefer the path with the lower multi-exit discriminator

### 71. A route learned in one region must be usable by a subnet in another. What should change?

- A. Keep the Cloud Router in regional dynamic routing mode
- B. Switch the Cloud Router to global dynamic routing mode
- C. Prefer the path with the lower multi-exit discriminator
- D. Give the static route a lower priority number than the learned route

### 72. An imported route must not override a local static route for the same prefix. What should be changed?

- A. Prefer the path with the lower multi-exit discriminator
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Give the static route a lower priority number than the learned route
- D. Switch best path selection back to the legacy behaviour

### 73. The interconnect hardware cannot do link encryption and the rule is mandatory. What should run over the circuit instead?

- A. Run HA VPN over Cloud Interconnect instead of MACsec
- B. Deploy an HA VPN gateway with two interfaces
- C. Enable MACsec on the interconnect
- D. Create a VLAN attachment on Cloud Router

---

## Domain 5 — Managing, Monitoring, and Troubleshooting Network Operations (Observability, Troubleshooting, and Traffic Movement)

### 74. A deny must be attributed to one specific rule for an audit. What should be enabled?

- A. Enable VPC Flow Logs on the subnet
- B. Enable Cloud NAT logging
- C. Enable Cloud DNS query logging
- D. Enable firewall rules logging

### 75. A security team needs the public address and port a private host used. What should be enabled?

- A. Enable VPC Flow Logs on the subnet
- B. Enable firewall rules logging
- C. Enable Cloud DNS query logging
- D. Enable Cloud NAT logging

### 76. An interconnect attachment must notify on call when it drops below a threshold. What should be created?

- A. Create a log-based metric from the firewall log entries
- B. Create an alert policy on the network metric
- C. Alert on the error budget of the service objective
- D. Publish a custom metric from the appliance

### 77. A specific denial message must be counted although no metric exists. What should be created?

- A. Alert on the error budget of the service objective
- B. Create a log-based metric from the firewall log entries
- C. Publish a custom metric from the appliance
- D. Create an alert policy on the network metric

### 78. A new firewall rule did not fix a blocked flow and the next step must be precise. What should be run?

- A. Inspect the flow in Network Topology
- B. Check the Performance Dashboard for packet loss
- C. Run a Connectivity Test between the two endpoints
- D. Query Flow Analyzer for the top talkers

### 79. A change window needs proof that a path works and a check for configuration risks. Which two tools fit? Select two.

- A. Enable Cloud DNS query logging
- B. Query Flow Analyzer for the top talkers
- C. Check the Performance Dashboard for packet loss
- D. Run a Connectivity Test between the two endpoints
- E. Read the Network Analyzer findings

### 80. A latency complaint spans Google and non-Google segments. What separates the two?

- A. Test the path with a large ping and the do-not-fragment bit
- B. Inspect the flow in Network Topology
- C. Query Flow Analyzer for the top talkers
- D. Check the Performance Dashboard for packet loss

### 81. A tunnel carries small packets and drops large ones with no error. What is the cause?

- A. Check the Performance Dashboard for packet loss
- B. Test the path with a large ping and the do-not-fragment bit
- C. Lower the tunnel MTU to 1460 bytes
- D. Leave the MTU mismatch unfixed

### 82. A rule was written and no traffic ever matched it. What should be reviewed?

- A. Query Flow Analyzer for the top talkers
- B. Run a Connectivity Test between the two endpoints
- C. Review Firewall Insights for shadowed rules
- D. Read the Network Analyzer findings

### 83. Quarterly hygiene must remove dead rules and surface quota pressure. Which two tools fit? Select two.

- A. Query Flow Analyzer for the top talkers
- B. Review Firewall Insights for shadowed rules
- C. Run a Connectivity Test between the two endpoints
- D. Check the Performance Dashboard for packet loss
- E. Read the Network Analyzer findings

### 84. The busiest inter-region flows must be ranked before a redesign. What should be queried?

- A. Check the Performance Dashboard for packet loss
- B. Review Firewall Insights for shadowed rules
- C. Query Flow Analyzer for the top talkers
- D. Inspect the flow in Network Topology

### 85. A diagram must show which links actually carry the traffic today. What should be opened?

- A. Check the Performance Dashboard for packet loss
- B. Inspect the flow in Network Topology
- C. Query Flow Analyzer for the top talkers
- D. Run a Connectivity Test between the two endpoints

### 86. One peer shows no received prefixes while the other shows many. What should be compared?

- A. Compare the BGP session state on both peers
- B. Enable Bidirectional Forwarding Detection with a short interval
- C. Run a Connectivity Test between the two endpoints
- D. Prefer the path with the lower multi-exit discriminator

### 87. A load balancer will be replaced and long-lived sessions must complete. What should be done first?

- A. Inspect the flow in Network Topology
- B. Drain the backend before removing it
- C. Enable connection draining with a timeout
- D. Query Flow Analyzer for the top talkers

---

## Domain 6 — Configuring, Implementing, and Managing a Cloud Network Security Solution (Cloud Armor, Cloud NGFW, NAT, and Egress Security)

### 88. A specific API path must be restricted to one country. What should be attached?

- A. Attach a Cloud Armor backend security policy
- B. Add a preconfigured WAF rule for the attack class
- C. Attach a Cloud Armor edge security policy
- D. Add a rate-based ban rule

### 89. A hostile range must be dropped before the proxy handles the request. What should be attached?

- A. Enable bot management on the policy
- B. Attach a Cloud Armor backend security policy
- C. Enable Adaptive Protection
- D. Attach a Cloud Armor edge security policy

### 90. A form endpoint is being probed with reflected script payloads. What should be added?

- A. Apply Google Threat Intelligence lists
- B. Enable Adaptive Protection
- C. Enable bot management on the policy
- D. Add a preconfigured WAF rule for the attack class

### 91. Automated clients must be split into allowed and blocked by behaviour. What fits?

- A. Add a preconfigured WAF rule for the attack class
- B. Enable bot management on the policy
- C. Enable Adaptive Protection
- D. Apply Google Threat Intelligence lists

### 92. A flood arrives from many addresses at once and must be absorbed. What should be relied on?

- A. Apply Google Threat Intelligence lists
- B. Enable Adaptive Protection
- C. Add a rate-based ban rule
- D. Rely on the default DDoS protection and add a rate limit

### 93. A rule must apply to every project, and another must cover every region of one network. Which two choices fit? Select two.

- A. Reorder the rules by priority
- B. Create a VPC firewall rule with a target tag
- C. Create a global network firewall policy
- D. Create a regional network firewall policy
- E. Create a hierarchical firewall policy at the organisation

### 94. A team must adopt the policy model and threat intelligence without payload inspection. Which tier fits?

- A. Stay on NGFW Essentials for the VPC rules
- B. Move the inspection to NGFW Enterprise
- C. Move the rules to NGFW Standard
- D. Create a VPC firewall rule with a target tag

### 95. A new deny rule has no effect because another rule already matched. What explains it?

- A. Add a deny-all egress rule with a higher priority
- B. Move the inspection to NGFW Enterprise
- C. Leave the default allow-ingress rule in place
- D. Reorder the rules by priority

### 96. Workloads reach the whole internet by default and only three hosts are allowed. What should be created?

- A. Leave the default allow-ingress rule in place
- B. Divide the network into micro-segmented tiers
- C. Reorder the rules by priority
- D. Add a deny-all egress rule with a higher priority

### 97. An existing rule targets instances by a tag that any owner can set. What risk does that carry?

- A. Target the rule with a service account
- B. Use secure tags as the rule target
- C. Target the rule with network tags
- D. Create a hierarchical firewall policy at the organisation

### 98. A NAT gateway must guarantee port capacity per instance during peak. What fits?

- A. Use automatic Cloud NAT IP allocation
- B. Use dynamic port allocation
- C. Assign a manual static Cloud NAT address
- D. Use static port allocation

### 99. Egress must be filtered by domain category with TLS inspection. What fits?

- A. Deploy Secure Web Proxy as the egress path
- B. Deploy a multi-NIC appliance VM between the two networks
- C. Assign a manual static Cloud NAT address
- D. Configure Packet Mirroring on the instance group

### 100. Inspection must happen inline between two networks that cannot be peered. What should be deployed?

- A. Add a policy-based route that matches the source and destination
- B. Configure Packet Mirroring on the instance group
- C. Use the internal load balancer as the next hop
- D. Deploy a multi-NIC appliance VM between the two networks

---

## Answer key and explanations

### Question 1 — C

Answer: Use the Premium network service tier. Premium hands each viewer to the nearest Google edge and carries the stream to a region. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: Premium hands each viewer to the nearest Google edge and carries the stream to a region.
- **B:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: Premium hands each viewer to the nearest Google edge and carries the stream to a region.
- **C:** Correct. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. In this case: Premium hands each viewer to the nearest Google edge and carries the stream to a region.
- **D:** Incorrect for this question. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Why the correct answer wins: Premium hands each viewer to the nearest Google edge and carries the stream to a region.

### Question 2 — C

Answer: Use the Standard network service tier. Standard keeps long-haul traffic on the public internet, which costs less here. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. Local study-map skill 1.1 (Network Service Tier Choice), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates TLS and forwards a separate connection to the backend. Why the correct answer wins: Standard keeps long-haul traffic on the public internet, which costs less here.
- **B:** Incorrect for this question. Traffic enters the Google network at the edge closest to the user and crosses it to the serving region. Why the correct answer wins: Standard keeps long-haul traffic on the public internet, which costs less here.
- **C:** Correct. Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet. In this case: Standard keeps long-haul traffic on the public internet, which costs less here.
- **D:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Standard keeps long-haul traffic on the public internet, which costs less here.

### Question 3 — B

Answer: Deploy a global external Application Load Balancer. One global anycast address reaches every continent and avoids failed regions. A global anycast address routes each user to the closest healthy region. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: One global anycast address reaches every continent and avoids failed regions.
- **B:** Correct. A global anycast address routes each user to the closest healthy region. In this case: One global anycast address reaches every continent and avoids failed regions.
- **C:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: One global anycast address reaches every continent and avoids failed regions.
- **D:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: One global anycast address reaches every continent and avoids failed regions.

### Question 4 — B, C

Answers: Deploy a global external Application Load Balancer; Attach a health check to the backend service. The global front end picks the closest healthy region, and the health check removes the failing backends. A global anycast address routes each user to the closest healthy region. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 1.2 (High Availability, Failover, and DR Design), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Affinity keeps a client on the backend that already holds its session state. Why the correct answer wins: The global front end picks the closest healthy region, and the health check removes the failing backends.
- **B:** Correct. A global anycast address routes each user to the closest healthy region. In this case: The global front end picks the closest healthy region, and the health check removes the failing backends.
- **C:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The global front end picks the closest healthy region, and the health check removes the failing backends.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The global front end picks the closest healthy region, and the health check removes the failing backends.
- **E:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: The global front end picks the closest healthy region, and the health check removes the failing backends.

### Question 5 — D

Answer: Create a DNS peering zone to the other project. A DNS peering zone resolves through the zone that owns the names. The consumer project resolves names from the producer project through a peering zone. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The binding makes the host project's zone answer for the service project's networks. Why the correct answer wins: A DNS peering zone resolves through the zone that owns the names.
- **B:** Incorrect for this question. On-premises resolvers send queries to that address to reach Cloud DNS names. Why the correct answer wins: A DNS peering zone resolves through the zone that owns the names.
- **C:** Incorrect for this question. Queries for the corporate suffix are forwarded to the on-premises resolvers. Why the correct answer wins: A DNS peering zone resolves through the zone that owns the names.
- **D:** Correct. The consumer project resolves names from the producer project through a peering zone. In this case: A DNS peering zone resolves through the zone that owns the names.

### Question 6 — C

Answer: Serve split-horizon answers from separate private and public zones. Separate private and public zones give each audience its own answer. Internal clients resolve the internal address while external clients resolve the public one. Local study-map skill 1.3 (Hybrid DNS Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: Separate private and public zones give each audience its own answer.
- **B:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: Separate private and public zones give each audience its own answer.
- **C:** Correct. Internal clients resolve the internal address while external clients resolve the public one. In this case: Separate private and public zones give each audience its own answer.
- **D:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: Separate private and public zones give each audience its own answer.

### Question 7 — B

Answer: Deploy an internal passthrough Network Load Balancer. An internal front end has no public address and is reachable only internally. The front end is an internal address reachable only from inside the VPC or its connected networks. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates the client connection and opens a separate one to the backend. Why the correct answer wins: An internal front end has no public address and is reachable only internally.
- **B:** Correct. The front end is an internal address reachable only from inside the VPC or its connected networks. In this case: An internal front end has no public address and is reachable only internally.
- **C:** Incorrect for this question. Packets keep their client source address and the backend sees the original flow. Why the correct answer wins: An internal front end has no public address and is reachable only internally.
- **D:** Incorrect for this question. A global anycast address routes each user to the closest healthy region. Why the correct answer wins: An internal front end has no public address and is reachable only internally.

### Question 8 — B

Answer: Deploy a global external Application Load Balancer. The global front end terminates TLS for the single hostname and routes by region. A global anycast address routes each user to the closest healthy region. Local study-map skill 1.4 (Load Balancer Selection), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The proxy terminates TLS and forwards a separate connection to the backend. Why the correct answer wins: The global front end terminates TLS for the single hostname and routes by region.
- **B:** Correct. A global anycast address routes each user to the closest healthy region. In this case: The global front end terminates TLS for the single hostname and routes by region.
- **C:** Incorrect for this question. The front end is an internal address reachable only from inside the VPC or its connected networks. Why the correct answer wins: The global front end terminates TLS for the single hostname and routes by region.
- **D:** Incorrect for this question. The front end is regional, so users are served from the region the address belongs to. Why the correct answer wins: The global front end terminates TLS for the single hostname and routes by region.

### Question 9 — A

Answer: Add the office range to the authorised networks. Authorised networks admit the named ranges and refuse the rest. The named range may reach the control plane endpoint even when it is public. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The named range may reach the control plane endpoint even when it is public. In this case: Authorised networks admit the named ranges and refuse the rest.
- **B:** Incorrect for this question. The API server is reachable only through the internal address or an authorised network. Why the correct answer wins: Authorised networks admit the named ranges and refuse the rest.
- **C:** Incorrect for this question. Nodes reach the control plane and Google APIs through internal paths only. Why the correct answer wins: Authorised networks admit the named ranges and refuse the rest.
- **D:** Incorrect for this question. The endpoint resolves through a private DNS name instead of a fixed address. Why the correct answer wins: Authorised networks admit the named ranges and refuse the rest.

### Question 10 — D

Answer: Enable dual-stack IPv6 on the subnet. Dual-stack gives the subnet and pods both address families. The subnet carries both an IPv4 range and an internal or external IPv6 range. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Dual-stack gives the subnet and pods both address families.
- **B:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: Dual-stack gives the subnet and pods both address families.
- **C:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Dual-stack gives the subnet and pods both address families.
- **D:** Correct. The subnet carries both an IPv4 range and an internal or external IPv6 range. In this case: Dual-stack gives the subnet and pods both address families.

### Question 11 — D, E

Answers: Use private nodes with no external addresses; Use a private control plane endpoint. Private nodes remove external node addresses, and the private endpoint removes the public API address. Nodes reach the control plane and Google APIs through internal paths only. The API server is reachable only through the internal address or an authorised network. Local study-map skill 1.5 (GKE Network Planning), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The named range may reach the control plane endpoint even when it is public. Why the correct answer wins: Private nodes remove external node addresses, and the private endpoint removes the public API address.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Private nodes remove external node addresses, and the private endpoint removes the public API address.
- **C:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: Private nodes remove external node addresses, and the private endpoint removes the public API address.
- **D:** Correct. The API server is reachable only through the internal address or an authorised network. In this case: Private nodes remove external node addresses, and the private endpoint removes the public API address.
- **E:** Correct. Nodes reach the control plane and Google APIs through internal paths only. In this case: Private nodes remove external node addresses, and the private endpoint removes the public API address.

### Question 12 — C

Answer: Grant the subnet user role on the specific shared subnets. Subnet user permits use of that subnet and nothing more. The role lets a service project deploy into the named subnets and nothing else. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Subnet user permits use of that subnet and nothing more.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Subnet user permits use of that subnet and nothing more.
- **C:** Correct. The role lets a service project deploy into the named subnets and nothing else. In this case: Subnet user permits use of that subnet and nothing more.
- **D:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: Subnet user permits use of that subnet and nothing more.

### Question 13 — A, C

Answers: Create a custom role with only the required network permissions; Grant the network administrator role in the host project. A custom role names exactly those permissions, and the network administrator role covers the subnet work. The custom role names the exact permissions the automation needs. That role creates and changes networks and subnets, which a service team should not hold. Local study-map skill 1.6 (IAM for Network Roles), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The custom role names the exact permissions the automation needs. In this case: A custom role names exactly those permissions, and the network administrator role covers the subnet work.
- **B:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: A custom role names exactly those permissions, and the network administrator role covers the subnet work.
- **C:** Correct. That role creates and changes networks and subnets, which a service team should not hold. In this case: A custom role names exactly those permissions, and the network administrator role covers the subnet work.
- **D:** Incorrect for this question. That role attaches service projects and delegates subnet use. Why the correct answer wins: A custom role names exactly those permissions, and the network administrator role covers the subnet work.
- **E:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: A custom role names exactly those permissions, and the network administrator role covers the subnet work.

### Question 14 — B

Answer: Allocate a private services access range. A reserved private services range gives the provider somewhere to place the instance. A reserved internal range lets a managed service provider peer into the VPC. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.
- **B:** Correct. A reserved internal range lets a managed service provider peer into the VPC. In this case: A reserved private services range gives the provider somewhere to place the instance.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.
- **D:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: A reserved private services range gives the provider somewhere to place the instance.

### Question 15 — A, B

Answers: Create a Private Service Connect endpoint; Use Direct VPC egress for the serverless workload. A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address. A private endpoint inside the consumer VPC targets a published service attachment. The workload receives its own address in the subnet instead of going through a connector. Local study-map skill 1.7 (Private Service Connectivity), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A private endpoint inside the consumer VPC targets a published service attachment. In this case: A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address.
- **B:** Correct. The workload receives its own address in the subnet instead of going through a connector. In this case: A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address.
- **C:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address.
- **D:** Incorrect for this question. A reserved internal range lets a managed service provider peer into the VPC. Why the correct answer wins: A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address.
- **E:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: A private endpoint reaches the partner attachment, and direct egress gives the revision a subnet address.

### Question 16 — C

Answer: Peer every VPC network with every other VPC network. A full mesh gives each network a direct peering to every other. A full mesh of peering sessions gives each network a direct path to all the others. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A central network peers with each leaf network, and the leaves do not peer with each other. Why the correct answer wins: A full mesh gives each network a direct peering to every other.
- **B:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: A full mesh gives each network a direct peering to every other.
- **C:** Correct. A full mesh of peering sessions gives each network a direct path to all the others. In this case: A full mesh gives each network a direct peering to every other.
- **D:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: A full mesh gives each network a direct peering to every other.

### Question 17 — D

Answer: Connect the networks as a hub-and-spoke peering topology. A hub-and-spoke peering reaches the centre without joining the branches. A central network peers with each leaf network, and the leaves do not peer with each other. Local study-map skill 1.8 (VPC Type and Interconnect Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two networks exchange routes directly without a gateway or a shared project. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches.
- **B:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches.
- **C:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: A hub-and-spoke peering reaches the centre without joining the branches.
- **D:** Correct. A central network peers with each leaf network, and the leaves do not peer with each other. In this case: A hub-and-spoke peering reaches the centre without joining the branches.

### Question 18 — A

Answer: Use privately used public IP address ranges. Privately used public ranges add space that is never advertised. Public ranges that are never advertised are used internally to gain address space without NAT. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Public ranges that are never advertised are used internally to gain address space without NAT. In this case: Privately used public ranges add space that is never advertised.
- **B:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Privately used public ranges add space that is never advertised.
- **C:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Privately used public ranges add space that is never advertised.
- **D:** Incorrect for this question. Source addresses are translated so two networks with the same private ranges can still talk. Why the correct answer wins: Privately used public ranges add space that is never advertised.

### Question 19 — C

Answer: Deploy Private NAT for the overlapping ranges. Private NAT translates the source so the identical ranges can still exchange traffic. Source addresses are translated so two networks with the same private ranges can still talk. Local study-map skill 1.9 (IP Address Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Private NAT translates the source so the identical ranges can still exchange traffic.
- **B:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Private NAT translates the source so the identical ranges can still exchange traffic.
- **C:** Correct. Source addresses are translated so two networks with the same private ranges can still talk. In this case: Private NAT translates the source so the identical ranges can still exchange traffic.
- **D:** Incorrect for this question. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Why the correct answer wins: Private NAT translates the source so the identical ranges can still exchange traffic.

### Question 20 — D

Answer: Raise the VPC MTU to 8896 bytes. A larger MTU carries more data per packet where the path supports it. A larger maximum transmission unit carries more payload per packet inside the VPC. Local study-map skill 1.10 (MTU Sizing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The default MTU matches ordinary Ethernet frames and needs no adjustment. Why the correct answer wins: A larger MTU carries more data per packet where the path supports it.
- **B:** Incorrect for this question. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Why the correct answer wins: A larger MTU carries more data per packet where the path supports it.
- **C:** Incorrect for this question. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Why the correct answer wins: A larger MTU carries more data per packet where the path supports it.
- **D:** Correct. A larger maximum transmission unit carries more payload per packet inside the VPC. In this case: A larger MTU carries more data per packet where the path supports it.

### Question 21 — C

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches the destination range and forwards to the appliance. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 1.11 (Third-Party Appliance Insertion), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 1 (designing and planning a Google Cloud VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A policy-based route matches the destination range and forwards to the appliance.
- **B:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches the destination range and forwards to the appliance.
- **C:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches the destination range and forwards to the appliance.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches the destination range and forwards to the appliance.

### Question 22 — A

Answer: Enable dual-stack IPv6 on the subnet. Dual-stack adds an IPv6 range beside the existing IPv4 range. The subnet carries both an IPv4 range and an internal or external IPv6 range. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The subnet carries both an IPv4 range and an internal or external IPv6 range. In this case: Dual-stack adds an IPv6 range beside the existing IPv4 range.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Dual-stack adds an IPv6 range beside the existing IPv4 range.
- **C:** Incorrect for this question. A subnet prefix can grow within its address range, and the growth cannot shrink later. Why the correct answer wins: Dual-stack adds an IPv6 range beside the existing IPv4 range.
- **D:** Incorrect for this question. Public ranges that are never advertised are used internally to gain address space without NAT. Why the correct answer wins: Dual-stack adds an IPv6 range beside the existing IPv4 range.

### Question 23 — A, C

Answers: Expand the existing subnet range; Automate address allocation from a central IPAM plan. Growing each prefix adds space, and central allocation stops the overlaps. A subnet prefix can grow within its address range, and the growth cannot shrink later. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. Local study-map skill 2.1 (VPC and Subnet Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Allocation is generated from one authoritative plan instead of hand-picked ranges per team. In this case: Growing each prefix adds space, and central allocation stops the overlaps.
- **B:** Incorrect for this question. Public prefixes the organisation already owns are advertised from Google Cloud. Why the correct answer wins: Growing each prefix adds space, and central allocation stops the overlaps.
- **C:** Correct. A subnet prefix can grow within its address range, and the growth cannot shrink later. In this case: Growing each prefix adds space, and central allocation stops the overlaps.
- **D:** Incorrect for this question. Two subnets with the same prefix cannot be routed to each other without translation. Why the correct answer wins: Growing each prefix adds space, and central allocation stops the overlaps.
- **E:** Incorrect for this question. The internal network uses address space outside the private ranges to avoid collisions later. Why the correct answer wins: Growing each prefix adds space, and central allocation stops the overlaps.

### Question 24 — B

Answer: Import and export custom routes over the peering. Exporting custom routes carries policy-based routes to the peer. The peering option carries static and policy-based routes between the two networks. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Peering is not transitive, so a route learned through one peer is not passed on to another. Why the correct answer wins: Exporting custom routes carries policy-based routes to the peer.
- **B:** Correct. The peering option carries static and policy-based routes between the two networks. In this case: Exporting custom routes carries policy-based routes to the peer.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: Exporting custom routes carries policy-based routes to the peer.
- **D:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: Exporting custom routes carries policy-based routes to the peer.

### Question 25 — B

Answer: Create a VPC Network Peering connection between the two networks. Peering joins the two networks directly with no shared project. Two networks exchange routes directly without a gateway or a shared project. Local study-map skill 2.2 (VPC Network Peering), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. One host project owns the network and subnets while service projects deploy into shared subnets. Why the correct answer wins: Peering joins the two networks directly with no shared project.
- **B:** Correct. Two networks exchange routes directly without a gateway or a shared project. In this case: Peering joins the two networks directly with no shared project.
- **C:** Incorrect for this question. A full mesh of peering sessions gives each network a direct path to all the others. Why the correct answer wins: Peering joins the two networks directly with no shared project.
- **D:** Incorrect for this question. A hub groups spokes so the connected networks reach each other through one managed topology. Why the correct answer wins: Peering joins the two networks directly with no shared project.

### Question 26 — A

Answer: Grant Shared VPC Admin on the host project. Shared VPC Admin attaches the consumers and delegates the subnets. That role attaches service projects and delegates subnet use. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC Admin attaches the consumers and delegates the subnets.
- **B:** Incorrect for this question. That role creates and changes networks and subnets, which a service team should not hold. Why the correct answer wins: Shared VPC Admin attaches the consumers and delegates the subnets.
- **C:** Incorrect for this question. The custom role names the exact permissions the automation needs. Why the correct answer wins: Shared VPC Admin attaches the consumers and delegates the subnets.
- **D:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: Shared VPC Admin attaches the consumers and delegates the subnets.

### Question 27 — B, D

Answers: Build the network as a Shared VPC with host and service projects; Grant Shared VPC Admin on the host project. Shared VPC centralises the network, and the admin role keeps attachment control with the platform team. One host project owns the network and subnets while service projects deploy into shared subnets. That role attaches service projects and delegates subnet use. Local study-map skill 2.3 (Shared VPC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Editor spans most services, so it can delete far more than the network resources involved. Why the correct answer wins: Shared VPC centralises the network, and the admin role keeps attachment control with the platform team.
- **B:** Correct. That role attaches service projects and delegates subnet use. In this case: Shared VPC centralises the network, and the admin role keeps attachment control with the platform team.
- **C:** Incorrect for this question. The role lets a service project deploy into the named subnets and nothing else. Why the correct answer wins: Shared VPC centralises the network, and the admin role keeps attachment control with the platform team.
- **D:** Correct. One host project owns the network and subnets while service projects deploy into shared subnets. In this case: Shared VPC centralises the network, and the admin role keeps attachment control with the platform team.
- **E:** Incorrect for this question. Separate projects own separate networks, and nothing is shared implicitly. Why the correct answer wins: Shared VPC centralises the network, and the admin role keeps attachment control with the platform team.

### Question 28 — B

Answer: Enable Private Google Access on the subnet. Private Google Access reaches the registry over internal routing. Instances without external addresses reach Google APIs through internal routing. Local study-map skill 2.4 (Private Google Access and APIs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private endpoint inside the consumer VPC targets a published service attachment. Why the correct answer wins: Private Google Access reaches the registry over internal routing.
- **B:** Correct. Instances without external addresses reach Google APIs through internal routing. In this case: Private Google Access reaches the registry over internal routing.
- **C:** Incorrect for this question. The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement. Why the correct answer wins: Private Google Access reaches the registry over internal routing.
- **D:** Incorrect for this question. A serverless runtime gets a path into the VPC through a connector or direct egress. Why the correct answer wins: Private Google Access reaches the registry over internal routing.

### Question 29 — A

Answer: Enclose the project in a VPC Service Controls perimeter. The service perimeter blocks reads across its boundary. The perimeter restricts which services the project may call and blocks data movement outside it. Local study-map skill 2.5 (VPC Service Controls Perimeters), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The perimeter restricts which services the project may call and blocks data movement outside it. In this case: The service perimeter blocks reads across its boundary.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: The service perimeter blocks reads across its boundary.
- **C:** Incorrect for this question. Instances without external addresses reach Google APIs through internal routing. Why the correct answer wins: The service perimeter blocks reads across its boundary.
- **D:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: The service perimeter blocks reads across its boundary.

### Question 30 — B

Answer: Give the static route a lower priority number than the learned route. The lower priority number wins between routes for one prefix. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The lower priority number wins between routes for one prefix.
- **B:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: The lower priority number wins between routes for one prefix.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The lower priority number wins between routes for one prefix.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The lower priority number wins between routes for one prefix.

### Question 31 — C

Answer: Switch the Cloud Router to global dynamic routing mode. Global mode makes the learned routes available in every region. Routes learned in one region are available to subnets in every region. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: Global mode makes the learned routes available in every region.
- **B:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global mode makes the learned routes available in every region.
- **C:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global mode makes the learned routes available in every region.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global mode makes the learned routes available in every region.

### Question 32 — B, C

Answers: Prefer the path with the lower multi-exit discriminator; Switch best path selection back to the legacy behaviour. The discriminator ranks the two paths, and the selection order breaks the remaining tie. The lower discriminator wins when the same prefix arrives over two attachments. The older selection order picks a different preferred path when the inputs tie. Local study-map skill 2.6 (Static and Dynamic Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: The discriminator ranks the two paths, and the selection order breaks the remaining tie.
- **B:** Correct. The older selection order picks a different preferred path when the inputs tie. In this case: The discriminator ranks the two paths, and the selection order breaks the remaining tie.
- **C:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: The discriminator ranks the two paths, and the selection order breaks the remaining tie.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: The discriminator ranks the two paths, and the selection order breaks the remaining tie.
- **E:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The discriminator ranks the two paths, and the selection order breaks the remaining tie.

### Question 33 — C

Answer: Add a policy-based route that matches the source and destination. A policy-based route matches the source and forwards to the appliance. The route forwards matching flows to the appliance even when the destination is not the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: A policy-based route matches the source and forwards to the appliance.
- **B:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A policy-based route matches the source and forwards to the appliance.
- **C:** Correct. The route forwards matching flows to the appliance even when the destination is not the appliance. In this case: A policy-based route matches the source and forwards to the appliance.
- **D:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: A policy-based route matches the source and forwards to the appliance.

### Question 34 — B

Answer: Create a static route with a tag-scoped next hop. A tag-scoped static route affects only the instances that carry the tag. Only instances carrying the tag send their traffic through the appliance. Local study-map skill 2.7 (Policy-Based Routing), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A tag-scoped static route affects only the instances that carry the tag.
- **B:** Correct. Only instances carrying the tag send their traffic through the appliance. In this case: A tag-scoped static route affects only the instances that carry the tag.
- **C:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: A tag-scoped static route affects only the instances that carry the tag.
- **D:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: A tag-scoped static route affects only the instances that carry the tag.

### Question 35 — C

Answer: Use the internal load balancer as the next hop. The internal load balancer hides instance replacement from the route. Traffic reaches whichever appliance instance the internal front end selects. Local study-map skill 2.8 (Internal Load Balancer as Next Hop), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Only instances carrying the tag send their traffic through the appliance. Why the correct answer wins: The internal load balancer hides instance replacement from the route.
- **B:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: The internal load balancer hides instance replacement from the route.
- **C:** Correct. Traffic reaches whichever appliance instance the internal front end selects. In this case: The internal load balancer hides instance replacement from the route.
- **D:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: The internal load balancer hides instance replacement from the route.

### Question 36 — A

Answer: Add the published service as a producer spoke. A producer spoke publishes the attachment to the hub. The spoke publishes a service attachment so consumers reach it through the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The spoke publishes a service attachment so consumers reach it through the hub. In this case: A producer spoke publishes the attachment to the hub.
- **B:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A producer spoke publishes the attachment to the hub.
- **C:** Incorrect for this question. Only the matching prefixes are exchanged with the hub. Why the correct answer wins: A producer spoke publishes the attachment to the hub.
- **D:** Incorrect for this question. The spoke carries the VLAN attachment or VPN into the hub. Why the correct answer wins: A producer spoke publishes the attachment to the hub.

### Question 37 — C

Answer: Apply a CIDR range filter to the spoke. A CIDR filter limits the prefixes the spoke shares. Only the matching prefixes are exchanged with the hub. Local study-map skill 2.9 (Network Connectivity Center), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The spoke exports the network subnets to the hub. Why the correct answer wins: A CIDR filter limits the prefixes the spoke shares.
- **B:** Incorrect for this question. The hub forwards between spokes, which peering alone cannot do. Why the correct answer wins: A CIDR filter limits the prefixes the spoke shares.
- **C:** Correct. Only the matching prefixes are exchanged with the hub. In this case: A CIDR filter limits the prefixes the spoke shares.
- **D:** Incorrect for this question. The spoke publishes a service attachment so consumers reach it through the hub. Why the correct answer wins: A CIDR filter limits the prefixes the spoke shares.

### Question 38 — D

Answer: Create a GKE network policy for the namespace. A network policy restricts which pods may reach the selected pods. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Outbound pod traffic is translated to the node address under the chosen conditions. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **B:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **C:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: A network policy restricts which pods may reach the selected pods.
- **D:** Correct. In this case: A network policy restricts which pods may reach the selected pods.

### Question 39 — D

Answer: Configure an IP masquerade policy on the node pool. Masquerading presents the node address instead of the pod address. Outbound pod traffic is translated to the node address under the chosen conditions. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The eBPF dataplane handles policy and service routing inside the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **B:** Incorrect for this question. An additional alias range gives pods more addresses without rebuilding the cluster. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **C:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: Masquerading presents the node address instead of the pod address.
- **D:** Correct. Outbound pod traffic is translated to the node address under the chosen conditions. In this case: Masquerading presents the node address instead of the pod address.

### Question 40 — A

Answer: Add a second pod range to the cluster. An extra pod range gives the cluster more alias addresses without a rebuild. An additional alias range gives pods more addresses without rebuilding the cluster. Local study-map skill 2.10 (GKE Cluster Networking), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. An additional alias range gives pods more addresses without rebuilding the cluster. In this case: An extra pod range gives the cluster more alias addresses without a rebuild.
- **B:** Incorrect for this question. The cluster consumes subnets that the host project owns. Why the correct answer wins: An extra pod range gives the cluster more alias addresses without a rebuild.
- **C:** Incorrect for this question. The service address range must have room for the services the cluster will run. Why the correct answer wins: An extra pod range gives the cluster more alias addresses without a rebuild.
- **D:** Incorrect for this question. Alias ranges give pods and services addresses that are separate from the node subnet. Why the correct answer wins: An extra pod range gives the cluster more alias addresses without a rebuild.

### Question 41 — A

Answer: Enable VPC Flow Logs on the subnet. Flow logs record destinations, ports and byte counts per sampled connection. The logs record sampled connections with source, destination, port and byte counts. Local study-map skill 2.11 (VPC Flow Logs), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 2 (implementing a VPC network): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The logs record sampled connections with source, destination, port and byte counts. In this case: Flow logs record destinations, ports and byte counts per sampled connection.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: Flow logs record destinations, ports and byte counts per sampled connection.
- **C:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Flow logs record destinations, ports and byte counts per sampled connection.
- **D:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Flow logs record destinations, ports and byte counts per sampled connection.

### Question 42 — A, D

Answers: Add the backends to a backend service behind the front end; Attach a health check to the backend service. The backend service holds the pool, and the health check decides membership. The backend service holds the health check, balancing mode and capacity settings. The check removes a backend that cannot answer, so traffic moves to a healthy one. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The backend service holds the health check, balancing mode and capacity settings. In this case: The backend service holds the pool, and the health check decides membership.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The backend service holds the pool, and the health check decides membership.
- **C:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The backend service holds the pool, and the health check decides membership.
- **D:** Correct. The check removes a backend that cannot answer, so traffic moves to a healthy one. In this case: The backend service holds the pool, and the health check decides membership.
- **E:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The backend service holds the pool, and the health check decides membership.

### Question 43 — D

Answer: Enable session affinity on the backend service. Affinity keeps each user on the instance holding their cart. Affinity keeps a client on the backend that already holds its session state. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Affinity keeps each user on the instance holding their cart.
- **B:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: Affinity keeps each user on the instance holding their cart.
- **C:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: Affinity keeps each user on the instance holding their cart.
- **D:** Correct. Affinity keeps a client on the backend that already holds its session state. In this case: Affinity keeps each user on the instance holding their cart.

### Question 44 — A

Answer: Register the backends as a zonal network endpoint group. A zonal endpoint group addresses specific pod endpoints. Local study-map skill 3.1 (Load Balancer Backend Configuration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A zonal endpoint group addresses specific pod endpoints.
- **B:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: A zonal endpoint group addresses specific pod endpoints.
- **C:** Incorrect for this question. The group adds and removes instances as the autoscaling signal changes. Why the correct answer wins: A zonal endpoint group addresses specific pod endpoints.
- **D:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: A zonal endpoint group addresses specific pod endpoints.

### Question 45 — A

Answer: Split traffic between two backend services by weight. Weighted backends move that share onto the new service. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Weighted backends move that share onto the new service.
- **B:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: Weighted backends move that share onto the new service.
- **C:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: Weighted backends move that share onto the new service.
- **D:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: Weighted backends move that share onto the new service.

### Question 46 — A

Answer: Route by URL path in the URL map. The URL map chooses a backend from host and path. The map selects a backend service from the request host and path. Local study-map skill 3.2 (Traffic Management and URL Maps), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The map selects a backend service from the request host and path. In this case: The URL map chooses a backend from host and path.
- **B:** Incorrect for this question. The mirrored request is sent for inspection while the response comes only from the primary. Why the correct answer wins: The URL map chooses a backend from host and path.
- **C:** Incorrect for this question. The rewrite presents the backend with the path it expects without changing the client. Why the correct answer wins: The URL map chooses a backend from host and path.
- **D:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The URL map chooses a backend from host and path.

### Question 47 — A

Answer: Autoscale a managed instance group behind the backend service. The autoscaler adds members as utilisation climbs. The group adds and removes instances as the autoscaling signal changes. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The group adds and removes instances as the autoscaling signal changes. In this case: The autoscaler adds members as utilisation climbs.
- **B:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: The autoscaler adds members as utilisation climbs.
- **C:** Incorrect for this question. The mode spreads load by connection count rather than by CPU utilisation. Why the correct answer wins: The autoscaler adds members as utilisation climbs.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The autoscaler adds members as utilisation climbs.

### Question 48 — B

Answer: Register the third-party origins as an internet network endpoint group. An internet endpoint group targets external endpoints by hostname and port. Local study-map skill 3.3 (Network Endpoint Groups and Autoscaling), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The backend service holds the health check, balancing mode and capacity settings. Why the correct answer wins: An internet endpoint group targets external endpoints by hostname and port.
- **B:** Correct. In this case: An internet endpoint group targets external endpoints by hostname and port.
- **C:** Incorrect for this question. A serverless endpoint group fronts a Cloud Run service without a managed instance group. Why the correct answer wins: An internet endpoint group targets external endpoints by hostname and port.
- **D:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: An internet endpoint group targets external endpoints by hostname and port.

### Question 49 — D

Answer: Expose the workload through the GKE Gateway controller. The Gateway controller supports shared gateways with route-level policy. A Gateway object configures the load balancer through the newer Kubernetes API. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.
- **B:** Incorrect for this question. An Ingress object creates a Google Cloud load balancer from the manifest. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.
- **C:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Gateway controller supports shared gateways with route-level policy.
- **D:** Correct. A Gateway object configures the load balancer through the newer Kubernetes API. In this case: The Gateway controller supports shared gateways with route-level policy.

### Question 50 — D

Answer: Expose the workload through the GKE Ingress controller. The Ingress controller creates the load balancer from that object. An Ingress object creates a Google Cloud load balancer from the manifest. Local study-map skill 3.4 (GKE Ingress and Gateway), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Weighted backends move a chosen share of traffic onto the new service. Why the correct answer wins: The Ingress controller creates the load balancer from that object.
- **B:** Incorrect for this question. The map selects a backend service from the request host and path. Why the correct answer wins: The Ingress controller creates the load balancer from that object.
- **C:** Incorrect for this question. A Gateway object configures the load balancer through the newer Kubernetes API. Why the correct answer wins: The Ingress controller creates the load balancer from that object.
- **D:** Correct. An Ingress object creates a Google Cloud load balancer from the manifest. In this case: The Ingress controller creates the load balancer from that object.

### Question 51 — D, E

Answers: Enable Cloud CDN on the backend service; Serve the object through a signed URL. Caching shortens the fetch, and the signed link limits who may read it. The edge holds a copy of the response so later requests are served closer to the user. A signed URL authorises one object for a limited time without making the bucket public. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: Caching shortens the fetch, and the signed link limits who may read it.
- **B:** Incorrect for this question. An internet endpoint group lets the CDN cache responses from backends outside Google Cloud. Why the correct answer wins: Caching shortens the fetch, and the signed link limits who may read it.
- **C:** Incorrect for this question. Invalidation removes the stale copy so the next request fetches the current version. Why the correct answer wins: Caching shortens the fetch, and the signed link limits who may read it.
- **D:** Correct. The edge holds a copy of the response so later requests are served closer to the user. In this case: Caching shortens the fetch, and the signed link limits who may read it.
- **E:** Correct. A signed URL authorises one object for a limited time without making the bucket public. In this case: Caching shortens the fetch, and the signed link limits who may read it.

### Question 52 — B

Answer: Invalidate the cached object after the change. Invalidation drops the cached copy so it cannot be served again. Invalidation removes the stale copy so the next request fetches the current version. Local study-map skill 3.5 (Cloud CDN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A longer lifetime reduces origin load and lengthens the window in which content can be stale. Why the correct answer wins: Invalidation drops the cached copy so it cannot be served again.
- **B:** Correct. Invalidation removes the stale copy so the next request fetches the current version. In this case: Invalidation drops the cached copy so it cannot be served again.
- **C:** Incorrect for this question. The edge holds a copy of the response so later requests are served closer to the user. Why the correct answer wins: Invalidation drops the cached copy so it cannot be served again.
- **D:** Incorrect for this question. An internet endpoint group targets endpoints outside Google Cloud by hostname and port. Why the correct answer wins: Invalidation drops the cached copy so it cannot be served again.

### Question 53 — C, D

Answers: Apply a failover routing policy with a health-checked primary; Lower the record TTL before the cutover. The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch. The standby answer is served when the primary fails its health check. A short TTL lets resolvers pick up the new address quickly after the change. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch.
- **B:** Incorrect for this question. The zone answers queries from the internet for the domain it holds. Why the correct answer wins: The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch.
- **C:** Correct. A short TTL lets resolvers pick up the new address quickly after the change. In this case: The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch.
- **D:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch.
- **E:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy serves the standby when the primary is unhealthy, and a short TTL speeds the switch.

### Question 54 — A

Answer: Create a public Cloud DNS zone. A public zone answers queries from the internet. Local study-map skill 3.6 (Cloud DNS Zones and Records), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: A public zone answers queries from the internet.
- **B:** Incorrect for this question. Internal clients resolve the internal address while external clients resolve the public one. Why the correct answer wins: A public zone answers queries from the internet.
- **C:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: A public zone answers queries from the internet.
- **D:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: A public zone answers queries from the internet.

### Question 55 — A

Answer: Apply a geolocation routing policy to the record set. Geolocation answers from the source region of the query. The answer depends on the source region of the query. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The answer depends on the source region of the query. In this case: Geolocation answers from the source region of the query.
- **B:** Incorrect for this question. The standby answer is served when the primary fails its health check. Why the correct answer wins: Geolocation answers from the source region of the query.
- **C:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: Geolocation answers from the source region of the query.
- **D:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: Geolocation answers from the source region of the query.

### Question 56 — C

Answer: Apply a failover routing policy with a health-checked primary. The failover policy serves the standby only while the primary fails its check. The standby answer is served when the primary fails its health check. Local study-map skill 3.7 (DNS Routing Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Signatures let a resolver verify that the answer was not altered in transit. Why the correct answer wins: The failover policy serves the standby only while the primary fails its check.
- **B:** Incorrect for this question. A short TTL lets resolvers pick up the new address quickly after the change. Why the correct answer wins: The failover policy serves the standby only while the primary fails its check.
- **C:** Correct. The standby answer is served when the primary fails its health check. In this case: The failover policy serves the standby only while the primary fails its check.
- **D:** Incorrect for this question. The answer depends on the source region of the query. Why the correct answer wins: The failover policy serves the standby only while the primary fails its check.

### Question 57 — A

Answer: Enable DNSSEC on the zone. DNSSEC lets resolvers verify the answer's signature. Signatures let a resolver verify that the answer was not altered in transit. Local study-map skill 3.8 (DNSSEC), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 3 (configuring managed network services): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. Signatures let a resolver verify that the answer was not altered in transit. In this case: DNSSEC lets resolvers verify the answer's signature.
- **B:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: DNSSEC lets resolvers verify the answer's signature.
- **C:** Incorrect for this question. The zone answers only for clients inside the authorised networks. Why the correct answer wins: DNSSEC lets resolvers verify the answer's signature.
- **D:** Incorrect for this question. Records are loaded and verified before the registrar points at the new name servers. Why the correct answer wins: DNSSEC lets resolvers verify the answer's signature.

### Question 58 — B, D

Answers: Create a VLAN attachment on Cloud Router; Order a Dedicated Interconnect connection. The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router. The attachment carries one VLAN over the interconnect and peers with the router. A private physical circuit connects the premises to a Google colocation facility. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router.
- **B:** Correct. The attachment carries one VLAN over the interconnect and peers with the router. In this case: The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router.
- **C:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router.
- **D:** Correct. A private physical circuit connects the premises to a Google colocation facility. In this case: The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router.
- **E:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: The dedicated circuit uses its own cage, and the VLAN attachment carries the subnet to the router.

### Question 59 — C

Answer: Order a Partner Interconnect connection. A partner delivers the circuit to Google from a nearby provider location. A service provider carries the circuit to Google on the customer behalf. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: A partner delivers the circuit to Google from a nearby provider location.
- **B:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: A partner delivers the circuit to Google from a nearby provider location.
- **C:** Correct. A service provider carries the circuit to Google on the customer behalf. In this case: A partner delivers the circuit to Google from a nearby provider location.
- **D:** Incorrect for this question. A dedicated circuit connects Google Cloud directly to another cloud provider. Why the correct answer wins: A partner delivers the circuit to Google from a nearby provider location.

### Question 60 — B

Answer: Set the Cloud Router ASN to a private value that differs from the peer. The two peers must not share an autonomous system number. Two peers cannot form a session when both claim the same autonomous system number. Local study-map skill 4.1 (Dedicated Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The two peers must not share an autonomous system number.
- **B:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The two peers must not share an autonomous system number.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The two peers must not share an autonomous system number.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: The two peers must not share an autonomous system number.

### Question 61 — C

Answer: Order a Cross-Cloud Interconnect connection. Cross-Cloud Interconnect is a dedicated circuit to another provider. A dedicated circuit connects Google Cloud directly to another cloud provider. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **B:** Incorrect for this question. A service provider carries the circuit to Google on the customer behalf. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **C:** Correct. A dedicated circuit connects Google Cloud directly to another cloud provider. In this case: Cross-Cloud Interconnect is a dedicated circuit to another provider.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Cross-Cloud Interconnect is a dedicated circuit to another provider.

### Question 62 — B

Answer: Enable MACsec on the interconnect. MACsec protects each hop between the premises and Google. Link-layer encryption protects each hop of the circuit between the premises and Google. Local study-map skill 4.2 (Partner and Cross-Cloud Interconnect), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Why the correct answer wins: MACsec protects each hop between the premises and Google.
- **B:** Correct. Link-layer encryption protects each hop of the circuit between the premises and Google. In this case: MACsec protects each hop between the premises and Google.
- **C:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: MACsec protects each hop between the premises and Google.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: MACsec protects each hop between the premises and Google.

### Question 63 — C, E

Answers: Deploy an HA VPN gateway with two interfaces; Deploy a Classic VPN with a single tunnel. Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair. Two interfaces in different zones give the tunnel pair a 99.99% topology. One tunnel gives a single path and no automatic failover. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair.
- **C:** Correct. Two interfaces in different zones give the tunnel pair a 99.99% topology. In this case: Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair.
- **E:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports the policy-based mode the device needs, and HA VPN supplies the redundant pair.

### Question 64 — A

Answer: Deploy an HA VPN gateway with two interfaces. Two interfaces in different zones give the tunnel pair redundancy. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Two interfaces in different zones give the tunnel pair redundancy.
- **B:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Two interfaces in different zones give the tunnel pair redundancy.
- **C:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: Two interfaces in different zones give the tunnel pair redundancy.
- **D:** Incorrect for this question. One tunnel gives a single path and no automatic failover. Why the correct answer wins: Two interfaces in different zones give the tunnel pair redundancy.

### Question 65 — A

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the failure far sooner than the hold timer. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.3 (HA VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the failure far sooner than the hold timer.
- **B:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: BFD detects the failure far sooner than the hold timer.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the failure far sooner than the hold timer.
- **D:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the failure far sooner than the hold timer.

### Question 66 — B

Answer: Deploy a Classic VPN with a single tunnel. Classic VPN supports the policy-based tunnel mode such a device requires. One tunnel gives a single path and no automatic failover. Local study-map skill 4.4 (Classic VPN), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.
- **B:** Correct. One tunnel gives a single path and no automatic failover. In this case: Classic VPN supports the policy-based tunnel mode such a device requires.
- **C:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.
- **D:** Incorrect for this question. A private physical circuit connects the premises to a Google colocation facility. Why the correct answer wins: Classic VPN supports the policy-based tunnel mode such a device requires.

### Question 67 — C

Answer: Advertise only the ranges the peer needs. The advertisement list publishes only the chosen prefixes. The router advertises a chosen prefix list instead of every subnet in the VPC. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.
- **C:** Correct. The router advertises a chosen prefix list instead of every subnet in the VPC. In this case: The advertisement list publishes only the chosen prefixes.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The advertisement list publishes only the chosen prefixes.

### Question 68 — D

Answer: Prefer the path with the lower multi-exit discriminator. A higher discriminator makes the cheaper path less preferred. The lower discriminator wins when the same prefix arrives over two attachments. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: A higher discriminator makes the cheaper path less preferred.
- **B:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: A higher discriminator makes the cheaper path less preferred.
- **C:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: A higher discriminator makes the cheaper path less preferred.
- **D:** Correct. The lower discriminator wins when the same prefix arrives over two attachments. In this case: A higher discriminator makes the cheaper path less preferred.

### Question 69 — C, E

Answers: Set the Cloud Router ASN to a private value that differs from the peer; Enable Bidirectional Forwarding Detection with a short interval. The ASN must differ from the peer, and BFD shortens the detection window. Two peers cannot form a session when both claim the same autonomous system number. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.5 (Cloud Router BGP), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The router advertises a chosen prefix list instead of every subnet in the VPC. Why the correct answer wins: The ASN must differ from the peer, and BFD shortens the detection window.
- **B:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: The ASN must differ from the peer, and BFD shortens the detection window.
- **C:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: The ASN must differ from the peer, and BFD shortens the detection window.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: The ASN must differ from the peer, and BFD shortens the detection window.
- **E:** Correct. Two peers cannot form a session when both claim the same autonomous system number. In this case: The ASN must differ from the peer, and BFD shortens the detection window.

### Question 70 — B

Answer: Enable Bidirectional Forwarding Detection with a short interval. BFD detects the degraded path while the session still looks established. The echo detects a dead path faster than the BGP hold timer allows. Local study-map skill 4.6 (BFD and Failover Timers), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Two peers cannot form a session when both claim the same autonomous system number. Why the correct answer wins: BFD detects the degraded path while the session still looks established.
- **B:** Correct. The echo detects a dead path faster than the BGP hold timer allows. In this case: BFD detects the degraded path while the session still looks established.
- **C:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: BFD detects the degraded path while the session still looks established.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: BFD detects the degraded path while the session still looks established.

### Question 71 — B

Answer: Switch the Cloud Router to global dynamic routing mode. Global dynamic routing makes learned routes available everywhere. Routes learned in one region are available to subnets in every region. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Routes stay inside the region that learned them. Why the correct answer wins: Global dynamic routing makes learned routes available everywhere.
- **B:** Correct. Routes learned in one region are available to subnets in every region. In this case: Global dynamic routing makes learned routes available everywhere.
- **C:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Global dynamic routing makes learned routes available everywhere.
- **D:** Incorrect for this question. The lower number wins when a static route and a dynamic route carry the same prefix. Why the correct answer wins: Global dynamic routing makes learned routes available everywhere.

### Question 72 — C

Answer: Give the static route a lower priority number than the learned route. A lower priority number on the static route keeps it preferred. The lower number wins when a static route and a dynamic route carry the same prefix. Local study-map skill 4.7 (Route Advertisement and Priority), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: A lower priority number on the static route keeps it preferred.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: A lower priority number on the static route keeps it preferred.
- **C:** Correct. The lower number wins when a static route and a dynamic route carry the same prefix. In this case: A lower priority number on the static route keeps it preferred.
- **D:** Incorrect for this question. The older selection order picks a different preferred path when the inputs tie. Why the correct answer wins: A lower priority number on the static route keeps it preferred.

### Question 73 — A

Answer: Run HA VPN over Cloud Interconnect instead of MACsec. IPsec tunnels encrypt the traffic even where MACsec is unavailable. IPsec tunnels inside the interconnect give encryption where MACsec is not available. Local study-map skill 4.8 (Interconnect Encryption and SLA), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 4 (configuring and implementing hybrid and multicloud network interconnectivity): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. IPsec tunnels inside the interconnect give encryption where MACsec is not available. In this case: IPsec tunnels encrypt the traffic even where MACsec is unavailable.
- **B:** Incorrect for this question. Two interfaces in different zones give the tunnel pair a 99.99% topology. Why the correct answer wins: IPsec tunnels encrypt the traffic even where MACsec is unavailable.
- **C:** Incorrect for this question. Link-layer encryption protects each hop of the circuit between the premises and Google. Why the correct answer wins: IPsec tunnels encrypt the traffic even where MACsec is unavailable.
- **D:** Incorrect for this question. The attachment carries one VLAN over the interconnect and peers with the router. Why the correct answer wins: IPsec tunnels encrypt the traffic even where MACsec is unavailable.

### Question 74 — D

Answer: Enable firewall rules logging. Firewall logging records the rule that allowed or denied each connection. The logs show which rule allowed or denied each connection. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: Firewall logging records the rule that allowed or denied each connection.
- **B:** Incorrect for this question. The logs record the translated address and port chosen for each flow. Why the correct answer wins: Firewall logging records the rule that allowed or denied each connection.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: Firewall logging records the rule that allowed or denied each connection.
- **D:** Correct. The logs show which rule allowed or denied each connection. In this case: Firewall logging records the rule that allowed or denied each connection.

### Question 75 — D

Answer: Enable Cloud NAT logging. NAT logging records the translated public address and port for each flow. The logs record the translated address and port chosen for each flow. Local study-map skill 5.1 (Logging for Network Components), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record sampled connections with source, destination, port and byte counts. Why the correct answer wins: NAT logging records the translated public address and port for each flow.
- **B:** Incorrect for this question. The logs show which rule allowed or denied each connection. Why the correct answer wins: NAT logging records the translated public address and port for each flow.
- **C:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: NAT logging records the translated public address and port for each flow.
- **D:** Correct. The logs record the translated address and port chosen for each flow. In this case: NAT logging records the translated public address and port for each flow.

### Question 76 — B

Answer: Create an alert policy on the network metric. An alert policy on the attachment metric notifies at the threshold. The policy notifies on the threshold instead of waiting for a user report. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Matching log entries become a counter the alerting policy can use. Why the correct answer wins: An alert policy on the attachment metric notifies at the threshold.
- **B:** Correct. The policy notifies on the threshold instead of waiting for a user report. In this case: An alert policy on the attachment metric notifies at the threshold.
- **C:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: An alert policy on the attachment metric notifies at the threshold.
- **D:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: An alert policy on the attachment metric notifies at the threshold.

### Question 77 — B

Answer: Create a log-based metric from the firewall log entries. A log-based metric turns matching entries into a counter. Matching log entries become a counter the alerting policy can use. Local study-map skill 5.2 (Network Metrics and Dashboards), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The alert fires on the reliability users experience rather than on a single resource. Why the correct answer wins: A log-based metric turns matching entries into a counter.
- **B:** Correct. Matching log entries become a counter the alerting policy can use. In this case: A log-based metric turns matching entries into a counter.
- **C:** Incorrect for this question. The appliance reports a signal that no managed metric covers. Why the correct answer wins: A log-based metric turns matching entries into a counter.
- **D:** Incorrect for this question. The policy notifies on the threshold instead of waiting for a user report. Why the correct answer wins: A log-based metric turns matching entries into a counter.

### Question 78 — C

Answer: Run a Connectivity Test between the two endpoints. A connectivity test names the rule that still blocks the path. The test evaluates the configuration along the path and names the blocking rule or missing route. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: A connectivity test names the rule that still blocks the path.
- **B:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A connectivity test names the rule that still blocks the path.
- **C:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: A connectivity test names the rule that still blocks the path.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: A connectivity test names the rule that still blocks the path.

### Question 79 — D, E

Answers: Run a Connectivity Test between the two endpoints; Read the Network Analyzer findings. The connectivity test proves reachability, and the analyser lists the remaining risks. The test evaluates the configuration along the path and names the blocking rule or missing route. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.3 (Connectivity Tests), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The logs record the names that clients asked for and the answers they received. Why the correct answer wins: The connectivity test proves reachability, and the analyser lists the remaining risks.
- **B:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The connectivity test proves reachability, and the analyser lists the remaining risks.
- **C:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: The connectivity test proves reachability, and the analyser lists the remaining risks.
- **D:** Correct. The test evaluates the configuration along the path and names the blocking rule or missing route. In this case: The connectivity test proves reachability, and the analyser lists the remaining risks.
- **E:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: The connectivity test proves reachability, and the analyser lists the remaining risks.

### Question 80 — D

Answer: Check the Performance Dashboard for packet loss. The performance dashboard reports loss and latency per segment. The dashboard separates loss on the Google network from loss outside it. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: The performance dashboard reports loss and latency per segment.
- **B:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: The performance dashboard reports loss and latency per segment.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: The performance dashboard reports loss and latency per segment.
- **D:** Correct. The dashboard separates loss on the Google network from loss outside it. In this case: The performance dashboard reports loss and latency per segment.

### Question 81 — D

Answer: Leave the MTU mismatch unfixed. A path that disagrees about frame size drops the oversized packets. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. Local study-map skill 5.4 (Performance Dashboard and Packet Loss), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: A path that disagrees about frame size drops the oversized packets.
- **B:** Incorrect for this question. The probe shows where the payload stops fitting along the path. Why the correct answer wins: A path that disagrees about frame size drops the oversized packets.
- **C:** Incorrect for this question. A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload. Why the correct answer wins: A path that disagrees about frame size drops the oversized packets.
- **D:** Correct. A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers. In this case: A path that disagrees about frame size drops the oversized packets.

### Question 82 — C

Answer: Review Firewall Insights for shadowed rules. Firewall Insights reports rules that never match. The insight names rules that never match because a broader rule already covered them. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights reports rules that never match.
- **B:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights reports rules that never match.
- **C:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights reports rules that never match.
- **D:** Incorrect for this question. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Why the correct answer wins: Firewall Insights reports rules that never match.

### Question 83 — B, E

Answers: Review Firewall Insights for shadowed rules; Read the Network Analyzer findings. Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure. The insight names rules that never match because a broader rule already covered them. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. Local study-map skill 5.5 (Firewall Insights and Network Analyzer), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure.
- **B:** Correct. The insight names rules that never match because a broader rule already covered them. In this case: Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure.
- **C:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure.
- **D:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure.
- **E:** Correct. The analyser reports misconfigurations and quota risks that would otherwise surface as an outage. In this case: Firewall Insights finds the dead rules, and the analyser surfaces the quota pressure.

### Question 84 — C

Answer: Query Flow Analyzer for the top talkers. Flow Analyzer ranks the flows by volume so the heaviest appear first. The analysis ranks the flows that consume the most bandwidth. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Flow Analyzer ranks the flows by volume so the heaviest appear first.
- **B:** Incorrect for this question. The insight names rules that never match because a broader rule already covered them. Why the correct answer wins: Flow Analyzer ranks the flows by volume so the heaviest appear first.
- **C:** Correct. The analysis ranks the flows that consume the most bandwidth. In this case: Flow Analyzer ranks the flows by volume so the heaviest appear first.
- **D:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Flow Analyzer ranks the flows by volume so the heaviest appear first.

### Question 85 — B

Answer: Inspect the flow in Network Topology. Network Topology draws the paths and their throughput. The view shows the paths and throughput between the resources that carry the traffic. Local study-map skill 5.6 (Flow Analyzer and Network Topology), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The dashboard separates loss on the Google network from loss outside it. Why the correct answer wins: Network Topology draws the paths and their throughput.
- **B:** Correct. The view shows the paths and throughput between the resources that carry the traffic. In this case: Network Topology draws the paths and their throughput.
- **C:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Network Topology draws the paths and their throughput.
- **D:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Network Topology draws the paths and their throughput.

### Question 86 — A

Answer: Compare the BGP session state on both peers. Comparing both peers isolates the fault to one side of the session. A session that is established on one side only points at the shared configuration. Local study-map skill 5.7 (BGP and VPN Troubleshooting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. A session that is established on one side only points at the shared configuration. In this case: Comparing both peers isolates the fault to one side of the session.
- **B:** Incorrect for this question. The echo detects a dead path faster than the BGP hold timer allows. Why the correct answer wins: Comparing both peers isolates the fault to one side of the session.
- **C:** Incorrect for this question. The test evaluates the configuration along the path and names the blocking rule or missing route. Why the correct answer wins: Comparing both peers isolates the fault to one side of the session.
- **D:** Incorrect for this question. The lower discriminator wins when the same prefix arrives over two attachments. Why the correct answer wins: Comparing both peers isolates the fault to one side of the session.

### Question 87 — B

Answer: Drain the backend before removing it. Draining lets the existing sessions finish while new ones go elsewhere. Draining lets in-flight requests finish instead of resetting the connections. Local study-map skill 5.8 (Traffic Draining and Migration), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 5 (managing, monitoring, and troubleshooting network operations): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The view shows the paths and throughput between the resources that carry the traffic. Why the correct answer wins: Draining lets the existing sessions finish while new ones go elsewhere.
- **B:** Correct. Draining lets in-flight requests finish instead of resetting the connections. In this case: Draining lets the existing sessions finish while new ones go elsewhere.
- **C:** Incorrect for this question. Removing a backend waits for in-flight requests to finish before the backend is detached. Why the correct answer wins: Draining lets the existing sessions finish while new ones go elsewhere.
- **D:** Incorrect for this question. The analysis ranks the flows that consume the most bandwidth. Why the correct answer wins: Draining lets the existing sessions finish while new ones go elsewhere.

### Question 88 — A

Answer: Attach a Cloud Armor backend security policy. A backend security policy can match the path and the origin region. The policy filters traffic that has already reached the load balancer. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. The policy filters traffic that has already reached the load balancer. In this case: A backend security policy can match the path and the origin region.
- **B:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: A backend security policy can match the path and the origin region.
- **C:** Incorrect for this question. The policy filters traffic at the edge before it is proxied to a backend. Why the correct answer wins: A backend security policy can match the path and the origin region.
- **D:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: A backend security policy can match the path and the origin region.

### Question 89 — D

Answer: Attach a Cloud Armor edge security policy. An edge policy drops the request before it is proxied. The policy filters traffic at the edge before it is proxied to a backend. Local study-map skill 6.1 (Cloud Armor Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: An edge policy drops the request before it is proxied.
- **B:** Incorrect for this question. The policy filters traffic that has already reached the load balancer. Why the correct answer wins: An edge policy drops the request before it is proxied.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: An edge policy drops the request before it is proxied.
- **D:** Correct. The policy filters traffic at the edge before it is proxied to a backend. In this case: An edge policy drops the request before it is proxied.

### Question 90 — D

Answer: Add a preconfigured WAF rule for the attack class. A preconfigured WAF rule matches that attack class. The rule matches the signatures of that class of request. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: A preconfigured WAF rule matches that attack class.
- **B:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: A preconfigured WAF rule matches that attack class.
- **C:** Incorrect for this question. Known bot categories are classified so the rule can allow or block them by intent. Why the correct answer wins: A preconfigured WAF rule matches that attack class.
- **D:** Correct. The rule matches the signatures of that class of request. In this case: A preconfigured WAF rule matches that attack class.

### Question 91 — B

Answer: Enable bot management on the policy. Bot management classifies clients so rules can act on intent. Known bot categories are classified so the rule can allow or block them by intent. Local study-map skill 6.2 (WAF and Bot Management), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule matches the signatures of that class of request. Why the correct answer wins: Bot management classifies clients so rules can act on intent.
- **B:** Correct. Known bot categories are classified so the rule can allow or block them by intent. In this case: Bot management classifies clients so rules can act on intent.
- **C:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Bot management classifies clients so rules can act on intent.
- **D:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Bot management classifies clients so rules can act on intent.

### Question 92 — D

Answer: Rely on the default DDoS protection and add a rate limit. Always-on DDoS protection absorbs the volumetric flood. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. Local study-map skill 6.3 (DDoS and Rate Limiting), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Requests from addresses on the threat lists are matched without writing rules by hand. Why the correct answer wins: Always-on DDoS protection absorbs the volumetric flood.
- **B:** Incorrect for this question. The model learns the normal request pattern and suggests rules for the anomaly it detects. Why the correct answer wins: Always-on DDoS protection absorbs the volumetric flood.
- **C:** Incorrect for this question. A client that exceeds the threshold is blocked for the ban duration. Why the correct answer wins: Always-on DDoS protection absorbs the volumetric flood.
- **D:** Correct. The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods. In this case: Always-on DDoS protection absorbs the volumetric flood.

### Question 93 — C, E

Answers: Create a hierarchical firewall policy at the organisation; Create a global network firewall policy. The organisation policy is inherited everywhere, and the global policy covers all regions. The policy applies to every project under the organisation node. The policy is evaluated for the networks it is associated with, in every region. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: The organisation policy is inherited everywhere, and the global policy covers all regions.
- **B:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The organisation policy is inherited everywhere, and the global policy covers all regions.
- **C:** Correct. The policy is evaluated for the networks it is associated with, in every region. In this case: The organisation policy is inherited everywhere, and the global policy covers all regions.
- **D:** Incorrect for this question. The policy applies only in the region it belongs to. Why the correct answer wins: The organisation policy is inherited everywhere, and the global policy covers all regions.
- **E:** Correct. The policy applies to every project under the organisation node. In this case: The organisation policy is inherited everywhere, and the global policy covers all regions.

### Question 94 — C

Answer: Move the rules to NGFW Standard. The standard tier adds the policy model and intelligence lists. The standard tier adds the policy model and threat intelligence over the base rules. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The base tier covers stateful filtering without advanced inspection. Why the correct answer wins: The standard tier adds the policy model and intelligence lists.
- **B:** Incorrect for this question. The enterprise tier adds layer 7 inspection through the managed engine. Why the correct answer wins: The standard tier adds the policy model and intelligence lists.
- **C:** Correct. The standard tier adds the policy model and threat intelligence over the base rules. In this case: The standard tier adds the policy model and intelligence lists.
- **D:** Incorrect for this question. The rule applies to instances carrying the tag and allows or denies the stated traffic. Why the correct answer wins: The standard tier adds the policy model and intelligence lists.

### Question 95 — D

Answer: Reorder the rules by priority. The lowest-numbered matching rule wins, so ordering decides the outcome. The lowest-numbered matching rule decides, so order changes the outcome. Local study-map skill 6.4 (NGFW Tiers and Policies), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. Why the correct answer wins: The lowest-numbered matching rule wins, so ordering decides the outcome.
- **B:** Incorrect for this question. The enterprise tier adds layer 7 inspection through the managed engine. Why the correct answer wins: The lowest-numbered matching rule wins, so ordering decides the outcome.
- **C:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: The lowest-numbered matching rule wins, so ordering decides the outcome.
- **D:** Correct. The lowest-numbered matching rule decides, so order changes the outcome. In this case: The lowest-numbered matching rule wins, so ordering decides the outcome.

### Question 96 — D

Answer: Add a deny-all egress rule with a higher priority. An explicit deny-all egress rule replaces the default allow. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Any source may reach the instance on the default ports, which defeats the segmentation. Why the correct answer wins: An explicit deny-all egress rule replaces the default allow.
- **B:** Incorrect for this question. Each tier carries a different tag and only the required flows are allowed between tiers. Why the correct answer wins: An explicit deny-all egress rule replaces the default allow.
- **C:** Incorrect for this question. The lowest-numbered matching rule decides, so order changes the outcome. Why the correct answer wins: An explicit deny-all egress rule replaces the default allow.
- **D:** Correct. Default-allow egress is replaced by an explicit deny, and only named destinations are permitted. In this case: An explicit deny-all egress rule replaces the default allow.

### Question 97 — C

Answer: Target the rule with network tags. Anyone who can set the tag can make an instance match the rule. Tags identify the instances the rule applies to, and any holder can set one. Local study-map skill 6.5 (Firewall Rules and Micro-Segmentation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The rule applies to the instances that run as that identity, which only a privileged caller can change. Why the correct answer wins: Anyone who can set the tag can make an instance match the rule.
- **B:** Incorrect for this question. Secure tags can only be applied by principals with the tag role, so they are harder to bypass. Why the correct answer wins: Anyone who can set the tag can make an instance match the rule.
- **C:** Correct. Tags identify the instances the rule applies to, and any holder can set one. In this case: Anyone who can set the tag can make an instance match the rule.
- **D:** Incorrect for this question. The policy applies to every project under the organisation node. Why the correct answer wins: Anyone who can set the tag can make an instance match the rule.

### Question 98 — D

Answer: Use static port allocation. Static allocation reserves a block of ports for each instance. Each VM reserves a block of ports, which gives predictable capacity and predictable consumption. Local study-map skill 6.6 (Cloud NAT and Port Allocation), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google assigns and releases external addresses as the demand changes. Why the correct answer wins: Static allocation reserves a block of ports for each instance.
- **B:** Incorrect for this question. Ports are assigned from a shared pool as the demand arrives. Why the correct answer wins: Static allocation reserves a block of ports for each instance.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Static allocation reserves a block of ports for each instance.
- **D:** Correct. Each VM reserves a block of ports, which gives predictable capacity and predictable consumption. In this case: Static allocation reserves a block of ports for each instance.

### Question 99 — A

Answer: Deploy Secure Web Proxy as the egress path. Secure Web Proxy applies URL and TLS policy to outbound traffic. Local study-map skill 6.7 (Secure Web Proxy), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Correct. In this case: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **B:** Incorrect for this question. Each interface sits in a different network, so the appliance can inspect and forward between them. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **C:** Incorrect for this question. A fixed address lets the partner allowlist the source. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.
- **D:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: Secure Web Proxy applies URL and TLS policy to outbound traffic.

### Question 100 — D

Answer: Deploy a multi-NIC appliance VM between the two networks. An appliance with an interface in each network inspects inline. Each interface sits in a different network, so the appliance can inspect and forward between them. Local study-map skill 6.8 (Multi-NIC Appliances and Packet Mirroring), mapped to the official guide: Google Cloud Professional Cloud Network Engineer exam guide (six sections, 24 April 2026 revision, retrieved October 2026). Primary reference: Professional Cloud Network Engineer exam guide section 6 (configuring, implementing, and managing a cloud network security solution): https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf.

- **A:** Incorrect for this question. The route forwards matching flows to the appliance even when the destination is not the appliance. Why the correct answer wins: An appliance with an interface in each network inspects inline.
- **B:** Incorrect for this question. Mirrored packets are delivered to the collector for analysis. Why the correct answer wins: An appliance with an interface in each network inspects inline.
- **C:** Incorrect for this question. Traffic reaches whichever appliance instance the internal front end selects. Why the correct answer wins: An appliance with an interface in each network inspects inline.
- **D:** Correct. Each interface sits in a different network, so the appliance can inspect and forward between them. In this case: An appliance with an interface in each network inspects inline.
