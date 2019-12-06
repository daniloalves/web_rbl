#!/bin/bash
## Dev environment
#yum install -y net-tools bind-utils
###
## Requirement to production
yum install -y dnsmasq 
echo "resolv-file=/etc/resolv.dnsmasq" >> /etc/dnsmasq.conf
echo "no-poll" >> /etc/dnsmasq.conf
echo "listen-address=127.0.0.1" >> /etc/dnsmasq.conf
echo "cache-size=1000" >> /etc/dnsmasq.conf
echo "nameserver 8.8.8.8" > /etc/resolv.dnsmasq
echo "nameserver 127.0.0.1" > /etc/resolv.conf
#netstat -ntlp | grep :53
###