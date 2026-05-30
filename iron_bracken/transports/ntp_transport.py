import struct
import time
import socket

class NTPTransport:
    def __init__(self, ntp_server):
        self.ntp_server = ntp_server

    def send(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        request = b'\x1b' + 47 * b'\0'
        try:
            sock.sendto(request, (self.ntp_server, 123))
            return True
        except Exception:
            return False
        finally:
            sock.close()
