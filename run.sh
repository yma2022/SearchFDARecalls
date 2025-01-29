#!/usr/bin/env bash

# Exit immediately if any command exits with a non-zero status
set -e

# Install required packages
pip install -r requirements.txt

# Run the main Python script
python main.py
sh