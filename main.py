
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Configurar dispatcher
dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("¡Hola! Soy tu bot.")

dispatcher.add_handler(CommandHandler("start", start))

# Ruta principal, escucha solo POST
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# Esto es opcional, para cuando accedes con GET desde el navegador
@app.route("/", methods=["GET"])
def index():
    return "Bot activo - Banca Blindada 🔒"



   
    
