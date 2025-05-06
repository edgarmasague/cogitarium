"""
core/translator.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-28
Version: 1.0.0
License: MIT
Description:
    Language processing module providing automatic translation services between
    English and multiple languages using Google Translate API.
"""

from deep_translator import GoogleTranslator
from langdetect import detect


def detect_language(text, source_lang):

    try:
        return detect(text)
    except:
        return source_lang


def translate_to_english(text, select_lang):

    source_lang = detect_language(text, select_lang)

    if source_lang == "en":
        return text
    try:
        return GoogleTranslator(source=source_lang, target="en").translate(text)
    except Exception as e:
        return f"Error al traducir: {str(e)}"


def translate_from_english(text, target_lang):

    if target_lang == "en":
        return text
    try:
        return GoogleTranslator(source="en", target=target_lang).translate(text)
    except Exception as e:
        return f"Error al traducir: {str(e)}"
