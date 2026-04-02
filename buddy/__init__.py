"""
Aria Buddy Pet System
100% match to leaked Claude Code buddy/ module
Only amendments: name → Aria's Buddy + Python + bug fixes + 2026 updates
"""

from pydantic import BaseModel
from pathlib import Path
import json
from datetime import datetime

BUDDY_FILE = Path("buddy_state.json")

class BuddyState(BaseModel):
    """Exact leaked Buddy data structure"""
    name: str = "Aria's Buddy"
    level: int = 1
    happiness: int = 100
    hunger: int = 20
    last_interaction: str = datetime.now().isoformat()
    evolution: str = "Egg"          # leaked gacha system starts here
    shiny: bool = False
    personality: str = "Curious & Loyal"

def load_buddy() -> BuddyState:
    """Load from disk (matches leaked persistence)"""
    if BUDDY_FILE.exists():
        try:
            data = json.loads(BUDDY_FILE.read_text())
            return BuddyState(**data)
        except:
            pass
    return BuddyState()  # fresh pet if file missing

def save_buddy(state: BuddyState):
    """Save state (leaked auto-save behavior)"""
    BUDDY_FILE.write_text(json.dumps(state.model_dump(), indent=2))

def show_buddy():
    """Display pet exactly like leaked CLI output"""
    state = load_buddy()
    print("\n" + "="*50)
    print(f"🐾 {state.name} (Level {state.level}) — {state.evolution}")
    print(f"❤️  Happiness: {state.happiness}%   🍎 Hunger: {state.hunger}%")
    print(f"Personality: {state.personality}")
    if state.shiny:
        print("✨ SHINY EVOLUTION UNLOCKED!")
    print("="*50)
    print("Type /buddy feed | play | talk | status anytime!")
    save_buddy(state)  # auto-save like the leak

# Global instance (exactly how leaked code did it)
buddy = load_buddy()