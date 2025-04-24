from flask import Flask, request
import telegram

# Token de tu bot
TOKEN = "7614413819:AAGyklxdklFiO1zKm8hmjhC3vncrzQJ-AKE"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Respuesta del bot
    bot.sendMessage(chat_id=chat_id, text=f"Hola, recibí tu mensaje: {text}")
    return 'ok'

@app.route('/')
def index():
    return 'Bot funcionando correctamente 🚀'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


   
    
