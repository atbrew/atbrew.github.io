#!/bin/bash
# Helper script to run Jekyll locally with proper configuration

cd "$(dirname "$0")"

echo "🔧 Configuring for local development..."

# Create a temporary config override
cat > _config_local.yml << 'EOF'
# Local development overrides
theme: bay_jekyll_theme
EOF

echo "🚀 Starting Jekyll server..."
echo "📍 http://localhost:4000"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Run Jekyll with both configs (local overrides production)
bundle exec jekyll serve --config _config.yml,_config_local.yml

# Cleanup
rm -f _config_local.yml
