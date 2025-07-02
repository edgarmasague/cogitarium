"""
main.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Entry point for the FastAPI application.
    It initializes the app, sets up middleware (like CORS), and includes all defined routes.
"""

from core.init import init_cache, init_logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as routes_router

# Initialize FastAPI app
app = FastAPI(
    title="Cogitarium API",
    description="An AI-powered search and assistant platform with logging and caching",
    version="1.0.0",
)

# Initialize logging and cache systems
init_logging()
init_cache()

# Allow frontend access (CORS configuration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(routes_router)
