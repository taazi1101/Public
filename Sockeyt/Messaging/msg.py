from time import sleep
import threading
import socket
import sys

port = 12346
print("Suggested ip: " + socket.gethostbyname(socket.gethostname()))
mode = input("1:Connect 2:Listen :")
ip = input("IP:")
s = socket.socket()


def recive(sock):
    while True:
        data = sock.recv(1024)
        print("[+] " + data.decode())

if mode == "2":
    s.bind((ip,port))
    s.listen()
    conn, addr = s.accept()
    threading.Thread(target=lambda:recive(conn)).start()
    while True:
        msg = input()
        conn.send(msg.encode())

elif mode == "1":
    s.connect((ip,port))
    threading.Thread(target=lambda:recive(s)).start()
    while True:
        msg = input()
        s.send(msg.encode())
