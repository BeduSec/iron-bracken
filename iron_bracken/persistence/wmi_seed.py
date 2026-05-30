import subprocess

class WindowsWMISeed:
    def install(self):
        subprocess.run(["wmic", "process", "call", "create", "calc.exe"], capture_output=True)
        return True

    def remove(self):
        return True
