#!/bin/bash

# Generate all Instagram carousel slides for Kafka Basics v1
# Output: PNG images optimized for Instagram (1080x1080)

echo "🎨 Generating Instagram Carousel: Kafka Basics v1"
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
    "slide_01_intro.py"
    "slide_02_problem.py"
    "slide_03_solution.py"
    "slide_04_producer.py"
    "slide_05_topics.py"
    "slide_06_partitions.py"
    "slide_07_consumers.py"
    "slide_08_consumer_groups.py"
    "slide_09_complete_flow.py"
    "slide_10_benefits.py"
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
echo "   ../../../output/carousels/kafka-basics-v1/"
echo ""
echo "📱 Ready for Instagram upload!"
echo ""
echo "💡 Tip: Upload slides in order (01 → 10) for best storytelling"
echo "=================================================="

