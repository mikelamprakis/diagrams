# Kafka Icon Libraries in PlantUML Stdlib

## Available Kafka Icons

Unfortunately, there are **no dedicated Kafka component libraries** in the plantum-stdlib. However, there are several Kafka logo/icons available:

### 1. Logos Library
- `!include <logos/kafka>` - Kafka wordmark logo
- `!include <logos/kafka-icon>` - Kafka icon sprite

### 2. CloudInsight Library  
- `!include <cloudinsight/kafka>` - Kafka logo sprite (`$kafka`)

### 3. DevIcons2 Library
- `!include <tupadr3/devicons2/apachekafka_original>` - Apache Kafka original logo
- `!include <tupadr3/devicons2/apachekafka_original_wordmark>` - Apache Kafka wordmark

## What's Missing

Unlike Kubernetes (which has a comprehensive `k8s` library), Kafka lacks:
- ❌ Dedicated Kafka component icons (Producer, Consumer, Broker, Topic, Partition)
- ❌ Kafka-specific styling and colors
- ❌ Pre-built Kafka architecture templates
- ❌ Kafka messaging flow components

## Alternative Approaches

### 1. Use Generic Icons
```plantuml
!include <logos/kafka>
!include <cloudinsight/kafka>

rectangle "Producer" as producer {
    $kafka
}
rectangle "Topic" as topic {
    $kafka
}
rectangle "Consumer" as consumer {
    $kafka
}
```

### 2. Use AWS Messaging Icons (for comparison)
```plantuml
!include <aws/Messaging/AmazonSQS>
!include <aws/Messaging/AmazonSNS>
!include <aws/Analytics/AmazonKinesis>

AmazonSQS(queue, "Message Queue", "SQS")
AmazonSNS(topic, "Topic", "SNS")
AmazonKinesis(stream, "Data Stream", "Kinesis")
```

### 3. Create Custom Components
```plantuml
!define KAFKA_PRODUCER(_alias, _label) rectangle _label as _alias <<Kafka Producer>>
!define KAFKA_CONSUMER(_alias, _label) rectangle _label as _alias <<Kafka Consumer>>
!define KAFKA_TOPIC(_alias, _label) rectangle _label as _alias <<Kafka Topic>>

KAFKA_PRODUCER(prod, "Producer")
KAFKA_TOPIC(topic, "Topic")
KAFKA_CONSUMER(cons, "Consumer")
```

## Available Messaging-Related Libraries

### AWS Messaging Services
- `aws/Messaging/AmazonSQS` - Simple Queue Service
- `aws/Messaging/AmazonSNS` - Simple Notification Service
- `aws/Messaging/AmazonPinpoint` - Customer engagement
- `aws/Messaging/AmazonSES` - Email service

### AWS Analytics/Streaming
- `aws/Analytics/AmazonKinesis` - Data streaming
- `aws/Analytics/AmazonKinesisAnalytics` - Stream analytics
- `aws/Analytics/AmazonKinesisFirehose` - Data delivery

### Generic Messaging Icons
- `tupadr3/material/queue` - Generic queue icon
- `tupadr3/material/view_stream` - Stream icon
- `office/Communications/queue_viewer` - Queue viewer
- `office/Communications/messages_queued` - Queued messages

## Recommendations

### For Kafka Diagrams:
1. **Use available Kafka logos** for branding/identification
2. **Create custom stereotypes** for Kafka components
3. **Use generic rectangles** with Kafka-specific labels
4. **Focus on architecture** rather than specific icons

### Example Custom Kafka Library:
```plantuml
!define KAFKA_PRODUCER(_alias, _label) rectangle _label as _alias <<Kafka Producer>>
!define KAFKA_CONSUMER(_alias, _label) rectangle _label as _alias <<Kafka Consumer>>
!define KAFKA_TOPIC(_alias, _label) rectangle _label as _alias <<Kafka Topic>>
!define KAFKA_BROKER(_alias, _label) rectangle _label as _alias <<Kafka Broker>>
!define KAFKA_PARTITION(_alias, _label) rectangle _label as _alias <<Partition>>

skinparam rectangle<<Kafka Producer>> {
    BackgroundColor #FF6B6B
    BorderColor #E53E3E
}
skinparam rectangle<<Kafka Consumer>> {
    BackgroundColor #4ECDC4
    BorderColor #38B2AC
}
skinparam rectangle<<Kafka Topic>> {
    BackgroundColor #45B7D1
    BorderColor #3182CE
}
skinparam rectangle<<Kafka Broker>> {
    BackgroundColor #96CEB4
    BorderColor #68D391
}
skinparam rectangle<<Partition>> {
    BackgroundColor #FECA57
    BorderColor #F39C12
}
```

## Conclusion

While plantum-stdlib doesn't have dedicated Kafka component libraries like it does for Kubernetes, you can still create effective Kafka diagrams using:
- Available Kafka logos for branding
- Custom stereotypes for component types
- Generic shapes with descriptive labels
- Color coding for different component types

The key is to focus on the **architecture and relationships** rather than relying on specific icons.
