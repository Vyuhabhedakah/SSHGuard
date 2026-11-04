#!/bin/bash
sudo -u cowrie bash -c '
cd /home/cowrie/sshguard
source cowrie-env/bin/activate
cowrie stop
'
