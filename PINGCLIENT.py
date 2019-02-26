# Author：Chang.
import socket
import time

server_address  = ('localhost', 12222)

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
server ="('127.0.0.1', 12222)"
print("\nStart PING socket ......\n")

for i in range(10):
    start_time=time.time()
    start = round(start_time * 1000)
    message ='PING %d %s \r\n.'%(i,time.ctime(start_time))
    try:
        send =sock.sendto(message,server_address)
        data,server_add = sock.recvfrom(12222)
        end =round((time.time()*1000))
        print('ping to %s, seq = %d,rtt = %d ms'%(server_add,i,(end-start)))
    except socket.timeout:
        print('ping to %s, seq = %d,time out ms'%(server,i))

print('\n Closing!\n')
sock.close()
