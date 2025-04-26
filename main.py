
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import requests
import os

# Obtener claves del entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # ✅ Nombre correcto según Render

# Inicializar Flask y Telegram
app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# Variables de contexto
BOT_CONTEXT = """
Eres el asistente virtual de Banca Blindada, un grupo de analistas deportivos con 6 años de experiencia en el sector.
Responde de forma clara, profesional y amigable al mensaje del usuario.
"""
BOT_PRESENTATION = "Hola, soy el asistente virtual de Banca Blindada, ¿en qué puedo ayudarte?\n"
BANCA_BLINDADA_INFO = (
    "Banca Blindada es un grupo de analistas deportivos con más de 6 años en el sector de pronósticos deportivos. "
    "Ofrecen asistencia gratuita para nuevos clientes así como una versión por suscripción para afiliados profesionales."
)

# Guardamos para saber si ya saludamos a cada chat
chats_saludados = set()

# Función para hablar con OpenRouter
def get_openrouter_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print("Error al obtener respuesta de OpenRouter:", e)
        print("Respuesta completa:", response.text)
        return "Error al obtener respuesta de OpenRouter."

# Función para detectar si el usuario pregunta sobre Banca Blindada
def pregunta_sobre_banca_blindada(texto):
    texto = texto.lower()
    palabras_clave = [
        "quién eres", "para quién trabajas", "qué es banca blindada", 
        "quién es banca blindada", "qué ofrecen", "a qué se dedican", 
        "qué hacen en banca blindada"
    ]
    return any(palabra in texto for palabra in palabras_clave)

# Función manejadora
def handle_message(update: Update, context):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    # Verificar si es una pregunta sobre Banca Blindada
    if pregunta_sobre_banca_blindada(user_message):
        reply = BANCA_BLINDADA_INFO
    else:
        prompt = f"{BOT_CONTEXT}\nUsuario: {user_message}\nAsistente:"
        response_text = get_openrouter_response(prompt)

        # Revisar si ya saludamos a este chat
        if chat_id not in chats_saludados:
            reply = f"{BOT_PRESENTATION}{response_text}"
            chats_saludados.add(chat_id)
        else:
            reply = response_text

    context.bot.send_message(chat_id=chat_id, text=reply)

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

   
   
       

   

    







   
    
