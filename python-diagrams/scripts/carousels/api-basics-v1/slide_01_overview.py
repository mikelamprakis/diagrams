"""
Instagram Carousel: API Basics v1 - Slide 1
Overview: APIs - The Hidden Connectors
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Nginx
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server

# Instagram-optimized settings with transparent background
graph_attr = {
    "bgcolor": "transparent",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "#000000",
    "fontsize": "22",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "15",
    "color": "#00ffff",
    "fillcolor": "#1a1a1a:#00ffff",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#00ffff",
    "penwidth": "3.0",
}

with Diagram(
    "APIs\nThe Hidden Connectors\nof the Digital World",
    filename="../../../output/carousels/api-basics-v1/slide_01_overview",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Mobile App")
    api = Nginx("API")
    server = Server("Server")
    
    client >> Edge(label="connects via") >> api >> Edge(label="to") >> server

