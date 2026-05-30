from .communicator import send_message
from .crypto import encrypt, decrypt
from .utils import generate_node_id

class RhizomeNode:
    def __init__(self, node_id=None):
        self.node_id = node_id or generate_node_id()
        self.peers = []

    def add_peer(self, peer_id, address):
        self.peers.append((peer_id, address))

    def gossip(self, message):
        encrypted = encrypt(message, self.node_id)
        for peer_id, addr in self.peers:
            send_message(addr, encrypted)
        return True

    def receive_gossip(self, message):
        plaintext = decrypt(message, self.node_id)
        if plaintext:
            self.process(plaintext)
        return bool(plaintext)

    def process(self, data):
        pass