"""
Instagram Carousel: Kafka Basics - Slide 4
Producer sends messages to Kafka
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
    "Step 1: Producer\nSends Events",
    filename="../../../output/carousels/kafka-basics-v1/slide_04_producer",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    producer = Server("Checkout\nService")
    kafka = Kafka("Kafka")
    
    producer >> Edge(label="Publish\nOrder Event") >> kafka

