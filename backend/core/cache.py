import json
import os
import re
import hashlib

CACHE_PATH = "cache"

def init_cache_db():
    os.makedirs(CACHE_PATH, exist_ok=True)
    print("Cache initialized.")

def sanitize_filename(filename: str) -> str:
    filename = filename.replace("\n", " ").replace("\r", "")
    return re.sub(r'[^\w\s-]', '', filename).strip().replace(" ", "_")

def key_to_filename(key: str) -> str:
    """Convierte cualquier key a un nombre de archivo corto usando SHA256."""
    hash_object = hashlib.sha256(key.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig + ".json"

def get_cached_response(key: str) -> dict | None:
    filename = key_to_filename(key)
    cache_file = os.path.join(CACHE_PATH, filename)
    if os.path.isfile(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_to_cache(key: str, data: dict):
    filename = key_to_filename(key)
    file_path = os.path.join(CACHE_PATH, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def delete_cached_response(key: str) -> bool:
    filename = key_to_filename(key)
    file_path = os.path.join(CACHE_PATH, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
