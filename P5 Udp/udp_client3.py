import argparse
import socket
import time

MAX_BYTES = 65535

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'Requesting current time'
    data = text.encode('ascii')

    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    
    try:
        data, address = sock.recvfrom(MAX_BYTES) # Danger !
        response_text = data.decode('ascii')
        print('The server {} replied {!r}'.format(address, text))
    except Exception as e:
        print(f"Error receiving data: {e}")
    finally:
        sock.close
        
if __name__ == '_main_':
    parser = argparse.ArgumentParser(description='Client UDP lokal')
    parser.add_argument('-p',metavar='PORT', type=int, default=1060,
                        help ='UDP port (default 1060)')
    args = parser.parse_args()
    client(args.p)