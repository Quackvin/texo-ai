"""
TEXO UDPATES:
- reduced to only 1 tier
- moved model_access_tiers to this file
- moved subscription_tiers to this file
"""
from utils.config import config

# Get subscription tiers IDs from config and apply limits
SUBSCRIPTION_TIERS = {
    config.STRIPE_FREE_TIER_ID: {'name': 'free', 'minutes': 0},
    config.STRIPE_BASIC_TIER_ID: {'name': 'basic', 'minutes': 9999999}
}

MODEL_ACCESS_TIERS = {
    "basic": [
        "openrouter/deepseek/deepseek-chat",
        # "xai/grok-3-mini-fast-beta",
        "openai/gpt-4o",
        # "openai/gpt-4-turbo",
        # "xai/grok-3-fast-latest",
        "openrouter/google/gemini-2.5-flash-preview-05-20",  # Added
        # "openai/gpt-4",
        "anthropic/claude-3-7-sonnet-latest",
        "anthropic/claude-sonnet-4-20250514",
        # "openai/gpt-4.1-2025-04-14",
        # "openrouter/deepseek/deepseek-r1",
        "openrouter/qwen/qwen3-235b-a22b",
    ],
    "free": []
}

MODEL_NAME_ALIASES = {
    # Short names to full names
    "sonnet-3.7": "anthropic/claude-3-7-sonnet-latest",
    "sonnet-3.5": "anthropic/claude-3-5-sonnet-latest",
    "haiku-3.5": "anthropic/claude-3-5-haiku-latest",
    "claude-sonnet-4": "anthropic/claude-sonnet-4-20250514",
    # "gpt-4.1": "openai/gpt-4.1-2025-04-14",  # Commented out in constants.py
    "gpt-4o": "openai/gpt-4o",
    "gpt-4.1": "openai/gpt-4.1",
    "gpt-4.1-mini": "gpt-4.1-mini",
    # "gpt-4-turbo": "openai/gpt-4-turbo",  # Commented out in constants.py
    # "gpt-4": "openai/gpt-4",  # Commented out in constants.py
    # "gemini-flash-2.5": "openrouter/google/gemini-2.5-flash-preview",  # Commented out in constants.py
    # "grok-3": "xai/grok-3-fast-latest",  # Commented out in constants.py
    "deepseek": "openrouter/deepseek/deepseek-chat",
    # "deepseek-r1": "openrouter/deepseek/deepseek-r1",
    # "grok-3-mini": "xai/grok-3-mini-fast-beta",  # Commented out in constants.py
    "qwen3": "openrouter/qwen/qwen3-235b-a22b",  # Commented out in constants.py
    "gemini-flash-2.5": "openrouter/google/gemini-2.5-flash-preview-05-20",
    "gemini-2.5-flash:thinking":"openrouter/google/gemini-2.5-flash-preview-05-20:thinking",
    
    # "google/gemini-2.5-flash-preview":"openrouter/google/gemini-2.5-flash-preview",
    # "google/gemini-2.5-flash-preview:thinking":"openrouter/google/gemini-2.5-flash-preview:thinking",
    "google/gemini-2.5-pro-preview":"openrouter/google/gemini-2.5-pro-preview",
    "deepseek/deepseek-chat-v3-0324":"openrouter/deepseek/deepseek-chat-v3-0324",
}

