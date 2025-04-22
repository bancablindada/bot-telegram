
from flask import Flask
import threading
import logging
import time

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask('')

@app.route('/')
def home():
    logger.info("Ping recibido - Servidor activo")
    return "Bot activo"

def run():
    retries = 5
    while retries > 0:
        try:
            app.run(host='0.0.0.0', port=8080, debug=False)
            break
        except Exception as e:
            logger.error(f"Error iniciando servidor web (intentos restantes: {retries}): {e}")
            retries -= 1
            time.sleep(2)
    
    if retries == 0:
        logger.critical("No se pudo iniciar el servidor web después de 5 intentos")

def keep_alive():
    server = threading.Thread(target=run)
    server.daemon = True
    server.start()
    logger.info("Servidor web iniciado en http://0.0.0.0:8080")
