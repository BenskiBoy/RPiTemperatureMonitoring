#!/usr/bin/python
import sys
import Adafruit_DHT
import json
import requests
import time

# For ip address and host
# https://www.raspberrypi.org/forums/viewtopic.php?t=79936
import socket
import os

gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()

api_token = 'API TOKEN'
api_url_base = 'API URL'

headers = {'Content-Type': 'application/json',
            'x-api-key': api_token,
            'ip_address': ipaddr,
            'host_device': host,
            'gateway': gateway}

api_submit_url = api_url_base + 'submit/'

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

headers['temperature'] = str(temperature)
headers['humidity'] = str(humidity)
headers['time'] = str(time.time())

response = requests.post(api_submit_url, headers=headers)