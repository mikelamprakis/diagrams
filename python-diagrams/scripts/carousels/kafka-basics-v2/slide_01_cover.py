"""
Instagram Carousel: Kafka Basics v2 - Slide 1
Cover: Overview of Kafka with producers and consumers
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server

# Instagram-optimized settings
graph_attr = {
    "bgcolor": "transparent",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "#000000",
    "fontsize": "20",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "14",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#00d4ff",
    "penwidth": "2.5",
}

with Diagram(
    "Apache Kafka\nDistributed Streaming",
    filename="../../../output/carousels/kafka-basics-v2/slide_01_cover",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Producers"):
        prod1 = Server("User Service")
        prod2 = Server("Order Service")
        prod3 = Server("Payment Service")
    
    kafka = Kafka("Apache\nKafka")
    
    with Cluster("Consumers"):
        cons1 = Server("Analytics")
        cons2 = Server("Notifications")
        cons3 = Server("Warehouse")
    
    # Producers to Kafka
    prod1 >> kafka
    prod2 >> kafka
    prod3 >> kafka
    
    # Kafka to Consumers
    kafka >> cons1
    kafka >> cons2
    kafka >> cons3

