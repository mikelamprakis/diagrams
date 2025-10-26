"""
Instagram Carousel: Kafka Basics - Slide 1
Title slide introducing Kafka
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server

# Instagram-optimized settings
graph_attr = {
    "bgcolor": "#0f0f0f",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "white",
    "fontsize": "20",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "16",
    "fontcolor": "white",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#4ECDC4",
    "penwidth": "3.0",
}

with Diagram(
    "What is Apache Kafka?",
    filename="../../../output/carousels/kafka-basics-v1/slide_01_intro",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    kafka = Kafka("Apache Kafka\n\nDistributed Event\nStreaming Platform")

