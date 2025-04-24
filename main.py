from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
import asyncio
import os

# Configura el token y la URL del webhook
TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
WEBHOOK_URL = "https://bot-telegram-nk7b.onrender.com/"

# Crea la aplicación de Telegram
application = Application.builder().token(TOKEN).build()

# Función para el comando /start
async def start(update: Update, context):
    await update.message.reply_text("¡Hola! Soy tu bot.")

# Agrega el handler a la aplicación
application.add_handler(CommandHandler("start", start))

# Crea la app Flask
app = Flask(__name__)

# ✅ Configura el webhook al iniciar el servidor
@app.before_first_request
def set_webhook():
    loop = asyncio.get_event_loop()
    loop.create_task(application.bot.set_webhook(WEBHOOK_URL))

# Ruta para manejar actualizaciones de Telegram (solo POST)
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok", 200

# Ruta simple para comprobar si el bot está activo
@app.route("/", methods=["GET"])
def index():
    return "Bot activo - Banca Blindada 🔒"









   
    
