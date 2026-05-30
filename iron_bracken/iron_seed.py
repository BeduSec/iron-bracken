import platform
from .persistence.wmi_seed import WindowsWMISeed
from .persistence.systemd_seed import LinuxSystemdSeed

def plant_seed():
    if platform.system() == "Windows":
        seed = WindowsWMISeed()
    else:
        seed = LinuxSystemdSeed()
    seed.install()
    return seed
