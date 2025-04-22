import logging
import os
import sys
from telegram.ext import Updater, CommandHandler
from bot import create_bot
from keep_alive import keep_alive

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Import the Flask app from app.py (not used directly here, but imported for completeness)
from app import app

if __name__ == '__main__':
    # Mantener el bot activo con un servidor web
    keep_alive()
    
    # Create and run the bot
    updater = create_bot()
    print("Banca Blindada Bot is running...")
    
    # Configuración para evitar instancias duplicadas
    updater.start_polling(drop_pending_updates=True)
    
    # Run the bot until the user presses Ctrl-C
    updater.idle()