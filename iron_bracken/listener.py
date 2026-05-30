import threading
from .communicator import receive_message

class Listener:
    def __init__(self, host='0.0.0.0', port=443):
        self.host = host
        self.port = port
        self.active = False

    def start(self):
        self.active = True
        self.thread = threading.Thread(target=self._listen)
        self.thread.start()

    def _listen(self):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        while self.active:
            conn, _ = sock.accept()
            data = receive_message(conn)
            print(f"Listener received: {len(data)} bytes")