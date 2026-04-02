#!/usr/bin/env python3
"""
Aria main entrypoint — now with Kairos daemon + autoDream memory
100% leaked architecture complete
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import typer
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

from constants import constants
from buddy import show_buddy
from commands import handle_command
from query import ask_aria
from memdir import memory, start_kairos   # ← Leaked Kairos + memory

load_dotenv()

app = typer.Typer(name="aria", help="Aria — open-source AI terminal agent", add_completion=False)
console = Console()

@app.command()
def start(
    model: str = typer.Option(None, "--model", "-m", help="Override default model"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug mode"),
):
    console.print(
        Panel(
            f"[bold cyan]🚀 {constants.APP_NAME} v{constants.VERSION} started[/]\n"
            f"Model: [green]{model or constants.DEFAULT_MODEL}[/]\n"
            f"Kairos daemon: {'[green]ENABLED[/]' if constants.FEATURE_FLAGS.ENABLE_KAIROS else '[red]OFF[/]'}\n"
            f"Buddy pet: {'[green]ENABLED[/]' if constants.FEATURE_FLAGS.ENABLE_BUDDY else '[red]OFF[/]'}\n"
            f"autoDream memory: {'[green]ENABLED[/]' if constants.FEATURE_FLAGS.ENABLE_AUTODREAM else '[red]OFF[/]'}\n"
            f"Coordinator swarm: {'[green]ENABLED[/]' if constants.FEATURE_FLAGS.ENABLE_COORDINATOR else '[red]OFF[/]'}",
            title=f"{constants.APP_NAME} — Ready",
            border_style="cyan",
        )
    )

    show_buddy()
    start_kairos()   # ← Kairos daemon starts here (leaked behavior)

    console.print("\n[bold green]Aria is FULLY ALIVE with Kairos + autoDream memory![/]")
    console.print("[dim]Press Ctrl+C to exit[/]")

    while True:
        try:
            user_input = input("\nYou > ").strip()
            if not user_input:
                continue

            if user_input.startswith("/"):
                response = handle_command(user_input)
                if response:
                    console.print(f"[cyan]Aria:[/] {response}")
            else:
                # autoDream memory (leaked self-healing)
                memory.add("user", user_input)
                console.print("[cyan]Aria:[/] Thinking...")
                answer = ask_aria(user_input)
                console.print(f"[cyan]Aria:[/] {answer}")
                memory.add("aria", answer)

        except KeyboardInterrupt:
            console.print("\n[bold red]Goodbye! Aria shutting down.[/]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/]")

@app.command()
def version():
    console.print(f"[bold]{constants.APP_NAME}[/] version {constants.VERSION}")

if __name__ == "__main__":
    app()