"""
Instagram Carousel: API Basics v1 - Slide 10
Summary: The Power of APIs
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
    "The Power of APIs\n✨ Complete Flow",
    filename="../../../output/carousels/api-basics-v1/slide_10_summary",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Client")
    
    with Cluster("API Benefits"):
        api = Nginx("API\n\n🔒 Security\n📈 Scalability\n♻️ Reusability")
    
    server = Server("Server")
    
    client >> Edge(label="Request") >> api
    api >> Edge(label="Process") >> server
    server >> Edge(label="Response", color="#00ff88") >> api
    api >> Edge(label="Return", color="#00ff88") >> client

