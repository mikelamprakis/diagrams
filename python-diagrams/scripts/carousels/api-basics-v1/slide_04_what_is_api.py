"""
Instagram Carousel: API Basics v1 - Slide 4
What is an API?
"""

from diagrams import Diagram, Cluster, Edge
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
    "fontsize": "15",
    "color": "#00ffff",
    "fillcolor": "#1a1a1a:#00ffff",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

with Diagram(
    "What is an API?\nApplication Programming\nInterface",
    filename="../../../output/carousels/api-basics-v1/slide_04_what_is_api",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    outformat="png"
):
    
    api = Nginx("API\n\nA contract between\nsoftware components\n\nDefines how they\ncommunicate")

