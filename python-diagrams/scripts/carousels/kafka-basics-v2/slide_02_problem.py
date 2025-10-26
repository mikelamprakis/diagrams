"""
Instagram Carousel: Kafka Basics v2 - Slide 2
The Problem: Point-to-point communication chaos
"""

from diagrams import Diagram, Edge
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
    "color": "#ff4444",
    "penwidth": "2.0",
}

with Diagram(
    "Without Kafka\n❌ Chaos",
    filename="../../../output/carousels/kafka-basics-v2/slide_02_problem",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    # Four services fully interconnected
    serviceA = Server("Service A")
    serviceB = Server("Service B")
    serviceC = Server("Service C")
    serviceD = Server("Service D")
    
    # Full mesh - everyone talks to everyone
    serviceA >> Edge(style="dashed") >> serviceB
    serviceA >> Edge(style="dashed") >> serviceC
    serviceA >> Edge(style="dashed") >> serviceD
    
    serviceB >> Edge(style="dashed") >> serviceA
    serviceB >> Edge(style="dashed") >> serviceC
    serviceB >> Edge(style="dashed") >> serviceD
    
    serviceC >> Edge(style="dashed") >> serviceA
    serviceC >> Edge(style="dashed") >> serviceB
    serviceC >> Edge(style="dashed") >> serviceD
    
    serviceD >> Edge(style="dashed") >> serviceA
    serviceD >> Edge(style="dashed") >> serviceB
    serviceD >> Edge(style="dashed") >> serviceC

