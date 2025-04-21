import json
import os
import logging
from openai import OpenAI

logger = logging.getLogger(__name__)

# Inicializar el cliente con la clave API de OpenRouter desde las variables de entorno
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def get_ai_response(mensaje, contexto=None):
    """
    Genera una respuesta utilizando el modelo GPT de OpenAI.
    
    Args:
        mensaje (str): El mensaje del usuario.
        contexto (str, opcional): Contexto adicional para la respuesta.
        
    Returns:
        str: La respuesta generada por la IA.
    """
    try:
        # Crear el prompt con instrucciones específicas
        system_message = """
        Eres el asistente de Banca Blindada, un servicio de pronósticos deportivos premium.
        Responde de manera amigable, profesional y concisa, como un asesor deportivo.
        Usa un tono informal y cercano, como hablando con un amigo que sabe de deportes.
        Incluye algunos emojis ocasionales para dar más personalidad.
        Limita tus respuestas a 2-3 oraciones como máximo.
        
        Información sobre Banca Blindada:
        - Ofrece pronósticos deportivos premium con alta tasa de acierto
        - El sistema de pagos está aún en desarrollo
        - Los pronósticos exclusivos se compartirán en un grupo especial
        - El enfoque principal es en fútbol, tenis, baloncesto y béisbol
        - No prometas porcentajes específicos de acierto
        """
        
        # Preparar el contexto si existe
        if contexto:
            system_message += f"\nContexto adicional: {contexto}"
            
        # Llamada a la API de OpenRouter
        # Usamos Anthropic Claude para una buena relación calidad/precio
        response = client.chat.completions.create(
            model="anthropic/claude-3-haiku",  # Modelo de Anthropic a través de OpenRouter
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": mensaje}
            ],
            max_tokens=150,  # Límite para mantener respuestas concisas
            headers={
                "HTTP-Referer": "https://bancablindada.com",  # Sitio web del proyecto
                "X-Title": "Banca Blindada Bot"  # Nombre del proyecto
            }
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"Error al generar respuesta con IA (OpenRouter): {e}")
        return "Lo siento, estoy teniendo problemas para procesar tu consulta. Por favor, intenta nuevamente en unos momentos. 🙏"