import unittest
from iron_bracken.rhizome import RhizomeNode

class TestRhizome(unittest.TestCase):
    def test_node_creation(self):
        n = RhizomeNode()
        self.assertIsNotNone(n.node_id)

    def test_gossip(self):
        n = RhizomeNode()
        n.add_peer("peer1", ("127.0.0.1", 9999))
        result = n.gossip("test")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
