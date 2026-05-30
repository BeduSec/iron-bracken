from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode() if isinstance(data, str) else data)

def decrypt(token, key):
    f = Fernet(key)
    try:
        return f.decrypt(token).decode()
    except Exception:
        return None
