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

        # Definir categorías de patrones
        saludos = ["hola", "buenas", "hey", "qué tal", "saludos"]
        despedidas = ["gracias", "muchas gracias", "ok gracias", "hasta luego", "nos vemos", "chao", "adiós"]
        preguntas_pago = [
            "precio", "pagar", "vale", "coste", "cuánto cuesta", "tarifa", 
            "cómo pago", "cómo pagar", "quiero pagar", "quiero ver los pronósticos",
            "cómo miro los pronósticos", "cómo puedo pagar", "dime precio", "cómo ver los pagos"
        ]

        # Responder según la categoría
        if any(palabra in texto for palabra in saludos):
            update.message.reply_text("¡Qué tal, crack! 👋 Bienvenido a *Banca Blindada*. ¿En qué puedo ayudarte?", parse_mode='Markdown')
        
        elif any(palabra in texto for palabra in despedidas):
            update.message.reply_text("¡De nada! Aquí me tienes para lo que necesites. Un saludo fuerte 🙌")
        
        elif any(palabra in texto for palabra in preguntas_pago):
            update.message.reply_text(
                "💸 Los pronósticos premium se envían en nuestro grupo principal.\n"
                "Ahí mismo se publica el enlace para realizar el pago cuando hay nuevos tips disponibles.\n"
                "👀 Mantente atento para no perdértelos."
            )
        
        else:
            update.message.reply_text("🤖 No estoy seguro de haber entendido eso. Pero si tienes dudas sobre pagos, pronósticos o cómo funciona todo, ¡aquí estoy para ayudarte!")
    
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
