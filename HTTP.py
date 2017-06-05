from socket import *

HOST = '202.114.200.243'
PORT = 80
ADDR = (HOST,PORT)

data='GET /net HTTP/1.1\r\nAccept-Encoding: identity\r\nHost:http://cugrobot.cug.edu.cn:8188/indexi1.html\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send(data)
datanew=tcpCliSock.recv(1024)
print datanew
tcpCliSock.close()
