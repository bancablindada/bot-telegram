# Punto de entrada principal para la aplicación web
# El bot se ejecuta en bot_runner.py separadamente

from app import app

# Este archivo es ejecutado por gunicorn para iniciar la aplicación web
# La aplicación web Flask sirve páginas HTML para los usuarios
# El bot Telegram se ejecuta en un proceso separado para evitar conflictos