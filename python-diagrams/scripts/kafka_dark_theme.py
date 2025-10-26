"""
Kafka Architecture with Dark/Transparent Background
Perfect for social media with dark themes
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client

# Dark theme configuration
graph_attr = {
    "fontsize": "16",
    "bgcolor": "transparent",  # Change to "black" or "#1a1a1a" for solid dark
    "fontcolor": "white",
    "pad": "0.5",
}

node_attr = {
    "fontsize": "12",
    "fontcolor": "white",
    "color": "white",  # Border color
}

edge_attr = {
    "color": "white",
    "fontcolor": "white",
}

cluster_attr = {
    "fontcolor": "white",
    "color": "white",
}

with Diagram(
    "Kafka Event Streaming - Dark Theme",
    filename="kafka_dark",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    # Producer
    producer = Client("Checkout Service")
    
    # Kafka Topic
    with Cluster("Kafka Cluster"):
        topic = Kafka("orders Topic\n(3 partitions)")
    
    # Consumers
    consumer1 = Client("Inventory Manager")
    consumer2 = Client("Billing Manager")
    
    # Flow
    producer >> Edge(label="produce") >> topic
    topic >> Edge(label="consume\n(inventory-group)") >> consumer1
    topic >> Edge(label="consume\n(billing-group)") >> consumer2

