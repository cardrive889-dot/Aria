"""
Aria autoDream Memory + Kairos Daemon — final fixed version
"""

import time
import threading
from pathlib import Path
from datetime import datetime
from rich.console import Console
console = Console()

MEMORY_FILE = Path("aria_memory.json")

class Memory:
    def __init__(self):
        self.history = []
        self.load()

    def load(self):
        if MEMORY_FILE.exists():
            try:
                import json
                self.history = json.loads(MEMORY_FILE.read_text())
            except:
                self.history = []

    def save(self):
        import json
        MEMORY_FILE.write_text(json.dumps(self.history[-50:], indent=2))

    def add(self, role: str, content: str):
        self.history.append({"time": datetime.now().isoformat(), "role": role, "content": content})
        self.save()

    def get_context(self) -> str:
        return "\n".join([f"{h['role']}: {h['content']}" for h in self.history[-10:]])

memory = Memory()

def kairos_daemon():
    time.sleep(3)  # small delay so welcome message finishes first
    console.print("[dim]🔥 Kairos daemon started (proactive mode)[/]")
    while True:
        time.sleep(60)
        try:
            console.print("\n[bold yellow]🔥 Kairos: I noticed the folder is quiet. Anything I can help with?[/]")
            console.print("[dim]Type anything to continue...[/]")
        except:
            break

def start_kairos():
    thread = threading.Thread(target=kairos_daemon, daemon=True)
    thread.start()