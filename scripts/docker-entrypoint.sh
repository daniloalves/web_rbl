#!/bin/sh
set -e

/usr/sbin/dnsmasq -C /etc/dnsmasq.conf &
cd /usr/src/app
python3 ./http_server.py -p 8000