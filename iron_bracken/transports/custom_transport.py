class CustomTransport:
    def __init__(self, handler):
        self.handler = handler

    def send(self, data):
        self.handler(data)
