import socket

s = socket.socket()
port = 60001
host = input("IP:")

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
