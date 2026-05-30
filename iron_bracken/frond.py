import random
import time
from .utils import get_local_ip

class FrondService:
    def __init__(self, service_type="ntp"):
        self.service_type = service_type
        self.running = False

    def start(self):
        self.running = True
        self.port = self._select_port()
        return self.port

    def _select_port(self):
        if self.service_type == "ntp":
            return 123
        elif self.service_type == "smb":
            return 445
        return random.randint(1024, 65535)

    def simulate_traffic(self):
        while self.running:
            time.sleep(random.uniform(0.5, 2.0))
            print(f"Frond {self.service_type} serving request")