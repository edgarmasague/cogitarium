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

__all__ = [
    "get_ai_client",
    "get_translation"
]