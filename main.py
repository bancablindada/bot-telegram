from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
import asyncio
import os

# === CONFIGURACIÓN ===
TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
WEBHOOK_URL = "https://bot-telegram-nk7b.onrender.com/"  # Asegúrate que esta sea tu URL exacta de Render

# === INICIALIZACIÓN FLASK Y TELEGRAM ===
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# === HANDLERS DE TELEGRAM ===
async def start(update: Update, context):
    await update.message.reply_text("¡Hola! Soy tu bot.")

application.add_handler(CommandHandler("start", start))

# === CONFIGURAR EL WEBHOOK JUSTO AL ARRANCAR ===
@app.before_request
def set_webhook_once():
    if not application.bot_data.get("webhook_set"):
        asyncio.run(application.bot.set_webhook(WEBHOOK_URL))
        application.bot_data["webhook_set"] = True

# === RUTA PRINCIPAL PARA TELEGRAM (POST) ===
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok", 200

# === RUTA GET PARA COMPROBAR ===
@app.route("/", methods=["GET"])
def index():
    return "Bot activo - Banca Blindada 🔒"









   
    
