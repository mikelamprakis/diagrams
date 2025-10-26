"""
Instagram Carousel: API Basics v1 - Slide 2
The Problem: Without APIs (Chaos)
"""

from diagrams import Diagram, Edge
from diagrams.onprem.compute import Server

graph_attr = {
    "bgcolor": "transparent",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "#000000",
    "fontsize": "22",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "14",
    "color": "#00ffff",
    "fillcolor": "#1a1a1a:#00ffff",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#ff0066",
    "penwidth": "2.0",
}

with Diagram(
    "Without APIs\n❌ Chaos & Complexity",
    filename="../../../output/carousels/api-basics-v1/slide_02_problem",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    appA = Server("App A")
    appB = Server("App B")
    appC = Server("App C")
    
    # Messy spaghetti connections
    appA >> Edge(style="dashed", label="custom") >> appB
    appA >> Edge(style="dashed", label="custom") >> appC
    appB >> Edge(style="dashed", label="custom") >> appA
    appB >> Edge(style="dashed", label="custom") >> appC
    appC >> Edge(style="dashed", label="custom") >> appA
    appC >> Edge(style="dashed", label="custom") >> appB

