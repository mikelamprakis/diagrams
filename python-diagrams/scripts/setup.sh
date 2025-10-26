#!/bin/bash

# Setup script for Python Diagrams
# Run this to install all dependencies

echo "🚀 Setting up Python Diagrams environment..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install Homebrew first."
    exit 1
fi

# Install Graphviz
echo "📦 Installing Graphviz..."
brew install graphviz

# Check if uv is available
if command -v uv &> /dev/null; then
    echo "📦 Installing Python packages with uv..."
    uv pip install diagrams
else
    echo "📦 Installing Python packages with pip..."
    pip install -r requirements.txt
fi

# Verify installation
echo "✅ Verifying installation..."
python3 -c "import diagrams; print('✅ Diagrams installed successfully!')"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Try running:"
echo "  python kafka_simple.py"
echo ""
echo "This will generate 'kafka_simple.png' with your Kafka architecture!"

