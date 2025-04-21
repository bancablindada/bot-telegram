import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "banca_blindada_temp_key")

# Datos de ejemplo para pronósticos
pronosticos_recientes = [
    {
        "deporte": "Fútbol",
        "partido": "Real Madrid vs Barcelona",
        "prediccion": "Victoria local",
        "resultado": "Acertado",
        "fecha": "20/04/2025"
    },
    {
        "deporte": "Tenis",
        "partido": "Alcaraz vs Djokovic",
        "prediccion": "Victoria Alcaraz",
        "resultado": "Acertado",
        "fecha": "19/04/2025"
    },
    {
        "deporte": "Baloncesto",
        "partido": "Lakers vs Celtics",
        "prediccion": "Handicap +5.5 Celtics",
        "resultado": "Fallado",
        "fecha": "18/04/2025"
    },
    {
        "deporte": "Fútbol",
        "partido": "Manchester City vs Liverpool",
        "prediccion": "Más de 2.5 goles",
        "resultado": "Acertado",
        "fecha": "17/04/2025"
    }
]

@app.route('/')
def index():
    return render_template('index.html', pronosticos=pronosticos_recientes[:3])

@app.route('/pronosticos')
def pronosticos():
    return render_template('pronosticos.html', pronosticos=pronosticos_recientes)

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/bot')
def bot_info():
    bot_name = "BancaBlindadaBot" 
    return render_template('bot.html', bot_name=bot_name)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Asegurarse de que exista la carpeta de plantillas
import os
if not os.path.exists('templates'):
    os.makedirs('templates')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)