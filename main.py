import logging
from telegram.ext import Updater, CommandHandler
from bot import create_bot

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create Flask app
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Banca Blindada Bot está funcionando en segundo plano."

if __name__ == '__main__':
    # Create and run the bot
    updater = create_bot()
    print("Banca Blindada Bot is running...")
    updater.start_polling()
    
    # Run the bot until the user presses Ctrl-C
    updater.idle()