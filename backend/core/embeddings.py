"""
core/embeddings.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Text embedding generator with batch processing and safety features
"""

from typing import List, Union

import numpy as np
from config.config import DEFAULT_BATCH_SIZE, EMBEDDING_SIZE, MODEL_NAME
from core.logger import setup_logger
from sentence_transformers import SentenceTransformer

logger = setup_logger(__name__)

try:
    logger.info("🧠 Loading embedding model: %s", MODEL_NAME)
    embedding_model = SentenceTransformer(MODEL_NAME)
    logger.success("✅ Embedding model loaded successfully")
except Exception as e:
    logger.critical("🔥 Failed to load embedding model: %s", str(e))
    raise


def embed_text(text: str, normalize: bool = True) -> List[float]:
    if not text or not isinstance(text, str):
        logger.error("Invalid text input: %s", text)
        raise ValueError("Input must be a non-empty string")

    try:
        embedding = embedding_model.encode(
            text, convert_to_numpy=True, normalize_embeddings=normalize
        )
        logger.debug("Generated embedding for text: %s...", text[:50])
        return embedding.tolist()
    except Exception as e:
        logger.error("Embedding generation failed: %s", str(e))
        raise


def embed_texts(
    texts: List[str], batch_size: int = DEFAULT_BATCH_SIZE
) -> List[List[float]]:
    if not texts or not isinstance(texts, list):
        logger.error("Invalid texts input")
        raise ValueError("Input must be a non-empty list of strings")

    try:
        embeddings = embedding_model.encode(
            texts, batch_size=batch_size, convert_to_numpy=True, show_progress_bar=False
        )
        logger.info(
            "Generated %d embeddings (shape: %s)",
            len(embeddings),
            str(embeddings.shape),
        )
        return embeddings.tolist()
    except Exception as e:
        logger.error("Batch embedding failed: %s", str(e))
        raise


def health_check() -> bool:
    try:
        test_embedding = embed_text("test")
        return len(test_embedding) == EMBEDDING_SIZE
    except:
        return False
