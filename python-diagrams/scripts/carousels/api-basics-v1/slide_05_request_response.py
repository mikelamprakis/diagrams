"""
Instagram Carousel: API Basics v1 - Slide 5
Request & Response Flow
"""

from diagrams import Diagram, Edge
from diagrams.onprem.client import Client
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
    "Request & Response\nThe API Flow",
    filename="../../../output/carousels/api-basics-v1/slide_05_request_response",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Client")
    server = Server("API\nServer")
    
    client >> Edge(label="1. Request\nGET /users/123", color="#00d4ff") >> server
    server >> Edge(label="2. Response\n{ user: {...} }", color="#00ff88") >> client

