# PlantUML Diagrams

Static architecture diagrams using PlantUML with extensive icon libraries.

## 📁 Structure

```
plantuml/
├── diagrams/          # .puml diagram files
├── docs/              # Documentation
└── plantuml-stdlib/   # Icon libraries (K8s, AWS, Azure, Kafka logos)
```

## 🚀 Quick Start

### View Diagrams
Open any `.puml` file in:
- VS Code with PlantUML extension
- IntelliJ IDEA with PlantUML plugin
- [PlantUML Online Server](http://www.plantuml.com/plantuml/uml/)

### Available Diagrams

#### Kubernetes
- `diagram.puml` - Full K8s cluster architecture
- `simple-example.puml` - Simple microservices example

#### Kafka
- `kafka-clean.puml` - Clean Kafka flow
- `kafka-simple.puml` - Simple producer-consumer
- `kafka-diagram.puml` - Full cluster with brokers
- `kafka-improved.puml` - Comprehensive setup
- `kafka-sequence.puml` - Sequence diagram
- `kafka-fixed.puml` - Fixed version without K8s syntax

## 📚 Documentation

See `docs/` folder for:
- Detailed icon documentation
- Kafka icons analysis
- Usage examples

## ⚠️ Note

PlantUML is best for:
- Static diagrams
- Documentation
- K8s architectures (has full K8s icon library)

For Kafka with proper icons and animations, use `../python-diagrams` or `../manim-animations`

