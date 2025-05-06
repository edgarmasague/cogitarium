"""
routes/chat.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:

"""

from typing import Dict, List, Optional

from config.config import SYSTEM_MESSAGES
from core.assistant import process_message_flow
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    success: bool
    reply: str
    error: Optional[str] = None


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = process_message_flow(
            user_message=request.message,
            system_prompt=SYSTEM_MESSAGES,
            session_id=request.session_id,
        )

        return ChatResponse(
            success=not response.startswith("Error"),
            reply=response,
            error=response if response.startswith("Error") else None,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=ChatResponse(
                success=False, reply="Internal server error", error=str(e)
            ).dict(),
        )
