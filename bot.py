import logging
from telegram.ext import Updater, CommandHandler

from config import TELEGRAM_TOKEN
from handlers import start_command, error_handler

logger = logging.getLogger(__name__)

def create_bot():
    """
    Creates and configures the Telegram bot application.
    
    Returns:
        The configured bot application ready to run
    """
    try:
        # Initialize the bot with the token from environment variables
        updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # Register command handlers
        dispatcher.add_handler(CommandHandler("start", start_command))
        
        # Register error handler
        dispatcher.add_error_handler(error_handler)
        
        return updater
    except Exception as e:
        logger.error(f"Failed to create bot: {e}")
        raise
