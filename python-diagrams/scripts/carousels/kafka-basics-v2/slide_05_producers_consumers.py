"""
Instagram Carousel: Kafka Basics v2 - Slide 5
Producers & Consumers with Topics
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
    "penwidth": "2.5",
}

with Diagram(
    "Producers & Consumers\nWith Topics",
    filename="../../../output/carousels/kafka-basics-v2/slide_05_producers_consumers",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Producers"):
        prod1 = Server("Web App")
        prod2 = Server("Mobile App")
        prod3 = Server("Backend API")
    
    with Cluster("Kafka Topics"):
        topic1 = Kafka("orders")
        topic2 = Kafka("events")
        topic3 = Kafka("metrics")
    
    with Cluster("Consumers"):
        cons1 = Server("Analytics")
        cons2 = Server("Storage")
    
    # Producers to Topics
    prod1 >> Edge(label="produce") >> topic1
    prod2 >> Edge(label="produce") >> topic2
    prod3 >> Edge(label="produce") >> topic3
    
    # Topics to Consumers
    topic1 >> Edge(label="consume") >> cons1
    topic2 >> Edge(label="consume") >> cons1
    topic3 >> Edge(label="consume") >> cons2

