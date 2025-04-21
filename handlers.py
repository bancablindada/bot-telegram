import logging
from telegram import Update
from telegram.ext import CallbackContext

logger = logging.getLogger(__name__)

def start_command(update: Update, context: CallbackContext):
    """
    Handler for the /start command.
    Sends a welcome message introducing the Banca Blindada service.
    """
    try:
        user = update.effective_user
        logger.info(f"User {user.id} started the bot")
        
        welcome_message = (
            f"🎯 Bienvenido a *Banca Blindada*, {user.first_name}!\n\n"
            "Aquí vas a recibir los mejores pronósticos deportivos del mercado.\n"
            "Pronto podrás acceder a nuestro servicio premium con pronósticos exclusivos.\n\n"
            "🔒 El sistema de pago estará disponible en breve. ¡Permanece atento!"
        )
        
        update.message.reply_text(
            welcome_message, 
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        update.message.reply_text(
            "Lo siento, ha ocurrido un error. Por favor, intenta nuevamente más tarde."
        )

def error_handler(update: object, context: CallbackContext) -> None:
    """
    Handler for bot errors.
    Logs errors and informs users about problems if possible.
    """
    logger.error(f"Exception while handling an update: {context.error}")
    
    if update and isinstance(update, Update) and update.effective_message:
        error_message = "Lo siento, ha ocurrido un error en el procesamiento de tu solicitud."
        update.effective_message.reply_text(error_message)
