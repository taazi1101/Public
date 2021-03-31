import subprocess
import os

print("w:Windows u:Unix")
oss = input("os:")
ip = input("Ip:")
port = input("Port:")
if oss == "w":
    os.system(f"./start_win {ip}, {port}")
elif oss == "u":
    os.system(f"./start_linux {ip}, {port}")
else:
    print("Invalid input")

#subprocess.run(["./start_win", ip, port])
