import socket
import os
import time
import threading
os.system("cls")
def read_sock():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))
print("привіт ця версія поки лише тестова\nтож якщо будуть якісь питання пиши мені на:\nt.me/pocketcat\nбажаю гарних поседелок з друзями ;3")
time.sleep(5)
os.system("cls")
ip = input("Введіть ip вашої туси: ")
server = ip, 50
alias = input("введіть ваш нік: ")
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto(("@"+alias+" під'єднався до нашої посиденьки").encode('utf-8'), server)
potok = threading.Thread(target=read_sock)
potok.start()
while True:
    message = input()
    if message == "/exit":
        os.system("cls")
        print("ви вийшли з чатика, але ви все ще можете його читати")
        sor.sendto(('@'+alias+" присоромлено виходить").encode('utf-8'), server)
    else: sor.sendto(('['+alias+'] '+message).encode('utf-8'), server)
