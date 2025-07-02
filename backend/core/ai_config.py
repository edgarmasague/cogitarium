"""
core/ai_config.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This module initializes the AI client configuration based on environment settings.
    It handles the creation of AI clients for different platforms such as OpenAI, Azure, and Ollama.
"""

import os

import azure.identity
import openai
from dotenv import load_dotenv

load_dotenv(override=True)


def get_ai_client():
    """
    Create and returns an AI Client and selected model name based on the API_HOST settings.

    Supported platforms:
        - Azure OpenAI
        - Ollama (local models)
        - Github-hosted moels via Azure
        - OpenAI

    Args:
        None

    Returns:
        tuple: (AI client instance, model name as string)
    """
    API_HOST = os.getenv("API_HOST", "github")

    if API_HOST == "azure":
        # Use Azure credentials to authenticate and create client
        token_provider = azure.identity.get_bearer_token_provider(
            azure.identity.DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default",
        )
        client = openai.AzureOpenAI(
            api_version=os.environ["AZURE_OPENAI_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            azure_ad_token_provider=token_provider,
        )
        model = os.environ["AZURE_OPENAI_DEPLOYMENT"]

    elif API_HOST == "ollama":
        # Use Ollama for local inference
        client = openai.OpenAI(
            base_url=os.environ["OLLAMA_ENDPOINT"], api_key="nokeyneeded"
        )
        model = os.environ["OLLAMA_MODEL"]

    elif API_HOST == "github":
        # Use GitHub-hosted model via Azure's inference endpoint
        client = openai.OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.environ["GITHUB_TOKEN"],
        )
        model = os.getenv("GITHUB_MODEL", "gpt-4o")

    else:
        # Default to OpenAI's API
        client = openai.OpenAI(api_key=os.environ["OPENAI_KEY"])
        model = os.environ["OPENAI_MODEL"]

    return client, model
