import argparse,socket
from datetime import datetime

MAX_BYTES = 65535

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES) # Danger !
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

if __name__ == '_main_':
    parser = argparse.ArgumentParser(description='Client UDP lokal')
    parser.add_argument('-p',metavar='PORT', type=int, default=1060,
                        help ='UDP port (default 1060)')
    args = parser.parse_args()
    client(args.p)