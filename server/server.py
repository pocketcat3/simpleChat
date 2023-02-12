import socket
import os
os.system("cls")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())
sock.bind ((ip,50))
client = []
print ('сервер ввімкнений')
print("ip вашої туси " + socket.gethostbyname(socket.gethostname()))
while True:
    data, addres = sock.recvfrom(1024)
    print (addres[0], addres[1])
    if addres not in client:
        client.append(addres)
    for clients in client:
        if clients == addres:
            continue
        sock.sendto(data,clients)