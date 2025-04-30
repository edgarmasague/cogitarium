from core.logger import logger
from core.cache import init_cache_db
from core.vector_store import add_documents
from core.loader import load_all_files
import os

# Definir la ruta de la base de datos, debes poner la ruta correcta de tu base de datos aquí
DB_PATH = "path_to_your_lancedb_database"

# Suponiendo que LanceDB usa alguna biblioteca específica, aquí hay un ejemplo
def get_table():
    """
    Obtiene la tabla en LanceDB donde se almacenan los documentos.
    Asegúrate de que esta función esté correctamente configurada
    según la biblioteca o sistema de base de datos que estés usando.
    """
    # Este es solo un ejemplo, puedes necesitar adaptarlo a tu implementación específica
    from lancedb import open_table
    return open_table(DB_PATH)

def init_lancedb():
    try:
        # Revisar si la base de datos existe o si está vacía
        table = get_table()
        if not os.path.exists(DB_PATH) or table.count_rows() == 0:
            logger.info("🗄️  LanceDB is empty. Loading data...")
            texts = load_all_files()
            add_documents(texts)
        else:
            logger.info("✅ LanceDB already populated.")
    except Exception as e:
        logger.error(f"❌ Error initializing LanceDB: {e}")

def init_logging():
    logger.info("🔧 Logging iniciado correctamente.")

def init_cache():
    init_cache_db()
