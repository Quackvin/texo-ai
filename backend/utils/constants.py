# TEXO UDPATES:
# - reduced to only 1 tier
MODEL_ACCESS_TIERS = {
    "basic": [
        "anthropic/claude-3-7-sonnet-latest"
        "openrouter/deepseek/deepseek-chat",
        "openrouter/qwen/qwen3-235b-a22b",
        "openrouter/google/gemini-2.5-flash-preview",
    ],
    "free": []
}

MODEL_NAME_ALIASES = {
    # Short names to full names
    "sonnet-3.7": "anthropic/claude-3-7-sonnet-latest", 
    "gpt-4o": "openai/gpt-4o",
    "deepseek": "openrouter/deepseek/deepseek-chat",
    "qwen3": "openrouter/qwen/qwen3-235b-a22b",  # Commented out in constants.py
    # "sonnet-3.7": "openrouter/anthropic/claude-3.7-sonnet",
    # "gpt-4.1": "openai/gpt-4.1-2025-04-14",  # Commented out in constants.py
    # "gpt-4-turbo": "openai/gpt-4-turbo",  # Commented out in constants.py
    # "gpt-4": "openai/gpt-4",  # Commented out in constants.py
    # "gemini-flash-2.5": "openrouter/google/gemini-2.5-flash-preview",  # Commented out in constants.py
    # "grok-3": "xai/grok-3-fast-latest",  # Commented out in constants.py
    # "deepseek-r1": "openrouter/deepseek/deepseek-r1",
    # "grok-3-mini": "xai/grok-3-mini-fast-beta",  # Commented out in constants.py

    # Also include full names as keys to ensure they map to themselves
    "anthropic/claude-3-7-sonnet-latest": "anthropic/claude-3-7-sonnet-latest",
    "openai/gpt-4o": "openai/gpt-4o",
    "deepseek/deepseek-chat": "openrouter/deepseek/deepseek-chat",
    "qwen/qwen3-235b-a22b": "openrouter/qwen/qwen3-235b-a22b",
    # "openai/gpt-4.1-2025-04-14": "openai/gpt-4.1-2025-04-14",  # Commented out in constants.py
    # "openai/gpt-4-turbo": "openai/gpt-4-turbo",  # Commented out in constants.py
    # "openai/gpt-4": "openai/gpt-4",  # Commented out in constants.py
    # "openrouter/google/gemini-2.5-flash-preview": "openrouter/google/gemini-2.5-flash-preview",  # Commented out in constants.py
    # "xai/grok-3-fast-latest": "xai/grok-3-fast-latest",  # Commented out in constants.py
    # "deepseek/deepseek-r1": "openrouter/deepseek/deepseek-r1",
    # "xai/grok-3-mini-fast-beta": "xai/grok-3-mini-fast-beta",  # Commented out in constants.py
}

