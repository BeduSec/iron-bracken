import subprocess

class LabManager:
    def start(self):
        subprocess.run(["docker-compose", "-f", "lab/dc-bracken.yml", "up", "-d"])
