from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text: str) -> str:
    """
    Detecta el idioma del texto ingresado.

    Args:
        text (str): Texto de entrada para detección de idioma.

    Returns:
        str: Código del idioma detectado, por ejemplo, 'en' para inglés.
    """
    try:
        return detect(text)
    except:
        return "en"  # Fallback al inglés en caso de error

def translate_to_english(text: str, source_lang: str) -> str:
    """
    Traduce el texto a inglés desde el idioma de origen especificado.

    Args:
        text (str): Texto que se quiere traducir.
        source_lang (str): Código de idioma de origen (por ejemplo, 'es' para español).

    Returns:
        str: Texto traducido al inglés.
    """
    if source_lang == "en":
        return text
    try:
        return GoogleTranslator(source=source_lang, target="en").translate(text)
    except Exception as e:
        return f"Error al traducir: {str(e)}"

def translate_from_english(text: str, target_lang: str) -> str:
    """
    Traduce el texto desde inglés al idioma de destino especificado.

    Args:
        text (str): Texto que se quiere traducir.
        target_lang (str): Código de idioma de destino (por ejemplo, 'es' para español).

    Returns:
        str: Texto traducido al idioma de destino.
    """
    if target_lang == "en":
        return text
    try:
        return GoogleTranslator(source="en", target=target_lang).translate(text)
    except Exception as e:
        return f"Error al traducir: {str(e)}"

# Nuevas funciones que faltan para la integración

def auto_translate_incoming(text: str) -> tuple:
    """
    Detecta el idioma del texto y lo traduce a inglés si es necesario.

    Args:
        text (str): Texto de entrada.

    Returns:
        tuple: Texto traducido al inglés y el idioma original detectado.
    """
    detected_lang = detect_language(text)
    translated_text = translate_to_english(text, detected_lang)
    return translated_text, detected_lang

def auto_translate_outgoing(text: str, target_lang: str) -> str:
    """
    Traduce el texto desde inglés al idioma de destino.

    Args:
        text (str): Texto en inglés a traducir.
        target_lang (str): Código de idioma de destino.

    Returns:
        str: Texto traducido al idioma de destino.
    """
    return translate_from_english(text, target_lang)
