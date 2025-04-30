# core/vector_store.py

import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer

DB_PATH = "cache/lancedb"
TABLE_NAME = "responses"

# Cargar el modelo
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Conectar a la base de datos
db = lancedb.connect(DB_PATH)

# Definir el esquema
schema = pa.schema([
    pa.field("vector", pa.list_(pa.float32(), list_size=384)),
    pa.field("text", pa.string())
])

# Crear tabla si no existe
if TABLE_NAME not in db.table_names():
    db.create_table(TABLE_NAME, schema=schema)

table = db.open_table(TABLE_NAME)


def add_documents(texts: list):
    """Añade una lista de documentos al vector store."""
    for text in texts:
        print(f"DEBUG: Recibido en add_documents: {text} (tipo: {type(text)})")
        if isinstance(text, tuple):
            text = text[0]
        add_to_store(text)


def search_similar(query: str, top_k: int = 5):
    # Asegurémonos de que la base de datos está conectada y que tenemos acceso a la tabla
    print("Conectando a la base de datos...", flush=True)

    # Convertir la consulta en un embedding
    query_embedding = model.encode(query).tolist()
    print(f"Embedding de la consulta: {query_embedding[:10]}...", flush=True)  # Mostrar los primeros 10 valores del embedding

    # Realizar la búsqueda en la base de datos
    try:
        results = table.search(query_embedding).limit(top_k).to_list()
        print(f"Resultados de la búsqueda: {results}", flush=True)
    except Exception as e:
        print(f"Error al buscar en la base de datos: {str(e)}", flush=True)
        return []

    if not results:
        print("No se encontraron resultados", flush=True)

    return [
        {
            "text": result["text"],
            "similarity": 1.0 - result["_distance"]
        }
        for result in results
    ]
