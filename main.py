from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# === CONFIGURACIÓN ===
TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"  # 🔐 Tu token
WEBHOOK_URL = "https://bot-telegram-nk7b.onrender.com/"   # Tu URL de Render

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

# === HANDLER DEL COMANDO /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot, y estoy activo 24/7 🔥")

bot_app.add_handler(CommandHandler("start", start))

# === FLASK: RUTA PARA RECIBIR MENSAJES DE TELEGRAM ===
@app.route("/", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "ok"

# === RUTA DE PRUEBA (GET) ===
@app.route("/", methods=["GET"])
def index():
    return "Bot activo y listo para la acción. 🚀"

# === SOLO PARA LOCAL (Render usa Gunicorn) ===
if __name__ == "__main__":
    app.run(port=5000)






   
    
