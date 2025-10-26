# Diagrams

Architecture diagrams and animations for the social-notebook project.

## 📁 Directory Structure

```
diagrams/
├── plantuml/              # PlantUML static diagrams
│   ├── diagrams/          # .puml files
│   ├── docs/              # Documentation
│   └── plantuml-stdlib/   # Icon libraries
│
├── python-diagrams/       # Python Diagrams (static frames)
│   ├── scripts/           # Python & shell scripts
│   ├── output/            # Generated media
│   │   ├── images/       # PNG, SVG
│   │   ├── gifs/         # Animated GIFs
│   │   └── videos/       # MP4 videos
│   ├── docs/              # Documentation
│   └── requirements.txt   # Dependencies
│
└── manim-animations/      # Manim smooth animations ⭐
    ├── animations/        # Python animation scripts
    ├── output/            # Generated videos
    │   ├── videos/       # MP4 outputs
    │   └── gifs/         # GIF conversions
    └── docs/              # Documentation
```

---

## 🎨 PlantUML (`plantuml/`)

**Static diagrams** with extensive icon libraries.

### Features
- ✅ Kubernetes icons (40+ components)
- ✅ Kafka logos
- ✅ AWS, Azure, GCP icons (1000+)
- ✅ Best for documentation

### Quick Start
```bash
# View in VS Code with PlantUML extension
# or online at plantuml.com
```

**→ [Full PlantUML Guide](plantuml/README.md)**

---

## 📊 Python Diagrams (`python-diagrams/`)

**Code-generated diagrams** with actual tech stack icons.

### Features
- ✅ 1000+ tech icons (Kafka, AWS, K8s, databases)
- ✅ Multiple formats (PNG, SVG, GIF, MP4)
- ✅ Dark/transparent backgrounds
- ✅ Frame-based animations

### Quick Start
```bash
cd python-diagrams/scripts

# Generate diagram
python kafka_simple.py
# Output: ../output/images/kafka_simple.png

# Create animation
python create_animation.py
./create_gif.sh
# Output: ../output/gifs/kafka_animation.gif
```

**→ [Full Python Diagrams Guide](python-diagrams/README.md)**

---

## 🎬 Manim Animations (`manim-animations/`) ⭐ BEST FOR SOCIAL MEDIA

**Professional smooth flowing animations** - Cinema quality!

### Features
- ✅ **Smooth transitions** - Icons fade in gradually
- ✅ **Growing arrows** - Arrows appear progressively
- ✅ **Flowing data** - Animated packets moving through system
- ✅ **Pulsing effects** - Components pulse and glow
- ✅ **Professional quality** - Like 3Blue1Brown videos

### Quick Start
```bash
cd manim-animations/animations

# Preview (fast, low quality)
manim -pql kafka_smooth.py KafkaFlowAnimation

# Export for Instagram Reels / TikTok
manim -pqh -r 1080,1920 kafka_smooth.py KafkaFlowAnimation

# Export for Instagram Posts
manim -pqh -r 1080,1080 kafka_smooth.py KafkaFlowAnimation
```

**→ [Full Manim Guide](manim-animations/README.md)**

---

## 🎯 Which Tool to Use?

| Use Case | Tool | Reason |
|----------|------|--------|
| **Smooth social media animations** | Manim | True flowing animations |
| **Static diagrams with K8s icons** | PlantUML | Native K8s library |
| **Static diagrams with Kafka icons** | Python Diagrams | Actual Kafka icons |
| **Instagram Reels / TikTok** | Manim | Smooth, engaging |
| **Documentation** | PlantUML | Easy to maintain |
| **GitHub README animations** | Python Diagrams | GIF export |

---

## 🚀 Quick Comparison

### Static Diagrams
```bash
# PlantUML - for K8s
code plantuml/diagrams/diagram.puml

# Python Diagrams - for Kafka
cd python-diagrams/scripts
python kafka_simple.py
```

### Animations
```bash
# Frame-based (choppy but simple)
cd python-diagrams/scripts
python create_animation.py
./create_gif.sh

# Smooth flowing (professional)
cd manim-animations/animations
manim -pqh kafka_smooth.py KafkaFlowAnimation
```

---

## 📦 Installation

### PlantUML
```bash
# Use VS Code PlantUML extension
# or IntelliJ IDEA plugin
```

### Python Diagrams
```bash
brew install graphviz imagemagick ffmpeg
pip install -r python-diagrams/requirements.txt
```

### Manim
```bash
brew install ffmpeg
pip install manim
```

---

## 📚 Documentation

Each tool has detailed documentation in its respective folder:

- **[plantuml/README.md](plantuml/README.md)** - PlantUML guide
- **[python-diagrams/README.md](python-diagrams/README.md)** - Python Diagrams guide
- **[manim-animations/README.md](manim-animations/README.md)** - Manim guide

---

## 💡 Recommended Workflow

### For Social Media Content (Reels, TikTok)
1. **Use Manim** for smooth animations
2. Navigate to `manim-animations/animations/`
3. Modify or create new animation script
4. Export with: `manim -pqh -r 1080,1920 your_script.py YourScene`

### For Documentation
1. **Use PlantUML** for static diagrams
2. Edit `.puml` files in `plantuml/diagrams/`
3. View in IDE or export to PNG/SVG

### For Blog Posts / Articles
1. **Use Python Diagrams** for static images
2. Navigate to `python-diagrams/scripts/`
3. Run Python script: `python your_diagram.py`
4. Find output in `../output/images/`

---

## 🎓 Learning Resources

- **PlantUML**: [plantuml.com](https://plantuml.com)
- **Python Diagrams**: [diagrams.mingrammer.com](https://diagrams.mingrammer.com)
- **Manim**: [docs.manim.community](https://docs.manim.community)

---

**Perfect for creating engaging tech content for your social-notebook project!** 🚀
