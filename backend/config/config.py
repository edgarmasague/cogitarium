"""
config/config.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This module contains general configuration constants and helper functions
    used across the application — including system messages and settings.
    It aims to centralize configuration in one place to simplify changes and maintenance.
"""

import os
from typing import List

# Paths
TRANSLATIONS_PATH: str = "translations"
CACHE_DB: str = os.path.join("cache", "cache.db")
TEMPLATES: str = "templates"
LOG_FILE: str = os.path.join("logs", "cogitarium.log")

# Language
DEFAULT_LANG: str = "en"

# System Prompts
SYSTEM_MESSAGES: str = """\
You are a kind, patient, and clear assistant. Your goal is to help people who may have 
difficulties remembering, focusing, or understanding complex concepts.
Always explain things using simple words, in a calm and step-by-step manner.
If something is unclear, provide examples. Never assume - ask for clarification when needed.
Your tone should be supportive, positive, and encouraging.
"""

# Query Rewriting
QUERY_REWRITE: str = """\
Your goal is to rewrite vague or incomplete questions to be more specific,
concise, and relevant for searching technical markdown documentation.
"""

QUERY_REWRITE_STYLE_1: str = """\
Focus on extracting keywords. Eliminate unnecessary words.
Add relevant technical terms if possible.
"""

QUERY_REWRITE_STYLE_2: str = """\
Use synonyms, add context if needed, and improve wording while preserving meaning.
"""

# Model Parameters
QUERY_TEMPERATURE: List[float] = [0.3, 0.5]
QUERY_TEMPERATURE_REFACT: float = 0.7

# Cache Configuration
CACHE_PATH: str = "cache"
DEFAULT_HASH_LENGTH: int = 16
MAX_FILENAME_LENGTH: int = 255

# Search Parameters
SIMILARITY_THRESHOLD: float = 0.85
MIN_RESULTS_DIFFERENCE: int = 3

# Vector Database
DB_PATH: str = os.path.join("cache", "lancedb")
TABLE_NAME: str = "responses"

# Embeddings
EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_SIZE: int = 384
DEFAULT_BATCH_SIZE: int = 32
