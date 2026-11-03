#!/usr/bin/env python3

import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
LOG = BASE / "var/log/cowrie/cowrie.json"
ALERTS = BASE / "alerts.jsonl"

EVENTS = {
    "cowrie.session.connect": "NEW CONNECTION",
    "cowrie.login.failed": "FAILED LOGIN",
    "cowrie.login.success": "HONEYPOT LOGIN ACCEPTED",
    "cowrie.command.input": "COMMAND ENTERED",
    "cowrie.session.closed": "SESSION CLOSED",
}


def process_event(event):
    if not isinstance(event, dict):
        return

    event_id = event.get("eventid")
    if event_id not in EVENTS:
        return

    alert = {
        "timestamp": event.get("timestamp"),
        "alert": EVENTS[event_id],
        "source_ip": event.get("src_ip", "unknown"),
        "session": event.get("session"),
    }

    # Deliberately exclude passwords from the alert copy.
    if "username" in event:
        alert["username"] = event["username"]

    if event_id == "cowrie.command.input":
        alert["command"] = event.get("input", "")

    # JSON encoding escapes control characters from untrusted input.
    text = json.dumps(alert, ensure_ascii=True)
    print(text, flush=True)

    with ALERTS.open("a", encoding="utf-8") as output:
        output.write(text + "\n")


def main():
    print(f"SSHGuard monitoring: {LOG}", flush=True)
    print("Waiting for new events. Press Ctrl+C to stop.", flush=True)

    # Ubuntu's tail -F follows the filename across log rotation.
    follower = subprocess.Popen(
        ["tail", "-n", "0", "-F", str(LOG)],
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    try:
        for line in follower.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            process_event(event)
    except KeyboardInterrupt:
        pass
    finally:
        follower.terminate()
        follower.wait()


if __name__ == "__main__":
    main()
