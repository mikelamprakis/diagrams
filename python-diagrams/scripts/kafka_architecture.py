"""
Kafka Orders Processing Architecture
Uses Python Diagrams library with actual tech icons
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.programming.framework import Spring

# Set diagram attributes
graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.5",
}

node_attr = {
    "fontsize": "12",
}

with Diagram(
    "Kafka Orders Processing Pipeline",
    filename="kafka_orders",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    # Producer
    checkout_service = Server("Checkout Service\n(Producer)")
    
    # Kafka Cluster
    with Cluster("Kafka Cluster"):
        # Orders topic with partitions
        with Cluster("orders Topic"):
            kafka_partition_0 = Kafka("Partition 0")
            kafka_partition_1 = Kafka("Partition 1")
            kafka_partition_2 = Kafka("Partition 2")
            
            kafka_topic = [kafka_partition_0, kafka_partition_1, kafka_partition_2]
    
    # Consumers
    with Cluster("Consumer Groups"):
        inventory_manager = Spring("Inventory Manager\n(inventory-group)")
        billing_manager = Spring("Billing Manager\n(billing-group)")
    
    # Message Flow
    checkout_service >> Edge(label="Publish Orders") >> kafka_topic
    kafka_topic >> Edge(label="Consume Orders") >> inventory_manager
    kafka_topic >> Edge(label="Consume Orders") >> billing_manager

