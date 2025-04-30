"""
routes/home.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-21
Description:
    This module defines the route responsible for rendering the main HTML interface.
    It uses Jinja2Templates to serve the frontend from the templates directory.
    Adds i18n support to load content in different languages.
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.i18n import get_translation

# Initialize a router for the homepage
router = APIRouter()

# Set the templates directory (make sure it exists at /templates)
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    lang = request.query_params.get("lang", "es")
    t = get_translation(lang)
    return templates.TemplateResponse("index.html", {"request": request, "t": t})

