import logging
import os
import sys
from telegram.ext import Updater

from bot import create_bot
from keep_alive import keep_alive

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    try:
        # Mantener el bot activo con un servidor web
        keep_alive()
        
        # Create and run the bot
        updater = create_bot()
        print("Banca Blindada Bot is running...")
        
        # Configuración para evitar instancias duplicadas
        updater.start_polling(drop_pending_updates=True)
        
        # Run the bot until the user presses Ctrl-C
        updater.idle()
    except Exception as e:
        logging.error(f"Error crítico en el bot: {e}")
        # Esperar antes de reintentar
        time.sleep(10)
        # El proceso se reiniciará automáticamente por Replit