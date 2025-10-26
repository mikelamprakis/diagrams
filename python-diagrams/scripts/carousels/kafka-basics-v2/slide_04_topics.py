"""
Instagram Carousel: Kafka Basics v2 - Slide 4
Topics: Message Categories
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark

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
    "Topics\nMessage Categories",
    filename="../../../output/carousels/kafka-basics-v2/slide_04_topics",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    kafka = Kafka("Kafka\nCluster")
    
    with Cluster("Topics"):
        payments = Kafka("payments")
        logs = Kafka("logs")
        analytics = Kafka("analytics")
    
    kafka >> payments
    kafka >> logs
    kafka >> analytics

