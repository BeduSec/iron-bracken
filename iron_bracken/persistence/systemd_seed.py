import os

class LinuxSystemdSeed:
    def install(self):
        unit = """
[Unit]
Description=Iron Bracken
[Service]
ExecStart=/usr/local/bin/bracken_daemon
[Install]
WantedBy=multi-user.target
"""
        with open("/tmp/bracken.service", "w") as f:
            f.write(unit)
        os.system("cp /tmp/bracken.service /etc/systemd/system/ && systemctl enable bracken")
        return True
