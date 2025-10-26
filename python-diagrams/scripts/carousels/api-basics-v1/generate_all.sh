#!/bin/bash

# Generate all Instagram carousel slides for API Basics v1
# Output: PNG images optimized for Instagram (1080x1080)

echo "🎨 Generating Instagram Carousel: API Basics v1"
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
    "slide_01_overview.py"
    "slide_02_problem.py"
    "slide_03_solution.py"
    "slide_04_what_is_api.py"
    "slide_05_request_response.py"
    "slide_06_http_methods.py"
    "slide_07_rest_api.py"
    "slide_08_json_format.py"
    "slide_09_security.py"
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
echo "   ../../../output/carousels/api-basics-v1/"
echo ""
echo "📱 Ready for Instagram upload!"
echo ""
echo "💡 API v1 Features:"
echo "   ✨ Transparent background"
echo "   • Clear problem → solution flow"
echo "   • Request/response visualization"
echo "   • HTTP methods (CRUD)"
echo "   • REST API concepts"
echo "   • JSON format examples"
echo "   • Security & authentication"
echo "=================================================="

