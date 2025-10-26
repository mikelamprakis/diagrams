# Python Diagrams

Code-generated diagrams with actual tech stack icons (Kafka, AWS, K8s, databases, etc.)

## 📁 Structure

```
python-diagrams/
├── scripts/           # Python & shell scripts
│   ├── kafka_*.py    # Diagram generation scripts
│   ├── create_*.py   # Animation frame generators
│   └── *.sh          # Shell automation scripts
├── output/            # Generated media
│   ├── images/       # PNG, SVG outputs
│   ├── gifs/         # Animated GIFs
│   └── videos/       # MP4 videos
├── docs/              # Documentation
└── requirements.txt   # Python dependencies
```

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
brew install graphviz imagemagick ffmpeg
pip install -r requirements.txt

# Or use the setup script
cd scripts
./setup.sh
```

### Generate Static Diagrams
```bash
cd scripts

# Simple clean diagram
python kafka_simple.py
# Output: ../output/images/kafka_simple.png

# Full architecture
python kafka_architecture.py
# Output: ../output/images/kafka_orders.png

# Dark theme (transparent background)
python kafka_dark_theme.py
# Output: ../output/images/kafka_dark.png

# Black background
python kafka_black_bg.py
# Output: ../output/images/kafka_black.png
```

### Create Animations

#### Animated GIF
```bash
cd scripts

# Generate frames
python create_animation.py
# Creates: frame_01.png, frame_02.png, etc.

# Combine into GIF
./create_gif.sh
# Output: ../output/gifs/kafka_animation.gif
```

#### Social Media Videos
```bash
cd scripts

# Generate frames (if not already done)
python create_animation.py

# Create videos for all platforms
./create_video.sh
# Outputs:
#   ../output/videos/kafka_square.mp4 (1080x1080 - Instagram)
#   ../output/videos/kafka_vertical.mp4 (1080x1920 - Reels/TikTok)
#   ../output/videos/kafka_horizontal.mp4 (1920x1080 - YouTube)
```

## 📊 Available Scripts

### Diagram Scripts
- `kafka_simple.py` - Clean simple Kafka flow
- `kafka_architecture.py` - Full architecture with partitions
- `kafka_detailed.py` - Detailed cluster with brokers
- `kafka_dark_theme.py` - Transparent background version
- `kafka_black_bg.py` - Black background version

### Animation Scripts
- `create_animation.py` - Generate animation frames
- `create_gif.sh` - Combine frames into GIF
- `create_video.sh` - Create social media videos

### Setup
- `setup.sh` - One-click installation

## 🎨 Features

✅ **1000+ Tech Icons** - Kafka, AWS, K8s, databases, etc.  
✅ **Multiple Formats** - PNG, SVG, GIF, MP4  
✅ **Dark Themes** - Transparent or black backgrounds  
✅ **Social Media Ready** - Pre-configured for Reels, TikTok, Instagram  

## 📚 Documentation

See `docs/` for:
- Animation guide
- Icon reference
- Customization tips

## ⚠️ Limitations

- Creates **static frames**, not smooth animations
- For smooth flowing animations, use `../manim-animations`

