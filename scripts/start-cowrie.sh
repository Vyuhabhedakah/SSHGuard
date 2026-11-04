#!/bin/bash
set -e
cd /home/cowrie/sshguard
source cowrie-env/bin/activate
cowrie start
echo "[+] Cowrie started on port 2222"
