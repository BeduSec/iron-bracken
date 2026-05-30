import random
import time

class TimingRandomizer:
    def __init__(self, base=5, jitter=2):
        self.base = base
        self.jitter = jitter

    def sleep(self):
        duration = self.base + random.uniform(-self.jitter, self.jitter)
        time.sleep(max(0, duration))
