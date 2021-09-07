from nest.experiment import *
from nest.topology import *

import os
import sys

##############################
# Topology: Dumbbell
#
#   ln0----------------                      ---------------rn0
#                      \                    /
#   ln1---------------  \                  /  ---------------rn1
#                      \ \                / /
#   ln2---------------- lr ------------- rr ---------------- rn2
#   .                  /                    \                .
#   .                 /                      \               .
#   .                /                        \              .
#   .               /                          \             .
#   ln6------------                              ------------rn6
#
##############################

queue_disciplines = ["cake"]
rates = [("800mbit","80mbit"),("1600mbit","160mbit"),("10000mbit","1000mbit")] # (Edge bandwidth, bottleneck bandwidth)
ecn_values = [True, False]
delays = [("0.25","1.5"),("2.5","15"),("5","30"),("10","380")] # (Edge delay, bottleneck delay)
flows = [1, 3, 16]
stop_times = [210]
offloads_value = ["ON", "OFF"]

###### TOPOLOGY CREATION ######

for qdisc in queue_disciplines:
    for (edge, bbw) in rates:
        for ecn in ecn_values:
            for (ed, bd) in delays:
                for number_of_flow in flows:
                    for offload in offloads_value:
                        for duration in stop_times:
                            # Creating the routers for the dumbbell topology
                            left_router = Node("left-router")
                            right_router = Node("right-router")
                            
                            # Enabling IP forwarding for the routers
                            left_router.enable_ip_forwarding()
                            right_router.enable_ip_forwarding()
                            
                            # Lists to store all the left and right nodes
                            left_nodes = []
                            right_nodes = []
                            
                            num_of_left_nodes = 1
                            num_of_right_nodes = 1

                            edge_delay = ed + "ms"
                            bottleneck_delay = bd + "ms"

                            if ecn == True:
                                # Creating all the left and right nodes
                                for i in range(num_of_left_nodes):
                                    left_nodes.append(Node("left-node-" + str(i)))
                                    left_nodes[i].configure_tcp_param("ecn", "1")
                            
                                for i in range(num_of_right_nodes):
                                    right_nodes.append(Node("right-node-" + str(i)))
                                    right_nodes[i].configure_tcp_param("ecn", "1")

                            elif ecn == False:
                                # Creating all the left and right nodes
                                for i in range(num_of_left_nodes):
                                    left_nodes.append(Node("left-node-" + str(i)))
                            
                                for i in range(num_of_right_nodes):
                                    right_nodes.append(Node("right-node-" + str(i)))


                            print("Nodes and routers created")
                            
                            # Add connections
                            
                            # Lists of tuples to store the interfaces connecting the router and nodes
                            left_node_connections = []
                            right_node_connections = []

                            # Connections of the left-nodes to the left-router
                            for i in range(num_of_left_nodes):
                                left_node_connections.append(connect(left_nodes[i], left_router))
                            
                            # Connections of the right-nodes to the right-router
                            for i in range(num_of_right_nodes):
                                right_node_connections.append(connect(right_nodes[i], right_router))
                            
                            # Connecting the two routers
                            (left_router_connection, right_router_connection) = connect(left_router, right_router)
                            
                            print("Connections made")
                        
                            ###### ADDRESS ASSIGNMENT ######
                            
                            # A subnet object to auto generate addresses in the same subnet
                            # This subnet is used for all the left-nodes and the left-router
                            left_subnet = Subnet("10.0.0.0/24")

                            for i in range(num_of_left_nodes):
                                # Copying a left-node's interface and it's pair to temporary variables
                                node_int = left_node_connections[i][0]
                                router_int = left_node_connections[i][1]
                            
                                # Assigning addresses to the interfaces
                                node_int.set_address(left_subnet.get_next_addr())
                                router_int.set_address(left_subnet.get_next_addr())

                                # This subnet is used for all the right-nodes and the right-router
                                right_subnet = Subnet("10.0.1.0/24")
                            
                            for i in range(num_of_right_nodes):
                                # Copying a right-node's interface and it's pair to temporary variables
                                node_int = right_node_connections[i][0]
                                router_int = right_node_connections[i][1]
                            
                                # Assigning addresses to the interfaces
                                node_int.set_address(right_subnet.get_next_addr())
                                router_int.set_address(right_subnet.get_next_addr())
                            
                            # This subnet is used for the connections between the two routers
                            router_subnet = Subnet("10.0.2.0/24")
                            
                            # Assigning addresses to the connections between the two routers
                            left_router_connection.set_address(router_subnet.get_next_addr())
                            right_router_connection.set_address(router_subnet.get_next_addr())
                            
                            print("Addresses are assigned")
                            
                            ####### ROUTING #######

                            # If any packet needs to be sent from any left-nodes, send it to left-router
                            for i in range(num_of_left_nodes):
                                left_nodes[i].add_route("DEFAULT", left_node_connections[i][0])
                            
                            # If the destination address for any packet in left-router is
                            # one of the left-nodes, forward the packet to that node
                            for i in range(num_of_left_nodes):
                                left_router.add_route(
                                    left_node_connections[i][0].get_address(), left_node_connections[i][1]
                                )
                            
                            # If the destination address doesn't match any of the entries
                            # in the left-router's iptables forward the packet to right-router
                            left_router.add_route("DEFAULT", left_router_connection)
                            
                            # If any packet needs to be sent from any right nodes, send it to right-router
                            for i in range(num_of_right_nodes):
                                right_nodes[i].add_route("DEFAULT", right_node_connections[i][0])
                            
                            # If the destination address for any packet in left-router is
                            # one of the left-nodes, forward the packet to that node
                            for i in range(num_of_right_nodes):
                                right_router.add_route(
                                    right_node_connections[i][0].get_address(), right_node_connections[i][1]
                                )

                            # If the destination address doesn't match any of the entries
                            # in the right-router's iptables forward the packet to left-router
                            right_router.add_route("DEFAULT", right_router_connection)
                            
                            # Setting up the attributes of the connections between
                            # the nodes on the left-side and the left-router
                            for i in range(num_of_left_nodes):
                                left_node_connections[i][0].set_attributes(edge, ed)
                                left_node_connections[i][1].set_attributes(edge, ed)
                            
                            # Setting up the attributes of the connections between
                            # the nodes on the right-side and the right-router
                            for i in range(num_of_right_nodes):
                                right_node_connections[i][0].set_attributes(edge, ed)
                                right_node_connections[i][1].set_attributes(edge, ed)

                            if ecn == True:
                                if qdisc == "fq_pie":
                                    qdisc_parameters = {'target': '5ms', 'ecn': ''}
                                elif qdisc == "cake":
                                    value = 2 * float(bd) + 4 * float(ed)
                                    qdisc_parameters = {'rtt' : str(value), 'ecn': ''}
                                else:
                                    qdisc_parameters = {'ecn': ''}

                                left_router_connection.set_attributes(bbw, bottleneck_delay, qdisc, **qdisc_parameters)
                                right_router_connection.set_attributes(bbw, bottleneck_delay, qdisc, **qdisc_parameters)

                            elif ecn == False: 
                                if qdisc == "fq_pie":
                                    qdisc_parameters = {'target': '5ms'}
                                elif qdisc == "cake":
                                    value = 2 * float(bd) + 4 * float(ed)
                                    qdisc_parameters = {'rtt' : str(value)}
                                else:
                                    qdisc_parameters = {}

                                left_router_connection.set_attributes(bbw, bottleneck_delay, qdisc, **qdisc_parameters)
                                right_router_connection.set_attributes(bbw, bottleneck_delay, qdisc, **qdisc_parameters)
                                

                            if qdisc == "cake":
                                value = 2 * float(bd) + 4 * float(ed)
                                qdisc_parameters = {'rtt' : value}

                            if offload == "OFF":
                                offload_type = ["gso", "gro", "tso"]
                                for i in range(num_of_left_nodes):
                                    left_node_connections[i][0].disable_offload(offload_type)
                                    left_node_connections[i][1].disable_offload(offload_type)

                                for i in range(num_of_right_nodes):
                                    right_node_connections[i][0].disable_offload(offload_type)
                                    right_node_connections[i][1].disable_offload(offload_type)


                                left_router_connection.disable_offload(offload_type)
                                right_router_connection.disable_offload(offload_type)

                            ######  RUN TESTS ######
                            name = ""
                            if(ecn == True):
                                name += qdisc + ' ECN-' + "ON "  + edge + " " + bbw + " " + ed + " " + bd + " " + str(number_of_flow)
                            else :
                                name += qdisc + ' ECN-' + "OFF " + edge + " " + bbw + " " + ed + " " + bd + " " + str(number_of_flow)
                            
                            # Giving the experiment a name
                            experiment = Experiment(name)
                            
                            # Add a flow from the left nodes to respective right nodes
                            for i in range(min(num_of_left_nodes, num_of_right_nodes)):
                                flow = Flow(
                                    left_nodes[i], right_nodes[i], right_node_connections[i][0].address, 0, duration, number_of_flow
                                )
                                # Use TCP reno
                                experiment.add_tcp_flow(flow,"cubic")
                            
                            # Request traffic control stats
                            experiment.require_qdisc_stats(left_router_connection)
                            
                            # Running the experiment
                            experiment.run()
