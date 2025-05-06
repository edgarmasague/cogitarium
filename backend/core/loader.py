"""
core/loader.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Load and process markdown files from a directory
"""

import os

from core.logger import setup_logger

logger = setup_logger(__name__)


def load_all_files(folder_path="data"):
    """
    Loads and concatenates all .md files within the specified folder.

    Args:
        folder_path (str): Path for the folder containing Markdown files.

    Returns:
        str: Conbined content of all files with separators and filenames.
    """
    content = ""
    # Ensure the folder_path is a string
    if not isinstance(folder_path, str):
        raise TypeError("folder_path must be a string.")

    # Check if the folder exists
    if not os.path.exists(folder_path):
        raise ValueError(f"Folder '{folder_path}' does not exist.")

    if not os.path.isdir(folder_path):
        raise ValueError(f"'{folder_path}' is not a directory.")

    # If exists get all files within the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                    file_content = f.read()
                    # Add separator and filename header
                content += f"\n---\n # {filename}\n{file_content}\n"
            except Exception as e:
                logger.error(f"Error reading {filename}: {str(e)}", exc_info=True)

    return content
