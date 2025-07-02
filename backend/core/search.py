"""
core/search.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:

"""

from core.logger import setup_logger
from lunr import lunr

# Global variables
search_index = None
logger = setup_logger(__name__)


def build_index(docs):
    """
    Builds a Lunr index from a list of documents.

    Args:
        docs (list): Each item must have keys 'id', 'title', 'content'.

    Returns:
        Lunr Index: In-memory search index.
    """
    global search_index
    search_index = lunr(ref="id", fields=("title", "content"), documents=docs)
    return search_index


def search_index(query, limit=5):
    """
    Searches the Lunr index.

    Args:
        query (str): Search query.
        limit (int): Max number of results.

    Returns:
        list: Search results metadata.
    """
    if not search_index:
        logger.warning("Search index not built. Returning empty results.")
        return []

    try:
        results = search_index.search(query)
        return results[:limit]
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return []
