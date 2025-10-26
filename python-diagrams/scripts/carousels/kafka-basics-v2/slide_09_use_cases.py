"""
Instagram Carousel: Kafka Basics v2 - Slide 9
Real-World Use Cases
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server

graph_attr = {
    "bgcolor": "transparent",
    "pad": "0.5",
    "dpi": "300",
    "fontcolor": "#000000",
    "fontsize": "20",
    "fontname": "Arial Bold",
}

node_attr = {
    "fontsize": "14",
    "fontcolor": "#000000",
    "fontname": "Arial",
}

edge_attr = {
    "color": "#00d4ff",
    "penwidth": "2.5",
}

with Diagram(
    "Real-World Use Cases\nWho Uses Kafka?",
    filename="../../../output/carousels/kafka-basics-v2/slide_09_use_cases",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    kafka = Kafka("Apache\nKafka")
    
    netflix = Server("Netflix\nStreaming")
    spotify = Server("Spotify\nAnalytics")
    linkedin = Server("LinkedIn\nEvent Data")
    uber = Server("Uber\nReal-time")
    
    kafka >> Edge(label="streaming") >> netflix
    kafka >> Edge(label="analytics") >> spotify
    kafka >> Edge(label="events") >> linkedin
    kafka >> Edge(label="real-time") >> uber

