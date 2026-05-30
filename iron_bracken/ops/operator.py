from ..rhizome import RhizomeNode

class Operator:
    def __init__(self, node):
        self.node = node

    def plant_seed(self, target):
        self.node.gossip(f"seed:{target}")

    def prune(self, target):
        self.node.gossip(f"prune:{target}")
