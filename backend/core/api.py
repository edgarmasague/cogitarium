from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from backend.core.ai_config import get_ai_client
from assistant import ask_ai
from loader import load_all_files

SYSTEM_MESSAGES = """
    You are a kind, patient, and clear assistant. Your goal is to help people who may have difficulties remembering, focusing, or understanding complex concepts.
    You always explain things using simple words, in a calm and step-by-step manner. If something is unclear, you provide examples. You never assume — you ask for clarification when needed.
    Your tone is supportive, positive, and encouraging. You are here to assist and make life easier for the user, without judgment or pressure.
"""

app = FastAPI()

# Cargar plantilla HTML
templates = Jinja2Templates(directory="templates")

# Modelo de mensaje
class Message(BaseModel):
    message: str

# Ruta para servir el HTML principal
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta de la API
@app.post("/chat")
async def chat(message: Message):
    context = load_all_files()
    client, model = get_ai_client()
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGES},
        {"role": "user", "content": f"Pregunta: {message.message}\n\nContext:\n{context[:2000]}"}
    ]
    try:
        response = ask_ai(messages)
        return {"reply": response}
    except Exception as e:
        return {"reply": f"Error al consultar la IA: {str(e)}"}