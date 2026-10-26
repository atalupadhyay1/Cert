"""Option bank for the Professional Cloud Network Engineer practice sets.

Every option label is a design choice or an engineering action, so an item can ask
which decision fits the stated constraints without the distractor collapsing into
a definition. Keys are authoring identifiers only and never appear in an export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Network service tier and topology --------------------------------------
t('premium_tier', 'Use the Premium network service tier',
  'Traffic enters the Google network at the edge closest to the user and crosses it to the serving region.')
t('standard_tier', 'Use the Standard network service tier',
  'Traffic enters the Google network in the region that hosts the resource, so long-haul travel happens on the public internet.')
t('shared_vpc', 'Build the network as a Shared VPC with host and service projects',
  'One host project owns the network and subnets while service projects deploy into shared subnets.')
t('standalone_vpc', 'Give each team its own standalone VPC network',
  'Separate projects own separate networks, and nothing is shared implicitly.')
t('ncc_hub', 'Connect the VPC networks through a Network Connectivity Center hub',
  'A hub groups spokes so the connected networks reach each other through one managed topology.')
t('hub_spoke', 'Connect the networks as a hub-and-spoke peering topology',
  'A central network peers with each leaf network, and the leaves do not peer with each other.')
t('mesh_peering', 'Peer every VPC network with every other VPC network',
  'A full mesh of peering sessions gives each network a direct path to all the others.')
t('peering_transitivity', 'Assume peered networks can reach each other transitively',
  'Peering is not transitive, so a route learned through one peer is not passed on to another.')
t('vpc_peering', 'Create a VPC Network Peering connection between the two networks',
  'Two networks exchange routes directly without a gateway or a shared project.')
t('subnet_expansion', 'Expand the existing subnet range',
  'A subnet prefix can grow within its address range, and the growth cannot shrink later.')
t('ipam_secondary', 'Plan secondary ranges for pods and services',
  'Alias ranges give pods and services addresses that are separate from the node subnet.')
t('ipv6_dual_stack', 'Enable dual-stack IPv6 on the subnet',
  'The subnet carries both an IPv4 range and an internal or external IPv6 range.')
t('byoip', 'Bring your own public IP prefixes',
  'Public prefixes the organisation already owns are advertised from Google Cloud.')
t('pupi', 'Use privately used public IP address ranges',
  'Public ranges that are never advertised are used internally to gain address space without NAT.')
t('private_nat', 'Deploy Private NAT for the overlapping ranges',
  'Source addresses are translated so two networks with the same private ranges can still talk.')
t('non_rfc1918', 'Use non-RFC 1918 space for the internal network',
  'The internal network uses address space outside the private ranges to avoid collisions later.')
t('ipam_automation', 'Automate address allocation from a central IPAM plan',
  'Allocation is generated from one authoritative plan instead of hand-picked ranges per team.')
t('subnet_overlap', 'Accept the overlapping subnet ranges as configured',
  'Two subnets with the same prefix cannot be routed to each other without translation.')

# --- MTU --------------------------------------------------------------------
t('mtu_8896', 'Raise the VPC MTU to 8896 bytes',
  'A larger maximum transmission unit carries more payload per packet inside the VPC.')
t('mtu_1460', 'Lower the tunnel MTU to 1460 bytes',
  'A smaller MTU leaves room for the tunnel encapsulation headers that reduce usable payload.')
t('mtu_1500', 'Keep the default 1500-byte MTU',
  'The default MTU matches ordinary Ethernet frames and needs no adjustment.')
t('mtu_mismatch', 'Leave the MTU mismatch unfixed',
  'A path that disagrees about frame size drops or fragments large packets, which shows up as stalled bulk transfers.')

# --- Connectivity to managed services --------------------------------------
t('private_google_access', 'Enable Private Google Access on the subnet',
  'Instances without external addresses reach Google APIs through internal routing.')
t('psc_endpoint', 'Create a Private Service Connect endpoint',
  'A private endpoint inside the consumer VPC targets a published service attachment.')
t('psc_propagation', 'Propagate the Private Service Connect connection through hybrid spokes',
  'Hybrid traffic reaches the private endpoint without a separate endpoint on each side.')
t('private_services_access', 'Allocate a private services access range',
  'A reserved internal range lets a managed service provider peer into the VPC.')
t('serverless_vpc_access', 'Attach the service to Serverless VPC Access',
  'A serverless runtime gets a path into the VPC through a connector or direct egress.')
t('direct_vpc_egress', 'Use Direct VPC egress for the serverless workload',
  'The workload receives its own address in the subnet instead of going through a connector.')
t('api_public_interface', 'Reach the API through its public interface',
  'The client resolves the public endpoint and traffic leaves Google Cloud, which fails a private-only requirement.')

# --- IAM --------------------------------------------------------------------
t('network_admin_role', 'Grant the network administrator role in the host project',
  'That role creates and changes networks and subnets, which a service team should not hold.')
t('subnet_user_role', 'Grant the subnet user role on the specific shared subnets',
  'The role lets a service project deploy into the named subnets and nothing else.')
t('custom_role_network', 'Create a custom role with only the required network permissions',
  'The custom role names the exact permissions the automation needs.')
t('basic_role', 'Grant the basic editor role to the automation',
  'Editor spans most services, so it can delete far more than the network resources involved.')
t('shared_vpc_admin', 'Grant Shared VPC Admin on the host project',
  'That role attaches service projects and delegates subnet use.')

# --- Load balancer shape ----------------------------------------------------
t('global_lb', 'Deploy a global external Application Load Balancer',
  'A global anycast address routes each user to the closest healthy region.')
t('regional_lb', 'Deploy a regional external Application Load Balancer',
  'The front end is regional, so users are served from the region the address belongs to.')
t('internal_lb', 'Deploy an internal passthrough Network Load Balancer',
  'The front end is an internal address reachable only from inside the VPC or its connected networks.')
t('proxy_lb', 'Use a proxy Network Load Balancer',
  'The proxy terminates the client connection and opens a separate one to the backend.')
t('passthrough_lb', 'Use a passthrough Network Load Balancer',
  'Packets keep their client source address and the backend sees the original flow.')
t('external_passthrough_lb', 'Use an external passthrough Network Load Balancer',
  'The front end is a public address and the backend receives the original packet.')
t('lb_ssl_proxy', 'Use an external proxy Network Load Balancer with TLS termination',
  'The proxy terminates TLS and forwards a separate connection to the backend.')

# --- Backends, NEGs, health checks ------------------------------------------
t('backend_service', 'Add the backends to a backend service behind the front end',
  'The backend service holds the health check, balancing mode and capacity settings.')
t('health_check_lb', 'Attach a health check to the backend service',
  'The check removes a backend that cannot answer, so traffic moves to a healthy one.')
t('neg_zonal', 'Register the backends as a zonal network endpoint group',
  'A zonal endpoint group addresses specific endpoints such as pods or VMs in one zone.')
t('neg_internet', 'Register the third-party origins as an internet network endpoint group',
  'An internet endpoint group targets endpoints outside Google Cloud by hostname and port.')
t('neg_serverless', 'Register the serverless service as a serverless network endpoint group',
  'A serverless endpoint group fronts a Cloud Run service without a managed instance group.')
t('mig_autoscaler', 'Autoscale a managed instance group behind the backend service',
  'The group adds and removes instances as the autoscaling signal changes.')
t('session_affinity', 'Enable session affinity on the backend service',
  'Affinity keeps a client on the backend that already holds its session state.')
t('connection_draining', 'Enable connection draining with a timeout',
  'Removing a backend waits for in-flight requests to finish before the backend is detached.')
t('balancing_mode_rate', 'Switch the balancing mode to connections per instance',
  'The mode spreads load by connection count rather than by CPU utilisation.')
t('global_access_flag', 'Enable global access on the internal load balancer',
  'Clients in any region can reach the internal front end instead of only its own region.')
t('url_map', 'Route by URL path in the URL map',
  'The map selects a backend service from the request host and path.')
t('traffic_split', 'Split traffic between two backend services by weight',
  'Weighted backends move a chosen share of traffic onto the new service.')
t('traffic_mirror', 'Mirror a copy of the traffic to a second backend',
  'The mirrored request is sent for inspection while the response comes only from the primary.')
t('url_rewrite', 'Rewrite the request path before it reaches the backend',
  'The rewrite presents the backend with the path it expects without changing the client.')
t('gke_ingress', 'Expose the workload through the GKE Ingress controller',
  'An Ingress object creates a Google Cloud load balancer from the manifest.')
t('gke_gateway', 'Expose the workload through the GKE Gateway controller',
  'A Gateway object configures the load balancer through the newer Kubernetes API.')

# --- Cloud CDN --------------------------------------------------------------
t('cdn_cache', 'Enable Cloud CDN on the backend service',
  'The edge holds a copy of the response so later requests are served closer to the user.')
t('cdn_origin_neg', 'Point Cloud CDN at the origins through an internet endpoint group',
  'An internet endpoint group lets the CDN cache responses from backends outside Google Cloud.')
t('cache_invalidation', 'Invalidate the cached object after the change',
  'Invalidation removes the stale copy so the next request fetches the current version.')
t('cache_ttl', 'Raise the cache time to live',
  'A longer lifetime reduces origin load and lengthens the window in which content can be stale.')
t('signed_url', 'Serve the object through a signed URL',
  'A signed URL authorises one object for a limited time without making the bucket public.')

# --- DNS --------------------------------------------------------------------
t('cloud_dns_private_zone', 'Create a private Cloud DNS zone',
  'The zone answers only for clients inside the authorised networks.')
t('cloud_dns_public_zone', 'Create a public Cloud DNS zone',
  'The zone answers queries from the internet for the domain it holds.')
t('split_horizon_dns', 'Serve split-horizon answers from separate private and public zones',
  'Internal clients resolve the internal address while external clients resolve the public one.')
t('dns_forwarding', 'Configure a DNS forwarding policy for the on-premises domain',
  'Queries for the corporate suffix are forwarded to the on-premises resolvers.')
t('dns_peering', 'Create a DNS peering zone to the other project',
  'The consumer project resolves names from the producer project through a peering zone.')
t('dns_inbound_policy', 'Create an inbound forwarding policy with a forwarding address',
  'On-premises resolvers send queries to that address to reach Cloud DNS names.')
t('dns_cross_project_binding', 'Bind the private zone to the service project networks',
  "The binding makes the host project's zone answer for the service project's networks.")
t('dns_geolocation', 'Apply a geolocation routing policy to the record set',
  'The answer depends on the source region of the query.')
t('dns_failover', 'Apply a failover routing policy with a health-checked primary',
  'The standby answer is served when the primary fails its health check.')
t('dnssec', 'Enable DNSSEC on the zone',
  'Signatures let a resolver verify that the answer was not altered in transit.')
t('external_dns_operator', 'Run the external DNS operator against the zone',
  'The operator reconciles Kubernetes service records into Cloud DNS.')
t('dns_record_ttl_low', 'Lower the record TTL before the cutover',
  'A short TTL lets resolvers pick up the new address quickly after the change.')
t('dns_migration', 'Migrate the zone with a staged import and a delegated test',
  'Records are loaded and verified before the registrar points at the new name servers.')

# --- Hybrid and multicloud --------------------------------------------------
t('interconnect_dedicated', 'Order a Dedicated Interconnect connection',
  'A private physical circuit connects the premises to a Google colocation facility.')
t('interconnect_partner', 'Order a Partner Interconnect connection',
  "A service provider carries the circuit to Google on the customer behalf.")
t('cross_cloud_interconnect', 'Order a Cross-Cloud Interconnect connection',
  'A dedicated circuit connects Google Cloud directly to another cloud provider.')
t('vlan_attachment', 'Create a VLAN attachment on Cloud Router',
  'The attachment carries one VLAN over the interconnect and peers with the router.')
t('macsec', 'Enable MACsec on the interconnect',
  'Link-layer encryption protects each hop of the circuit between the premises and Google.')
t('ha_vpn_over_ic', 'Run HA VPN over Cloud Interconnect instead of MACsec',
  'IPsec tunnels inside the interconnect give encryption where MACsec is not available.')
t('cloud_vpn_ha', 'Deploy an HA VPN gateway with two interfaces',
  'Two interfaces in different zones give the tunnel pair a 99.99% topology.')
t('classic_vpn', 'Deploy a Classic VPN with a single tunnel',
  'One tunnel gives a single path and no automatic failover.')
t('bgp_asn', 'Set the Cloud Router ASN to a private value that differs from the peer',
  'Two peers cannot form a session when both claim the same autonomous system number.')
t('med_route_priority', 'Prefer the path with the lower multi-exit discriminator',
  'The lower discriminator wins when the same prefix arrives over two attachments.')
t('bfd', 'Enable Bidirectional Forwarding Detection with a short interval',
  'The echo detects a dead path faster than the BGP hold timer allows.')
t('custom_advertised_routes', 'Advertise only the ranges the peer needs',
  'The router advertises a chosen prefix list instead of every subnet in the VPC.')
t('global_dynamic_routing', 'Switch the Cloud Router to global dynamic routing mode',
  'Routes learned in one region are available to subnets in every region.')
t('regional_dynamic_routing', 'Keep the Cloud Router in regional dynamic routing mode',
  'Routes stay inside the region that learned them.')
t('legacy_best_path', 'Switch best path selection back to the legacy behaviour',
  'The older selection order picks a different preferred path when the inputs tie.')
t('route_priority_manual', 'Give the static route a lower priority number than the learned route',
  'The lower number wins when a static route and a dynamic route carry the same prefix.')
t('route_advertisement_conflict', 'Let both paths advertise the same prefix with the same attributes',
  'Identical inputs leave the tie-break to an order the operator did not intend.')

# --- Routing and appliances -------------------------------------------------
t('ilb_next_hop', 'Use the internal load balancer as the next hop',
  'Traffic reaches whichever appliance instance the internal front end selects.')
t('policy_based_route', 'Add a policy-based route that matches the source and destination',
  'The route forwards matching flows to the appliance even when the destination is not the appliance.')
t('custom_route_static', 'Create a static route with a tag-scoped next hop',
  'Only instances carrying the tag send their traffic through the appliance.')
t('multi_nic_vm', 'Deploy a multi-NIC appliance VM between the two networks',
  'Each interface sits in a different network, so the appliance can inspect and forward between them.')
t('out_of_band_inspection', 'Inspect the traffic out of band with Packet Mirroring',
  'A copy of the traffic goes to a collector while the original flow continues untouched.')
t('packet_mirroring', 'Configure Packet Mirroring on the instance group',
  'Mirrored packets are delivered to the collector for analysis.')

# --- GKE networking ---------------------------------------------------------
t('gke_private_nodes', 'Use private nodes with no external addresses',
  'Nodes reach the control plane and Google APIs through internal paths only.')
t('gke_private_control_plane', 'Use a private control plane endpoint',
  'The API server is reachable only through the internal address or an authorised network.')
t('gke_authorized_networks', 'Add the office range to the authorised networks',
  'The named range may reach the control plane endpoint even when it is public.')
t('gke_dns_endpoint', 'Use the DNS-based control plane endpoint',
  'The endpoint resolves through a private DNS name instead of a fixed address.')
t('dataplane_v2', 'Enable GKE Dataplane V2',
  'The eBPF dataplane handles policy and service routing inside the cluster.')
t('ip_masquerade', 'Configure an IP masquerade policy on the node pool',
  'Outbound pod traffic is translated to the node address under the chosen conditions.')
t('gke_network_policy', 'Create a GKE network policy for the namespace',
  'The policy restricts which pods may talk to the selected pods.')
t('pod_range', 'Add a second pod range to the cluster',
  'An additional alias range gives pods more addresses without rebuilding the cluster.')
t('service_range', 'Resize the service range allocation',
  'The service address range must have room for the services the cluster will run.')
t('gke_shared_vpc', 'Deploy the cluster into a shared subnet',
  'The cluster consumes subnets that the host project owns.')
t('node_pool_secondary', 'Give each node pool its own secondary range',
  'Per-pool ranges keep the address plan separable as the cluster grows.')

# --- Network Connectivity Center -------------------------------------------
t('ncc_vpc_spoke', 'Add the VPC network as a VPC spoke',
  'The spoke exports the network subnets to the hub.')
t('ncc_hybrid_spoke', 'Add the attachment as a hybrid spoke',
  'The spoke carries the VLAN attachment or VPN into the hub.')
t('ncc_producer_spoke', 'Add the published service as a producer spoke',
  'The spoke publishes a service attachment so consumers reach it through the hub.')
t('ncc_cidr_filter', 'Apply a CIDR range filter to the spoke',
  'Only the matching prefixes are exchanged with the hub.')
t('ncc_transitivity', 'Expect spoke-to-spoke reachability through the hub',
  'The hub forwards between spokes, which peering alone cannot do.')

# --- Observability ---------------------------------------------------------
t('vpc_flow_logs', 'Enable VPC Flow Logs on the subnet',
  'The logs record sampled connections with source, destination, port and byte counts.')
t('firewall_logs', 'Enable firewall rules logging',
  'The logs show which rule allowed or denied each connection.')
t('nat_logging', 'Enable Cloud NAT logging',
  'The logs record the translated address and port chosen for each flow.')
t('dns_logging', 'Enable Cloud DNS query logging',
  'The logs record the names that clients asked for and the answers they received.')
t('vpn_logging', 'Enable Cloud VPN logging',
  'The logs record tunnel state changes and IKE negotiation outcomes.')
t('connectivity_tests', 'Run a Connectivity Test between the two endpoints',
  'The test evaluates the configuration along the path and names the blocking rule or missing route.')
t('network_topology', 'Inspect the flow in Network Topology',
  'The view shows the paths and throughput between the resources that carry the traffic.')
t('performance_dashboard', 'Check the Performance Dashboard for packet loss',
  'The dashboard separates loss on the Google network from loss outside it.')
t('firewall_insights', 'Review Firewall Insights for shadowed rules',
  'The insight names rules that never match because a broader rule already covered them.')
t('network_analyzer', 'Read the Network Analyzer findings',
  'The analyser reports misconfigurations and quota risks that would otherwise surface as an outage.')
t('flow_analyzer', 'Query Flow Analyzer for the top talkers',
  'The analysis ranks the flows that consume the most bandwidth.')
t('traffic_draining', 'Drain the backend before removing it',
  'Draining lets in-flight requests finish instead of resetting the connections.')
t('bgp_troubleshooting', 'Compare the BGP session state on both peers',
  'A session that is established on one side only points at the shared configuration.')
t('uptime_check', 'Create an uptime check on the front end',
  'The check probes the service from outside and alerts on failure.')
t('alert_policy', 'Create an alert policy on the network metric',
  'The policy notifies on the threshold instead of waiting for a user report.')
t('custom_metric', 'Publish a custom metric from the appliance',
  'The appliance reports a signal that no managed metric covers.')
t('log_based_metric', 'Create a log-based metric from the firewall log entries',
  'Matching log entries become a counter the alerting policy can use.')
t('slo_alert', 'Alert on the error budget of the service objective',
  'The alert fires on the reliability users experience rather than on a single resource.')

# --- Cloud Armor ------------------------------------------------------------
t('cloud_armor_backend', 'Attach a Cloud Armor backend security policy',
  'The policy filters traffic that has already reached the load balancer.')
t('cloud_armor_edge', 'Attach a Cloud Armor edge security policy',
  'The policy filters traffic at the edge before it is proxied to a backend.')
t('waf_rule', 'Add a preconfigured WAF rule for the attack class',
  'The rule matches the signatures of that class of request.')
t('adaptive_protection', 'Enable Adaptive Protection',
  'The model learns the normal request pattern and suggests rules for the anomaly it detects.')
t('ddos_protection', 'Rely on the default DDoS protection and add a rate limit',
  'The always-on protection absorbs volumetric floods, and the rate limit covers application-level floods.')
t('rate_limit_ban', 'Add a rate-based ban rule',
  'A client that exceeds the threshold is blocked for the ban duration.')
t('bot_management', 'Enable bot management on the policy',
  'Known bot categories are classified so the rule can allow or block them by intent.')
t('threat_intelligence', 'Apply Google Threat Intelligence lists',
  'Requests from addresses on the threat lists are matched without writing rules by hand.')

# --- Firewalls and NGFW -----------------------------------------------------
t('vpc_firewall_rules', 'Create a VPC firewall rule with a target tag',
  'The rule applies to instances carrying the tag and allows or denies the stated traffic.')
t('hierarchical_firewall', 'Create a hierarchical firewall policy at the organisation',
  'The policy applies to every project under the organisation node.')
t('ngfw_global_policy', 'Create a global network firewall policy',
  'The policy is evaluated for the networks it is associated with, in every region.')
t('ngfw_regional_policy', 'Create a regional network firewall policy',
  'The policy applies only in the region it belongs to.')
t('ngfw_essentials', 'Stay on NGFW Essentials for the VPC rules',
  'The base tier covers stateful filtering without advanced inspection.')
t('ngfw_standard', 'Move the rules to NGFW Standard',
  'The standard tier adds the policy model and threat intelligence over the base rules.')
t('ngfw_enterprise', 'Move the inspection to NGFW Enterprise',
  'The enterprise tier adds layer 7 inspection through the managed engine.')
t('l7_inspection', 'Enable layer 7 packet inspection',
  'The inspection engine examines application payload rather than only the five-tuple.')
t('firewall_rule_priority', 'Reorder the rules by priority',
  'The lowest-numbered matching rule decides, so order changes the outcome.')
t('firewall_priority_numbering', 'Leave gaps in the priority numbering',
  'Spare numbers let later rules be inserted without renumbering the whole policy.')
t('network_tags_firewall', 'Target the rule with network tags',
  'Tags identify the instances the rule applies to, and any holder can set one.')
t('service_account_firewall', 'Target the rule with a service account',
  'The rule applies to the instances that run as that identity, which only a privileged caller can change.')
t('secure_tags', 'Use secure tags as the rule target',
  'Secure tags can only be applied by principals with the tag role, so they are harder to bypass.')
t('micro_segmentation', 'Divide the network into micro-segmented tiers',
  'Each tier carries a different tag and only the required flows are allowed between tiers.')
t('egress_deny_rule', 'Add a deny-all egress rule with a higher priority',
  'Default-allow egress is replaced by an explicit deny, and only named destinations are permitted.')
t('default_allow_ingress', 'Leave the default allow-ingress rule in place',
  'Any source may reach the instance on the default ports, which defeats the segmentation.')

# --- Cloud NAT and Secure Web Proxy ----------------------------------------
t('cloud_nat_auto_ip', 'Use automatic Cloud NAT IP allocation',
  'Google assigns and releases external addresses as the demand changes.')
t('cloud_nat_manual_ip', 'Assign a manual static Cloud NAT address',
  'A fixed address lets the partner allowlist the source.')
t('static_port_allocation', 'Use static port allocation',
  'Each VM reserves a block of ports, which gives predictable capacity and predictable consumption.')
t('dynamic_port_allocation', 'Use dynamic port allocation',
  'Ports are assigned from a shared pool as the demand arrives.')
t('secure_web_proxy', 'Deploy Secure Web Proxy as the egress path',
  'The proxy applies URL and TLS inspection policy to outbound traffic.')
t('nat_port_exhaustion', 'Accept the port exhaustion as expected',
  'Running out of translated ports drops new connections even though addresses remain.')

# --- Appliance and inspection patterns -------------------------------------
t('ilb_next_hop_appliance', 'Route through the internal load balancer in front of the appliances',
  'The load balancer hides appliance failure, so a lost instance is replaced without a route change.')
t('asymmetric_routing', 'Leave the return path asymmetric',
  'The reply leaves by a different path, and a stateful device on one side drops it.')
t('mtu_probe', 'Test the path with a large ping and the do-not-fragment bit',
  'The probe shows where the payload stops fitting along the path.')

# --- Service perimeters and peering options ---------------------------------
t('vpc_sc_perimeter', 'Enclose the project in a VPC Service Controls perimeter',
  'The perimeter restricts which services the project may call and blocks data movement outside it.')
t('peering_custom_routes', 'Import and export custom routes over the peering',
  'The peering option carries static and policy-based routes between the two networks.')
