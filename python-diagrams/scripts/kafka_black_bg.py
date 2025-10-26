"""
Kafka Architecture with Solid Black Background
For dark mode presentations
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server

# Black background configuration
graph_attr = {
    "fontsize": "16",
    "bgcolor": "#000000",  # Solid black
    "fontcolor": "#FFFFFF",
    "pad": "0.8",
    "nodesep": "1.0",
    "ranksep": "1.0",
}

node_attr = {
    "fontsize": "13",
    "fontcolor": "#FFFFFF",
    "color": "#FFFFFF",
    "style": "rounded",
}

edge_attr = {
    "color": "#00D9FF",  # Cyan color for visibility
    "fontcolor": "#00D9FF",
    "fontsize": "11",
}

with Diagram(
    "Kafka Orders Processing",
    filename="kafka_black",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    # Producer
    checkout = Server("Checkout Service\n(Producer)")
    
    # Kafka Cluster
    with Cluster("Kafka Cluster"):
        with Cluster("orders Topic"):
            kafka_p0 = Kafka("Partition 0")
            kafka_p1 = Kafka("Partition 1")
            kafka_p2 = Kafka("Partition 2")
            topic = [kafka_p0, kafka_p1, kafka_p2]
    
    # Consumers
    inventory = Client("Inventory Manager\n(Consumer)")
    billing = Client("Billing Manager\n(Consumer)")
    
    # Flow
    checkout >> Edge(label="Publish Orders", color="#FF6B6B") >> topic
    topic >> Edge(label="inventory-group", color="#4ECDC4") >> inventory
    topic >> Edge(label="billing-group", color="#45B7D1") >> billing

