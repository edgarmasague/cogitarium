"""
core/vector_store.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-28
Version: 1.0.0
License: MIT
Description:
    Entry point for the FastAPI application.
    It initializes the app, sets up middleware (like CORS), and includes all defined routes.
"""

from typing import Any, Dict, List

import lancedb
import numpy as np
import pyarrow as pa
from config.config import DB_PATH, TABLE_NAME
from core.logger import logger
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

try:
    db = lancedb.connect(DB_PATH)
    logger.info("Successfully connected to LanceDB")
except Exception as e:
    logger.error(f"Failed to connect to LanceDB: {str(e)}")
    raise

schema = pa.schema(
    [
        pa.field("vector", pa.list_(pa.float32(), list_size=384)),
        pa.field("text", pa.string()),
        pa.field("metadata", pa.string()),
    ]
)

try:
    if TABLE_NAME not in db.table_names():
        table = db.create_table(TABLE_NAME, schema=schema)
        logger.info(f"Created new table: {TABLE_NAME}")
    else:
        table = db.open_table(TABLE_NAME)
        logger.info(f"Opened existing table: {TABLE_NAME}")
except Exception as e:
    logger.error(f"Table operation failed: {str(e)}")
    raise


def add_to_store(text: str, metadata: Dict[str, Any] = None) -> None:
    try:
        if not isinstance(text, str) or len(text.strip()) == 0:
            raise ValueError("Invalid text input")

        embedding = model.encode(text).tolist()

        meta_str = str(metadata) if metadata else ""

        table.add([{"vector": embedding, "text": text, "metadata": meta_str}])
        logger.debug(f"Added text to store: {text[:50]}...")

    except Exception as e:
        logger.error(f"Failed to add to store: {str(e)}")
        raise


def add_documents(texts: List[str]) -> None:
    try:
        if not isinstance(texts, list):
            raise TypeError("Input must be a list of strings")

        for text in texts:
            try:
                if isinstance(text, tuple):
                    text = text[0]

                if isinstance(text, str) and len(text.strip()) > 0:
                    add_to_store(text)
                else:
                    logger.warning("Skipping invalid document")
            except Exception as e:
                logger.error(f"Failed to process document: {str(e)}")
                continue

        logger.info(f"Successfully added {len(texts)} documents")

    except Exception as e:
        logger.error(f"Document addition failed: {str(e)}")
        raise


def search_similar(query: str, top_k: int = 5) -> List[Dict]:
    try:
        if not isinstance(query, str) or len(query.strip()) == 0:
            raise ValueError("Invalid query")

        query_embedding = model.encode(query).tolist()
        logger.debug(f"Query embedding generated for: {query[:50]}...")

        results = table.search(query_embedding).limit(top_k).to_list()

        if not results:
            logger.info("No results found")
            return []

        formatted_results = []
        for result in results:
            try:
                formatted_results.append(
                    {
                        "text": result["text"],
                        "similarity": 1.0 - result["_distance"],
                        "metadata": (
                            eval(result["metadata"]) if result["metadata"] else {}
                        ),
                    }
                )
            except:
                logger.warning("Failed to parse metadata")

        return formatted_results

    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        return []
