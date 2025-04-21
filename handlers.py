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

def message_handler(update: Update, context: CallbackContext):
    """
    Handler for text messages.
    Responds based on natural language understanding.
    """
    try:
        texto = update.message.text.lower()

        if any(palabra in texto for palabra in ["hola", "buenas", "hey", "qué tal", "saludos"]):
            update.message.reply_text("¡Hola crack! 👋 Bienvenido a *Banca Blindada*, el lugar donde se ganan apuestas de verdad. ¿En qué te puedo ayudar?", parse_mode='Markdown')
        
        elif any(palabra in texto for palabra in ["precio", "pagar", "vale", "coste", "cuánto", "tarifa", "cuesta"]):
            update.message.reply_text(
                "💸 Los pronósticos de pago se mandan por el grupo principal.\n"
                "Ahí mismo se comparte el enlace para que puedas realizar el pago y acceder al contenido exclusivo.\n"
                "Estate atento en el grupo para no perderte nada."
            )
        
        else:
            update.message.reply_text("🤖 No entendí muy bien lo que dijiste. Si necesitas ayuda sobre pagos o pronósticos, pregúntame sin miedo 😉")
    
    except Exception as e:
        logger.error(f"Error in message handler: {e}")
        update.message.reply_text(
            "Lo siento, ha ocurrido un error procesando tu mensaje. Por favor, intenta nuevamente más tarde."
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
