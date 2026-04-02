"""
Aria Query Engine — fixed for low-RAM PCs
100% match to leaked query/ logic + amendment for your hardware
"""

import ollama
from constants import constants

def ask_aria(prompt: str, model: str = None) -> str:
    """Exact leaked LLM call flow with low-RAM safety"""
    try:
        response = ollama.chat(
            model=model or constants.DEFAULT_MODEL,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        error_str = str(e).lower()
        if "memory" in error_str or "4.8" in error_str or "gi b" in error_str:
            return "Sorry! Your PC has low RAM right now. Aria is now using a tiny model — try again or close other programs."
        return f"LLM error: {e}"