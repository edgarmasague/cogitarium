"""
core/__init__.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This file initializes the core module. It can be used to import all necessary components from the core package.
    It helps in organizing code by separating functionality into different modules.
"""

from .ai_config import get_ai_client
from .assistant import (_build_messages, _get_ai_response,
                        _handle_language_detection, _translate_response,
                        process_message_flow)
from .cache import (delete_cached_response, get_cached_response, init_cache_db,
                    key_to_filename, sanitize_filename, save_to_cache)
from .embedder import add_embedding, connect_db, init_table, search_similar
from .embeddings import embed_text, embed_texts, health_check
from .i18n import get_translation
from .init import init_cache, init_logging
from .loader import load_all_files
from .logger import setup_logger
from .search import build_index, search_index
from .translator import (detect_language, translate_from_english,
                         translate_to_english)
from .vector_store import add_documents, add_to_store, search_similar

__all__ = [
    "get_ai_client",
    "get_translation",
    "init_cache",
    "init_logging",
    "load_all_files",
    "setup_logger",
    "detect_language",
    "translate_from_english",
    "translate_to_english",
    "build_index",
    "search_index",
    "init_cache_db",
    "sanitize_filename",
    "key_to_filename",
    "get_cached_response",
    "save_to_cache",
    "delete_cached_response",
    "add_to_store",
    "add_documents",
    "search_similar",
    "connect_db",
    "init_table",
    "add_embedding",
    "embed_text",
    "embed_texts",
    "health_check",
    "process_message_flow",
    "_handle_language_detection",
    "_build_messages",
    "_get_ai_response",
    "_translate_response",
]
