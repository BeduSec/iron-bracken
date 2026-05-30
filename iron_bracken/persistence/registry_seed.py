import winreg

class RegistrySeed:
    def install(self, path=r"Software\Microsoft\Windows\CurrentVersion\Run", name="Bracken", command="bracken.exe"):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, command)
            winreg.CloseKey(key)
            return True
        except Exception:
            return False
