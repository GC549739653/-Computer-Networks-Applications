# Author：Chang.
import socket

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ServerHost = '127.0.0.1'

serverPort=12000
serverSocket.bind((ServerHost, serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr =serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata= f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        connectionSocket.close()

serverSocket.close()