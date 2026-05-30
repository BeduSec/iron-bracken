from .windows import WindowsPayload
from .linux import LinuxPayload
from ..config import get_setting

class HybridPayload:
    def __init__(self, config):
        self.config = config
        self.payload = self._select_payload()

    def _select_payload(self):
        if get_setting('os') == 'windows':
            return WindowsPayload()
        return LinuxPayload()

    def write(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.payload.serialize())

def compile_payload(config):
    return HybridPayload(config)
