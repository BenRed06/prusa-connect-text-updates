import time
import requests
import json

#192.168.1.253/api/telemetry


#{"temp_nozzle":24,"temp_bed":24,"material":"PLA","pos_z_mm":0.00,"printing_speed":100,"flow_factor":100}
res = requests.get('http://192.168.1.253/api/telemetery')
stats = res.text
print(stats)







#information
name = 'Prusa Mini' #put your printers name here (it can be anything)
ip = "192.168.1.253" #put the IP of the printer here, it is purely cosmic but if your managing many printers having the IP visible may be beneficial
wait = 10 #set this to how often you want to be notified of the status. MUST BE a decimal: example: 1.0 or 3.6, (it is in seconds)
tz = [] #set this as your time zone



#DO NOT TOUCH
hotend = []
bed = []
ete = []
percent = []
material = []





#res = requests.get('ip'+ uri)


#stuff = res.json()

#{"temp_nozzle":240,"temp_bed":85,"material":"PETG","pos_z_mm":0.22,"printing_speed":100,"flow_factor":95,"progress":0,"print_dur":"      2m 54s","time_est":"6240","time_zone":"-4","project_name":"cam mount.gcode"}

while True:
    print("Connected To: " + name) #name of printer
    print("Ip: " + ip)
    print("material:" + temp_nozzle)
    print("Hotend Temp:") #hotend temp
    print("Bed Temp:") #bed temp
    print("Est Till Done:") #estimated time till done
    print("Percent Done:") #percentage done
    print("---------------------")
    time.sleep(wait)


