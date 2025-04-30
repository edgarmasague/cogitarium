from core.logger import logger
from core.cache import get_cached_response, save_to_cache
from core.embedder import add_to_store
from core.translator import auto_translate_incoming, auto_translate_outgoing
from core.ai_config import get_ai_client

def ask_ai(messages, temperature=0.7, client=None, model=None) -> str:
    """
    Procesa los mensajes, consulta caché, manda al modelo y almacena el resultado.

    Args:
        messages (list): Lista de mensajes para el modelo (rol + contenido)
        temperature (float): Parámetro de temperatura para el modelo (por defecto 0.7)
        client (optional): Cliente de IA para interactuar con el modelo.
        model (optional): Modelo de IA que se utilizará.

    Returns:
        str: Respuesta generada por el modelo.
    """

    try:
        # Extraer la pregunta principal del usuario
        user_message = next((m["content"] for m in messages if m["role"] == "user"), None)
        if not user_message:
            return "No user message found."

        # Buscar en la caché primero
        cached = get_cached_response(user_message)
        if cached:
            logger.info("✅ Cache hit")
            return cached

        # Traducir si es necesario
        user_message_translated, detected_lang = auto_translate_incoming(user_message)

        # Actualizar el mensaje traducido en la lista
        updated_messages = []
        for m in messages:
            if m["role"] == "user":
                updated_messages.append({"role": "user", "content": user_message_translated})
            else:
                updated_messages.append(m)

        # Si no se pasa un cliente ni un modelo, obtenemos el cliente y el modelo predeterminados
        if client is None or model is None:
            client, model = get_ai_client()

        # Revisar el cliente para asegurarse de que tenga el atributo 'chat' o 'ChatCompletion'
        if not hasattr(client, "chat") and not hasattr(client, "ChatCompletion"):
            raise AttributeError("El cliente de IA no tiene el atributo 'ChatCompletion'.")

        # Llamada al modelo usando el cliente proporcionado
        logger.info("🧠 Sending to AI model...")
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=updated_messages
        )

        # Log para ver la respuesta completa
        logger.info(f"🧠 AI Response: {response}")

        try:
            ai_response = response.choices[0].message.content
        except Exception as e:
            ai_response = f"Error parsing response: {e}"


        # Traducir la respuesta de vuelta al idioma original
        final_response = auto_translate_outgoing(ai_response, detected_lang)

        # Guardar en caché
        save_to_cache(user_message, final_response)

        # Guardar en vector store (LanceDB)
        add_to_store(user_message, final_response)

        return final_response

    except Exception as e:
        logger.error(f"❌ Error in ask_ai: {e}")
        return f"Error: {str(e)}"
