# Python Diagrams - Kafka Architecture

This directory contains Kafka architecture diagrams created using the Python `diagrams` library with actual tech stack icons.

## Setup

### 1. Install Graphviz (Required for rendering)
```bash
brew install graphviz
```

### 2. Install Python Dependencies
```bash
# Using uv (recommended for this project)
uv pip install diagrams

# Or using pip
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import diagrams; print('Diagrams installed successfully!')"
```

## Available Diagrams

### 1. `kafka_architecture.py` - Full Architecture
Comprehensive Kafka setup with:
- Checkout Service (Producer)
- Kafka Cluster with 3 partitions
- Inventory Manager (Consumer)
- Billing Manager (Consumer)

**Run:**
```bash
python kafka_architecture.py
```

**Output:** `kafka_orders.png`

---

### 2. `kafka_simple.py` - Simple Flow
Clean, minimal diagram showing basic producer-consumer flow.

**Run:**
```bash
python kafka_simple.py
```

**Output:** `kafka_simple.png`

---

### 3. `kafka_detailed.py` - Detailed Cluster
Shows complete cluster architecture with:
- 3 Kafka brokers
- 3 partitions
- Consumer groups with databases
- Full message flow

**Run:**
```bash
python kafka_detailed.py
```

**Output:** `kafka_detailed.png`

---

## Available Icons in Diagrams Library

### Messaging & Queuing
- `Kafka` - Apache Kafka
- `RabbitMQ` - RabbitMQ
- `ActiveMQ` - ActiveMQ
- `ZeroMQ` - ZeroMQ

### Cloud Providers
#### AWS
- `EC2`, `S3`, `Lambda`, `RDS`, `DynamoDB`
- `SQS`, `SNS`, `Kinesis`
- 200+ AWS services

#### Azure
- `VM`, `Functions`, `CosmosDB`, `AKS`
- `ServiceBus`, `EventHub`
- 100+ Azure services

#### GCP
- `GCE`, `GCS`, `GCF`, `CloudSQL`
- `PubSub`, `Dataflow`
- 100+ GCP services

### Kubernetes
- `Pod`, `Service`, `Deployment`, `StatefulSet`
- `ConfigMap`, `Secret`, `Ingress`
- 40+ K8s components

### Databases
- `PostgreSQL`, `MySQL`, `MongoDB`, `Redis`
- `Cassandra`, `Elasticsearch`, `InfluxDB`

### Programming
- `Python`, `Java`, `Go`, `JavaScript`
- `Spring`, `Django`, `Flask`, `React`

### On-Premise
- `Server`, `Client`, `Database`
- `Nginx`, `Apache`, `Tomcat`

## Usage Examples

### Basic Kafka Flow
```python
from diagrams import Diagram
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client

with Diagram("My Kafka", show=False):
    producer = Client("Producer")
    kafka = Kafka("Topic")
    consumer = Client("Consumer")
    
    producer >> kafka >> consumer
```

### Multi-Consumer Setup
```python
from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client

with Diagram("Multi Consumer", show=False):
    producer = Client("Producer")
    kafka = Kafka("Topic")
    
    with Cluster("Consumers"):
        consumers = [
            Client("Consumer 1"),
            Client("Consumer 2"),
            Client("Consumer 3")
        ]
    
    producer >> kafka >> consumers
```

### Cloud Integration
```python
from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS

with Diagram("Kafka to AWS", show=False):
    kafka = Kafka("Events")
    s3 = S3("Data Lake")
    rds = RDS("Analytics DB")
    
    kafka >> [s3, rds]
```

## Creating Animated Diagrams

To create step-by-step animations:

### 1. Create Multiple Frames
```python
# frame1.py - Just producer
from diagrams import Diagram
from diagrams.onprem.client import Client

with Diagram("Frame 1", filename="frame1", show=False):
    Client("Producer")
```

```python
# frame2.py - Add Kafka
from diagrams import Diagram
from diagrams.onprem.client import Client
from diagrams.onprem.queue import Kafka

with Diagram("Frame 2", filename="frame2", show=False):
    producer = Client("Producer")
    kafka = Kafka("Topic")
    producer >> kafka
```

### 2. Combine into GIF
```bash
# Generate all frames
python frame1.py
python frame2.py
python frame3.py

# Combine into animated GIF
convert -delay 100 -loop 0 frame*.png animation.gif
```

## Output Formats

Diagrams supports multiple output formats:

```python
with Diagram("My Diagram", filename="output", show=False, outformat="png"):
    # Your diagram code
```

Supported formats:
- `png` (default)
- `jpg`
- `svg`
- `pdf`
- `dot`

## Tips & Best Practices

1. **Direction:** Control layout with `direction` parameter
   - `LR` - Left to Right
   - `TB` - Top to Bottom
   - `RL` - Right to Left
   - `BT` - Bottom to Top

2. **Clustering:** Group related components
   ```python
   with Cluster("Group Name"):
       # components
   ```

3. **Edge Labels:** Add labels to connections
   ```python
   a >> Edge(label="HTTP") >> b
   ```

4. **Custom Attributes:** Style your diagrams
   ```python
   graph_attr = {
       "fontsize": "16",
       "bgcolor": "white"
   }
   ```

5. **Multiple Connections:** Connect to multiple nodes
   ```python
   a >> [b, c, d]
   ```

## Browse All Available Icons

Visit the official documentation:
- https://diagrams.mingrammer.com/docs/nodes/onprem
- https://diagrams.mingrammer.com/docs/nodes/aws
- https://diagrams.mingrammer.com/docs/nodes/azure
- https://diagrams.mingrammer.com/docs/nodes/gcp
- https://diagrams.mingrammer.com/docs/nodes/k8s

## Troubleshooting

### Error: "Graphviz executables not found"
```bash
brew install graphviz
```

### Error: "No module named 'diagrams'"
```bash
uv pip install diagrams
```

### Images not generating
Make sure `show=False` is set in the Diagram constructor to save files instead of displaying them.

## Next Steps

1. Run the example scripts to see the output
2. Modify the diagrams to match your specific architecture
3. Create animated sequences by generating multiple frames
4. Export to different formats for presentations or social media

