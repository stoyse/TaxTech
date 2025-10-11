#!/bin/zsh

# Start the Doc2Flow application
source venv/bin/activate
# Ensure the environment variables are loaded
export $(grep -v '^#' .env | xargs)

# Run the Python script
streamlit run streamlite-test1.py
