"""
core/embedder.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Description:
    Embedding and semantic search using LanceDB with safe checks.
"""

import lancedb
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Optional

# Constantes
TABLE_NAME = "semantic_cache"
DB_PATH = "cache/lancedb"

# Cargar modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Conectar a la base de datos LanceDB
db = lancedb.connect(DB_PATH)

# Crear tabla si no existe
if TABLE_NAME not in db.table_names():
    db.create_table(
        TABLE_NAME,
        data=[{
            "id": "",
            "text": "",
            "vector": list(np.zeros(384, dtype='float32')),
            "metadata": {}
        }],
        mode="overwrite"
    )

# Función para añadir a LanceDB
def add_to_store(id: str, text: str, metadata: Optional[Dict] = None):
    """Añadir un nuevo texto embebido a LanceDB."""
    embedding = model.encode(text).astype(np.float32)
    table = db.open_table(TABLE_NAME)
    table.add([{
        "id": id,
        "text": text,
        "vector": embedding.tolist(),
        "metadata": metadata or {}
    }])

# Función para hacer búsquedas seguras
def safe_query_store(query: str, top_k: int = 5) -> List[Dict]:
    """Semantic search in LanceDB (safe version)."""
    try:
        db.create_table(
            TABLE_NAME,
            data=[{
                "id": "",
                "text": "",
                "vector": list(np.zeros(384, dtype='float32')),
                "metadata": {},
                "response": ""  # <-- AÑADIDO AQUI
            }],
            mode="create"
        )
    except Exception:
        pass

    table = db.open_table(TABLE_NAME)

    query_embedding = model.encode(query).astype("float32")
    results_df = table.search(query_embedding).limit(top_k).to_df()

    return [{
        "id": row["id"],
        "text": row["text"],
        "metadata": row["metadata"],
        "score": 1 - row["_distance"]
    } for _, row in results_df.iterrows()]
