"""
Instagram Carousel: Kafka Basics v2 - Slide 3
Kafka as Message Broker
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
    "Kafka as Broker\n✅ Decoupled",
    filename="../../../output/carousels/kafka-basics-v2/slide_03_broker",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Producers"):
        prod1 = Server("Producer 1")
        prod2 = Server("Producer 2")
        prod3 = Server("Producer 3")
    
    broker = Kafka("Kafka\nBroker")
    
    with Cluster("Consumers"):
        cons1 = Server("Consumer 1")
        cons2 = Server("Consumer 2")
        cons3 = Server("Consumer 3")
    
    # Producers to Broker
    prod1 >> Edge(label="produce") >> broker
    prod2 >> Edge(label="produce") >> broker
    prod3 >> Edge(label="produce") >> broker
    
    # Broker to Consumers
    broker >> Edge(label="consume") >> cons1
    broker >> Edge(label="consume") >> cons2
    broker >> Edge(label="consume") >> cons3

