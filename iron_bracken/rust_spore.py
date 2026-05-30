import hashlib
from .config import get_setting

class RustSpore:
    def __init__(self, trigger_hash=None):
        self.trigger_hash = trigger_hash or hashlib.sha256(b"default_trigger").hexdigest()
        self.payload = None

    def set_payload(self, payload):
        self.payload = payload

    def check_environment(self, env_data):
        env_hash = hashlib.sha256(env_data.encode()).hexdigest()
        if env_hash == self.trigger_hash:
            self.activate()
            return True
        return False

    def activate(self):
        if self.payload:
            self.payload.execute()