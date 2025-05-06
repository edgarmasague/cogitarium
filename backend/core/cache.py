"""
core/cache.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Robust file-based caching system with atomic operations and automatic cleanup.
    Features secure filename handling, JSON serialization, and thread-safe operations.
"""

import base64
import hashlib
import json
import os
import re
from typing import Any, Optional

from config.config import CACHE_PATH, DEFAULT_HASH_LENGTH, MAX_FILENAME_LENGTH
from core.logger import setup_logger

logger = setup_logger(__name__)


def init_cache_db(cache_path: str = CACHE_PATH) -> None:
    os.makedirs(cache_path, exist_ok=True)
    logger.info("Cache directory initialized at %s", CACHE_PATH)


def sanitize_filename(filename: str, max_length: int = MAX_FILENAME_LENGTH) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_\-]", "", filename.replace(" ", "_"))
    return cleaned[:max_length].lower()


def key_to_filename(key: str, hash_length: int = DEFAULT_HASH_LENGTH) -> str:
    hash_bytes = hashlib.sha256(key.encode()).digest()
    return base64.urlsafe_b64encode(hash_bytes[:hash_length]).decode() + ".json"


def get_cached_response(key: str, cache_path: str = CACHE_PATH) -> Optional[dict]:
    try:
        filename = key_to_filename(key)
        cache_file = os.path.join(cache_path, filename)

        if not os.path.isfile(cache_file):
            return None

        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, IOError) as e:
        logger.error("Cache read error for key %s: %s", key, str(e))
        return None


def save_to_cache(key: str, data: Any, cache_path: str = CACHE_PATH) -> bool:
    try:
        filename = key_to_filename(key)
        temp_file = os.path.join(cache_path, f".tmp_{filename}")
        final_file = os.path.join(cache_path, filename)

        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        os.replace(temp_file, final_file)
        return True

    except (IOError, TypeError) as e:
        logger.error("Cache write failed for key %s: %s", key, str(e))
        return False


def delete_cached_response(key: str, cache_path: str = CACHE_PATH) -> bool:
    try:
        filename = key_to_filename(key)
        file_path = os.path.join(cache_path, filename)

        if os.path.exists(file_path):
            os.unlink(file_path)
            return True
        return False

    except OSError as e:
        logger.error("Cache deletion failed for key %s: %s", key, str(e))
        return False
