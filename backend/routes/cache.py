"""
routes/cache.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Defines API routes for cache management and semantic search operations.
    It uses Jinja2Templates to serve the frontend from the templates directory.
    Provides both HTML interface and JSON API endpoints with i18n support.
"""

import os
import sqlite3
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.i18n import get_translation
from config.config import TEMPLATES, DEFAULT_LANG, CACHE_DB

# Initialize a router for the homepage
router = APIRouter()

# Set the templates directory
templates = Jinja2Templates(directory = TEMPLATES)

@router.get("/cache", response_class = HTMLResponse)
async def show_cache(request: Request):
    lang = request.query_params.get("lang", DEFAULT_LANG)
    t = get_translation(lang)

    if not os.path.exists(CACHE_DB):
        cache_content = []
    else:
        conn = sqlite3.connect(CACHE_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT prompt, response FROM cache")
        cache_content = cursor.fetchall()
        conn.close()

    return templates.TemplateResponse("cache.html", {
        "request": request,
        "cache_content": cache_content,
        "t": t
    })