"""
core/query_rewrite.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-23
Description:
    This module handles rewriting user queries using the AI to improve search quality.
    It takes a user's search query and interacts with the AI to provide a more refined or contextually relevant query for searching.
"""

from difflib import SequenceMatcher
from core.assistant import ask_ai
from config.config import QUERY_REWRITE_STYLE_1, QUERY_REWRITE_STYLE_2, QUERY_TEMPERATURE, QUERY_TEMPERATURE_REFACT
from core.search import search

def get_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def build_messages(prompt: str, user_prompt: str):
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Original question: {user_prompt}"}
    ]

def rewrite_query(user_prompt: str) -> str:
    rewrites = []
    prompts = [QUERY_REWRITE_STYLE_1, QUERY_REWRITE_STYLE_2]

    for style_idx, prompt in enumerate(prompts):
        for temp in QUERY_TEMPERATURE:
            messages = build_messages(prompt, user_prompt)
            try:
                rewrite = ask_ai(messages, temperature=temp).strip()
                result = search(rewrite)
                rewrites.append({
                    "style": style_idx,
                    "prompt": prompt,
                    "temperature": temp,
                    "rewrite": rewrite,
                    "result": result
                })
            except Exception as e:
                print(f"Error rewriting with style {style_idx}, temp {temp}: {e}")

    # Extra refinement if two versions are very similar
    similarities = []
    for i in range(0, len(rewrites) - 1, 2):
        sim = get_similarity(rewrites[i]["rewrite"], rewrites[i + 1]["rewrite"])
        similarities.append({"style": i // 2, "similarity": sim})

    for sim_data in similarities:
        if sim_data["similarity"] > 0.9:
            style_idx = sim_data["style"]
            prompt = prompts[style_idx]
            messages = build_messages(prompt, user_prompt)
            try:
                rewrite = ask_ai(messages, temperature=QUERY_TEMPERATURE_REFACT).strip()
                result = search(rewrite)
                rewrites.append({
                    "style": style_idx,
                    "prompt": prompt,
                    "temperature": QUERY_TEMPERATURE_REFACT,
                    "rewrite": rewrite,
                    "result": result
                })
            except Exception as e:
                print(f"Error in refinement for style {style_idx}: {e}")

    if not rewrites:
        return user_prompt

    best = max(rewrites, key=lambda r: len(r["result"]))
    return best["rewrite"]
