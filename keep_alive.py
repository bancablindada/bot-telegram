
from flask import Flask
import threading
import logging
import os
import psutil
import time

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask('')

def is_bot_running():
    """Verifica si el proceso del bot está activo"""
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if 'python' in proc.info['name'] and 'bot_runner.py' in ' '.join(proc.info['cmdline'] or []):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

@app.route('/')
def home():
    if is_bot_running():
        logger.info("Ping recibido - Bot activo y funcionando")
        return "Bot activo y funcionando"
    else:
        logger.warning("Ping recibido pero el bot no está ejecutándose")
        return "Bot inactivo", 500

def run():
    try:
        app.run(host='0.0.0.0', port=8080, debug=False)
    except Exception as e:
        logger.error(f"Error iniciando servidor web: {e}")
        
def keep_alive():
    server = threading.Thread(target=run)
    server.daemon = True
    server.start()
    logger.info("Servidor web iniciado en http://0.0.0.0:8080")
