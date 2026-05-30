import unittest
from iron_bracken.crypto import generate_key, encrypt, decrypt

class TestCrypto(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = generate_key()
        msg = "secret"
        tok = encrypt(msg, key)
        self.assertEqual(decrypt(tok, key), msg)

if __name__ == "__main__":
    unittest.main()
