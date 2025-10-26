# Creating Animated Kafka Diagrams 🎬

This guide shows you how to create animated diagrams for social media from code!

## Background Options

### 1. Transparent Background (Best for overlays)
```python
graph_attr = {
    "bgcolor": "transparent",
}
```
**Use for:** Instagram Stories, overlaying on videos, presentations

### 2. Black Background (Dark mode)
```python
graph_attr = {
    "bgcolor": "#000000",  # Pure black
    # or
    "bgcolor": "#1a1a1a",  # Dark gray
}
```
**Use for:** Dark themed content, tech presentations

### 3. White Background (Default)
```python
graph_attr = {
    "bgcolor": "white",
}
```
**Use for:** Light themed content, documentation

## Creating Animations

### Quick Start - Animated GIF

```bash
# Step 1: Generate all frames
python create_animation.py

# Step 2: Combine into GIF
./create_gif.sh
```

**Output:** `kafka_animation.gif` - Perfect for GitHub README, documentation

---

### Social Media Videos - MP4

```bash
# Step 1: Generate all frames
python create_animation.py

# Step 2: Create videos for social media
./create_video.sh
```

**Outputs:**
- `kafka_square.mp4` (1080x1080) - Instagram Posts
- `kafka_vertical.mp4` (1080x1920) - Instagram Reels, TikTok, YouTube Shorts
- `kafka_horizontal.mp4` (1920x1080) - YouTube, LinkedIn

---

## Generated Files

### Static Diagrams (with backgrounds)
```bash
python kafka_dark_theme.py    # → kafka_dark.png (transparent)
python kafka_black_bg.py       # → kafka_black.png (black bg)
```

### Animation Frames
```bash
python create_animation.py     # → frame_01.png through frame_05.png
```

### Final Animations
```bash
./create_gif.sh               # → kafka_animation.gif
./create_video.sh             # → 3 MP4 files for social media
```

---

## Customization

### Adjust Animation Speed

Edit `create_gif.sh`:
```bash
convert -delay 150 ...  # Change 150 to adjust speed
# -delay 100 = 1 second per frame
# -delay 150 = 1.5 seconds per frame
# -delay 200 = 2 seconds per frame
```

### Adjust Video Timing

Edit `create_video.sh`:
```bash
duration 1.5  # Change to adjust how long each frame shows
```

### Change Colors

In `create_animation.py`, modify edge colors:
```python
Edge(label="Publish", color="#FF6B6B")  # Red
Edge(label="inventory", color="#4ECDC4")  # Teal
Edge(label="billing", color="#45B7D1")  # Blue
```

### Add More Frames

Edit `create_animation.py` and add more diagram generations:
```python
# Frame 6: Your custom frame
print("Generating Frame 6: Custom...")
with Diagram(
    "Kafka Orders Processing",
    filename="frame_06_custom",
    show=False,
    # ... your diagram code
):
    # Add your components here
    pass
```

Then update `create_gif.sh` to include the new frame:
```bash
convert -delay 150 -loop 0 \
    frame_01_producer.png \
    frame_02_kafka.png \
    frame_03_consumer1.png \
    frame_04_consumer2.png \
    frame_05_partitions.png \
    frame_06_custom.png \
    kafka_animation.gif
```

---

## Tips for Social Media

### Instagram Reels / TikTok
- Use vertical format (1080x1920)
- Keep each frame 1-2 seconds
- Use transparent or dark backgrounds
- Add text overlays in your video editor

### YouTube Shorts
- Use vertical format (1080x1920)
- 2-3 seconds per frame works well
- Add voiceover or music

### Instagram Posts
- Use square format (1080x1080)
- Can be slower (2-3 seconds per frame)
- Works great in carousels

### LinkedIn
- Use horizontal format (1920x1080)
- Professional dark theme works well
- Longer durations (3-4 seconds) for detailed frames

---

## Advanced: Custom Animation Sequence

Create your own animation by copying `create_animation.py` and modifying the frames:

```python
# Example: Showing data flow
# Frame 1: Empty system
# Frame 2: Order arrives
# Frame 3: Order in Kafka
# Frame 4: Consumers processing
# Frame 5: Final state
```

---

## Requirements

### For GIF Creation
```bash
brew install imagemagick
```

### For Video Creation
```bash
brew install ffmpeg
```

---

## Troubleshooting

### "convert: command not found"
```bash
brew install imagemagick
```

### "ffmpeg: command not found"
```bash
brew install ffmpeg
```

### Frames look pixelated
Increase resolution in the scripts:
```bash
-resize 1920x1080  # Change to higher resolution like 2560x1440
```

### Animation too fast/slow
Adjust `-delay` in `create_gif.sh` or `duration` in `create_video.sh`

---

## Examples

### Generate Everything
```bash
# Generate all diagrams
python kafka_simple.py
python kafka_dark_theme.py
python kafka_black_bg.py

# Create animation
python create_animation.py
./create_gif.sh
./create_video.sh
```

Now you have:
- Static diagrams (light/dark/transparent backgrounds)
- Animated GIF for documentation
- 3 video formats for different social platforms

Perfect for your social-notebook project! 🚀

