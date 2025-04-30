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
from .i18n import get_translation
from .init import init_cache, init_logging
from .loader import load_all_files
from .logger import setup_logger
from .translator import detect_language, translate_from_english, translate_to_english
from .search import build_index, search_index
from .cache import init_cache_db, sanitize_filename, key_to_filename, get_cached_response, save_to_cache, delete_cached_response
from .vector_store import add_to_store, add_documents, search_similar
from .embedder import connect_db, init_table, add_embedding, search_similar
from.embeddings import embed_text, embed_texts, health_check
from .assistant import process_message_flow, _handle_language_detection, _build_messages, _get_ai_response, _translate_response
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
    "_translate_response"
]