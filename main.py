import time
#import requests
import json


#192.168.1.253/api/telemetry



#information
name = 'Prusa Mini' #put your printers name here (it can be anything)
ip = "192.168.1.253" #put the IP of the printer here
wait = 5 #set this as a decimal: example: 1.0 or 3.6, (it is in seconds)



#DO NOT TOUCH
hotend = []
bed = []
ete = []
percent = []




#res = requests.get('http://162.168.1.253'+ uri)


#stuff = res.json()




while True:
    print("stats on: " + name) #name of printer
    print("ip: " + ip)
    print("hotend temp:") #hotend temp
    print("bed temp:") #bed temp
    print("est till done:") #estimated time till done
    print("percent done:") #percentage done
    print("---------------------")
    time.sleep(wait)

