from .base import BasePayload

class WindowsPayload(BasePayload):
    def execute(self):
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "Iron Bracken", "Windows Payload", 0)