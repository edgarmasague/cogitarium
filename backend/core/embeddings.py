from sentence_transformers import SentenceTransformer
from core.logger import logger

# Inicializamos el modelo al cargar el módulo
logger.info("🧠 Loading sentence-transformer model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    """Genera un embedding para un solo texto."""
    return embedding_model.encode(text)

def embed_texts(texts: list[str]) -> list[list[float]]:
    """Genera embeddings para una lista de textos."""
    return embedding_model.encode(texts).tolist()
