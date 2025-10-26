"""
Generate animated Kafka diagram frames
Creates multiple frames showing the message flow step-by-step
Run this, then use create_gif.sh to combine into animated GIF
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server

# Shared styling for all frames
def get_graph_attr(transparent=True):
    return {
        "fontsize": "18",
        "bgcolor": "transparent" if transparent else "#1a1a1a",
        "fontcolor": "white",
        "pad": "1.0",
        "nodesep": "1.2",
        "ranksep": "1.5",
    }

node_attr = {
    "fontsize": "14",
    "fontcolor": "white",
    "color": "white",
}

edge_attr = {
    "fontcolor": "white",
    "fontsize": "12",
}

# Frame 1: Just the producer
print("Generating Frame 1: Producer...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_01_producer",
    show=False,
    direction="LR",
    graph_attr=get_graph_attr(),
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    checkout = Server("Checkout Service\n(Producer)")

# Frame 2: Producer + Kafka
print("Generating Frame 2: Producer + Kafka...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_02_kafka",
    show=False,
    direction="LR",
    graph_attr=get_graph_attr(),
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    checkout = Server("Checkout Service\n(Producer)")
    
    with Cluster("Kafka Cluster"):
        topic = Kafka("orders Topic")
    
    checkout >> topic

# Frame 3: Add first consumer
print("Generating Frame 3: Add Inventory Consumer...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_03_consumer1",
    show=False,
    direction="LR",
    graph_attr=get_graph_attr(),
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    checkout = Server("Checkout Service\n(Producer)")
    
    with Cluster("Kafka Cluster"):
        topic = Kafka("orders Topic")
    
    inventory = Client("Inventory Manager")
    
    checkout >> topic
    topic >> Edge(label="inventory-group", color="#4ECDC4") >> inventory

# Frame 4: Add second consumer
print("Generating Frame 4: Add Billing Consumer...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_04_consumer2",
    show=False,
    direction="LR",
    graph_attr=get_graph_attr(),
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    checkout = Server("Checkout Service\n(Producer)")
    
    with Cluster("Kafka Cluster"):
        topic = Kafka("orders Topic")
    
    inventory = Client("Inventory Manager")
    billing = Client("Billing Manager")
    
    checkout >> topic
    topic >> Edge(label="inventory-group", color="#4ECDC4") >> inventory
    topic >> Edge(label="billing-group", color="#45B7D1") >> billing

# Frame 5: Show partitions
print("Generating Frame 5: Show Partitions...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_05_partitions",
    show=False,
    direction="LR",
    graph_attr=get_graph_attr(),
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    checkout = Server("Checkout Service\n(Producer)")
    
    with Cluster("Kafka Cluster"):
        with Cluster("orders Topic"):
            p0 = Kafka("Partition 0")
            p1 = Kafka("Partition 1")
            p2 = Kafka("Partition 2")
            partitions = [p0, p1, p2]
    
    inventory = Client("Inventory Manager")
    billing = Client("Billing Manager")
    
    checkout >> Edge(label="Publish", color="#FF6B6B") >> partitions
    partitions >> Edge(label="inventory-group", color="#4ECDC4") >> inventory
    partitions >> Edge(label="billing-group", color="#45B7D1") >> billing

print("\n✅ All frames generated!")
print("\nGenerated files:")
print("  - frame_01_producer.png")
print("  - frame_02_kafka.png")
print("  - frame_03_consumer1.png")
print("  - frame_04_consumer2.png")
print("  - frame_05_partitions.png")
print("\nNow run: ./create_gif.sh")

