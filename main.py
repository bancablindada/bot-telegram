import logging
from telegram.ext import Updater, CommandHandler
from bot import create_bot
from keep_alive import keep_alive

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Import the Flask app from app.py
from app import app

if __name__ == '__main__':
    # Mantener el bot activo con un servidor web
    keep_alive()
    
    # Create and run the bot
    updater = create_bot()
    print("Banca Blindada Bot is running...")
    updater.start_polling()
    
    # Run the bot until the user presses Ctrl-C
    updater.idle()