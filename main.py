import time
#import requests
import json


#192.168.1.253/api/telemetry



#information
name = Prusa Mini #put your printers name here (it can be anything)
ip = YOUR_PRINTER_IP_HERE #put the IP of the printer here
wait = 20 #set this as a decimal: example: 1.0 or 3.6, (it is in seconds)






#res = requests.get('http://162.168.1.253'+ uri)


#stuff = res.json()




while True:
    print(name)
    print(ip)
    time.sleep(wait)

