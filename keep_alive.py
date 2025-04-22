
from flask import Flask
import threading
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask('')

@app.route('/')
def home():
    logger.info("Ping recibido en /")
    return "Bot activo"

def run():
    try:
        app.run(host='0.0.0.0', port=8080)
    except Exception as e:
        logger.error(f"Error iniciando servidor web: {e}")
        
def keep_alive():
    server = threading.Thread(target=run)
    server.daemon = True  # El hilo se cerrará cuando el programa principal termine
    server.start()
    logger.info("Servidor web iniciado en http://0.0.0.0:8080")
