import sys
import urllib.request
import urllib.error
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            console.print(f"[bold red]❌ Error:[/] GitHub user '{username}' not found.")
        else:
            console.print(f"[bold red]❌ HTTP Error:[/] {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        console.print(f"[bold red]🌐 Network Error:[/] {e.reason}")
    return None


def format_event(event):
    type = event["type"]
    repo = event["repo"]["name"]

    if type == "PushEvent":
        count = len(event["payload"]["commits"])
        return f"🚀 Pushed {count} commit(s) to [cyan]{repo}[/]"
    elif type == "IssuesEvent":
        action = event["payload"]["action"]
        return f"🐛 {action.capitalize()} an issue in [cyan]{repo}[/]"
    elif type == "WatchEvent":
        return f"⭐ Starred [cyan]{repo}[/]"
    elif type == "ForkEvent":
        return f"🍴 Forked [cyan]{repo}[/]"
    elif type == "CreateEvent":
        ref_type = event["payload"].get("ref_type", "repository")
        return f"✨ Created a new {ref_type} in [cyan]{repo}[/]"
    else:
        return f"🔍 {type} in [cyan]{repo}[/]"


def display_activity(username):
    events = fetch_github_activity(username)
    if not events:
        return

    if len(events) == 0:
        console.print(f"[yellow]No recent public activity found for '{username}'.[/]")
        return

    table = Table(
        title=f"📊 GitHub Activity for [bold cyan]{username}[/]",
        box=box.ROUNDED,
        title_justify="center",
        expand=False,
        padding=(0, 1),
        border_style="bright_blue",
    )
    table.add_column("#", style="dim", justify="right")
    table.add_column("Activity", style="bold green")

    for i, event in enumerate(events[:10], 1):
        table.add_row(str(i), format_event(event))

    console.print(
        Panel.fit(
            table,
            title="gitlog-cli",
            subtitle="🧰 Terminal GitHub Activity Tracker",
            border_style="magenta",
            padding=(1, 2),
        )
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        console.print("[bold yellow]Usage:[/] python gitlog_cli.py <github_username>")
    else:
        display_activity(sys.argv[1])
