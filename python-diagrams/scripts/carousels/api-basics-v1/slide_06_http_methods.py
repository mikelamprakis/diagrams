"""
Instagram Carousel: API Basics v1 - Slide 6
HTTP Methods (CRUD)
"""

from diagrams import Diagram, Cluster
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

with Diagram(
    "HTTP Methods\nCRUD Operations",
    filename="../../../output/carousels/api-basics-v1/slide_06_http_methods",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    outformat="png"
):
    
    with Cluster("API Endpoint: /users"):
        get = Nginx("GET\n(Read)")
        post = Nginx("POST\n(Create)")
        put = Nginx("PUT\n(Update)")
        delete = Nginx("DELETE\n(Delete)")

