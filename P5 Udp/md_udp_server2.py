import argparse
import socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))

        if text == 'REQUEST_TIME':
            current_time = 'Current time: {}'.format(datetime.now())
            data = current_time.encode('ascii')
            sock.sendto(data, address)
        else:
            error_message = 'Unknown request'
            sock.sendto(error_message.encode('ascii'), address)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP server that provides current time')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,help='UDP port (default 1060)')
    args = parser.parse_args()
    server(args.p)
