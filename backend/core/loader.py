"""
core/loader.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-21
Description:
    This module loads all files (e.g., text files or documents) that are used for context in the AI interactions.
"""

import os

def load_all_files(folder_path="data"):
    """
        Loads and concatenates all .md files within the specified folder.

        Args:
            folder_path (str): Path for the folder containing Markdown files.
            
        Returns:
            str: Conbined content of all files with separators and filenames.
    """
    content = ""

    #Ensure the folder_path is a string
    if not isinstance(folder_path, str):
        raise TypeError("folder_path must be a string.")
    
    #Check if the folder exists
    if not os.path.exists(folder_path):
        return content
    
    #If exists get all files within the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    file_content = f.read()
                    #Add separator and filename header
                content += f"\n---\n # {filename}\n{file_content}\n"
            except Exception as e:
                break
    return content