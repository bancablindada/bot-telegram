
from flask import Flask
import threading
import logging
import time
import os
import signal

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask('')
server_thread = None
monitor_thread = None

@app.route('/')
def home():
    logger.info("Ping recibido - Bot activo")
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
        os._exit(1)

def keep_alive():
    global server_thread, monitor_thread
    
    # Configurar el manejo de señales
    signal.signal(signal.SIGTERM, lambda signo, frame: None)
    signal.signal(signal.SIGINT, lambda signo, frame: None)
    
    # Iniciar servidor web
    server_thread = threading.Thread(target=run)
    server_thread.daemon = False
    server_thread.start()
    logger.info("Servidor web iniciado en http://0.0.0.0:8080")
    
    def monitor():
        while True:
            try:
                if not server_thread.is_alive():
                    logger.warning("Servidor web caído, reiniciando...")
                    new_thread = threading.Thread(target=run)
                    new_thread.daemon = False
                    new_thread.start()
                    global server_thread
                    server_thread = new_thread
            except Exception as e:
                logger.error(f"Error en monitor: {e}")
            time.sleep(30)
    
    # Iniciar monitor
    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.daemon = False
    monitor_thread.start()
