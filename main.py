from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
WEBHOOK_URL = "https://bot-telegram-nk7b.onrender.com/"  # Asegúrate que sea la URL correcta de tu proyecto en Render

app = Flask(__name__)

# Creamos el Application de telegram
application = Application.builder().token(TOKEN).build()

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot.")

# Añadimos el handler
application.add_handler(CommandHandler("start", start))

# Webhook endpoint (para Telegram)
@app.route("/", methods=["POST"])
async def telegram_webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok", 200

# Página informativa si entras por GET (opcional)
@app.route("/", methods=["GET"])
def index():
    return "Bot activo - Banca Blindada 🔒"

# Establecer webhook cuando arranca la app
@app.before_first_request
def set_webhook():
    asyncio.run(application.bot.set_webhook(WEBHOOK_URL))







   
    
