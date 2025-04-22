
from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import threading
import logging
from handlers import start_command, help_command, pronosticos_command, message_handler, error_handler
from config import TELEGRAM_TOKEN

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configurar Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot activo - Banca Blindada 🔐"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def create_bot():
    try:
        updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # Registrar handlers
        dispatcher.add_handler(CommandHandler("start", start_command))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("pronosticos", pronosticos_command))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
        dispatcher.add_error_handler(error_handler)
        
        return updater
    except Exception as e:
        logger.error(f"Failed to create bot: {e}")
        raise

if __name__ == '__main__':
    # Iniciar servidor web en un thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Crear y ejecutar el bot
    updater = create_bot()
    print("Banca Blindada Bot is running...")
    updater.start_polling(drop_pending_updates=True)
    updater.idle()
