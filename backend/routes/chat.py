"""
routes/chat.py

Author: Edgar Masagué https://github.com/edgarmasague
Created: 2025-04-21
Description:
    This module defines the `/chat` API route that receives user messages,
    adds system context, and sends them to the configured AI model.
    It uses the assistant core logic to return helpful responses
    in a structured JSON format.

    It is part of a modular FastAPI backend where routes, core logic,
    configuration, and templates are separated for clarity and maintainability.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from core.context_builder import build_context
from core.assistant import ask_ai
from config.config import SYSTEM_MESSAGES

from core.cache import get_cached_response, save_to_cache

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/chat")
async def post_chat(message: Message):
    try:
        context = build_context(message.message)

        messages = [
            {"role": "system", "content": SYSTEM_MESSAGES},
            {"role": "user", "content": f"Pregunta: {message.message}\n\nContexto:\n{context}"}
        ]

        response = ask_ai(messages)

        return {"reply": response}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
