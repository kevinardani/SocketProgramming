from socket import socket, AF_INET, SOCK_DGRAM

MAX_SIZE = 4096 
PORT = 12345

if __name__== '_main_':
    sock = socket(AF_INET,SOCK_DGRAM)
    msg = "Hello UDP Server"
    sock.sendto(msg.encode(), ('',PORT))
    data, addr = sock.recvfrom(MAX_SIZE)
    print("server says:")
    print(repr(data))