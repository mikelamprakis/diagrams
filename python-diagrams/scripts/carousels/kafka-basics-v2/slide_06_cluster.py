"""
Instagram Carousel: Kafka Basics v2 - Slide 6
Kafka Cluster with Multiple Brokers
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka

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
    "Kafka Cluster\nMultiple Brokers",
    filename="../../../output/carousels/kafka-basics-v2/slide_06_cluster",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Kafka Cluster"):
        broker1 = Kafka("Broker 1")
        broker2 = Kafka("Broker 2")
        broker3 = Kafka("Broker 3")
        
        # Brokers communicate with each other
        broker1 - Edge(style="dotted", color="#888888") - broker2
        broker2 - Edge(style="dotted", color="#888888") - broker3
        broker3 - Edge(style="dotted", color="#888888") - broker1

