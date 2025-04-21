import logging
from telegram import Update
from telegram.ext import CallbackContext
from ai_utils import get_ai_response

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
            # Usar OpenAI para generar una respuesta personalizada
            user = update.effective_user
            logger.info(f"Generando respuesta con IA para usuario {user.id}, mensaje: '{texto}'")
            
            # Añadimos un mensaje de "escribiendo..." mientras se genera la respuesta
            update.message.chat.send_action(action="typing")
            
            # Obtenemos respuesta de OpenAI
            ai_response = get_ai_response(texto)
            update.message.reply_text(ai_response)
    
    except Exception as e:
        logger.error(f"Error in message handler: {e}")
        update.message.reply_text(
            "Lo siento, ha ocurrido un error procesando tu mensaje. Por favor, intenta nuevamente más tarde."
        )

def help_command(update: Update, context: CallbackContext):
    """
    Handler for the /help command.
    Provides information about available commands and bot functionality.
    """
    try:
        help_text = (
            "🏆 *Comandos de Banca Blindada* 🏆\n\n"
            "/start - Iniciar el bot y recibir mensaje de bienvenida\n"
            "/help - Ver esta lista de comandos\n"
            "/pronosticos - Ver los últimos pronósticos disponibles\n\n"
            "También puedes escribirme en lenguaje natural para consultar sobre:\n"
            "• Precios y pagos 💰\n"
            "• Tipos de pronósticos disponibles 🎯\n"
            "• Fechas de próximos eventos 📅\n"
            "• Y cualquier otra duda que tengas sobre nuestro servicio ⚽🏀🎾"
        )
        
        update.message.reply_text(help_text, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error in help command: {e}")
        update.message.reply_text(
            "Lo siento, ha ocurrido un error. Por favor, intenta nuevamente más tarde."
        )

def pronosticos_command(update: Update, context: CallbackContext):
    """
    Handler for the /pronosticos command.
    Shows the latest available predictions.
    """
    try:
        # En una versión futura, estos pronósticos vendrían de una base de datos
        pronosticos_texto = (
            "🔮 *Últimos Pronósticos* 🔮\n\n"
            "*FÚTBOL*\n"
            "• Real Madrid vs Barcelona: Victoria local ✅\n"
            "• Manchester City vs Liverpool: Más de 2.5 goles ✅\n\n"
            "*TENIS*\n"
            "• Alcaraz vs Djokovic: Victoria Alcaraz ✅\n\n"
            "*BALONCESTO*\n"
            "• Lakers vs Celtics: Handicap +5.5 Celtics ❌\n\n"
            "💎 Para acceder a los pronósticos premium con mayor porcentaje de acierto, permanece atento a la activación del sistema de pago."
        )
        
        update.message.reply_text(pronosticos_texto, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error in pronosticos command: {e}")
        update.message.reply_text(
            "Lo siento, ha ocurrido un error mostrando los pronósticos. Por favor, intenta nuevamente más tarde."
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
