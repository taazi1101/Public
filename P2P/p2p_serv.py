import socket
import threading

def start_serv(sock,ip,port):
    sock.bind((ip,port))
    sock.listen()
    conn, addr = sock.accept()
    print("connection from: " + addr[0])
    return conn,addr

def start_conn(sock,ip,port):
    sock.connect((ip,port))
    return sock

def send(sock, data):
    sock.send(data)

def recv(sock):
    while True:
        data = sock.recv(1024)

def redirect(sock,sock_2):
    while True:
        try:
            data = sock.recv(1024)
            sock_2.send(data)
        except:
            return

ip = input("IP:")
while True:
    s = socket.socket()
    s_2 = socket.socket()

    s,addr = start_serv(s,ip,60001)
    s_2,addr2 = start_serv(s_2,ip,60002)

    threading.Thread(target=lambda:redirect(s,s_2)).start()
    threading.Thread(target=lambda:redirect(s_2,s)).start()