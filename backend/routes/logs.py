from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from core.i18n import get_translation

router = APIRouter()
templates = Jinja2Templates(directory="templates")
LOG_FILE = "logs/cogitarium.log"

@router.get("/logs", response_class=HTMLResponse)
async def show_logs(request: Request):
    lang = request.query_params.get("lang", "es")
    t = get_translation(lang)

    # Verificar si el archivo de logs existe
    if not os.path.exists(LOG_FILE):
        log_content = "No logs found."
    else:
        try:
            # Leer el contenido del archivo de log de forma segura
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_content = f.read()
        except Exception as e:
            # Si ocurre algún error al leer el archivo
            log_content = f"Error reading log file: {str(e)}"

    return templates.TemplateResponse("logs.html", {
        "request": request,
        "log_content": log_content,
        "t": t
    })
