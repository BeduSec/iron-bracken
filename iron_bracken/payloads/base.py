class BasePayload:
    def execute(self):
        raise NotImplementedError

    def serialize(self):
        return b""