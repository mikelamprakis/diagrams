"""
Instagram Carousel: API Basics v1 - Slide 7
REST API - The Most Popular Style
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
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
    "color": "#00ffff",
    "penwidth": "2.5",
}

with Diagram(
    "REST API\nREpresentational State Transfer",
    filename="../../../output/carousels/api-basics-v1/slide_07_rest_api",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    client = Client("Client")
    
    with Cluster("REST API"):
        users = Nginx("/users")
        posts = Nginx("/posts")
        comments = Nginx("/comments")
    
    client >> users
    client >> posts
    client >> comments

