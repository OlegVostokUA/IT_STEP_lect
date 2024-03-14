import socket
import threading

hostname = socket.gethostbyname(socket.gethostname())
port = 9090

server = hostname, port

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def read_sock():
    while 1:
        data = client.recv(1024)
        print(data.decode('utf-8'))


alias = input('Enter you name: ')
client.bind((hostname, port))
client.sendto((alias + ' Connect to server').encode('utf-8'), server)

thr = threading.Thread(target=read_sock)
thr.start()

while 1:
    msg = input()
    client.sendto((f' [ {alias} ] {msg.encode("utf-8")}'), server)



