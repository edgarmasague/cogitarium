import json
import os

TRANSLATIONS_PATH = "translations"

def get_translation(lang: str = "es") -> dict:
    filepath = os.path.join(TRANSLATIONS_PATH, f"{lang}.json")
    if not os.path.isfile(filepath):
        filepath = os.path.join(TRANSLATIONS_PATH, "es.json")  # fallback
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
