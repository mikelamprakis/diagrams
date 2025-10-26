# Manim Smooth Animations

Professional, cinema-quality flowing animations for tech content.

## 📁 Structure

```
manim-animations/
├── animations/        # Python animation scripts  
│   ├── kafka_smooth.py    # Clean smooth Kafka flow
│   └── kafka_advanced.py  # Advanced with effects
├── output/            # Generated videos (created by manim)
│   ├── videos/       # MP4 video outputs
│   └── gifs/         # GIF conversions
├── docs/              # Documentation
└── media/             # Manim's media cache (auto-generated)
```

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
brew install ffmpeg
pip install manim
```

### Preview Animation (Fast)
```bash
cd animations

# Low quality preview (fast rendering)
manim -pql kafka_smooth.py KafkaFlowAnimation
```

### High Quality Export
```bash
cd animations

# Full HD quality
manim -pqh kafka_smooth.py KafkaFlowAnimation
```

### Social Media Formats
```bash
cd animations

# Instagram Reels / TikTok (1080x1920 vertical)
manim -pqh -r 1080,1920 kafka_smooth.py KafkaFlowAnimation

# Instagram Post (1080x1080 square)
manim -pqh -r 1080,1080 kafka_smooth.py KafkaFlowAnimation

# YouTube (1920x1080 horizontal)
manim -pqh -r 1920,1080 kafka_smooth.py KafkaFlowAnimation
```

## 🎬 Available Animations

### `kafka_smooth.py` - KafkaFlowAnimation
**Duration:** ~15 seconds  
**Features:**
- ✅ Icons fade in gradually
- ✅ Arrows grow smoothly
- ✅ Animated data packets flowing
- ✅ Pulsing effects
- ✅ Professional transitions

**Best for:** Quick Reels, TikTok videos

### `kafka_advanced.py` - KafkaAdvancedFlow
**Duration:** ~20 seconds  
**Features:**
- ✅ Dark theme background
- ✅ Partition visualization
- ✅ Multiple data packets
- ✅ Glow effects
- ✅ More detailed architecture

**Best for:** Detailed explanations, YouTube videos

## 🎨 Animation Effects

### What You Get
- **Smooth fades** - Components appear gradually
- **Growing arrows** - Arrows draw from start to end
- **Moving objects** - Data packets travel along paths
- **Pulsing** - Components pulse and glow
- **Professional timing** - Perfectly timed transitions

### vs. Other Tools
- ❌ Python Diagrams = Static frames (choppy)
- ✅ Manim = True smooth animations (cinema-quality)

## 📹 Output Locations

After rendering, videos are in:
```
../media/videos/kafka_smooth/[quality]/KafkaFlowAnimation.mp4
```

Quality options:
- `-ql` = 480p (preview)
- `-qm` = 720p
- `-qh` = 1080p (social media)
- `-qk` = 4K

## 🎓 Customization

### Change Colors
Edit in the `.py` files:
```python
fill_color="#FF6B6B"  # Red
fill_color="#4ECDC4"  # Teal
fill_color="#45B7D1"  # Blue
```

### Adjust Speed
```python
self.play(FadeIn(box), run_time=1.5)  # Slower
self.play(FadeIn(box), run_time=0.5)  # Faster
```

### Change Background
```python
self.camera.background_color = "#1a1a1a"  # Dark
self.camera.background_color = WHITE      # Light  
self.camera.background_color = "transparent"  # Transparent
```

## 📚 Documentation

See `docs/README.md` for:
- Complete animation guide
- Effects reference
- Troubleshooting
- Advanced techniques

## 🎯 Best For

✅ Social media content (Reels, TikTok, YouTube Shorts)  
✅ Educational tech videos  
✅ Conference presentations  
✅ Marketing materials  

This is the **recommended tool** for creating engaging animated content for your social-notebook project! 🚀
