"""
TEXO UDPATES:
- reduced to only 1 tier
- moved model_access_tiers to this file
- moved subscription_tiers to this file
"""
from utils.config import config

# Get subscription tiers IDs from config and apply limits
SUBSCRIPTION_TIERS = {
    config.STRIPE_SPARK_TIER_ID: {'name': 'Spark', 'minutes': 120},
    config.STRIPE_BOOST_TIER_ID: {'name': 'Boost', 'minutes': 360},
    config.STRIPE_ASCEND_TIER_ID: {'name': 'Ascend', 'minutes': 720},
    config.STRIPE_PRO_TIER_ID: {'name': 'Pro', 'minutes': 1500},
    config.STRIPE_ELITE_TIER_ID: {'name': 'Elite', 'minutes': 3000},
    config.STRIPE_ULTIMATE_TIER_ID: {'name': 'Ultimate', 'minutes': 7500},
    config.STRIPE_ENTERPRISE_TIER_ID: {'name': 'Enterprise', 'minutes': 12000},
}

# THIS DETERMINES IS THE USER WILL GET THE FORBIDDEN ERROR MESSAGE
ALL_MODELS = [
    "openrouter/deepseek/deepseek-chat",
    "openai/gpt-4o",
    "openrouter/google/gemini-2.5-flash-preview-05-20",
    "bedrock/claude-3-7-sonnet-latest",
    "anthropic/claude-sonnet-4-20250514",
    "openrouter/qwen/qwen3-235b-a22b",
]

MODEL_ACCESS_TIERS = {
    "Spark": ALL_MODELS,
    "Boost": ALL_MODELS,
    "Ascend": ALL_MODELS,
    "Pro": ALL_MODELS,
    "Elite": ALL_MODELS,
    "Ultimate": ALL_MODELS,
    "Enterprise": ALL_MODELS,
}
# THIS IS WHAT IS SHOWN IN THE FRONT END DROPDOWN
MODEL_NAME_ALIASES = {
    # Short names to full names
    "sonnet-3.7": "bedrock/claude-3-7-sonnet-latest",
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
