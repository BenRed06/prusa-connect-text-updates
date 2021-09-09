import time
import requests
import json


#PRINTER_IP/api/telemetry

res = requests.get('YOUR_PRINTERS_IP')


stuff = res.json()

while True:
    time.sleep(60.0)
    print(stuff)
