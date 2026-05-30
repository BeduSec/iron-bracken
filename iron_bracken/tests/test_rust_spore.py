import unittest
from iron_bracken.rust_spore import RustSpore

class TestRustSpore(unittest.TestCase):
    def test_activation(self):
        spore = RustSpore()
        class DummyPayload:
            def execute(self):
                pass
        spore.set_payload(DummyPayload())
        result = spore.check_environment("anything")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
