from core.vector_store import search_similar
from core.loader import load_all_files

def build_context(user_query: str, top_k: int = 5) -> str:
    """
    Construye el contexto para enviar a la IA:
    - Intenta buscar información similar en LanceDB.
    - Si no encuentra resultados, carga contexto desde archivos locales.
    """
    similar_docs = search_similar(user_query, top_k=top_k)

    if similar_docs:
        context = "\n\n".join(doc["text"] for doc in similar_docs)
    else:
        context = load_all_files()[:2000]  # fallback

    return context
