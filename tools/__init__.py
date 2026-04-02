"""
Aria Tools — FINAL version (100% leaked tools/ + fixes)
"""

import os
import subprocess
from pathlib import Path
from rich.console import Console
console = Console()

def tool_ls(path: str = ".") -> str:
    try:
        items = os.listdir(path)
        return "📁 " + "\n📁 ".join(items[:30]) + ("\n...and more" if len(items) > 30 else "")
    except Exception as e:
        return f"Error: {e}"

def tool_echo(text: str) -> str:
    return text

def tool_read_file(filepath: str) -> str:
    try:
        p = Path(filepath)
        if p.exists() and p.is_file():
            content = p.read_text(encoding="utf-8")
            return content[:800] + ("\n...truncated" if len(content) > 800 else "")
        return "File not found."
    except Exception as e:
        return f"Error: {e}"

def tool_git_status(_args: str = "") -> str:   # ← FIXED: accepts argument
    try:
        result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, timeout=5)
        return result.stdout.strip() if result.stdout else "No changes or not a git repo."
    except:
        return "Git not available or not a git repository."

AVAILABLE_TOOLS = {
    "/tool ls": tool_ls,
    "/tool echo": tool_echo,
    "/tool read": tool_read_file,
    "/tool git": tool_git_status,
}