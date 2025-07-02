"""
routes/logs.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Log viewer module for monitoring system activity.
    It uses Jinja2Templates to serve the frontend from the templates directory.
    Provides both HTML interface and JSON API endpoints with i18n support.
"""

import os

from config.config import DEFAULT_LANG, LOG_FILE, TEMPLATES
from core.i18n import get_translation
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize a router for the homepage
router = APIRouter()

# Set the templates directory
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("/logs", response_class=HTMLResponse)
async def show_logs(request: Request):
    lang = request.query_params.get("lang", DEFAULT_LANG)
    t = get_translation(lang)

    if not os.path.exists(LOG_FILE):
        log_content = "No logs found."
    else:
        with open(LOG_FILE, "r") as f:
            log_content = f.read()

    return templates.TemplateResponse(
        "logs.html", {"request": request, "log_content": log_content, "t": t}
    )
