# Instagram Carousel: Kafka Basics v1

A 10-slide Instagram carousel explaining Apache Kafka fundamentals with beautiful diagrams.

## 📱 Carousel Structure

### Slide Flow (Storytelling Order)

1. **Intro** - What is Apache Kafka?
2. **Problem** - Traditional message queues fail at scale
3. **Solution** - Kafka distributed streaming
4. **Producer** - Services send events to Kafka
5. **Topics** - Organizing events by category
6. **Partitions** - Horizontal scaling mechanism
7. **Consumers** - Services read events from topics
8. **Consumer Groups** - Parallel processing
9. **Complete Flow** - End-to-end message flow
10. **Benefits** - Why use Kafka?

## 🚀 Quick Start

### Generate All Slides

```bash
cd diagrams/python-diagrams/scripts/carousels/kafka-basics-v1/

# Make script executable
chmod +x generate_all.sh

# Generate all slides
./generate_all.sh
```

### Generate Single Slide

```bash
# Activate virtual environment first (if needed)
source ../../../.venv/bin/activate

# Generate specific slide
python slide_01_intro.py
python slide_05_topics.py
# etc.
```

## 📁 Output Location

All generated images will be saved to:
```
diagrams/python-diagrams/output/carousels/kafka-basics-v1/
├── slide_01_intro.png
├── slide_02_problem.png
├── slide_03_solution.png
├── slide_04_producer.png
├── slide_05_topics.png
├── slide_06_partitions.png
├── slide_07_consumers.png
├── slide_08_consumer_groups.png
├── slide_09_complete_flow.png
└── slide_10_benefits.png
```

## 🎨 Design Specs

- **Format**: PNG
- **Size**: 1080x1080 (Instagram square)
- **DPI**: 300 (high quality)
- **Background**: Dark (#0f0f0f) - Instagram-friendly
- **Text Color**: White
- **Accent Color**: Teal (#4ECDC4)
- **Font**: Arial (clean, readable on mobile)

## 📱 Instagram Upload Guide

### Step 1: Upload to Instagram
1. Open Instagram app
2. Tap "+" to create new post
3. Select all 10 images in order (01 → 10)
4. Tap "Next"

### Step 2: Write Caption

**Suggested Caption:**
```
🔥 Apache Kafka Explained (Swipe 👉)

Everything you need to know about Kafka in 10 slides:

1️⃣ What is Kafka?
2️⃣ The problem it solves
3️⃣ How it works
4️⃣ Producers & Consumers
5️⃣ Topics & Partitions
6️⃣ Consumer Groups
7️⃣ Complete flow
8️⃣ Why companies use it

💡 Kafka powers real-time data at Netflix, Uber, LinkedIn, and thousands of companies.

📚 Save this for your next system design interview!

#kafka #systemdesign #softwareengineering #backend #distributedsystems #tech #coding #programming #developer #learntocode
```

### Step 3: Add Hashtags

**Recommended Tags:**
- #kafka
- #apachekafka
- #systemdesign
- #softwareengineering
- #backend
- #distributedsystems
- #microservices
- #eventstreaming
- #programming
- #coding

## 🎯 Engagement Tips

### Best Posting Times
- **Weekdays**: 11 AM - 1 PM, 7 PM - 9 PM
- **Weekends**: 9 AM - 11 AM, 5 PM - 7 PM

### Caption Strategy
- Start with a hook ("🔥 Apache Kafka Explained")
- Use emojis for visual breaks
- Number the slides
- Ask for engagement ("Save this!", "Which slide helped you most?")
- Include call-to-action

### Story Reshare
- Share slide 1 to your story
- Add poll: "Ever used Kafka?" Yes/No
- Add link sticker to full carousel

## 🔧 Customization

### Change Colors
Edit the `graph_attr` in each Python file:

```python
graph_attr = {
    "bgcolor": "#0f0f0f",  # Background color
    "fontcolor": "white",  # Text color
}

edge_attr = {
    "color": "#4ECDC4",  # Accent color (arrows, connections)
}
```

### Change Size
For different formats:

```python
# Square (Instagram feed)
graph_attr = {"dpi": "300"}  # Default 1080x1080

# Portrait (Instagram Stories)
# Manually set with image editor after generation

# Landscape (LinkedIn)
# Use direction="LR" for better landscape fit
```

### Add More Content
Each slide is a standalone Python script. Modify as needed:
- Add more nodes
- Change labels
- Adjust layout direction
- Add clusters

## 📊 Expected Engagement

Based on tech content performance:

- **Impressions**: 500-2,000
- **Likes**: 50-200
- **Saves**: 30-150 (high-value educational content)
- **Shares**: 10-50
- **Comments**: 5-20

**💡 Carousel posts get 3x more engagement than single images!**

## 🔄 Variations

Create more versions:
- `kafka-basics-v2/` - Different color scheme
- `kafka-advanced-v1/` - Deep dive topics
- `kafka-vs-rabbitmq-v1/` - Comparison
- `kafka-production-tips-v1/` - Best practices

## 📝 Notes

- All slides use actual Kafka icons from the `diagrams` library
- Dark background performs better on Instagram
- Keep text concise for mobile readability
- Test one slide first before generating all 10

## 🐛 Troubleshooting

### Issue: Import errors
```bash
# Install dependencies
pip install diagrams
brew install graphviz
```

### Issue: Font not found
```bash
# The scripts will fall back to default fonts
# For best results, use Arial (usually pre-installed)
```

### Issue: Images not generating
```bash
# Check virtual environment
source ../../../.venv/bin/activate

# Verify diagrams is installed
pip list | grep diagrams
```

---

**Created**: 2025-10-25  
**Version**: 1.0  
**Status**: Ready for Instagram 📱✨

