"""
core/embedder.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Procedural version for embedding management with LanceDB integration
    Maintains full consistency with vector_store.py operations
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional

import lancedb
import numpy as np
from config.config import DB_PATH, EMBEDDING_MODEL, EMBEDDING_SIZE, TABLE_NAME
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

model = SentenceTransformer(EMBEDDING_MODEL)


def connect_db() -> lancedb.DBConnection:
    try:
        DB_PATH.mkdir(parents=True, exist_ok=True)
        return lancedb.connect(DB_PATH)
    except Exception as e:
        logger.error(f"Connection error: {str(e)}")
        raise


def init_table() -> lancedb.Table:
    db = connect_db()

    schema = lancedb.Schema(
        [
            lancedb.Field("vector", lancedb.Vector(EMBEDDING_SIZE)),
            lancedb.Field("text", "str"),
            lancedb.Field("metadata", "map<str, str>"),
        ]
    )

    try:
        if TABLE_NAME in db.table_names():
            table = db.open_table(TABLE_NAME)
            if table.schema != schema:
                logger.warning("Schema mismatch detected, recreating table")
                db.drop_table(TABLE_NAME)
                raise ValueError
            return table
        return db.create_table(TABLE_NAME, schema=schema)
    except:
        return db.create_table(
            TABLE_NAME,
            data=[
                {
                    "vector": np.zeros(EMBEDDING_SIZE, dtype=np.float32),
                    "text": "",
                    "metadata": {},
                }
            ],
            schema=schema,
        )


table = init_table()


def add_embedding(text: str, metadata: Optional[Dict] = None) -> bool:
    if not text or not isinstance(text, str):
        logger.error("Invalid text input")
        return False

    try:
        embedding = model.encode(text).astype(np.float32).tolist()
        table.add([{"vector": embedding, "text": text, "metadata": metadata or {}}])
        logger.debug(f"Added embedding: {text[:50]}...")
        return True
    except Exception as e:
        logger.error(f"Failed to add embedding: {str(e)}")
        return False


def search_similar(query: str, top_k: int = 5) -> List[Dict]:
    if not query or not isinstance(query, str):
        logger.error("Invalid query")
        return []

    try:
        query_embedding = model.encode(query).astype(np.float32).tolist()
        results = table.search(query_embedding).limit(top_k).to_list()

        return [
            {
                "text": res["text"],
                "similarity": 1 - res["_distance"],
                "metadata": res.get("metadata", {}),
            }
            for res in results
        ]
    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        return []
