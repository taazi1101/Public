import requests
import sys
import time
import datetime
from socket import gethostbyname
from datetime import date

sys.argv.pop(0)

if "-h" in sys.argv:
    print("Add time zones as arguments\nFormat: Area/Location/region\nExamples: europe/heslinki America/Argentina/Salta\nMore help at: http://worldtimeapi.org")
    exit()

def get(zone):
    if zone.startswith("ip"):
        try:
            splitted = zone.split("/")
            ip = zone.replace(splitted[len(splitted)-1],gethostbyname(splitted[len(splitted)-1]))
        except:
            ip = zone
        try:
            return requests.get("http://worldtimeapi.org/api/" + ip).json()
        except:
            return "Error"
    else:
        try:
            return requests.get("http://worldtimeapi.org/api/timezone/" + zone).json()
        except:
            return "Error"

t = time.localtime()
sys_time = str(date.today()) + "--" + time.strftime("%H:%M:%S", t)
print("System time: " + sys_time)
try:
    ipb = dict(requests.get("http://worldtimeapi.org/api/ip").json()).get("datetime")
    ipbl = ipb.split(".")
    print("Ip based time: " + ipbl[0].replace("T","--"))
except:
    print("Failed to grap ip based time")
for arg in sys.argv:
    resp = dict(get(arg))
    retime = str(resp.get("datetime"))
    splitt = retime.split(".")[0]
    print(resp.get("timezone") + ": " + splitt.replace("T","--"))