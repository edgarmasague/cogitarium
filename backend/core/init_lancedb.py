"""
scripts/init_lancedb.py

Author: Edgar Masagué
Created: 2025-04-26
Description:
    Script para inicializar la tabla 'semantic_cache' en LanceDB manualmente.
"""

import lancedb
import numpy as np
import os

def init_lancedb():
    # Asegurar que la carpeta cache/lancedb existe
    os.makedirs("cache/lancedb", exist_ok=True)
    
    # Conectar
    db = lancedb.connect("cache/lancedb")

    # Si la tabla ya existe, borrarla
    if "semantic_cache" in db.table_names():
        db.drop_table("semantic_cache")
        print("Tabla 'semantic_cache' eliminada.")

    # Crear nueva tabla
    db.create_table(
        "semantic_cache",
        data=[{
            "id": "",
            "text": "",
            "vector": list(np.zeros(384, dtype='float32')),
            "metadata": {}
        }],
        mode="overwrite"
    )
    print("Tabla 'semantic_cache' creada correctamente.")

if __name__ == "__main__":
    init_lancedb()
