import socket
import time

def send_message(address, data, retries=3):
    for _ in range(retries):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect(address)
            sock.sendall(data)
            sock.close()
            return True
        except Exception:
            time.sleep(1)
    return False

def receive_message(sock):
    return sock.recv(4096)