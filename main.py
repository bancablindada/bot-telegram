
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
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

async def main():
    try:
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        # Registrar comandos y manejadores
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("pronosticos", pronosticos_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
        application.add_error_handler(error_handler)

        # Iniciar Flask en un hilo separado
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        print("Banca Blindada Bot is running...")
        await application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


   
    
