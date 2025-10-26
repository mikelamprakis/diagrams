"""
Simple Kafka Architecture
Clean and minimal design
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client

with Diagram(
    "Kafka Event Streaming",
    filename="kafka_simple",
    show=False,
    direction="TB",
):
    # Producer
    producer = Client("Checkout Service")
    
    # Kafka Topic
    with Cluster("Kafka Cluster"):
        topic = Kafka("orders Topic\n(3 partitions)")
    
    # Consumers
    consumer1 = Client("Inventory Manager")
    consumer2 = Client("Billing Manager")
    
    # Flow
    producer >> Edge(label="produce") >> topic
    topic >> Edge(label="consume\n(inventory-group)") >> consumer1
    topic >> Edge(label="consume\n(billing-group)") >> consumer2

