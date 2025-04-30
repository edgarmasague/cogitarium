from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import sqlite3
from core.i18n import get_translation
from core.cache import get_cached_response, delete_cached_response

router = APIRouter()
templates = Jinja2Templates(directory="templates")
CACHE_DB = "cache/cache.db"

# Ruta para mostrar el contenido del caché con soporte de búsqueda
@router.get("/cache", response_class=HTMLResponse)
async def show_cache(request: Request, q: str = ""):
    lang = request.query_params.get("lang", "es")
    t = get_translation(lang)

    # Obtener el contenido del caché, filtrado por búsqueda si es necesario
    if not os.path.exists(CACHE_DB):
        cache_content = []
    else:
        cache_content = get_cached_response(search_query=q)

    return templates.TemplateResponse("cache.html", {
        "request": request,
        "cache_content": cache_content,
        "t": t,
        "search_query": q  # Para mostrar el término de búsqueda actual
    })

# Ruta para eliminar una entrada del caché
@router.post("/cache/delete", response_class=RedirectResponse)
async def delete_cache_entry(question: str = Form(...)):
    """Elimina una entrada del caché por su pregunta."""
    delete_cached_response(question)
    return RedirectResponse("/cache", status_code=303)
