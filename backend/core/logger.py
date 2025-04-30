import logging
import os

# Ruta donde se almacenarán los logs
LOG_PATH = "logs/cogitarium.log"

# Asegurarse de que el directorio de logs exista
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Configuración básica de logging
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,  # Se ajusta el nivel de log (INFO, DEBUG, ERROR, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Crear un logger con el nombre de la aplicación o módulo
logger = logging.getLogger("cogitarium")

# Ejemplo de cómo utilizar el logger
def log_example():
    logger.debug("Este es un mensaje de depuración")
    logger.info("Este es un mensaje informativo")
    logger.warning("Este es un mensaje de advertencia")
    logger.error("Este es un mensaje de error")
    logger.critical("Este es un mensaje crítico")

# Llamar a log_example para probar los logs
log_example()
