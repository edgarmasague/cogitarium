"""
routes/home.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This module defines the route responsible for rendering the main HTML interface.
    It uses Jinja2Templates to serve the frontend from the templates directory.
    Provides both HTML interface and JSON API endpoints with i18n support.
"""

from config.config import DEFAULT_LANG, TEMPLATES
from core.i18n import get_translation
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize a router for the homepage
router = APIRouter()

# Set the templates directory
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    lang = request.query_params.get("lang", DEFAULT_LANG)
    t = get_translation(lang)
    return templates.TemplateResponse("home.html", {"request": request, "t": t})
