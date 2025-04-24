from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import requests
import os

# Tus claves (NO compartas esto con nadie más)
TELEGRAM_TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
OPENROUTER_API_KEY = "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"

# Inicializar Flask y Telegram
app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# Función para hablar con OpenRouter
def get_openrouter_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openrouter/cinematika:extended",  # Puedes cambiar de modelo si lo deseas
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error al conectar con OpenRouter: {str(e)}"

# Manejador de mensajes normales (texto)
def handle_message(update: Update, context):
    user_text = update.message.text
    reply_text = get_openrouter_response(user_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

# Registrar el manejador
dispatcher.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_message))

# Webhook para recibir updates
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot online", 200






   
    
