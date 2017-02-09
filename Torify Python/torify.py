import socks
import socket

TOR_HOST = "127.0.0.1"
TOR_PORT = "9050"

def create_connection(address, timeout=None, source_address=None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, TOR_HOST , TOR_PORT)

socket.socket = socks.socksocket
socket.create_connection = create_connection

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo = getaddrinfo

