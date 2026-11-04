
#!/bin/bash
set -e

echo "[+] Installing SSHGuard dependencies..."

sudo apt update
sudo apt install -y \
    python3 python3-pip python3-venv \
    python3-dev build-essential \
    libssl-dev libffi-dev \
    git openssh-client

echo "[+] Creating Cowrie user..."

if ! id cowrie >/dev/null 2>&1; then
    sudo adduser --disabled-password --gecos "" cowrie
fi

echo "[+] Setting up Cowrie environment..."

sudo -u cowrie bash <<'EOF'
cd /home/cowrie

mkdir -p sshguard
cd sshguard

python3 -m venv cowrie-env
source cowrie-env/bin/activate

python -m pip install --upgrade pip
python -m pip install cowrie

cowrie init
EOF

echo "[+] SSHGuard installation completed!"
echo "[+] Configure Cowrie before starting it."
