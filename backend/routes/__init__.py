"""
routes/__init__.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This module aggregates all route modules under a single APIRouter instance.
    It includes the home and chat route handlers, making them accessible via the main app.
"""

from fastapi import APIRouter

from .cache import router as cache_router
from .chat import router as chat_router
# Import individual routers from route modules
from .home import router as home_router
from .logs import router as logs_router

# Main router that includes all sub-routers
router = APIRouter()

# Register route modules
router.include_router(home_router)
router.include_router(chat_router)
router.include_router(logs_router)
router.include_router(cache_router)
