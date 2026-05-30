from .base import BasePayload

class LinuxPayload(BasePayload):
    def execute(self):
        import os
        os.system("echo 'Iron Bracken Linux' > /dev/null")
