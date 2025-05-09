import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TELEGRAM_TOKEN
from handlers import start_command, help_command, pronosticos_command, message_handler, error_handler

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
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("pronosticos", pronosticos_command))
        
        # Register message handler for text messages
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
        
        # Register error handler
        dispatcher.add_error_handler(error_handler)
        
        return updater
    except Exception as e:
        logger.error(f"Failed to create bot: {e}")
        raise
