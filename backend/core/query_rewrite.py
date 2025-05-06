"""
core/query_rewrite.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    This module handles rewriting user queries using the AI to improve search quality.
    It takes a user's search query and interacts with the AI to provide a more refined or contextually relevant query for searching.
"""

from difflib import SequenceMatcher
from typing import Dict, List, Optional

from config.config import (MIN_RESULTS_DIFFERENCE, QUERY_REWRITE_STYLE_1,
                           QUERY_REWRITE_STYLE_2, QUERY_TEMPERATURE,
                           QUERY_TEMPERATURE_REFACT, SIMILARITY_THRESHOLD)
from core.assistant import ask_ai
from core.logger import setup_logger
from core.search import search

logger = setup_logger(__name__)


def get_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def build_messages(system_prompt: str, user_prompt: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Pregunta original: {user_prompt}"},
    ]


def generate_rewrite(prompt: str, user_prompt: str) -> list[dict]:
    rewrites = []

    for temp in QUERY_TEMPERATURE:
        try:
            messages = build_messages(prompt, user_prompt)
            rewrite = ask_ai(messages, temperature=temp).strip()

            if not rewrite or rewrite.lower() == user_prompt.lower():
                continue

            search_results = search(rewrite)
            rewrites.append(
                {
                    "rewrite": rewrite,
                    "result_count": len(search_results),
                    "temperature": temp,
                    "results": search_results[:3],
                }
            )

        except Exception as e:
            logger.error(f"Error con temperatura {temp}: {str(e)}")
            continue

    return rewrites


def select_best_rewrite(rewrites: List[Dict], original: str) -> str:
    if not rewrites:
        return original

    best_result = max(rewrites, key=lambda x: x["result_count"])

    best_balanced = max(
        rewrites,
        key=lambda x: (x["result_count"], -get_similarity(original, x["rewrite"])),
    )

    if (
        best_balanced["result_count"] - best_result["result_count"]
    ) >= MIN_RESULTS_DIFFERENCE:
        return best_balanced["rewrite"]
    return best_result["rewrite"]


def rewrite_query(user_prompt: str) -> str:
    if not user_prompt or not isinstance(user_prompt, str):
        return user_prompt

    all_rewrites = []
    prompts = [QUERY_REWRITE_STYLE_1, QUERY_REWRITE_STYLE_2]

    for style in prompts:
        for temp in QUERY_TEMPERATURE:
            rewrite_data = generate_rewrite(style, user_prompt, temp)
            if rewrite_data:
                all_rewrites.append(rewrite_data)

    style_groups = {}
    for rewrite in all_rewrites:
        style_groups.setdefault(rewrite["style"], []).append(rewrite)

    for style, group in style_groups.items():
        if len(group) >= 2:
            similarity = get_similarity(group[0]["rewrite"], group[1]["rewrite"])
            if similarity > SIMILARITY_THRESHOLD:
                refined = generate_rewrite(
                    prompts[style], user_prompt, QUERY_TEMPERATURE_REFACT
                )
                if refined:
                    all_rewrites.append(refined)

    return select_best_rewrite(all_rewrites, user_prompt)
