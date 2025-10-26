"""
Instagram Carousel: Kafka Basics - Slide 9
Complete end-to-end flow
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
    "fontsize": "13",
    "fontcolor": "white",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#4ECDC4",
    "penwidth": "2.5",
}

with Diagram(
    "Complete Flow\nEnd-to-End",
    filename="../../../output/carousels/kafka-basics-v1/slide_09_complete_flow",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    producer = Server("Checkout\nService")
    
    with Cluster("Kafka Cluster"):
        kafka = Kafka("orders-topic")
    
    consumer1 = Server("Inventory\nManager")
    consumer2 = Server("Billing\nManager")
    
    producer >> Edge(label="Publish") >> kafka
    kafka >> Edge(label="Subscribe") >> consumer1
    kafka >> Edge(label="Subscribe") >> consumer2

