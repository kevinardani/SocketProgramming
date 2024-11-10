import argparse
import socket

MAX_BYTES = 65535

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    request = 'REQUEST_TIME'
    sock.sendto(request.encode('ascii'), ('127.0.0.1', port))
    print('Meminta waktu sekarang ke server...')
    
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied: {}'.format(address, text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP client meminta waktu sekarang ke server')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,help='UDP port (default 1060)')
    args = parser.parse_args()
    client(args.p)
