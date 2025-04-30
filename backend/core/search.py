"""
core/search.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-21
Description:
    This module is responsible for building a Lunr search index and performing searches on indexed documents.
    It allows searching through large collections of documents efficiently.
"""

from lunr import lunr
import logging

# Global search index
search_index = None

def build_index(docs):
    """
    Builds a Lunr index from a list of documents.

    Args:
        docs (list): Each item must have keys 'id', 'title', 'content'.

    Returns:
        Lunr Index: In-memory search index.
    """
    global search_index
    search_index = lunr(ref='id', fields=('title', 'content'), documents=docs)
    return search_index

def search(query, limit=5):
    """
    Searches the Lunr index.

    Args:
        query (str): Search query.
        limit (int): Max number of results.

    Returns:
        list: Search results metadata.
    """
    if not search_index:
        logging.warning("Search index not built. Returning empty results.")
        return []

    try:
        results = search_index.search(query)
        return results[:limit]
    except Exception as e:
        logging.error(f"Search failed: {e}")
        return []
