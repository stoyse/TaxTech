"""
Configuration file for Doc2Flow Cleaner Service
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# CLEANER AI PROVIDER CONFIGURATION
# =============================================================================

# Cleaner model is assumed to be OpenAI for this service
CLEANER_AI_PROVIDER = "openai"

# =============================================================================
# CLEANER MODEL SETTINGS
# =============================================================================

# Configuration for the BPMN XML cleaning model
CLEANER_OPENAI_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "model": "gpt-4o",  # Use a fast and reliable model for cleaning
    "temperature": 0.0,  # No creativity needed, just cleaning
    "max_completion_tokens": 8192,  # Generous limit for returning full XML
}

# =============================================================================
# ACTIVE CLEANER CONFIGURATION
# =============================================================================

def get_cleaner_config():
    """
    Returns the active cleaner configuration.
    """
    return CLEANER_OPENAI_CONFIG

# =============================================================================
# CLEANER SYSTEM PROMPT
# =============================================================================

def load_cleaner_system_prompt():
    """
    Load the cleaner system prompt from cleaner_system_prompt.md file
    """
    try:
        with open("cleaner_system_prompt.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """You are an expert AI assistant specialized in refining and cleaning BPMN 2.0 XML for optimal visual presentation."""

