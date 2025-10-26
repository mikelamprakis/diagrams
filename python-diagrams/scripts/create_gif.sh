#!/bin/bash

# Create animated GIF from frames
# Make sure you've run create_animation.py first

echo "🎬 Creating animated GIF from frames..."

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "❌ ImageMagick not found. Installing..."
    brew install imagemagick
fi

# Create animated GIF
convert -delay 150 -loop 0 \
    frame_01_producer.png \
    frame_02_kafka.png \
    frame_03_consumer1.png \
    frame_04_consumer2.png \
    frame_05_partitions.png \
    -resize 1920x1080 \
    kafka_animation.gif

echo "✅ Animation created: kafka_animation.gif"
echo ""
echo "Animation settings:"
echo "  - Delay: 150ms between frames (1.5 seconds)"
echo "  - Loop: Infinite"
echo "  - Size: 1920x1080 (Full HD)"
echo ""
echo "To adjust timing, edit the -delay value (in 1/100th of a second)"
echo "  -delay 100 = 1 second"
echo "  -delay 150 = 1.5 seconds"
echo "  -delay 200 = 2 seconds"

