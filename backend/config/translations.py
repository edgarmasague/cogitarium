# config/translations.py

translations = {
    "es": {
        "title": "Cogitarium",
        "input_placeholder": "Escribí algo...",
        "send": "Enviar",
        "logs_title": "🧠 Logs de Cogitarium",
        "cache_title": "📦 Caché de Cogitarium",
        "back": "← Volver al chat"
    },
    "en": {
        "title": "Cogitarium",
        "input_placeholder": "Type something...",
        "send": "Send",
        "logs_title": "🧠 Cogitarium Logs",
        "cache_title": "📦 Cogitarium Cache",
        "back": "← Back to chat"
    },
    "pt": {
        "title": "Cogitarium",
        "input_placeholder": "Digite algo...",
        "send": "Enviar",
        "logs_title": "🧠 Logs do Cogitarium",
        "cache_title": "📦 Cache do Cogitarium",
        "back": "← Voltar ao chat"
    }
}

def get_translation(lang: str) -> dict:
    """
    Devuelve el diccionario de traducciones para el idioma especificado.
    Si el idioma no existe, retorna el español como fallback.
    """
    return translations.get(lang, translations["es"])
