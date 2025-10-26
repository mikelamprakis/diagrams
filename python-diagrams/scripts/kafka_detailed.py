"""
Detailed Kafka Cluster Architecture
Shows brokers, topics, and full consumer setup
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.queue import Kafka, RabbitMQ
from diagrams.onprem.client import Client
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.compute import Server

with Diagram(
    "Kafka Cluster - Detailed Architecture",
    filename="kafka_detailed",
    show=False,
    direction="LR",
    graph_attr={
        "fontsize": "16",
        "splines": "ortho",
        "nodesep": "0.8",
        "ranksep": "1.5",
    }
):
    # Producer Service
    with Cluster("Producer"):
        checkout = Server("Checkout Service")
    
    # Kafka Cluster
    with Cluster("Kafka Cluster"):
        # Brokers
        with Cluster("Brokers"):
            broker1 = Kafka("Broker 1")
            broker2 = Kafka("Broker 2")
            broker3 = Kafka("Broker 3")
            brokers = [broker1, broker2, broker3]
        
        # Topic
        with Cluster("orders Topic"):
            partition0 = RabbitMQ("Partition 0")
            partition1 = RabbitMQ("Partition 1")
            partition2 = RabbitMQ("Partition 2")
            partitions = [partition0, partition1, partition2]
    
    # Consumer Services
    with Cluster("Consumers"):
        with Cluster("Inventory Service"):
            inventory_consumer = Client("Inventory Consumer")
            inventory_db = PostgreSQL("Inventory DB")
            inventory_consumer >> inventory_db
        
        with Cluster("Billing Service"):
            billing_consumer = Client("Billing Consumer")
            billing_db = PostgreSQL("Billing DB")
            billing_consumer >> billing_db
    
    # Message Flow
    checkout >> Edge(label="Publish Orders") >> broker1
    
    # Brokers host partitions
    broker1 >> partitions
    broker2 >> partitions
    broker3 >> partitions
    
    # Partitions to consumers
    partition0 >> Edge(label="inventory-group") >> inventory_consumer
    partition1 >> Edge(label="billing-group") >> billing_consumer
    partition2 >> [inventory_consumer, billing_consumer]

