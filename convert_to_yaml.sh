#!/bin/bash

# Python script file
PYTHON_SCRIPT="beanstalk.py"

# Output YAML file
YAML_FILE="elastic_beanstalk_template.yaml"

# Convert Python to YAML using cdk synth
cdk synth -o . > "$YAML_FILE" || { echo "CDK synthesis failed"; exit 1; }

# Check if the YAML file exists
if [ ! -f "$YAML_FILE" ]; then
    echo "Error: YAML file not found"
    exit 1
fi

# Clean up generated YAML file to remove CDK-specific comments
sed -i '' '/^#.*Generated.*By.*CDK.*/d' "$YAML_FILE" || { echo "Sed command failed"; exit 1; }

echo "Conversion complete. YAML template saved to $YAML_FILE"
