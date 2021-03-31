import socket

s = socket.socket()
host = input("IP:")
port = int(input("Port:"))

s.connect((host, port))
while True:
    command = input("[=]:")
    s.send(command.encode())
    inp = s.recv(4096)
    try:
        print(inp.decode())
    except:
        print(inp)
        pass
