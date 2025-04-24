from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN", "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE")

# Crear Flask app
app = Flask(__name__)

# Crear Application de telegram
application = Application.builder().token(TOKEN).build()

# Handler de comandos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot.")

# Añadir handler
application.add_handler(CommandHandler("start", start))

# Webhook Flask route
@app.route("/", methods=["POST"])
def webhook():
    # Recibir update y procesar con Application
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok", 200

# Ruta GET opcional
@app.route("/", methods=["GET"])
def index():
    return "Bot activo - Banca Blindada 🔒"








   
    
