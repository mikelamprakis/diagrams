"""
Instagram Carousel: Kafka Basics - Slide 6
Partitions enable horizontal scaling
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
    "Partitions\nHorizontal Scaling",
    filename="../../../output/carousels/kafka-basics-v1/slide_06_partitions",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    outformat="png"
):
    
    with Cluster("orders-topic"):
        partition0 = Kafka("Partition 0\n(Orders 1,4,7...)")
        partition1 = Kafka("Partition 1\n(Orders 2,5,8...)")
        partition2 = Kafka("Partition 2\n(Orders 3,6,9...)")

