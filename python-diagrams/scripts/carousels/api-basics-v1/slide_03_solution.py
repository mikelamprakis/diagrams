"""
Instagram Carousel: API Basics v1 - Slide 3
The Solution: APIs to the Rescue
"""

from diagrams import Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Nginx

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
    "color": "#00ff00",
    "penwidth": "3.0",
}

with Diagram(
    "With APIs\n✅ Clean & Simple",
    filename="../../../output/carousels/api-basics-v1/slide_03_solution",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    api = Nginx("API\nGateway")
    
    appA = Server("App A")
    appB = Server("App B")
    appC = Server("App C")
    
    # Clean hub-and-spoke pattern
    appA >> Edge(label="standard") >> api
    appB >> Edge(label="standard") >> api
    appC >> Edge(label="standard") >> api

