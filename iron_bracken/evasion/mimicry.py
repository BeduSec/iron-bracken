class MimicryEngine:
    def __init__(self, template):
        self.template = template

    def disguise(self, payload):
        return self.template.replace(b'{{PAYLOAD}}', payload)
