import sys
import urllib.request
import urllib.error
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: GitHub user '{username}' not found.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
    return None

def format_event(event):
    type = event["type"]
    repo = event["repo"]["name"]

    if type == "PushEvent":
        count = len(event["payload"]["commits"])
        return f"Pushed {count} commit(s) to {repo}"
    elif type == "IssuesEvent":
        action = event["payload"]["action"]
        return f"{action.capitalize()} an issue in {repo}"
    elif type == "WatchEvent":
        return f"Starred {repo}"
    elif type == "ForkEvent":
        return f"Forked {repo}"
    elif type == "CreateEvent":
        ref_type = event["payload"].get("ref_type", "repository")
        return f"Created a new {ref_type} in {repo}"
    else:
        return f"{type} in {repo}"

def display_activity(username):
    events = fetch_github_activity(username)
    if not events:
        print(f"No recent public activity found for '{username}'.")
        return

    print(f"\nRecent activity for GitHub user: {username}")
    print("-" * 50)
    for i, event in enumerate(events[:10], start=1):
        print(f"{i}. {format_event(event)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <github_username>")
    else:
        display_activity(sys.argv[1])
