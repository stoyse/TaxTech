"""
Configuration file for Doc2Flow
Manage API providers and model settings here
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# AI PROVIDER CONFIGURATION
# =============================================================================

# Choose your AI provider: "openai", "anthropic", or "gemini"
AI_PROVIDER = "openai"

# =============================================================================
# MODEL SETTINGS BY PROVIDER
# =============================================================================

# OpenAI Configuration
OPENAI_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "model": "gpt-4o",  # GPT-4o - fast and reliable
    "temperature": 0.7,  # Controls randomness (0-2), lower is more focused
    "max_completion_tokens": 8192,  # Maximum tokens for completion
}

# Anthropic Configuration
ANTHROPIC_CONFIG = {
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "model": "claude-3-5-sonnet-20241022",  # Options: claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307
    "temperature": 0.7,
    "max_tokens": 8192,  # Anthropic uses max_tokens
}

# Google Gemini Configuration
GEMINI_CONFIG = {
    "api_key": os.getenv("GEMINI_API_KEY"),
    "model": "gemini-1.5-pro",  # Options: gemini-1.5-pro, gemini-1.5-flash, gemini-pro
    "temperature": 0.7,
    "max_output_tokens": 8192,  # Gemini uses max_output_tokens
}

# =============================================================================
# ACTIVE CONFIGURATION (Based on AI_PROVIDER selection)
# =============================================================================

def get_active_config():
    """
    Returns the active configuration based on AI_PROVIDER setting
    """
    if AI_PROVIDER == "openai":
        return OPENAI_CONFIG
    elif AI_PROVIDER == "anthropic":
        return ANTHROPIC_CONFIG
    elif AI_PROVIDER == "gemini":
        return GEMINI_CONFIG
    else:
        raise ValueError(f"Invalid AI_PROVIDER: {AI_PROVIDER}. Must be 'openai', 'anthropic', or 'gemini'")

# =============================================================================
# SYSTEM PROMPT
# =============================================================================

def load_system_prompt():
    """
    Load the system prompt from system_prompt.md file
    """
    try:
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """You are an expert AI assistant specialized in analyzing documents and generating BPMN workflows."""

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================

APP_CONFIG = {
    "title": "Doc2Flow",
    "icon": "📄",
    "layout": "wide",
    "supported_file_types": ['pdf', 'docx', 'txt', 'md'],
    "max_upload_size_mb": 10,
}

# =============================================================================
# USAGE EXAMPLE
# =============================================================================

if __name__ == "__main__":
    print(f"Active AI Provider: {AI_PROVIDER}")
    print(f"Active Configuration: {get_active_config()}")
    print(f"\nSystem Prompt Preview:")
    print(load_system_prompt()[:200] + "...")
