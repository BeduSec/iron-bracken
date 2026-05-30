import unittest
from iron_bracken.dead_hedge import DeadHedge

class TestDeadHedge(unittest.TestCase):
    def test_lateral_move_inaccessible(self):
        dh = DeadHedge()
        result = dh.move_laterally("192.168.1.100")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
