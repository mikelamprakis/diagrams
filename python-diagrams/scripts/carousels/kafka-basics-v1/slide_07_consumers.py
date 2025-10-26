"""
Instagram Carousel: Kafka Basics - Slide 7
Consumers read messages from topics
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server

graph_attr = {
    "bgcolor": "#0f0f0f",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "white",
    "fontsize": "18",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "14",
    "fontcolor": "white",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#4ECDC4",
    "penwidth": "3.0",
}

with Diagram(
    "Step 2: Consumers\nRead Events",
    filename="../../../output/carousels/kafka-basics-v1/slide_07_consumers",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    kafka = Kafka("orders-topic")
    consumer1 = Server("Inventory\nService")
    consumer2 = Server("Billing\nService")
    
    kafka >> Edge(label="Subscribe") >> consumer1
    kafka >> Edge(label="Subscribe") >> consumer2

