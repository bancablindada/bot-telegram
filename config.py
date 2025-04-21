import os
import logging

logger = logging.getLogger(__name__)

# Get Telegram bot token from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Check if token is available
if not TELEGRAM_TOKEN:
    logger.warning(
        "Telegram bot token not found in environment variables. "
        "Please set the TELEGRAM_TOKEN environment variable."
    )
    # For development, you can set a default token, but it's not recommended for production
    # This is just to prevent immediate crash on startup without a token
    TELEGRAM_TOKEN = "MISSING_TOKEN"
