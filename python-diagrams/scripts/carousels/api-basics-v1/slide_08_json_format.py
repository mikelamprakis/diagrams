"""
Instagram Carousel: API Basics v1 - Slide 8
JSON - The Language of APIs
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
    "JSON Format\nJavaScript Object Notation",
    filename="../../../output/carousels/api-basics-v1/slide_08_json_format",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Client")
    api = Server("API")
    
    client >> Edge(label='Request:\nGET /user/1') >> api
    api >> Edge(
        label='Response:\n{\n  "id": 1,\n  "name": "John"\n}',
        color="#00ff88"
    ) >> client

