"""
core/i18n.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Translation utility module for loading localized JSON language files.
    Provides fallback to English ('en') when requested translations are unavailable.
"""

import json
import os

from config.config import TRANSLATIONS_PATH


def get_translation(lang: str = "en") -> dict:
    """
    Loads [lang].json translations with English fallback.

    Args:
        lang: Language code (default 'es')

    Returns:
        {key: text} mappings from JSON file
    """
    filepath = os.path.join(TRANSLATIONS_PATH, f"{lang}.json")

    if not os.path.isfile(filepath):
        filepath = os.path.join(TRANSLATIONS_PATH, "en.json")

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
