# Kafka PlantUML Diagrams

This directory contains PlantUML diagrams showing Kafka event streaming architecture with the orders processing pipeline.

## Files

- `kafka-diagram.puml` - Comprehensive Kafka cluster architecture with brokers, topics, and consumer groups
- `kafka-simple.puml` - Simplified Kafka messaging flow focusing on the orders topic
- `kafka-sequence.puml` - Sequence diagram showing the order processing flow

## Architecture Overview

The diagrams illustrate an event-driven architecture where:

### Components
- **Checkout Service** (Producer) - Publishes order events to Kafka
- **Kafka Cluster** - Manages the orders topic with 3 partitions
- **Inventory Manager** (Consumer) - Processes orders for stock management
- **Billing Manager** (Consumer) - Processes orders for billing and invoicing

### Topic Structure
- **Topic Name**: `orders`
- **Partitions**: 3 (for scalability and parallel processing)
- **Replication Factor**: 3 (for fault tolerance)
- **Retention**: 7 days

### Consumer Groups
- **inventory-group**: Processes order events for inventory management
- **billing-group**: Processes order events for billing operations

## Message Flow

1. **Order Creation**: Checkout service creates an order and publishes it to the `orders` topic
2. **Message Distribution**: Kafka distributes the message across partitions based on order ID hash
3. **Parallel Consumption**: Both consumer groups independently consume the same order event
4. **Processing**: Each service processes the order according to its business logic

## Event Schema

Each order event contains:
```json
{
  "orderId": "12345",
  "customerId": "67890", 
  "items": [
    {
      "productId": "ABC123",
      "quantity": 2,
      "price": 29.99
    }
  ],
  "totalAmount": 99.99,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Benefits of This Architecture

### Scalability
- Multiple partitions allow parallel processing
- Consumer groups can scale horizontally
- Each service can process orders independently

### Reliability
- Message persistence with replication
- Fault tolerance through consumer groups
- At-least-once delivery guarantees

### Decoupling
- Services are loosely coupled through events
- No direct dependencies between inventory and billing
- Easy to add new consumers without affecting existing ones

## Available Kafka Icons

The diagrams use icons from the plantum-stdlib:

### CloudInsight Library
- `$kafka` - Kafka logo sprite
- `!include <cloudinsight/kafka>` - Basic Kafka icon

### DevIcons2 Library  
- `DEV2_APACHEKAFKA_ORIGINAL` - Apache Kafka original logo
- `!include <tupadr3/devicons2/apachekafka_original>` - Full Kafka icon set

## Usage Examples

### Basic Producer-Consumer
```plantuml
!include <cloudinsight/kafka>
!include <tupadr3/devicons2/apachekafka_original>

DEV2_APACHEKAFKA_ORIGINAL(producer, "Producer", rectangle, #FF6B6B)
DEV2_APACHEKAFKA_ORIGINAL(consumer, "Consumer", rectangle, #4ECDC4)
rectangle "orders Topic" as topic

Rel(producer, topic, "Publishes")
Rel(topic, consumer, "Consumes")
```

### Consumer Groups
```plantuml
rectangle "orders Topic" as topic
rectangle "group-1" as group1 {
    DEV2_APACHEKAFKA_ORIGINAL(consumer1, "Consumer 1")
}
rectangle "group-2" as group2 {
    DEV2_APACHEKAFKA_ORIGINAL(consumer2, "Consumer 1")
}

Rel(topic, consumer1, "Consumes")
Rel(topic, consumer2, "Consumes")
```

## Best Practices

1. **Partitioning Strategy**: Use meaningful partition keys (e.g., customer ID, order ID)
2. **Consumer Groups**: Each service should have its own consumer group
3. **Error Handling**: Implement retry logic and dead letter queues
4. **Monitoring**: Track consumer lag and processing metrics
5. **Schema Evolution**: Use schema registry for message compatibility

## Rendering

To render these diagrams:
- Use PlantUML online server
- VS Code PlantUML extension
- PlantUML command line tool
- Include the required icon libraries from plantum-stdlib
