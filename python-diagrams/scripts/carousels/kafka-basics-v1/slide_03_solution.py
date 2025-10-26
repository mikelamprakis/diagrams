"""
Instagram Carousel: Kafka Basics - Slide 3
The solution: Kafka distributed streaming
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

edge_attr = {
    "color": "#4ECDC4",
    "penwidth": "2.0",
}

with Diagram(
    "The Solution\nKafka Streaming",
    filename="../../../output/carousels/kafka-basics-v1/slide_03_solution",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Kafka Cluster"):
        brokers = [
            Kafka("Broker 1"),
            Kafka("Broker 2"),
            Kafka("Broker 3"),
        ]

