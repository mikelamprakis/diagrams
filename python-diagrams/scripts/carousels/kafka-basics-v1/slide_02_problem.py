"""
Instagram Carousel: Kafka Basics - Slide 2
The problem: Traditional message queues
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

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
    "color": "#FF6B6B",
    "penwidth": "2.0",
}

with Diagram(
    "The Problem\nTraditional Systems",
    filename="../../../output/carousels/kafka-basics-v1/slide_02_problem",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    producer = Server("Service A")
    queue = PostgreSQL("Database\nQueue")
    consumer = Server("Service B")
    
    producer >> Edge(label="❌ Slow\n❌ Not Scalable\n❌ Single Point") >> queue >> consumer

