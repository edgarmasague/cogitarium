"""
core/init.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-27
Version: 1.0.0
License: MIT
Description:
    Initialization module that sets up logging and cache systems on app startup.
"""

import os
from pathlib import Path
from typing import Optional

from config.config import CACHE_PATH, LANCE_DB_PATH
from core.cache import init_cache_db
from core.loader import load_all_files
from core.logger import setup_logger
from core.vector_store import add_documents
from lancedb import DBConnection, LanceTable

logger = setup_logger(__name__)


def get_table(db_path: Path = LANCE_DB_PATH) -> Optional[LanceTable]:
    try:
        db = DBConnection(db_path)
        return db.open_table("documents")
    except Exception as e:
        logger.error(f"Error connecting to LanceDB: {str(e)}")
        return None


def init_lancedb() -> bool:
    try:
        table = get_table()

        if not table or table.count_rows() == 0:
            logger.info("🗄️ Initializing LanceDB...")
            if not LANCE_DB_PATH.exists():
                LANCE_DB_PATH.mkdir(parents=True, exist_ok=True)

            if texts := load_all_files():
                add_documents(texts, table)
                logger.success("✅ LanceDB initialized successfully")
                return True
            logger.warning("⚠️ No documents found to load")
            return False

        logger.info("✅ LanceDB already contains data")
        return True

    except Exception as e:
        logger.critical(f"❌ Critical error initializing LanceDB: {str(e)}")
        return False


def init_logging() -> None:
    logger.info("📝 Logging system operational")


def init_cache() -> bool:
    try:
        init_cache_db(CACHE_PATH)
        logger.info("💾 Cache initialized")
        return True
    except Exception as e:
        logger.error(f"❌ Error initializing cache: {str(e)}")
        return False


def initialize_all() -> None:
    init_logging()
    if not init_cache():
        raise RuntimeError("Failed to initialize cache")
    if not init_lancedb():
        raise RuntimeError("Failed to initialize LanceDB")
