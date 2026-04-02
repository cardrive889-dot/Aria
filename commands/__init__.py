"""
Aria Slash Commands — final version with all leaked tools
"""

from buddy import load_buddy, save_buddy, show_buddy
from constants import constants
from tools import AVAILABLE_TOOLS
from rich.console import Console
console = Console()

def handle_command(command: str) -> str:
    cmd = command.strip().lower()

    if cmd == "/help":
        return (
            "Aria Slash Commands (full leaked style):\n"
            "/help          → Show this\n"
            "/buddy status  → Show pet\n"
            "/buddy feed    → Reduce hunger\n"
            "/buddy play    → Increase happiness\n"
            "/tool ls       → List files\n"
            "/tool echo [text] → Repeat text\n"
            "/tool read [file] → Read file\n"
            "/tool git      → Git status\n"
            "/version       → Show version\n"
            "Just talk normally for LLM chat!"
        )

    elif cmd.startswith("/buddy"):
        parts = cmd.split()
        state = load_buddy()
        if len(parts) > 1:
            action = parts[1]
            if action == "feed":
                state.hunger = max(0, state.hunger - 30)
                console.print("[green]🍎 Buddy ate! Hunger down.[/]")
            elif action == "play":
                state.happiness = min(100, state.happiness + 25)
                console.print("[green]❤️  Buddy played! Happiness up.[/]")
            elif action == "talk":
                console.print("[yellow]Buddy:[/] Hi! I'm feeling great today! 🐾")
            elif action == "status":
                pass
        show_buddy()
        save_buddy(state)
        return ""

    elif cmd.startswith("/tool "):
        tool_name = cmd.split()[1]
        args = " ".join(cmd.split()[2:]) if len(cmd.split()) > 2 else "."
        if tool_name in ["ls", "echo", "read", "git"]:
            tool_func = AVAILABLE_TOOLS.get(f"/tool {tool_name}")
            if tool_func:
                return tool_func(args)
        return "Unknown tool. Try /tool ls or /tool git"

    elif cmd == "/version":
        return f"Aria v{constants.VERSION}"

    return f"Unknown command: {cmd}  (try /help)"