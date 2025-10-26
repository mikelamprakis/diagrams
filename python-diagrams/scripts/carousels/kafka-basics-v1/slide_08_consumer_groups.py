"""
Instagram Carousel: Kafka Basics - Slide 8
Consumer groups enable parallel processing
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
    "penwidth": "2.5",
}

with Diagram(
    "Consumer Groups\nParallel Processing",
    filename="../../../output/carousels/kafka-basics-v1/slide_08_consumer_groups",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("orders-topic"):
        p0 = Kafka("P0")
        p1 = Kafka("P1")
        p2 = Kafka("P2")
    
    with Cluster("inventory-group"):
        c1 = Server("Consumer 1")
        c2 = Server("Consumer 2")
        c3 = Server("Consumer 3")
    
    p0 >> c1
    p1 >> c2
    p2 >> c3

