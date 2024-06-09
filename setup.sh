#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
pip install python-dotenv

# Install dependencies
pip install -r requirements.txt

echo "Setup complete. Virtual environment created and dependencies installed."
