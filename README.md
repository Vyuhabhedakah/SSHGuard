# SSHGuard

SSHGuard is a Linux cybersecurity project that uses Cowrie
to simulate an SSH server and monitor connection activity.

## Features

- Monitors SSH connection attempts
- Records successful and failed honeypot logins
- Displays commands entered in the simulated shell
- Stores selected alerts in JSON Lines format

## Technologies

- Ubuntu Linux
- Cowrie Honeypot
- Python 3
- SSH
- Linux networking

## Architecture

Testing machine → Cowrie SSH honeypot → JSON logs
→ Python monitor → Security alerts

## Project status

Lab implementation and testing are in progress.

## Security

Run the honeypot in an isolated lab. Do not upload
logs, passwords, SSH keys, tokens, or downloaded samples.
