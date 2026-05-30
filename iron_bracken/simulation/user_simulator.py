import random
import time

class UserSimulator:
    def __init__(self, actions):
        self.actions = actions

    def run(self):
        for action in self.actions:
            print(f"Simulating: {action}")
            time.sleep(random.uniform(0.1, 0.5))
