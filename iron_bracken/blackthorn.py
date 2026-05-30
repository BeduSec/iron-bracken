from .rhizome import RhizomeNode

class Blackthorn:
    def __init__(self, node):
        self.node = node

    def detect_tamper(self):
        return False

    def regenerate(self, implant_data):
        self.node.process(implant_data)
        return True