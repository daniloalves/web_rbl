# -*- encoding: utf-8 -*-

import socket
import sys
import json
import os
from commons import log

URI = 'dnsbl.httpbl.org'
TOKEN = ''
if 'DNSBL_TOKEN' in os.environ:
    TOKEN = os.environ['DNSBL_TOKEN']
THREAT = {0:'Search Engine',1:'Suspicious',2:'Harvester',4:'Comment Spammer'}

def query(reverse_ip):
    try:
        reverse_dns = f"{TOKEN}.{reverse_ip}.{URI}"
        addr1 = socket.gethostbyname(reverse_dns)
        return analyse(addr1)
    except socket.gaierror as e:
        log(f'IP not found! Sound Good!','debug')
        return analyse('127.0.0.0')
    except Exception as e:
        log(f'{e}','error')

def analyse(return_ip):
    status_ip = return_ip.split('.')[-1]
    status_name = THREAT[int(status_ip)]
    sugestion = 'nil'
    if int(status_ip) > 0:
        sugestion = 'Block'
    else:
        sugestion = 'Pass'
    response = f'IP: {return_ip} || Status: {status_name} || Sugestion: {sugestion}'
    response = '{"info":{"IP":"%s","Status":"%s","Sugestion":"%s"} }'%(return_ip,status_name,sugestion)
    print(response)
    return response

def help(script_name='script.py'):
    print('You need put a IP (eq.):')
    print(f'$ {script_name} 1.2.3.4')
    exit()

def main(ip):
    try:
        reverse_ip = ip.split('.')
        response = json.loads(query(f"{reverse_ip[3]}.{reverse_ip[2]}.{reverse_ip[1]}.{reverse_ip[0]}"))
        response['info']['IP'] = ip
        return response
    except Exception as e:
        log(e,'error')
        log(f'Try split to reverse: {ip}', 'error')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help(sys.argv[0])
    ip = sys.argv[1]
    main(ip)