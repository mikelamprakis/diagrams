#!/bin/bash

# Generate all Instagram carousel slides for Kafka Basics v2
# Output: PNG images optimized for Instagram (1080x1080)

echo "🎨 Generating Instagram Carousel: Kafka Basics v2"
echo "=================================================="
echo ""

# Navigate to script directory
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "../../../../../.venv" ]; then
    source ../../../../../.venv/bin/activate
    echo "✅ Virtual environment activated"
elif [ -d "../../../.venv" ]; then
    source ../../../.venv/bin/activate
    echo "✅ Virtual environment activated"
fi

# Generate each slide
slides=(
    "slide_01_cover.py"
    "slide_02_problem.py"
    "slide_03_broker.py"
    "slide_04_topics.py"
    "slide_05_producers_consumers.py"
    "slide_06_cluster.py"
    "slide_07_partitions.py"
    "slide_08_replication.py"
    "slide_09_use_cases.py"
    "slide_10_summary.py"
)

total=${#slides[@]}
current=0

for slide in "${slides[@]}"; do
    current=$((current + 1))
    echo "[$current/$total] Generating $slide..."
    python "$slide"
    
    if [ $? -eq 0 ]; then
        echo "  ✅ Success"
    else
        echo "  ❌ Failed"
        exit 1
    fi
done

echo ""
echo "=================================================="
echo "✨ All slides generated successfully!"
echo ""
echo "📁 Output location:"
echo "   ../../../output/carousels/kafka-basics-v2/"
echo ""
echo "📱 Ready for Instagram upload!"
echo ""
echo "💡 v2 Features:"
echo "   • More detailed architecture diagrams"
echo "   • Real-world use cases (Netflix, Spotify, etc.)"
echo "   • Replication & fault tolerance explained"
echo "   • Complete end-to-end pipeline"
echo "=================================================="

