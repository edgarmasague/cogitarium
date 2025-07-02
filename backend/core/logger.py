"""
core/logger.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:

"""

import logging
import sys
from pathlib import Path

from config.config import LOG_FILE, LOG_NAME


def setup_logger(name: str = LOG_NAME, log_file: str = LOG_FILE) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
