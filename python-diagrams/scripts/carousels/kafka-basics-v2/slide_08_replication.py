"""
Instagram Carousel: Kafka Basics v2 - Slide 8
Replication & Fault Tolerance
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka

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
    "color": "#ffaa00",
    "penwidth": "3.0",
}

with Diagram(
    "Replication\nFault Tolerance",
    filename="../../../output/carousels/kafka-basics-v2/slide_08_replication",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png"
):
    
    with Cluster("Broker 1"):
        leader = Kafka("Partition 0\n⭐ LEADER")
    
    with Cluster("Broker 2"):
        follower1 = Kafka("Partition 0\n📋 Follower")
    
    with Cluster("Broker 3"):
        follower2 = Kafka("Partition 0\n📋 Follower")
    
    # Leader replicates to followers
    leader >> Edge(label="replicate", color="#00ff88") >> follower1
    leader >> Edge(label="replicate", color="#00ff88") >> follower2

