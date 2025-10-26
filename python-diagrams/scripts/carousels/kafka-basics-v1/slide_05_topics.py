"""
Instagram Carousel: Kafka Basics - Slide 5
Topics organize events by category
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka

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

with Diagram(
    "Topics\nOrganizing Events",
    filename="../../../output/carousels/kafka-basics-v1/slide_05_topics",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    outformat="png"
):
    
    with Cluster("Kafka Cluster"):
        orders = Kafka("orders-topic")
        payments = Kafka("payments-topic")
        inventory = Kafka("inventory-topic")

