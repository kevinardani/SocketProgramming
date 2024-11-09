import argparse
import socket
import time

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}' .format(sock.getsockname))
    
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))

        #Mengambil waktu saat ini
        current_time = time.ctime() 
        response_text = f'The current time is: {current_time}'
        response_data = response_text.encode('ascii')

        sock.sendto(response_data, address)
    
if __name__ == '_main_':
    parser = argparse.ArgumentParser(description='Server UDP lokal')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args
    server(args.p)