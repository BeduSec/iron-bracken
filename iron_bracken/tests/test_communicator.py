import unittest
from iron_bracken.communicator import send_message

class TestCommunicator(unittest.TestCase):
    def test_send_failure(self):
        result = send_message(("127.0.0.1", 12345), b"data", retries=1)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
