"""
Instagram Carousel: Kafka Basics v2 - Slide 10
Complete Summary Pipeline
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
    "fontsize": "13",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#00d4ff",
    "penwidth": "3.0",
}

with Diagram(
    "Complete Pipeline\nEnd-to-End",
    filename="../../../output/carousels/kafka-basics-v2/slide_10_summary",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Producers"):
        prod1 = Server("Service 1")
        prod2 = Server("Service 2")
    
    with Cluster("Kafka Cluster"):
        with Cluster("Brokers"):
            broker1 = Kafka("Broker 1")
            broker2 = Kafka("Broker 2")
            broker3 = Kafka("Broker 3")
        
        with Cluster("Partitions"):
            p0 = Kafka("P0")
            p1 = Kafka("P1")
            p2 = Kafka("P2")
    
    with Cluster("Consumers"):
        cons1 = Server("Consumer 1")
        cons2 = Server("Consumer 2")
    
    # Pipeline flow
    prod1 >> Edge(label="Produce") >> broker1
    prod2 >> Edge(label="Produce") >> broker2
    
    broker1 >> Edge(label="Store") >> p0
    broker2 >> Edge(label="Store") >> p1
    broker3 >> Edge(label="Store") >> p2
    
    p0 >> Edge(label="Consume") >> cons1
    p1 >> Edge(label="Consume") >> cons2
    p2 >> Edge(label="Consume") >> cons1

