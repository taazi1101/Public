import socket
import time
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

def redirect(sock,sock_2,addr,addr2):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                return
            try:
                with open(f"LOG{addr[0]}-.log","ab") as fil:
                    t = time.localtime()
                    current_time = time.strftime("%D:H:%M:%S", t)
                    bss = f"{current_time} | From <{addr[0]}> | To <{addr2[0]}> : "
                    fil.write(bss.encode())
                    fil.write(data)
            except:
                print("Error logging")
                pass
            sock_2.send(data)
        except:
            return

ip = input("IP:")
while True:
    s = socket.socket()
    s_2 = socket.socket()

    s,addr = start_serv(s,ip,60001)
    s_2,addr2 = start_serv(s_2,ip,60002)

    threading.Thread(target=lambda:redirect(s,s_2,addr,addr2)).start()
    threading.Thread(target=lambda:redirect(s_2,s,addr2,addr)).start()
