"""
core/assistant.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Central AI processing module with caching, translation and vector storage integration
"""

from typing import Dict, List, Optional

from core.ai_config import get_ai_client
from core.cache import get_cached_response, save_to_cache
from core.logger import setup_logger
from core.translator import (detect_language, translate_from_english,
                             translate_to_english)
from core.vector_store import add_to_store

logger = setup_logger(__name__)


def process_message_flow(
    user_message: str,
    system_prompt: str,
    temperature: float = 0.7,
    use_cache: bool = True,
    session_id: Optional[str] = None,
) -> str:

    try:
        cache_key = f"{session_id}:{user_message}" if session_id else user_message

        if use_cache and (cached := get_cached_response(cache_key)):
            logger.info("Cache hit for: %s...", cache_key[:50])
            return cached

        original_lang, needs_translation = _handle_language_detection(user_message)

        messages = _build_messages(
            user_message, system_prompt, original_lang, needs_translation
        )

        ai_response = _get_ai_response(messages, temperature)

        final_response = _translate_response(
            ai_response, original_lang, needs_translation
        )

        if use_cache:
            save_to_cache(cache_key, final_response)
            add_to_store(user_message, final_response)

        return final_response

    except Exception as e:
        logger.error("Processing error: %s", str(e), exc_info=True)
        return f"Error: {str(e)}"


def _handle_language_detection(text: str) -> Tuple[str, bool]:
    try:
        lang = detect_language(text, "en")
        return lang, lang != "en"
    except Exception as e:
        logger.warning("Language detection failed: %s", str(e))
        return "en", False


def _build_messages(
    user_message: str, system_prompt: str, source_lang: str, needs_translation: bool
) -> List[Dict]:
    translated_message = (
        translate_to_english(user_message, source_lang)
        if needs_translation
        else user_message
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": translated_message},
    ]


def _get_ai_response(messages: List[Dict], temperature: float) -> str:
    client, model = get_ai_client()

    try:
        response = client.chat.completions.create(
            model=model, temperature=temperature, messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error("AI API call failed: %s", str(e))
        raise


def _translate_response(
    response: str, target_lang: str, needs_translation: bool
) -> str:
    if not needs_translation or target_lang == "en":
        return response

    translated = translate_from_english(response, target_lang)
    if "Error" in translated:
        logger.warning("Back translation failed, returning English response")
        return response

    return translated
