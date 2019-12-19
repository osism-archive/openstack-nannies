#!/usr/bin/env python3

# This script checks if networks with DHCP have more than one DHCP agent assigned.
# If this is not the case, additional DHCP agents are assigned to the network.

import openstack

conn = openstack.connect(cloud='service')

for network in conn.network.networks():
    if network.is_admin_state_up == False or network.is_router_external:
         continue

    is_dhcp_enabled = False
    for subnet in network.subnet_ids:
        subnet = conn.network.find_subnet(subnet)
        if subnet.is_dhcp_enabled:
            is_dhcp_enabled = True

    if is_dhcp_enabled:
        agents = conn.network.network_hosting_dhcp_agents(network)
        length = sum(1 for x in agents)
        if length < 2:
            print("Network %s has only %d agents assigned" % (network.name, length))

            # FIXME(berendt): make the number of assigned DHCP agents configurable
            # FIXME(berendt): randomly select the assigned DHCP agents
            for agent in conn.network.agents(binary="neutron-dhcp-agent"):
                conn.network.add_dhcp_agent_to_network(agent, network)
