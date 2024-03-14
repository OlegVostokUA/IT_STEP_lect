import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostbyname(socket.gethostname())
port = 9090

server.bind((hostname, port))
#server.listen(5)

clients = []

print('Start server')

while 1:
    data, addres = server.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in clients:
        clients.append(addres)

    for cl in clients:
        if cl == addres:
            continue
        server.sendto(data, cl)
