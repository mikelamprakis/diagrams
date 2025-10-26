"""
Instagram Carousel: Kafka Basics - Slide 10
Key benefits of Apache Kafka
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
    "Why Kafka?\nKey Benefits",
    filename="../../../output/carousels/kafka-basics-v1/slide_10_benefits",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    outformat="png"
):
    
    kafka = Kafka("Apache Kafka\n\n✅ Real-time Streaming\n✅ Horizontally Scalable\n✅ Fault Tolerant\n✅ High Throughput")

