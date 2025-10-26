#!/bin/bash

# Create MP4 video from frames for social media (Reels/TikTok)
# Make sure you've run create_animation.py first

echo "🎥 Creating video from frames..."

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg not found. Installing..."
    brew install ffmpeg
fi

# Create a file list for FFmpeg
cat > frames.txt << EOF
file 'frame_01_producer.png'
duration 1.5
file 'frame_02_kafka.png'
duration 1.5
file 'frame_03_consumer1.png'
duration 1.5
file 'frame_04_consumer2.png'
duration 1.5
file 'frame_05_partitions.png'
duration 2.0
EOF

# Create MP4 video (1080x1080 for Instagram, 1080x1920 for Reels/TikTok)
echo "Creating square video (1080x1080) for Instagram..."
ffmpeg -f concat -safe 0 -i frames.txt -vf "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2" -pix_fmt yuv420p -y kafka_square.mp4

echo "Creating vertical video (1080x1920) for Reels/TikTok..."
ffmpeg -f concat -safe 0 -i frames.txt -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -pix_fmt yuv420p -y kafka_vertical.mp4

echo "Creating horizontal video (1920x1080) for YouTube..."
ffmpeg -f concat -safe 0 -i frames.txt -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -pix_fmt yuv420p -y kafka_horizontal.mp4

# Clean up
rm frames.txt

echo ""
echo "✅ Videos created:"
echo "  - kafka_square.mp4 (1080x1080) - Instagram Posts"
echo "  - kafka_vertical.mp4 (1080x1920) - Instagram Reels, TikTok"
echo "  - kafka_horizontal.mp4 (1920x1080) - YouTube, LinkedIn"
echo ""
echo "Each frame displays for 1.5 seconds, final frame for 2 seconds"

