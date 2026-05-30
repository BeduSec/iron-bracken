import unittest
from iron_bracken.frond import FrondService

class TestFrond(unittest.TestCase):
    def test_start(self):
        f = FrondService("ntp")
        port = f.start()
        self.assertEqual(port, 123)

if __name__ == "__main__":
    unittest.main()
