"""
core/__init__.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-24
Description:
    This file initializes the core module. It can be used to import all necessary components from the core package.
    It helps in organizing code by separating functionality into different modules.
"""

from .assistant import ask_ai
from .ai_config import get_ai_client
from .loader import load_all_files
from .query_rewrite import rewrite_query
from .search import build_index, search
from .logger import logger
from .cache import (
    get_cached_response,
    save_to_cache,
    get_cached_response,
    init_cache_db,
)

__all__ = [
    "ask_ai", 
    "get_ai_client", 
    "load_all_files", 
    "rewrite_query", 
    "build_index", 
    "search",
    "logger",
    "get_cached_response",
    "save_to_cache",
    "get_cached_responses",
    "init_cache_db"
]
