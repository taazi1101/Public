import subprocess
import socket
import platform
import os

if platform.system() == "Windows":
    startcmd = "ping -n 1"
else:
    startcmd = "ping -c 1"
print(f"Using {startcmd}")

if len(os.sys.argv) < 2:
    print("Syntax = IP.f\nExample: 192.168.1.f")
    exit()
succes = []
ip = str(os.sys.argv[1])
for i in range(0, 256):
    cmd = f"{startcmd} {ip}".replace("f", str(i))
    rpcs = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = rpcs.stdout.read()
    if b"Average" in out or b"ttl" in out:
        tip = ip.replace("f", str(i))
        try:
            print(socket.gethostbyaddr(tip))
        except:
            print(tip)
            pass
    else:
        if "-v" in os.sys.argv:
            print(i)
