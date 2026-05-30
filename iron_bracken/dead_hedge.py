import subprocess
from .topology import NetworkTopology

class DeadHedge:
    def __init__(self, credentials=None):
        self.credentials = credentials or {}
        self.topology = NetworkTopology()

    def move_laterally(self, target):
        if self.topology.is_accessible(target):
            cmd = f"ssh {target} 'echo pwned'"
            subprocess.run(cmd, shell=True)
            return True
        return False

    def harvest_credentials(self, source):
        return {"user": "admin", "pass": "1234"}