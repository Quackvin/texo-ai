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
        # "anthropic/claude-3-7-sonnet-latest",
        "openrouter/anthropic/claude-sonnet-4",
        "openrouter/anthropic/claude-3.7-sonnet",
        "openrouter/anthropic/claude-3.7-sonnet:thinking",
        "openrouter/deepseek/deepseek-chat",
        # "openai/gpt-4o",
        "openrouter/openai/gpt-4o", #openai/gpt-4o-2024-11-20
        "openrouter/qwen/qwen3-235b-a22b",
        "openrouter/google/gemini-2.5-flash-preview", #google/gemini-2.5-flash-preview-05-20
        "openrouter/google/gemini-2.5-flash-preview:thinking", #google/gemini-2.5-flash-preview-05-20:thinking
        "openrouter/google/gemini-2.5-pro-preview", #google/gemini-2.5-pro-preview
    ],
    "free": []
}

MODEL_NAME_ALIASES = {
    # Short names to full names
    "sonnet-4": "openrouter/anthropic/claude-sonnet-4",
    "sonnet-3.7": "openrouter/anthropic/claude-3-7-sonnet", 
    "sonnet-3.7:thinking": "openrouter/anthropic/claude-3.7-sonnet:thinking",
    "deepseek": "openrouter/deepseek/deepseek-chat",
    "gpt-4o": "openai/gpt-4o",
    "qwen3": "openrouter/qwen/qwen3-235b-a22b",  # Commented out in constants.py
    "gemini-flash-2.5": "openrouter/google/gemini-2.5-flash-preview",
    "gemini-flash-2.5:thinking": "openrouter/google/gemini-2.5-flash-preview:thinking",
    "gemini-flash-2.5-pro": "openrouter/google/gemini-2.5-pro-preview",
    # "sonnet-3.7": "openrouter/anthropic/claude-3.7-sonnet",
    # "gpt-4.1": "openai/gpt-4.1-2025-04-14",  # Commented out in constants.py
    # "gpt-4-turbo": "openai/gpt-4-turbo",  # Commented out in constants.py
    # "gpt-4": "openai/gpt-4",  # Commented out in constants.py
    # "grok-3": "xai/grok-3-fast-latest",  # Commented out in constants.py
    # "deepseek-r1": "openrouter/deepseek/deepseek-r1",
    # "grok-3-mini": "xai/grok-3-mini-fast-beta",  # Commented out in constants.py

    # Also include full names as keys to ensure they map to themselves
    "openrouter/anthropic/claude-sonnet-4": "openrouter/anthropic/claude-sonnet-4",
    # "anthropic/claude-3-7-sonnet-latest": "anthropic/claude-3-7-sonnet-latest",
    "openrouter/anthropic/claude-3-7-sonnet": "openrouter/anthropic/claude-3-7-sonnet", 
    "openrouter/anthropic/claude-3.7-sonnet:thinking": "openrouter/anthropic/claude-3.7-sonnet:thinking",
    "openrouter/deepseek/deepseek-chat": "openrouter/deepseek/deepseek-chat",
    "openai/gpt-4o": "openai/gpt-4o",
    "openrouter/qwen/qwen3-235b-a22b": "openrouter/qwen/qwen3-235b-a22b",
    "openrouter/google/gemini-2.5-flash-preview": "openrouter/google/gemini-2.5-flash-preview",
    "openrouter/google/gemini-2.5-flash-preview:thinking": "openrouter/google/gemini-2.5-flash-preview:thinking",
    "openrouter/google/gemini-2.5-pro-preview": "openrouter/google/gemini-2.5-pro-preview",
    # "openai/gpt-4.1-2025-04-14": "openai/gpt-4.1-2025-04-14",  # Commented out in constants.py
    # "openai/gpt-4-turbo": "openai/gpt-4-turbo",  # Commented out in constants.py
    # "openai/gpt-4": "openai/gpt-4",  # Commented out in constants.py
    # "xai/grok-3-fast-latest": "xai/grok-3-fast-latest",  # Commented out in constants.py
    # "deepseek/deepseek-r1": "openrouter/deepseek/deepseek-r1",
    # "xai/grok-3-mini-fast-beta": "xai/grok-3-mini-fast-beta",  # Commented out in constants.py
}

