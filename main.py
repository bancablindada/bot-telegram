from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import requests
import os

# Obtener claves del entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")  # Este es el nombre exacto de Render

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
        "model": "openrouter/cinematika:extended",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "Error al obtener respuesta de OpenRouter."

# Función manejadora
def handle_message(update: Update, context):
    prompt = update.message.text
    reply = get_openrouter_response(prompt)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

# Agregar manejador
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Ruta para recibir mensajes desde Telegram
@app.route('/', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

# Ruta raíz para verificar que el bot funciona
@app.route('/')
def home():
    return "Bot de Telegram funcionando con IA de OpenRouter"

    







   
    
