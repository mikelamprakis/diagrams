# Manim Smooth Animations

Professional, smooth flowing animations for tech content using Manim (Mathematical Animation Engine).

## 🎬 What You Get

- **Smooth transitions** - Icons fade in gradually
- **Growing arrows** - Arrows appear progressively
- **Flowing data** - Animated dots moving through the system
- **Pulsing effects** - Components pulse and glow
- **Professional quality** - Cinema-grade animations

## 📦 Installation

```bash
# Install FFmpeg (required)
brew install ffmpeg

# Install Manim
pip install manim

# Or with uv
uv pip install manim
```

## 🚀 Quick Start

### Preview (Low Quality, Fast)
```bash
manim -pql kafka_smooth.py KafkaFlowAnimation
```

### High Quality Export
```bash
manim -pqh kafka_smooth.py KafkaFlowAnimation
```

### Social Media Formats

```bash
# Instagram Reels / TikTok (1080x1920 vertical)
manim -pqh -r 1080,1920 kafka_smooth.py KafkaFlowAnimation

# Instagram Post (1080x1080 square)
manim -pqh -r 1080,1080 kafka_smooth.py KafkaFlowAnimation

# YouTube (1920x1080 horizontal)
manim -pqh -r 1920,1080 kafka_smooth.py KafkaFlowAnimation
```

## 📁 Available Animations

### 1. `kafka_smooth.py` - KafkaFlowAnimation
**Features:**
- Smooth component appearance
- Growing arrows
- Animated data flow with moving dots
- Clean, modern design
- Perfect for educational content

**Duration:** ~15 seconds

**Best for:** 
- Quick explanations
- Instagram Reels
- TikTok videos

---

### 2. `kafka_advanced.py` - KafkaAdvancedFlow
**Features:**
- Dark theme background
- Pulsing components
- Multiple data packets flowing
- Partition visualization
- Glow effects on data
- More detailed architecture

**Duration:** ~20 seconds

**Best for:**
- Detailed technical explanations
- YouTube videos
- LinkedIn posts
- Conference presentations

---

## 🎨 Customization

### Change Colors

Edit the color values in the Python files:

```python
fill_color="#FF6B6B"  # Red for producer
fill_color="#45B7D1"  # Blue for Kafka
fill_color="#4ECDC4"  # Teal for consumers
```

### Adjust Animation Speed

Change `run_time` parameters:

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

### Modify Text

```python
title = Text("Your Custom Title", font_size=48)
```

## 🎯 Animation Effects Available

### Appearing Effects
- `FadeIn()` - Gradual fade in
- `Write()` - Text writing effect
- `GrowArrow()` - Arrow growing from start to end
- `Create()` - Drawing effect

### Movement
- `MoveAlongPath()` - Move object along a path
- `.animate.move_to()` - Smooth movement
- `.animate.shift()` - Relative movement

### Transformations
- `.animate.scale()` - Scale up/down
- `.animate.rotate()` - Rotation
- `Transform()` - Morph one object into another

### Effects
- `Flash()` - Quick flash
- Pulsing: `animate.scale(1.2).set_opacity(0.8)` with `there_and_back`

## 📹 Output Files

After rendering, videos are saved in:
```
media/videos/[script_name]/[quality]/[Scene_name].mp4
```

Example:
```
media/videos/kafka_smooth/1080p60/KafkaFlowAnimation.mp4
```

## 💡 Tips for Social Media

### Instagram Reels / TikTok
1. Use vertical format: `-r 1080,1920`
2. Keep duration under 15 seconds for Reels, 60 seconds for TikTok
3. Add text overlays for context
4. Use trending music (add in editing software)

### YouTube Shorts
1. Use vertical format: `-r 1080,1920`
2. Keep under 60 seconds
3. Add engaging title cards

### LinkedIn
1. Use horizontal format: `-r 1920,1080`
2. Professional color scheme
3. Keep it informative

## 🔧 Troubleshooting

### "command not found: manim"
```bash
pip install manim
# or
uv pip install manim
```

### "ffmpeg not found"
```bash
brew install ffmpeg
```

### Slow rendering
Use low quality for preview:
```bash
manim -pql  # Low quality, fast
manim -pqm  # Medium quality
manim -pqh  # High quality (slow)
```

### Black screen / No output
Check that scene name matches the class name:
```bash
manim -pql kafka_smooth.py KafkaFlowAnimation
#                           ^^^^^^^^^^^^^^^^^^
#                           Must match class name
```

## 📚 Learn More

- [Manim Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [Tutorial Videos](https://www.youtube.com/c/TheoremofBeethoven)

## 🎓 Creating Your Own Animations

### Basic Template

```python
from manim import *

class MyAnimation(Scene):
    def construct(self):
        # Create objects
        box = Square(fill_color=BLUE, fill_opacity=0.7)
        text = Text("Hello", font_size=48)
        
        # Animate
        self.play(Create(box), run_time=1)
        self.play(FadeIn(text), run_time=0.5)
        self.wait(2)
```

### Render it
```bash
manim -pql myfile.py MyAnimation
```

## 🌟 Next Steps

1. **Try the examples** - Run both animations to see the difference
2. **Customize colors** - Match your brand colors
3. **Add your logo** - Import SVG of your logo
4. **Export for social media** - Use the resolution commands above
5. **Add voiceover** - Use video editing software to add audio

Perfect for creating engaging tech content for your social-notebook project! 🚀

