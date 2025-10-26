"""
Instagram Carousel: API Basics v1 - Slide 9
Security & Control
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
from diagrams.onprem.network import Nginx
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
    "color": "#00ffff",
    "penwidth": "3.0",
}

with Diagram(
    "Security & Control\n🔒 Protected Access",
    filename="../../../output/carousels/api-basics-v1/slide_09_security",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Client\n(with API Key)")
    gateway = Nginx("API Gateway\n🔒 Auth\n🔑 Rate Limit\n🛡️ Validation")
    server = Server("Protected\nServer")
    
    client >> Edge(label="Token", color="#00ff88") >> gateway
    gateway >> Edge(label="Authorized", color="#00ff88") >> server

