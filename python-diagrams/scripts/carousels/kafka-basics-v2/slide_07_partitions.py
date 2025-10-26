"""
Instagram Carousel: Kafka Basics v2 - Slide 7
Partitions & Parallelism
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server

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
    "Partitions\nParallel Processing",
    filename="../../../output/carousels/kafka-basics-v2/slide_07_partitions",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("payments-topic"):
        p0 = Kafka("Partition 0")
        p1 = Kafka("Partition 1")
        p2 = Kafka("Partition 2")
    
    with Cluster("Consumer Group"):
        c1 = Server("Consumer 1")
        c2 = Server("Consumer 2")
        c3 = Server("Consumer 3")
    
    # Each partition to dedicated consumer
    p0 >> Edge(label="parallel") >> c1
    p1 >> Edge(label="parallel") >> c2
    p2 >> Edge(label="parallel") >> c3

